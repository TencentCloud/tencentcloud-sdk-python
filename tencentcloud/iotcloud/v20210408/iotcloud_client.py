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


    def BatchUpdateFirmware(self, request):
        """本接口（BatchUpdateFirmware）用于批量更新设备固件

        :param request: Request instance for BatchUpdateFirmware.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.BatchUpdateFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.BatchUpdateFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchUpdateFirmware", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.BindDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.BindDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDevices", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CancelDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CancelDeviceFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDeviceFirmwareTask", params, headers=headers)
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


    def CreateMultiDevicesTask(self, request):
        """本接口（CreateMultiDevicesTask）用于创建产品级别的批量创建设备任务

        :param request: Request instance for CreateMultiDevicesTask.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateMultiDevicesTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateMultiDevicesTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiDevicesTask", params, headers=headers)
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


    def CreateProduct(self, request):
        """本接口（CreateProduct）用于创建一个新的物联网通信产品

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProduct", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateTaskFileUrlRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateTaskFileUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFileUrl", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopicPolicy", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopicRule", params, headers=headers)
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


    def DeleteDeviceResource(self, request):
        """本接口（DeleteDeviceResource）用于删除设备资源

        :param request: Request instance for DeleteDeviceResource.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteDeviceResourceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteDeviceResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceResource", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResourceResponse()
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


    def DeleteTopicRule(self, request):
        """本接口（DeleteTopicRule）用于删除规则

        :param request: Request instance for DeleteTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopicRule", params, headers=headers)
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


    def DescribeDeviceClientKey(self, request):
        """获取证书认证类型设备的私钥，刚生成或者重置设备后仅可调用一次

        :param request: Request instance for DescribeDeviceClientKey.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceClientKeyRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceClientKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceClientKey", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResourceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceResource", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResourcesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceResources", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceShadowRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceShadow", params, headers=headers)
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


    def DescribeFirmware(self, request):
        """查询固件信息

        :param request: Request instance for DescribeFirmware.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmware", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTask", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTaskDevices", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskDistributionRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTaskDistribution", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTaskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTaskStatistics", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeFirmwareTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirmwareTasks", params, headers=headers)
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


    def DescribeGatewayBindDevices(self, request):
        """本接口（DescribeGatewayBindDevices）用于获取网关绑定的子设备列表

        :param request: Request instance for DescribeGatewayBindDevices.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeGatewayBindDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeGatewayBindDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayBindDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayBindDevicesResponse()
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


    def DescribeProductResource(self, request):
        """本接口（DescribeProductResource）用于查询产品资源详情。

        :param request: Request instance for DescribeProductResource.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductResourceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductResource", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductResourcesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductResources", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductTask", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductTasks", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducts", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePushResourceTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePushResourceTaskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushResourceTaskStatistics", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeResourceTasksRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeResourceTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTasks", params, headers=headers)
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


    def DisableTopicRule(self, request):
        """本接口（DisableTopicRule）用于禁用规则

        :param request: Request instance for DisableTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DisableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DisableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableTopicRule", params, headers=headers)
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


    def DownloadDeviceResource(self, request):
        """本接口（DownloadDeviceResource）用于下载设备资源

        :param request: Request instance for DownloadDeviceResource.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DownloadDeviceResourceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DownloadDeviceResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadDeviceResource", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadDeviceResourceResponse()
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.EditFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.EditFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditFirmware", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.EnableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.EnableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTopicRule", params, headers=headers)
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


    def GetAllVersion(self, request):
        """本接口（GetAllVersion）用于获取所有的版本列表

        :param request: Request instance for GetAllVersion.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.GetAllVersionRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.GetAllVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAllVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAllVersionResponse()
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.GetCOSURLRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.GetCOSURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCOSURL", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.GetUserResourceInfoRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.GetUserResourceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUserResourceInfo", params, headers=headers)
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


    def ListFirmwares(self, request):
        """本接口（ListFirmwares）用于获取固件列表

        :param request: Request instance for ListFirmwares.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ListFirmwaresRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ListFirmwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFirmwares", params, headers=headers)
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


    def ListTopicRules(self, request):
        """本接口（ListTopicRules）用于分页获取规则列表

        :param request: Request instance for ListTopicRules.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ListTopicRulesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ListTopicRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTopicRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopicRulesResponse()
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


    def PublishMessage(self, request):
        """本接口（PublishMessage）用于向某个主题发消息。

        :param request: Request instance for PublishMessage.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.PublishMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishMessage", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.PublishRRPCMessageRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.PublishRRPCMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishRRPCMessage", params, headers=headers)
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


    def ReplaceTopicRule(self, request):
        """本接口（ReplaceTopicRule）用于修改替换规则

        :param request: Request instance for ReplaceTopicRule.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ReplaceTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ReplaceTopicRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceTopicRule", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.ResetDeviceStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.ResetDeviceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDeviceState", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.RetryDeviceFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.RetryDeviceFirmwareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDeviceFirmwareTask", params, headers=headers)
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


    def UnbindDevices(self, request):
        """本接口（UnbindDevices）用于网关设备批量解绑子设备

        :param request: Request instance for UnbindDevices.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UnbindDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UnbindDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindDevices", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceAvailableStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceAvailableStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceAvailableState", params, headers=headers)
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


    def UpdateDeviceShadow(self, request):
        """本接口（UpdateDeviceShadow）用于更新虚拟设备信息。

        :param request: Request instance for UpdateDeviceShadow.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceShadowRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceShadow", params, headers=headers)
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


    def UpdateTopicPolicy(self, request):
        """本接口（UpdateTopicPolicy）用于更新Topic信息

        :param request: Request instance for UpdateTopicPolicy.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTopicPolicy", params, headers=headers)
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
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UploadFirmwareRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UploadFirmwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFirmware", params, headers=headers)
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