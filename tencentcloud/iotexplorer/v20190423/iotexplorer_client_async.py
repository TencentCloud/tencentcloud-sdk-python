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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.iotexplorer.v20190423 import models
from typing import Dict


class IotexplorerClient(AbstractClient):
    _apiVersion = '2019-04-23'
    _endpoint = 'iotexplorer.tencentcloudapi.com'
    _service = 'iotexplorer'

    async def ActivateTWeCallLicense(
            self,
            request: models.ActivateTWeCallLicenseRequest,
            opts: Dict = None,
    ) -> models.ActivateTWeCallLicenseResponse:
        """
        激活
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateTWeCallLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateTWeCallLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateTWeSeeRecognitionTask(
            self,
            request: models.BatchCreateTWeSeeRecognitionTaskRequest,
            opts: Dict = None,
    ) -> models.BatchCreateTWeSeeRecognitionTaskResponse:
        """
        批量同步执行 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateTWeSeeRecognitionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateTWeSeeRecognitionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchInvokeTWeSeeRecognitionTask(
            self,
            request: models.BatchInvokeTWeSeeRecognitionTaskRequest,
            opts: Dict = None,
    ) -> models.BatchInvokeTWeSeeRecognitionTaskResponse:
        """
        批量同步执行 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchInvokeTWeSeeRecognitionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchInvokeTWeSeeRecognitionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchUpdateFirmware(
            self,
            request: models.BatchUpdateFirmwareRequest,
            opts: Dict = None,
    ) -> models.BatchUpdateFirmwareResponse:
        """
        本接口（BatchUpdateFirmware）用于批量更新设备固件
        """
        
        kwargs = {}
        kwargs["action"] = "BatchUpdateFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchUpdateFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindCloudStorageUser(
            self,
            request: models.BindCloudStorageUserRequest,
            opts: Dict = None,
    ) -> models.BindCloudStorageUserResponse:
        """
        绑定云存用户
        """
        
        kwargs = {}
        kwargs["action"] = "BindCloudStorageUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindCloudStorageUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDevices(
            self,
            request: models.BindDevicesRequest,
            opts: Dict = None,
    ) -> models.BindDevicesResponse:
        """
        批量绑定子设备
        """
        
        kwargs = {}
        kwargs["action"] = "BindDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindProducts(
            self,
            request: models.BindProductsRequest,
            opts: Dict = None,
    ) -> models.BindProductsResponse:
        """
        批量绑定子产品。
        """
        
        kwargs = {}
        kwargs["action"] = "BindProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindTWeTalkAIBot(
            self,
            request: models.BindTWeTalkAIBotRequest,
            opts: Dict = None,
    ) -> models.BindTWeTalkAIBotResponse:
        """
        用于绑定一个产品和智能体。
        """
        
        kwargs = {}
        kwargs["action"] = "BindTWeTalkAIBot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindTWeTalkAIBotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallDeviceActionAsync(
            self,
            request: models.CallDeviceActionAsyncRequest,
            opts: Dict = None,
    ) -> models.CallDeviceActionAsyncResponse:
        """
        提供给用户异步调用设备行为的能力
        """
        
        kwargs = {}
        kwargs["action"] = "CallDeviceActionAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallDeviceActionAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallDeviceActionSync(
            self,
            request: models.CallDeviceActionSyncRequest,
            opts: Dict = None,
    ) -> models.CallDeviceActionSyncResponse:
        """
        为用户提供同步调用设备行为的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "CallDeviceActionSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallDeviceActionSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelAssignTWeCallLicense(
            self,
            request: models.CancelAssignTWeCallLicenseRequest,
            opts: Dict = None,
    ) -> models.CancelAssignTWeCallLicenseResponse:
        """
        业务已下线

        取消分配
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAssignTWeCallLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAssignTWeCallLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeP2PRoute(
            self,
            request: models.ChangeP2PRouteRequest,
            opts: Dict = None,
    ) -> models.ChangeP2PRouteResponse:
        """
        p2p路线切换（此接口目前处于内测接口，可以联系申请加白 ）
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeP2PRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeP2PRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFirmwareUpdate(
            self,
            request: models.CheckFirmwareUpdateRequest,
            opts: Dict = None,
    ) -> models.CheckFirmwareUpdateResponse:
        """
        本接口（CheckFirmwareUpdate）用于查询设备可升级固件版本
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFirmwareUpdate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFirmwareUpdateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDeviceData(
            self,
            request: models.ControlDeviceDataRequest,
            opts: Dict = None,
    ) -> models.ControlDeviceDataResponse:
        """
        根据设备产品ID、设备名称，设置控制设备的属性数据。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDeviceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDeviceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAISearchTaskAsync(
            self,
            request: models.CreateAISearchTaskAsyncRequest,
            opts: Dict = None,
    ) -> models.CreateAISearchTaskAsyncResponse:
        """
        创建视频语义异步搜索任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAISearchTaskAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAISearchTaskAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBatchProduction(
            self,
            request: models.CreateBatchProductionRequest,
            opts: Dict = None,
    ) -> models.CreateBatchProductionResponse:
        """
        用于新建批量生产设备
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBatchProduction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBatchProductionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudStorageAIService(
            self,
            request: models.CreateCloudStorageAIServiceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudStorageAIServiceResponse:
        """
        开通设备云存AI分析服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudStorageAIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudStorageAIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudStorageAIServiceTask(
            self,
            request: models.CreateCloudStorageAIServiceTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCloudStorageAIServiceTaskResponse:
        """
        创建设备云存 AI 分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudStorageAIServiceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudStorageAIServiceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevice(
            self,
            request: models.CreateDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceResponse:
        """
        创建设备
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceChannel(
            self,
            request: models.CreateDeviceChannelRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceChannelResponse:
        """
        创建设备通道
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExternalSourceAIServiceTask(
            self,
            request: models.CreateExternalSourceAIServiceTaskRequest,
            opts: Dict = None,
    ) -> models.CreateExternalSourceAIServiceTaskResponse:
        """
        创建外部视频 AI 分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExternalSourceAIServiceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExternalSourceAIServiceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFenceBind(
            self,
            request: models.CreateFenceBindRequest,
            opts: Dict = None,
    ) -> models.CreateFenceBindResponse:
        """
        > 创建围栏绑定信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFenceBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFenceBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFreeCloudStorage(
            self,
            request: models.CreateFreeCloudStorageRequest,
            opts: Dict = None,
    ) -> models.CreateFreeCloudStorageResponse:
        """
        开通云存卡服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFreeCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFreeCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIotVideoCloudStorage(
            self,
            request: models.CreateIotVideoCloudStorageRequest,
            opts: Dict = None,
    ) -> models.CreateIotVideoCloudStorageResponse:
        """
        开通云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIotVideoCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIotVideoCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoRaFrequency(
            self,
            request: models.CreateLoRaFrequencyRequest,
            opts: Dict = None,
    ) -> models.CreateLoRaFrequencyResponse:
        """
        创建 LoRa 自定义频点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoRaFrequency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoRaFrequencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoRaGateway(
            self,
            request: models.CreateLoRaGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateLoRaGatewayResponse:
        """
        创建新 LoRa 网关设备接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoRaGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoRaGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOtaModule(
            self,
            request: models.CreateOtaModuleRequest,
            opts: Dict = None,
    ) -> models.CreateOtaModuleResponse:
        """
        本接口（CreateOtaModule）用于新建OTA模块
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOtaModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOtaModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePositionFence(
            self,
            request: models.CreatePositionFenceRequest,
            opts: Dict = None,
    ) -> models.CreatePositionFenceResponse:
        """
        创建围栏。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePositionFence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePositionFenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePositionSpace(
            self,
            request: models.CreatePositionSpaceRequest,
            opts: Dict = None,
    ) -> models.CreatePositionSpaceResponse:
        """
        创建位置空间。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePositionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePositionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        为用户提供新建项目的能力，用于集中管理产品和应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStudioProduct(
            self,
            request: models.CreateStudioProductRequest,
            opts: Dict = None,
    ) -> models.CreateStudioProductResponse:
        """
        为用户提供新建产品的能力，用于管理用户的设备
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStudioProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStudioProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTRTCSignaturesWithRoomId(
            self,
            request: models.CreateTRTCSignaturesWithRoomIdRequest,
            opts: Dict = None,
    ) -> models.CreateTRTCSignaturesWithRoomIdResponse:
        """
        创建TRTC通话参数
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTRTCSignaturesWithRoomId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTRTCSignaturesWithRoomIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTWeSeeRecognitionTask(
            self,
            request: models.CreateTWeSeeRecognitionTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTWeSeeRecognitionTaskResponse:
        """
        创建 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTWeSeeRecognitionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTWeSeeRecognitionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTWeSeeRecognitionTaskWithFile(
            self,
            request: models.CreateTWeSeeRecognitionTaskWithFileRequest,
            opts: Dict = None,
    ) -> models.CreateTWeSeeRecognitionTaskWithFileResponse:
        """
        同步执行 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTWeSeeRecognitionTaskWithFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTWeSeeRecognitionTaskWithFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTWeSeeService(
            self,
            request: models.CreateTWeSeeServiceRequest,
            opts: Dict = None,
    ) -> models.CreateTWeSeeServiceResponse:
        """
        开通 TWeSee 后付费服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTWeSeeService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTWeSeeServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTWeTalkAIBot(
            self,
            request: models.CreateTWeTalkAIBotRequest,
            opts: Dict = None,
    ) -> models.CreateTWeTalkAIBotResponse:
        """
        用于新增TWeTalk智能体。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTWeTalkAIBot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTWeTalkAIBotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTWeTalkProductConfig(
            self,
            request: models.CreateTWeTalkProductConfigRequest,
            opts: Dict = None,
    ) -> models.CreateTWeTalkProductConfigResponse:
        """
        用于配置TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTWeTalkProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTWeTalkProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTWeTalkProductConfigV2(
            self,
            request: models.CreateTWeTalkProductConfigV2Request,
            opts: Dict = None,
    ) -> models.CreateTWeTalkProductConfigV2Response:
        """
        用于配置TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTWeTalkProductConfigV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTWeTalkProductConfigV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopicPolicy(
            self,
            request: models.CreateTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateTopicPolicyResponse:
        """
        本接口（CreateTopicPolicy）用于创建一个Topic
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopicRule(
            self,
            request: models.CreateTopicRuleRequest,
            opts: Dict = None,
    ) -> models.CreateTopicRuleResponse:
        """
        创建规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudStorageEvent(
            self,
            request: models.DeleteCloudStorageEventRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudStorageEventResponse:
        """
        删除云存事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudStorageEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudStorageEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        删除设备
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevices(
            self,
            request: models.DeleteDevicesRequest,
            opts: Dict = None,
    ) -> models.DeleteDevicesResponse:
        """
        批量删除设备
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFenceBind(
            self,
            request: models.DeleteFenceBindRequest,
            opts: Dict = None,
    ) -> models.DeleteFenceBindResponse:
        """
        删除围栏绑定信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFenceBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFenceBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoRaFrequency(
            self,
            request: models.DeleteLoRaFrequencyRequest,
            opts: Dict = None,
    ) -> models.DeleteLoRaFrequencyResponse:
        """
        提供删除LoRa自定义频点的能力
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoRaFrequency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoRaFrequencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoRaGateway(
            self,
            request: models.DeleteLoRaGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteLoRaGatewayResponse:
        """
        删除  LoRa 网关的接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoRaGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoRaGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOtaModule(
            self,
            request: models.DeleteOtaModuleRequest,
            opts: Dict = None,
    ) -> models.DeleteOtaModuleResponse:
        """
        本接口（DeleteOtaModule）用于删除OTA模块
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOtaModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOtaModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePositionFence(
            self,
            request: models.DeletePositionFenceRequest,
            opts: Dict = None,
    ) -> models.DeletePositionFenceResponse:
        """
        删除围栏。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePositionFence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePositionFenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePositionSpace(
            self,
            request: models.DeletePositionSpaceRequest,
            opts: Dict = None,
    ) -> models.DeletePositionSpaceResponse:
        """
        删除位置空间。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePositionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePositionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        提供删除某个项目的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStudioProduct(
            self,
            request: models.DeleteStudioProductRequest,
            opts: Dict = None,
    ) -> models.DeleteStudioProductResponse:
        """
        提供删除某个项目下产品的能力
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStudioProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStudioProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTWeTalkAIBot(
            self,
            request: models.DeleteTWeTalkAIBotRequest,
            opts: Dict = None,
    ) -> models.DeleteTWeTalkAIBotResponse:
        """
        用于删除TWeTalk智能体。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTWeTalkAIBot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTWeTalkAIBotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTWeTalkProductConfigV2(
            self,
            request: models.DeleteTWeTalkProductConfigV2Request,
            opts: Dict = None,
    ) -> models.DeleteTWeTalkProductConfigV2Response:
        """
        用于删除配置TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTWeTalkProductConfigV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTWeTalkProductConfigV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopicPolicy(
            self,
            request: models.DeleteTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicPolicyResponse:
        """
        本接口（DeleteTopicPolicy）用于删除Topic
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopicRule(
            self,
            request: models.DeleteTopicRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicRuleResponse:
        """
        删除规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAISearchTaskAsync(
            self,
            request: models.DescribeAISearchTaskAsyncRequest,
            opts: Dict = None,
    ) -> models.DescribeAISearchTaskAsyncResponse:
        """
        获取视频语义异步搜索任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAISearchTaskAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAISearchTaskAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActivateDevice(
            self,
            request: models.DescribeActivateDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeActivateDeviceResponse:
        """
        获取设备激活详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActivateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActivateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActivateLicenseService(
            self,
            request: models.DescribeActivateLicenseServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeActivateLicenseServiceResponse:
        """
        获取增值服务激活码详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActivateLicenseService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActivateLicenseServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchProduction(
            self,
            request: models.DescribeBatchProductionRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchProductionResponse:
        """
        获取量产详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchProduction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchProductionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindedProducts(
            self,
            request: models.DescribeBindedProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeBindedProductsResponse:
        """
        获取网关产品已经绑定的子产品
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindedProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindedProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorage(
            self,
            request: models.DescribeCloudStorageRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageResponse:
        """
        获取设备云存服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageAIService(
            self,
            request: models.DescribeCloudStorageAIServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageAIServiceResponse:
        """
        查询指定设备的云存 AI 服务开通状态与参数配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageAIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageAIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageAIServiceCallback(
            self,
            request: models.DescribeCloudStorageAIServiceCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageAIServiceCallbackResponse:
        """
        查询云存AI分析回调配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageAIServiceCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageAIServiceCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageAIServiceTask(
            self,
            request: models.DescribeCloudStorageAIServiceTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageAIServiceTaskResponse:
        """
        查询指定的云存 AI 分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageAIServiceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageAIServiceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageAIServiceTasks(
            self,
            request: models.DescribeCloudStorageAIServiceTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageAIServiceTasksResponse:
        """
        查询指定设备的云存 AI 分析任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageAIServiceTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageAIServiceTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageDate(
            self,
            request: models.DescribeCloudStorageDateRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageDateResponse:
        """
        获取具有云存的日期
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageEvents(
            self,
            request: models.DescribeCloudStorageEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageEventsResponse:
        """
        拉取云存事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageEventsWithAITasks(
            self,
            request: models.DescribeCloudStorageEventsWithAITasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageEventsWithAITasksResponse:
        """
        拉取云存事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageEventsWithAITasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageEventsWithAITasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageMultiThumbnail(
            self,
            request: models.DescribeCloudStorageMultiThumbnailRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageMultiThumbnailResponse:
        """
        拉取多个云存事件缩略图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageMultiThumbnail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageMultiThumbnailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageOrder(
            self,
            request: models.DescribeCloudStorageOrderRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageOrderResponse:
        """
        查询云存服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStoragePackageConsumeDetails(
            self,
            request: models.DescribeCloudStoragePackageConsumeDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStoragePackageConsumeDetailsResponse:
        """
        获取云存套餐包消耗详细记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStoragePackageConsumeDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStoragePackageConsumeDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStoragePackageConsumeStats(
            self,
            request: models.DescribeCloudStoragePackageConsumeStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStoragePackageConsumeStatsResponse:
        """
        获取云存套餐包消耗统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStoragePackageConsumeStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStoragePackageConsumeStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageStreamData(
            self,
            request: models.DescribeCloudStorageStreamDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageStreamDataResponse:
        """
        获取设备图片流数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageStreamData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageStreamDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageThumbnail(
            self,
            request: models.DescribeCloudStorageThumbnailRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageThumbnailResponse:
        """
        拉取云存事件缩略图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageThumbnail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageThumbnailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageThumbnailList(
            self,
            request: models.DescribeCloudStorageThumbnailListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageThumbnailListResponse:
        """
        批量拉取云存事件缩略图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageThumbnailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageThumbnailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageTime(
            self,
            request: models.DescribeCloudStorageTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageTimeResponse:
        """
        获取某一天云存时间轴
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudStorageUsers(
            self,
            request: models.DescribeCloudStorageUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudStorageUsersResponse:
        """
        拉取云存用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudStorageUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudStorageUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCsReportCountDataInfo(
            self,
            request: models.DescribeCsReportCountDataInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCsReportCountDataInfoResponse:
        """
        获取云存上报统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCsReportCountDataInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCsReportCountDataInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevice(
            self,
            request: models.DescribeDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResponse:
        """
        用于查看某个设备的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceBindGateway(
            self,
            request: models.DescribeDeviceBindGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceBindGatewayResponse:
        """
        查询设备绑定的网关设备
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceBindGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceBindGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceData(
            self,
            request: models.DescribeDeviceDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceDataResponse:
        """
        根据设备产品ID、设备名称，获取设备上报的属性数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceDataHistory(
            self,
            request: models.DescribeDeviceDataHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceDataHistoryResponse:
        """
        获取设备在指定时间范围内上报的历史数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceDataHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceDataHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceFirmWare(
            self,
            request: models.DescribeDeviceFirmWareRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceFirmWareResponse:
        """
        获取设备固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceFirmWare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceFirmWareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceFirmwares(
            self,
            request: models.DescribeDeviceFirmwaresRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceFirmwaresResponse:
        """
        获取设备当前固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceFirmwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceFirmwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePackages(
            self,
            request: models.DescribeDevicePackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePackagesResponse:
        """
        根据设备信息拉取有效套餐列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePositionList(
            self,
            request: models.DescribeDevicePositionListRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePositionListResponse:
        """
        获取设备位置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePositionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePositionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFenceBindList(
            self,
            request: models.DescribeFenceBindListRequest,
            opts: Dict = None,
    ) -> models.DescribeFenceBindListResponse:
        """
        获取围栏绑定信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFenceBindList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFenceBindListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFenceEventList(
            self,
            request: models.DescribeFenceEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeFenceEventListResponse:
        """
        获取围栏告警事件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFenceEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFenceEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmware(
            self,
            request: models.DescribeFirmwareRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareResponse:
        """
        查询固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTask(
            self,
            request: models.DescribeFirmwareTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskResponse:
        """
        查询固件升级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTaskDevices(
            self,
            request: models.DescribeFirmwareTaskDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskDevicesResponse:
        """
        查询固件升级任务的设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTasks(
            self,
            request: models.DescribeFirmwareTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTasksResponse:
        """
        搜索固件升级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareUpdateStatus(
            self,
            request: models.DescribeFirmwareUpdateStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareUpdateStatusResponse:
        """
        本接口（DescribeFirmwareUpdateStatus）用于查询设备固件升级状态及进度。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareUpdateStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareUpdateStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFreeCloudStorageNum(
            self,
            request: models.DescribeFreeCloudStorageNumRequest,
            opts: Dict = None,
    ) -> models.DescribeFreeCloudStorageNumResponse:
        """
        查询云存卡套餐信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFreeCloudStorageNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFreeCloudStorageNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayBindDevices(
            self,
            request: models.DescribeGatewayBindDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayBindDevicesResponse:
        """
        获取网关绑定的子设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayBindDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayBindDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewaySubDeviceList(
            self,
            request: models.DescribeGatewaySubDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewaySubDeviceListResponse:
        """
        查询绑定到家庭的网关设备的子设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewaySubDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewaySubDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewaySubProducts(
            self,
            request: models.DescribeGatewaySubProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewaySubProductsResponse:
        """
        用于获取网关可绑定或解绑的子产品。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewaySubProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewaySubProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        公共实例过期时间 0001-01-01T00:00:00Z，公共实例是永久有效
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoRaFrequency(
            self,
            request: models.DescribeLoRaFrequencyRequest,
            opts: Dict = None,
    ) -> models.DescribeLoRaFrequencyResponse:
        """
        提供查询LoRa自定义频点详情的能力
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoRaFrequency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoRaFrequencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelDefinition(
            self,
            request: models.DescribeModelDefinitionRequest,
            opts: Dict = None,
    ) -> models.DescribeModelDefinitionResponse:
        """
        查询产品配置的数据模板信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelDefinition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelDefinitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeP2PRoute(
            self,
            request: models.DescribeP2PRouteRequest,
            opts: Dict = None,
    ) -> models.DescribeP2PRouteResponse:
        """
        当前p2p线路
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeP2PRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeP2PRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackageConsumeTask(
            self,
            request: models.DescribePackageConsumeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribePackageConsumeTaskResponse:
        """
        查询套餐消耗记录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackageConsumeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackageConsumeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackageConsumeTasks(
            self,
            request: models.DescribePackageConsumeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePackageConsumeTasksResponse:
        """
        查询套餐消耗记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackageConsumeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackageConsumeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePositionFenceList(
            self,
            request: models.DescribePositionFenceListRequest,
            opts: Dict = None,
    ) -> models.DescribePositionFenceListResponse:
        """
        获取围栏列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePositionFenceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePositionFenceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductCloudStorageAIService(
            self,
            request: models.DescribeProductCloudStorageAIServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeProductCloudStorageAIServiceResponse:
        """
        查询指定产品的云存 AI 服务开通状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductCloudStorageAIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductCloudStorageAIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProject(
            self,
            request: models.DescribeProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectResponse:
        """
        查询项目详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceFenceEventList(
            self,
            request: models.DescribeSpaceFenceEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceFenceEventListResponse:
        """
        获取位置空间中围栏告警事件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceFenceEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceFenceEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStudioProduct(
            self,
            request: models.DescribeStudioProductRequest,
            opts: Dict = None,
    ) -> models.DescribeStudioProductResponse:
        """
        提供查看产品详细信息的能力，包括产品的ID、数据协议、认证类型等重要参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStudioProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStudioProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribedTopicPolicy(
            self,
            request: models.DescribeSubscribedTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribedTopicPolicyResponse:
        """
        本接口（DescribeSubscribedTopicPolicy）用于获取设备已订阅Topic列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribedTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribedTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTWeSeeConfig(
            self,
            request: models.DescribeTWeSeeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeTWeSeeConfigResponse:
        """
        拉取 TWeSee 配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTWeSeeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTWeSeeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTWeSeeRecognitionTask(
            self,
            request: models.DescribeTWeSeeRecognitionTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTWeSeeRecognitionTaskResponse:
        """
        查询 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTWeSeeRecognitionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTWeSeeRecognitionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTWeTalkAIBot(
            self,
            request: models.DescribeTWeTalkAIBotRequest,
            opts: Dict = None,
    ) -> models.DescribeTWeTalkAIBotResponse:
        """
        用于查询TWeTalk智能体详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTWeTalkAIBot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTWeTalkAIBotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTWeTalkProductConfig(
            self,
            request: models.DescribeTWeTalkProductConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeTWeTalkProductConfigResponse:
        """
        用于获取TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTWeTalkProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTWeTalkProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTWeTalkProductConfigV2(
            self,
            request: models.DescribeTWeTalkProductConfigV2Request,
            opts: Dict = None,
    ) -> models.DescribeTWeTalkProductConfigV2Response:
        """
        用于查询TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTWeTalkProductConfigV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTWeTalkProductConfigV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicPolicy(
            self,
            request: models.DescribeTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicPolicyResponse:
        """
        本接口（DescribeTopicPolicy）用于查看Topic详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicRule(
            self,
            request: models.DescribeTopicRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicRuleResponse:
        """
        获取规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnbindedDevices(
            self,
            request: models.DescribeUnbindedDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeUnbindedDevicesResponse:
        """
        获取未绑定的设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnbindedDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnbindedDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoLicense(
            self,
            request: models.DescribeVideoLicenseRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoLicenseResponse:
        """
        用于查询视频激活码统计概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DirectBindDeviceInFamily(
            self,
            request: models.DirectBindDeviceInFamilyRequest,
            opts: Dict = None,
    ) -> models.DirectBindDeviceInFamilyResponse:
        """
        直接绑定设备和家庭
        """
        
        kwargs = {}
        kwargs["action"] = "DirectBindDeviceInFamily"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DirectBindDeviceInFamilyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableTopicRule(
            self,
            request: models.DisableTopicRuleRequest,
            opts: Dict = None,
    ) -> models.DisableTopicRuleResponse:
        """
        禁用规则
        """
        
        kwargs = {}
        kwargs["action"] = "DisableTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DismissRoomByStrRoomIdFromTRTC(
            self,
            request: models.DismissRoomByStrRoomIdFromTRTCRequest,
            opts: Dict = None,
    ) -> models.DismissRoomByStrRoomIdFromTRTCResponse:
        """
        解散TRTC房间
        """
        
        kwargs = {}
        kwargs["action"] = "DismissRoomByStrRoomIdFromTRTC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DismissRoomByStrRoomIdFromTRTCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTopicRule(
            self,
            request: models.EnableTopicRuleRequest,
            opts: Dict = None,
    ) -> models.EnableTopicRuleResponse:
        """
        启用规则
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenSingleDeviceSignatureOfPublic(
            self,
            request: models.GenSingleDeviceSignatureOfPublicRequest,
            opts: Dict = None,
    ) -> models.GenSingleDeviceSignatureOfPublicResponse:
        """
        无
        """
        
        kwargs = {}
        kwargs["action"] = "GenSingleDeviceSignatureOfPublic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenSingleDeviceSignatureOfPublicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateCloudStorageAIServiceTaskFileURL(
            self,
            request: models.GenerateCloudStorageAIServiceTaskFileURLRequest,
            opts: Dict = None,
    ) -> models.GenerateCloudStorageAIServiceTaskFileURLResponse:
        """
        获取云存 AI 分析任务输出文件的下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateCloudStorageAIServiceTaskFileURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateCloudStorageAIServiceTaskFileURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateSignedVideoURL(
            self,
            request: models.GenerateSignedVideoURLRequest,
            opts: Dict = None,
    ) -> models.GenerateSignedVideoURLResponse:
        """
        获取视频防盗链播放URL
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateSignedVideoURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateSignedVideoURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAuthMiniProgramAppList(
            self,
            request: models.GetAuthMiniProgramAppListRequest,
            opts: Dict = None,
    ) -> models.GetAuthMiniProgramAppListResponse:
        """
        查询小程序列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetAuthMiniProgramAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAuthMiniProgramAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetBatchProductionsList(
            self,
            request: models.GetBatchProductionsListRequest,
            opts: Dict = None,
    ) -> models.GetBatchProductionsListResponse:
        """
        列出量产数据列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetBatchProductionsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetBatchProductionsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCOSURL(
            self,
            request: models.GetCOSURLRequest,
            opts: Dict = None,
    ) -> models.GetCOSURLResponse:
        """
        本接口（GetCOSURL）用于获取固件COS存储的上传请求URL地址
        """
        
        kwargs = {}
        kwargs["action"] = "GetCOSURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCOSURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceList(
            self,
            request: models.GetDeviceListRequest,
            opts: Dict = None,
    ) -> models.GetDeviceListResponse:
        """
        用于查询某个产品下的设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceLocationHistory(
            self,
            request: models.GetDeviceLocationHistoryRequest,
            opts: Dict = None,
    ) -> models.GetDeviceLocationHistoryResponse:
        """
        获取设备历史位置
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceLocationHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceLocationHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceSumStatistics(
            self,
            request: models.GetDeviceSumStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetDeviceSumStatisticsResponse:
        """
        拉取设备统计汇总数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceSumStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceSumStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFamilyDeviceUserList(
            self,
            request: models.GetFamilyDeviceUserListRequest,
            opts: Dict = None,
    ) -> models.GetFamilyDeviceUserListResponse:
        """
        用于获取设备绑定的用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetFamilyDeviceUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFamilyDeviceUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGatewaySubDeviceList(
            self,
            request: models.GetGatewaySubDeviceListRequest,
            opts: Dict = None,
    ) -> models.GetGatewaySubDeviceListResponse:
        """
        获取指定网关设备的子设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetGatewaySubDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGatewaySubDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLoRaGatewayList(
            self,
            request: models.GetLoRaGatewayListRequest,
            opts: Dict = None,
    ) -> models.GetLoRaGatewayListResponse:
        """
        获取 LoRa 网关列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetLoRaGatewayList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLoRaGatewayListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPositionSpaceList(
            self,
            request: models.GetPositionSpaceListRequest,
            opts: Dict = None,
    ) -> models.GetPositionSpaceListResponse:
        """
        获取位置空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetPositionSpaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPositionSpaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProjectList(
            self,
            request: models.GetProjectListRequest,
            opts: Dict = None,
    ) -> models.GetProjectListResponse:
        """
        提供查询用户所创建的项目列表查询功能。
        """
        
        kwargs = {}
        kwargs["action"] = "GetProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetStudioProductList(
            self,
            request: models.GetStudioProductListRequest,
            opts: Dict = None,
    ) -> models.GetStudioProductListResponse:
        """
        提供查询某个项目下所有产品信息的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "GetStudioProductList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetStudioProductListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTWeCallActiveStatus(
            self,
            request: models.GetTWeCallActiveStatusRequest,
            opts: Dict = None,
    ) -> models.GetTWeCallActiveStatusResponse:
        """
        查询激活状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetTWeCallActiveStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTWeCallActiveStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTWeTalkAIBotList(
            self,
            request: models.GetTWeTalkAIBotListRequest,
            opts: Dict = None,
    ) -> models.GetTWeTalkAIBotListResponse:
        """
        用于查询TWeTalk智能体列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTWeTalkAIBotList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTWeTalkAIBotListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTWeTalkProductConfigList(
            self,
            request: models.GetTWeTalkProductConfigListRequest,
            opts: Dict = None,
    ) -> models.GetTWeTalkProductConfigListResponse:
        """
        用于获取TWeTalk服务连接产品配置信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTWeTalkProductConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTWeTalkProductConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTWeTalkProductConfigListV2(
            self,
            request: models.GetTWeTalkProductConfigListV2Request,
            opts: Dict = None,
    ) -> models.GetTWeTalkProductConfigListV2Response:
        """
        用于查询TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTWeTalkProductConfigListV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTWeTalkProductConfigListV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTopicRuleList(
            self,
            request: models.GetTopicRuleListRequest,
            opts: Dict = None,
    ) -> models.GetTopicRuleListResponse:
        """
        获取规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTopicRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTopicRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWechatDeviceTicket(
            self,
            request: models.GetWechatDeviceTicketRequest,
            opts: Dict = None,
    ) -> models.GetWechatDeviceTicketResponse:
        """
        查询微信设备授权票据
        """
        
        kwargs = {}
        kwargs["action"] = "GetWechatDeviceTicket"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWechatDeviceTicketResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InheritCloudStorageUser(
            self,
            request: models.InheritCloudStorageUserRequest,
            opts: Dict = None,
    ) -> models.InheritCloudStorageUserResponse:
        """
        继承云存用户
        """
        
        kwargs = {}
        kwargs["action"] = "InheritCloudStorageUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InheritCloudStorageUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeAISearchService(
            self,
            request: models.InvokeAISearchServiceRequest,
            opts: Dict = None,
    ) -> models.InvokeAISearchServiceResponse:
        """
        视频语义搜索
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeAISearchService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeAISearchServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeCloudStorageAIServiceTask(
            self,
            request: models.InvokeCloudStorageAIServiceTaskRequest,
            opts: Dict = None,
    ) -> models.InvokeCloudStorageAIServiceTaskResponse:
        """
        同步执行设备云存 AI 分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeCloudStorageAIServiceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeCloudStorageAIServiceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeExternalSourceAIServiceTask(
            self,
            request: models.InvokeExternalSourceAIServiceTaskRequest,
            opts: Dict = None,
    ) -> models.InvokeExternalSourceAIServiceTaskResponse:
        """
        创建外部视频 AI 分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeExternalSourceAIServiceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeExternalSourceAIServiceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeTWeSeeRecognitionTask(
            self,
            request: models.InvokeTWeSeeRecognitionTaskRequest,
            opts: Dict = None,
    ) -> models.InvokeTWeSeeRecognitionTaskResponse:
        """
        同步执行 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeTWeSeeRecognitionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeTWeSeeRecognitionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeTWeSeeRecognitionTaskWithFile(
            self,
            request: models.InvokeTWeSeeRecognitionTaskWithFileRequest,
            opts: Dict = None,
    ) -> models.InvokeTWeSeeRecognitionTaskWithFileResponse:
        """
        同步执行 TWeSee 语义理解任务
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeTWeSeeRecognitionTaskWithFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeTWeSeeRecognitionTaskWithFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeVideosKeywordsAnalyzer(
            self,
            request: models.InvokeVideosKeywordsAnalyzerRequest,
            opts: Dict = None,
    ) -> models.InvokeVideosKeywordsAnalyzerResponse:
        """
        获取某个时间段的视频内容关键字
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeVideosKeywordsAnalyzer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeVideosKeywordsAnalyzerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEventHistory(
            self,
            request: models.ListEventHistoryRequest,
            opts: Dict = None,
    ) -> models.ListEventHistoryResponse:
        """
        获取设备的历史事件
        """
        
        kwargs = {}
        kwargs["action"] = "ListEventHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEventHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFirmwares(
            self,
            request: models.ListFirmwaresRequest,
            opts: Dict = None,
    ) -> models.ListFirmwaresResponse:
        """
        本接口（ListFirmwares）用于获取固件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListFirmwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFirmwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOtaModules(
            self,
            request: models.ListOtaModulesRequest,
            opts: Dict = None,
    ) -> models.ListOtaModulesResponse:
        """
        本接口（ListOtaModules）用于获取OTA模块列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOtaModules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOtaModulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProductOtaModules(
            self,
            request: models.ListProductOtaModulesRequest,
            opts: Dict = None,
    ) -> models.ListProductOtaModulesResponse:
        """
        本接口（ListProductOtaModules）用于获取产品OTA模块列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListProductOtaModules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProductOtaModulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTopicPolicy(
            self,
            request: models.ListTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.ListTopicPolicyResponse:
        """
        本接口（ListTopicPolicy）用于获取Topic列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        更新应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudStorageAIService(
            self,
            request: models.ModifyCloudStorageAIServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudStorageAIServiceResponse:
        """
        修改指定设备的云存 AI 服务参数配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudStorageAIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudStorageAIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudStorageAIServiceCallback(
            self,
            request: models.ModifyCloudStorageAIServiceCallbackRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudStorageAIServiceCallbackResponse:
        """
        修改云存AI分析回调配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudStorageAIServiceCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudStorageAIServiceCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFenceBind(
            self,
            request: models.ModifyFenceBindRequest,
            opts: Dict = None,
    ) -> models.ModifyFenceBindResponse:
        """
        更新围栏绑定信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFenceBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFenceBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoRaFrequency(
            self,
            request: models.ModifyLoRaFrequencyRequest,
            opts: Dict = None,
    ) -> models.ModifyLoRaFrequencyResponse:
        """
        修改LoRa自定义频点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoRaFrequency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoRaFrequencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoRaGateway(
            self,
            request: models.ModifyLoRaGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyLoRaGatewayResponse:
        """
        修改 LoRa 网关信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoRaGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoRaGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModelDefinition(
            self,
            request: models.ModifyModelDefinitionRequest,
            opts: Dict = None,
    ) -> models.ModifyModelDefinitionResponse:
        """
        提供修改产品的数据模板的能力
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModelDefinition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModelDefinitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPositionFence(
            self,
            request: models.ModifyPositionFenceRequest,
            opts: Dict = None,
    ) -> models.ModifyPositionFenceResponse:
        """
        更新围栏。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPositionFence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPositionFenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPositionSpace(
            self,
            request: models.ModifyPositionSpaceRequest,
            opts: Dict = None,
    ) -> models.ModifyPositionSpaceResponse:
        """
        更新位置空间。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPositionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPositionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProductCloudStorageAIService(
            self,
            request: models.ModifyProductCloudStorageAIServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyProductCloudStorageAIServiceResponse:
        """
        修改指定产品的云存 AI 服务开通状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProductCloudStorageAIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProductCloudStorageAIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySpaceProperty(
            self,
            request: models.ModifySpacePropertyRequest,
            opts: Dict = None,
    ) -> models.ModifySpacePropertyResponse:
        """
        更新位置空间产品属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySpaceProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySpacePropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStudioProduct(
            self,
            request: models.ModifyStudioProductRequest,
            opts: Dict = None,
    ) -> models.ModifyStudioProductResponse:
        """
        提供修改产品的名称和描述等信息的能力，对于已发布产品不允许进行修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStudioProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStudioProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTWeSeeConfig(
            self,
            request: models.ModifyTWeSeeConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyTWeSeeConfigResponse:
        """
        修改 TWeSee 配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTWeSeeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTWeSeeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTWeTalkAIBot(
            self,
            request: models.ModifyTWeTalkAIBotRequest,
            opts: Dict = None,
    ) -> models.ModifyTWeTalkAIBotResponse:
        """
        用于修改TWeTalk智能体。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTWeTalkAIBot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTWeTalkAIBotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTWeTalkProductConfig(
            self,
            request: models.ModifyTWeTalkProductConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyTWeTalkProductConfigResponse:
        """
        用于修改TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTWeTalkProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTWeTalkProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTWeTalkProductConfigV2(
            self,
            request: models.ModifyTWeTalkProductConfigV2Request,
            opts: Dict = None,
    ) -> models.ModifyTWeTalkProductConfigV2Response:
        """
        用于修改配置TWeTalk服务连接产品配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTWeTalkProductConfigV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTWeTalkProductConfigV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopicPolicy(
            self,
            request: models.ModifyTopicPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicPolicyResponse:
        """
        本接口（UpdateTopicPolicy）用于更新Topic信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopicPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopicRule(
            self,
            request: models.ModifyTopicRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicRuleResponse:
        """
        修改规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseTWeCallDevice(
            self,
            request: models.PauseTWeCallDeviceRequest,
            opts: Dict = None,
    ) -> models.PauseTWeCallDeviceResponse:
        """
        暂停设备
        """
        
        kwargs = {}
        kwargs["action"] = "PauseTWeCallDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseTWeCallDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishBroadcastMessage(
            self,
            request: models.PublishBroadcastMessageRequest,
            opts: Dict = None,
    ) -> models.PublishBroadcastMessageResponse:
        """
        发布广播消息、发布RRPC消息属于早期服务，目前已停止维护，需要从官网下线。

        发布广播消息
        """
        
        kwargs = {}
        kwargs["action"] = "PublishBroadcastMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishBroadcastMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishFirmwareUpdateMessage(
            self,
            request: models.PublishFirmwareUpdateMessageRequest,
            opts: Dict = None,
    ) -> models.PublishFirmwareUpdateMessageResponse:
        """
        本接口（PublishFirmwareUpdateMessage）用于用户确认升级后，云端向设备发起固件升级请求。
        """
        
        kwargs = {}
        kwargs["action"] = "PublishFirmwareUpdateMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishFirmwareUpdateMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishMessage(
            self,
            request: models.PublishMessageRequest,
            opts: Dict = None,
    ) -> models.PublishMessageResponse:
        """
        本接口（PublishMessage）用于使用自定义透传协议进行设备远控
        """
        
        kwargs = {}
        kwargs["action"] = "PublishMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishRRPCMessage(
            self,
            request: models.PublishRRPCMessageRequest,
            opts: Dict = None,
    ) -> models.PublishRRPCMessageResponse:
        """
        发布广播消息、发布RRPC消息属于早期服务，目前已停止维护，需要从官网下线。

        下发RRPC消息
        """
        
        kwargs = {}
        kwargs["action"] = "PublishRRPCMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishRRPCMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseStudioProduct(
            self,
            request: models.ReleaseStudioProductRequest,
            opts: Dict = None,
    ) -> models.ReleaseStudioProductResponse:
        """
        产品开发完成并测试通过后，通过发布产品将产品设置为发布状态
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseStudioProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseStudioProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserByRoomIdFromTRTC(
            self,
            request: models.RemoveUserByRoomIdFromTRTCRequest,
            opts: Dict = None,
    ) -> models.RemoveUserByRoomIdFromTRTCResponse:
        """
        TRTC操作，将用户从房间移出
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserByRoomIdFromTRTC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserByRoomIdFromTRTCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetCloudStorage(
            self,
            request: models.ResetCloudStorageRequest,
            opts: Dict = None,
    ) -> models.ResetCloudStorageResponse:
        """
        重置云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "ResetCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetCloudStorageAIService(
            self,
            request: models.ResetCloudStorageAIServiceRequest,
            opts: Dict = None,
    ) -> models.ResetCloudStorageAIServiceResponse:
        """
        重置指定设备的云存 AI 服务
        """
        
        kwargs = {}
        kwargs["action"] = "ResetCloudStorageAIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetCloudStorageAIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetCloudStorageEvent(
            self,
            request: models.ResetCloudStorageEventRequest,
            opts: Dict = None,
    ) -> models.ResetCloudStorageEventResponse:
        """
        重置云存事件
        """
        
        kwargs = {}
        kwargs["action"] = "ResetCloudStorageEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetCloudStorageEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetTWeCallDevice(
            self,
            request: models.ResetTWeCallDeviceRequest,
            opts: Dict = None,
    ) -> models.ResetTWeCallDeviceResponse:
        """
        重置设备
        """
        
        kwargs = {}
        kwargs["action"] = "ResetTWeCallDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetTWeCallDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeWeCallDevice(
            self,
            request: models.ResumeWeCallDeviceRequest,
            opts: Dict = None,
    ) -> models.ResumeWeCallDeviceResponse:
        """
        恢复设备
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeWeCallDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeWeCallDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchPositionSpace(
            self,
            request: models.SearchPositionSpaceRequest,
            opts: Dict = None,
    ) -> models.SearchPositionSpaceResponse:
        """
        搜索位置空间
        """
        
        kwargs = {}
        kwargs["action"] = "SearchPositionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchPositionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchStudioProduct(
            self,
            request: models.SearchStudioProductRequest,
            opts: Dict = None,
    ) -> models.SearchStudioProductResponse:
        """
        提供根据产品名称查找产品的能力
        """
        
        kwargs = {}
        kwargs["action"] = "SearchStudioProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchStudioProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchTopicRule(
            self,
            request: models.SearchTopicRuleRequest,
            opts: Dict = None,
    ) -> models.SearchTopicRuleResponse:
        """
        搜索规则
        """
        
        kwargs = {}
        kwargs["action"] = "SearchTopicRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchTopicRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferCloudStorage(
            self,
            request: models.TransferCloudStorageRequest,
            opts: Dict = None,
    ) -> models.TransferCloudStorageResponse:
        """
        转移云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "TransferCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferTWeCallDevice(
            self,
            request: models.TransferTWeCallDeviceRequest,
            opts: Dict = None,
    ) -> models.TransferTWeCallDeviceResponse:
        """
        转移设备
        """
        
        kwargs = {}
        kwargs["action"] = "TransferTWeCallDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferTWeCallDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindDevices(
            self,
            request: models.UnbindDevicesRequest,
            opts: Dict = None,
    ) -> models.UnbindDevicesResponse:
        """
        批量解绑子设备
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindProducts(
            self,
            request: models.UnbindProductsRequest,
            opts: Dict = None,
    ) -> models.UnbindProductsResponse:
        """
        批量解绑子产品。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindTWeTalkAIBot(
            self,
            request: models.UnbindTWeTalkAIBotRequest,
            opts: Dict = None,
    ) -> models.UnbindTWeTalkAIBotResponse:
        """
        用于解除一个产品和智能体的绑定。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindTWeTalkAIBot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindTWeTalkAIBotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceTWeCallAuthorizeStatus(
            self,
            request: models.UpdateDeviceTWeCallAuthorizeStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceTWeCallAuthorizeStatusResponse:
        """
        更新用户对设备的TweCall授权状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceTWeCallAuthorizeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceTWeCallAuthorizeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDevicesEnableState(
            self,
            request: models.UpdateDevicesEnableStateRequest,
            opts: Dict = None,
    ) -> models.UpdateDevicesEnableStateResponse:
        """
        批量禁用启用设备
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDevicesEnableState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDevicesEnableStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFirmware(
            self,
            request: models.UpdateFirmwareRequest,
            opts: Dict = None,
    ) -> models.UpdateFirmwareResponse:
        """
        本接口（UpdateFirmware）用于对指定设备发起固件升级请求
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOtaModule(
            self,
            request: models.UpdateOtaModuleRequest,
            opts: Dict = None,
    ) -> models.UpdateOtaModuleResponse:
        """
        本接口（UpdateOtaModule）用于修改OTA模块
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOtaModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOtaModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOtaTaskStatus(
            self,
            request: models.UpdateOtaTaskStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateOtaTaskStatusResponse:
        """
        本接口（UpdateOtaTask）当固件升级大任务处于没有在全部成功的状态时，可修改为取消状态，取消部分或全部设备的升级;或其它允许的可修改的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOtaTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOtaTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFirmware(
            self,
            request: models.UploadFirmwareRequest,
            opts: Dict = None,
    ) -> models.UploadFirmwareResponse:
        """
        本接口（UploadFirmware）用于创建设备固件版本信息，在平台用于固件版本升级、固件资源下发等。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)