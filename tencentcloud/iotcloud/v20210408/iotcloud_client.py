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
            body = self.call("CreateDevice", params)
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
            body = self.call("CreatePrivateCA", params)
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


    def DeletePrivateCA(self, request):
        """删除私有CA证书

        :param request: Request instance for DeletePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeletePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeletePrivateCAResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivateCA", params)
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


    def DescribeDevice(self, request):
        """本接口（DescribeDevice）用于查看设备信息

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResponse`

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


    def DescribeDevices(self, request):
        """本接口（DescribeDevices）用于查询物联网通信设备的设备列表。

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDevicesResponse`

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


    def DescribePrivateCA(self, request):
        """查询私有化CA信息

        :param request: Request instance for DescribePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateCA", params)
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
            body = self.call("DescribePrivateCABindedProducts", params)
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
            body = self.call("DescribePrivateCAs", params)
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


    def DescribeProductCA(self, request):
        """查询产品绑定的CA证书

        :param request: Request instance for DescribeProductCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductCAResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductCA", params)
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


    def UpdateDeviceLogLevel(self, request):
        """设置设备上报的日志级别

        :param request: Request instance for UpdateDeviceLogLevel.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceLogLevelRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceLogLevelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDeviceLogLevel", params)
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


    def UpdateDevicesEnableState(self, request):
        """批量启用或者禁用设备

        :param request: Request instance for UpdateDevicesEnableState.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicesEnableStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicesEnableStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDevicesEnableState", params)
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
            body = self.call("UpdatePrivateCA", params)
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