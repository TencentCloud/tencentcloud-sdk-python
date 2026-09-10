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
from tencentcloud.cngw.v20230418 import models
from typing import Dict


class CngwClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'cngw.tencentcloudapi.com'
    _service = 'cngw'

    async def AddCloudNativeAPIGatewayConsumerGroupAuth(
            self,
            request: models.AddCloudNativeAPIGatewayConsumerGroupAuthRequest,
            opts: Dict = None,
    ) -> models.AddCloudNativeAPIGatewayConsumerGroupAuthResponse:
        """
        为资源（模型 API / MCP Server）添加消费者组授权。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCloudNativeAPIGatewayConsumerGroupAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCloudNativeAPIGatewayConsumerGroupAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCloudNativeAPIGatewayConsumerInGroup(
            self,
            request: models.AddCloudNativeAPIGatewayConsumerInGroupRequest,
            opts: Dict = None,
    ) -> models.AddCloudNativeAPIGatewayConsumerInGroupResponse:
        """
        将消费者添加到消费者组。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCloudNativeAPIGatewayConsumerInGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCloudNativeAPIGatewayConsumerInGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindCloudNativeAPIGatewaySecretKey(
            self,
            request: models.BindCloudNativeAPIGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.BindCloudNativeAPIGatewaySecretKeyResponse:
        """
        添加密钥与资源的引用关系接口
        """
        
        kwargs = {}
        kwargs["action"] = "BindCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCloudNativeAPIGatewayMCPRouteMatch(
            self,
            request: models.CheckCloudNativeAPIGatewayMCPRouteMatchRequest,
            opts: Dict = None,
    ) -> models.CheckCloudNativeAPIGatewayMCPRouteMatchResponse:
        """
        上传插件前置操作，获取COS相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCloudNativeAPIGatewayMCPRouteMatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCloudNativeAPIGatewayMCPRouteMatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCloudNativeAPIGatewayMCPToolVersionExist(
            self,
            request: models.CheckCloudNativeAPIGatewayMCPToolVersionExistRequest,
            opts: Dict = None,
    ) -> models.CheckCloudNativeAPIGatewayMCPToolVersionExistResponse:
        """
        修改云原生智能网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCloudNativeAPIGatewayMCPToolVersionExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCloudNativeAPIGatewayMCPToolVersionExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareCloudNativeAPIGatewayMCPToolVersion(
            self,
            request: models.CompareCloudNativeAPIGatewayMCPToolVersionRequest,
            opts: Dict = None,
    ) -> models.CompareCloudNativeAPIGatewayMCPToolVersionResponse:
        """
        修改云原生智能网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "CompareCloudNativeAPIGatewayMCPToolVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareCloudNativeAPIGatewayMCPToolVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayAIServiceSource(
            self,
            request: models.CreateCloudNativeAPIGatewayAIServiceSourceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayAIServiceSourceResponse:
        """
        创建云原生网关AI服务来源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayAIServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayAIServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayConsumer(
            self,
            request: models.CreateCloudNativeAPIGatewayConsumerRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayConsumerResponse:
        """
        创建AI网关消费者。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayConsumerGroup(
            self,
            request: models.CreateCloudNativeAPIGatewayConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayConsumerGroupResponse:
        """
        创建AI 网关消费者组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayLLMModelAPI(
            self,
            request: models.CreateCloudNativeAPIGatewayLLMModelAPIRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayLLMModelAPIResponse:
        """
        创建 LLM 模型 API。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayLLMModelAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayLLMModelAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayLLMModelService(
            self,
            request: models.CreateCloudNativeAPIGatewayLLMModelServiceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayLLMModelServiceResponse:
        """
        创建 LLM 模型服务。同一网关下 Name 唯一。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayLLMModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayLLMModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayMCPRoute(
            self,
            request: models.CreateCloudNativeAPIGatewayMCPRouteRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayMCPRouteResponse:
        """
        上传插件前置操作，获取COS相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayMCPRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayMCPRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayMCPServer(
            self,
            request: models.CreateCloudNativeAPIGatewayMCPServerRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayMCPServerResponse:
        """
        创建AI网关MCP Server
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayMCPServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayMCPServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayMCPTool(
            self,
            request: models.CreateCloudNativeAPIGatewayMCPToolRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayMCPToolResponse:
        """
        创建AI网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayMCPTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayMCPToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewaySecretKey(
            self,
            request: models.CreateCloudNativeAPIGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewaySecretKeyResponse:
        """
        创建消费者密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayAIServiceSource(
            self,
            request: models.DeleteCloudNativeAPIGatewayAIServiceSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayAIServiceSourceResponse:
        """
        删除云原生网关AI服务来源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayAIServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayAIServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayConsumer(
            self,
            request: models.DeleteCloudNativeAPIGatewayConsumerRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayConsumerResponse:
        """
        删除AI 网关消费者（被绑定到消费者组/密钥时需先解绑）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayConsumerGroup(
            self,
            request: models.DeleteCloudNativeAPIGatewayConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayConsumerGroupResponse:
        """
        删除AI网关消费者组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayLLMModelAPI(
            self,
            request: models.DeleteCloudNativeAPIGatewayLLMModelAPIRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayLLMModelAPIResponse:
        """
        删除 LLM 模型 API。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayLLMModelAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayLLMModelAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayLLMModelService(
            self,
            request: models.DeleteCloudNativeAPIGatewayLLMModelServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayLLMModelServiceResponse:
        """
        删除 LLM 模型服务（被模型 API 绑定时需先解绑）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayLLMModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayLLMModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayMCPRoute(
            self,
            request: models.DeleteCloudNativeAPIGatewayMCPRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayMCPRouteResponse:
        """
        上传插件前置操作，获取COS相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayMCPRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayMCPRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayMCPServer(
            self,
            request: models.DeleteCloudNativeAPIGatewayMCPServerRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayMCPServerResponse:
        """
        删除AI网关MCP服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayMCPServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayMCPServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayMCPTool(
            self,
            request: models.DeleteCloudNativeAPIGatewayMCPToolRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayMCPToolResponse:
        """
        删除AI网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayMCPTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayMCPToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayMCPToolVersion(
            self,
            request: models.DeleteCloudNativeAPIGatewayMCPToolVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayMCPToolVersionResponse:
        """
        修改云原生智能网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayMCPToolVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayMCPToolVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewaySecretKey(
            self,
            request: models.DeleteCloudNativeAPIGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewaySecretKeyResponse:
        """
        删除消费者密钥（被绑定时需先解绑）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCNGWServicesWithRoutes(
            self,
            request: models.DescribeCNGWServicesWithRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeCNGWServicesWithRoutesResponse:
        """
        查询云原生网关服务和路由列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCNGWServicesWithRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCNGWServicesWithRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayAIQuota(
            self,
            request: models.DescribeCloudNativeAPIGatewayAIQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayAIQuotaResponse:
        """
        查询AI网关配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayAIQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayAIQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayAIQuotaList(
            self,
            request: models.DescribeCloudNativeAPIGatewayAIQuotaListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayAIQuotaListResponse:
        """
        查询AI配额配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayAIQuotaList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayAIQuotaListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayAIServiceSourceList(
            self,
            request: models.DescribeCloudNativeAPIGatewayAIServiceSourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayAIServiceSourceListResponse:
        """
        查询云原生网关AI服务来源
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayAIServiceSourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayAIServiceSourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayConsumer(
            self,
            request: models.DescribeCloudNativeAPIGatewayConsumerRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayConsumerResponse:
        """
        查询云原生消费者详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayConsumerGroup(
            self,
            request: models.DescribeCloudNativeAPIGatewayConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayConsumerGroupResponse:
        """
        查询消费者组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayLLMModelAPI(
            self,
            request: models.DescribeCloudNativeAPIGatewayLLMModelAPIRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayLLMModelAPIResponse:
        """
        查询单个 LLM 模型 API 详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayLLMModelAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayLLMModelAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayLLMModelAPIs(
            self,
            request: models.DescribeCloudNativeAPIGatewayLLMModelAPIsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayLLMModelAPIsResponse:
        """
        查询指定网关实例下的所有 LLM 模型 API 列表。支持按名称关键词模糊搜索、按过滤器筛选，以及分页查询。用于绑定场景时，可通过 ConsumerGroupId 和 UseToBind 参数筛选可绑定的模型 API。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayLLMModelAPIs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayLLMModelAPIsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayLLMModelService(
            self,
            request: models.DescribeCloudNativeAPIGatewayLLMModelServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayLLMModelServiceResponse:
        """
        查询单个 LLM 模型服务详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayLLMModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayLLMModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayLLMModelServices(
            self,
            request: models.DescribeCloudNativeAPIGatewayLLMModelServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayLLMModelServicesResponse:
        """
        查询 LLM 模型服务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayLLMModelServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayLLMModelServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayLLMTokenUsageList(
            self,
            request: models.DescribeCloudNativeAPIGatewayLLMTokenUsageListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayLLMTokenUsageListResponse:
        """
        查询 AI 网关Token 消耗统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayLLMTokenUsageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayLLMTokenUsageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics(
            self,
            request: models.DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsResponse:
        """
        查询 AI 网关Token 消耗统计汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPRouteList(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPRouteListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPRouteListResponse:
        """
        上传插件前置操作，获取COS相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPRouteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPRouteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPServer(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPServerRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPServerResponse:
        """
        查询AI 网关MCP服务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPServerACL(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPServerACLRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPServerACLResponse:
        """
        查看 MCP Server ACL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPServerACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPServerACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPServerAuth(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPServerAuthRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPServerAuthResponse:
        """
        查询 MCP Server 的认证配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPServerAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPServerAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPServerList(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPServerListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPServerListResponse:
        """
        AI网关查询MCP服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPServerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPServerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPTool(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolResponse:
        """
        查看AI网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPToolACLList(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolACLListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolACLListResponse:
        """
        查询云原生网关 MCP Server 下所有 Tool 的 ACL 状态一览（含 Server ACLType 回显）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPToolACLList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolACLListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPToolImportTask(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolImportTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolImportTaskResponse:
        """
        查询批量导入MCP Tools的任务进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPToolImportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolImportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPToolList(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolListResponse:
        """
        查询 AI 网关MCP Tool 列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPToolList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPToolVersion(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolVersionResponse:
        """
        修改云原生智能网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPToolVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPToolVersionList(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolVersionListResponse:
        """
        修改云原生智能网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPToolVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayMCPToolsFromFile(
            self,
            request: models.DescribeCloudNativeAPIGatewayMCPToolsFromFileRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayMCPToolsFromFileResponse:
        """
        从OpenAPI文件中解析出可导入的MCP tools
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayMCPToolsFromFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayMCPToolsFromFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewaySecretKey(
            self,
            request: models.DescribeCloudNativeAPIGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewaySecretKeyResponse:
        """
        查询密钥详情（SecretValue 字段会被掩码）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewaySecretKeyList(
            self,
            request: models.DescribeCloudNativeAPIGatewaySecretKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewaySecretKeyListResponse:
        """
        查询密钥列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewaySecretKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewaySecretKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewaySecretKeyValue(
            self,
            request: models.DescribeCloudNativeAPIGatewaySecretKeyValueRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewaySecretKeyValueResponse:
        """
        查询密钥明文值（KMS 类型密钥不可获取）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewaySecretKeyValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewaySecretKeyValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayAIServiceSource(
            self,
            request: models.ModifyCloudNativeAPIGatewayAIServiceSourceRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayAIServiceSourceResponse:
        """
        修改云原生网关AI服务来源
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayAIServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayAIServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayConsumer(
            self,
            request: models.ModifyCloudNativeAPIGatewayConsumerRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayConsumerResponse:
        """
        修改AI网关消费者
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayConsumerGroup(
            self,
            request: models.ModifyCloudNativeAPIGatewayConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayConsumerGroupResponse:
        """
        修改消费者组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayLLMModelAPI(
            self,
            request: models.ModifyCloudNativeAPIGatewayLLMModelAPIRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayLLMModelAPIResponse:
        """
        修改 LLM 模型 API。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayLLMModelAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayLLMModelAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayLLMModelService(
            self,
            request: models.ModifyCloudNativeAPIGatewayLLMModelServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayLLMModelServiceResponse:
        """
        修改 LLM 模型服务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayLLMModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayLLMModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPRoute(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPRouteRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPRouteResponse:
        """
        上传插件前置操作，获取COS相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPRouteStatus(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPRouteStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPRouteStatusResponse:
        """
        上传插件前置操作，获取COS相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPRouteStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPRouteStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPServer(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPServerRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPServerResponse:
        """
        修改MCP服务配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPServerACL(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPServerACLRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPServerACLResponse:
        """
        修改 MCP Server ACL
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPServerACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPServerACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPServerAuth(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPServerAuthRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPServerAuthResponse:
        """
        修改 MCP Server 的认证配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPServerAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPServerAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPServerStatus(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPServerStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPServerStatusResponse:
        """
        创建AI 网关MCP Server
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPServerStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPServerStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPTool(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPToolRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPToolResponse:
        """
        修改AI网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPToolACL(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPToolACLRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPToolACLResponse:
        """
        修改 MCP Server Tool ACL
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPToolACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPToolACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayMCPToolStatus(
            self,
            request: models.ModifyCloudNativeAPIGatewayMCPToolStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayMCPToolStatusResponse:
        """
        AI网关修改MCP Tool上下线状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayMCPToolStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayMCPToolStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewaySecretKey(
            self,
            request: models.ModifyCloudNativeAPIGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewaySecretKeyResponse:
        """
        修改AI网关密钥
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveCloudNativeAPIGatewayConsumerGroupAuth(
            self,
            request: models.RemoveCloudNativeAPIGatewayConsumerGroupAuthRequest,
            opts: Dict = None,
    ) -> models.RemoveCloudNativeAPIGatewayConsumerGroupAuthResponse:
        """
        从资源（模型 API / MCP Server）移除消费者组授权。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveCloudNativeAPIGatewayConsumerGroupAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveCloudNativeAPIGatewayConsumerGroupAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveCloudNativeAPIGatewayConsumerInGroup(
            self,
            request: models.RemoveCloudNativeAPIGatewayConsumerInGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveCloudNativeAPIGatewayConsumerInGroupResponse:
        """
        将消费者从消费者组移除。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveCloudNativeAPIGatewayConsumerInGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveCloudNativeAPIGatewayConsumerInGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackCloudNativeAPIGatewayMCPToolVersion(
            self,
            request: models.RollbackCloudNativeAPIGatewayMCPToolVersionRequest,
            opts: Dict = None,
    ) -> models.RollbackCloudNativeAPIGatewayMCPToolVersionResponse:
        """
        修改云原生智能网关MCP Tool
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackCloudNativeAPIGatewayMCPToolVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackCloudNativeAPIGatewayMCPToolVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindCloudNativeAPIGatewaySecretKey(
            self,
            request: models.UnbindCloudNativeAPIGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.UnbindCloudNativeAPIGatewaySecretKeyResponse:
        """
        解绑密钥
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCloudNativeAPIGatewayMCPTools(
            self,
            request: models.UpdateCloudNativeAPIGatewayMCPToolsRequest,
            opts: Dict = None,
    ) -> models.UpdateCloudNativeAPIGatewayMCPToolsResponse:
        """
        批量导入从OpenAPI文件中解析的MCP Tools
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCloudNativeAPIGatewayMCPTools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCloudNativeAPIGatewayMCPToolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)