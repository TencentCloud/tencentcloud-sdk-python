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
from tencentcloud.iotcloud.v20210408 import models


class IotcloudClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'iotcloud.tencentcloudapi.com'
    _service = 'iotcloud'


    def CreateDevice(self, request):
        """本接口（CreateDevice）用于新建一个物联网通信设备。

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceResponse()
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


    def CreatePrivateCA(self, request):
        """创建私有CA证书

        :param request: Request instance for CreatePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreatePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreatePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrivateCAResponse()
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
        """本接口（DeleteDevice）用于删除物联网通信设备。

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
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


    def DeletePrivateCA(self, request):
        """删除私有CA证书

        :param request: Request instance for DeletePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeletePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeletePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivateCAResponse()
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
        """本接口（DeleteProduct）用于删除一个物联网通信产品

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProduct", params, headers=headers)
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


    def DeleteProductPrivateCA(self, request):
        """删除产品的私有CA证书

        :param request: Request instance for DeleteProductPrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteProductPrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteProductPrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProductPrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProductPrivateCAResponse()
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
        """本接口（DescribeDevice）用于查看设备信息

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevice", params, headers=headers)
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


    def DescribeDevices(self, request):
        """本接口（DescribeDevices）用于查询物联网通信设备的设备列表。

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
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


    def DescribePrivateCA(self, request):
        """查询私有化CA信息

        :param request: Request instance for DescribePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateCAResponse()
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


    def DescribePrivateCABindedProducts(self, request):
        """查询私有CA绑定的产品列表

        :param request: Request instance for DescribePrivateCABindedProducts.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCABindedProductsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCABindedProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateCABindedProducts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateCABindedProductsResponse()
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


    def DescribePrivateCAs(self, request):
        """查询私有CA证书列表

        :param request: Request instance for DescribePrivateCAs.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateCAs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateCAsResponse()
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
        """本接口（DescribeProduct）用于查看产品详情

        :param request: Request instance for DescribeProduct.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProduct", params, headers=headers)
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


    def DescribeProductCA(self, request):
        """查询产品绑定的CA证书

        :param request: Request instance for DescribeProductCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductCAResponse()
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


    def ListLog(self, request):
        """本接口（ListLog）用于查看日志信息

        :param request: Request instance for ListLog.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ListLogRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ListLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListLogResponse()
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


    def ListLogPayload(self, request):
        """获取日志内容列表

        :param request: Request instance for ListLogPayload.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ListLogPayloadRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ListLogPayloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLogPayload", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListLogPayloadResponse()
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


    def ListSDKLog(self, request):
        """获取设备上报的日志

        :param request: Request instance for ListSDKLog.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ListSDKLogRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ListSDKLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSDKLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSDKLogResponse()
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


    def PublishBroadcastMessage(self, request):
        """发布广播消息

        :param request: Request instance for PublishBroadcastMessage.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.PublishBroadcastMessageRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.PublishBroadcastMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishBroadcastMessage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishBroadcastMessageResponse()
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


    def SetProductsForbiddenStatus(self, request):
        """批量设置产品禁用状态

        :param request: Request instance for SetProductsForbiddenStatus.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.SetProductsForbiddenStatusRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.SetProductsForbiddenStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetProductsForbiddenStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetProductsForbiddenStatusResponse()
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


    def UpdateDeviceLogLevel(self, request):
        """设置设备上报的日志级别

        :param request: Request instance for UpdateDeviceLogLevel.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceLogLevelRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceLogLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceLogLevel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceLogLevelResponse()
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


    def UpdateDevicePSK(self, request):
        """本接口（UpdateDevicePSK）用于更新设备的PSK

        :param request: Request instance for UpdateDevicePSK.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicePSKRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicePSKResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevicePSK", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDevicePSKResponse()
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


    def UpdateDevicesEnableState(self, request):
        """批量启用或者禁用设备

        :param request: Request instance for UpdateDevicesEnableState.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicesEnableStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicesEnableStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevicesEnableState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDevicesEnableStateResponse()
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


    def UpdatePrivateCA(self, request):
        """更新私有CA证书

        :param request: Request instance for UpdatePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdatePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdatePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePrivateCAResponse()
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


    def UpdateProductDynamicRegister(self, request):
        """更新产品动态注册的配置

        :param request: Request instance for UpdateProductDynamicRegister.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateProductDynamicRegisterRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateProductDynamicRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProductDynamicRegister", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateProductDynamicRegisterResponse()
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


    def UpdateProductPrivateCA(self, request):
        """更新产品的私有CA

        :param request: Request instance for UpdateProductPrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateProductPrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateProductPrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProductPrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateProductPrivateCAResponse()
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