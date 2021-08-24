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
from tencentcloud.iotvideo.v20201215 import models


class IotvideoClient(AbstractClient):
    _apiVersion = '2020-12-15'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'


    def ApplyAIModel(self, request):
        """申请AI模型

        :param request: Request instance for ApplyAIModel.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ApplyAIModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ApplyAIModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyAIModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyAIModelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchUpdateFirmware(self, request):
        """本接口（BatchUpdateFirmware）用于批量更新设备固件

        :param request: Request instance for BatchUpdateFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.BatchUpdateFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.BatchUpdateFirmwareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchUpdateFirmware", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchUpdateFirmwareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindCloudStorageUser(self, request):
        """绑定云存用户

        :param request: Request instance for BindCloudStorageUser.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.BindCloudStorageUserRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.BindCloudStorageUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindCloudStorageUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindCloudStorageUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelAIModelApplication(self, request):
        """取消AI模型申请

        :param request: Request instance for CancelAIModelApplication.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CancelAIModelApplicationRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CancelAIModelApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelAIModelApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelAIModelApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelDeviceFirmwareTask(self, request):
        """本接口用于取消设备升级任务

        :param request: Request instance for CancelDeviceFirmwareTask.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CancelDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CancelDeviceFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelDeviceFirmwareTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelDeviceFirmwareTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckForwardAuth(self, request):
        """判断是否开启的转发的权限

        :param request: Request instance for CheckForwardAuth.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CheckForwardAuthRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CheckForwardAuthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckForwardAuth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckForwardAuthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlDeviceData(self, request):
        """根据设备产品ID、设备名称，设置控制设备的属性数据。

        :param request: Request instance for ControlDeviceData.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ControlDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ControlDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ControlDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlDeviceDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAIDetection(self, request):
        """发起AI推理请求

        :param request: Request instance for CreateAIDetection.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateAIDetectionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateAIDetectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAIDetection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAIDetectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBatch(self, request):
        """创建批次

        :param request: Request instance for CreateBatch.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateBatchRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCOSCredentials(self, request):
        """创建COS上传密钥

        :param request: Request instance for CreateCOSCredentials.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateCOSCredentialsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateCOSCredentialsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCOSCredentials", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCOSCredentialsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCloudStorage(self, request):
        """开通云存服务

        :param request: Request instance for CreateCloudStorage.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateCloudStorageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCloudStorage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCloudStorageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDataForward(self, request):
        """创建数据转发

        :param request: Request instance for CreateDataForward.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateDataForwardRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateDataForwardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDataForward", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDataForwardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateForwardRule(self, request):
        """创建转发规则

        :param request: Request instance for CreateForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateForwardRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateForwardRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateForwardRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProduct(self, request):
        """创建产品

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTaskFileUrl(self, request):
        """本接口（CreateTaskFileUrl）用于获取产品级任务文件上传链接

        :param request: Request instance for CreateTaskFileUrl.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.CreateTaskFileUrlRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.CreateTaskFileUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskFileUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskFileUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDevice(self, request):
        """删除设备

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFirmware(self, request):
        """本接口（DeleteFirmware）用于删除固件

        :param request: Request instance for DeleteFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DeleteFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DeleteFirmwareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFirmware", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFirmwareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteForwardRule(self, request):
        """删除转发规则

        :param request: Request instance for DeleteForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DeleteForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DeleteForwardRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteForwardRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteForwardRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProduct(self, request):
        """删除产品

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAIModelApplications(self, request):
        """用户AI模型申请记录

        :param request: Request instance for DescribeAIModelApplications.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelApplicationsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIModelApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIModelApplicationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAIModelChannel(self, request):
        """查看AI推理结果推送配置

        :param request: Request instance for DescribeAIModelChannel.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIModelChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIModelChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAIModelUsage(self, request):
        """查看AI模型资源包

        :param request: Request instance for DescribeAIModelUsage.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelUsageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIModelUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIModelUsageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAIModels(self, request):
        """拉取AI模型列表

        :param request: Request instance for DescribeAIModels.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeAIModelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIModels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIModelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBalance(self, request):
        """查询账户余额

        :param request: Request instance for DescribeBalance.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBalanceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBalanceTransactions(self, request):
        """拉取账户流水

        :param request: Request instance for DescribeBalanceTransactions.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBalanceTransactionsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBalanceTransactionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBalanceTransactions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBalanceTransactionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBatch(self, request):
        """获取批次详情

        :param request: Request instance for DescribeBatch.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBatchRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBatchs(self, request):
        """获取批次列表

        :param request: Request instance for DescribeBatchs.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBatchsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeBatchsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBatchs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBatchsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCategory(self, request):
        """获取Category详情

        :param request: Request instance for DescribeCategory.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCategoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCategoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCategory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCategoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudStorage(self, request):
        """获取设备云存服务详情

        :param request: Request instance for DescribeCloudStorage.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudStorage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudStorageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudStorageDate(self, request):
        """获取具有云存的日期

        :param request: Request instance for DescribeCloudStorageDate.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageDateRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageDateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudStorageDate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudStorageDateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudStorageEvents(self, request):
        """拉取云存事件列表

        :param request: Request instance for DescribeCloudStorageEvents.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageEventsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudStorageEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudStorageEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudStorageThumbnail(self, request):
        """拉取云存事件缩略图

        :param request: Request instance for DescribeCloudStorageThumbnail.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageThumbnailRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageThumbnailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudStorageThumbnail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudStorageThumbnailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudStorageTime(self, request):
        """获取某一天云存时间轴

        :param request: Request instance for DescribeCloudStorageTime.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageTimeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudStorageTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudStorageTimeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudStorageUsers(self, request):
        """拉取云存用户列表

        :param request: Request instance for DescribeCloudStorageUsers.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageUsersRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeCloudStorageUsersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudStorageUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudStorageUsersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataForwardList(self, request):
        """获取数据转发列表

        :param request: Request instance for DescribeDataForwardList.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDataForwardListRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDataForwardListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDataForwardList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataForwardListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevice(self, request):
        """查看设备详情

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceActionHistory(self, request):
        """为用户提供获取动作历史的能力。

        :param request: Request instance for DescribeDeviceActionHistory.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceActionHistoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceActionHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceActionHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceActionHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceCommLog(self, request):
        """获取设备在指定时间范围内的通讯日志

        :param request: Request instance for DescribeDeviceCommLog.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceCommLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceCommLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceCommLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceCommLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceData(self, request):
        """获取设备属性数据

        :param request: Request instance for DescribeDeviceData.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceDataHistory(self, request):
        """获取设备在指定时间范围内上报的历史数据。

        :param request: Request instance for DescribeDeviceDataHistory.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceDataHistoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceDataHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceDataHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceEventHistory(self, request):
        """获取设备的历史事件

        :param request: Request instance for DescribeDeviceEventHistory.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceEventHistoryRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceEventHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceEventHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceEventHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceStatusLog(self, request):
        """获取设备上下线日志

        :param request: Request instance for DescribeDeviceStatusLog.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceStatusLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDeviceStatusLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceStatusLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceStatusLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevices(self, request):
        """获取设备列表

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmware(self, request):
        """本接口（DescribeFirmware）用于查询固件信息

        :param request: Request instance for DescribeFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirmware", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirmwareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmwareTask(self, request):
        """此接口查询固件升级任务详情

        :param request: Request instance for DescribeFirmwareTask.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirmwareTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirmwareTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmwareTaskDevices(self, request):
        """本接口用于查询固件升级任务的设备列表

        :param request: Request instance for DescribeFirmwareTaskDevices.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirmwareTaskDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirmwareTaskDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmwareTaskDistribution(self, request):
        """本接口用于查询固件升级任务状态分布

        :param request: Request instance for DescribeFirmwareTaskDistribution.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskDistributionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskDistributionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirmwareTaskDistribution", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirmwareTaskDistributionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmwareTaskStatistics(self, request):
        """本接口用于查询固件升级任务统计信息

        :param request: Request instance for DescribeFirmwareTaskStatistics.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTaskStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirmwareTaskStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirmwareTaskStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmwareTasks(self, request):
        """本接口用于查询固件升级任务列表

        :param request: Request instance for DescribeFirmwareTasks.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTasksRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeFirmwareTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirmwareTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirmwareTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeForwardRule(self, request):
        """获取产品转发规则

        :param request: Request instance for DescribeForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeForwardRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeForwardRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeForwardRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeModelDefinition(self, request):
        """查询产品配置的数据模板信息

        :param request: Request instance for DescribeModelDefinition.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModelDefinitionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProduct(self, request):
        """获取产品详情

        :param request: Request instance for DescribeProduct.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProducts(self, request):
        """获取产品列表

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProducts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSDKLog(self, request):
        """获取设备sdk日志

        :param request: Request instance for DescribeSDKLog.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.DescribeSDKLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.DescribeSDKLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSDKLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSDKLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EditFirmware(self, request):
        """本接口用于编辑固件信息

        :param request: Request instance for EditFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.EditFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.EditFirmwareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditFirmware", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditFirmwareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateSignedVideoURL(self, request):
        """获取视频防盗链播放URL

        :param request: Request instance for GenerateSignedVideoURL.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.GenerateSignedVideoURLRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.GenerateSignedVideoURLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateSignedVideoURL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateSignedVideoURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetAllFirmwareVersion(self, request):
        """本接口（GetAllFirmwareVersion）用于获取所有的版本列表

        :param request: Request instance for GetAllFirmwareVersion.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.GetAllFirmwareVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.GetAllFirmwareVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAllFirmwareVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAllFirmwareVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetFirmwareURL(self, request):
        """本接口（GetFirmwareURL）用于获取固件存储的URL

        :param request: Request instance for GetFirmwareURL.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.GetFirmwareURLRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.GetFirmwareURLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFirmwareURL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFirmwareURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportModelDefinition(self, request):
        """导入其它产品的数据模板，覆盖现有数据模板的物模型和产品分类信息

        :param request: Request instance for ImportModelDefinition.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ImportModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ImportModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportModelDefinitionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InheritCloudStorageUser(self, request):
        """继承云存用户

        :param request: Request instance for InheritCloudStorageUser.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.InheritCloudStorageUserRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.InheritCloudStorageUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InheritCloudStorageUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InheritCloudStorageUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListFirmwares(self, request):
        """本接口（ListFirmwares）用于获取固件列表

        :param request: Request instance for ListFirmwares.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ListFirmwaresRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ListFirmwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListFirmwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListFirmwaresResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDataForward(self, request):
        """修改数据转发

        :param request: Request instance for ModifyDataForward.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDataForwardRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDataForwardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDataForward", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDataForwardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDataForwardStatus(self, request):
        """设置数据转发状态

        :param request: Request instance for ModifyDataForwardStatus.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDataForwardStatusRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDataForwardStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDataForwardStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDataForwardStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDevice(self, request):
        """修改设备信息

        :param request: Request instance for ModifyDevice.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDeviceLogLevel(self, request):
        """更新设备日志级别

        :param request: Request instance for ModifyDeviceLogLevel.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDeviceLogLevelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyDeviceLogLevelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDeviceLogLevel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDeviceLogLevelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyForwardRule(self, request):
        """修改转发规则

        :param request: Request instance for ModifyForwardRule.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyForwardRuleRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyForwardRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyForwardRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyForwardRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModelDefinition(self, request):
        """提供修改产品的数据模板的能力

        :param request: Request instance for ModifyModelDefinition.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModelDefinitionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProduct(self, request):
        """修改产品信息

        :param request: Request instance for ModifyProduct.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ModifyProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ModifyProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishMessage(self, request):
        """本接口（PublishMessage）用于使用自定义透传协议进行设备远控

        :param request: Request instance for PublishMessage.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.PublishMessageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishMessage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishMessageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReportAliveDevice(self, request):
        """上报活跃设备

        :param request: Request instance for ReportAliveDevice.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ReportAliveDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ReportAliveDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReportAliveDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportAliveDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetCloudStorage(self, request):
        """重置云存服务

        :param request: Request instance for ResetCloudStorage.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.ResetCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.ResetCloudStorageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetCloudStorage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetCloudStorageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RetryDeviceFirmwareTask(self, request):
        """本接口用于重试设备升级任务

        :param request: Request instance for RetryDeviceFirmwareTask.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.RetryDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.RetryDeviceFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RetryDeviceFirmwareTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RetryDeviceFirmwareTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetForwardAuth(self, request):
        """设置转发权限

        :param request: Request instance for SetForwardAuth.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.SetForwardAuthRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.SetForwardAuthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetForwardAuth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetForwardAuthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransferCloudStorage(self, request):
        """转移云存服务

        :param request: Request instance for TransferCloudStorage.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.TransferCloudStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.TransferCloudStorageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransferCloudStorage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransferCloudStorageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAIModelChannel(self, request):
        """更新AI推理结果推送配置

        :param request: Request instance for UpdateAIModelChannel.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.UpdateAIModelChannelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.UpdateAIModelChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAIModelChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAIModelChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadFirmware(self, request):
        """本接口（UploadFirmware）用于上传设备固件信息

        :param request: Request instance for UploadFirmware.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.UploadFirmwareRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.UploadFirmwareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadFirmware", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadFirmwareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WakeUpDevice(self, request):
        """设备唤醒

        :param request: Request instance for WakeUpDevice.
        :type request: :class:`tencentcloud.iotvideo.v20201215.models.WakeUpDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20201215.models.WakeUpDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WakeUpDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WakeUpDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)