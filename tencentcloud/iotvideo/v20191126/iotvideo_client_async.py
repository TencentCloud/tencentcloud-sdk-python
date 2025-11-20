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
from tencentcloud.iotvideo.v20191126 import models
from typing import Dict


class IotvideoClient(AbstractClient):
    _apiVersion = '2019-11-26'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'

    async def ClearDeviceActiveCode(
            self,
            request: models.ClearDeviceActiveCodeRequest,
            opts: Dict = None,
    ) -> models.ClearDeviceActiveCodeResponse:
        """
        清除设备激活码
        """
        
        kwargs = {}
        kwargs["action"] = "ClearDeviceActiveCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearDeviceActiveCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAnonymousAccessToken(
            self,
            request: models.CreateAnonymousAccessTokenRequest,
            opts: Dict = None,
    ) -> models.CreateAnonymousAccessTokenResponse:
        """
        创建匿名访问Token
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAnonymousAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAnonymousAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAppUsr(
            self,
            request: models.CreateAppUsrRequest,
            opts: Dict = None,
    ) -> models.CreateAppUsrResponse:
        """
        本接口（CreateAppUsr）用于接收由厂商云发送过来的注册请求,建立厂商云终端用户与IoT Video终端用户的映射关系。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppUsr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppUsrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBinding(
            self,
            request: models.CreateBindingRequest,
            opts: Dict = None,
    ) -> models.CreateBindingResponse:
        """
        本接口（CreateBinding）用于终端用户和设备进行绑定，具体的应用场景如下：
            终端用户与设备具有“强关联”关系。用户与设备绑定之后，用户终端即具备了该设备的访问权限,访问或操作设备时，无需获取设备访问Token。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevToken(
            self,
            request: models.CreateDevTokenRequest,
            opts: Dict = None,
    ) -> models.CreateDevTokenResponse:
        """
        本接口（CreateDevToken）用于以下场景：
        终端用户与设备没有强绑定关联关系;
        允许终端用户短时或一次性临时访问设备;
        当终端用户与设备有强绑定关系时，可以不用调用此接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDevTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevices(
            self,
            request: models.CreateDevicesRequest,
            opts: Dict = None,
    ) -> models.CreateDevicesResponse:
        """
        本接口（CreateDevices）用于批量创建新的物联网视频通信设备。
        注意：腾讯云不会对设备私钥进行保存，请自行保管好您的设备私钥。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGencode(
            self,
            request: models.CreateGencodeRequest,
            opts: Dict = None,
    ) -> models.CreateGencodeResponse:
        """
        本接口（CreateGencode）用于生成设备物模型源代码
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGencode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGencodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIotDataType(
            self,
            request: models.CreateIotDataTypeRequest,
            opts: Dict = None,
    ) -> models.CreateIotDataTypeResponse:
        """
        本接口（CreateIotDataType）用于创建自定义物模型数据类型。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIotDataType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIotDataTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIotModel(
            self,
            request: models.CreateIotModelRequest,
            opts: Dict = None,
    ) -> models.CreateIotModelResponse:
        """
        本接口（CreateIotModel）用于定义的物模型提交。
        该接口实现了物模型草稿箱的功能，保存用户最后一次编辑的物模型数据。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIotModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIotModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProduct(
            self,
            request: models.CreateProductRequest,
            opts: Dict = None,
    ) -> models.CreateProductResponse:
        """
        本接口（CreateProduct）用于创建一个新的物联网智能视频产品。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorage(
            self,
            request: models.CreateStorageRequest,
            opts: Dict = None,
    ) -> models.CreateStorageResponse:
        """
        该接口已经停止维护，请勿使用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorageService(
            self,
            request: models.CreateStorageServiceRequest,
            opts: Dict = None,
    ) -> models.CreateStorageServiceResponse:
        """
        购买云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorageService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTraceIds(
            self,
            request: models.CreateTraceIdsRequest,
            opts: Dict = None,
    ) -> models.CreateTraceIdsResponse:
        """
        本接口（CreateTraceIds）用于将设备加到日志跟踪白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTraceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTraceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUploadPath(
            self,
            request: models.CreateUploadPathRequest,
            opts: Dict = None,
    ) -> models.CreateUploadPathResponse:
        """
        本接口（CreateUploadPath）用于获取固件上传路径。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUploadPath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUploadPathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUploadTest(
            self,
            request: models.CreateUploadTestRequest,
            opts: Dict = None,
    ) -> models.CreateUploadTestResponse:
        """
        设备申请cos上传证书
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUploadTest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUploadTestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsrToken(
            self,
            request: models.CreateUsrTokenRequest,
            opts: Dict = None,
    ) -> models.CreateUsrTokenResponse:
        """
        本接口（CreateUsrToken）用于终端用户获取IoT Video平台的accessToken，初始化SDK,连接到IoT Video接入服务器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsrToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsrTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppUsr(
            self,
            request: models.DeleteAppUsrRequest,
            opts: Dict = None,
    ) -> models.DeleteAppUsrResponse:
        """
        本接口（DeleteAppUsr）用于删除终端用户。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppUsr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppUsrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBinding(
            self,
            request: models.DeleteBindingRequest,
            opts: Dict = None,
    ) -> models.DeleteBindingResponse:
        """
        本接口（DeleteBinding）用于终端用户和设备进行解绑定。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        本接口（DeleteDevice）用于删除设备，可进行批量操作，每次操作最多100台设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIotDataType(
            self,
            request: models.DeleteIotDataTypeRequest,
            opts: Dict = None,
    ) -> models.DeleteIotDataTypeResponse:
        """
        本接口（DeleteIotDataType）用于删除自定义物模型数据类型。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIotDataType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIotDataTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMessageQueue(
            self,
            request: models.DeleteMessageQueueRequest,
            opts: Dict = None,
    ) -> models.DeleteMessageQueueResponse:
        """
        本接口（DeleteMessageQueue）用于删除物联网智能视频产品的转发消息配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMessageQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMessageQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOtaVersion(
            self,
            request: models.DeleteOtaVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteOtaVersionResponse:
        """
        本接口（DeleteOtaVersion）用于删除固件版本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOtaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOtaVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProduct(
            self,
            request: models.DeleteProductRequest,
            opts: Dict = None,
    ) -> models.DeleteProductResponse:
        """
        本接口（DeleteProduct）用于删除一个物联网智能视频产品。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTraceIds(
            self,
            request: models.DeleteTraceIdsRequest,
            opts: Dict = None,
    ) -> models.DeleteTraceIdsResponse:
        """
        本接口（DeleteTraceIds）用于将设备从日志跟踪白名单中删除，该接口可批量操作，最多支持同时操作100台设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTraceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTraceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeliverStorageService(
            self,
            request: models.DeliverStorageServiceRequest,
            opts: Dict = None,
    ) -> models.DeliverStorageServiceResponse:
        """
        将已购买的云存服务转移到另一设备
        """
        
        kwargs = {}
        kwargs["action"] = "DeliverStorageService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeliverStorageServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountBalance(
            self,
            request: models.DescribeAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountBalanceResponse:
        """
        客户可通过本接口获取账户余额信息, 默认接口请求频率限制：1次/秒
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindDev(
            self,
            request: models.DescribeBindDevRequest,
            opts: Dict = None,
    ) -> models.DescribeBindDevResponse:
        """
        本接口（DescribeBindDev）用于查询终端用户绑定的设备列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindDev"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindDevResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindUsr(
            self,
            request: models.DescribeBindUsrRequest,
            opts: Dict = None,
    ) -> models.DescribeBindUsrResponse:
        """
        本接口（DescribeBindUsr）用于查询设备被分享的所有用户列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindUsr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindUsrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevice(
            self,
            request: models.DescribeDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResponse:
        """
        本接口（DescribeDevice）获取设备信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceModel(
            self,
            request: models.DescribeDeviceModelRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceModelResponse:
        """
        本接口（DescribeDeviceModel）用于获取设备物模型。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        本接口（DescribeDevices）用于获取设备信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIotDataType(
            self,
            request: models.DescribeIotDataTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeIotDataTypeResponse:
        """
        本接口（DescribeIotDataType）用于查询自定义的物模型数据类型。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIotDataType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIotDataTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIotModel(
            self,
            request: models.DescribeIotModelRequest,
            opts: Dict = None,
    ) -> models.DescribeIotModelResponse:
        """
        本接口（DescribeIotModel）用于获取物模型定义详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIotModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIotModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIotModels(
            self,
            request: models.DescribeIotModelsRequest,
            opts: Dict = None,
    ) -> models.DescribeIotModelsResponse:
        """
        本接口（DescribeIotModels）用于列出物模型历史版本列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIotModels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIotModelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogs(
            self,
            request: models.DescribeLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogsResponse:
        """
        本接口（DescribeLogs）用于查询设备日志列表。
        设备日志最长保留时长为15天,超期自动清除。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageQueue(
            self,
            request: models.DescribeMessageQueueRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageQueueResponse:
        """
        本接口（DescribeMessageQueue）用于查询物联网智能视频产品转发消息配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelDataRet(
            self,
            request: models.DescribeModelDataRetRequest,
            opts: Dict = None,
    ) -> models.DescribeModelDataRetResponse:
        """
        本接口（DescribeModelDataRet）用于根据TaskId获取对设备物模型操作最终响应的结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelDataRet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelDataRetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOsList(
            self,
            request: models.DescribeOsListRequest,
            opts: Dict = None,
    ) -> models.DescribeOsListResponse:
        """
        查看操作系统支持的芯片列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOtaVersions(
            self,
            request: models.DescribeOtaVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeOtaVersionsResponse:
        """
        本接口（DescribeOtaVersions）用于查询固件版本信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOtaVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOtaVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProduct(
            self,
            request: models.DescribeProductRequest,
            opts: Dict = None,
    ) -> models.DescribeProductResponse:
        """
        本接口（DescribeProduct）用于获取单个产品的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducts(
            self,
            request: models.DescribeProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductsResponse:
        """
        本接口（DescribeProducts）用于列出用户账号下的物联网智能视频产品列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePubVersions(
            self,
            request: models.DescribePubVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribePubVersionsResponse:
        """
        本接口（DescribePubVersions）用于获取某一产品发布过的全部固件版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePubVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePubVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRechargeRecords(
            self,
            request: models.DescribeRechargeRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeRechargeRecordsResponse:
        """
        客户可通过本接口获取充值记录信息, 一次最多返回50条记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRechargeRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRechargeRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistrationStatus(
            self,
            request: models.DescribeRegistrationStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistrationStatusResponse:
        """
        本接口（DescribeRegistrationStatus）用于查询终端用户的注册状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistrationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistrationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRunLog(
            self,
            request: models.DescribeRunLogRequest,
            opts: Dict = None,
    ) -> models.DescribeRunLogResponse:
        """
        本接口（DescribeRunLog）用于获取设备运行日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRunLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRunLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageService(
            self,
            request: models.DescribeStorageServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageServiceResponse:
        """
        查询云存服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStream(
            self,
            request: models.DescribeStreamRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamResponse:
        """
        请求设备直播流地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTraceIds(
            self,
            request: models.DescribeTraceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeTraceIdsResponse:
        """
        本接口（DescribeTraceIds）用于查询设备日志跟踪白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTraceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTraceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTraceStatus(
            self,
            request: models.DescribeTraceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTraceStatusResponse:
        """
        本接口（DescribeTraceStatus）用于查询指定设备是否在白名单中。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTraceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTraceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDevice(
            self,
            request: models.DisableDeviceRequest,
            opts: Dict = None,
    ) -> models.DisableDeviceResponse:
        """
        本接口（DisableDevice）用于禁用设备，可进行批量操作，每次操作最多100台设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDeviceStream(
            self,
            request: models.DisableDeviceStreamRequest,
            opts: Dict = None,
    ) -> models.DisableDeviceStreamResponse:
        """
        本接口（DisableDeviceStream）用于停止设备推流，可进行批量操作，每次操作最多100台设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDeviceStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDeviceStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableOtaVersion(
            self,
            request: models.DisableOtaVersionRequest,
            opts: Dict = None,
    ) -> models.DisableOtaVersionResponse:
        """
        本接口（DisableOtaVersion）用于禁用固件版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableOtaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableOtaVersionResponse
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
        
    async def ModifyDeviceAction(
            self,
            request: models.ModifyDeviceActionRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceActionResponse:
        """
        本接口（ModifyDeviceAction）用于修改设备物模型的行为（Action）。

        可对ctlVal数据属性进行写入,如:Action.takePhoto.ctlVal,设备在线且成功发送到设备才返回,物模型写入数据时,不需要传入时标信息,平台以当前时标作为数据的时标更新物模型中的时标信息。
        注意:
          1.若设备当前不在线,会直接返回错误
          2.若设备网络出现异常时,消息发送可能超时,超时等待最长时间为3秒
          3.value的内容必须与实际物模型的定义一致
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceProperty(
            self,
            request: models.ModifyDevicePropertyRequest,
            opts: Dict = None,
    ) -> models.ModifyDevicePropertyResponse:
        """
        本接口（ModifyDeviceProperty）用于修改设备物模型的属性（ProWritable）。
        可对setVal数据属性进行写入,如:
        ProWritable.Pos.setVal
        对于嵌套类型的可写属性，可以仅对其部分数据内容进行写入，如:
        ProWritable.Pos.setVal.x;
        可写属性云端写入成功即返回;云端向设备端发布属性变更参数;若当前设备不在线,在设备下次上线时会自动更新这些属性参数;
        物模型写入数据时,不需要传入时标信息,平台以当前时标作为数据的时标更新物模型中的时标信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDevicePropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProduct(
            self,
            request: models.ModifyProductRequest,
            opts: Dict = None,
    ) -> models.ModifyProductResponse:
        """
        本接口（ModifyProduct）用于编辑物联网智能视频产品的相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVerContent(
            self,
            request: models.ModifyVerContentRequest,
            opts: Dict = None,
    ) -> models.ModifyVerContentResponse:
        """
        编辑版本描述信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVerContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVerContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundStorageService(
            self,
            request: models.RefundStorageServiceRequest,
            opts: Dict = None,
    ) -> models.RefundStorageServiceResponse:
        """
        本接口（RefundStorageService）用于退订已购买的云存服务。
        退订时，云存服务对应订单的处理方式 :
        1. 未开始的订单自动回到已付费订单池
        2. 已开始的订单自动失效
        3. 购买云存接口,优先从已付费订单池中分配订单
        """
        
        kwargs = {}
        kwargs["action"] = "RefundStorageService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundStorageServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewUploadTest(
            self,
            request: models.RenewUploadTestRequest,
            opts: Dict = None,
    ) -> models.RenewUploadTestResponse:
        """
        设备刷新cos上传证书
        """
        
        kwargs = {}
        kwargs["action"] = "RenewUploadTest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewUploadTestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunDevice(
            self,
            request: models.RunDeviceRequest,
            opts: Dict = None,
    ) -> models.RunDeviceResponse:
        """
        本接口（RunDevice）用于启用设备，可进行批量操作，每次操作最多100台设备。
        """
        
        kwargs = {}
        kwargs["action"] = "RunDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunDeviceStream(
            self,
            request: models.RunDeviceStreamRequest,
            opts: Dict = None,
    ) -> models.RunDeviceStreamResponse:
        """
        本接口（RunDeviceStream）用于开启设备推流，可进行批量操作，每次操作最多100台设备。
        """
        
        kwargs = {}
        kwargs["action"] = "RunDeviceStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunDeviceStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunIotModel(
            self,
            request: models.RunIotModelRequest,
            opts: Dict = None,
    ) -> models.RunIotModelResponse:
        """
        本接口（RunIotModel）用于对定义的物模型进行发布。
        """
        
        kwargs = {}
        kwargs["action"] = "RunIotModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunIotModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunOtaVersion(
            self,
            request: models.RunOtaVersionRequest,
            opts: Dict = None,
    ) -> models.RunOtaVersionResponse:
        """
        本接口（RunOtaVersion）用于固件版本正式发布。
        """
        
        kwargs = {}
        kwargs["action"] = "RunOtaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunOtaVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunTestOtaVersion(
            self,
            request: models.RunTestOtaVersionRequest,
            opts: Dict = None,
    ) -> models.RunTestOtaVersionResponse:
        """
        本接口（RunTestOtaVersion）用于固件版本测试发布。
        """
        
        kwargs = {}
        kwargs["action"] = "RunTestOtaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunTestOtaVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendOnlineMsg(
            self,
            request: models.SendOnlineMsgRequest,
            opts: Dict = None,
    ) -> models.SendOnlineMsgResponse:
        """
        本接口（SendOnlineMsg）用于向设备发送在线消息。
        注意：
        若设备当前不在线,会直接返回错误;
        若设备网络出现异常时,消息发送可能超时,超时等待最长时间为3秒.waitresp非0情况下,会导致本接口阻塞3秒。
        """
        
        kwargs = {}
        kwargs["action"] = "SendOnlineMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendOnlineMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetMessageQueue(
            self,
            request: models.SetMessageQueueRequest,
            opts: Dict = None,
    ) -> models.SetMessageQueueResponse:
        """
        本接口（SetMessageQueue）用于配置物联网智能视频产品的转发消息队列。
        """
        
        kwargs = {}
        kwargs["action"] = "SetMessageQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetMessageQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDevice(
            self,
            request: models.UpgradeDeviceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDeviceResponse:
        """
        本接口（UpgradeDevice）用于对设备进行固件升级。
        该接口向指定的设备下发固件更新指令,可将固件升级到任意版本(可实现固件降级)。
        警告:使能UpgradeNow参数存在一定的风险性！建议仅在debug场景下使用!
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadOtaVersion(
            self,
            request: models.UploadOtaVersionRequest,
            opts: Dict = None,
    ) -> models.UploadOtaVersionResponse:
        """
        本接口（UploadOtaVersion）接收上传到控制台的固件版本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadOtaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadOtaVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)