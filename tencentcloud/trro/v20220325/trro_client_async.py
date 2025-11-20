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
from tencentcloud.trro.v20220325 import models
from typing import Dict


class TrroClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'trro.tencentcloudapi.com'
    _service = 'trro'

    async def BatchDeleteDevices(
            self,
            request: models.BatchDeleteDevicesRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteDevicesResponse:
        """
        用于批量删除设备
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeletePolicy(
            self,
            request: models.BatchDeletePolicyRequest,
            opts: Dict = None,
    ) -> models.BatchDeletePolicyResponse:
        """
        用于批量删除修改权限配置
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeletePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeletePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BoundLicenses(
            self,
            request: models.BoundLicensesRequest,
            opts: Dict = None,
    ) -> models.BoundLicensesResponse:
        """
        为推流设备绑定license，优先绑定到期时间最近的，到期时间相同优先绑定月包
        """
        
        kwargs = {}
        kwargs["action"] = "BoundLicenses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BoundLicensesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudRecording(
            self,
            request: models.CreateCloudRecordingRequest,
            opts: Dict = None,
    ) -> models.CreateCloudRecordingResponse:
        """
        启动云端录制功能，完成房间内的音视频录制，并上传到指定的云存储。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudRecording"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudRecordingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevice(
            self,
            request: models.CreateDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceResponse:
        """
        用于创建设备
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        用于创建项目
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudRecording(
            self,
            request: models.DeleteCloudRecordingRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudRecordingResponse:
        """
        成功开启录制后，可以使用此接口来停止录制任务。停止录制成功后不代表文件全部传输完成，如果未完成后台将会继续上传文件，成功后通过事件回调通知客户文件全部传输完成状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudRecording"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudRecordingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        用于删除项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceInfo(
            self,
            request: models.DescribeDeviceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceInfoResponse:
        """
        用于获取指定设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceList(
            self,
            request: models.DescribeDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceListResponse:
        """
        用于获取设备信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceSessionDetails(
            self,
            request: models.DescribeDeviceSessionDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceSessionDetailsResponse:
        """
        获取设备会话数据详单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceSessionDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceSessionDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceSessionList(
            self,
            request: models.DescribeDeviceSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceSessionListResponse:
        """
        获取设备会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicy(
            self,
            request: models.DescribePolicyRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyResponse:
        """
        用于查看权限配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectInfo(
            self,
            request: models.DescribeProjectInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectInfoResponse:
        """
        用于获取项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectList(
            self,
            request: models.DescribeProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectListResponse:
        """
        用于获取项目列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecentSessionList(
            self,
            request: models.DescribeRecentSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecentSessionListResponse:
        """
        获取最新设备会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecentSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecentSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionStatistics(
            self,
            request: models.DescribeSessionStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionStatisticsResponse:
        """
        获取会话统计值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionStatisticsByInterval(
            self,
            request: models.DescribeSessionStatisticsByIntervalRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionStatisticsByIntervalResponse:
        """
        获取各时间段的会话统计值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionStatisticsByInterval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionStatisticsByIntervalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceLicense(
            self,
            request: models.GetDeviceLicenseRequest,
            opts: Dict = None,
    ) -> models.GetDeviceLicenseResponse:
        """
        获取设备已经绑定的可用授权数量
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevices(
            self,
            request: models.GetDevicesRequest,
            opts: Dict = None,
    ) -> models.GetDevicesResponse:
        """
        查询用户设备的授权绑定情况
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDurationDetails(
            self,
            request: models.GetDurationDetailsRequest,
            opts: Dict = None,
    ) -> models.GetDurationDetailsResponse:
        """
        查询该时间段、对应项目、设备的不同分辨率的通话时长流水，流水以日期（天）为单位
        """
        
        kwargs = {}
        kwargs["action"] = "GetDurationDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDurationDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLicenseStat(
            self,
            request: models.GetLicenseStatRequest,
            opts: Dict = None,
    ) -> models.GetLicenseStatResponse:
        """
        统计license类型数量
        """
        
        kwargs = {}
        kwargs["action"] = "GetLicenseStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLicenseStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLicenses(
            self,
            request: models.GetLicensesRequest,
            opts: Dict = None,
    ) -> models.GetLicensesResponse:
        """
        按授权查看license列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetLicenses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLicensesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTotalDuration(
            self,
            request: models.GetTotalDurationRequest,
            opts: Dict = None,
    ) -> models.GetTotalDurationResponse:
        """
        查询该时间段、对应项目、设备的不同分辨率的通话时长汇总
        """
        
        kwargs = {}
        kwargs["action"] = "GetTotalDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTotalDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCallbackUrl(
            self,
            request: models.ModifyCallbackUrlRequest,
            opts: Dict = None,
    ) -> models.ModifyCallbackUrlResponse:
        """
        设置回调URL
        录制回调事件内容参考：https://cloud.tencent.com/document/product/647/81113
        转推回调事件内容参考：https://cloud.tencent.com/document/product/647/88552
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCallbackUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCallbackUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDevice(
            self,
            request: models.ModifyDeviceRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceResponse:
        """
        用于修改设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPolicy(
            self,
            request: models.ModifyPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyPolicyResponse:
        """
        用于修改权限配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        用于修改项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProjectSecMode(
            self,
            request: models.ModifyProjectSecModeRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectSecModeResponse:
        """
        使用项目共享密钥可动态生成设备登录密钥，登录前无需对设备进行提前注册，适合希望简化业务流程的客户。由于是公共密钥，请务必注意保护项目共享密钥，并及时更新。建议项目共享密钥保存在服务器侧。由服务器生成设备登录密码下发给设备，避免密钥保存在客户端侧产生的密钥泄露风险。

        开启项目共享密钥后，对于已注册的设备，仍可使用原设备密码登录。若希望仅能通过共享密钥生成密码登录，请通过云 API 将设备密码更新为"USEPROJECTKEYPWD"。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProjectSecMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectSecModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishLiveStream(
            self,
            request: models.StartPublishLiveStreamRequest,
            opts: Dict = None,
    ) -> models.StartPublishLiveStreamResponse:
        """
        启动一个混流转推任务，将 TRTC 房间的多路音视频流混成一路音视频流，编码后推到直播 CDN 或者回推到 TRTC 房间。也支持不转码直接转推 TRTC 房间的单路流。启动成功后，会返回一个 SdkAppid 维度唯一的任务 Id（TaskId）。您需要保存该 TaskId，后续需要依赖此 TaskId 更新和结束任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPublishLiveStream(
            self,
            request: models.StopPublishLiveStreamRequest,
            opts: Dict = None,
    ) -> models.StopPublishLiveStreamResponse:
        """
        停止指定的混流转推任务。如果没有调用 Stop 接口停止任务，所有参与混流转推的主播离开房间超过MaxIdleTime 设置的时间后，任务也会自动停止。
        """
        
        kwargs = {}
        kwargs["action"] = "StopPublishLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPublishLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)