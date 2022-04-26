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
            if "Error" not in response["Response"]:
                model = models.AddUserContactResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CancelKillTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateDBDiagReportTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateDBDiagReportUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateKillTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateMailProfileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateProxySessionKillTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateSchedulerMailProfileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateSecurityAuditLogExportTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.CreateSqlFilterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityAuditLogExportTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DeleteSqlFiltersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeAllUserContactResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeAllUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagReportTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeDBSpaceStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeDiagDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeHealthScoreResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeMailProfileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeMySqlProcessListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeNoPrimaryKeyTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeProxySessionKillTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeRedisTopBigKeysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityAuditLogDownloadUrlsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityAuditLogExportTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogTimeSeriesStatsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogTopSqlsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogUserHostStatsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSqlFiltersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeSqlTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeTopSpaceSchemaTimeSeriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeTopSpaceSchemasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeTopSpaceTableTimeSeriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeTopSpaceTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.DescribeUserSqlAdviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.KillMySqlThreadsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDiagDBInstanceConf(self, request):
        """修改实例巡检开关。

        :param request: Request instance for ModifyDiagDBInstanceConf.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyDiagDBInstanceConfRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyDiagDBInstanceConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiagDBInstanceConf", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDiagDBInstanceConfResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.ModifySqlFiltersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            if "Error" not in response["Response"]:
                model = models.VerifyUserAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)