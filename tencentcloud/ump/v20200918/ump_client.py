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
        """优mall产品启动下线流程

        上报相机移动、遮挡等告警信息


        :param request: Request instance for CreateCameraAlerts.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCameraAlerts", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCameraAlertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCameraState(self, request):
        """优mall产品启动下线流程

        上报当前场内所有相机的当前状态

        :param request: Request instance for CreateCameraState.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateCameraStateRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCameraStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCameraState", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCameraStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCapture(self, request):
        """优mall产品下线

        场内抓拍上报接口

        :param request: Request instance for CreateCapture.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateCaptureRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCaptureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCapture", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCaptureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiBizAlert(self, request):
        """优mall产品启动下线流程

        集团广场的多经点位告警

        :param request: Request instance for CreateMultiBizAlert.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateMultiBizAlertRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateMultiBizAlertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiBizAlert", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiBizAlertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProgramState(self, request):
        """优mall产品启动下线流程

        上报所有进程监控信息

        :param request: Request instance for CreateProgramState.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateProgramStateRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateProgramStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProgramState", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProgramStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServerState(self, request):
        """优mall产品启动下线流程

        上报所有服务器硬件监控信息

        :param request: Request instance for CreateServerState.
        :type request: :class:`tencentcloud.ump.v20200918.models.CreateServerStateRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateServerStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerState", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultiBizAlert(self, request):
        """优mall产品启动下线流程

        集团广场的多经点位消警

        :param request: Request instance for DeleteMultiBizAlert.
        :type request: :class:`tencentcloud.ump.v20200918.models.DeleteMultiBizAlertRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DeleteMultiBizAlertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultiBizAlert", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultiBizAlertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        """优mall产品启动下线流程

        删除集团广场对应的任务

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.ump.v20200918.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCameras(self, request):
        """优mall产品启动下线流程

        获取集团广场对应的摄像头列表

        :param request: Request instance for DescribeCameras.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeCamerasRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeCamerasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCameras", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCamerasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfig(self, request):
        """优mall产品启动下线流程

        获取摄像头配置信息
        mac不为空返回指定相机配置
        mac为空返回对应GroupCode和MallId全量配置

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImage(self, request):
        """优mall产品启动下线流程

        实时获取底图接口

        :param request: Request instance for DescribeImage.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeImageRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiBizBaseImage(self, request):
        """优mall产品启动下线流程

        获取多经点位底图

        :param request: Request instance for DescribeMultiBizBaseImage.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeMultiBizBaseImageRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeMultiBizBaseImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiBizBaseImage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiBizBaseImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """优mall产品启动下线流程

        查询集团广场对应的任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """优mall产品启动下线流程

        获取集团广场的点位列表

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.ump.v20200918.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiBizConfig(self, request):
        """优mall产品启动下线流程

        集团广场的多经点位配置更新

        :param request: Request instance for ModifyMultiBizConfig.
        :type request: :class:`tencentcloud.ump.v20200918.models.ModifyMultiBizConfigRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.ModifyMultiBizConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiBizConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiBizConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportServiceRegister(self, request):
        """优mall产品启动下线流程

        上报服务注册自身的服务地址作为回调地址, 用于信息回传。

        :param request: Request instance for ReportServiceRegister.
        :type request: :class:`tencentcloud.ump.v20200918.models.ReportServiceRegisterRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.ReportServiceRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportServiceRegister", params, headers=headers)
            response = json.loads(body)
            model = models.ReportServiceRegisterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchImage(self, request):
        """优mall产品启动下线流程

        以图搜图

        :param request: Request instance for SearchImage.
        :type request: :class:`tencentcloud.ump.v20200918.models.SearchImageRequest`
        :rtype: :class:`tencentcloud.ump.v20200918.models.SearchImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchImage", params, headers=headers)
            response = json.loads(body)
            model = models.SearchImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))