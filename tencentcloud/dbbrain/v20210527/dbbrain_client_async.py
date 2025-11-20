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
from tencentcloud.dbbrain.v20210527 import models
from typing import Dict


class DbbrainClient(AbstractClient):
    _apiVersion = '2021-05-27'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'

    async def AddUserContact(
            self,
            request: models.AddUserContactRequest,
            opts: Dict = None,
    ) -> models.AddUserContactResponse:
        """
        添加邮件接收联系人的姓名， 邮件地址，返回值为添加成功的联系人id。
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserContact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserContactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDBAutonomyAction(
            self,
            request: models.CancelDBAutonomyActionRequest,
            opts: Dict = None,
    ) -> models.CancelDBAutonomyActionResponse:
        """
        自治中心-终止自治任务（单次）
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDBAutonomyAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDBAutonomyActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDBAutonomyEvent(
            self,
            request: models.CancelDBAutonomyEventRequest,
            opts: Dict = None,
    ) -> models.CancelDBAutonomyEventResponse:
        """
        自治中心-终止自治事件
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDBAutonomyEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDBAutonomyEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelKillTask(
            self,
            request: models.CancelKillTaskRequest,
            opts: Dict = None,
    ) -> models.CancelKillTaskResponse:
        """
        终止中断会话任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelKillTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelKillTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelRedisBigKeyAnalysisTasks(
            self,
            request: models.CancelRedisBigKeyAnalysisTasksRequest,
            opts: Dict = None,
    ) -> models.CancelRedisBigKeyAnalysisTasksResponse:
        """
        自治中心-终止自治任务（单次）
        """
        
        kwargs = {}
        kwargs["action"] = "CancelRedisBigKeyAnalysisTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelRedisBigKeyAnalysisTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAuditService(
            self,
            request: models.CloseAuditServiceRequest,
            opts: Dict = None,
    ) -> models.CloseAuditServiceResponse:
        """
        不用审计日志时，关闭数据库审计
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditLogFile(
            self,
            request: models.CreateAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.CreateAuditLogFileResponse:
        """
        用于创建云数据库实例的审计日志文件，最多下载600w审计日志。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBDiagReportTask(
            self,
            request: models.CreateDBDiagReportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDBDiagReportTaskResponse:
        """
        创建健康报告，并可以选择是否发送邮件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBDiagReportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBDiagReportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBDiagReportUrl(
            self,
            request: models.CreateDBDiagReportUrlRequest,
            opts: Dict = None,
    ) -> models.CreateDBDiagReportUrlResponse:
        """
        创建健康报告的浏览地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBDiagReportUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBDiagReportUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKillTask(
            self,
            request: models.CreateKillTaskRequest,
            opts: Dict = None,
    ) -> models.CreateKillTaskResponse:
        """
        创建中断会话的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKillTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKillTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMailProfile(
            self,
            request: models.CreateMailProfileRequest,
            opts: Dict = None,
    ) -> models.CreateMailProfileResponse:
        """
        创建邮件配置。其中入参ProfileType表示所创建配置的类型，ProfileType 取值包括：dbScan_mail_configuration（数据库巡检邮件配置）、scheduler_mail_configuration（定期生成健康报告的邮件发送配置）。Region统一选择广州，和实例所属地域无关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxySessionKillTask(
            self,
            request: models.CreateProxySessionKillTaskRequest,
            opts: Dict = None,
    ) -> models.CreateProxySessionKillTaskResponse:
        """
        创建中止所有代理节点连接会话的异步任务。当前仅支持 Redis。得到的返回值为异步任务 id，可以作为参数传入接口 DescribeProxySessionKillTasks 查询kill会话任务执行状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxySessionKillTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxySessionKillTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRedisBigKeyAnalysisTask(
            self,
            request: models.CreateRedisBigKeyAnalysisTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRedisBigKeyAnalysisTaskResponse:
        """
        即时创建redis实例大key分析任务，限制正在运行的即时分析任务数量默认为5。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRedisBigKeyAnalysisTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRedisBigKeyAnalysisTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchedulerMailProfile(
            self,
            request: models.CreateSchedulerMailProfileRequest,
            opts: Dict = None,
    ) -> models.CreateSchedulerMailProfileResponse:
        """
        该接口用于创建定期生成健康报告并邮件发送的配置，将健康报告的定期生成时间作为参数传入（周一至周日），用于设置健康报告的定期生成时间，同时保存相应的定期邮件发送的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedulerMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchedulerMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityAuditLogExportTask(
            self,
            request: models.CreateSecurityAuditLogExportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityAuditLogExportTaskResponse:
        """
        创建安全审计日志导出任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityAuditLogExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityAuditLogExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSqlFilter(
            self,
            request: models.CreateSqlFilterRequest,
            opts: Dict = None,
    ) -> models.CreateSqlFilterResponse:
        """
        创建实例SQL限流任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSqlFilter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSqlFilterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserAutonomyProfile(
            self,
            request: models.CreateUserAutonomyProfileRequest,
            opts: Dict = None,
    ) -> models.CreateUserAutonomyProfileResponse:
        """
        自治中心-终止自治任务（单次）；注意：接口需要加白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserAutonomyProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserAutonomyProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditLogFile(
            self,
            request: models.DeleteAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditLogFileResponse:
        """
        用于删除云数据库实例的审计日志文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBDiagReportTasks(
            self,
            request: models.DeleteDBDiagReportTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteDBDiagReportTasksResponse:
        """
        根据任务id删除健康报告生成任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBDiagReportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBDiagReportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRedisBigKeyAnalysisTasks(
            self,
            request: models.DeleteRedisBigKeyAnalysisTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteRedisBigKeyAnalysisTasksResponse:
        """
        删除Redis实例的大key分析任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRedisBigKeyAnalysisTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRedisBigKeyAnalysisTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityAuditLogExportTasks(
            self,
            request: models.DeleteSecurityAuditLogExportTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityAuditLogExportTasksResponse:
        """
        删除安全审计日志导出任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityAuditLogExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityAuditLogExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSqlFilters(
            self,
            request: models.DeleteSqlFiltersRequest,
            opts: Dict = None,
    ) -> models.DeleteSqlFiltersResponse:
        """
        删除实例SQL限流任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSqlFilters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSqlFiltersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmTemplate(
            self,
            request: models.DescribeAlarmTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmTemplateResponse:
        """
        通知模板查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllUserContact(
            self,
            request: models.DescribeAllUserContactRequest,
            opts: Dict = None,
    ) -> models.DescribeAllUserContactResponse:
        """
        获取邮件发送中联系人的相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllUserContact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllUserContactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllUserGroup(
            self,
            request: models.DescribeAllUserGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeAllUserGroupResponse:
        """
        获取邮件发送联系组的相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        查询实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogFiles(
            self,
            request: models.DescribeAuditLogFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogFilesResponse:
        """
        用于创建云数据库实例的审计日志文件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBAutonomyAction(
            self,
            request: models.DescribeDBAutonomyActionRequest,
            opts: Dict = None,
    ) -> models.DescribeDBAutonomyActionResponse:
        """
        自治中心-查询自治事件任务详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBAutonomyAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBAutonomyActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBAutonomyActions(
            self,
            request: models.DescribeDBAutonomyActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBAutonomyActionsResponse:
        """
        自治中心-终止自治任务（单次）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBAutonomyActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBAutonomyActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBAutonomyEvents(
            self,
            request: models.DescribeDBAutonomyEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBAutonomyEventsResponse:
        """
        自治中心-终止自治任务（单次）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBAutonomyEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBAutonomyEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagEvent(
            self,
            request: models.DescribeDBDiagEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagEventResponse:
        """
        获取实例异常诊断事件的详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagEvents(
            self,
            request: models.DescribeDBDiagEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagEventsResponse:
        """
        获取指定时间段内的诊断事件列表，支持依据风险等级、实例ID等条件过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagHistory(
            self,
            request: models.DescribeDBDiagHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagHistoryResponse:
        """
        获取实例诊断事件的列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagReportContent(
            self,
            request: models.DescribeDBDiagReportContentRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagReportContentResponse:
        """
        健康报告内容。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagReportContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagReportContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBDiagReportTasks(
            self,
            request: models.DescribeDBDiagReportTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDBDiagReportTasksResponse:
        """
        查询健康报告生成任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBDiagReportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBDiagReportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBPerfTimeSeries(
            self,
            request: models.DescribeDBPerfTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBPerfTimeSeriesResponse:
        """
        根据实例ID获取指定时间段的性能趋势。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBPerfTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBPerfTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSpaceStatus(
            self,
            request: models.DescribeDBSpaceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSpaceStatusResponse:
        """
        获取指定时间段内的实例空间使用概览，包括磁盘增长量(MB)、磁盘剩余(MB)、磁盘总量(MB)及预计可用天数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSpaceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSpaceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiagDBInstances(
            self,
            request: models.DescribeDiagDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDiagDBInstancesResponse:
        """
        获取实例信息列表。Region统一选择广州。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiagDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiagDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthScore(
            self,
            request: models.DescribeHealthScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthScoreResponse:
        """
        根据实例ID获取指定时间段（30分钟）的健康得分，以及异常扣分项。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthScoreTimeSeries(
            self,
            request: models.DescribeHealthScoreTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthScoreTimeSeriesResponse:
        """
        获取指定时间段内的健康得分趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthScoreTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthScoreTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexRecommendAggregationSlowLogs(
            self,
            request: models.DescribeIndexRecommendAggregationSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexRecommendAggregationSlowLogsResponse:
        """
        查询某张表的慢查模板概览，这个接口是对用户点击对应的推荐索引后，展示慢日志用的
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexRecommendAggregationSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexRecommendAggregationSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexRecommendInfo(
            self,
            request: models.DescribeIndexRecommendInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexRecommendInfoResponse:
        """
        查询实例的索引推荐信息，包括索引统计相关信息，推荐索引列表，无效索引列表等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexRecommendInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexRecommendInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMailProfile(
            self,
            request: models.DescribeMailProfileRequest,
            opts: Dict = None,
    ) -> models.DescribeMailProfileResponse:
        """
        获取发送邮件的配置， 包括数据库巡检的邮件配置以及定期生成健康报告的邮件发送配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMailProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricTopProxies(
            self,
            request: models.DescribeMetricTopProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricTopProxiesResponse:
        """
        获取指定时间段内Redis Proxy 指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricTopProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricTopProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMongoDBProcessList(
            self,
            request: models.DescribeMongoDBProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeMongoDBProcessListResponse:
        """
        查询MongoDB实时会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMongoDBProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMongoDBProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMySqlProcessList(
            self,
            request: models.DescribeMySqlProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeMySqlProcessListResponse:
        """
        查询关系型数据库的实时线程列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMySqlProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMySqlProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNoPrimaryKeyTables(
            self,
            request: models.DescribeNoPrimaryKeyTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeNoPrimaryKeyTablesResponse:
        """
        查询实例无主键表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNoPrimaryKeyTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNoPrimaryKeyTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyProcessStatistics(
            self,
            request: models.DescribeProxyProcessStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyProcessStatisticsResponse:
        """
        获取当前实例下的单个proxy的会话统计详情信息， 返回数据为单个 proxy 的会话统计信息。【注意】该接口仅限部分环境调用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyProcessStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyProcessStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySessionKillTasks(
            self,
            request: models.DescribeProxySessionKillTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySessionKillTasksResponse:
        """
        用于查询 redis 执行 kill 会话任务后代理节点的执行结果，入参异步任务 ID 从接口 CreateProxySessionKillTask 调用成功后取得。当前 product 只支持：redis。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySessionKillTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySessionKillTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisBigKeyAnalysisTasks(
            self,
            request: models.DescribeRedisBigKeyAnalysisTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisBigKeyAnalysisTasksResponse:
        """
        查询redis大key分析任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisBigKeyAnalysisTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisBigKeyAnalysisTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisCmdPerfTimeSeries(
            self,
            request: models.DescribeRedisCmdPerfTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisCmdPerfTimeSeriesResponse:
        """
        延迟分析-命令字分析-查询命令延迟趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisCmdPerfTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisCmdPerfTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisCommandCostStatistics(
            self,
            request: models.DescribeRedisCommandCostStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisCommandCostStatisticsResponse:
        """
        延迟分析-查询命令延迟分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisCommandCostStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisCommandCostStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisCommandOverview(
            self,
            request: models.DescribeRedisCommandOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisCommandOverviewResponse:
        """
        延迟分析-查询实例访问命令统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisCommandOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisCommandOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisProcessList(
            self,
            request: models.DescribeRedisProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisProcessListResponse:
        """
        获取 Redis 实例所有 proxy 节点的实时会话详情列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisSlowLogTopSqls(
            self,
            request: models.DescribeRedisSlowLogTopSqlsRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisSlowLogTopSqlsResponse:
        """
        统计排序指定时间段内的top慢sql。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisSlowLogTopSqls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisSlowLogTopSqlsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisTopBigKeys(
            self,
            request: models.DescribeRedisTopBigKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisTopBigKeysResponse:
        """
        查询redis实例大key列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisTopBigKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisTopBigKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisTopCostCommands(
            self,
            request: models.DescribeRedisTopCostCommandsRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisTopCostCommandsResponse:
        """
        获取指定时间段内Redis 访问命令 cost top N
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisTopCostCommands"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisTopCostCommandsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisTopHotKeys(
            self,
            request: models.DescribeRedisTopHotKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisTopHotKeysResponse:
        """
        热Key分析
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisTopHotKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisTopHotKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisTopKeyPrefixList(
            self,
            request: models.DescribeRedisTopKeyPrefixListRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisTopKeyPrefixListResponse:
        """
        查询redis实例top key前缀列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisTopKeyPrefixList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisTopKeyPrefixListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAuditLogDownloadUrls(
            self,
            request: models.DescribeSecurityAuditLogDownloadUrlsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAuditLogDownloadUrlsResponse:
        """
        查询安全审计日志导出文件下载链接。目前日志文件下载仅提供腾讯云内网地址，请通过广州地域的腾讯云服务器进行下载。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAuditLogDownloadUrls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAuditLogDownloadUrlsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAuditLogExportTasks(
            self,
            request: models.DescribeSecurityAuditLogExportTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAuditLogExportTasksResponse:
        """
        查询安全审计日志导出任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAuditLogExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAuditLogExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogQueryTimeStats(
            self,
            request: models.DescribeSlowLogQueryTimeStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogQueryTimeStatsResponse:
        """
        统计排序指定时间段内的top慢sql。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogQueryTimeStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogQueryTimeStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogTimeSeriesStats(
            self,
            request: models.DescribeSlowLogTimeSeriesStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogTimeSeriesStatsResponse:
        """
        获取慢日志统计柱状图。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogTimeSeriesStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogTimeSeriesStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogTopSqls(
            self,
            request: models.DescribeSlowLogTopSqlsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogTopSqlsResponse:
        """
        按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogTopSqls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogTopSqlsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogUserHostStats(
            self,
            request: models.DescribeSlowLogUserHostStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogUserHostStatsResponse:
        """
        获取慢日志来源地址统计分布图。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogUserHostStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogUserHostStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        获取指定时间内某个sql模板的慢日志明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSqlFilters(
            self,
            request: models.DescribeSqlFiltersRequest,
            opts: Dict = None,
    ) -> models.DescribeSqlFiltersResponse:
        """
        查询实例SQL限流任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSqlFilters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSqlFiltersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSqlTemplate(
            self,
            request: models.DescribeSqlTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeSqlTemplateResponse:
        """
        查询SQL模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSqlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSqlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceSchemaTimeSeries(
            self,
            request: models.DescribeTopSpaceSchemaTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceSchemaTimeSeriesResponse:
        """
        获取实例占用空间最大的前几个库在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceSchemaTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceSchemaTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceSchemas(
            self,
            request: models.DescribeTopSpaceSchemasRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceSchemasResponse:
        """
        获取实例Top库的实时空间统计信息，默认返回按大小排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceSchemas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceSchemasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceTableTimeSeries(
            self,
            request: models.DescribeTopSpaceTableTimeSeriesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceTableTimeSeriesResponse:
        """
        获取实例占用空间最大的前几张表在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceTableTimeSeries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceTableTimeSeriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopSpaceTables(
            self,
            request: models.DescribeTopSpaceTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopSpaceTablesResponse:
        """
        获取实例Top表的实时空间统计信息，默认返回按大小排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopSpaceTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopSpaceTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserAutonomyProfile(
            self,
            request: models.DescribeUserAutonomyProfileRequest,
            opts: Dict = None,
    ) -> models.DescribeUserAutonomyProfileResponse:
        """
        自治中心-终止自治任务（单次）；注意： 接口调用需要加白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserAutonomyProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserAutonomyProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSqlAdvice(
            self,
            request: models.DescribeUserSqlAdviceRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSqlAdviceResponse:
        """
        获取SQL优化建议。【产品用户回馈，此接口限免开放，后续将并入dbbrain专业版】
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSqlAdvice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSqlAdviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillMySqlThreads(
            self,
            request: models.KillMySqlThreadsRequest,
            opts: Dict = None,
    ) -> models.KillMySqlThreadsResponse:
        """
        根据会话ID中断当前会话，该接口分为两次提交：第一次为预提交阶段，Stage为"Prepare"，得到的返回值包含SqlExecId；第二次为确认提交， Stage为"Commit"， 将SqlExecId的值作为参数传入，最终终止会话进程。
        """
        
        kwargs = {}
        kwargs["action"] = "KillMySqlThreads"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillMySqlThreadsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicy(
            self,
            request: models.ModifyAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyResponse:
        """
        修改告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditService(
            self,
            request: models.ModifyAuditServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditServiceResponse:
        """
        修改审计配置相关信息，如高频存储时长等
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiagDBInstanceConf(
            self,
            request: models.ModifyDiagDBInstanceConfRequest,
            opts: Dict = None,
    ) -> models.ModifyDiagDBInstanceConfResponse:
        """
        修改实例的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiagDBInstanceConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiagDBInstanceConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySqlFilters(
            self,
            request: models.ModifySqlFiltersRequest,
            opts: Dict = None,
    ) -> models.ModifySqlFiltersResponse:
        """
        更改实例限流任务状态，目前仅用于终止限流。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySqlFilters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySqlFiltersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserAutonomyProfile(
            self,
            request: models.ModifyUserAutonomyProfileRequest,
            opts: Dict = None,
    ) -> models.ModifyUserAutonomyProfileResponse:
        """
        自治中心-终止自治任务（单次）；注意：接口需要加白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserAutonomyProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserAutonomyProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        开启数据库审计服务
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAgentSwitch(
            self,
            request: models.UpdateAgentSwitchRequest,
            opts: Dict = None,
    ) -> models.UpdateAgentSwitchResponse:
        """
        更新agent状态（停止或重连Agent）
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAgentSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAgentSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateMonitorSwitch(
            self,
            request: models.UpdateMonitorSwitchRequest,
            opts: Dict = None,
    ) -> models.UpdateMonitorSwitchResponse:
        """
        更新Agent实例状态（停止或重连实例）
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateMonitorSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateMonitorSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyUserAccount(
            self,
            request: models.VerifyUserAccountRequest,
            opts: Dict = None,
    ) -> models.VerifyUserAccountResponse:
        """
        验证用户数据库账号权限，获取会话token。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyUserAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyUserAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)