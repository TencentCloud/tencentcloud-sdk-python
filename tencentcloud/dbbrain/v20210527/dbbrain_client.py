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
from tencentcloud.dbbrain.v20210527 import models


class DbbrainClient(AbstractClient):
    _apiVersion = '2021-05-27'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'


    def AddUserContact(self, request):
        r"""添加邮件接收联系人的姓名， 邮件地址，返回值为添加成功的联系人id。

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


    def CancelDBAutonomyAction(self, request):
        r"""自治中心-终止自治任务（单次）

        :param request: Request instance for CancelDBAutonomyAction.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CancelDBAutonomyActionRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CancelDBAutonomyActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDBAutonomyAction", params, headers=headers)
            response = json.loads(body)
            model = models.CancelDBAutonomyActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelDBAutonomyEvent(self, request):
        r"""自治中心-终止自治事件

        :param request: Request instance for CancelDBAutonomyEvent.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CancelDBAutonomyEventRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CancelDBAutonomyEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDBAutonomyEvent", params, headers=headers)
            response = json.loads(body)
            model = models.CancelDBAutonomyEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelKillTask(self, request):
        r"""终止中断会话任务。

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


    def CancelRedisBigKeyAnalysisTasks(self, request):
        r"""自治中心-终止自治任务（单次）

        :param request: Request instance for CancelRedisBigKeyAnalysisTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CancelRedisBigKeyAnalysisTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CancelRedisBigKeyAnalysisTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelRedisBigKeyAnalysisTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CancelRedisBigKeyAnalysisTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAuditService(self, request):
        r"""不用审计日志时，关闭数据库审计

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
        r"""用于创建云数据库实例的审计日志文件，最多下载600w审计日志。

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
        r"""创建健康报告，并可以选择是否发送邮件。

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
        r"""创建健康报告的浏览地址。

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


    def CreateDBDiagReportUrls(self, request):
        r"""批量创建健康报告的PDF下载链接，支持一次获取多个报告的下载地址。

        :param request: Request instance for CreateDBDiagReportUrls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportUrlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBDiagReportUrls", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBDiagReportUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIgnoreDiagRecord(self, request):
        r"""对实例的某个诊断项设置忽略或取消忽略状态。

        :param request: Request instance for CreateIgnoreDiagRecord.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateIgnoreDiagRecordRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateIgnoreDiagRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIgnoreDiagRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIgnoreDiagRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKillTask(self, request):
        r"""创建中断会话的任务。

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
        r"""创建邮件配置。其中入参ProfileType表示所创建配置的类型，ProfileType 取值包括：dbScan_mail_configuration（数据库巡检邮件配置）、scheduler_mail_configuration（定期生成健康报告的邮件发送配置）。Region统一选择广州，和实例所属地域无关。

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


    def CreateMongoDBKillTask(self, request):
        r"""创建中断会话的任务。

        :param request: Request instance for CreateMongoDBKillTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateMongoDBKillTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateMongoDBKillTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMongoDBKillTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMongoDBKillTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxySessionKillTask(self, request):
        r"""创建中止所有代理节点连接会话的异步任务。当前仅支持 Redis。得到的返回值为异步任务 id，可以作为参数传入接口 DescribeProxySessionKillTasks 查询kill会话任务执行状态。

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
        r"""即时创建redis实例大key分析任务，限制正在运行的即时分析任务数量默认为5。

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
        r"""该接口用于创建定期生成健康报告并邮件发送的配置，将健康报告的定期生成时间作为参数传入（周一至周日），用于设置健康报告的定期生成时间，同时保存相应的定期邮件发送的配置。

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
        r"""创建安全审计日志导出任务。

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
        r"""创建实例SQL限流任务。

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


    def CreateUserAutonomyProfile(self, request):
        r"""自治中心-终止自治任务（单次）；注意：接口需要加白名单。

        :param request: Request instance for CreateUserAutonomyProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateUserAutonomyProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateUserAutonomyProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserAutonomyProfile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserAutonomyProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditLogFile(self, request):
        r"""用于删除云数据库实例的审计日志文件。

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
        r"""根据任务id删除健康报告生成任务

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
        r"""删除Redis实例的大key分析任务。

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
        r"""删除安全审计日志导出任务。

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
        r"""删除实例SQL限流任务。

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
        r"""通知模板查询

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
        r"""获取邮件发送中联系人的相关信息。

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
        r"""获取邮件发送联系组的相关信息。

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
        r"""查询实例列表

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
        r"""用于创建云数据库实例的审计日志文件

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


    def DescribeBlockingLockTree(self, request):
        r"""根据指定快照 token 查询该快照时刻的完整阻塞树（多层嵌套，根节点为头 blocker，支持多叉/多层展开）。支持两种定位方式，任选其一：(1) 优先 MonitorLoop（精确，lock monitor 一次扫描快照的唯一标识），可从 DescribeBlockingTimeRange / DescribeBlockingLogs / DescribeBlockingTrend 返回获取；(2) 兑底 BlockingTime（近似，任意阻塞时间点），后端会在该时间点±1分钟范围内找到最接近的 MonitorLoop 再下钻其阻塞树。当 MonitorLoop 不为空时优先采用；为空时回退使用 BlockingTime；两者都为空则返回参数错误。一个 MonitorLoop 可包含多棵独立阻塞树（若该快照内存在多组互不相干的阻塞链路）。对标 dbaas-pfs 的 DescribeLockTree。

        :param request: Request instance for DescribeBlockingLockTree.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeBlockingLockTreeRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeBlockingLockTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockingLockTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockingLockTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockingLogs(self, request):
        r"""查询指定实例在时间窗口内的阻塞日志扁平明细列表，不建阻塞树。每一条Item对应一次blocked_process_report（一条blocker→blocked边）在某一次monitorLoop内被lock monitor捕获的瞬时数据。支持按ReportTime / DurationMs / BlockedWaitTimeMs / BlockingWaitTimeMs升降序排序，并支持根因、数据库名、头SQL / 被阻塞SQL MD5、会话ID、登录名、客户端主机 / 应用、被阻塞锁模式、等待时长范围过滤与分页。适合普通表格展示与二次过滤；若需查看某个采集点的完整链路拓扑，请透传返回的MonitorLoop调用DescribeBlockingLockTree。注意：同一blocker→blocked会话对跨monitorLoop连续采集场景下会产生多条明细行，若需统计发生多少次阻塞请按(BlockingSessionId, BlockedSessionId, BlockedWaitResource)自行去重。时间字段按服务端时区UTC+8解析，建议单次查询跨度≤7天。

        :param request: Request instance for DescribeBlockingLogs.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeBlockingLogsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeBlockingLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockingLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockingLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockingTrend(self, request):
        r"""查询指定实例在时间窗口内按时间粒度聚合的阻塞计数时序，用于前端绘制阻塞趋势图。返回每个粒度 bucket 的 (StartTime, EndTime, LockCount, MonitorLoopCount)，实际聚合区间为前闭后开 [StartTime, EndTime)。为稠密时序：时间窗口内每个粒度 bucket 都返回一个点，无数据的 bucket 补零（LockCount=0, MonitorLoopCount=0），前端可直接绘制连续趋势图。粒度自动按时间跨度 deltaMs = EndTime - StartTime 决定（右开上界判定）：deltaMs≤5min→SECONDS(1s)，deltaMs≤1h→MINUTES(1min)，deltaMs≤3h→FIVE_MINUTES(5min)，deltaMs≤6h→TEN_MINUTES(10min)，deltaMs≤12h→FIFTEEN_MINUTES(15min)，deltaMs≤24h→THIRTY_MINUTES(30min)，deltaMs>24h→HOUR(1h)。底层走 Druid timeseries 原生聚合，服务端完成聚合，适合高频前端刷新。

        :param request: Request instance for DescribeBlockingTrend.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeBlockingTrendRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeBlockingTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockingTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockingTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBAuditLogTopSqls(self, request):
        r"""按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。

        :param request: Request instance for DescribeDBAuditLogTopSqls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAuditLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAuditLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBAuditLogTopSqls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBAuditLogTopSqlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBAuditLogs(self, request):
        r"""查询指定实例在时间窗口内的审计日志明细，支持按 SQL 类型、执行耗时、错误码、关键词等多条件过滤。当前仅支持 dcdb、mariadb 产品（cdb、cynosdb 已切至中台）。注意 Filter.MultiSql 与 Filter.ExcludeMultiSql 需以 JSON 字符串形式传递二维数组内容，例如 [["a","b"]] 表示 (a OR b)，服务端会自动解析。

        :param request: Request instance for DescribeDBAuditLogs.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAuditLogsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAuditLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBAuditLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBAuditLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBAutonomyAction(self, request):
        r"""自治中心-查询自治事件任务详情。

        :param request: Request instance for DescribeDBAutonomyAction.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAutonomyActionRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAutonomyActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBAutonomyAction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBAutonomyActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBAutonomyActions(self, request):
        r"""自治中心-终止自治任务（单次）

        :param request: Request instance for DescribeDBAutonomyActions.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAutonomyActionsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAutonomyActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBAutonomyActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBAutonomyActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBAutonomyEvents(self, request):
        r"""自治中心-终止自治任务（单次）

        :param request: Request instance for DescribeDBAutonomyEvents.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAutonomyEventsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBAutonomyEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBAutonomyEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBAutonomyEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagEvent(self, request):
        r"""获取实例异常诊断事件的详情信息。

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
        r"""获取指定时间段内的诊断事件列表，支持依据风险等级、实例ID等条件过滤。

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
        r"""获取实例诊断事件的列表。

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


    def DescribeDBDiagReportContent(self, request):
        r"""健康报告内容。

        :param request: Request instance for DescribeDBDiagReportContent.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagReportContentRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagReportContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagReportContent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagReportContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagReportTasks(self, request):
        r"""查询健康报告生成任务列表。

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


    def DescribeDBInstances(self, request):
        r"""根据实例ID列表查询数据库实例基本信息，支持跨产品查询（MySQL、CynosDB、MariaDB、DCDB、MongoDB、PostgreSQL、Redis、TDStore等）。不支持分页，通过InstanceIds限制查询数量（最多100条）。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBPerfTimeSeries(self, request):
        r"""根据实例ID获取指定时间段的性能趋势。

        :param request: Request instance for DescribeDBPerfTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBPerfTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBPerfTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBPerfTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBPerfTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSpaceStatus(self, request):
        r"""获取指定时间段内的实例空间使用概览，包括磁盘增长量(MB)、磁盘剩余(MB)、磁盘总量(MB)及预计可用天数。

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


    def DescribeDatabaseAutonomyStatus(self, request):
        r"""查询数据库自治功能的开关状态。当前支持 MongoDB 的索引推荐（AutoIndexAdvice）功能状态查询。

        :param request: Request instance for DescribeDatabaseAutonomyStatus.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDatabaseAutonomyStatusRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDatabaseAutonomyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAutonomyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAutonomyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseObjectV2(self, request):
        r"""查询指定 SELECT SQL 在实例上的执行计划，常用于慢 SQL 分析、SQL 优化等场景。仅支持 SELECT 类语句

        :param request: Request instance for DescribeDatabaseObjectV2.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDatabaseObjectV2Request`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDatabaseObjectV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseObjectV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseObjectV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeadLockLogs(self, request):
        r"""查询实例的死锁事件列表

        :param request: Request instance for DescribeDeadLockLogs.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDeadLockLogsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDeadLockLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeadLockLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeadLockLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiagDBInstances(self, request):
        r"""获取实例信息列表。Region统一选择广州。

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
        r"""根据实例ID获取指定时间段（30分钟）的健康得分，以及异常扣分项。

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


    def DescribeHealthScoreTimeSeries(self, request):
        r"""获取指定时间段内的健康得分趋势

        :param request: Request instance for DescribeHealthScoreTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeHealthScoreTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeHealthScoreTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthScoreTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthScoreTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexRecommendAggregationSlowLogs(self, request):
        r"""查询某张表的慢查模板概览，这个接口是对用户点击对应的推荐索引后，展示慢日志用的

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
        r"""查询实例的索引推荐信息，包括索引统计相关信息，推荐索引列表，无效索引列表等。

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
        r"""获取发送邮件的配置， 包括数据库巡检的邮件配置以及定期生成健康报告的邮件发送配置。

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


    def DescribeMetricTopProxies(self, request):
        r"""获取指定时间段内Redis Proxy 指标

        :param request: Request instance for DescribeMetricTopProxies.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMetricTopProxiesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMetricTopProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricTopProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricTopProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMongoDBProcessList(self, request):
        r"""查询MongoDB实时会话列表

        :param request: Request instance for DescribeMongoDBProcessList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMongoDBProcessListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMongoDBProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMongoDBProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMongoDBProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySqlProcessList(self, request):
        r"""查询关系型数据库的实时线程列表。

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
        r"""查询实例无主键表。

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
        r"""获取当前实例下的单个proxy的会话统计详情信息， 返回数据为单个 proxy 的会话统计信息。【注意】该接口仅限部分环境调用。

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
        r"""用于查询 redis 执行 kill 会话任务后代理节点的执行结果，入参异步任务 ID 从接口 CreateProxySessionKillTask 调用成功后取得。当前 product 只支持：redis。

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
        r"""查询redis大key分析任务列表。

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


    def DescribeRedisCmdPerfTimeSeries(self, request):
        r"""延迟分析-命令字分析-查询命令延迟趋势

        :param request: Request instance for DescribeRedisCmdPerfTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisCmdPerfTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisCmdPerfTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisCmdPerfTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisCmdPerfTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisCommandCostStatistics(self, request):
        r"""延迟分析-查询命令延迟分布

        :param request: Request instance for DescribeRedisCommandCostStatistics.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisCommandCostStatisticsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisCommandCostStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisCommandCostStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisCommandCostStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisCommandOverview(self, request):
        r"""延迟分析-查询实例访问命令统计

        :param request: Request instance for DescribeRedisCommandOverview.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisCommandOverviewRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisCommandOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisCommandOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisCommandOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisProcessList(self, request):
        r"""获取 Redis 实例所有 proxy 节点的实时会话详情列表。

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


    def DescribeRedisSlowLogTopSqls(self, request):
        r"""统计排序指定时间段内的top慢sql。

        :param request: Request instance for DescribeRedisSlowLogTopSqls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisSlowLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisSlowLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisSlowLogTopSqls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisSlowLogTopSqlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisTopBigKeys(self, request):
        r"""查询redis实例大key列表。

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


    def DescribeRedisTopCostCommands(self, request):
        r"""获取指定时间段内Redis 访问命令 cost top N

        :param request: Request instance for DescribeRedisTopCostCommands.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopCostCommandsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopCostCommandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisTopCostCommands", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisTopCostCommandsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisTopHotKeys(self, request):
        r"""热Key分析

        :param request: Request instance for DescribeRedisTopHotKeys.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopHotKeysRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopHotKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisTopHotKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisTopHotKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisTopKeyPrefixList(self, request):
        r"""查询redis实例top key前缀列表。

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


    def DescribeRedisUnExpiredKeyStatistics(self, request):
        r"""查询Redis全量Key的内存分布情况。

        :param request: Request instance for DescribeRedisUnExpiredKeyStatistics.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisUnExpiredKeyStatisticsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisUnExpiredKeyStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisUnExpiredKeyStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisUnExpiredKeyStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAuditLogDownloadUrls(self, request):
        r"""查询安全审计日志导出文件下载链接。目前日志文件下载仅提供腾讯云内网地址，请通过广州地域的腾讯云服务器进行下载。

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
        r"""查询安全审计日志导出任务列表。

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


    def DescribeSlowLogQueryTimeStats(self, request):
        r"""统计排序指定时间段内的top慢sql。

        :param request: Request instance for DescribeSlowLogQueryTimeStats.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogQueryTimeStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogQueryTimeStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogQueryTimeStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogQueryTimeStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogTimeSeriesStats(self, request):
        r"""获取慢日志统计柱状图。

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
        r"""按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。

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
        r"""获取慢日志来源地址统计分布图。

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
        r"""获取指定时间内某个sql模板的慢日志明细

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
        r"""查询实例SQL限流任务列表。

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
        r"""查询SQL模板。

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


    def DescribeTableSpaceDataV2(self, request):
        r"""表空间数据查询（融合接口，多产品统一入口）。按入参 TableSchema + TableName（PG 系额外需 TableCatalog）定位单张表/集合，返回该表的空间使用明细。支持产品：mysql（云数据库 MySQL）、cynosdb（TDSQL-C MySQL 版）、mongodb（云数据库 MongoDB）、postgres（云数据库 PostgreSQL）、sqlserver（SQL Server）、dcdb（TDSQL MySQL 版）、tdsql（TDSQL）、mariadb（云数据库 MariaDB）。返回值按产品隔离：MySQL 系列返回 MysqlTableSpaceData；PostgreSQL 返回 PostgresTableSpaceData；MongoDB 返回 MongodbTableSpaceData（含集合明细列表 SpaceSchemas 和外层 Timestamp）；SQL Server 返回 SqlServerTableSpaceData。注意：只读实例（CDB RO / RO 组 / CynosDB RO / TDSQL-C 集群 RO）不支持空间分析，调用将直接报错。

        :param request: Request instance for DescribeTableSpaceDataV2.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTableSpaceDataV2Request`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTableSpaceDataV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableSpaceDataV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableSpaceDataV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceSchemaTimeSeries(self, request):
        r"""获取实例占用空间最大的前几个库在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。

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
        r"""获取实例Top库的实时空间统计信息，默认返回按大小排序。

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
        r"""获取实例占用空间最大的前几张表在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。

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
        r"""获取实例Top表的实时空间统计信息，默认返回按大小排序。

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


    def DescribeTopSpaceTablesV2(self, request):
        r"""表级空间 Top 对象查询（融合接口，多产品统一入口），按 SortBy 指定的排序字段返回实例内空间占用 Top N 的表/集合。支持产品：mysql（云数据库 MySQL）、cynosdb（TDSQL-C MySQL 版）、mongodb（云数据库 MongoDB）、postgres（云数据库 PostgreSQL）、dcdb（TDSQL MySQL 版）、tdsql（TDSQL）、mariadb（云数据库 MariaDB）。返回值根据产品类型返回对应字段：MySQL 系列返回 MysqlObjects，PostgreSQL 返回 PostgresObjects（PG 的 relation/bloat 字段与 MySQL 语义不同），MongoDB 返回 MongodbObjects。

        :param request: Request instance for DescribeTopSpaceTablesV2.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTablesV2Request`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTablesV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceTablesV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceTablesV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserAutonomyProfile(self, request):
        r"""自治中心-终止自治任务（单次）；注意： 接口调用需要加白名单。

        :param request: Request instance for DescribeUserAutonomyProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeUserAutonomyProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeUserAutonomyProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserAutonomyProfile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserAutonomyProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserSqlAdvice(self, request):
        r"""获取SQL优化建议。【产品用户回馈，此接口限免开放，后续将并入dbbrain专业版】

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
        r"""根据会话ID中断当前会话，该接口分为两次提交：第一次为预提交阶段，Stage为"Prepare"，得到的返回值包含SqlExecId；第二次为确认提交， Stage为"Commit"， 将SqlExecId的值作为参数传入，最终终止会话进程。注意：Prepare请求与Commit请求的间隔不能超过10秒，否则Prepare阶段生成的执行凭证（SqlExecId）将过期失效，Commit操作不会执行任何kill动作。

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
        r"""修改告警策略

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
        r"""修改审计配置相关信息，如高频存储时长等

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
        r"""修改实例的配置信息。

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
        r"""更改实例限流任务状态，目前仅用于终止限流。

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


    def ModifyUserAutonomyProfile(self, request):
        r"""自治中心-终止自治任务（单次）；注意：接口需要加白名单。

        :param request: Request instance for ModifyUserAutonomyProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyUserAutonomyProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyUserAutonomyProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserAutonomyProfile", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserAutonomyProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        r"""开启数据库审计服务

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
        r"""更新agent状态（停止或重连Agent）

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


    def UpdateDatabaseAutonomyStatus(self, request):
        r"""设置数据库自治功能的开关状态。当前支持 MongoDB 的索引推荐（AutoIndexAdvice）功能的开启或关闭。

        :param request: Request instance for UpdateDatabaseAutonomyStatus.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.UpdateDatabaseAutonomyStatusRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.UpdateDatabaseAutonomyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDatabaseAutonomyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDatabaseAutonomyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMonitorSwitch(self, request):
        r"""更新Agent实例状态（停止或重连实例）

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
        r"""验证用户数据库账号权限，获取会话token。

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