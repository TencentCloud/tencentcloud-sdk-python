# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.iot.v20180123 import models
from typing import Dict


class IotClient(AbstractClient):
    _apiVersion = '2018-01-23'
    _endpoint = 'iot.tencentcloudapi.com'
    _service = 'iot'

    async def ActivateRule(
            self,
            request: models.ActivateRuleRequest,
            opts: Dict = None,
    ) -> models.ActivateRuleResponse:
        """
        启用规则
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddDevice(
            self,
            request: models.AddDeviceRequest,
            opts: Dict = None,
    ) -> models.AddDeviceResponse:
        """
        提供在指定的产品Id下创建一个设备的能力，生成设备名称与设备秘钥。
        """
        
        kwargs = {}
        kwargs["action"] = "AddDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddProduct(
            self,
            request: models.AddProductRequest,
            opts: Dict = None,
    ) -> models.AddProductResponse:
        """
        本接口(AddProduct)用于创建、定义某款硬件产品。
        """
        
        kwargs = {}
        kwargs["action"] = "AddProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRule(
            self,
            request: models.AddRuleRequest,
            opts: Dict = None,
    ) -> models.AddRuleResponse:
        """
        新增规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddTopic(
            self,
            request: models.AddTopicRequest,
            opts: Dict = None,
    ) -> models.AddTopicResponse:
        """
        新增Topic，用于设备或应用发布消息至该Topic或订阅该Topic的消息。
        """
        
        kwargs = {}
        kwargs["action"] = "AddTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppAddUser(
            self,
            request: models.AppAddUserRequest,
            opts: Dict = None,
    ) -> models.AppAddUserResponse:
        """
        为APP提供用户注册功能
        """
        
        kwargs = {}
        kwargs["action"] = "AppAddUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppAddUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppDeleteDevice(
            self,
            request: models.AppDeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.AppDeleteDeviceResponse:
        """
        用户解除与设备的关联关系，解除后APP用户无法控制设备，获取设备数据
        """
        
        kwargs = {}
        kwargs["action"] = "AppDeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppDeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppGetDevice(
            self,
            request: models.AppGetDeviceRequest,
            opts: Dict = None,
    ) -> models.AppGetDeviceResponse:
        """
        获取绑定设备的基本信息与数据模板定义
        """
        
        kwargs = {}
        kwargs["action"] = "AppGetDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppGetDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppGetDeviceData(
            self,
            request: models.AppGetDeviceDataRequest,
            opts: Dict = None,
    ) -> models.AppGetDeviceDataResponse:
        """
        获取绑定设备数据，用于实时展示设备的最新数据
        """
        
        kwargs = {}
        kwargs["action"] = "AppGetDeviceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppGetDeviceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppGetDeviceStatuses(
            self,
            request: models.AppGetDeviceStatusesRequest,
            opts: Dict = None,
    ) -> models.AppGetDeviceStatusesResponse:
        """
        获取绑定设备的上下线状态
        """
        
        kwargs = {}
        kwargs["action"] = "AppGetDeviceStatuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppGetDeviceStatusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppGetDevices(
            self,
            request: models.AppGetDevicesRequest,
            opts: Dict = None,
    ) -> models.AppGetDevicesResponse:
        """
        获取用户的绑定设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "AppGetDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppGetDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppGetToken(
            self,
            request: models.AppGetTokenRequest,
            opts: Dict = None,
    ) -> models.AppGetTokenResponse:
        """
        获取用户token
        """
        
        kwargs = {}
        kwargs["action"] = "AppGetToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppGetTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppGetUser(
            self,
            request: models.AppGetUserRequest,
            opts: Dict = None,
    ) -> models.AppGetUserResponse:
        """
        获取用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "AppGetUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppGetUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppIssueDeviceControl(
            self,
            request: models.AppIssueDeviceControlRequest,
            opts: Dict = None,
    ) -> models.AppIssueDeviceControlResponse:
        """
        用户通过APP控制设备
        """
        
        kwargs = {}
        kwargs["action"] = "AppIssueDeviceControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppIssueDeviceControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppResetPassword(
            self,
            request: models.AppResetPasswordRequest,
            opts: Dict = None,
    ) -> models.AppResetPasswordResponse:
        """
        重置APP用户密码
        """
        
        kwargs = {}
        kwargs["action"] = "AppResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppSecureAddDevice(
            self,
            request: models.AppSecureAddDeviceRequest,
            opts: Dict = None,
    ) -> models.AppSecureAddDeviceResponse:
        """
        用户绑定设备，绑定后可以在APP端进行控制。绑定设备前需调用“获取设备绑定签名”接口
        """
        
        kwargs = {}
        kwargs["action"] = "AppSecureAddDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppSecureAddDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppUpdateDevice(
            self,
            request: models.AppUpdateDeviceRequest,
            opts: Dict = None,
    ) -> models.AppUpdateDeviceResponse:
        """
        修改设备别名，便于用户个性化定义设备的名称
        """
        
        kwargs = {}
        kwargs["action"] = "AppUpdateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppUpdateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppUpdateUser(
            self,
            request: models.AppUpdateUserRequest,
            opts: Dict = None,
    ) -> models.AppUpdateUserResponse:
        """
        修改用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "AppUpdateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppUpdateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSubDeviceToGatewayProduct(
            self,
            request: models.AssociateSubDeviceToGatewayProductRequest,
            opts: Dict = None,
    ) -> models.AssociateSubDeviceToGatewayProductResponse:
        """
        关联子设备产品和网关产品
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSubDeviceToGatewayProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSubDeviceToGatewayProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeactivateRule(
            self,
            request: models.DeactivateRuleRequest,
            opts: Dict = None,
    ) -> models.DeactivateRuleResponse:
        """
        禁用规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeactivateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeactivateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        提供在指定的产品Id下删除一个设备的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProduct(
            self,
            request: models.DeleteProductRequest,
            opts: Dict = None,
    ) -> models.DeleteProductResponse:
        """
        删除用户指定的产品Id对应的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        删除Topic
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataHistory(
            self,
            request: models.GetDataHistoryRequest,
            opts: Dict = None,
    ) -> models.GetDataHistoryResponse:
        """
        批量获取设备某一段时间范围的设备上报数据。该接口适用于使用高级版类型的产品
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDebugLog(
            self,
            request: models.GetDebugLogRequest,
            opts: Dict = None,
    ) -> models.GetDebugLogResponse:
        """
        获取设备的调试日志，用于定位问题
        """
        
        kwargs = {}
        kwargs["action"] = "GetDebugLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDebugLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevice(
            self,
            request: models.GetDeviceRequest,
            opts: Dict = None,
    ) -> models.GetDeviceResponse:
        """
        提供查询某个设备详细信息的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceData(
            self,
            request: models.GetDeviceDataRequest,
            opts: Dict = None,
    ) -> models.GetDeviceDataResponse:
        """
        获取某个设备当前上报到云端的数据，该接口适用于使用数据模板协议的产品。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceLog(
            self,
            request: models.GetDeviceLogRequest,
            opts: Dict = None,
    ) -> models.GetDeviceLogResponse:
        """
        批量获取设备与云端的详细通信日志，该接口适用于使用高级版类型的产品。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceSignatures(
            self,
            request: models.GetDeviceSignaturesRequest,
            opts: Dict = None,
    ) -> models.GetDeviceSignaturesResponse:
        """
        获取设备绑定签名，用于用户绑定某个设备的应用场景
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceSignatures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceSignaturesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceStatistics(
            self,
            request: models.GetDeviceStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetDeviceStatisticsResponse:
        """
        查询某段时间范围内产品的在线、激活设备数
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceStatuses(
            self,
            request: models.GetDeviceStatusesRequest,
            opts: Dict = None,
    ) -> models.GetDeviceStatusesResponse:
        """
        批量获取设备的当前状态，状态包括在线、离线或未激活状态。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceStatuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceStatusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevices(
            self,
            request: models.GetDevicesRequest,
            opts: Dict = None,
    ) -> models.GetDevicesResponse:
        """
        提供分页查询某个产品Id下设备信息的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProduct(
            self,
            request: models.GetProductRequest,
            opts: Dict = None,
    ) -> models.GetProductResponse:
        """
        获取产品定义的详细信息，包括产品名称、产品描述，鉴权模式等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProducts(
            self,
            request: models.GetProductsRequest,
            opts: Dict = None,
    ) -> models.GetProductsResponse:
        """
        获取用户在物联网套件所创建的所有产品信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRule(
            self,
            request: models.GetRuleRequest,
            opts: Dict = None,
    ) -> models.GetRuleResponse:
        """
        获取转发规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRules(
            self,
            request: models.GetRulesRequest,
            opts: Dict = None,
    ) -> models.GetRulesResponse:
        """
        获取转发规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTopic(
            self,
            request: models.GetTopicRequest,
            opts: Dict = None,
    ) -> models.GetTopicResponse:
        """
        获取Topic信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTopics(
            self,
            request: models.GetTopicsRequest,
            opts: Dict = None,
    ) -> models.GetTopicsResponse:
        """
        获取Topic列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IssueDeviceControl(
            self,
            request: models.IssueDeviceControlRequest,
            opts: Dict = None,
    ) -> models.IssueDeviceControlResponse:
        """
        提供下发控制指令到指定设备的能力，该接口适用于使用高级版类型的产品。
        """
        
        kwargs = {}
        kwargs["action"] = "IssueDeviceControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IssueDeviceControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishMsg(
            self,
            request: models.PublishMsgRequest,
            opts: Dict = None,
    ) -> models.PublishMsgResponse:
        """
        提供向指定的Topic发布消息的能力，常用于向设备下发控制指令。该接口只适用于产品版本为“基础版”类型的产品，使用高级版的产品需使用“下发设备控制指令”接口
        """
        
        kwargs = {}
        kwargs["action"] = "PublishMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDevice(
            self,
            request: models.ResetDeviceRequest,
            opts: Dict = None,
    ) -> models.ResetDeviceResponse:
        """
        重置设备操作，将会为设备生成新的证书及清空最新数据，需谨慎操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassociateSubDeviceFromGatewayProduct(
            self,
            request: models.UnassociateSubDeviceFromGatewayProductRequest,
            opts: Dict = None,
    ) -> models.UnassociateSubDeviceFromGatewayProductResponse:
        """
        业务无客户使用，下线接口。

        取消子设备产品与网关设备产品的关联
        """
        
        kwargs = {}
        kwargs["action"] = "UnassociateSubDeviceFromGatewayProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassociateSubDeviceFromGatewayProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProduct(
            self,
            request: models.UpdateProductRequest,
            opts: Dict = None,
    ) -> models.UpdateProductResponse:
        """
        提供修改产品信息及数据模板的能力。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRule(
            self,
            request: models.UpdateRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateRuleResponse:
        """
        更新规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)