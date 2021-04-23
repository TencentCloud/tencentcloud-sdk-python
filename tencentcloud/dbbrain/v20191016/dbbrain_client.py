# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.dbbrain.v20191016 import models


class DbbrainClient(AbstractClient):
    _apiVersion = '2019-10-16'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'


    def AddUserContact(self, request):
        """添加邮件接收联系人的姓名， 邮件地址，返回值为添加成功的联系人id。Region统一选择广州。

        :param request: Request instance for AddUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.AddUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.AddUserContactResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUserContact", params)
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


    def CreateDBDiagReportTask(self, request):
        """创建健康报告，并可以选择是否发送邮件。

        :param request: Request instance for CreateDBDiagReportTask.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateDBDiagReportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateDBDiagReportTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBDiagReportTask", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateDBDiagReportUrlRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateDBDiagReportUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBDiagReportUrl", params)
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


    def CreateMailProfile(self, request):
        """创建邮件配置。其中入参ProfileType表示所创建配置的类型，ProfileType 取值包括：dbScan_mail_configuration（数据库巡检邮件配置）、scheduler_mail_configuration（定期生成健康报告的邮件发送配置）。Region统一选择广州，和实例所属地域无关。

        :param request: Request instance for CreateMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateMailProfileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMailProfile", params)
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


    def CreateSchedulerMailProfile(self, request):
        """该接口用于创建定期生成健康报告并邮件发送的配置，将健康报告的定期生成时间作为参数传入（周一至周日），用于设置健康报告的定期生成时间，同时保存相应的定期邮件发送的配置。

        :param request: Request instance for CreateSchedulerMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateSchedulerMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateSchedulerMailProfileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSchedulerMailProfile", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateSecurityAuditLogExportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateSecurityAuditLogExportTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityAuditLogExportTask", params)
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


    def DeleteSecurityAuditLogExportTasks(self, request):
        """删除安全审计日志导出任务。

        :param request: Request instance for DeleteSecurityAuditLogExportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DeleteSecurityAuditLogExportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DeleteSecurityAuditLogExportTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityAuditLogExportTasks", params)
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


    def DescribeAllUserContact(self, request):
        """获取邮件发送中联系人的相关信息。

        :param request: Request instance for DescribeAllUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserContactResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllUserContact", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserGroupRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllUserGroup", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagEventRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagEvent", params)
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


    def DescribeDBDiagHistory(self, request):
        """获取实例诊断事件的列表。

        :param request: Request instance for DescribeDBDiagHistory.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagHistoryRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagHistory", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagReportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagReportTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagReportTasks", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBSpaceStatusRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBSpaceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSpaceStatus", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDiagDBInstancesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDiagDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiagDBInstances", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeHealthScoreRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeHealthScoreResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHealthScore", params)
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
        """获取发送邮件的配置， 包括数据库巡检的邮件配置以及定期生成健康报告的邮件发送配置。Region统一选择广州。

        :param request: Request instance for DescribeMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeMailProfileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMailProfile", params)
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


    def DescribeSecurityAuditLogDownloadUrls(self, request):
        """查询安全审计日志导出文件下载链接。目前日志文件下载仅提供腾讯云内网地址，请通过广州地域的腾讯云服务器进行下载。

        :param request: Request instance for DescribeSecurityAuditLogDownloadUrls.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSecurityAuditLogDownloadUrlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSecurityAuditLogDownloadUrlsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityAuditLogDownloadUrls", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSecurityAuditLogExportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSecurityAuditLogExportTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityAuditLogExportTasks", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTimeSeriesStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTimeSeriesStatsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogTimeSeriesStats", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogTopSqls", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogUserHostStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogUserHostStatsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogUserHostStats", params)
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


    def DescribeTopSpaceSchemaTimeSeries(self, request):
        """获取实例占用空间最大的前几个库在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。

        :param request: Request instance for DescribeTopSpaceSchemaTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceSchemaTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceSchemaTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopSpaceSchemaTimeSeries", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceSchemasRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceSchemasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopSpaceSchemas", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTableTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTableTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopSpaceTableTimeSeries", params)
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
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTablesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopSpaceTables", params)
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
        """获取SQL优化建议。

        :param request: Request instance for DescribeUserSqlAdvice.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeUserSqlAdviceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeUserSqlAdviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserSqlAdvice", params)
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


    def ModifyDiagDBInstanceConf(self, request):
        """修改实例巡检开关。

        :param request: Request instance for ModifyDiagDBInstanceConf.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.ModifyDiagDBInstanceConfRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.ModifyDiagDBInstanceConfResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDiagDBInstanceConf", params)
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