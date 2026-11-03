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
        【消费者批量自动分配 API Key｜修改：内部并发/配额逻辑，字段不变】ResourceType=Consumer 时与批量预留共用实例写锁，单消费者绑定配额使用当前锁定读。仍按原 SecretKeyId、ResourceIds 绑定；消费者目标最多一个，单密钥不能同时绑定多个消费者，成功仍返回 Result=true。此入口不新增 OperationDenied.BatchKeyPending；该错误属于下述四个变更入口的保护逻辑。
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
        
    async def CreateAIGWCustomGuardrailPolicy(
            self,
            request: models.CreateAIGWCustomGuardrailPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAIGWCustomGuardrailPolicyResponse:
        """
        创建自定义外部审核策略，并把资源绑定配置同步到 Kong Route。建议先调用 DescribeAIGWCustomGuardrailCapabilities、DescribeAIGWCustomGuardrailBindableResources 和 TestAIGWCustomGuardrailPolicy。支持模型 API、MCP Streamable HTTP、A2A Agent API；当前不开放 Dify、Custom Agent、Legacy SSE MCP。请检查 Result.Success、SyncStatus、FailedResources；部分同步失败不等于策略未创建，应按返回 PolicyId 查询并处理，避免重复创建。网关需满足最低版本 3.9.6，且已安装、启用并加载 cngw-ai-custom-guardrail。创建、修改、删除要求网关处于稳定 Running 状态，升级/回滚/撤销升级期间不能修改策略。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。

        输入约束：新配置只接受 field_mapping，不再默认为 standard_v2。创建时鉴权和检测行为必须完整填写；修改为 PATCH，省略保留，显式空值不补默认值。存量 standard_v2 策略仍可查询、删除或直接停用；修改其判定配置或重新启用前需迁移到 field_mapping。条件必填由后端按完整配置校验，非法配置不写库、不下发。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIGWCustomGuardrailPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIGWCustomGuardrailPolicyResponse
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
        创建指定网关实例内的 LLM 模型服务。同一网关下 Name 唯一。可为明确请求 gzip 的供应商选择是否关闭上游压缩协商。
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
        【消费者批量自动分配 API Key｜修改：内部并发/配额逻辑，字段不变】消费者密钥单条创建在事务中使用与批量预留相同的实例写锁，配额检查使用当前锁定读，避免单条与批量并发绕过配额。仍是单条创建；原 GenerateType、请求字段、既有配额错误语义及 Result.Success/ID 不变，不增加 ConsumerIds/ClientToken。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrModifyCloudNativeAPIGatewayIPRestriction(
            self,
            request: models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionRequest,
            opts: Dict = None,
    ) -> models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionResponse:
        """
        创建或编辑云原生网关访问控制
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrModifyCloudNativeAPIGatewayIPRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIGWCustomGuardrailPolicy(
            self,
            request: models.DeleteAIGWCustomGuardrailPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAIGWCustomGuardrailPolicyResponse:
        """
        先清理该策略的 Route 插件投影，再删除策略和绑定。清理失败返回 Result.Success=false，保留策略供排障后重试；不删除绑定的模型、MCP、Agent 或审核引擎服务。网关需满足最低版本 3.9.6，且已安装、启用并加载 cngw-ai-custom-guardrail。创建、修改、删除要求网关处于稳定 Running 状态，升级/回滚/撤销升级期间不能修改策略。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIGWCustomGuardrailPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIGWCustomGuardrailPolicyResponse
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

        同步组仅在 soft_deleted 状态且全部依赖已清理后允许手动硬删除；ConsumerGroupId 使用组织 UUID。存在配额规则时须先删除规则，单纯停用不能解除依赖。硬删除时重新校验，依赖变化可能导致删除失败。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayIPRestriction(
            self,
            request: models.DeleteCloudNativeAPIGatewayIPRestrictionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayIPRestrictionResponse:
        """
        删除云原生网关访问控制
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayIPRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayIPRestrictionResponse
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
        【消费者批量自动分配 API Key｜修改：新增未完成批次保护，字段不变】目标密钥属于批次且对应项处于 Pending/Running/Reconciling 时，删除返回 OperationDenied.BatchKeyPending。完成后仍执行原绑定/依赖删除检查；原 GatewayId/SecretKeyId 不变，成功不新增业务 Result。删除已生成密钥不改写批次历史成功，后续批次明文读取返回逐项 ResourceNotFound.SecretKey。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIGWCustomGuardrailBindableResources(
            self,
            request: models.DescribeAIGWCustomGuardrailBindableResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIGWCustomGuardrailBindableResourcesResponse:
        """
        按一种业务资源类型分页查询绑定候选及 Route 占用情况。编辑策略时传 PolicyId 排除自身占用，选择时同时检查 Supported 和 Occupied。当前屏蔽的 Dify/Custom Agent、Legacy SSE MCP 不进入可绑定列表。创建策略时使用 ResourceId，不使用 RouteIds。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIGWCustomGuardrailBindableResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIGWCustomGuardrailBindableResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIGWCustomGuardrailCapabilities(
            self,
            request: models.DescribeAIGWCustomGuardrailCapabilitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIGWCustomGuardrailCapabilitiesResponse:
        """
        查询当前控制面支持的协议分类、业务资源类型、审核方向及限制。会校验网关版本和插件可用性。Limits 是能力说明，不等于创建/修改策略可配置的字段，也不是逐个数据面实例的实时状态。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIGWCustomGuardrailCapabilities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIGWCustomGuardrailCapabilitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIGWCustomGuardrailHits(
            self,
            request: models.DescribeAIGWCustomGuardrailHitsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIGWCustomGuardrailHitsResponse:
        """
        从网关 RuntimeEventLog 对应 CLS 主题分页查询审核记录，调用前需开启日志投递。按时间倒序返回，查询时间入参为 Unix 秒，记录 Timestamp 为 Unix 毫秒；同一流式业务请求可有多次审核记录。当前查询无导出接口的 1000 条截断限制，使用 Offset/Limit 翻页。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIGWCustomGuardrailHits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIGWCustomGuardrailHitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIGWCustomGuardrailPolicy(
            self,
            request: models.DescribeAIGWCustomGuardrailPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeAIGWCustomGuardrailPolicyResponse:
        """
        查询已有策略、脱敏鉴权配置、资源绑定与配置同步状态。Result 本身就是策略对象，不是 Result.Policy。密钥不返回明文，编辑时省略 ApiKey 即可保留。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIGWCustomGuardrailPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIGWCustomGuardrailPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIGWCustomGuardrailPolicyList(
            self,
            request: models.DescribeAIGWCustomGuardrailPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIGWCustomGuardrailPolicyListResponse:
        """
        按网关分页查询策略；Limit 必填，范围 1～100，Offset 默认 0。支持名称/描述搜索及配置过滤；同项多值 OR，不同过滤项 AND。Result.DataList 为策略数组。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIGWCustomGuardrailPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIGWCustomGuardrailPolicyListResponse
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

        支持 ConsumerGroup 配额，返回 ConsumerGroupPath、ConsumerGroupActive 及实际用量；失效组的规则仍可查询。
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

        支持按 ConsumerGroup 查询组自身配额，默认仍只查询 Consumer；返回组路径、有效状态及实际用量。上下级关联配额请使用 DescribeAIGWConsumerGroupAIQuotaList。
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

        组织架构扩展：保留原消费者详情与完整字段，ConsumerGroups 补齐对应组织成员关系；同步成员保持目录归属隔离。
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

        组织架构扩展：ConsumerGroupId 同时支持原 cg-* 和组织部门 UUID；保留状态、数量、时间和描述逻辑。原普通组状态为 Enable/Disable，目录部门状态为 active/disabled/soft_deleted。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayIPRestriction(
            self,
            request: models.DescribeCloudNativeAPIGatewayIPRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayIPRestrictionResponse:
        """
        查询云原生网关访问控制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayIPRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayIPRestrictionResponse
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
        查询 AI 网关 Token 用量列表。网关版本不低于 3.9.8 且 Dimension=ConsumerGroup 时，未指定节点筛选则列出 Kong CP 当前目录的全部真实节点，包含同步、自定义、禁用及保留中的软删节点，排除合成展示节点。按当前名称、节点 UUID 升序，先分页节点再查询历史指标；无调用节点仍返回，Token 与请求数补零。节点指标包含历史下属，同一请求可计入多个组行，不能逐行相加作为网关总量。 网关版本不低于 3.9.8 时，所有支持维度的消费者组筛选统一为 ConsumerGroupId / ConsumerGroupName，均按历史归属查询；旧 OrganizationNodeId / OrganizationNodeName 筛选不再接受。
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
        查询 AI 网关 Token 用量汇总。网关版本不低于 3.9.8 且 Dimension=ConsumerGroup 时，按历史归属对日志并集去重统计；无节点筛选则查询全部成功归属且祖先集合非空的日志，不依赖当前组织目录候选。返回一份汇总，TopConsumers 为空数组。 网关版本不低于 3.9.8 时，所有支持维度的消费者组筛选统一为 ConsumerGroupId / ConsumerGroupName，均按历史归属查询；旧 OrganizationNodeId / OrganizationNodeName 筛选不再接受。
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
        普通版批量新建密钥的生成来源扩展：新页面按需 IncludeCreationInfo=true，省略/false 保持原响应字段。原 GenerateType 不新增 Batch；批量记录仍为 System。
        【消费者批量自动分配 API Key｜修改：可选参数及可选出参】增加可选 IncludeCreationInfo（默认 false）。仅 true 且 ResourceType=Consumer 时在原 Result 增加 CredentialGenerateType、CreationSource、BatchId 三个非必返字段；省略/false 保持旧响应。原字段、SecretValue 脱敏和单条详情结构不变。
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
        普通版批量新建密钥的生成来源扩展：新页面按需 IncludeCreationInfo=true，省略/false 保持原响应字段。原 GenerateType 不新增 Batch；批量记录仍为 System。
        【消费者批量自动分配 API Key｜修改：可选参数、可选出参及筛选】增加可选 IncludeCreationInfo（默认 false）。仅 true 且 ResourceType=Consumer 时在原 Result.SecretKeys[] 增加 CredentialGenerateType、CreationSource、BatchId 三个非必返字段；Result.TotalCount/SecretKeys 结构不变。Filters 新增 CredentialGenerateType、CreationSource，先过滤后计数分页，与是否返回来源字段独立；保留原 GenerateType 枚举和原分页上限。
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
        
    async def ExportAIGWCustomGuardrailHits(
            self,
            request: models.ExportAIGWCustomGuardrailHitsRequest,
            opts: Dict = None,
    ) -> models.ExportAIGWCustomGuardrailHitsResponse:
        """
        从 RuntimeEventLog 对应 CLS 主题同步导出审核记录，需先开启投递。单次最多 1000 条，可选择 csv（默认）或 json；Result.Content 是 Base64 编码文件内容，不是下载链接。Truncated=true 时可能还有更多记录，请缩小时间范围分别导出。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAIGWCustomGuardrailHits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAIGWCustomGuardrailHitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAIGWCustomGuardrailPolicy(
            self,
            request: models.ModifyAIGWCustomGuardrailPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyAIGWCustomGuardrailPolicyResponse:
        """
        局部修改已有策略并重新同步。省略字段保留原值，显式 false/0/[] 与省略不同；数组按整体替换，Scope 传入时替换完整范围。切换 AddressMode 时会自动清除未显式传入的另一模式地址字段；AuthType=none 会清除已有密钥并默认清空 HeaderName。请检查 Result.Success 和 FailedResources。网关需满足最低版本 3.9.6，且已安装、启用并加载 cngw-ai-custom-guardrail。创建、修改、删除要求网关处于稳定 Running 状态，升级/回滚/撤销升级期间不能修改策略。

        本产品为 cngw，版本为 2023-04-18。公共参数及签名按云 API 规范配置；在 API Explorer 选择目标环境，示例正文仅为业务参数，中文诊断示例以公共参数 Language=zh-CN 为前提。响应业务字段统一位于 Response.Result，Response.RequestId 为云 API 请求 ID；HTTP 成功不代表 Result.Success=true。示例 ID、域名和鉴权值均为占位内容，须替换为实际值。

        输入约束：新配置只接受 field_mapping，不再默认为 standard_v2。创建时鉴权和检测行为必须完整填写；修改为 PATCH，省略保留，显式空值不补默认值。存量 standard_v2 策略仍可查询、删除或直接停用；修改其判定配置或重新启用前需迁移到 field_mapping。条件必填由后端按完整配置校验，非法配置不写库、不下发。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAIGWCustomGuardrailPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIGWCustomGuardrailPolicyResponse
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
        更新指定网关实例内的 LLM 模型服务，可调整该服务向上游请求压缩响应的协商方式。
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
        【消费者批量自动分配 API Key｜修改：新增未完成批次保护，字段不变】目标密钥属于批次且对应项处于 Pending/Running/Reconciling 时，编辑返回 OperationDenied.BatchKeyPending，提示等待批次完成。其他情况继续原编辑校验和行为；原 GatewayId/SecretKeyId/Name/Description 不变，成功不新增业务 Result。
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
        【消费者批量自动分配 API Key｜修改：新增未完成批次保护，字段不变】目标密钥属于批次且对应项处于 Pending/Running/Reconciling 时，解绑返回 OperationDenied.BatchKeyPending。完成后继续原解绑；原 GatewayId/SecretKeyId/ResourceType/ResourceIds 不变，成功不新增业务 Result。解绑不改写批次历史成功，后续批次明文读取返回逐项 OperationDenied.BindingChanged。
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