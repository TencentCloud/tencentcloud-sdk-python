# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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
from tencentcloud.iot.v20180123 import models


class IotClient(AbstractClient):
    _apiVersion = '2018-01-23'
    _endpoint = 'iot.tencentcloudapi.com'


    def ActivateRule(self, request):
        """启用规则

        :param request: 调用ActivateRule所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.ActivateRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.ActivateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ActivateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActivateRuleResponse()
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


    def AddDevice(self, request):
        """新增设备

        :param request: 调用AddDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.AddDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDeviceResponse()
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


    def AddProduct(self, request):
        """新增产品

        :param request: 调用AddProduct所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.AddProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddProductResponse()
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


    def AddRule(self, request):
        """新增规则

        :param request: 调用AddRule所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.AddRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddRuleResponse()
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


    def AddTopic(self, request):
        """新增Topic

        :param request: 调用AddTopic所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.AddTopicRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTopicResponse()
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


    def DeactivateRule(self, request):
        """禁用规则

        :param request: 调用DeactivateRule所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.DeactivateRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeactivateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeactivateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeactivateRuleResponse()
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
        """删除设备

        :param request: 调用DeleteDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteDeviceResponse`

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
        """删除产品

        :param request: 调用DeleteProduct所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteProductResponse`

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


    def DeleteRule(self, request):
        """删除规则

        :param request: 调用DeleteRule所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DeleteTopic(self, request):
        """删除Topic

        :param request: 调用DeleteTopic所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicResponse()
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


    def GetDataHistory(self, request):
        """获取数据历史

        :param request: 调用GetDataHistory所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDataHistoryRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDataHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDataHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDataHistoryResponse()
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


    def GetDevice(self, request):
        """获取设备信息

        :param request: 调用GetDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceResponse()
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


    def GetDeviceData(self, request):
        """获取设备数据

        :param request: 调用GetDeviceData所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceDataRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceDataResponse()
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


    def GetDeviceLog(self, request):
        """获取设备日志

        :param request: 调用GetDeviceLog所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceLogRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceLogResponse()
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


    def GetDeviceStatuses(self, request):
        """批量获取设备状态

        :param request: 调用GetDeviceStatuses所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceStatusesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceStatusesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceStatuses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceStatusesResponse()
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


    def GetDevices(self, request):
        """获取设备列表

        :param request: 调用GetDevices所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDevicesResponse()
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


    def GetProduct(self, request):
        """获取产品信息

        :param request: 调用GetProduct所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProductResponse()
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


    def GetProducts(self, request):
        """获取用户名下的产品列表

        :param request: 调用GetProducts所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetProductsRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetProductsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProducts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProductsResponse()
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


    def GetRule(self, request):
        """获取转发规则信息

        :param request: 调用GetRule所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRuleResponse()
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


    def GetRules(self, request):
        """获取转发规则列表

        :param request: 调用GetRules所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetRulesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRulesResponse()
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


    def GetTopic(self, request):
        """获取Topic信息

        :param request: 调用GetTopic所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetTopicRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTopicResponse()
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


    def GetTopics(self, request):
        """获取Topic列表

        :param request: 调用GetTopics所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetTopicsRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetTopicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTopics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTopicsResponse()
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


    def GetUser(self, request):
        """获取用户信息

        :param request: 调用GetUser所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.GetUserRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserResponse()
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


    def IssueDeviceControl(self, request):
        """下发设备控制指令

        :param request: 调用IssueDeviceControl所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.IssueDeviceControlRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.IssueDeviceControlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IssueDeviceControl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IssueDeviceControlResponse()
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


    def PublishMsg(self, request):
        """向Topic发布消息

        :param request: 调用PublishMsg所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.PublishMsgRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.PublishMsgResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishMsg", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishMsgResponse()
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


    def ResetDevice(self, request):
        """重置设备

        :param request: 调用ResetDevice所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.ResetDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.ResetDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetDeviceResponse()
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


    def UpdateProduct(self, request):
        """更新产品信息

        :param request: 调用UpdateProduct所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.UpdateProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.UpdateProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateProductResponse()
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


    def UpdateRule(self, request):
        """更新规则

        :param request: 调用UpdateRule所需参数的结构体。
        :type request: :class:`tencentcloud.iot.v20180123.models.UpdateRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRuleResponse()
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