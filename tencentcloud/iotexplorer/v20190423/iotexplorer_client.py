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
from tencentcloud.iotexplorer.v20190423 import models


class IotexplorerClient(AbstractClient):
    _apiVersion = '2019-04-23'
    _endpoint = 'iotexplorer.tencentcloudapi.com'
    _service = 'iotexplorer'


    def ActivateTWeCallLicense(self, request):
        """激活

        :param request: Request instance for ActivateTWeCallLicense.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ActivateTWeCallLicenseRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ActivateTWeCallLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateTWeCallLicense", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateTWeCallLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignTWeCallLicense(self, request):
        """分配License

        :param request: Request instance for AssignTWeCallLicense.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.AssignTWeCallLicenseRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.AssignTWeCallLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignTWeCallLicense", params, headers=headers)
            response = json.loads(body)
            model = models.AssignTWeCallLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindCloudStorageUser(self, request):
        """绑定云存用户

        :param request: Request instance for BindCloudStorageUser.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.BindCloudStorageUserRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.BindCloudStorageUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindCloudStorageUser", params, headers=headers)
            response = json.loads(body)
            model = models.BindCloudStorageUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDevices(self, request):
        """批量绑定子设备

        :param request: Request instance for BindDevices.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.BindDevicesRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.BindDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDevices", params, headers=headers)
            response = json.loads(body)
            model = models.BindDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindProducts(self, request):
        """批量绑定子产品

        :param request: Request instance for BindProducts.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.BindProductsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.BindProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindProducts", params, headers=headers)
            response = json.loads(body)
            model = models.BindProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CallDeviceActionAsync(self, request):
        """提供给用户异步调用设备行为的能力

        :param request: Request instance for CallDeviceActionAsync.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionAsyncRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallDeviceActionAsync", params, headers=headers)
            response = json.loads(body)
            model = models.CallDeviceActionAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CallDeviceActionSync(self, request):
        """为用户提供同步调用设备行为的能力。

        :param request: Request instance for CallDeviceActionSync.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionSyncRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallDeviceActionSync", params, headers=headers)
            response = json.loads(body)
            model = models.CallDeviceActionSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelAssignTWeCallLicense(self, request):
        """取消分配

        :param request: Request instance for CancelAssignTWeCallLicense.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CancelAssignTWeCallLicenseRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CancelAssignTWeCallLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAssignTWeCallLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAssignTWeCallLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFirmwareUpdate(self, request):
        """本接口（CheckFirmwareUpdate）用于查询设备可升级固件版本

        :param request: Request instance for CheckFirmwareUpdate.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CheckFirmwareUpdateRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CheckFirmwareUpdateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFirmwareUpdate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFirmwareUpdateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDeviceData(self, request):
        """根据设备产品ID、设备名称，设置控制设备的属性数据。

        :param request: Request instance for ControlDeviceData.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDeviceData", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDeviceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBatchProduction(self, request):
        """用于新建批量生产设备

        :param request: Request instance for CreateBatchProduction.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateBatchProductionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateBatchProductionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatchProduction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchProductionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudStorageAIService(self, request):
        """开通设备云存AI分析服务

        :param request: Request instance for CreateCloudStorageAIService.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateCloudStorageAIServiceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateCloudStorageAIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudStorageAIService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudStorageAIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDevice(self, request):
        """创建设备

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateDeviceResponse`

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


    def CreateExternalSourceAIServiceTask(self, request):
        """创建外部视频 AI 分析任务

        :param request: Request instance for CreateExternalSourceAIServiceTask.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateExternalSourceAIServiceTaskRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateExternalSourceAIServiceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExternalSourceAIServiceTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExternalSourceAIServiceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFenceBind(self, request):
        """创建围栏绑定信息

        :param request: Request instance for CreateFenceBind.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateFenceBindRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateFenceBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFenceBind", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFenceBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIotVideoCloudStorage(self, request):
        """开通云存服务

        :param request: Request instance for CreateIotVideoCloudStorage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateIotVideoCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateIotVideoCloudStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIotVideoCloudStorage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIotVideoCloudStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoRaFrequency(self, request):
        """创建 LoRa 自定义频点

        :param request: Request instance for CreateLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoRaFrequency", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoRaFrequencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoRaGateway(self, request):
        """创建新 LoRa 网关设备接口

        :param request: Request instance for CreateLoRaGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoRaGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoRaGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePositionFence(self, request):
        """创建围栏

        :param request: Request instance for CreatePositionFence.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreatePositionFenceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreatePositionFenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePositionFence", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePositionFenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePositionSpace(self, request):
        """创建位置空间

        :param request: Request instance for CreatePositionSpace.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreatePositionSpaceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreatePositionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePositionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePositionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        """为用户提供新建项目的能力，用于集中管理产品和应用。

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectResponse`

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


    def CreateStudioProduct(self, request):
        """为用户提供新建产品的能力，用于管理用户的设备

        :param request: Request instance for CreateStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStudioProduct", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStudioProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTRTCSignaturesWithRoomId(self, request):
        """创建TRTC通话参数

        :param request: Request instance for CreateTRTCSignaturesWithRoomId.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTRTCSignaturesWithRoomIdRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTRTCSignaturesWithRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTRTCSignaturesWithRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTRTCSignaturesWithRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopicPolicy(self, request):
        """本接口（CreateTopicPolicy）用于创建一个Topic

        :param request: Request instance for CreateTopicPolicy.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopicPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopicRule(self, request):
        """创建规则

        :param request: Request instance for CreateTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudStorageEvent(self, request):
        """删除云存事件

        :param request: Request instance for DeleteCloudStorageEvent.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteCloudStorageEventRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteCloudStorageEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudStorageEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudStorageEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevice(self, request):
        """删除设备

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevices(self, request):
        """批量删除设备

        :param request: Request instance for DeleteDevices.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDevicesRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFenceBind(self, request):
        """删除围栏绑定信息

        :param request: Request instance for DeleteFenceBind.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteFenceBindRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteFenceBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFenceBind", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFenceBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoRaFrequency(self, request):
        """提供删除LoRa自定义频点的能力

        :param request: Request instance for DeleteLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoRaFrequency", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoRaFrequencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoRaGateway(self, request):
        """删除  LoRa 网关的接口

        :param request: Request instance for DeleteLoRaGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoRaGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoRaGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePositionFence(self, request):
        """删除围栏

        :param request: Request instance for DeletePositionFence.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeletePositionFenceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeletePositionFenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePositionFence", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePositionFenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePositionSpace(self, request):
        """删除位置空间

        :param request: Request instance for DeletePositionSpace.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeletePositionSpaceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeletePositionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePositionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePositionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        """提供删除某个项目的能力

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectResponse`

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


    def DeleteStudioProduct(self, request):
        """提供删除某个项目下产品的能力

        :param request: Request instance for DeleteStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStudioProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStudioProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopicPolicy(self, request):
        """本接口（DeleteTopicPolicy）用于删除Topic

        :param request: Request instance for DeleteTopicPolicy.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopicPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopicRule(self, request):
        """删除规则

        :param request: Request instance for DeleteTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchProduction(self, request):
        """获取量产详情信息。

        :param request: Request instance for DescribeBatchProduction.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeBatchProductionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeBatchProductionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchProduction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchProductionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBindedProducts(self, request):
        """获取网关产品已经绑定的子产品

        :param request: Request instance for DescribeBindedProducts.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeBindedProductsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeBindedProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindedProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindedProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorage(self, request):
        """获取设备云存服务详情

        :param request: Request instance for DescribeCloudStorage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageAIService(self, request):
        """查询指定设备的云存 AI 服务开通状态与参数配置

        :param request: Request instance for DescribeCloudStorageAIService.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageAIService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageAIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageAIServiceCallback(self, request):
        """查询云存AI分析回调配置

        :param request: Request instance for DescribeCloudStorageAIServiceCallback.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceCallbackRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageAIServiceCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageAIServiceCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageAIServiceTask(self, request):
        """查询指定的云存 AI 分析任务

        :param request: Request instance for DescribeCloudStorageAIServiceTask.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceTaskRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageAIServiceTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageAIServiceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageAIServiceTasks(self, request):
        """查询指定设备的云存 AI 分析任务列表

        :param request: Request instance for DescribeCloudStorageAIServiceTasks.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceTasksRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageAIServiceTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageAIServiceTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageAIServiceTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageDate(self, request):
        """获取具有云存的日期

        :param request: Request instance for DescribeCloudStorageDate.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageDateRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageDate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageEvents(self, request):
        """拉取云存事件列表

        :param request: Request instance for DescribeCloudStorageEvents.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageEventsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageMultiThumbnail(self, request):
        """拉取多个云存事件缩略图

        :param request: Request instance for DescribeCloudStorageMultiThumbnail.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageMultiThumbnailRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageMultiThumbnailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageMultiThumbnail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageMultiThumbnailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageOrder(self, request):
        """查询云存服务详情

        :param request: Request instance for DescribeCloudStorageOrder.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageOrderRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStoragePackageConsumeDetails(self, request):
        """获取云存套餐包消耗详细记录

        :param request: Request instance for DescribeCloudStoragePackageConsumeDetails.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStoragePackageConsumeDetailsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStoragePackageConsumeDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStoragePackageConsumeDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStoragePackageConsumeDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStoragePackageConsumeStats(self, request):
        """获取云存套餐包消耗统计

        :param request: Request instance for DescribeCloudStoragePackageConsumeStats.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStoragePackageConsumeStatsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStoragePackageConsumeStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStoragePackageConsumeStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStoragePackageConsumeStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageStreamData(self, request):
        """获取设备图片流数据

        :param request: Request instance for DescribeCloudStorageStreamData.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageStreamDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageStreamDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageStreamData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageStreamDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageThumbnail(self, request):
        """拉取云存事件缩略图

        :param request: Request instance for DescribeCloudStorageThumbnail.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageThumbnailRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageThumbnailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageThumbnail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageThumbnailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageThumbnailList(self, request):
        """批量拉取云存事件缩略图

        :param request: Request instance for DescribeCloudStorageThumbnailList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageThumbnailListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageThumbnailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageThumbnailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageThumbnailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageTime(self, request):
        """获取某一天云存时间轴

        :param request: Request instance for DescribeCloudStorageTime.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageTimeRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudStorageUsers(self, request):
        """拉取云存用户列表

        :param request: Request instance for DescribeCloudStorageUsers.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageUsersRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeCloudStorageUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudStorageUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudStorageUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevice(self, request):
        """用于查看某个设备的详细信息

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceBindGateway(self, request):
        """查询设备绑定的网关设备

        :param request: Request instance for DescribeDeviceBindGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceBindGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceBindGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceBindGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceBindGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceData(self, request):
        """根据设备产品ID、设备名称，获取设备上报的属性数据。

        :param request: Request instance for DescribeDeviceData.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceDataHistory(self, request):
        """获取设备在指定时间范围内上报的历史数据。

        :param request: Request instance for DescribeDeviceDataHistory.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceDataHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceDataHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceFirmWare(self, request):
        """获取设备固件信息

        :param request: Request instance for DescribeDeviceFirmWare.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceFirmWareRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceFirmWareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceFirmWare", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceFirmWareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceFirmwares(self, request):
        """获取设备当前固件信息

        :param request: Request instance for DescribeDeviceFirmwares.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceFirmwaresRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceFirmwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceFirmwares", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceFirmwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceLocationSolve(self, request):
        """获取实时位置解析

        :param request: Request instance for DescribeDeviceLocationSolve.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceLocationSolveRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceLocationSolveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceLocationSolve", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceLocationSolveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePackages(self, request):
        """根据设备信息拉取有效套餐列表

        :param request: Request instance for DescribeDevicePackages.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDevicePackagesRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDevicePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePositionList(self, request):
        """获取设备位置列表

        :param request: Request instance for DescribeDevicePositionList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDevicePositionListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDevicePositionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePositionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePositionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFenceBindList(self, request):
        """获取围栏绑定信息列表

        :param request: Request instance for DescribeFenceBindList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFenceBindListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFenceBindListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFenceBindList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFenceBindListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFenceEventList(self, request):
        """获取围栏告警事件列表

        :param request: Request instance for DescribeFenceEventList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFenceEventListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFenceEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFenceEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFenceEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmware(self, request):
        """查询固件信息

        :param request: Request instance for DescribeFirmware.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmware", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmwareTask(self, request):
        """查询固件升级任务列表

        :param request: Request instance for DescribeFirmwareTask.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmwareUpdateStatus(self, request):
        """本接口（DescribeFirmwareUpdateStatus）用于查询设备固件升级状态及进度。

        :param request: Request instance for DescribeFirmwareUpdateStatus.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareUpdateStatusRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareUpdateStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareUpdateStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareUpdateStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayBindDevices(self, request):
        """获取网关绑定的子设备列表

        :param request: Request instance for DescribeGatewayBindDevices.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeGatewayBindDevicesRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeGatewayBindDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayBindDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayBindDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewaySubDeviceList(self, request):
        """查询绑定到家庭的网关设备的子设备列表

        :param request: Request instance for DescribeGatewaySubDeviceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeGatewaySubDeviceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeGatewaySubDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewaySubDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewaySubDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewaySubProducts(self, request):
        """用于获取网关可绑定或解绑的子产品

        :param request: Request instance for DescribeGatewaySubProducts.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeGatewaySubProductsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeGatewaySubProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewaySubProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewaySubProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        """公共实例过期时间 0001-01-01T00:00:00Z，公共实例是永久有效

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoRaFrequency(self, request):
        """提供查询LoRa自定义频点详情的能力

        :param request: Request instance for DescribeLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoRaFrequency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoRaFrequencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelDefinition(self, request):
        """查询产品配置的数据模板信息

        :param request: Request instance for DescribeModelDefinition.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelDefinition", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelDefinitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackageConsumeTask(self, request):
        """查询套餐消耗记录详情

        :param request: Request instance for DescribePackageConsumeTask.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribePackageConsumeTaskRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribePackageConsumeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackageConsumeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackageConsumeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackageConsumeTasks(self, request):
        """查询套餐消耗记录列表

        :param request: Request instance for DescribePackageConsumeTasks.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribePackageConsumeTasksRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribePackageConsumeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackageConsumeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackageConsumeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePositionFenceList(self, request):
        """获取围栏列表

        :param request: Request instance for DescribePositionFenceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribePositionFenceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribePositionFenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePositionFenceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePositionFenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductCloudStorageAIService(self, request):
        """查询指定产品的云存 AI 服务开通状态

        :param request: Request instance for DescribeProductCloudStorageAIService.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProductCloudStorageAIServiceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProductCloudStorageAIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductCloudStorageAIService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductCloudStorageAIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProject(self, request):
        """查询项目详情

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceFenceEventList(self, request):
        """获取位置空间中围栏告警事件列表

        :param request: Request instance for DescribeSpaceFenceEventList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeSpaceFenceEventListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeSpaceFenceEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceFenceEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceFenceEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStudioProduct(self, request):
        """提供查看产品详细信息的能力，包括产品的ID、数据协议、认证类型等重要参数

        :param request: Request instance for DescribeStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStudioProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStudioProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicPolicy(self, request):
        """本接口（DescribeTopicPolicy）用于查看Topic详细信息

        :param request: Request instance for DescribeTopicPolicy.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicRule(self, request):
        """获取规则信息

        :param request: Request instance for DescribeTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DirectBindDeviceInFamily(self, request):
        """直接绑定设备和家庭

        :param request: Request instance for DirectBindDeviceInFamily.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DirectBindDeviceInFamilyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DirectBindDeviceInFamilyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DirectBindDeviceInFamily", params, headers=headers)
            response = json.loads(body)
            model = models.DirectBindDeviceInFamilyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableTopicRule(self, request):
        """禁用规则

        :param request: Request instance for DisableTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DisableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DisableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.DisableTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismissRoomByStrRoomIdFromTRTC(self, request):
        """解散TRTC房间

        :param request: Request instance for DismissRoomByStrRoomIdFromTRTC.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DismissRoomByStrRoomIdFromTRTCRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DismissRoomByStrRoomIdFromTRTCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoomByStrRoomIdFromTRTC", params, headers=headers)
            response = json.loads(body)
            model = models.DismissRoomByStrRoomIdFromTRTCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTopicRule(self, request):
        """启用规则

        :param request: Request instance for EnableTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.EnableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.EnableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenSingleDeviceSignatureOfPublic(self, request):
        """无

        :param request: Request instance for GenSingleDeviceSignatureOfPublic.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GenSingleDeviceSignatureOfPublicRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GenSingleDeviceSignatureOfPublicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenSingleDeviceSignatureOfPublic", params, headers=headers)
            response = json.loads(body)
            model = models.GenSingleDeviceSignatureOfPublicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateCloudStorageAIServiceTaskFileURL(self, request):
        """获取云存 AI 分析任务输出文件的下载地址

        :param request: Request instance for GenerateCloudStorageAIServiceTaskFileURL.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GenerateCloudStorageAIServiceTaskFileURLRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GenerateCloudStorageAIServiceTaskFileURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateCloudStorageAIServiceTaskFileURL", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateCloudStorageAIServiceTaskFileURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateSignedVideoURL(self, request):
        """获取视频防盗链播放URL

        :param request: Request instance for GenerateSignedVideoURL.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GenerateSignedVideoURLRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GenerateSignedVideoURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateSignedVideoURL", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateSignedVideoURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAuthMiniProgramAppList(self, request):
        """查询小程序列表

        :param request: Request instance for GetAuthMiniProgramAppList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetAuthMiniProgramAppListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetAuthMiniProgramAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAuthMiniProgramAppList", params, headers=headers)
            response = json.loads(body)
            model = models.GetAuthMiniProgramAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetBatchProductionsList(self, request):
        """列出量产数据列表信息。

        :param request: Request instance for GetBatchProductionsList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetBatchProductionsListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetBatchProductionsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBatchProductionsList", params, headers=headers)
            response = json.loads(body)
            model = models.GetBatchProductionsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCOSURL(self, request):
        """本接口（GetCOSURL）用于获取固件COS存储的上传请求URL地址

        :param request: Request instance for GetCOSURL.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetCOSURLRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetCOSURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCOSURL", params, headers=headers)
            response = json.loads(body)
            model = models.GetCOSURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceList(self, request):
        """用于查询某个产品下的设备列表

        :param request: Request instance for GetDeviceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceLocationHistory(self, request):
        """获取设备历史位置

        :param request: Request instance for GetDeviceLocationHistory.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceLocationHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceLocationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceLocationHistory", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceLocationHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceSumStatistics(self, request):
        """拉取设备统计汇总数据

        :param request: Request instance for GetDeviceSumStatistics.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceSumStatisticsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceSumStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceSumStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceSumStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFamilyDeviceUserList(self, request):
        """用于获取设备绑定的用户列表

        :param request: Request instance for GetFamilyDeviceUserList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetFamilyDeviceUserListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetFamilyDeviceUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFamilyDeviceUserList", params, headers=headers)
            response = json.loads(body)
            model = models.GetFamilyDeviceUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGatewaySubDeviceList(self, request):
        """获取指定网关设备的子设备列表

        :param request: Request instance for GetGatewaySubDeviceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetGatewaySubDeviceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetGatewaySubDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGatewaySubDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetGatewaySubDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLoRaGatewayList(self, request):
        """获取 LoRa 网关列表接口

        :param request: Request instance for GetLoRaGatewayList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetLoRaGatewayListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetLoRaGatewayListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLoRaGatewayList", params, headers=headers)
            response = json.loads(body)
            model = models.GetLoRaGatewayListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPositionSpaceList(self, request):
        """获取位置空间列表

        :param request: Request instance for GetPositionSpaceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetPositionSpaceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetPositionSpaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPositionSpaceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetPositionSpaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProjectList(self, request):
        """提供查询用户所创建的项目列表查询功能。

        :param request: Request instance for GetProjectList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.GetProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetStudioProductList(self, request):
        """提供查询某个项目下所有产品信息的能力。

        :param request: Request instance for GetStudioProductList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStudioProductList", params, headers=headers)
            response = json.loads(body)
            model = models.GetStudioProductListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTWeCallActiveStatus(self, request):
        """查询激活状态

        :param request: Request instance for GetTWeCallActiveStatus.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetTWeCallActiveStatusRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetTWeCallActiveStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTWeCallActiveStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetTWeCallActiveStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTWeCallPkgList(self, request):
        """查询TWeCall包列表

        :param request: Request instance for GetTWeCallPkgList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetTWeCallPkgListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetTWeCallPkgListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTWeCallPkgList", params, headers=headers)
            response = json.loads(body)
            model = models.GetTWeCallPkgListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTopicRuleList(self, request):
        """获取规则列表

        :param request: Request instance for GetTopicRuleList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetTopicRuleListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetTopicRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTopicRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.GetTopicRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWechatDeviceTicket(self, request):
        """查询微信设备授权票据

        :param request: Request instance for GetWechatDeviceTicket.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetWechatDeviceTicketRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetWechatDeviceTicketResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWechatDeviceTicket", params, headers=headers)
            response = json.loads(body)
            model = models.GetWechatDeviceTicketResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InheritCloudStorageUser(self, request):
        """继承云存用户

        :param request: Request instance for InheritCloudStorageUser.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.InheritCloudStorageUserRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.InheritCloudStorageUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InheritCloudStorageUser", params, headers=headers)
            response = json.loads(body)
            model = models.InheritCloudStorageUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeExternalSourceAIServiceTask(self, request):
        """创建外部视频 AI 分析任务

        :param request: Request instance for InvokeExternalSourceAIServiceTask.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.InvokeExternalSourceAIServiceTaskRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.InvokeExternalSourceAIServiceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeExternalSourceAIServiceTask", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeExternalSourceAIServiceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEventHistory(self, request):
        """获取设备的历史事件

        :param request: Request instance for ListEventHistory.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ListEventHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ListEventHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEventHistory", params, headers=headers)
            response = json.loads(body)
            model = models.ListEventHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListFirmwares(self, request):
        """本接口（ListFirmwares）用于获取固件列表

        :param request: Request instance for ListFirmwares.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ListFirmwaresRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ListFirmwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFirmwares", params, headers=headers)
            response = json.loads(body)
            model = models.ListFirmwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTopicPolicy(self, request):
        """本接口（ListTopicPolicy）用于获取Topic列表

        :param request: Request instance for ListTopicPolicy.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ListTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ListTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTopicPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ListTopicPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudStorageAIService(self, request):
        """修改指定设备的云存 AI 服务参数配置

        :param request: Request instance for ModifyCloudStorageAIService.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyCloudStorageAIServiceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyCloudStorageAIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudStorageAIService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudStorageAIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudStorageAIServiceCallback(self, request):
        """修改云存AI分析回调配置

        :param request: Request instance for ModifyCloudStorageAIServiceCallback.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyCloudStorageAIServiceCallbackRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyCloudStorageAIServiceCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudStorageAIServiceCallback", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudStorageAIServiceCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFenceBind(self, request):
        """更新围栏绑定信息

        :param request: Request instance for ModifyFenceBind.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyFenceBindRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyFenceBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFenceBind", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFenceBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoRaFrequency(self, request):
        """修改LoRa自定义频点

        :param request: Request instance for ModifyLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoRaFrequency", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoRaFrequencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoRaGateway(self, request):
        """修改 LoRa 网关信息

        :param request: Request instance for ModifyLoRaGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoRaGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoRaGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModelDefinition(self, request):
        """提供修改产品的数据模板的能力

        :param request: Request instance for ModifyModelDefinition.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModelDefinition", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelDefinitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPositionFence(self, request):
        """更新围栏

        :param request: Request instance for ModifyPositionFence.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyPositionFenceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyPositionFenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPositionFence", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPositionFenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPositionSpace(self, request):
        """更新位置空间

        :param request: Request instance for ModifyPositionSpace.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyPositionSpaceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyPositionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPositionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPositionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProductCloudStorageAIService(self, request):
        """修改指定产品的云存 AI 服务开通状态

        :param request: Request instance for ModifyProductCloudStorageAIService.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProductCloudStorageAIServiceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProductCloudStorageAIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProductCloudStorageAIService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProductCloudStorageAIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        """修改项目

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectResponse`

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


    def ModifySpaceProperty(self, request):
        """更新位置空间产品属性

        :param request: Request instance for ModifySpaceProperty.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifySpacePropertyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifySpacePropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpaceProperty", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpacePropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStudioProduct(self, request):
        """提供修改产品的名称和描述等信息的能力，对于已发布产品不允许进行修改。

        :param request: Request instance for ModifyStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStudioProduct", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStudioProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopicPolicy(self, request):
        """本接口（UpdateTopicPolicy）用于更新Topic信息

        :param request: Request instance for ModifyTopicPolicy.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopicPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopicRule(self, request):
        """修改规则

        :param request: Request instance for ModifyTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishBroadcastMessage(self, request):
        """发布广播消息

        :param request: Request instance for PublishBroadcastMessage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.PublishBroadcastMessageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.PublishBroadcastMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishBroadcastMessage", params, headers=headers)
            response = json.loads(body)
            model = models.PublishBroadcastMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishFirmwareUpdateMessage(self, request):
        """本接口（PublishFirmwareUpdateMessage）用于用户确认升级后，云端向设备发起固件升级请求。

        :param request: Request instance for PublishFirmwareUpdateMessage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.PublishFirmwareUpdateMessageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.PublishFirmwareUpdateMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishFirmwareUpdateMessage", params, headers=headers)
            response = json.loads(body)
            model = models.PublishFirmwareUpdateMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishMessage(self, request):
        """本接口（PublishMessage）用于使用自定义透传协议进行设备远控

        :param request: Request instance for PublishMessage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.PublishMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishMessage", params, headers=headers)
            response = json.loads(body)
            model = models.PublishMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishRRPCMessage(self, request):
        """下发RRPC消息

        :param request: Request instance for PublishRRPCMessage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.PublishRRPCMessageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.PublishRRPCMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishRRPCMessage", params, headers=headers)
            response = json.loads(body)
            model = models.PublishRRPCMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseStudioProduct(self, request):
        """产品开发完成并测试通过后，通过发布产品将产品设置为发布状态

        :param request: Request instance for ReleaseStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseStudioProduct", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseStudioProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUserByRoomIdFromTRTC(self, request):
        """TRTC操作，将用户从房间移出

        :param request: Request instance for RemoveUserByRoomIdFromTRTC.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.RemoveUserByRoomIdFromTRTCRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.RemoveUserByRoomIdFromTRTCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserByRoomIdFromTRTC", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserByRoomIdFromTRTCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetCloudStorage(self, request):
        """重置云存服务

        :param request: Request instance for ResetCloudStorage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ResetCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ResetCloudStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetCloudStorage", params, headers=headers)
            response = json.loads(body)
            model = models.ResetCloudStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetCloudStorageAIService(self, request):
        """重置指定设备的云存 AI 服务

        :param request: Request instance for ResetCloudStorageAIService.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ResetCloudStorageAIServiceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ResetCloudStorageAIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetCloudStorageAIService", params, headers=headers)
            response = json.loads(body)
            model = models.ResetCloudStorageAIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetCloudStorageEvent(self, request):
        """重置云存事件

        :param request: Request instance for ResetCloudStorageEvent.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ResetCloudStorageEventRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ResetCloudStorageEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetCloudStorageEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ResetCloudStorageEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchPositionSpace(self, request):
        """搜索位置空间

        :param request: Request instance for SearchPositionSpace.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchPositionSpaceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchPositionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchPositionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.SearchPositionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchStudioProduct(self, request):
        """提供根据产品名称查找产品的能力

        :param request: Request instance for SearchStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchStudioProduct", params, headers=headers)
            response = json.loads(body)
            model = models.SearchStudioProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchTopicRule(self, request):
        """搜索规则

        :param request: Request instance for SearchTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchTopicRule", params, headers=headers)
            response = json.loads(body)
            model = models.SearchTopicRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransferCloudStorage(self, request):
        """转移云存服务

        :param request: Request instance for TransferCloudStorage.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.TransferCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TransferCloudStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferCloudStorage", params, headers=headers)
            response = json.loads(body)
            model = models.TransferCloudStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindDevices(self, request):
        """批量解绑子设备

        :param request: Request instance for UnbindDevices.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UnbindDevicesRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UnbindDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindDevices", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindProducts(self, request):
        """批量解绑子产品

        :param request: Request instance for UnbindProducts.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UnbindProductsRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UnbindProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindProducts", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDeviceTWeCallAuthorizeStatus(self, request):
        """更新用户对设备的TweCall授权状态

        :param request: Request instance for UpdateDeviceTWeCallAuthorizeStatus.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateDeviceTWeCallAuthorizeStatusRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateDeviceTWeCallAuthorizeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceTWeCallAuthorizeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceTWeCallAuthorizeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDevicesEnableState(self, request):
        """批量禁用启用设备

        :param request: Request instance for UpdateDevicesEnableState.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateDevicesEnableStateRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateDevicesEnableStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevicesEnableState", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDevicesEnableStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFirmware(self, request):
        """本接口（UpdateFirmware）用于对指定设备发起固件升级请求

        :param request: Request instance for UpdateFirmware.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateFirmwareRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFirmware", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFirmwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadFirmware(self, request):
        """本接口（UploadFirmware）用于创建设备固件版本信息，在平台用于固件版本升级、固件资源下发等。

        :param request: Request instance for UploadFirmware.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UploadFirmwareRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UploadFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFirmware", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFirmwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))