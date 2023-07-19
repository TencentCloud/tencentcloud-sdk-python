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
from tencentcloud.iot.v20180123 import models


class IotClient(AbstractClient):
    _apiVersion = '2018-01-23'
    _endpoint = 'iot.tencentcloudapi.com'
    _service = 'iot'


    def ActivateRule(self, request):
        """启用规则

        :param request: Request instance for ActivateRule.
        :type request: :class:`tencentcloud.iot.v20180123.models.ActivateRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.ActivateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateRule", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDevice(self, request):
        """提供在指定的产品Id下创建一个设备的能力，生成设备名称与设备秘钥。

        :param request: Request instance for AddDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.AddDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AddDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddProduct(self, request):
        """本接口(AddProduct)用于创建、定义某款硬件产品。

        :param request: Request instance for AddProduct.
        :type request: :class:`tencentcloud.iot.v20180123.models.AddProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddProduct", params, headers=headers)
            response = json.loads(body)
            model = models.AddProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRule(self, request):
        """新增规则

        :param request: Request instance for AddRule.
        :type request: :class:`tencentcloud.iot.v20180123.models.AddRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddTopic(self, request):
        """新增Topic，用于设备或应用发布消息至该Topic或订阅该Topic的消息。

        :param request: Request instance for AddTopic.
        :type request: :class:`tencentcloud.iot.v20180123.models.AddTopicRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AddTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTopic", params, headers=headers)
            response = json.loads(body)
            model = models.AddTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppAddUser(self, request):
        """为APP提供用户注册功能

        :param request: Request instance for AppAddUser.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppAddUserRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppAddUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppAddUser", params, headers=headers)
            response = json.loads(body)
            model = models.AppAddUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppDeleteDevice(self, request):
        """用户解除与设备的关联关系，解除后APP用户无法控制设备，获取设备数据

        :param request: Request instance for AppDeleteDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppDeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppDeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppDeleteDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AppDeleteDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppGetDevice(self, request):
        """获取绑定设备的基本信息与数据模板定义

        :param request: Request instance for AppGetDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppGetDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppGetDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppGetDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AppGetDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppGetDeviceData(self, request):
        """获取绑定设备数据，用于实时展示设备的最新数据

        :param request: Request instance for AppGetDeviceData.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppGetDeviceDataRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppGetDeviceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppGetDeviceData", params, headers=headers)
            response = json.loads(body)
            model = models.AppGetDeviceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppGetDeviceStatuses(self, request):
        """获取绑定设备的上下线状态

        :param request: Request instance for AppGetDeviceStatuses.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppGetDeviceStatusesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppGetDeviceStatusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppGetDeviceStatuses", params, headers=headers)
            response = json.loads(body)
            model = models.AppGetDeviceStatusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppGetDevices(self, request):
        """获取用户的绑定设备列表

        :param request: Request instance for AppGetDevices.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppGetDevicesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppGetDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppGetDevices", params, headers=headers)
            response = json.loads(body)
            model = models.AppGetDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppGetToken(self, request):
        """获取用户token

        :param request: Request instance for AppGetToken.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppGetTokenRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppGetTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppGetToken", params, headers=headers)
            response = json.loads(body)
            model = models.AppGetTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppGetUser(self, request):
        """获取用户信息

        :param request: Request instance for AppGetUser.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppGetUserRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppGetUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppGetUser", params, headers=headers)
            response = json.loads(body)
            model = models.AppGetUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppIssueDeviceControl(self, request):
        """用户通过APP控制设备

        :param request: Request instance for AppIssueDeviceControl.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppIssueDeviceControlRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppIssueDeviceControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppIssueDeviceControl", params, headers=headers)
            response = json.loads(body)
            model = models.AppIssueDeviceControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppResetPassword(self, request):
        """重置APP用户密码

        :param request: Request instance for AppResetPassword.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppResetPasswordRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppResetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppResetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.AppResetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppSecureAddDevice(self, request):
        """用户绑定设备，绑定后可以在APP端进行控制。绑定设备前需调用“获取设备绑定签名”接口

        :param request: Request instance for AppSecureAddDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppSecureAddDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppSecureAddDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppSecureAddDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AppSecureAddDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppUpdateDevice(self, request):
        """修改设备别名，便于用户个性化定义设备的名称

        :param request: Request instance for AppUpdateDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppUpdateDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppUpdateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppUpdateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AppUpdateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppUpdateUser(self, request):
        """修改用户信息

        :param request: Request instance for AppUpdateUser.
        :type request: :class:`tencentcloud.iot.v20180123.models.AppUpdateUserRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppUpdateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppUpdateUser", params, headers=headers)
            response = json.loads(body)
            model = models.AppUpdateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSubDeviceToGatewayProduct(self, request):
        """关联子设备产品和网关产品

        :param request: Request instance for AssociateSubDeviceToGatewayProduct.
        :type request: :class:`tencentcloud.iot.v20180123.models.AssociateSubDeviceToGatewayProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.AssociateSubDeviceToGatewayProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSubDeviceToGatewayProduct", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSubDeviceToGatewayProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeactivateRule(self, request):
        """禁用规则

        :param request: Request instance for DeactivateRule.
        :type request: :class:`tencentcloud.iot.v20180123.models.DeactivateRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeactivateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeactivateRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeactivateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevice(self, request):
        """提供在指定的产品Id下删除一个设备的能力。

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteDeviceResponse`

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


    def DeleteProduct(self, request):
        """删除用户指定的产品Id对应的信息。

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteProductResponse`

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


    def DeleteRule(self, request):
        """删除规则

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        """删除Topic

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.iot.v20180123.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDataHistory(self, request):
        """批量获取设备某一段时间范围的设备上报数据。该接口适用于使用高级版类型的产品

        :param request: Request instance for GetDataHistory.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDataHistoryRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDataHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDataHistory", params, headers=headers)
            response = json.loads(body)
            model = models.GetDataHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDebugLog(self, request):
        """获取设备的调试日志，用于定位问题

        :param request: Request instance for GetDebugLog.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDebugLogRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDebugLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDebugLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetDebugLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevice(self, request):
        """提供查询某个设备详细信息的能力。

        :param request: Request instance for GetDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevice", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceData(self, request):
        """获取某个设备当前上报到云端的数据，该接口适用于使用数据模板协议的产品。

        :param request: Request instance for GetDeviceData.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceDataRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceData", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceLog(self, request):
        """批量获取设备与云端的详细通信日志，该接口适用于使用高级版类型的产品。

        :param request: Request instance for GetDeviceLog.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceLogRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceSignatures(self, request):
        """获取设备绑定签名，用于用户绑定某个设备的应用场景

        :param request: Request instance for GetDeviceSignatures.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceSignaturesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceSignaturesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceSignatures", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceSignaturesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceStatistics(self, request):
        """查询某段时间范围内产品的在线、激活设备数

        :param request: Request instance for GetDeviceStatistics.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceStatisticsRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceStatuses(self, request):
        """批量获取设备的当前状态，状态包括在线、离线或未激活状态。

        :param request: Request instance for GetDeviceStatuses.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDeviceStatusesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDeviceStatusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceStatuses", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceStatusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevices(self, request):
        """提供分页查询某个产品Id下设备信息的能力。

        :param request: Request instance for GetDevices.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevices", params, headers=headers)
            response = json.loads(body)
            model = models.GetDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProduct(self, request):
        """获取产品定义的详细信息，包括产品名称、产品描述，鉴权模式等信息。

        :param request: Request instance for GetProduct.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProduct", params, headers=headers)
            response = json.loads(body)
            model = models.GetProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProducts(self, request):
        """获取用户在物联网套件所创建的所有产品信息。

        :param request: Request instance for GetProducts.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetProductsRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProducts", params, headers=headers)
            response = json.loads(body)
            model = models.GetProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRule(self, request):
        """获取转发规则信息

        :param request: Request instance for GetRule.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRule", params, headers=headers)
            response = json.loads(body)
            model = models.GetRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRules(self, request):
        """获取转发规则列表

        :param request: Request instance for GetRules.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetRulesRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRules", params, headers=headers)
            response = json.loads(body)
            model = models.GetRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTopic(self, request):
        """获取Topic信息

        :param request: Request instance for GetTopic.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetTopicRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTopic", params, headers=headers)
            response = json.loads(body)
            model = models.GetTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTopics(self, request):
        """获取Topic列表

        :param request: Request instance for GetTopics.
        :type request: :class:`tencentcloud.iot.v20180123.models.GetTopicsRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.GetTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTopics", params, headers=headers)
            response = json.loads(body)
            model = models.GetTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IssueDeviceControl(self, request):
        """提供下发控制指令到指定设备的能力，该接口适用于使用高级版类型的产品。

        :param request: Request instance for IssueDeviceControl.
        :type request: :class:`tencentcloud.iot.v20180123.models.IssueDeviceControlRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.IssueDeviceControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IssueDeviceControl", params, headers=headers)
            response = json.loads(body)
            model = models.IssueDeviceControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishMsg(self, request):
        """提供向指定的Topic发布消息的能力，常用于向设备下发控制指令。该接口只适用于产品版本为“基础版”类型的产品，使用高级版的产品需使用“下发设备控制指令”接口

        :param request: Request instance for PublishMsg.
        :type request: :class:`tencentcloud.iot.v20180123.models.PublishMsgRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.PublishMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishMsg", params, headers=headers)
            response = json.loads(body)
            model = models.PublishMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDevice(self, request):
        """重置设备操作，将会为设备生成新的证书及清空最新数据，需谨慎操作。

        :param request: Request instance for ResetDevice.
        :type request: :class:`tencentcloud.iot.v20180123.models.ResetDeviceRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.ResetDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassociateSubDeviceFromGatewayProduct(self, request):
        """业务无客户使用，下线接口。

        取消子设备产品与网关设备产品的关联

        :param request: Request instance for UnassociateSubDeviceFromGatewayProduct.
        :type request: :class:`tencentcloud.iot.v20180123.models.UnassociateSubDeviceFromGatewayProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.UnassociateSubDeviceFromGatewayProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassociateSubDeviceFromGatewayProduct", params, headers=headers)
            response = json.loads(body)
            model = models.UnassociateSubDeviceFromGatewayProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProduct(self, request):
        """提供修改产品信息及数据模板的能力。

        :param request: Request instance for UpdateProduct.
        :type request: :class:`tencentcloud.iot.v20180123.models.UpdateProductRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.UpdateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProduct", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRule(self, request):
        """更新规则

        :param request: Request instance for UpdateRule.
        :type request: :class:`tencentcloud.iot.v20180123.models.UpdateRuleRequest`
        :rtype: :class:`tencentcloud.iot.v20180123.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))