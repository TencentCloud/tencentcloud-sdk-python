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
from tencentcloud.dbbrain.v20210527 import models


class DbbrainClient(AbstractClient):
    _apiVersion = '2021-05-27'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'


    def AddUserContact(self, request):
        """添加邮件接收联系人的姓名， 邮件地址，返回值为添加成功的联系人id。

        :param request: Request instance for AddUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.AddUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.AddUserContactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserContact", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserContactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelKillTask(self, request):
        """终止中断会话任务。

        :param request: Request instance for CancelKillTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CancelKillTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CancelKillTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelKillTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelKillTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAuditService(self, request):
        """不用审计日志时，关闭数据库审计

        :param request: Request instance for CloseAuditService.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CloseAuditServiceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CloseAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditLogFile(self, request):
        """用于创建云数据库实例的审计日志文件，最多下载600w审计日志。

        :param request: Request instance for CreateAuditLogFile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateAuditLogFileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBDiagReportTask(self, request):
        """创建健康报告，并可以选择是否发送邮件。

        :param request: Request instance for CreateDBDiagReportTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBDiagReportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBDiagReportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBDiagReportUrl(self, request):
        """创建健康报告的浏览地址。

        :param request: Request instance for CreateDBDiagReportUrl.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportUrlRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBDiagReportUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBDiagReportUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKillTask(self, request):
        """创建中断会话的任务。

        :param request: Request instance for CreateKillTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateKillTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateKillTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKillTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKillTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMailProfile(self, request):
        """创建邮件配置。其中入参ProfileType表示所创建配置的类型，ProfileType 取值包括：dbScan_mail_configuration（数据库巡检邮件配置）、scheduler_mail_configuration（定期生成健康报告的邮件发送配置）。Region统一选择广州，和实例所属地域无关。

        :param request: Request instance for CreateMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateMailProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMailProfile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMailProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxySessionKillTask(self, request):
        """创建中止所有代理节点连接会话的异步任务。当前仅支持 Redis。得到的返回值为异步任务 id，可以作为参数传入接口 DescribeProxySessionKillTasks 查询kill会话任务执行状态。

        :param request: Request instance for CreateProxySessionKillTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateProxySessionKillTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateProxySessionKillTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxySessionKillTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxySessionKillTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRedisBigKeyAnalysisTask(self, request):
        """即时创建redis实例大key分析任务，限制正在运行的即时分析任务数量默认为5。

        :param request: Request instance for CreateRedisBigKeyAnalysisTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateRedisBigKeyAnalysisTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateRedisBigKeyAnalysisTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRedisBigKeyAnalysisTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRedisBigKeyAnalysisTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSchedulerMailProfile(self, request):
        """该接口用于创建定期生成健康报告并邮件发送的配置，将健康报告的定期生成时间作为参数传入（周一至周日），用于设置健康报告的定期生成时间，同时保存相应的定期邮件发送的配置。

        :param request: Request instance for CreateSchedulerMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateSchedulerMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateSchedulerMailProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSchedulerMailProfile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSchedulerMailProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityAuditLogExportTask(self, request):
        """创建安全审计日志导出任务。

        :param request: Request instance for CreateSecurityAuditLogExportTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateSecurityAuditLogExportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateSecurityAuditLogExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityAuditLogExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityAuditLogExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSqlFilter(self, request):
        """创建实例SQL限流任务。

        :param request: Request instance for CreateSqlFilter.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateSqlFilterRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateSqlFilterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSqlFilter", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSqlFilterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditLogFile(self, request):
        """用于删除云数据库实例的审计日志文件。

        :param request: Request instance for DeleteAuditLogFile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteAuditLogFileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBDiagReportTasks(self, request):
        """根据任务id删除健康报告生成任务

        :param request: Request instance for DeleteDBDiagReportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteDBDiagReportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteDBDiagReportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBDiagReportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBDiagReportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRedisBigKeyAnalysisTasks(self, request):
        """删除Redis实例的大key分析任务。

        :param request: Request instance for DeleteRedisBigKeyAnalysisTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteRedisBigKeyAnalysisTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteRedisBigKeyAnalysisTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRedisBigKeyAnalysisTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRedisBigKeyAnalysisTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityAuditLogExportTasks(self, request):
        """删除安全审计日志导出任务。

        :param request: Request instance for DeleteSecurityAuditLogExportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteSecurityAuditLogExportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteSecurityAuditLogExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityAuditLogExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityAuditLogExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSqlFilters(self, request):
        """删除实例SQL限流任务。

        :param request: Request instance for DeleteSqlFilters.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteSqlFiltersRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteSqlFiltersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSqlFilters", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSqlFiltersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmTemplate(self, request):
        """通知模板查询

        :param request: Request instance for DescribeAlarmTemplate.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAlarmTemplateRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAlarmTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllUserContact(self, request):
        """获取邮件发送中联系人的相关信息。

        :param request: Request instance for DescribeAllUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserContactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllUserContact", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllUserContactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllUserGroup(self, request):
        """获取邮件发送联系组的相关信息。

        :param request: Request instance for DescribeAllUserGroup.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserGroupRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditInstanceList(self, request):
        """查询实例列表

        :param request: Request instance for DescribeAuditInstanceList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAuditInstanceListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAuditInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLogFiles(self, request):
        """用于创建云数据库实例的审计日志文件

        :param request: Request instance for DescribeAuditLogFiles.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAuditLogFilesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAuditLogFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLogFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagEvent(self, request):
        """获取实例异常诊断事件的详情信息。

        :param request: Request instance for DescribeDBDiagEvent.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagEvents(self, request):
        """获取指定时间段内的诊断事件列表，支持依据风险等级、实例ID等条件过滤。

        :param request: Request instance for DescribeDBDiagEvents.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagHistory(self, request):
        """获取实例诊断事件的列表。

        :param request: Request instance for DescribeDBDiagHistory.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagHistoryRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagReportTasks(self, request):
        """查询健康报告生成任务列表。

        :param request: Request instance for DescribeDBDiagReportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagReportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagReportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagReportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagReportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSpaceStatus(self, request):
        """获取指定时间段内的实例空间使用概览，包括磁盘增长量(MB)、磁盘剩余(MB)、磁盘总量(MB)及预计可用天数。

        :param request: Request instance for DescribeDBSpaceStatus.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBSpaceStatusRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBSpaceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSpaceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSpaceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiagDBInstances(self, request):
        """获取实例信息列表。Region统一选择广州。

        :param request: Request instance for DescribeDiagDBInstances.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDiagDBInstancesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDiagDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiagDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiagDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthScore(self, request):
        """根据实例ID获取指定时间段（30分钟）的健康得分，以及异常扣分项。

        :param request: Request instance for DescribeHealthScore.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeHealthScoreRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeHealthScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexRecommendAggregationSlowLogs(self, request):
        """查询某张表的慢查模板概览

        :param request: Request instance for DescribeIndexRecommendAggregationSlowLogs.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeIndexRecommendAggregationSlowLogsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeIndexRecommendAggregationSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexRecommendAggregationSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexRecommendAggregationSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexRecommendInfo(self, request):
        """查询实例的索引推荐信息，包括索引统计相关信息，推荐索引列表，无效索引列表等。

        :param request: Request instance for DescribeIndexRecommendInfo.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeIndexRecommendInfoRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeIndexRecommendInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexRecommendInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexRecommendInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMailProfile(self, request):
        """获取发送邮件的配置， 包括数据库巡检的邮件配置以及定期生成健康报告的邮件发送配置。

        :param request: Request instance for DescribeMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMailProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMailProfile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMailProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySqlProcessList(self, request):
        """查询关系型数据库的实时线程列表。

        :param request: Request instance for DescribeMySqlProcessList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMySqlProcessListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMySqlProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMySqlProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMySqlProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNoPrimaryKeyTables(self, request):
        """查询实例无主键表。

        :param request: Request instance for DescribeNoPrimaryKeyTables.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeNoPrimaryKeyTablesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeNoPrimaryKeyTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNoPrimaryKeyTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNoPrimaryKeyTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyProcessStatistics(self, request):
        """获取当前实例下的单个proxy的会话统计详情信息， 返回数据为单个 proxy 的会话统计信息。【注意】该接口仅限部分环境调用。

        :param request: Request instance for DescribeProxyProcessStatistics.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxyProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxyProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySessionKillTasks(self, request):
        """用于查询 redis 执行 kill 会话任务后代理节点的执行结果，入参异步任务 ID 从接口 CreateProxySessionKillTask 调用成功后取得。当前 product 只支持：redis。

        :param request: Request instance for DescribeProxySessionKillTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxySessionKillTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxySessionKillTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySessionKillTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySessionKillTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisBigKeyAnalysisTasks(self, request):
        """查询redis大key分析任务列表。

        :param request: Request instance for DescribeRedisBigKeyAnalysisTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisBigKeyAnalysisTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisBigKeyAnalysisTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisBigKeyAnalysisTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisBigKeyAnalysisTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisProcessList(self, request):
        """获取 Redis 实例所有 proxy 节点的实时会话详情列表。

        :param request: Request instance for DescribeRedisProcessList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisProcessListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisTopBigKeys(self, request):
        """查询redis实例大key列表。

        :param request: Request instance for DescribeRedisTopBigKeys.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopBigKeysRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopBigKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisTopBigKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisTopBigKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisTopKeyPrefixList(self, request):
        """查询redis实例top key前缀列表。

        :param request: Request instance for DescribeRedisTopKeyPrefixList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopKeyPrefixListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopKeyPrefixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisTopKeyPrefixList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisTopKeyPrefixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAuditLogDownloadUrls(self, request):
        """查询安全审计日志导出文件下载链接。目前日志文件下载仅提供腾讯云内网地址，请通过广州地域的腾讯云服务器进行下载。

        :param request: Request instance for DescribeSecurityAuditLogDownloadUrls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogDownloadUrlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogDownloadUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAuditLogDownloadUrls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAuditLogDownloadUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAuditLogExportTasks(self, request):
        """查询安全审计日志导出任务列表。

        :param request: Request instance for DescribeSecurityAuditLogExportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogExportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAuditLogExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAuditLogExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogTimeSeriesStats(self, request):
        """获取慢日志统计柱状图。

        :param request: Request instance for DescribeSlowLogTimeSeriesStats.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTimeSeriesStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTimeSeriesStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogTimeSeriesStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogTimeSeriesStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogTopSqls(self, request):
        """按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。

        :param request: Request instance for DescribeSlowLogTopSqls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogTopSqls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogTopSqlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogUserHostStats(self, request):
        """获取慢日志来源地址统计分布图。

        :param request: Request instance for DescribeSlowLogUserHostStats.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogUserHostStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogUserHostStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogUserHostStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogUserHostStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogs(self, request):
        """获取指定时间内某个sql模板的慢日志明细

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSqlFilters(self, request):
        """查询实例SQL限流任务列表。

        :param request: Request instance for DescribeSqlFilters.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSqlFiltersRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSqlFiltersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSqlFilters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSqlFiltersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSqlTemplate(self, request):
        """查询SQL模板。

        :param request: Request instance for DescribeSqlTemplate.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSqlTemplateRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSqlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSqlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSqlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceSchemaTimeSeries(self, request):
        """获取实例占用空间最大的前几个库在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。

        :param request: Request instance for DescribeTopSpaceSchemaTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemaTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemaTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceSchemaTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceSchemaTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceSchemas(self, request):
        """获取实例Top库的实时空间统计信息，默认返回按大小排序。

        :param request: Request instance for DescribeTopSpaceSchemas.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemasRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceSchemas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceSchemasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceTableTimeSeries(self, request):
        """获取实例占用空间最大的前几张表在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。

        :param request: Request instance for DescribeTopSpaceTableTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTableTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTableTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceTableTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceTableTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceTables(self, request):
        """获取实例Top表的实时空间统计信息，默认返回按大小排序。

        :param request: Request instance for DescribeTopSpaceTables.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTablesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserSqlAdvice(self, request):
        """获取SQL优化建议。【产品用户回馈，此接口限免开放，后续将并入dbbrain专业版】

        :param request: Request instance for DescribeUserSqlAdvice.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeUserSqlAdviceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeUserSqlAdviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserSqlAdvice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserSqlAdviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillMySqlThreads(self, request):
        """根据会话ID中断当前会话，该接口分为两次提交：第一次为预提交阶段，Stage为"Prepare"，得到的返回值包含SqlExecId；第二次为确认提交， Stage为"Commit"， 将SqlExecId的值作为参数传入，最终终止会话进程。

        :param request: Request instance for KillMySqlThreads.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.KillMySqlThreadsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.KillMySqlThreadsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillMySqlThreads", params, headers=headers)
            response = json.loads(body)
            model = models.KillMySqlThreadsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmPolicy(self, request):
        """修改告警策略

        :param request: Request instance for ModifyAlarmPolicy.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditService(self, request):
        """修改审计配置相关信息，如高频存储时长等

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiagDBInstanceConf(self, request):
        """修改实例的配置信息。

        :param request: Request instance for ModifyDiagDBInstanceConf.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyDiagDBInstanceConfRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyDiagDBInstanceConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiagDBInstanceConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiagDBInstanceConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySqlFilters(self, request):
        """更改实例限流任务状态，目前仅用于终止限流。

        :param request: Request instance for ModifySqlFilters.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifySqlFiltersRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifySqlFiltersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySqlFilters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySqlFiltersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        """开启数据库审计服务

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.OpenAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAgentSwitch(self, request):
        """更新agent状态（停止或重连Agent）

        :param request: Request instance for UpdateAgentSwitch.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.UpdateAgentSwitchRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.UpdateAgentSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAgentSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAgentSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMonitorSwitch(self, request):
        """更新Agent实例状态（停止或重连实例）

        :param request: Request instance for UpdateMonitorSwitch.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.UpdateMonitorSwitchRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.UpdateMonitorSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateMonitorSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateMonitorSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyUserAccount(self, request):
        """验证用户数据库账号权限，获取会话token。

        :param request: Request instance for VerifyUserAccount.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.VerifyUserAccountRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.VerifyUserAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyUserAccount", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyUserAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))