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
from tencentcloud.iotvideo.v20201215 import models


class IotvideoClient(AbstractClient):
    _apiVersion = '2020-12-15'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'


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