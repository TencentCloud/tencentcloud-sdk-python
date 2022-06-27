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
from tencentcloud.mmps.v20200710 import models


class MmpsClient(AbstractClient):
    _apiVersion = '2020-07-10'
    _endpoint = 'mmps.tencentcloudapi.com'
    _service = 'mmps'


    def CreateAppScanTask(self, request):
        """创建小程序隐私合规诊断任务

        :param request: Request instance for CreateAppScanTask.
        :type request: :class:`tencentcloud.mmps.v20200710.models.CreateAppScanTaskRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.CreateAppScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAppScanTaskResponse()
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


    def CreateAppScanTaskRepeat(self, request):
        """小程序隐私合规诊断重试任务

        :param request: Request instance for CreateAppScanTaskRepeat.
        :type request: :class:`tencentcloud.mmps.v20200710.models.CreateAppScanTaskRepeatRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.CreateAppScanTaskRepeatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppScanTaskRepeat", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAppScanTaskRepeatResponse()
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


    def CreateFlySecMiniAppScanTask(self, request):
        """创建小程序翼扬安全的基础或深度诊断任务

        :param request: Request instance for CreateFlySecMiniAppScanTask.
        :type request: :class:`tencentcloud.mmps.v20200710.models.CreateFlySecMiniAppScanTaskRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.CreateFlySecMiniAppScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlySecMiniAppScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlySecMiniAppScanTaskResponse()
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


    def CreateFlySecMiniAppScanTaskRepeat(self, request):
        """重新提交基础诊断任务

        :param request: Request instance for CreateFlySecMiniAppScanTaskRepeat.
        :type request: :class:`tencentcloud.mmps.v20200710.models.CreateFlySecMiniAppScanTaskRepeatRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.CreateFlySecMiniAppScanTaskRepeatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlySecMiniAppScanTaskRepeat", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlySecMiniAppScanTaskRepeatResponse()
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


    def DescribeBasicDiagnosisResourceUsageInfo(self, request):
        """查询翼扬安全基础诊断资源使用情况

        :param request: Request instance for DescribeBasicDiagnosisResourceUsageInfo.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeBasicDiagnosisResourceUsageInfoRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeBasicDiagnosisResourceUsageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBasicDiagnosisResourceUsageInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicDiagnosisResourceUsageInfoResponse()
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


    def DescribeFlySecMiniAppReportUrl(self, request):
        """获取翼扬诊断任务报告链接地址

        :param request: Request instance for DescribeFlySecMiniAppReportUrl.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppReportUrlRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlySecMiniAppReportUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlySecMiniAppReportUrlResponse()
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


    def DescribeFlySecMiniAppScanReportList(self, request):
        """查询指定小程序版本的翼扬诊断安全得分

        :param request: Request instance for DescribeFlySecMiniAppScanReportList.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanReportListRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlySecMiniAppScanReportList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlySecMiniAppScanReportListResponse()
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


    def DescribeFlySecMiniAppScanTaskList(self, request):
        """获取翼扬安全诊断任务列表

        :param request: Request instance for DescribeFlySecMiniAppScanTaskList.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanTaskListRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlySecMiniAppScanTaskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlySecMiniAppScanTaskListResponse()
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


    def DescribeFlySecMiniAppScanTaskParam(self, request):
        """获取用户提交的基础诊断任务参数信息

        :param request: Request instance for DescribeFlySecMiniAppScanTaskParam.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanTaskParamRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanTaskParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlySecMiniAppScanTaskParam", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlySecMiniAppScanTaskParamResponse()
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


    def DescribeFlySecMiniAppScanTaskStatus(self, request):
        """查询翼扬安全诊断任务状态

        :param request: Request instance for DescribeFlySecMiniAppScanTaskStatus.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeFlySecMiniAppScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlySecMiniAppScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlySecMiniAppScanTaskStatusResponse()
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


    def DescribeResourceUsageInfo(self, request):
        """查询翼扬安全资源使用情况

        :param request: Request instance for DescribeResourceUsageInfo.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeResourceUsageInfoRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeResourceUsageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUsageInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceUsageInfoResponse()
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


    def DescribeScanTaskList(self, request):
        """获取小程序隐私合规诊断任务列表

        :param request: Request instance for DescribeScanTaskList.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeScanTaskListRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanTaskListResponse()
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


    def DescribeScanTaskReportUrl(self, request):
        """获取小程序合规诊断任务报告url

        :param request: Request instance for DescribeScanTaskReportUrl.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeScanTaskReportUrlRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeScanTaskReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskReportUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanTaskReportUrlResponse()
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


    def DescribeScanTaskStatus(self, request):
        """查询小程序隐私合规诊断任务状态

        :param request: Request instance for DescribeScanTaskStatus.
        :type request: :class:`tencentcloud.mmps.v20200710.models.DescribeScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.mmps.v20200710.models.DescribeScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanTaskStatusResponse()
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