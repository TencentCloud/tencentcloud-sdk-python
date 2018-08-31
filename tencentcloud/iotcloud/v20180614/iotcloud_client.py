# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.iotcloud.v20180614 import models


class IotcloudClient(AbstractClient):
    _apiVersion = '2018-06-14'
    _endpoint = 'iotcloud.tencentcloudapi.com'


    def CancelTask(self, request):
        """本接口（CancelTask）用于取消一个未被调度的任务。

        :param request: 调用CancelTask所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDevice(self, request):
        """本接口（CreateDevice）用于新建一个物联网通信设备。

        :param request: 调用CreateDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateDeviceResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMultiDevice(self, request):
        """本接口（CreateMultiDevice）用于批量创建物联云设备。

        :param request: 调用CreateMultiDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateMultiDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateMultiDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMultiDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMultiDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProduct(self, request):
        """本接口（CreateProduct）用于创建一个新的物联网通信产品

        :param request: 调用CreateProduct所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateProductResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTask(self, request):
        """本接口（CreateTask）用于创建一个批量任务。目前此接口可以创建批量更新影子以及批量下发消息的任务

        :param request: 调用CreateTask所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDevice(self, request):
        """本接口（DeleteDevice）用于删除物联网通信设备。

        :param request: 调用DeleteDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DeleteDeviceResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProduct(self, request):
        """本接口（DeleteProduct）用于删除一个物联网通信产品。

        :param request: 调用DeleteProduct所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DeleteProductResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceShadow(self, request):
        """本接口（DescribeDeviceShadow）用于查询虚拟设备信息。

        :param request: 调用DescribeDeviceShadow所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceShadowRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceShadow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceShadowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevices(self, request):
        """本接口（DescribeDevices）用于查询物联网通信设备的设备列表。

        :param request: 调用DescribeDevices所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDevicesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMultiDevTask(self, request):
        """本接口（DescribeMultiDevTask）用于查询批量创建设备任务的执行状态。

        :param request: 调用DescribeMultiDevTask所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeMultiDevTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeMultiDevTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMultiDevTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMultiDevTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMultiDevices(self, request):
        """本接口（DescribeMultiDevices）用于查询批量创建设备的执行结果。

        :param request: 调用DescribeMultiDevices所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeMultiDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeMultiDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMultiDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMultiDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProducts(self, request):
        """本接口（DescribeProducts）用于列出产品列表。

        :param request: 调用DescribeProducts所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductsResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTask(self, request):
        """本接口（DescribeTask）用于查询一个已创建任务的详情，任务保留一个月

        :param request: 调用DescribeTask所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """本接口（DescribeTasks）用于查询已创建的任务列表，任务保留一个月

        :param request: 调用DescribeTasks所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDeviceShadow(self, request):
        """本接口（GetDeviceShadow）用于查询虚拟设备信息。

        :param request: 调用GetDeviceShadow所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.GetDeviceShadowRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.GetDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceShadow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceShadowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishMessage(self, request):
        """本接口（PublishMessage）用于向某个主题发消息。

        :param request: 调用PublishMessage所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.PublishMessageResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDeviceShadow(self, request):
        """本接口（UpdateDeviceShadow）用于更新虚拟设备信息。

        :param request: 调用UpdateDeviceShadow所需参数的结构体。
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.UpdateDeviceShadowRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.UpdateDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDeviceShadow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceShadowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)