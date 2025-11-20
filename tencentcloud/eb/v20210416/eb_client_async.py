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
from tencentcloud.eb.v20210416 import models
from typing import Dict


class EbClient(AbstractClient):
    _apiVersion = '2021-04-16'
    _endpoint = 'eb.tencentcloudapi.com'
    _service = 'eb'

    async def CheckRule(
            self,
            request: models.CheckRuleRequest,
            opts: Dict = None,
    ) -> models.CheckRuleResponse:
        """
        检验规则
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckTransformation(
            self,
            request: models.CheckTransformationRequest,
            opts: Dict = None,
    ) -> models.CheckTransformationResponse:
        """
        用于在ETL配置页面, 测试规则和数据.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConnection(
            self,
            request: models.CreateConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateConnectionResponse:
        """
        创建事件连接器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEventBus(
            self,
            request: models.CreateEventBusRequest,
            opts: Dict = None,
    ) -> models.CreateEventBusResponse:
        """
        用于创建事件集
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        创建事件规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTarget(
            self,
            request: models.CreateTargetRequest,
            opts: Dict = None,
    ) -> models.CreateTargetResponse:
        """
        创建事件目标
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTransformation(
            self,
            request: models.CreateTransformationRequest,
            opts: Dict = None,
    ) -> models.CreateTransformationResponse:
        """
        用于创建转换器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConnection(
            self,
            request: models.DeleteConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteConnectionResponse:
        """
        删除事件连接器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEventBus(
            self,
            request: models.DeleteEventBusRequest,
            opts: Dict = None,
    ) -> models.DeleteEventBusResponse:
        """
        删除事件集
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        删除事件规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTarget(
            self,
            request: models.DeleteTargetRequest,
            opts: Dict = None,
    ) -> models.DeleteTargetResponse:
        """
        删除事件目标
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTransformation(
            self,
            request: models.DeleteTransformationRequest,
            opts: Dict = None,
    ) -> models.DeleteTransformationResponse:
        """
        用于删除转换器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogTagValue(
            self,
            request: models.DescribeLogTagValueRequest,
            opts: Dict = None,
    ) -> models.DescribeLogTagValueResponse:
        """
        前置条件：需开启事件存储；事件查询维度值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogTagValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogTagValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEventBus(
            self,
            request: models.GetEventBusRequest,
            opts: Dict = None,
    ) -> models.GetEventBusResponse:
        """
        获取事件集详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPlatformEventTemplate(
            self,
            request: models.GetPlatformEventTemplateRequest,
            opts: Dict = None,
    ) -> models.GetPlatformEventTemplateResponse:
        """
        获取平台产品事件模板
        """
        
        kwargs = {}
        kwargs["action"] = "GetPlatformEventTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPlatformEventTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRule(
            self,
            request: models.GetRuleRequest,
            opts: Dict = None,
    ) -> models.GetRuleResponse:
        """
        获取事件规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTransformation(
            self,
            request: models.GetTransformationRequest,
            opts: Dict = None,
    ) -> models.GetTransformationResponse:
        """
        用于获取转换器详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConnections(
            self,
            request: models.ListConnectionsRequest,
            opts: Dict = None,
    ) -> models.ListConnectionsResponse:
        """
        获取事件连接器列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEventBuses(
            self,
            request: models.ListEventBusesRequest,
            opts: Dict = None,
    ) -> models.ListEventBusesResponse:
        """
        获取事件集列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListEventBuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEventBusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPlatformEventNames(
            self,
            request: models.ListPlatformEventNamesRequest,
            opts: Dict = None,
    ) -> models.ListPlatformEventNamesResponse:
        """
        获取平台产品事件名称
        """
        
        kwargs = {}
        kwargs["action"] = "ListPlatformEventNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPlatformEventNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPlatformEventPatterns(
            self,
            request: models.ListPlatformEventPatternsRequest,
            opts: Dict = None,
    ) -> models.ListPlatformEventPatternsResponse:
        """
        获取平台产品事件匹配规则
        """
        
        kwargs = {}
        kwargs["action"] = "ListPlatformEventPatterns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPlatformEventPatternsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPlatformProducts(
            self,
            request: models.ListPlatformProductsRequest,
            opts: Dict = None,
    ) -> models.ListPlatformProductsResponse:
        """
        获取平台产品列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListPlatformProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPlatformProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRules(
            self,
            request: models.ListRulesRequest,
            opts: Dict = None,
    ) -> models.ListRulesResponse:
        """
        获取事件规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTargets(
            self,
            request: models.ListTargetsRequest,
            opts: Dict = None,
    ) -> models.ListTargetsResponse:
        """
        获取事件目标列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishEvent(
            self,
            request: models.PublishEventRequest,
            opts: Dict = None,
    ) -> models.PublishEventResponse:
        """
        （已废弃）用于Event事件投递
        """
        
        kwargs = {}
        kwargs["action"] = "PublishEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutEvents(
            self,
            request: models.PutEventsRequest,
            opts: Dict = None,
    ) -> models.PutEventsResponse:
        """
        用于Event事件投递
        """
        
        kwargs = {}
        kwargs["action"] = "PutEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        前置条件：开启事件存储；查询历史推送事件
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConnection(
            self,
            request: models.UpdateConnectionRequest,
            opts: Dict = None,
    ) -> models.UpdateConnectionResponse:
        """
        更新事件连接器
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEventBus(
            self,
            request: models.UpdateEventBusRequest,
            opts: Dict = None,
    ) -> models.UpdateEventBusResponse:
        """
        更新事件集
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRule(
            self,
            request: models.UpdateRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateRuleResponse:
        """
        更新事件规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTarget(
            self,
            request: models.UpdateTargetRequest,
            opts: Dict = None,
    ) -> models.UpdateTargetResponse:
        """
        更新事件目标
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTransformation(
            self,
            request: models.UpdateTransformationRequest,
            opts: Dict = None,
    ) -> models.UpdateTransformationResponse:
        """
        用于更新转换器
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)