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
from tencentcloud.iotvideo.v20191126 import models


class IotvideoClient(AbstractClient):
    _apiVersion = '2019-11-26'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'


    def ClearDeviceActiveCode(self, request):
        """清除设备激活码

        :param request: Request instance for ClearDeviceActiveCode.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ClearDeviceActiveCodeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ClearDeviceActiveCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearDeviceActiveCode", params, headers=headers)
            response = json.loads(body)
            model = models.ClearDeviceActiveCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAnonymousAccessToken(self, request):
        """创建匿名访问Token

        :param request: Request instance for CreateAnonymousAccessToken.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateAnonymousAccessTokenRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateAnonymousAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAnonymousAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAnonymousAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAppUsr(self, request):
        """本接口（CreateAppUsr）用于接收由厂商云发送过来的注册请求,建立厂商云终端用户与IoT Video终端用户的映射关系。

        :param request: Request instance for CreateAppUsr.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateAppUsrRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateAppUsrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppUsr", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppUsrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBinding(self, request):
        """本接口（CreateBinding）用于终端用户和设备进行绑定，具体的应用场景如下：
            终端用户与设备具有“强关联”关系。用户与设备绑定之后，用户终端即具备了该设备的访问权限,访问或操作设备时，无需获取设备访问Token。

        :param request: Request instance for CreateBinding.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateBindingRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBinding", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDevToken(self, request):
        """本接口（CreateDevToken）用于以下场景：
        终端用户与设备没有强绑定关联关系;
        允许终端用户短时或一次性临时访问设备;
        当终端用户与设备有强绑定关系时，可以不用调用此接口

        :param request: Request instance for CreateDevToken.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevTokenRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDevTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDevices(self, request):
        """本接口（CreateDevices）用于批量创建新的物联网视频通信设备。
        注意：腾讯云不会对设备私钥进行保存，请自行保管好您的设备私钥。

        :param request: Request instance for CreateDevices.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevices", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGencode(self, request):
        """本接口（CreateGencode）用于生成设备物模型源代码

        :param request: Request instance for CreateGencode.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateGencodeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateGencodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGencode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGencodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIotDataType(self, request):
        """本接口（CreateIotDataType）用于创建自定义物模型数据类型。

        :param request: Request instance for CreateIotDataType.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotDataTypeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotDataTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIotDataType", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIotDataTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIotModel(self, request):
        """本接口（CreateIotModel）用于定义的物模型提交。
        该接口实现了物模型草稿箱的功能，保存用户最后一次编辑的物模型数据。

        :param request: Request instance for CreateIotModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIotModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIotModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProduct(self, request):
        """本接口（CreateProduct）用于创建一个新的物联网智能视频产品。

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateProductResponse`

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


    def CreateStorage(self, request):
        """该接口已经停止维护，请勿使用

        :param request: Request instance for CreateStorage.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStorageService(self, request):
        """购买云存服务

        :param request: Request instance for CreateStorageService.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateStorageServiceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateStorageServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorageService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTraceIds(self, request):
        """本接口（CreateTraceIds）用于将设备加到日志跟踪白名单。

        :param request: Request instance for CreateTraceIds.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateTraceIdsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateTraceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceIds", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTraceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUploadPath(self, request):
        """本接口（CreateUploadPath）用于获取固件上传路径。

        :param request: Request instance for CreateUploadPath.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateUploadPathRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateUploadPathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUploadPath", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUploadPathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUsrToken(self, request):
        """本接口（CreateUsrToken）用于终端用户获取IoT Video平台的accessToken，初始化SDK,连接到IoT Video接入服务器。

        :param request: Request instance for CreateUsrToken.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateUsrTokenRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateUsrTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUsrToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUsrTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAppUsr(self, request):
        """本接口（DeleteAppUsr）用于删除终端用户。

        :param request: Request instance for DeleteAppUsr.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteAppUsrRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteAppUsrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAppUsr", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppUsrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBinding(self, request):
        """本接口（DeleteBinding）用于终端用户和设备进行解绑定。

        :param request: Request instance for DeleteBinding.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteBindingRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBinding", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevice(self, request):
        """本接口（DeleteDevice）用于删除设备，可进行批量操作，每次操作最多100台设备。

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteDeviceResponse`

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


    def DeleteIotDataType(self, request):
        """本接口（DeleteIotDataType）用于删除自定义物模型数据类型。

        :param request: Request instance for DeleteIotDataType.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteIotDataTypeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteIotDataTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIotDataType", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIotDataTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMessageQueue(self, request):
        """本接口（DeleteMessageQueue）用于删除物联网智能视频产品的转发消息配置信息。

        :param request: Request instance for DeleteMessageQueue.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteMessageQueueRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteMessageQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMessageQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMessageQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOtaVersion(self, request):
        """本接口（DeleteOtaVersion）用于删除固件版本信息。

        :param request: Request instance for DeleteOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteOtaVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOtaVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOtaVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProduct(self, request):
        """本接口（DeleteProduct）用于删除一个物联网智能视频产品。

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteProductResponse`

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


    def DeleteTraceIds(self, request):
        """本接口（DeleteTraceIds）用于将设备从日志跟踪白名单中删除，该接口可批量操作，最多支持同时操作100台设备。

        :param request: Request instance for DeleteTraceIds.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteTraceIdsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteTraceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTraceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTraceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeliverStorageService(self, request):
        """将已购买的云存服务转移到另一设备

        :param request: Request instance for DeliverStorageService.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeliverStorageServiceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeliverStorageServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeliverStorageService", params, headers=headers)
            response = json.loads(body)
            model = models.DeliverStorageServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountBalance(self, request):
        """客户可通过本接口获取账户余额信息, 默认接口请求频率限制：1次/秒

        :param request: Request instance for DescribeAccountBalance.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeAccountBalanceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBindDev(self, request):
        """本接口（DescribeBindDev）用于查询终端用户绑定的设备列表。

        :param request: Request instance for DescribeBindDev.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindDevRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindDevResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindDev", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindDevResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBindUsr(self, request):
        """本接口（DescribeBindUsr）用于查询设备被分享的所有用户列表。

        :param request: Request instance for DescribeBindUsr.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindUsrRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindUsrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindUsr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindUsrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevice(self, request):
        """本接口（DescribeDevice）获取设备信息。

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceResponse`

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


    def DescribeDeviceModel(self, request):
        """本接口（DescribeDeviceModel）用于获取设备物模型。

        :param request: Request instance for DescribeDeviceModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevices(self, request):
        """本接口（DescribeDevices）用于获取设备信息列表。

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDevicesResponse`

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


    def DescribeIotDataType(self, request):
        """本接口（DescribeIotDataType）用于查询自定义的物模型数据类型。

        :param request: Request instance for DescribeIotDataType.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotDataTypeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotDataTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIotDataType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIotDataTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIotModel(self, request):
        """本接口（DescribeIotModel）用于获取物模型定义详情。

        :param request: Request instance for DescribeIotModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIotModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIotModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIotModels(self, request):
        """本接口（DescribeIotModels）用于列出物模型历史版本列表。

        :param request: Request instance for DescribeIotModels.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIotModels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIotModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogs(self, request):
        """本接口（DescribeLogs）用于查询设备日志列表。
        设备日志最长保留时长为15天,超期自动清除。

        :param request: Request instance for DescribeLogs.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeLogsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageQueue(self, request):
        """本接口（DescribeMessageQueue）用于查询物联网智能视频产品转发消息配置。

        :param request: Request instance for DescribeMessageQueue.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeMessageQueueRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeMessageQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelDataRet(self, request):
        """本接口（DescribeModelDataRet）用于根据TaskId获取对设备物模型操作最终响应的结果。

        :param request: Request instance for DescribeModelDataRet.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeModelDataRetRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeModelDataRetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelDataRet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelDataRetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOsList(self, request):
        """查看操作系统支持的芯片列表

        :param request: Request instance for DescribeOsList.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeOsListRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeOsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOtaVersions(self, request):
        """本接口（DescribeOtaVersions）用于查询固件版本信息列表。

        :param request: Request instance for DescribeOtaVersions.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeOtaVersionsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeOtaVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOtaVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOtaVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProduct(self, request):
        """本接口（DescribeProduct）用于获取单个产品的详细信息。

        :param request: Request instance for DescribeProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductResponse`

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


    def DescribeProducts(self, request):
        """本接口（DescribeProducts）用于列出用户账号下的物联网智能视频产品列表。

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductsResponse`

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


    def DescribePubVersions(self, request):
        """本接口（DescribePubVersions）用于获取某一产品发布过的全部固件版本。

        :param request: Request instance for DescribePubVersions.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribePubVersionsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribePubVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePubVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePubVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRechargeRecords(self, request):
        """客户可通过本接口获取充值记录信息, 一次最多返回50条记录。

        :param request: Request instance for DescribeRechargeRecords.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRechargeRecordsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRechargeRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRechargeRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRechargeRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistrationStatus(self, request):
        """本接口（DescribeRegistrationStatus）用于查询终端用户的注册状态。

        :param request: Request instance for DescribeRegistrationStatus.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRegistrationStatusRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRegistrationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistrationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistrationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRunLog(self, request):
        """本接口（DescribeRunLog）用于获取设备运行日志。

        :param request: Request instance for DescribeRunLog.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRunLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRunLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRunLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRunLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageService(self, request):
        """查询云存服务

        :param request: Request instance for DescribeStorageService.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeStorageServiceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeStorageServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStream(self, request):
        """请求设备直播流地址

        :param request: Request instance for DescribeStream.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeStreamRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStream", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTraceIds(self, request):
        """本接口（DescribeTraceIds）用于查询设备日志跟踪白名单。

        :param request: Request instance for DescribeTraceIds.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceIdsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTraceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTraceStatus(self, request):
        """本接口（DescribeTraceStatus）用于查询指定设备是否在白名单中。

        :param request: Request instance for DescribeTraceStatus.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceStatusRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTraceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableDevice(self, request):
        """本接口（DisableDevice）用于禁用设备，可进行批量操作，每次操作最多100台设备。

        :param request: Request instance for DisableDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DisableDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableDeviceStream(self, request):
        """本接口（DisableDeviceStream）用于停止设备推流，可进行批量操作，每次操作最多100台设备。

        :param request: Request instance for DisableDeviceStream.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceStreamRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableDeviceStream", params, headers=headers)
            response = json.loads(body)
            model = models.DisableDeviceStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableOtaVersion(self, request):
        """本接口（DisableOtaVersion）用于禁用固件版本。

        :param request: Request instance for DisableOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DisableOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DisableOtaVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableOtaVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DisableOtaVersionResponse()
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
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDeviceResponse`

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


    def ModifyDeviceAction(self, request):
        """本接口（ModifyDeviceAction）用于修改设备物模型的行为（Action）。

        可对ctlVal数据属性进行写入,如:Action.takePhoto.ctlVal,设备在线且成功发送到设备才返回,物模型写入数据时,不需要传入时标信息,平台以当前时标作为数据的时标更新物模型中的时标信息。
        注意:
          1.若设备当前不在线,会直接返回错误
          2.若设备网络出现异常时,消息发送可能超时,超时等待最长时间为3秒
          3.value的内容必须与实际物模型的定义一致

        :param request: Request instance for ModifyDeviceAction.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDeviceActionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDeviceActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceAction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceProperty(self, request):
        """本接口（ModifyDeviceProperty）用于修改设备物模型的属性（ProWritable）。
        可对setVal数据属性进行写入,如:
        ProWritable.Pos.setVal
        对于嵌套类型的可写属性，可以仅对其部分数据内容进行写入，如:
        ProWritable.Pos.setVal.x;
        可写属性云端写入成功即返回;云端向设备端发布属性变更参数;若当前设备不在线,在设备下次上线时会自动更新这些属性参数;
        物模型写入数据时,不需要传入时标信息,平台以当前时标作为数据的时标更新物模型中的时标信息。

        :param request: Request instance for ModifyDeviceProperty.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDevicePropertyRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDevicePropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceProperty", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDevicePropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProduct(self, request):
        """本接口（ModifyProduct）用于编辑物联网智能视频产品的相关信息。

        :param request: Request instance for ModifyProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyProductResponse`

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


    def ModifyVerContent(self, request):
        """编辑版本描述信息

        :param request: Request instance for ModifyVerContent.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyVerContentRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyVerContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVerContent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVerContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefundStorageService(self, request):
        """本接口（RefundStorageService）用于退订已购买的云存服务。
        退订时，云存服务对应订单的处理方式 :
        1. 未开始的订单自动回到已付费订单池
        2. 已开始的订单自动失效
        3. 购买云存接口,优先从已付费订单池中分配订单

        :param request: Request instance for RefundStorageService.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RefundStorageServiceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RefundStorageServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundStorageService", params, headers=headers)
            response = json.loads(body)
            model = models.RefundStorageServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunDevice(self, request):
        """本接口（RunDevice）用于启用设备，可进行批量操作，每次操作最多100台设备。

        :param request: Request instance for RunDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunDevice", params, headers=headers)
            response = json.loads(body)
            model = models.RunDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunDeviceStream(self, request):
        """本接口（RunDeviceStream）用于开启设备推流，可进行批量操作，每次操作最多100台设备。

        :param request: Request instance for RunDeviceStream.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceStreamRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunDeviceStream", params, headers=headers)
            response = json.loads(body)
            model = models.RunDeviceStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunIotModel(self, request):
        """本接口（RunIotModel）用于对定义的物模型进行发布。

        :param request: Request instance for RunIotModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunIotModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunIotModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunIotModel", params, headers=headers)
            response = json.loads(body)
            model = models.RunIotModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunOtaVersion(self, request):
        """本接口（RunOtaVersion）用于固件版本正式发布。

        :param request: Request instance for RunOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunOtaVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunOtaVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RunOtaVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunTestOtaVersion(self, request):
        """本接口（RunTestOtaVersion）用于固件版本测试发布。

        :param request: Request instance for RunTestOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunTestOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunTestOtaVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunTestOtaVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RunTestOtaVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendOnlineMsg(self, request):
        """本接口（SendOnlineMsg）用于向设备发送在线消息。
        注意：
        若设备当前不在线,会直接返回错误;
        若设备网络出现异常时,消息发送可能超时,超时等待最长时间为3秒.waitresp非0情况下,会导致本接口阻塞3秒。

        :param request: Request instance for SendOnlineMsg.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.SendOnlineMsgRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.SendOnlineMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendOnlineMsg", params, headers=headers)
            response = json.loads(body)
            model = models.SendOnlineMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetMessageQueue(self, request):
        """本接口（SetMessageQueue）用于配置物联网智能视频产品的转发消息队列。

        :param request: Request instance for SetMessageQueue.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.SetMessageQueueRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.SetMessageQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetMessageQueue", params, headers=headers)
            response = json.loads(body)
            model = models.SetMessageQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDevice(self, request):
        """本接口（UpgradeDevice）用于对设备进行固件升级。
        该接口向指定的设备下发固件更新指令,可将固件升级到任意版本(可实现固件降级)。
        警告:使能UpgradeNow参数存在一定的风险性！建议仅在debug场景下使用!

        :param request: Request instance for UpgradeDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.UpgradeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.UpgradeDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDevice", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadOtaVersion(self, request):
        """本接口（UploadOtaVersion）接收上传到控制台的固件版本信息。

        :param request: Request instance for UploadOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.UploadOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.UploadOtaVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadOtaVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UploadOtaVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))