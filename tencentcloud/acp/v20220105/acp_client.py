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
from tencentcloud.acp.v20220105 import models


class AcpClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'acp.tencentcloudapi.com'
    _service = 'acp'


    def CreateAppScanTask(self, request):
        """创建应用合规隐私诊断任务

        :param request: Request instance for CreateAppScanTask.
        :type request: :class:`tencentcloud.acp.v20220105.models.CreateAppScanTaskRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.CreateAppScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAppScanTaskRepeat(self, request):
        """App应用合规隐私诊断重试任务

        :param request: Request instance for CreateAppScanTaskRepeat.
        :type request: :class:`tencentcloud.acp.v20220105.models.CreateAppScanTaskRepeatRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.CreateAppScanTaskRepeatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppScanTaskRepeat", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppScanTaskRepeatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannelTaskReportUrl(self, request):
        """获取子渠道的App合规诊断任务报告url

        :param request: Request instance for DescribeChannelTaskReportUrl.
        :type request: :class:`tencentcloud.acp.v20220105.models.DescribeChannelTaskReportUrlRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.DescribeChannelTaskReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelTaskReportUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChannelTaskReportUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileTicket(self, request):
        """获取应用合规文件上传凭证，用于上传诊断文件

        :param request: Request instance for DescribeFileTicket.
        :type request: :class:`tencentcloud.acp.v20220105.models.DescribeFileTicketRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.DescribeFileTicketResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTicket", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTicketResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceUsageInfo(self, request):
        """查询应用合规平台用户资源的使用情况

        :param request: Request instance for DescribeResourceUsageInfo.
        :type request: :class:`tencentcloud.acp.v20220105.models.DescribeResourceUsageInfoRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.DescribeResourceUsageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUsageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceUsageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScanTaskList(self, request):
        """获取App隐私合规诊断任务列表

        :param request: Request instance for DescribeScanTaskList.
        :type request: :class:`tencentcloud.acp.v20220105.models.DescribeScanTaskListRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.DescribeScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScanTaskReportUrl(self, request):
        """获取App合规诊断任务报告url

        :param request: Request instance for DescribeScanTaskReportUrl.
        :type request: :class:`tencentcloud.acp.v20220105.models.DescribeScanTaskReportUrlRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.DescribeScanTaskReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskReportUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskReportUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScanTaskStatus(self, request):
        """查询App隐私合规诊断任务状态

        :param request: Request instance for DescribeScanTaskStatus.
        :type request: :class:`tencentcloud.acp.v20220105.models.DescribeScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.acp.v20220105.models.DescribeScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)