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
from tencentcloud.iotexplorer.v20190423 import models


class IotexplorerClient(AbstractClient):
    _apiVersion = '2019-04-23'
    _endpoint = 'iotexplorer.tencentcloudapi.com'
    _service = 'iotexplorer'


    def CallDeviceActionAsync(self, request):
        """提供给用户异步调用设备行为的能力

        :param request: Request instance for CallDeviceActionAsync.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionAsyncRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionAsyncResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CallDeviceActionAsync", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallDeviceActionAsyncResponse()
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


    def CallDeviceActionSync(self, request):
        """为用户提供同步调用设备行为的能力。

        :param request: Request instance for CallDeviceActionSync.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionSyncRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CallDeviceActionSyncResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CallDeviceActionSync", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallDeviceActionSyncResponse()
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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataResponse`

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


    def CreateDevice(self, request):
        """创建设备

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateDeviceResponse`

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


    def CreateLoRaFrequency(self, request):
        """创建 LoRa 自定义频点

        :param request: Request instance for CreateLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoRaFrequency", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoRaFrequencyResponse()
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


    def CreateLoRaGateway(self, request):
        """创建新 LoRa 网关设备接口

        :param request: Request instance for CreateLoRaGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateLoRaGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoRaGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoRaGatewayResponse()
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


    def CreateProject(self, request):
        """为用户提供新建项目的能力，用于集中管理产品和应用。

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
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


    def CreateStudioProduct(self, request):
        """为用户提供新建产品的能力，用于管理用户的设备

        :param request: Request instance for CreateStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStudioProductResponse()
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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicPolicyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicPolicyResponse`

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
        """创建规则

        :param request: Request instance for CreateTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateTopicRuleResponse`

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
        """删除设备

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDeviceResponse`

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


    def DeleteDevices(self, request):
        """批量删除设备

        :param request: Request instance for DeleteDevices.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDevicesRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDevicesResponse()
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


    def DeleteLoRaFrequency(self, request):
        """提供删除LoRa自定义频点的能力

        :param request: Request instance for DeleteLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoRaFrequency", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoRaFrequencyResponse()
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


    def DeleteLoRaGateway(self, request):
        """删除  LoRa 网关的接口

        :param request: Request instance for DeleteLoRaGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteLoRaGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoRaGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoRaGatewayResponse()
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


    def DeleteProject(self, request):
        """提供删除某个项目的能力

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
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


    def DeleteStudioProduct(self, request):
        """提供删除某个项目下产品的能力

        :param request: Request instance for DeleteStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStudioProductResponse()
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
        """删除规则

        :param request: Request instance for DeleteTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteTopicRuleResponse`

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


    def DescribeDevice(self, request):
        """用于查看某个设备的详细信息

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceResponse`

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


    def DescribeDeviceData(self, request):
        """根据设备产品ID、设备名称，获取设备上报的属性数据。

        :param request: Request instance for DescribeDeviceData.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataResponse`

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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryResponse`

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


    def DescribeFirmwareTask(self, request):
        """查询固件升级任务列表

        :param request: Request instance for DescribeFirmwareTask.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareTaskRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeFirmwareTaskResponse`

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


    def DescribeLoRaFrequency(self, request):
        """提供查询LoRa自定义频点详情的能力

        :param request: Request instance for DescribeLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoRaFrequency", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoRaFrequencyResponse()
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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionResponse`

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


    def DescribeProject(self, request):
        """查询项目详情

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectResponse()
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


    def DescribeStudioProduct(self, request):
        """提供查看产品详细信息的能力，包括产品的ID、数据协议、认证类型等重要参数

        :param request: Request instance for DescribeStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStudioProductResponse()
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


    def DescribeTopicRule(self, request):
        """获取规则信息

        :param request: Request instance for DescribeTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopicRuleResponse()
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


    def DirectBindDeviceInFamily(self, request):
        """直接绑定设备和家庭

        :param request: Request instance for DirectBindDeviceInFamily.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DirectBindDeviceInFamilyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DirectBindDeviceInFamilyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DirectBindDeviceInFamily", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DirectBindDeviceInFamilyResponse()
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
        """禁用规则

        :param request: Request instance for DisableTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DisableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DisableTopicRuleResponse`

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


    def EnableTopicRule(self, request):
        """启用规则

        :param request: Request instance for EnableTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.EnableTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.EnableTopicRuleResponse`

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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetCOSURLRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetCOSURLResponse`

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


    def GetDeviceList(self, request):
        """用于查询某个产品下的设备列表

        :param request: Request instance for GetDeviceList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetDeviceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceListResponse()
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


    def GetLoRaGatewayList(self, request):
        """获取 LoRa 网关列表接口

        :param request: Request instance for GetLoRaGatewayList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetLoRaGatewayListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetLoRaGatewayListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLoRaGatewayList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLoRaGatewayListResponse()
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


    def GetProjectList(self, request):
        """提供查询用户所创建的项目列表查询功能。

        :param request: Request instance for GetProjectList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProjectList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProjectListResponse()
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


    def GetStudioProductList(self, request):
        """提供查询某个项目下所有产品信息的能力。

        :param request: Request instance for GetStudioProductList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetStudioProductList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetStudioProductListResponse()
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


    def GetTopicRuleList(self, request):
        """获取规则列表

        :param request: Request instance for GetTopicRuleList.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetTopicRuleListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetTopicRuleListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTopicRuleList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTopicRuleListResponse()
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


    def ListEventHistory(self, request):
        """获取设备的历史事件

        :param request: Request instance for ListEventHistory.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ListEventHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ListEventHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEventHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEventHistoryResponse()
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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ListFirmwaresRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ListFirmwaresResponse`

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


    def ModifyLoRaFrequency(self, request):
        """修改LoRa自定义频点

        :param request: Request instance for ModifyLoRaFrequency.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaFrequencyRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaFrequencyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoRaFrequency", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoRaFrequencyResponse()
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


    def ModifyLoRaGateway(self, request):
        """修改 LoRa 网关信息

        :param request: Request instance for ModifyLoRaGateway.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaGatewayRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyLoRaGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoRaGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoRaGatewayResponse()
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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionResponse`

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


    def ModifyProject(self, request):
        """修改项目

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
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


    def ModifyStudioProduct(self, request):
        """提供修改产品的名称和描述等信息的能力，对于已发布产品不允许进行修改。

        :param request: Request instance for ModifyStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStudioProductResponse()
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


    def ModifyTopicRule(self, request):
        """修改规则

        :param request: Request instance for ModifyTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTopicRuleResponse()
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
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.PublishMessageRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.PublishMessageResponse`

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


    def ReleaseStudioProduct(self, request):
        """产品开发完成并测试通过后，通过发布产品将产品设置为发布状态

        :param request: Request instance for ReleaseStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseStudioProductResponse()
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


    def SearchStudioProduct(self, request):
        """提供根据产品名称查找产品的能力

        :param request: Request instance for SearchStudioProduct.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchStudioProductResponse()
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


    def SearchTopicRule(self, request):
        """搜索规则

        :param request: Request instance for SearchTopicRule.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchTopicRuleRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchTopicRuleResponse()
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
        """批量禁用启用设备

        :param request: Request instance for UpdateDevicesEnableState.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateDevicesEnableStateRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateDevicesEnableStateResponse`

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


    def UpdateFirmware(self, request):
        """本接口（UpdateFirmware）用于对指定设备发起固件升级请求

        :param request: Request instance for UpdateFirmware.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateFirmwareRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UpdateFirmwareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFirmware", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFirmwareResponse()
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
        """本接口（UploadFirmware）用于上传设备固件至平台

        :param request: Request instance for UploadFirmware.
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.UploadFirmwareRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.UploadFirmwareResponse`

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