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
from tencentcloud.workbuddyenterprise.v20260709 import models
from typing import Dict


class WorkbuddyenterpriseClient(AbstractClient):
    _apiVersion = '2026-07-09'
    _endpoint = 'workbuddyenterprise.tencentcloudapi.com'
    _service = 'workbuddyenterprise'

    async def BindExternalAgent(
            self,
            request: models.BindExternalAgentRequest,
            opts: Dict = None,
    ) -> models.BindExternalAgentResponse:
        """
        把外部 agent 绑定到某 managed agent
        """
        
        kwargs = {}
        kwargs["action"] = "BindExternalAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindExternalAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgent(
            self,
            request: models.CreateAgentRequest,
            opts: Dict = None,
    ) -> models.CreateAgentResponse:
        """
        创建一个新的 Managed Agent，同时自动生成 default 版本。配置采用 Manifest v2.0。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentSession(
            self,
            request: models.CreateAgentSessionRequest,
            opts: Dict = None,
    ) -> models.CreateAgentSessionResponse:
        """
        为指定 Agent 创建新的会话，返回会话 ID 和聊天凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentVersion(
            self,
            request: models.CreateAgentVersionRequest,
            opts: Dict = None,
    ) -> models.CreateAgentVersionResponse:
        """
        完全新建版本：外部准备完整 Manifest 后直接传入，不引用任何已有版本。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentVersionFromSource(
            self,
            request: models.CreateAgentVersionFromSourceRequest,
            opts: Dict = None,
    ) -> models.CreateAgentVersionFromSourceResponse:
        """
        基于源版本创建新版本：Manifest / Model / Description 传入即整体覆盖，未传则沿用源版本。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentVersionFromSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentVersionFromSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgent(
            self,
            request: models.DeleteAgentRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentResponse:
        """
        删除指定的 Agent 及其所有版本。删除后不可恢复。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgent(
            self,
            request: models.DescribeAgentRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentResponse:
        """
        查询单个 Agent 的详细信息，包括基础配置和路由配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentList(
            self,
            request: models.DescribeAgentListRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentListResponse:
        """
        查询当前企业的 Agent 列表，支持分页、过滤和排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentSession(
            self,
            request: models.DescribeAgentSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentSessionResponse:
        """
        查询单个 Agent 会话详情：返回会话基础信息（会话名称 / Agent / 版本 / 状态 / 来源 / 发起人）与可用的聊天接入点列表（EndpointSet）。数据面鉴权走 DescribeUserAccessToken 的用户级访问令牌。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentSessionList(
            self,
            request: models.DescribeAgentSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentSessionListResponse:
        """
        分页查询企业下所有会话（跨 Agent）：支持按 SessionId / Status / AgentId / UserId 过滤，按创建 / 更新时间排序，返回会话摘要列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentVersion(
            self,
            request: models.DescribeAgentVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentVersionResponse:
        """
        查询单个版本的详细信息，包括 Manifest、Model、状态等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentVersionList(
            self,
            request: models.DescribeAgentVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentVersionListResponse:
        """
        查询指定 Agent 下的版本列表，支持分页和版本类型过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBuiltinModelList(
            self,
            request: models.DescribeBuiltinModelListRequest,
            opts: Dict = None,
    ) -> models.DescribeBuiltinModelListResponse:
        """
        查询当前企业的内置模型列表，支持分页与过滤。内置模型由平台预置，企业可按需启用/停用。过滤字段支持：ModelId（模型ID，模糊）、Name（模型名称，模糊）、Vendor（供应商，模糊）、Status（状态，精确：enabled/disabled）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBuiltinModelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBuiltinModelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConnectorList(
            self,
            request: models.DescribeConnectorListRequest,
            opts: Dict = None,
    ) -> models.DescribeConnectorListResponse:
        """
        查询指定企业下的连接器列表（PageNumber/PageSize 分页，支持名称模糊与状态、来源过滤）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConnectorList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConnectorListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExpertList(
            self,
            request: models.DescribeExpertListRequest,
            opts: Dict = None,
    ) -> models.DescribeExpertListResponse:
        """
        分页查询 Expert 列表，支持关键词、分类、发布状态过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExpertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExpertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalAgent(
            self,
            request: models.DescribeExternalAgentRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalAgentResponse:
        """
        查询某 managed agent 绑定的单个外部 agent 详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalAgentList(
            self,
            request: models.DescribeExternalAgentListRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalAgentListResponse:
        """
        列某 managed agent 绑定的外部 agent 列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalAgentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalAgentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageEventList(
            self,
            request: models.DescribeMessageEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageEventListResponse:
        """
        按 Session 分页查询消息事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillList(
            self,
            request: models.DescribeSkillListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillListResponse:
        """
        分页查询 Skill 列表，支持关键词、分类、发布状态过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateAgentSession(
            self,
            request: models.MigrateAgentSessionRequest,
            opts: Dict = None,
    ) -> models.MigrateAgentSessionResponse:
        """
        将指定会话迁移到目标版本。SessionID / RuntimeID 保持不变，通过 AgentOS UpdateSession 在原沙箱上更新 manifest 到新版本；AgentId 必须与原 Session 一致（禁止跨 Agent 迁移）；ChatToken 复用旧值不轮转。
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateAgentSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateAgentSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgent(
            self,
            request: models.ModifyAgentRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentResponse:
        """
        修改 Agent 基础信息（名称、描述、头像）。AgentName / Description / AvatarUrl 均为可选，仅传递需要更新的字段。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentA2AConfig(
            self,
            request: models.ModifyAgentA2AConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentA2AConfigResponse:
        """
        修改 Agent 的 A2A 配置。A2AEnabled 是 Agent 级唯一开关，与具体版本和流量分发策略无关。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentA2AConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentA2AConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentRouting(
            self,
            request: models.ModifyAgentRoutingRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentRoutingResponse:
        """
        覆盖式写入 Agent 路由配置（版本权重）。所有 VersionId 必须属于同一 Agent 且未弃用；允许空数组（下线 Agent 对外流量）；非空时权重总和须等于 1。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentRouting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentRoutingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentVersion(
            self,
            request: models.ModifyAgentVersionRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentVersionResponse:
        """
        原地更新 default 或 test 版本的 Manifest / Model / Description / SandboxTemplateId / ConnectorSet（prod 版本冻结不可修改），五个可选字段至少提供一个。ConnectorSet 为全量覆盖语义：缺省表示不改动连接器绑定；空数组表示解绑全部连接器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindExternalAgent(
            self,
            request: models.UnbindExternalAgentRequest,
            opts: Dict = None,
    ) -> models.UnbindExternalAgentResponse:
        """
        解除外部 agent 与 managed agent 的绑定
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindExternalAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindExternalAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)