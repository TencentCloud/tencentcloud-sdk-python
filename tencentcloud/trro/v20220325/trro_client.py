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
from tencentcloud.trro.v20220325 import models


class TrroClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'trro.tencentcloudapi.com'
    _service = 'trro'


    def BatchDeleteDevices(self, request):
        r"""用于批量删除设备

        :param request: Request instance for BatchDeleteDevices.
        :type request: :class:`tencentcloud.trro.v20220325.models.BatchDeleteDevicesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.BatchDeleteDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteDevices", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeletePolicy(self, request):
        r"""用于批量删除修改权限配置

        :param request: Request instance for BatchDeletePolicy.
        :type request: :class:`tencentcloud.trro.v20220325.models.BatchDeletePolicyRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.BatchDeletePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeletePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeletePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BoundLicenses(self, request):
        r"""为推流设备绑定license，优先绑定到期时间最近的，到期时间相同优先绑定月包

        :param request: Request instance for BoundLicenses.
        :type request: :class:`tencentcloud.trro.v20220325.models.BoundLicensesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.BoundLicensesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BoundLicenses", params, headers=headers)
            response = json.loads(body)
            model = models.BoundLicensesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudRecording(self, request):
        r"""启动云端录制功能，完成房间内的音视频录制，并上传到指定的云存储。

        :param request: Request instance for CreateCloudRecording.
        :type request: :class:`tencentcloud.trro.v20220325.models.CreateCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.CreateCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDevice(self, request):
        r"""用于创建设备

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.trro.v20220325.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        r"""用于创建项目

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.trro.v20220325.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudRecording(self, request):
        r"""成功开启录制后，可以使用此接口来停止录制任务。停止录制成功后不代表文件全部传输完成，如果未完成后台将会继续上传文件，成功后通过事件回调通知客户文件全部传输完成状态。

        :param request: Request instance for DeleteCloudRecording.
        :type request: :class:`tencentcloud.trro.v20220325.models.DeleteCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DeleteCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        r"""用于删除项目

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.trro.v20220325.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceInfo(self, request):
        r"""用于获取指定设备信息

        :param request: Request instance for DescribeDeviceInfo.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceInfoRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceList(self, request):
        r"""用于获取设备信息列表

        :param request: Request instance for DescribeDeviceList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceSessionDetails(self, request):
        r"""获取设备会话数据详单

        :param request: Request instance for DescribeDeviceSessionDetails.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceSessionDetailsRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceSessionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceSessionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceSessionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceSessionList(self, request):
        r"""获取设备会话列表

        :param request: Request instance for DescribeDeviceSessionList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceSessionListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicy(self, request):
        r"""用于查看权限配置

        :param request: Request instance for DescribePolicy.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribePolicyRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectInfo(self, request):
        r"""用于获取项目信息

        :param request: Request instance for DescribeProjectInfo.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeProjectInfoRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeProjectInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectList(self, request):
        r"""用于获取项目列表

        :param request: Request instance for DescribeProjectList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeProjectListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecentSessionList(self, request):
        r"""获取最新设备会话列表

        :param request: Request instance for DescribeRecentSessionList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeRecentSessionListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeRecentSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecentSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecentSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionStatistics(self, request):
        r"""获取会话统计值

        :param request: Request instance for DescribeSessionStatistics.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionStatisticsByInterval(self, request):
        r"""获取各时间段的会话统计值

        :param request: Request instance for DescribeSessionStatisticsByInterval.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsByIntervalRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsByIntervalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionStatisticsByInterval", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionStatisticsByIntervalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceLicense(self, request):
        r"""获取设备已经绑定的可用授权数量

        :param request: Request instance for GetDeviceLicense.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetDeviceLicenseRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetDeviceLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceLicense", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevices(self, request):
        r"""查询用户设备的授权绑定情况

        :param request: Request instance for GetDevices.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevices", params, headers=headers)
            response = json.loads(body)
            model = models.GetDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDurationDetails(self, request):
        r"""查询该时间段、对应项目、设备的不同分辨率的通话时长流水，流水以日期（天）为单位

        :param request: Request instance for GetDurationDetails.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetDurationDetailsRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetDurationDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDurationDetails", params, headers=headers)
            response = json.loads(body)
            model = models.GetDurationDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLicenseStat(self, request):
        r"""统计license类型数量

        :param request: Request instance for GetLicenseStat.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetLicenseStatRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetLicenseStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLicenseStat", params, headers=headers)
            response = json.loads(body)
            model = models.GetLicenseStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLicenses(self, request):
        r"""按授权查看license列表

        :param request: Request instance for GetLicenses.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetLicensesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetLicensesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLicenses", params, headers=headers)
            response = json.loads(body)
            model = models.GetLicensesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTotalDuration(self, request):
        r"""查询该时间段、对应项目、设备的不同分辨率的通话时长汇总

        :param request: Request instance for GetTotalDuration.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetTotalDurationRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetTotalDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTotalDuration", params, headers=headers)
            response = json.loads(body)
            model = models.GetTotalDurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCallbackUrl(self, request):
        r"""设置回调URL
        录制回调事件内容参考：https://cloud.tencent.com/document/product/647/81113
        转推回调事件内容参考：https://cloud.tencent.com/document/product/647/88552

        :param request: Request instance for ModifyCallbackUrl.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyCallbackUrlRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyCallbackUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCallbackUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCallbackUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDevice(self, request):
        r"""用于修改设备信息

        :param request: Request instance for ModifyDevice.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPolicy(self, request):
        r"""用于修改权限配置

        :param request: Request instance for ModifyPolicy.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyPolicyRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        r"""用于修改项目信息

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProjectSecMode(self, request):
        r"""使用项目共享密钥可动态生成设备登录密钥，登录前无需对设备进行提前注册，适合希望简化业务流程的客户。由于是公共密钥，请务必注意保护项目共享密钥，并及时更新。建议项目共享密钥保存在服务器侧。由服务器生成设备登录密码下发给设备，避免密钥保存在客户端侧产生的密钥泄露风险。

        开启项目共享密钥后，对于已注册的设备，仍可使用原设备密码登录。若希望仅能通过共享密钥生成密码登录，请通过云 API 将设备密码更新为"USEPROJECTKEYPWD"。

        :param request: Request instance for ModifyProjectSecMode.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyProjectSecModeRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyProjectSecModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProjectSecMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectSecModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishLiveStream(self, request):
        r"""启动一个混流转推任务，将 TRTC 房间的多路音视频流混成一路音视频流，编码后推到直播 CDN 或者回推到 TRTC 房间。也支持不转码直接转推 TRTC 房间的单路流。启动成功后，会返回一个 SdkAppid 维度唯一的任务 Id（TaskId）。您需要保存该 TaskId，后续需要依赖此 TaskId 更新和结束任务。

        :param request: Request instance for StartPublishLiveStream.
        :type request: :class:`tencentcloud.trro.v20220325.models.StartPublishLiveStreamRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.StartPublishLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPublishLiveStream(self, request):
        r"""停止指定的混流转推任务。如果没有调用 Stop 接口停止任务，所有参与混流转推的主播离开房间超过MaxIdleTime 设置的时间后，任务也会自动停止。

        :param request: Request instance for StopPublishLiveStream.
        :type request: :class:`tencentcloud.trro.v20220325.models.StopPublishLiveStreamRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.StopPublishLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPublishLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopPublishLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))