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
from tencentcloud.trro.v20220325 import models


class TrroClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'trro.tencentcloudapi.com'
    _service = 'trro'


    def BatchDeleteDevices(self, request):
        """用于批量删除设备

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
        """用于批量删除修改权限配置

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
        """为推流设备绑定license，优先绑定到期时间最近的，到期时间相同优先绑定月包

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


    def CreateDevice(self, request):
        """用于创建设备

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
        """用于创建项目

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


    def DeleteProject(self, request):
        """用于删除项目

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
        """用于获取指定设备信息

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
        """用于获取设备信息列表

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
        """获取设备会话数据详单

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
        """获取设备会话列表

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
        """用于查看权限配置

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
        """用于获取项目信息

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
        """用于获取项目列表

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
        """获取最新设备会话列表

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
        """获取会话统计值

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
        """获取各时间段的会话统计值

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
        """获取设备已经绑定的可用授权数量

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
        """查询用户设备的授权绑定情况

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


    def GetLicenseStat(self, request):
        """统计license类型数量

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
        """按授权查看license列表

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


    def ModifyDevice(self, request):
        """用于修改设备信息

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
        """用于修改权限配置

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
        """用于修改项目信息

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
        """使用项目共享密钥可动态生成设备登录密钥，登录前无需对设备进行提前注册，适合希望简化业务流程的客户。由于是公共密钥，请务必注意保护项目共享密钥，并及时更新。建议项目共享密钥保存在服务器侧。由服务器生成设备登录密码下发给设备，避免密钥保存在客户端侧产生的密钥泄露风险。

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