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
from tencentcloud.iotvideo.v20211125 import models
from typing import Dict


class IotvideoClient(AbstractClient):
    _apiVersion = '2021-11-25'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'

    async def ApplyAIModel(
            self,
            request: models.ApplyAIModelRequest,
            opts: Dict = None,
    ) -> models.ApplyAIModelResponse:
        """
        申请AI模型
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyAIModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyAIModelResponse
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
        
    async def CallDeviceActionAsync(
            self,
            request: models.CallDeviceActionAsyncRequest,
            opts: Dict = None,
    ) -> models.CallDeviceActionAsyncResponse:
        """
        异步调用设备行为
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
        同步调用设备行为
        """
        
        kwargs = {}
        kwargs["action"] = "CallDeviceActionSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallDeviceActionSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallTRTCDevice(
            self,
            request: models.CallTRTCDeviceRequest,
            opts: Dict = None,
    ) -> models.CallTRTCDeviceResponse:
        """
        呼叫TRTC设备
        """
        
        kwargs = {}
        kwargs["action"] = "CallTRTCDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallTRTCDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelAIModelApplication(
            self,
            request: models.CancelAIModelApplicationRequest,
            opts: Dict = None,
    ) -> models.CancelAIModelApplicationResponse:
        """
        取消AI模型申请
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAIModelApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAIModelApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDeviceFirmwareTask(
            self,
            request: models.CancelDeviceFirmwareTaskRequest,
            opts: Dict = None,
    ) -> models.CancelDeviceFirmwareTaskResponse:
        """
        本接口用于取消设备升级任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDeviceFirmwareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDeviceFirmwareTaskResponse
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
        
    async def CheckForwardAuth(
            self,
            request: models.CheckForwardAuthRequest,
            opts: Dict = None,
    ) -> models.CheckForwardAuthResponse:
        """
        判断是否开启转发的权限
        """
        
        kwargs = {}
        kwargs["action"] = "CheckForwardAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckForwardAuthResponse
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
        
    async def CreateAIDetection(
            self,
            request: models.CreateAIDetectionRequest,
            opts: Dict = None,
    ) -> models.CreateAIDetectionResponse:
        """
        发起AI推理请求
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIDetection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIDetectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBatch(
            self,
            request: models.CreateBatchRequest,
            opts: Dict = None,
    ) -> models.CreateBatchResponse:
        """
        创建批次
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCOSCredentials(
            self,
            request: models.CreateCOSCredentialsRequest,
            opts: Dict = None,
    ) -> models.CreateCOSCredentialsResponse:
        """
        创建COS上传密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCOSCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCOSCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudStorage(
            self,
            request: models.CreateCloudStorageRequest,
            opts: Dict = None,
    ) -> models.CreateCloudStorageResponse:
        """
        开通云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataForward(
            self,
            request: models.CreateDataForwardRequest,
            opts: Dict = None,
    ) -> models.CreateDataForwardResponse:
        """
        创建数据转发
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataForward"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataForwardResponse
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
        
    async def CreateForwardRule(
            self,
            request: models.CreateForwardRuleRequest,
            opts: Dict = None,
    ) -> models.CreateForwardRuleResponse:
        """
        创建转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFreeCloudStorage(
            self,
            request: models.CreateFreeCloudStorageRequest,
            opts: Dict = None,
    ) -> models.CreateFreeCloudStorageResponse:
        """
        开通免费云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFreeCloudStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFreeCloudStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProduct(
            self,
            request: models.CreateProductRequest,
            opts: Dict = None,
    ) -> models.CreateProductResponse:
        """
        创建产品
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFileUrl(
            self,
            request: models.CreateTaskFileUrlRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFileUrlResponse:
        """
        本接口（CreateTaskFileUrl）用于获取产品级任务文件上传链接
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFileUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFileUrlResponse
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
        
    async def DeleteFirmware(
            self,
            request: models.DeleteFirmwareRequest,
            opts: Dict = None,
    ) -> models.DeleteFirmwareResponse:
        """
        本接口（DeleteFirmware）用于删除固件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardRule(
            self,
            request: models.DeleteForwardRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardRuleResponse:
        """
        删除转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProduct(
            self,
            request: models.DeleteProductRequest,
            opts: Dict = None,
    ) -> models.DeleteProductResponse:
        """
        删除产品
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIModelApplications(
            self,
            request: models.DescribeAIModelApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIModelApplicationsResponse:
        """
        用户AI模型申请记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIModelApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIModelApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIModelChannel(
            self,
            request: models.DescribeAIModelChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeAIModelChannelResponse:
        """
        查看AI推理结果推送配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIModelChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIModelChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIModelUsage(
            self,
            request: models.DescribeAIModelUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeAIModelUsageResponse:
        """
        查看AI模型资源包
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIModelUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIModelUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIModels(
            self,
            request: models.DescribeAIModelsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIModelsResponse:
        """
        拉取AI模型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIModels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIModelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccount(
            self,
            request: models.DescribeAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountResponse:
        """
        获取消费版账号信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBalance(
            self,
            request: models.DescribeBalanceRequest,
            opts: Dict = None,
    ) -> models.DescribeBalanceResponse:
        """
        查询账户余额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBalanceTransactions(
            self,
            request: models.DescribeBalanceTransactionsRequest,
            opts: Dict = None,
    ) -> models.DescribeBalanceTransactionsResponse:
        """
        拉取账户流水
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBalanceTransactions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBalanceTransactionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatch(
            self,
            request: models.DescribeBatchRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchResponse:
        """
        获取批次详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchs(
            self,
            request: models.DescribeBatchsRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchsResponse:
        """
        获取批次列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBonuses(
            self,
            request: models.DescribeBonusesRequest,
            opts: Dict = None,
    ) -> models.DescribeBonusesResponse:
        """
        查看运营活动资源包列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBonuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBonusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCategory(
            self,
            request: models.DescribeCategoryRequest,
            opts: Dict = None,
    ) -> models.DescribeCategoryResponse:
        """
        获取Category详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCategoryResponse
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
        
    async def DescribeDataForwardList(
            self,
            request: models.DescribeDataForwardListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataForwardListResponse:
        """
        获取数据转发列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataForwardList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataForwardListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevice(
            self,
            request: models.DescribeDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResponse:
        """
        查看设备详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceActionHistory(
            self,
            request: models.DescribeDeviceActionHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceActionHistoryResponse:
        """
        为用户提供获取动作历史的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceActionHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceActionHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceCommLog(
            self,
            request: models.DescribeDeviceCommLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceCommLogResponse:
        """
        获取设备在指定时间范围内的通讯日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceCommLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceCommLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceData(
            self,
            request: models.DescribeDeviceDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceDataResponse:
        """
        获取设备属性数据
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
        
    async def DescribeDeviceDataStats(
            self,
            request: models.DescribeDeviceDataStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceDataStatsResponse:
        """
        查询设备数据统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceDataStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceDataStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceEventHistory(
            self,
            request: models.DescribeDeviceEventHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceEventHistoryResponse:
        """
        获取设备的历史事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceEventHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceEventHistoryResponse
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
        
    async def DescribeDeviceStatusLog(
            self,
            request: models.DescribeDeviceStatusLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceStatusLogResponse:
        """
        获取设备上下线日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceStatusLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceStatusLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        获取设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmware(
            self,
            request: models.DescribeFirmwareRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareResponse:
        """
        本接口（DescribeFirmware）用于查询固件信息
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
        此接口查询固件升级任务详情
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
        本接口用于查询固件升级任务的设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTaskDistribution(
            self,
            request: models.DescribeFirmwareTaskDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskDistributionResponse:
        """
        本接口用于查询固件升级任务状态分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTaskStatistics(
            self,
            request: models.DescribeFirmwareTaskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTaskStatisticsResponse:
        """
        本接口用于查询固件升级任务统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTaskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTaskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirmwareTasks(
            self,
            request: models.DescribeFirmwareTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeFirmwareTasksResponse:
        """
        本接口用于查询固件升级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirmwareTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirmwareTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardRule(
            self,
            request: models.DescribeForwardRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardRuleResponse:
        """
        获取产品转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardRuleResponse
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
        
    async def DescribeMessageDataStats(
            self,
            request: models.DescribeMessageDataStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageDataStatsResponse:
        """
        查询设备消息数量统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageDataStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageDataStatsResponse
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
        
    async def DescribeP2PInfo(
            self,
            request: models.DescribeP2PInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeP2PInfoResponse:
        """
        拉取设备p2p信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeP2PInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeP2PInfoResponse
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
        
    async def DescribeProduct(
            self,
            request: models.DescribeProductRequest,
            opts: Dict = None,
    ) -> models.DescribeProductResponse:
        """
        获取产品详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductDynamicRegister(
            self,
            request: models.DescribeProductDynamicRegisterRequest,
            opts: Dict = None,
    ) -> models.DescribeProductDynamicRegisterResponse:
        """
        获取产品动态注册详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductDynamicRegister"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductDynamicRegisterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducts(
            self,
            request: models.DescribeProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductsResponse:
        """
        获取产品列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushChannel(
            self,
            request: models.DescribePushChannelRequest,
            opts: Dict = None,
    ) -> models.DescribePushChannelResponse:
        """
        查看推送通道
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSDKLog(
            self,
            request: models.DescribeSDKLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSDKLogResponse:
        """
        获取设备sdk日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSDKLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSDKLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        获取video消费版用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditFirmware(
            self,
            request: models.EditFirmwareRequest,
            opts: Dict = None,
    ) -> models.EditFirmwareResponse:
        """
        本接口用于编辑固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "EditFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenSingleDeviceSignatureOfPublic(
            self,
            request: models.GenSingleDeviceSignatureOfPublicRequest,
            opts: Dict = None,
    ) -> models.GenSingleDeviceSignatureOfPublicResponse:
        """
        获取设备的绑定签名
        """
        
        kwargs = {}
        kwargs["action"] = "GenSingleDeviceSignatureOfPublic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenSingleDeviceSignatureOfPublicResponse
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
        
    async def GetAllFirmwareVersion(
            self,
            request: models.GetAllFirmwareVersionRequest,
            opts: Dict = None,
    ) -> models.GetAllFirmwareVersionResponse:
        """
        本接口（GetAllFirmwareVersion）用于获取所有的版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetAllFirmwareVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAllFirmwareVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFirmwareURL(
            self,
            request: models.GetFirmwareURLRequest,
            opts: Dict = None,
    ) -> models.GetFirmwareURLResponse:
        """
        本接口（GetFirmwareURL）用于获取固件存储的URL
        """
        
        kwargs = {}
        kwargs["action"] = "GetFirmwareURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFirmwareURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportModelDefinition(
            self,
            request: models.ImportModelDefinitionRequest,
            opts: Dict = None,
    ) -> models.ImportModelDefinitionResponse:
        """
        导入其它产品的数据模板，覆盖现有数据模板的物模型和产品分类信息
        """
        
        kwargs = {}
        kwargs["action"] = "ImportModelDefinition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportModelDefinitionResponse
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
        
    async def ModifyDataForward(
            self,
            request: models.ModifyDataForwardRequest,
            opts: Dict = None,
    ) -> models.ModifyDataForwardResponse:
        """
        修改数据转发
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataForward"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataForwardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataForwardStatus(
            self,
            request: models.ModifyDataForwardStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDataForwardStatusResponse:
        """
        设置数据转发状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataForwardStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataForwardStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDevice(
            self,
            request: models.ModifyDeviceRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceResponse:
        """
        修改设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceLogLevel(
            self,
            request: models.ModifyDeviceLogLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceLogLevelResponse:
        """
        更新设备日志级别
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceLogLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceLogLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardRule(
            self,
            request: models.ModifyForwardRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardRuleResponse:
        """
        修改转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardRuleResponse
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
        
    async def ModifyProduct(
            self,
            request: models.ModifyProductRequest,
            opts: Dict = None,
    ) -> models.ModifyProductResponse:
        """
        修改产品信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProductDynamicRegister(
            self,
            request: models.ModifyProductDynamicRegisterRequest,
            opts: Dict = None,
    ) -> models.ModifyProductDynamicRegisterResponse:
        """
        修改产品动态注册
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProductDynamicRegister"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProductDynamicRegisterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPushChannel(
            self,
            request: models.ModifyPushChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyPushChannelResponse:
        """
        更新推送通道
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPushChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPushChannelResponse
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
        
    async def ReportAliveDevice(
            self,
            request: models.ReportAliveDeviceRequest,
            opts: Dict = None,
    ) -> models.ReportAliveDeviceResponse:
        """
        上报活跃设备
        """
        
        kwargs = {}
        kwargs["action"] = "ReportAliveDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportAliveDeviceResponse
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
        
    async def RetryDeviceFirmwareTask(
            self,
            request: models.RetryDeviceFirmwareTaskRequest,
            opts: Dict = None,
    ) -> models.RetryDeviceFirmwareTaskResponse:
        """
        本接口用于重试设备升级任务
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDeviceFirmwareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDeviceFirmwareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetForwardAuth(
            self,
            request: models.SetForwardAuthRequest,
            opts: Dict = None,
    ) -> models.SetForwardAuthResponse:
        """
        设置转发权限
        """
        
        kwargs = {}
        kwargs["action"] = "SetForwardAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetForwardAuthResponse
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
        
    async def UpdateAIModelChannel(
            self,
            request: models.UpdateAIModelChannelRequest,
            opts: Dict = None,
    ) -> models.UpdateAIModelChannelResponse:
        """
        更新AI推理结果推送配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAIModelChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAIModelChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFirmware(
            self,
            request: models.UploadFirmwareRequest,
            opts: Dict = None,
    ) -> models.UploadFirmwareResponse:
        """
        本接口（UploadFirmware）用于上传设备固件信息
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFirmware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFirmwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WakeUpDevice(
            self,
            request: models.WakeUpDeviceRequest,
            opts: Dict = None,
    ) -> models.WakeUpDeviceResponse:
        """
        设备唤醒
        """
        
        kwargs = {}
        kwargs["action"] = "WakeUpDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WakeUpDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)