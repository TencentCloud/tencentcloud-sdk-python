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
from tencentcloud.tiw.v20190919 import models


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.tencentcloudapi.com'
    _service = 'tiw'


    def ApplyTiwTrial(self, request):
        """申请互动白板试用，默认15天

        :param request: Request instance for ApplyTiwTrial.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ApplyTiwTrialRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ApplyTiwTrialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyTiwTrial", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyTiwTrialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplication(self, request):
        """创建白板应用

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOfflineRecord(self, request):
        """创建课后录制任务

        :param request: Request instance for CreateOfflineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateOfflineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateOfflineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOfflineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePPTCheckTask(self, request):
        """检测PPT文件，识别PPT中包含的动态转码任务（Transcode）不支持的元素

        :param request: Request instance for CreatePPTCheckTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreatePPTCheckTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreatePPTCheckTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePPTCheckTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePPTCheckTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSnapshotTask(self, request):
        """创建白板板书生成任务, 在任务结束后，如果提供了回调地址，将通过回调地址通知板书生成结果

        :param request: Request instance for CreateSnapshotTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateSnapshotTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateSnapshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTranscode(self, request):
        """创建一个文档转码任务

        :param request: Request instance for CreateTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVideoGenerationTask(self, request):
        """创建视频生成任务

        :param request: Request instance for CreateVideoGenerationTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateVideoGenerationTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateVideoGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAPIService(self, request):
        """通过服务角色调用其他云产品API接口获取信息

        :param request: Request instance for DescribeAPIService.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeAPIServiceRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationInfos(self, request):
        """查询白板应用详情

        :param request: Request instance for DescribeApplicationInfos.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationInfosRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationUsage(self, request):
        """查询互动白板各个子产品用量

        :param request: Request instance for DescribeApplicationUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBoardSDKLog(self, request):
        """查询客户端白板日志

        :param request: Request instance for DescribeBoardSDKLog.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeBoardSDKLogRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeBoardSDKLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBoardSDKLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBoardSDKLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIMApplications(self, request):
        """查询可用于创建白板应用的IM应用列表

        :param request: Request instance for DescribeIMApplications.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeIMApplicationsRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeIMApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIMApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIMApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOfflineRecord(self, request):
        """查询课后录制任务的进度与录制结果等相关信息

        :param request: Request instance for DescribeOfflineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOfflineRecordCallback(self, request):
        """查询课后录制回调地址

        :param request: Request instance for DescribeOfflineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOnlineRecord(self, request):
        """查询录制任务状态与结果

        :param request: Request instance for DescribeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOnlineRecordCallback(self, request):
        """查询实时录制回调地址

        :param request: Request instance for DescribeOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePPTCheck(self, request):
        """查询PPT检测任务的执行进度或结果

        :param request: Request instance for DescribePPTCheck.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePPTCheck", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePPTCheckResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePPTCheckCallback(self, request):
        """查询PPT检测任务回调地址

        :param request: Request instance for DescribePPTCheckCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePPTCheckCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePPTCheckCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePostpaidUsage(self, request):
        """查询用户后付费用量

        :param request: Request instance for DescribePostpaidUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribePostpaidUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribePostpaidUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostpaidUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostpaidUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeQualityMetrics(self, request):
        """查询互动白板质量数据

        :param request: Request instance for DescribeQualityMetrics.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeQualityMetricsRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeQualityMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordSearch(self, request):
        """根据房间号搜索实时录制任务

        :param request: Request instance for DescribeRecordSearch.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeRecordSearchRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeRecordSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRoomList(self, request):
        """查询白板房间列表

        :param request: Request instance for DescribeRoomList.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeRoomListRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeRoomListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRunningTasks(self, request):
        """根据指定的任务类型，获取当前正在执行中的任务列表。只能查询最近3天内创建的任务。

        :param request: Request instance for DescribeRunningTasks.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeRunningTasksRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeRunningTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRunningTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRunningTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshotTask(self, request):
        """获取指定白板板书生成任务信息

        :param request: Request instance for DescribeSnapshotTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeSnapshotTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeSnapshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTIWDailyUsage(self, request):
        """查询互动白板天维度计费用量。
        1. 单次查询统计区间最多不能超过31天。
        2. 由于统计延迟等原因，暂时不支持查询当天数据，建议在次日上午7点以后再来查询前一天的用量，例如在10月27日上午7点后，再来查询到10月26日整天的用量

        :param request: Request instance for DescribeTIWDailyUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWDailyUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWDailyUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTIWDailyUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTIWDailyUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTIWRoomDailyUsage(self, request):
        """查询互动白板房间维度每天计费用量。
        1. 单次查询统计区间最多不能超过31天。
        2. 由于统计延迟等原因，暂时不支持查询当天数据，建议在次日上午7点以后再来查询前一天的用量，例如在10月27日上午7点后，再来查询到10月26日整天的用量

        :param request: Request instance for DescribeTIWRoomDailyUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWRoomDailyUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWRoomDailyUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTIWRoomDailyUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTIWRoomDailyUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscode(self, request):
        """查询文档转码任务的执行进度与转码结果

        :param request: Request instance for DescribeTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscodeCallback(self, request):
        """查询文档转码回调地址

        :param request: Request instance for DescribeTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscodeSearch(self, request):
        """按文档名称搜索转码任务

        :param request: Request instance for DescribeTranscodeSearch.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeSearchRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsageSummary(self, request):
        """查询指定时间段内子产品的用量汇总

        :param request: Request instance for DescribeUsageSummary.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUsageSummaryRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUsageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsageSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserList(self, request):
        """查询白板用户列表

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserResources(self, request):
        """查询客户资源列表

        :param request: Request instance for DescribeUserResources.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUserResourcesRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUserResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserStatus(self, request):
        """查询互动白板用户详情，包括是否开通了互动白板，当前互动白板服务有效期等信息

        :param request: Request instance for DescribeUserStatus.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUserStatusRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUserStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVideoGenerationTask(self, request):
        """查询录制视频生成任务状态与结果

        :param request: Request instance for DescribeVideoGenerationTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVideoGenerationTaskCallback(self, request):
        """查询录制视频生成回调地址

        :param request: Request instance for DescribeVideoGenerationTaskCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoGenerationTaskCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoGenerationTaskCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWarningCallback(self, request):
        """查询告警回调地址。此功能需要申请白名单使用。

        :param request: Request instance for DescribeWarningCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWarningCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWarningCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWhiteboardApplicationConfig(self, request):
        """查询白板应用任务相关的配置，包括存储桶、回调等

        :param request: Request instance for DescribeWhiteboardApplicationConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWhiteboardBucketConfig(self, request):
        """查询文档转码，实时录制存储桶的配置

        :param request: Request instance for DescribeWhiteboardBucketConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardBucketConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardBucketConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardBucketConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardBucketConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWhiteboardPush(self, request):
        """查询推流任务状态与结果

        :param request: Request instance for DescribeWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWhiteboardPushCallback(self, request):
        """查询白板推流回调地址

        :param request: Request instance for DescribeWhiteboardPushCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPushCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWhiteboardPushSearch(self, request):
        """根据房间号搜索白板推流任务

        :param request: Request instance for DescribeWhiteboardPushSearch.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushSearchRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPushSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplication(self, request):
        """修改白板应用

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAutoRenewFlag(self, request):
        """设置白板月功能费自动续费

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWhiteboardApplicationConfig(self, request):
        """修改白板应用任务相关的配置，包括存储桶、回调等

        :param request: Request instance for ModifyWhiteboardApplicationConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWhiteboardApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWhiteboardApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWhiteboardBucketConfig(self, request):
        """设置文档转码，实时录制存储桶的配置

        :param request: Request instance for ModifyWhiteboardBucketConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardBucketConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardBucketConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWhiteboardBucketConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWhiteboardBucketConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseOnlineRecord(self, request):
        """暂停实时录制

        :param request: Request instance for PauseOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PauseOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeOnlineRecord(self, request):
        """恢复实时录制

        :param request: Request instance for ResumeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetOfflineRecordCallback(self, request):
        """设置课后录制回调地址

        :param request: Request instance for SetOfflineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOfflineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOfflineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOfflineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetOfflineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetOnlineRecordCallback(self, request):
        """设置实时录制回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258

        :param request: Request instance for SetOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetOnlineRecordCallbackKey(self, request):
        """设置实时录制回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetOnlineRecordCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetPPTCheckCallback(self, request):
        """设置PPT检测任务回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260#c9cbe05f-fe1a-4410-b4dc-40cc301c7b81

        :param request: Request instance for SetPPTCheckCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPPTCheckCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetPPTCheckCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetPPTCheckCallbackKey(self, request):
        """设置PPT检测任务回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetPPTCheckCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPPTCheckCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetPPTCheckCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTranscodeCallback(self, request):
        """设置文档转码回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260

        :param request: Request instance for SetTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTranscodeCallbackKey(self, request):
        """设置文档转码回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetTranscodeCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetVideoGenerationTaskCallback(self, request):
        """设置录制视频生成回调地址

        :param request: Request instance for SetVideoGenerationTaskCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVideoGenerationTaskCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetVideoGenerationTaskCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetVideoGenerationTaskCallbackKey(self, request):
        """设置视频生成回调鉴权密钥

        :param request: Request instance for SetVideoGenerationTaskCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVideoGenerationTaskCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetVideoGenerationTaskCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetWarningCallback(self, request):
        """设置告警回调地址。此功能需要申请白名单使用。

        :param request: Request instance for SetWarningCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWarningCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWarningCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWarningCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetWarningCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetWhiteboardPushCallback(self, request):
        """设置白板推流回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetWhiteboardPushCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWhiteboardPushCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetWhiteboardPushCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetWhiteboardPushCallbackKey(self, request):
        """设置白板推流回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetWhiteboardPushCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWhiteboardPushCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetWhiteboardPushCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartOnlineRecord(self, request):
        """发起一个实时录制任务

        :param request: Request instance for StartOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartWhiteboardPush(self, request):
        """发起一个白板推流任务

        :param request: Request instance for StartWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.StartWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopOnlineRecord(self, request):
        """停止实时录制

        :param request: Request instance for StopOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopWhiteboardPush(self, request):
        """停止白板推流任务

        :param request: Request instance for StopWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.StopWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)