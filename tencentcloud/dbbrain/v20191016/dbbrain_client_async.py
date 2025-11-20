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
from tencentcloud.dbbrain.v20191016 import models
from typing import Dict


class DbbrainClient(AbstractClient):
    _apiVersion = '2019-10-16'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'

    async def AddUserContact(
            self,
            request: models.AddUserContactRequest,
            opts: Dict = None,
    ) -> models.AddUserContactResponse:
        """
        添加邮件接收联系人的姓名， 邮件地址，返回值为添加成功的联系人id。Region统一选择广州。
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserContact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserContactResponse
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
        
    async def DescribeMailProfile(
            self,
            request: models.DescribeMailProfileRequest,
            opts: Dict = None,
    ) -> models.DescribeMailProfileResponse:
        """
        获取发送邮件的配置， 包括数据库巡检的邮件配置以及定期生成健康报告的邮件发送配置。Region统一选择广州。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMailProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMailProfileResponse
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
        
    async def DescribeUserSqlAdvice(
            self,
            request: models.DescribeUserSqlAdviceRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSqlAdviceResponse:
        """
        获取SQL优化建议。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSqlAdvice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSqlAdviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiagDBInstanceConf(
            self,
            request: models.ModifyDiagDBInstanceConfRequest,
            opts: Dict = None,
    ) -> models.ModifyDiagDBInstanceConfResponse:
        """
        修改实例巡检开关。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiagDBInstanceConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiagDBInstanceConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)