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
from tencentcloud.iotcloud.v20180614 import models


class IotcloudClient(AbstractClient):
    _apiVersion = '2018-06-14'
    _endpoint = 'iotcloud.tencentcloudapi.com'
    _service = 'iotcloud'


    def BatchUpdateFirmware(self, request):
        """本接口（BatchUpdateFirmware）用于批量更新设备固件

        :param request: Request instance for BatchUpdateFirmware.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.BatchUpdateFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.BatchUpdateFirmwareResponse`

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


    def BindDevices(self, request):
        """本接口（BindDevices）用于网关设备批量绑定子设备

        :param request: Request instance for BindDevices.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.BindDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.BindDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindDevicesResponse()
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
        """取消设备升级任务

        :param request: Request instance for CancelDeviceFirmwareTask.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CancelDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CancelDeviceFirmwareTaskResponse`

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


    def CancelTask(self, request):
        """本接口（CancelTask）用于取消一个未被调度的任务。

        :param request: Request instance for CancelTask.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDevice(self, request):
        """本接口（CreateDevice）用于新建一个物联网通信设备。

        :param request: Request instance for CreateDevice.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLoraDevice(self, request):
        """创建lora类型的设备

        :param request: Request instance for CreateLoraDevice.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateLoraDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateLoraDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoraDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoraDeviceResponse()
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


    def CreateMultiDevice(self, request):
        """本接口（CreateMultiDevice）用于批量创建物联云设备。

        :param request: Request instance for CreateMultiDevice.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMultiDevicesTask(self, request):
        """本接口（CreateMultiDevicesTask）用于创建产品级别的批量创建设备任务

        :param request: Request instance for CreateMultiDevicesTask.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateMultiDevicesTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateMultiDevicesTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMultiDevicesTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMultiDevicesTaskResponse()
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
        """本接口（CreateProduct）用于创建一个新的物联网通信产品

        :param request: Request instance for CreateProduct.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTask(self, request):
        """本接口（CreateTask）用于创建一个批量任务。目前此接口可以创建批量更新影子以及批量下发消息的任务

        :param request: Request instance for CreateTask.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTaskFileUrl(self, request):
        """本接口（CreateTaskFileUrl）用于获取产品级任务文件上传链接

        :param request: Request instance for CreateTaskFileUrl.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateTaskFileUrlRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateTaskFileUrlResponse`

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


    def CreateTopicPolicy(self, request):
        """本接口（CreateTopicPolicy）用于创建一个Topic

        :param request: Request instance for CreateTopicPolicy.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopicPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicPolicyResponse()
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


    def CreateTopicRule(self, request):
        """本接口（CreateTopicRule）用于创建一个规则

        :param request: Request instance for CreateTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.CreateTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.CreateTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicRuleResponse()
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLoraDevice(self, request):
        """删除lora类型的设备

        :param request: Request instance for DeleteLoraDevice.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DeleteLoraDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DeleteLoraDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoraDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoraDeviceResponse()
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTopicRule(self, request):
        """本接口（DeleteTopicRule）用于删除规则

        :param request: Request instance for DeleteTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DeleteTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DeleteTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicRuleResponse()
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


    def DescribeAllDevices(self, request):
        """查询所有设备列表

        :param request: Request instance for DescribeAllDevices.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeAllDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeAllDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllDevicesResponse()
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
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceResponse`

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


    def DescribeDeviceClientKey(self, request):
        """获取证书认证类型设备的私钥，刚生成或者重置设备后仅可调用一次

        :param request: Request instance for DescribeDeviceClientKey.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceClientKeyRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceClientKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceClientKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceClientKeyResponse()
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


    def DescribeDeviceResource(self, request):
        """本接口（DescribeDeviceResource）用于查询设备资源详情。

        :param request: Request instance for DescribeDeviceResource.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceResourceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResourceResponse()
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


    def DescribeDeviceResources(self, request):
        """本接口（DescribeDeviceResources）用于查询设备资源列表。

        :param request: Request instance for DescribeDeviceResources.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceResourcesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeDeviceResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResourcesResponse()
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


    def DescribeDeviceShadow(self, request):
        """本接口（DescribeDeviceShadow）用于查询虚拟设备信息。

        :param request: Request instance for DescribeDeviceShadow.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevices(self, request):
        """本接口（DescribeDevices）用于查询物联网通信设备的设备列表。

        :param request: Request instance for DescribeDevices.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirmware(self, request):
        """查询固件信息

        :param request: Request instance for DescribeFirmware.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareResponse`

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
        """查询固件升级任务详情

        :param request: Request instance for DescribeFirmwareTask.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskResponse`

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
        """查询固件升级任务的设备列表

        :param request: Request instance for DescribeFirmwareTaskDevices.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskDevicesResponse`

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
        """查询固件升级任务状态分布

        :param request: Request instance for DescribeFirmwareTaskDistribution.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskDistributionRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskDistributionResponse`

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
        """查询固件升级任务统计信息

        :param request: Request instance for DescribeFirmwareTaskStatistics.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTaskStatisticsResponse`

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
        """查询固件升级任务列表

        :param request: Request instance for DescribeFirmwareTasks.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeFirmwareTasksResponse`

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


    def DescribeLoraDevice(self, request):
        """获取lora类型设备的详细信息

        :param request: Request instance for DescribeLoraDevice.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeLoraDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeLoraDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoraDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoraDeviceResponse()
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


    def DescribeMultiDevTask(self, request):
        """本接口（DescribeMultiDevTask）用于查询批量创建设备任务的执行状态。

        :param request: Request instance for DescribeMultiDevTask.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMultiDevices(self, request):
        """本接口（DescribeMultiDevices）用于查询批量创建设备的执行结果。

        :param request: Request instance for DescribeMultiDevices.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProductResource(self, request):
        """本接口（DescribeProductResource）用于查询产品资源详情。

        :param request: Request instance for DescribeProductResource.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductResourceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductResourceResponse()
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


    def DescribeProductResources(self, request):
        """本接口（DescribeProductResources）用于查询产品资源列表。

        :param request: Request instance for DescribeProductResources.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductResourcesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductResourcesResponse()
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


    def DescribeProductTask(self, request):
        """本接口（DescribeProductTask）用于查看产品级别的任务信息

        :param request: Request instance for DescribeProductTask.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductTaskResponse()
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


    def DescribeProductTasks(self, request):
        """本接口（DescribeProductTasks）用于查看产品级别的任务列表

        :param request: Request instance for DescribeProductTasks.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeProductTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductTasksResponse()
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
        """本接口（DescribeProducts）用于列出产品列表。

        :param request: Request instance for DescribeProducts.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePushResourceTaskStatistics(self, request):
        """查询推送资源任务统计信息

        :param request: Request instance for DescribePushResourceTaskStatistics.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribePushResourceTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribePushResourceTaskStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePushResourceTaskStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePushResourceTaskStatisticsResponse()
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


    def DescribeResourceTasks(self, request):
        """查询资源推送任务列表

        :param request: Request instance for DescribeResourceTasks.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DescribeResourceTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DescribeResourceTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTasksResponse()
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


    def DescribeTask(self, request):
        """本接口（DescribeTask）用于查询一个已创建任务的详情，任务保留一个月

        :param request: Request instance for DescribeTask.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """本接口（DescribeTasks）用于查询已创建的任务列表，任务保留一个月

        :param request: Request instance for DescribeTasks.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableTopicRule(self, request):
        """本接口（DisableTopicRule）用于禁用规则

        :param request: Request instance for DisableTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.DisableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DisableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableTopicRuleResponse()
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
        """编辑固件信息

        :param request: Request instance for EditFirmware.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.EditFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.EditFirmwareResponse`

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


    def EnableTopicRule(self, request):
        """本接口（EnableTopicRule）用于启用规则

        :param request: Request instance for EnableTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.EnableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.EnableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableTopicRuleResponse()
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


    def GetCOSURL(self, request):
        """本接口（GetCOSURL）用于获取固件存储在COS的URL

        :param request: Request instance for GetCOSURL.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.GetCOSURLRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.GetCOSURLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCOSURL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCOSURLResponse()
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


    def GetUserResourceInfo(self, request):
        """本接口（GetUserResourceInfo）用于查询用户资源使用信息。

        :param request: Request instance for GetUserResourceInfo.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.GetUserResourceInfoRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.GetUserResourceInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUserResourceInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserResourceInfoResponse()
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


    def PublishAsDevice(self, request):
        """模拟lora类型的设备端向服务器端发送消息

        :param request: Request instance for PublishAsDevice.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.PublishAsDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.PublishAsDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishAsDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishAsDeviceResponse()
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
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.PublishBroadcastMessageRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.PublishBroadcastMessageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishBroadcastMessage", params)
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


    def PublishMessage(self, request):
        """本接口（PublishMessage）用于向某个主题发消息。

        :param request: Request instance for PublishMessage.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishRRPCMessage(self, request):
        """发布RRPC消息

        :param request: Request instance for PublishRRPCMessage.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.PublishRRPCMessageRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.PublishRRPCMessageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishRRPCMessage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishRRPCMessageResponse()
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


    def PublishToDevice(self, request):
        """服务器端下发消息给lora类型的设备

        :param request: Request instance for PublishToDevice.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.PublishToDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.PublishToDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishToDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishToDeviceResponse()
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


    def ReplaceTopicRule(self, request):
        """本接口（ReplaceTopicRule）用于修改替换规则

        :param request: Request instance for ReplaceTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.ReplaceTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ReplaceTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceTopicRuleResponse()
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


    def ResetDeviceState(self, request):
        """重置设备的连接状态

        :param request: Request instance for ResetDeviceState.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.ResetDeviceStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ResetDeviceStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetDeviceState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetDeviceStateResponse()
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
        """重试设备升级任务

        :param request: Request instance for RetryDeviceFirmwareTask.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.RetryDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.RetryDeviceFirmwareTaskResponse`

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


    def UnbindDevices(self, request):
        """本接口（UnbindDevices）用于网关设备批量解绑子设备

        :param request: Request instance for UnbindDevices.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.UnbindDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.UnbindDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindDevicesResponse()
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


    def UpdateDeviceAvailableState(self, request):
        """启用或者禁用设备

        :param request: Request instance for UpdateDeviceAvailableState.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.UpdateDeviceAvailableStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.UpdateDeviceAvailableStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDeviceAvailableState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceAvailableStateResponse()
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


    def UpdateDeviceShadow(self, request):
        """本接口（UpdateDeviceShadow）用于更新虚拟设备信息。

        :param request: Request instance for UpdateDeviceShadow.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateTopicPolicy(self, request):
        """本接口（UpdateTopicPolicy）用于更新Topic信息

        :param request: Request instance for UpdateTopicPolicy.
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.UpdateTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.UpdateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateTopicPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTopicPolicyResponse()
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
        :type request: :class:`tencentcloud.iotcloud.v20180614.models.UploadFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.UploadFirmwareResponse`

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