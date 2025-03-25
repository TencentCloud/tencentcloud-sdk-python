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
from tencentcloud.iotvideo.v20211125 import models


class IotvideoClient(AbstractClient):
    _apiVersion = '2021-11-25'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'


    def ApplyAIModel(self, request):
        """申请AI模型

        :param request: Request instance for ApplyAIModel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ApplyAIModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ApplyAIModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyAIModel", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyAIModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchUpdateFirmware(self, request):
        """本接口（BatchUpdateFirmware）用于批量更新设备固件

        :param request: Request instance for BatchUpdateFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.BatchUpdateFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.BatchUpdateFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchUpdateFirmware", params, headers=headers)
            response = json.loads(body)
            model = models.BatchUpdateFirmwareResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.BindCloudStorageUserRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.BindCloudStorageUserResponse`

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


    def CallDeviceActionAsync(self, request):
        """异步调用设备行为

        :param request: Request instance for CallDeviceActionAsync.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionAsyncRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionAsyncResponse`

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
        """同步调用设备行为

        :param request: Request instance for CallDeviceActionSync.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionSyncRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionSyncResponse`

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


    def CallTRTCDevice(self, request):
        """呼叫TRTC设备

        :param request: Request instance for CallTRTCDevice.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CallTRTCDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CallTRTCDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallTRTCDevice", params, headers=headers)
            response = json.loads(body)
            model = models.CallTRTCDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelAIModelApplication(self, request):
        """取消AI模型申请

        :param request: Request instance for CancelAIModelApplication.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CancelAIModelApplicationRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CancelAIModelApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAIModelApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAIModelApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelDeviceFirmwareTask(self, request):
        """本接口用于取消设备升级任务

        :param request: Request instance for CancelDeviceFirmwareTask.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CancelDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CancelDeviceFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDeviceFirmwareTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelDeviceFirmwareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeP2PRoute(self, request):
        """p2p路线切换（此接口目前处于内测接口，可以联系申请加白 ）

        :param request: Request instance for ChangeP2PRoute.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ChangeP2PRouteRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ChangeP2PRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeP2PRoute", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeP2PRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckForwardAuth(self, request):
        """判断是否开启转发的权限

        :param request: Request instance for CheckForwardAuth.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CheckForwardAuthRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CheckForwardAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckForwardAuth", params, headers=headers)
            response = json.loads(body)
            model = models.CheckForwardAuthResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ControlDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ControlDeviceDataResponse`

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


    def CreateAIDetection(self, request):
        """发起AI推理请求

        :param request: Request instance for CreateAIDetection.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateAIDetectionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateAIDetectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIDetection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIDetectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBatch(self, request):
        """创建批次

        :param request: Request instance for CreateBatch.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateBatchRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCOSCredentials(self, request):
        """创建COS上传密钥

        :param request: Request instance for CreateCOSCredentials.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateCOSCredentialsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateCOSCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCOSCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCOSCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudStorage(self, request):
        """开通云存服务

        :param request: Request instance for CreateCloudStorage.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateCloudStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudStorage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataForward(self, request):
        """创建数据转发

        :param request: Request instance for CreateDataForward.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateDataForwardRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateDataForwardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataForward", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataForwardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceChannel(self, request):
        """创建设备通道

        :param request: Request instance for CreateDeviceChannel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateDeviceChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateDeviceChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateForwardRule(self, request):
        """创建转发规则

        :param request: Request instance for CreateForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFreeCloudStorage(self, request):
        """开通免费云存服务

        :param request: Request instance for CreateFreeCloudStorage.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateFreeCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateFreeCloudStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFreeCloudStorage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFreeCloudStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProduct(self, request):
        """创建产品

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProduct", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFileUrl(self, request):
        """本接口（CreateTaskFileUrl）用于获取产品级任务文件上传链接

        :param request: Request instance for CreateTaskFileUrl.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateTaskFileUrlRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateTaskFileUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFileUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFileUrlResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DeleteCloudStorageEventRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DeleteCloudStorageEventResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DeleteDeviceResponse`

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


    def DeleteFirmware(self, request):
        """本接口（DeleteFirmware）用于删除固件

        :param request: Request instance for DeleteFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DeleteFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DeleteFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFirmware", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFirmwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteForwardRule(self, request):
        """删除转发规则

        :param request: Request instance for DeleteForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DeleteForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DeleteForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProduct(self, request):
        """删除产品

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIModelApplications(self, request):
        """用户AI模型申请记录

        :param request: Request instance for DescribeAIModelApplications.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelApplicationsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIModelApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIModelApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIModelChannel(self, request):
        """查看AI推理结果推送配置

        :param request: Request instance for DescribeAIModelChannel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIModelChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIModelChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIModelUsage(self, request):
        """查看AI模型资源包

        :param request: Request instance for DescribeAIModelUsage.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelUsageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIModelUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIModelUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIModels(self, request):
        """拉取AI模型列表

        :param request: Request instance for DescribeAIModels.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAIModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIModels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccount(self, request):
        """获取消费版账号信息

        :param request: Request instance for DescribeAccount.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAccountRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBalance(self, request):
        """查询账户余额

        :param request: Request instance for DescribeBalance.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBalanceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBalance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBalanceTransactions(self, request):
        """拉取账户流水

        :param request: Request instance for DescribeBalanceTransactions.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBalanceTransactionsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBalanceTransactionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBalanceTransactions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBalanceTransactionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatch(self, request):
        """获取批次详情

        :param request: Request instance for DescribeBatch.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBatchRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchs(self, request):
        """获取批次列表

        :param request: Request instance for DescribeBatchs.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBatchsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBatchsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBonuses(self, request):
        """查看运营活动资源包列表

        :param request: Request instance for DescribeBonuses.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBonusesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeBonusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBonuses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBonusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCategory(self, request):
        """获取Category详情

        :param request: Request instance for DescribeCategory.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCategoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCategoryResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageResponse`

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


    def DescribeCloudStorageDate(self, request):
        """获取具有云存的日期

        :param request: Request instance for DescribeCloudStorageDate.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageDateRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageDateResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageEventsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageEventsResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageMultiThumbnailRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageMultiThumbnailResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageOrderRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageOrderResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStoragePackageConsumeDetailsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStoragePackageConsumeDetailsResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStoragePackageConsumeStatsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStoragePackageConsumeStatsResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageStreamDataRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageStreamDataResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageThumbnailRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageThumbnailResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageThumbnailListRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageThumbnailListResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageTimeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageTimeResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageUsersRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeCloudStorageUsersResponse`

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


    def DescribeDataForwardList(self, request):
        """获取数据转发列表

        :param request: Request instance for DescribeDataForwardList.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDataForwardListRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDataForwardListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataForwardList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataForwardListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevice(self, request):
        """查看设备详情

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceResponse`

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


    def DescribeDeviceActionHistory(self, request):
        """为用户提供获取动作历史的能力。

        :param request: Request instance for DescribeDeviceActionHistory.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceActionHistoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceActionHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceActionHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceActionHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceCommLog(self, request):
        """获取设备在指定时间范围内的通讯日志

        :param request: Request instance for DescribeDeviceCommLog.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceCommLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceCommLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceCommLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceCommLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceData(self, request):
        """获取设备属性数据

        :param request: Request instance for DescribeDeviceData.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataHistoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataHistoryResponse`

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


    def DescribeDeviceDataStats(self, request):
        """查询设备数据统计

        :param request: Request instance for DescribeDeviceDataStats.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataStatsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceDataStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceDataStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceEventHistory(self, request):
        """获取设备的历史事件

        :param request: Request instance for DescribeDeviceEventHistory.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceEventHistoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceEventHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceEventHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceEventHistoryResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDevicePackagesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDevicePackagesResponse`

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


    def DescribeDeviceStatusLog(self, request):
        """获取设备上下线日志

        :param request: Request instance for DescribeDeviceStatusLog.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceStatusLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceStatusLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceStatusLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceStatusLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevices(self, request):
        """获取设备列表

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmware(self, request):
        """本接口（DescribeFirmware）用于查询固件信息

        :param request: Request instance for DescribeFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareResponse`

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
        """此接口查询固件升级任务详情

        :param request: Request instance for DescribeFirmwareTask.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskResponse`

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


    def DescribeFirmwareTaskDevices(self, request):
        """本接口用于查询固件升级任务的设备列表

        :param request: Request instance for DescribeFirmwareTaskDevices.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTaskDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareTaskDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmwareTaskDistribution(self, request):
        """本接口用于查询固件升级任务状态分布

        :param request: Request instance for DescribeFirmwareTaskDistribution.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskDistributionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTaskDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareTaskDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmwareTaskStatistics(self, request):
        """本接口用于查询固件升级任务统计信息

        :param request: Request instance for DescribeFirmwareTaskStatistics.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTaskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTaskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareTaskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirmwareTasks(self, request):
        """本接口用于查询固件升级任务列表

        :param request: Request instance for DescribeFirmwareTasks.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTasksRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFirmwareTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirmwareTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForwardRule(self, request):
        """获取产品转发规则

        :param request: Request instance for DescribeForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFreeCloudStorageNum(self, request):
        """查询云存卡套餐信息

        :param request: Request instance for DescribeFreeCloudStorageNum.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFreeCloudStorageNumRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeFreeCloudStorageNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFreeCloudStorageNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFreeCloudStorageNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageDataStats(self, request):
        """查询设备消息数量统计

        :param request: Request instance for DescribeMessageDataStats.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeMessageDataStatsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeMessageDataStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageDataStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageDataStatsResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeModelDefinitionResponse`

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


    def DescribeP2PInfo(self, request):
        """拉取设备p2p信息

        :param request: Request instance for DescribeP2PInfo.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeP2PInfoRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeP2PInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeP2PInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeP2PInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeP2PRoute(self, request):
        """当前p2p线路

        :param request: Request instance for DescribeP2PRoute.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeP2PRouteRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeP2PRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeP2PRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeP2PRouteResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribePackageConsumeTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribePackageConsumeTaskResponse`

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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribePackageConsumeTasksRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribePackageConsumeTasksResponse`

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


    def DescribeProduct(self, request):
        """获取产品详情

        :param request: Request instance for DescribeProduct.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductDynamicRegister(self, request):
        """获取产品动态注册详情

        :param request: Request instance for DescribeProductDynamicRegister.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeProductDynamicRegisterRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeProductDynamicRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductDynamicRegister", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductDynamicRegisterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProducts(self, request):
        """获取产品列表

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePushChannel(self, request):
        """查看推送通道

        :param request: Request instance for DescribePushChannel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribePushChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribePushChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePushChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSDKLog(self, request):
        """获取设备sdk日志

        :param request: Request instance for DescribeSDKLog.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeSDKLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeSDKLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSDKLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSDKLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUser(self, request):
        """获取video消费版用户信息

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditFirmware(self, request):
        """本接口用于编辑固件信息

        :param request: Request instance for EditFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.EditFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.EditFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditFirmware", params, headers=headers)
            response = json.loads(body)
            model = models.EditFirmwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenSingleDeviceSignatureOfPublic(self, request):
        """获取设备的绑定签名

        :param request: Request instance for GenSingleDeviceSignatureOfPublic.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.GenSingleDeviceSignatureOfPublicRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.GenSingleDeviceSignatureOfPublicResponse`

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


    def GenerateSignedVideoURL(self, request):
        """获取视频防盗链播放URL

        :param request: Request instance for GenerateSignedVideoURL.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.GenerateSignedVideoURLRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.GenerateSignedVideoURLResponse`

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


    def GetAllFirmwareVersion(self, request):
        """本接口（GetAllFirmwareVersion）用于获取所有的版本列表

        :param request: Request instance for GetAllFirmwareVersion.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.GetAllFirmwareVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.GetAllFirmwareVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAllFirmwareVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetAllFirmwareVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFirmwareURL(self, request):
        """本接口（GetFirmwareURL）用于获取固件存储的URL

        :param request: Request instance for GetFirmwareURL.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.GetFirmwareURLRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.GetFirmwareURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFirmwareURL", params, headers=headers)
            response = json.loads(body)
            model = models.GetFirmwareURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportModelDefinition(self, request):
        """导入其它产品的数据模板，覆盖现有数据模板的物模型和产品分类信息

        :param request: Request instance for ImportModelDefinition.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ImportModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ImportModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportModelDefinition", params, headers=headers)
            response = json.loads(body)
            model = models.ImportModelDefinitionResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.InheritCloudStorageUserRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.InheritCloudStorageUserResponse`

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


    def ListFirmwares(self, request):
        """本接口（ListFirmwares）用于获取固件列表

        :param request: Request instance for ListFirmwares.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ListFirmwaresRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ListFirmwaresResponse`

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


    def ModifyDataForward(self, request):
        """修改数据转发

        :param request: Request instance for ModifyDataForward.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDataForwardRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDataForwardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataForward", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataForwardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataForwardStatus(self, request):
        """设置数据转发状态

        :param request: Request instance for ModifyDataForwardStatus.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDataForwardStatusRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDataForwardStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataForwardStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataForwardStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDevice(self, request):
        """修改设备信息

        :param request: Request instance for ModifyDevice.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDeviceResponse`

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


    def ModifyDeviceLogLevel(self, request):
        """更新设备日志级别

        :param request: Request instance for ModifyDeviceLogLevel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDeviceLogLevelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyDeviceLogLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceLogLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceLogLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyForwardRule(self, request):
        """修改转发规则

        :param request: Request instance for ModifyForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyForwardRuleResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyModelDefinitionResponse`

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


    def ModifyProduct(self, request):
        """修改产品信息

        :param request: Request instance for ModifyProduct.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProduct", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProductDynamicRegister(self, request):
        """修改产品动态注册

        :param request: Request instance for ModifyProductDynamicRegister.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyProductDynamicRegisterRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyProductDynamicRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProductDynamicRegister", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProductDynamicRegisterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPushChannel(self, request):
        """更新推送通道

        :param request: Request instance for ModifyPushChannel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ModifyPushChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ModifyPushChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPushChannel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPushChannelResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.PublishMessageResponse`

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


    def ReportAliveDevice(self, request):
        """上报活跃设备

        :param request: Request instance for ReportAliveDevice.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ReportAliveDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ReportAliveDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportAliveDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ReportAliveDeviceResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ResetCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ResetCloudStorageResponse`

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


    def ResetCloudStorageEvent(self, request):
        """重置云存事件

        :param request: Request instance for ResetCloudStorageEvent.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.ResetCloudStorageEventRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.ResetCloudStorageEventResponse`

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


    def RetryDeviceFirmwareTask(self, request):
        """本接口用于重试设备升级任务

        :param request: Request instance for RetryDeviceFirmwareTask.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.RetryDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.RetryDeviceFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDeviceFirmwareTask", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDeviceFirmwareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetForwardAuth(self, request):
        """设置转发权限

        :param request: Request instance for SetForwardAuth.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.SetForwardAuthRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.SetForwardAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetForwardAuth", params, headers=headers)
            response = json.loads(body)
            model = models.SetForwardAuthResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.TransferCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.TransferCloudStorageResponse`

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


    def UpdateAIModelChannel(self, request):
        """更新AI推理结果推送配置

        :param request: Request instance for UpdateAIModelChannel.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.UpdateAIModelChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.UpdateAIModelChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAIModelChannel", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAIModelChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadFirmware(self, request):
        """本接口（UploadFirmware）用于上传设备固件信息

        :param request: Request instance for UploadFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.UploadFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.UploadFirmwareResponse`

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


    def WakeUpDevice(self, request):
        """设备唤醒

        :param request: Request instance for WakeUpDevice.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.WakeUpDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.WakeUpDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WakeUpDevice", params, headers=headers)
            response = json.loads(body)
            model = models.WakeUpDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))