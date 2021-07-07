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
from tencentcloud.ump.v20200918 import models


class UmpClient(AbstractClient):
    _apiVersion = '2020-09-18'
    _endpoint = 'ump.tencentcloudapi.com'
    _service = 'ump'


    def CreateCameraAlerts(self, request):
        """上报相机移动、遮挡等告警信息


        :param request: Request instance for CreateCameraAlerts.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCameraAlerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCameraAlertsResponse()
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


    def CreateCameraState(self, request):
        """上报当前场内所有相机的当前状态

        :param request: Request instance for CreateCameraState.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateCameraStateRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCameraStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCameraState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCameraStateResponse()
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


    def CreateCapture(self, request):
        """场内抓拍上报接口

        :param request: Request instance for CreateCapture.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateCaptureRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCaptureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCapture", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCaptureResponse()
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


    def CreateMultiBizAlert(self, request):
        """集团广场的多经点位告警

        :param request: Request instance for CreateMultiBizAlert.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateMultiBizAlertRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateMultiBizAlertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMultiBizAlert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMultiBizAlertResponse()
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


    def CreateProgramState(self, request):
        """上报所有进程监控信息

        :param request: Request instance for CreateProgramState.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateProgramStateRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateProgramStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProgramState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProgramStateResponse()
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


    def CreateServerState(self, request):
        """上报所有服务器硬件监控信息

        :param request: Request instance for CreateServerState.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateServerStateRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateServerStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServerState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServerStateResponse()
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


    def DeleteMultiBizAlert(self, request):
        """集团广场的多经点位消警

        :param request: Request instance for DeleteMultiBizAlert.
        :type request: :class:`tencentcloud.ump.v20200918.models.DeleteMultiBizAlertRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DeleteMultiBizAlertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMultiBizAlert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMultiBizAlertResponse()
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


    def DeleteTask(self, request):
        """删除集团广场对应的任务

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.ump.v20200918.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTaskResponse()
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


    def DescribeCameras(self, request):
        """获取集团广场对应的摄像头列表

        :param request: Request instance for DescribeCameras.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeCamerasRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeCamerasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCameras", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCamerasResponse()
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


    def DescribeConfig(self, request):
        """获取摄像头配置信息
        mac不为空返回指定相机配置
        mac为空返回对应GroupCode和MallId全量配置

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeImage(self, request):
        """实时获取底图接口

        :param request: Request instance for DescribeImage.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeImageRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageResponse()
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


    def DescribeMultiBizBaseImage(self, request):
        """获取多经点位底图

        :param request: Request instance for DescribeMultiBizBaseImage.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeMultiBizBaseImageRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeMultiBizBaseImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMultiBizBaseImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMultiBizBaseImageResponse()
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


    def DescribeTasks(self, request):
        """查询集团广场对应的任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def DescribeZones(self, request):
        """获取集团广场的点位列表

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def ModifyMultiBizConfig(self, request):
        """集团广场的多经点位配置更新

        :param request: Request instance for ModifyMultiBizConfig.
        :type request: :class:`tencentcloud.ump.v20200918.models.ModifyMultiBizConfigRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.ModifyMultiBizConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMultiBizConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMultiBizConfigResponse()
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


    def ReportServiceRegister(self, request):
        """上报服务注册自身的服务地址作为回调地址, 用于信息回传。

        :param request: Request instance for ReportServiceRegister.
        :type request: :class:`tencentcloud.ump.v20200918.models.ReportServiceRegisterRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.ReportServiceRegisterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReportServiceRegister", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportServiceRegisterResponse()
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


    def SearchImage(self, request):
        """以图搜图

        :param request: Request instance for SearchImage.
        :type request: :class:`tencentcloud.ump.v20200918.models.SearchImageRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.SearchImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchImageResponse()
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