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
from tencentcloud.iss.v20230517 import models


class IssClient(AbstractClient):
    _apiVersion = '2023-05-17'
    _endpoint = 'iss.tencentcloudapi.com'
    _service = 'iss'


    def AddAITask(self, request):
        """添加AI任务

        :param request: Request instance for AddAITask.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddAITaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddAITaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAITask", params, headers=headers)
            response = json.loads(body)
            model = models.AddAITaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganization(self, request):
        """用于新增组织。

        :param request: Request instance for AddOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordBackupPlan(self, request):
        """用于新增录像上云计划 （当前仅适用于通过GB28181协议和网关接入的设备/视频通道）

        :param request: Request instance for AddRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordBackupTemplate(self, request):
        """用于新增录像上云模板。
        > 该功能本质是拉取设备本地录像数据上云（即存在 IPC 摄像头存储卡或 NVR 硬盘中的录像），操作时需先设定录像时间段（即想要上云的设备本地录像），再设定上云时间段和上云倍速，平台将于上云时间段倍速拉取设备对应前一天的录像时间段数据。

        > 设定需至少满足（上云时间段=前一天的录像时间段/上云倍速），建议上云时间段可多设定10%左右的时间，避免因网络波动导致数据拉取不完整。

        :param request: Request instance for AddRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordPlan(self, request):
        """用于新增实时上云计划

        :param request: Request instance for AddRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordRetrieveTask(self, request):
        """用于新建取回任务

        :param request: Request instance for AddRecordRetrieveTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordRetrieveTask", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordRetrieveTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordTemplate(self, request):
        """用于新增实时上云模板

        :param request: Request instance for AddRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddStreamAuth(self, request):
        """用于设置推拉流鉴权配置。

        :param request: Request instance for AddStreamAuth.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddStreamAuth", params, headers=headers)
            response = json.loads(body)
            model = models.AddStreamAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUserDevice(self, request):
        """用于新增单个设备。添加设备之后，可根据返回结果到设备上进行配置，配置后等待设备注册/推流。

        :param request: Request instance for AddUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchOperateDevice(self, request):
        """用于批量操作（启用，禁用，删除）设备

        :param request: Request instance for BatchOperateDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchOperateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.BatchOperateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDomain(self, request):
        """用于检测域名是否备案。

        :param request: Request instance for CheckDomain.
        :type request: :class:`tencentcloud.iss.v20230517.models.CheckDomainRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CheckDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDevicePTZ(self, request):
        """用于设备通道云台控制，包括转动、变倍、变焦、光圈等。

        :param request: Request instance for ControlDevicePTZ.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDevicePTZRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDevicePTZResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDevicePTZ", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDevicePTZResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDevicePreset(self, request):
        """用于操作设备预置位，包括设置、删除、调用。

        :param request: Request instance for ControlDevicePreset.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDevicePresetRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDevicePresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDevicePreset", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDevicePresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDeviceStream(self, request):
        """用于获取设备的实时开流地址。

        :param request: Request instance for ControlDeviceStream.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDeviceStream", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDeviceStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlRecord(self, request):
        """用于录像回放过程中的倍速、跳转、播放/暂停/停止等控制。

        :param request: Request instance for ControlRecord.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlRecordRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ControlRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlRecordTimeline(self, request):
        """用于查询设备本地录像时间轴信息，为NVR/IPC本地存储的录像。

        :param request: Request instance for ControlRecordTimeline.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlRecordTimelineRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlRecordTimelineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlRecordTimeline", params, headers=headers)
            response = json.loads(body)
            model = models.ControlRecordTimelineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAITask(self, request):
        """删除AI任务

        :param request: Request instance for DeleteAITask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteAITaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteAITaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAITask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAITaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomain(self, request):
        """用于删除域名。

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGateway(self, request):
        """用于删除网关。

        :param request: Request instance for DeleteGateway.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteGatewayRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganization(self, request):
        """用于删除组织。

        :param request: Request instance for DeleteOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordBackupPlan(self, request):
        """用于删除录像上云模板。

        :param request: Request instance for DeleteRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordBackupTemplate(self, request):
        """用于删除录像上云模板。

        :param request: Request instance for DeleteRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordPlan(self, request):
        """用于删除实时上云计划

        :param request: Request instance for DeleteRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordRetrieveTask(self, request):
        """用于删除取回任务

        :param request: Request instance for DeleteRecordRetrieveTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordRetrieveTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordRetrieveTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordRetrieveTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordRetrieveTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordTemplate(self, request):
        """用于删除实时上云模板

        :param request: Request instance for DeleteRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserDevice(self, request):
        """用于删除已添加的设备。

        :param request: Request instance for DeleteUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAITask(self, request):
        """获取AI任务详情

        :param request: Request instance for DescribeAITask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeAITaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeAITaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAITask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAITaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAITaskResult(self, request):
        """获取AI任务识别结果

        :param request: Request instance for DescribeAITaskResult.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeAITaskResultRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeAITaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAITaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAITaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCNAME(self, request):
        """用于根据服务节点获取 CNAME 值。

        :param request: Request instance for DescribeCNAME.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeCNAMERequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceChannel(self, request):
        """用于查询设备的通道。

        :param request: Request instance for DescribeDeviceChannel.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceChannelRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePreset(self, request):
        """用于查询设备通道预置位信息。

        :param request: Request instance for DescribeDevicePreset.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDevicePresetRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDevicePresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePreset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceRegion(self, request):
        """用于添加设备时，查询设备可以使用的服务节点，查询结果为已经绑定了域名的服务节点。

        :param request: Request instance for DescribeDeviceRegion.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceRegionRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomain(self, request):
        """用于查询添加的域名列表。

        :param request: Request instance for DescribeDomain.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDomainRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainRegion(self, request):
        """用于用户添加域名时，查询可以绑定的服务节点，结果为平台支持的所有服务节点。（注意：每个服务节点只能绑定一个域名）

        :param request: Request instance for DescribeDomainRegion.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDomainRegionRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDomainRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGateway(self, request):
        """用于获取网关详情。

        :param request: Request instance for DescribeGateway.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayMonitor(self, request):
        """用于获取网关的数据及流量监控信息。

        :param request: Request instance for DescribeGatewayMonitor.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayMonitorRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayProtocol(self, request):
        """用于查询网关接入协议。

        :param request: Request instance for DescribeGatewayProtocol.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayProtocolRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayProtocolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayProtocol", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayProtocolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayVersion(self, request):
        """查询网关服务版本

        :param request: Request instance for DescribeGatewayVersion.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayVersionRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganization(self, request):
        """用于查询组织。

        :param request: Request instance for DescribeOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordBackupPlan(self, request):
        """用于查询录像上云计划详情。

        :param request: Request instance for DescribeRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordBackupTemplate(self, request):
        """用于查询录像上云模板详情。

        :param request: Request instance for DescribeRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordFile(self, request):
        """用于查询设备云端录像时间轴信息（即为视频上云后设置录像计划后云存储的录像）

        :param request: Request instance for DescribeRecordFile.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordPlan(self, request):
        """用于查询实时上云计划详情

        :param request: Request instance for DescribeRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordPlaybackUrl(self, request):
        """用于获取云端录像回放url地址

        :param request: Request instance for DescribeRecordPlaybackUrl.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlaybackUrlRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlaybackUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordPlaybackUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordPlaybackUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordRetrieveTask(self, request):
        """用于查询云录像取回任务详情

        :param request: Request instance for DescribeRecordRetrieveTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordRetrieveTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordRetrieveTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordSlice(self, request):
        """平台支持将数据以TS切片的形式存入客户自有COS桶，该接口用于支持客户快捷查询切片信息列表
        （注意：只支持标准存储类型的查询）

        :param request: Request instance for DescribeRecordSlice.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordSliceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordSliceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordSlice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordSliceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordTemplate(self, request):
        """用于查询实时上云模板详情

        :param request: Request instance for DescribeRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamAuth(self, request):
        """用于查询推拉流鉴权配置。

        :param request: Request instance for DescribeStreamAuth.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTask(self, request):
        """用于查询任务详情

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDevice(self, request):
        """用于查询设备的详细信息。

        :param request: Request instance for DescribeUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoBitRate(self, request):
        """用于获取视频通道的码率信息

        :param request: Request instance for DescribeVideoBitRate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoBitRate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoBitRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoDownloadUrl(self, request):
        """用于获取云录像下载 url

        :param request: Request instance for DescribeVideoDownloadUrl.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAITasks(self, request):
        """获取AI任务列表

        :param request: Request instance for ListAITasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListAITasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListAITasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAITasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListAITasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDevices(self, request):
        """用于获取对应组织下的设备列表。

        :param request: Request instance for ListDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListGatewayDevices(self, request):
        """用于查询网关下挂载的设备列表。

        :param request: Request instance for ListGatewayDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListGatewayDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListGatewayDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGatewayDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListGatewayDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListGateways(self, request):
        """用于获取网关列表。

        :param request: Request instance for ListGateways.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListGatewaysRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGateways", params, headers=headers)
            response = json.loads(body)
            model = models.ListGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationChannelNumbers(self, request):
        """用于查询组织目录下的未添加到实时上云计划中的通道数量

        :param request: Request instance for ListOrganizationChannelNumbers.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelNumbersRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelNumbersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationChannelNumbers", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationChannelNumbersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationChannels(self, request):
        """用于查询组织目录下的通道列表

        :param request: Request instance for ListOrganizationChannels.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationChannels", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordBackupPlanDevices(self, request):
        """用于查询录像上云计划下的设备通道列表。

        :param request: Request instance for ListRecordBackupPlanDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordBackupPlanDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordBackupPlanDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordBackupPlans(self, request):
        """用于查询录像上云计划列表。

        :param request: Request instance for ListRecordBackupPlans.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlansRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordBackupTemplates(self, request):
        """用于查询录像上云模板列表。

        :param request: Request instance for ListRecordBackupTemplates.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupTemplatesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordBackupTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordBackupTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordPlanChannels(self, request):
        """用于查询用户下所有实时上云计划中的通道列表

        :param request: Request instance for ListRecordPlanChannels.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanChannelsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordPlanChannels", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordPlanChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordPlanDevices(self, request):
        """用于查询实时上云计划下的设备通道列表

        :param request: Request instance for ListRecordPlanDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordPlanDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordPlanDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordPlans(self, request):
        """用于查询实时上云计划列表

        :param request: Request instance for ListRecordPlans.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordPlansRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordPlans", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordRetrieveTasks(self, request):
        """用于查询取回任务列表

        :param request: Request instance for ListRecordRetrieveTasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordRetrieveTasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordRetrieveTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordRetrieveTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordRetrieveTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordTemplates(self, request):
        """用于查询实时上云模板列表

        :param request: Request instance for ListRecordTemplates.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSubTasks(self, request):
        """用于查询任务的子任务列表

        :param request: Request instance for ListSubTasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListSubTasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListSubTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSubTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListSubTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTasks(self, request):
        """用于查询批量任务和简单任务列表

        :param request: Request instance for ListTasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListTasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PlayRecord(self, request):
        """用于获取设备本地录像 URL 地址。

        :param request: Request instance for PlayRecord.
        :type request: :class:`tencentcloud.iss.v20230517.models.PlayRecordRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.PlayRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PlayRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PlayRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryForbidPlayChannelList(self, request):
        """查询禁播通道列表

        :param request: Request instance for QueryForbidPlayChannelList.
        :type request: :class:`tencentcloud.iss.v20230517.models.QueryForbidPlayChannelListRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.QueryForbidPlayChannelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryForbidPlayChannelList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryForbidPlayChannelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshDeviceChannel(self, request):
        """用于刷新国标设备的通道（接口调用后，触发向设备请求通道列表，新增的通道入库，设备上已删除的通道需自行删除、后台不自动删除）。

        :param request: Request instance for RefreshDeviceChannel.
        :type request: :class:`tencentcloud.iss.v20230517.models.RefreshDeviceChannelRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.RefreshDeviceChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshDeviceChannel", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshDeviceChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetForbidPlayChannels(self, request):
        """禁止主、子账号对视频通道的实况预览

        :param request: Request instance for SetForbidPlayChannels.
        :type request: :class:`tencentcloud.iss.v20230517.models.SetForbidPlayChannelsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.SetForbidPlayChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetForbidPlayChannels", params, headers=headers)
            response = json.loads(body)
            model = models.SetForbidPlayChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAITask(self, request):
        """更新AI任务

        :param request: Request instance for UpdateAITask.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateAITaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateAITaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAITask", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAITaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAITaskStatus(self, request):
        """更新 AI 任务状态

        :param request: Request instance for UpdateAITaskStatus.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateAITaskStatusRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateAITaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAITaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAITaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDeviceOrganization(self, request):
        """用于批量更改设备的组织。

        :param request: Request instance for UpdateDeviceOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDeviceStatus(self, request):
        """用于启用/禁用设备，禁用后拒绝设备注册。

        :param request: Request instance for UpdateDeviceStatus.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceStatusRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGateway(self, request):
        """用于修改网关信息（支持对网关名称和描述的修改）。

        :param request: Request instance for UpdateGateway.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateGatewayRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGateway", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganization(self, request):
        """用于修改组织。

        :param request: Request instance for UpdateOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordBackupPlan(self, request):
        """用于修改录像上云计划。

        :param request: Request instance for UpdateRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordBackupTemplate(self, request):
        """用于修改录像上云模板。

        :param request: Request instance for UpdateRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordPlan(self, request):
        """用于修改实时上云计划

        :param request: Request instance for UpdateRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordTemplate(self, request):
        """用于修改实时上云模板

        :param request: Request instance for UpdateRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserDevice(self, request):
        """用于修改设备的配置信息。

        :param request: Request instance for UpdateUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeGateway(self, request):
        """用于网关升级（支持对所有待更新的服务一键升级）。

        :param request: Request instance for UpgradeGateway.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpgradeGatewayRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpgradeGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeGateway", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))