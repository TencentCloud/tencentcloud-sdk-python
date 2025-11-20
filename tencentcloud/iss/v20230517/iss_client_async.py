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
from tencentcloud.iss.v20230517 import models
from typing import Dict


class IssClient(AbstractClient):
    _apiVersion = '2023-05-17'
    _endpoint = 'iss.tencentcloudapi.com'
    _service = 'iss'

    async def AddAITask(
            self,
            request: models.AddAITaskRequest,
            opts: Dict = None,
    ) -> models.AddAITaskResponse:
        """
        添加AI任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddAITask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAITaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganization(
            self,
            request: models.AddOrganizationRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationResponse:
        """
        用于新增组织。
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordBackupPlan(
            self,
            request: models.AddRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.AddRecordBackupPlanResponse:
        """
        用于新增录像上云计划 （当前仅适用于通过GB28181协议和网关接入的设备/视频通道）
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordBackupTemplate(
            self,
            request: models.AddRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.AddRecordBackupTemplateResponse:
        """
        用于新增录像上云模板。
        > 该功能本质是拉取设备本地录像数据上云（即存在 IPC 摄像头存储卡或 NVR 硬盘中的录像），操作时需先设定录像时间段（即想要上云的设备本地录像），再设定上云时间段和上云倍速，平台将于上云时间段倍速拉取设备对应前一天的录像时间段数据。

        > 设定需至少满足（上云时间段=前一天的录像时间段/上云倍速），建议上云时间段可多设定10%左右的时间，避免因网络波动导致数据拉取不完整。
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordPlan(
            self,
            request: models.AddRecordPlanRequest,
            opts: Dict = None,
    ) -> models.AddRecordPlanResponse:
        """
        用于新增实时上云计划
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordRetrieveTask(
            self,
            request: models.AddRecordRetrieveTaskRequest,
            opts: Dict = None,
    ) -> models.AddRecordRetrieveTaskResponse:
        """
        用于新建取回任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordRetrieveTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordRetrieveTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordTemplate(
            self,
            request: models.AddRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.AddRecordTemplateResponse:
        """
        用于新增实时上云模板
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddStreamAuth(
            self,
            request: models.AddStreamAuthRequest,
            opts: Dict = None,
    ) -> models.AddStreamAuthResponse:
        """
        用于设置推拉流鉴权配置。
        """
        
        kwargs = {}
        kwargs["action"] = "AddStreamAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddStreamAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserDevice(
            self,
            request: models.AddUserDeviceRequest,
            opts: Dict = None,
    ) -> models.AddUserDeviceResponse:
        """
        用于新增单个设备。添加设备之后，可根据返回结果到设备上进行配置，配置后等待设备注册/推流。
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteVideoDownloadTask(
            self,
            request: models.BatchDeleteVideoDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteVideoDownloadTaskResponse:
        """
        用于批量删除本地录像下载失败的任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteVideoDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteVideoDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchOperateDevice(
            self,
            request: models.BatchOperateDeviceRequest,
            opts: Dict = None,
    ) -> models.BatchOperateDeviceResponse:
        """
        用于批量操作（启用，禁用，删除）设备
        """
        
        kwargs = {}
        kwargs["action"] = "BatchOperateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchOperateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallISAPI(
            self,
            request: models.CallISAPIRequest,
            opts: Dict = None,
    ) -> models.CallISAPIResponse:
        """
        本接口可基于海康ISUP 5.0协议实现透传ISAPI的请求数据，调用接口前需确保设备采用ISUP协议成功注册至本平台
        """
        
        kwargs = {}
        kwargs["action"] = "CallISAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallISAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDevicePTZ(
            self,
            request: models.ControlDevicePTZRequest,
            opts: Dict = None,
    ) -> models.ControlDevicePTZResponse:
        """
        用于设备通道云台控制，包括转动、变倍、变焦、光圈等。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDevicePTZ"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDevicePTZResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDevicePreset(
            self,
            request: models.ControlDevicePresetRequest,
            opts: Dict = None,
    ) -> models.ControlDevicePresetResponse:
        """
        用于操作设备预置位，包括设置、删除、调用。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDevicePreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDevicePresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDeviceSnapshot(
            self,
            request: models.ControlDeviceSnapshotRequest,
            opts: Dict = None,
    ) -> models.ControlDeviceSnapshotResponse:
        """
        控制设备抓拍--单次，当前仅支持国标设备
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDeviceSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDeviceSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDeviceStream(
            self,
            request: models.ControlDeviceStreamRequest,
            opts: Dict = None,
    ) -> models.ControlDeviceStreamResponse:
        """
        用于获取设备的实时开流地址。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDeviceStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDeviceStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlRecord(
            self,
            request: models.ControlRecordRequest,
            opts: Dict = None,
    ) -> models.ControlRecordResponse:
        """
        用于录像回放过程中的倍速、跳转、播放/暂停/停止等控制。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlRecordTimeline(
            self,
            request: models.ControlRecordTimelineRequest,
            opts: Dict = None,
    ) -> models.ControlRecordTimelineResponse:
        """
        用于查询设备本地录像时间轴信息，为NVR/IPC本地存储的录像。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlRecordTimeline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlRecordTimelineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoDownloadTask(
            self,
            request: models.CreateVideoDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoDownloadTaskResponse:
        """
        创建本地录像下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAITask(
            self,
            request: models.DeleteAITaskRequest,
            opts: Dict = None,
    ) -> models.DeleteAITaskResponse:
        """
        删除AI任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAITask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAITaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        用于删除域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGateway(
            self,
            request: models.DeleteGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteGatewayResponse:
        """
        用于删除网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganization(
            self,
            request: models.DeleteOrganizationRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationResponse:
        """
        用于删除组织。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordBackupPlan(
            self,
            request: models.DeleteRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordBackupPlanResponse:
        """
        用于删除录像上云模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordBackupTemplate(
            self,
            request: models.DeleteRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordBackupTemplateResponse:
        """
        用于删除录像上云模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordPlan(
            self,
            request: models.DeleteRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordPlanResponse:
        """
        用于删除实时上云计划
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordRetrieveTask(
            self,
            request: models.DeleteRecordRetrieveTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordRetrieveTaskResponse:
        """
        用于删除取回任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordRetrieveTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordRetrieveTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordTemplate(
            self,
            request: models.DeleteRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordTemplateResponse:
        """
        用于删除实时上云模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        用于删除执行完成的任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserDevice(
            self,
            request: models.DeleteUserDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteUserDeviceResponse:
        """
        用于删除已添加的设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAITask(
            self,
            request: models.DescribeAITaskRequest,
            opts: Dict = None,
    ) -> models.DescribeAITaskResponse:
        """
        获取AI任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAITask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAITaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAITaskResult(
            self,
            request: models.DescribeAITaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeAITaskResultResponse:
        """
        获取AI任务识别结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAITaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAITaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCNAME(
            self,
            request: models.DescribeCNAMERequest,
            opts: Dict = None,
    ) -> models.DescribeCNAMEResponse:
        """
        用于根据服务节点获取 CNAME 值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceChannel(
            self,
            request: models.DescribeDeviceChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceChannelResponse:
        """
        用于查询设备的通道。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePreset(
            self,
            request: models.DescribeDevicePresetRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePresetResponse:
        """
        用于查询设备通道预置位信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceRegion(
            self,
            request: models.DescribeDeviceRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceRegionResponse:
        """
        用于添加设备时，查询设备可以使用的服务节点，查询结果为已经绑定了域名的服务节点。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomain(
            self,
            request: models.DescribeDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainResponse:
        """
        用于查询添加的域名列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainRegion(
            self,
            request: models.DescribeDomainRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainRegionResponse:
        """
        用于用户添加域名时，查询可以绑定的服务节点，结果为平台支持的所有服务节点。（注意：每个服务节点只能绑定一个域名）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGBDeviceAddr(
            self,
            request: models.DescribeGBDeviceAddrRequest,
            opts: Dict = None,
    ) -> models.DescribeGBDeviceAddrResponse:
        """
        用于获取国标设备的公网地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGBDeviceAddr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGBDeviceAddrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGateway(
            self,
            request: models.DescribeGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayResponse:
        """
        用于获取网关详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayMonitor(
            self,
            request: models.DescribeGatewayMonitorRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayMonitorResponse:
        """
        用于获取网关的数据及流量监控信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayProtocol(
            self,
            request: models.DescribeGatewayProtocolRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayProtocolResponse:
        """
        用于查询网关接入协议。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayProtocol"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayProtocolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayVersion(
            self,
            request: models.DescribeGatewayVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayVersionResponse:
        """
        查询网关服务版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganization(
            self,
            request: models.DescribeOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationResponse:
        """
        用于查询组织。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordBackupPlan(
            self,
            request: models.DescribeRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordBackupPlanResponse:
        """
        用于查询录像上云计划详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordBackupTemplate(
            self,
            request: models.DescribeRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordBackupTemplateResponse:
        """
        用于查询录像上云模板详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordFile(
            self,
            request: models.DescribeRecordFileRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordFileResponse:
        """
        用于查询设备云端录像时间轴信息（即为视频上云后设置录像计划后云存储的录像）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordPlan(
            self,
            request: models.DescribeRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordPlanResponse:
        """
        用于查询实时上云计划详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordPlaybackUrl(
            self,
            request: models.DescribeRecordPlaybackUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordPlaybackUrlResponse:
        """
        用于获取云端录像回放url地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordPlaybackUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordPlaybackUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordRetrieveTask(
            self,
            request: models.DescribeRecordRetrieveTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordRetrieveTaskResponse:
        """
        用于查询云录像取回任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordRetrieveTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordRetrieveTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordSlice(
            self,
            request: models.DescribeRecordSliceRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordSliceResponse:
        """
        平台支持将数据以TS切片的形式存入客户自有COS桶，该接口用于支持客户快捷查询切片信息列表
        （注意：只支持标准存储类型的查询）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordSlice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordSliceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordTemplate(
            self,
            request: models.DescribeRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTemplateResponse:
        """
        用于查询实时上云模板详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamAuth(
            self,
            request: models.DescribeStreamAuthRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamAuthResponse:
        """
        用于查询推拉流鉴权配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        用于查询任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDevice(
            self,
            request: models.DescribeUserDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDeviceResponse:
        """
        用于查询设备的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDeviceList(
            self,
            request: models.DescribeUserDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDeviceListResponse:
        """
        用于批量查询设备详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoBitRate(
            self,
            request: models.DescribeVideoBitRateRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoBitRateResponse:
        """
        用于获取视频通道的码率信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoBitRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoBitRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoDownloadUrl(
            self,
            request: models.DescribeVideoDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoDownloadUrlResponse:
        """
        用于获取云录像下载 url
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAITasks(
            self,
            request: models.ListAITasksRequest,
            opts: Dict = None,
    ) -> models.ListAITasksResponse:
        """
        获取AI任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAITasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAITasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDeviceSnapshots(
            self,
            request: models.ListDeviceSnapshotsRequest,
            opts: Dict = None,
    ) -> models.ListDeviceSnapshotsResponse:
        """
        获取设备抓拍结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListDeviceSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDeviceSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDevices(
            self,
            request: models.ListDevicesRequest,
            opts: Dict = None,
    ) -> models.ListDevicesResponse:
        """
        用于获取对应组织下的设备列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGatewayDevices(
            self,
            request: models.ListGatewayDevicesRequest,
            opts: Dict = None,
    ) -> models.ListGatewayDevicesResponse:
        """
        用于查询网关下挂载的设备列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListGatewayDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGatewayDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGateways(
            self,
            request: models.ListGatewaysRequest,
            opts: Dict = None,
    ) -> models.ListGatewaysResponse:
        """
        用于获取网关列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationChannelNumbers(
            self,
            request: models.ListOrganizationChannelNumbersRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationChannelNumbersResponse:
        """
        用于查询组织目录下的未添加到实时上云计划中的通道数量
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationChannelNumbers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationChannelNumbersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationChannels(
            self,
            request: models.ListOrganizationChannelsRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationChannelsResponse:
        """
        用于查询组织目录下的通道列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordBackupPlanDevices(
            self,
            request: models.ListRecordBackupPlanDevicesRequest,
            opts: Dict = None,
    ) -> models.ListRecordBackupPlanDevicesResponse:
        """
        用于查询录像上云计划下的设备通道列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordBackupPlanDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordBackupPlanDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordBackupPlans(
            self,
            request: models.ListRecordBackupPlansRequest,
            opts: Dict = None,
    ) -> models.ListRecordBackupPlansResponse:
        """
        用于查询录像上云计划列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordBackupTemplates(
            self,
            request: models.ListRecordBackupTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListRecordBackupTemplatesResponse:
        """
        用于查询录像上云模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordBackupTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordBackupTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordPlanChannels(
            self,
            request: models.ListRecordPlanChannelsRequest,
            opts: Dict = None,
    ) -> models.ListRecordPlanChannelsResponse:
        """
        用于查询用户下所有实时上云计划中的通道列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordPlanChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordPlanChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordPlanDevices(
            self,
            request: models.ListRecordPlanDevicesRequest,
            opts: Dict = None,
    ) -> models.ListRecordPlanDevicesResponse:
        """
        用于查询实时上云计划下的设备通道列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordPlanDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordPlanDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordPlans(
            self,
            request: models.ListRecordPlansRequest,
            opts: Dict = None,
    ) -> models.ListRecordPlansResponse:
        """
        用于查询实时上云计划列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordRetrieveTasks(
            self,
            request: models.ListRecordRetrieveTasksRequest,
            opts: Dict = None,
    ) -> models.ListRecordRetrieveTasksResponse:
        """
        用于查询取回任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordRetrieveTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordRetrieveTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordTemplates(
            self,
            request: models.ListRecordTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListRecordTemplatesResponse:
        """
        用于查询实时上云模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSubTasks(
            self,
            request: models.ListSubTasksRequest,
            opts: Dict = None,
    ) -> models.ListSubTasksResponse:
        """
        用于查询任务的子任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSubTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSubTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTasks(
            self,
            request: models.ListTasksRequest,
            opts: Dict = None,
    ) -> models.ListTasksResponse:
        """
        用于查询批量任务和简单任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVideoDownloadTask(
            self,
            request: models.ListVideoDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.ListVideoDownloadTaskResponse:
        """
        查询本店里录像下载任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListVideoDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVideoDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PlayRecord(
            self,
            request: models.PlayRecordRequest,
            opts: Dict = None,
    ) -> models.PlayRecordResponse:
        """
        用于获取设备本地录像 URL 地址。
        """
        
        kwargs = {}
        kwargs["action"] = "PlayRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PlayRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryForbidPlayChannelList(
            self,
            request: models.QueryForbidPlayChannelListRequest,
            opts: Dict = None,
    ) -> models.QueryForbidPlayChannelListResponse:
        """
        查询禁播通道列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryForbidPlayChannelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryForbidPlayChannelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshDeviceChannel(
            self,
            request: models.RefreshDeviceChannelRequest,
            opts: Dict = None,
    ) -> models.RefreshDeviceChannelResponse:
        """
        用于同步国标设备的通道（接口调用后，触发向设备请求通道列表，新增的通道入库，设备上已删除的通道需自行删除、后台不自动删除）。
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshDeviceChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshDeviceChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetForbidPlayChannels(
            self,
            request: models.SetForbidPlayChannelsRequest,
            opts: Dict = None,
    ) -> models.SetForbidPlayChannelsResponse:
        """
        禁止主、子账号对视频通道的实况预览
        """
        
        kwargs = {}
        kwargs["action"] = "SetForbidPlayChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetForbidPlayChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAITask(
            self,
            request: models.UpdateAITaskRequest,
            opts: Dict = None,
    ) -> models.UpdateAITaskResponse:
        """
        更新AI任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAITask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAITaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAITaskStatus(
            self,
            request: models.UpdateAITaskStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAITaskStatusResponse:
        """
        更新 AI 任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAITaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAITaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceOrganization(
            self,
            request: models.UpdateDeviceOrganizationRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceOrganizationResponse:
        """
        用于批量更改设备的组织。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceStatus(
            self,
            request: models.UpdateDeviceStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceStatusResponse:
        """
        用于启用/禁用设备，禁用后拒绝设备注册。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGateway(
            self,
            request: models.UpdateGatewayRequest,
            opts: Dict = None,
    ) -> models.UpdateGatewayResponse:
        """
        用于修改网关信息（支持对网关名称和描述的修改）。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganization(
            self,
            request: models.UpdateOrganizationRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationResponse:
        """
        用于修改组织。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordBackupPlan(
            self,
            request: models.UpdateRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordBackupPlanResponse:
        """
        用于修改录像上云计划。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordBackupTemplate(
            self,
            request: models.UpdateRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordBackupTemplateResponse:
        """
        用于修改录像上云模板。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordPlan(
            self,
            request: models.UpdateRecordPlanRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordPlanResponse:
        """
        用于修改实时上云计划
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordTemplate(
            self,
            request: models.UpdateRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordTemplateResponse:
        """
        用于修改实时上云模板
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserDevice(
            self,
            request: models.UpdateUserDeviceRequest,
            opts: Dict = None,
    ) -> models.UpdateUserDeviceResponse:
        """
        用于修改设备的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeGateway(
            self,
            request: models.UpgradeGatewayRequest,
            opts: Dict = None,
    ) -> models.UpgradeGatewayResponse:
        """
        用于网关升级（支持对所有待更新的服务一键升级）。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)