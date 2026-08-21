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
from tencentcloud.adp.v20260520 import models
from typing import Dict


class AdpClient(AbstractClient):
    _apiVersion = '2026-05-20'
    _endpoint = 'adp.tencentcloudapi.com'
    _service = 'adp'

    async def CopyAgentFromApp(
            self,
            request: models.CopyAgentFromAppRequest,
            opts: Dict = None,
    ) -> models.CopyAgentFromAppResponse:
        """
        创建Agent
        """
        
        kwargs = {}
        kwargs["action"] = "CopyAgentFromApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyAgentFromAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyApp(
            self,
            request: models.CopyAppRequest,
            opts: Dict = None,
    ) -> models.CopyAppResponse:
        """
        复制应用
        """
        
        kwargs = {}
        kwargs["action"] = "CopyApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgent(
            self,
            request: models.CreateAgentRequest,
            opts: Dict = None,
    ) -> models.CreateAgentResponse:
        """
        创建Agent
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApp(
            self,
            request: models.CreateAppRequest,
            opts: Dict = None,
    ) -> models.CreateAppResponse:
        """
        创建应用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAppTrigger(
            self,
            request: models.CreateAppTriggerRequest,
            opts: Dict = None,
    ) -> models.CreateAppTriggerResponse:
        """
        CreateAppTrigger
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConversation(
            self,
            request: models.CreateConversationRequest,
            opts: Dict = None,
    ) -> models.CreateConversationResponse:
        """
        新建会话
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMsgRecordCategory(
            self,
            request: models.CreateMsgRecordCategoryRequest,
            opts: Dict = None,
    ) -> models.CreateMsgRecordCategoryResponse:
        """
        创建一条消息记录分类，支持指定分类名称与父分类（ParentId 为 0 时表示一级分类）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMsgRecordCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMsgRecordCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlugin(
            self,
            request: models.CreatePluginRequest,
            opts: Dict = None,
    ) -> models.CreatePluginResponse:
        """
        获取插件详情
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRelease(
            self,
            request: models.CreateReleaseRequest,
            opts: Dict = None,
    ) -> models.CreateReleaseResponse:
        """
        新增发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSkill(
            self,
            request: models.CreateSkillRequest,
            opts: Dict = None,
    ) -> models.CreateSkillResponse:
        """
        创建skill
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSkillShare(
            self,
            request: models.CreateSkillShareRequest,
            opts: Dict = None,
    ) -> models.CreateSkillShareResponse:
        """
        提交自定义Skill至企业级共享审批（两段式：提交→审批→回调创建共享任务）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSkillShare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSkillShareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSpace(
            self,
            request: models.CreateSpaceRequest,
            opts: Dict = None,
    ) -> models.CreateSpaceResponse:
        """
        创建空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVariable(
            self,
            request: models.CreateVariableRequest,
            opts: Dict = None,
    ) -> models.CreateVariableResponse:
        """
        创建参数变量
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVariable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVariableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebSocketToken(
            self,
            request: models.CreateWebSocketTokenRequest,
            opts: Dict = None,
    ) -> models.CreateWebSocketTokenResponse:
        """
        创建 WebSocket Token
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebSocketToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebSocketTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspaceCredential(
            self,
            request: models.CreateWorkspaceCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceCredentialResponse:
        """
        创建工作空间凭证
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspaceCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgent(
            self,
            request: models.DeleteAgentRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentResponse:
        """
        删除Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApp(
            self,
            request: models.DeleteAppRequest,
            opts: Dict = None,
    ) -> models.DeleteAppResponse:
        """
        删除应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppTrigger(
            self,
            request: models.DeleteAppTriggerRequest,
            opts: Dict = None,
    ) -> models.DeleteAppTriggerResponse:
        """
        DeleteAppTrigger
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConversation(
            self,
            request: models.DeleteConversationRequest,
            opts: Dict = None,
    ) -> models.DeleteConversationResponse:
        """
        删除会话
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMsgRecordCategory(
            self,
            request: models.DeleteMsgRecordCategoryRequest,
            opts: Dict = None,
    ) -> models.DeleteMsgRecordCategoryResponse:
        """
        删除指定的消息记录分类
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMsgRecordCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMsgRecordCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePlugin(
            self,
            request: models.DeletePluginRequest,
            opts: Dict = None,
    ) -> models.DeletePluginResponse:
        """
        修改插件
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSkill(
            self,
            request: models.DeleteSkillRequest,
            opts: Dict = None,
    ) -> models.DeleteSkillResponse:
        """
        删除自定义 Skill  鉴权：创建者 ∨ (编辑权限 ∧ 删除权限） 拒绝场景：非 Custom 类型 / 已共享 / 安全检测中 / 上架审批中 / 下架审批中
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSkillShare(
            self,
            request: models.DeleteSkillShareRequest,
            opts: Dict = None,
    ) -> models.DeleteSkillShareResponse:
        """
        提交共享 Skill 下架审批（v2，两段式：提交→审批→回调下架共享 Skill） 鉴权：删除权 拒绝场景：未共享 / 上架审批中 / 下架审批中
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSkillShare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSkillShareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSpace(
            self,
            request: models.DeleteSpaceRequest,
            opts: Dict = None,
    ) -> models.DeleteSpaceResponse:
        """
        删除空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVariable(
            self,
            request: models.DeleteVariableRequest,
            opts: Dict = None,
    ) -> models.DeleteVariableResponse:
        """
        删除参数变量
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVariable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVariableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountList(
            self,
            request: models.DescribeAccountListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountListResponse:
        """
        查看企业下的员工列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDetail(
            self,
            request: models.DescribeAgentDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDetailResponse:
        """
        查询 Agent 详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentReleasePreviewList(
            self,
            request: models.DescribeAgentReleasePreviewListRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentReleasePreviewListResponse:
        """
        获取应用下 Agent 的发布预览列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentReleasePreviewList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentReleasePreviewListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentSummaryList(
            self,
            request: models.DescribeAgentSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentSummaryListResponse:
        """
        查询 Agent 摘要信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApp(
            self,
            request: models.DescribeAppRequest,
            opts: Dict = None,
    ) -> models.DescribeAppResponse:
        """
        获取应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppSummaryList(
            self,
            request: models.DescribeAppSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppSummaryListResponse:
        """
        获取应用摘要列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppTrigger(
            self,
            request: models.DescribeAppTriggerRequest,
            opts: Dict = None,
    ) -> models.DescribeAppTriggerResponse:
        """
        DescribeAppTrigger
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppTriggerInstance(
            self,
            request: models.DescribeAppTriggerInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeAppTriggerInstanceResponse:
        """
        DescribeAppTriggerInstance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppTriggerInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppTriggerInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppTriggerRunLogList(
            self,
            request: models.DescribeAppTriggerRunLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppTriggerRunLogListResponse:
        """
        DescribeAppTriggerRunLogList
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppTriggerRunLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppTriggerRunLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppTriggerSummaryList(
            self,
            request: models.DescribeAppTriggerSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppTriggerSummaryListResponse:
        """
        DescribeAppTriggerSummaryList
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppTriggerSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppTriggerSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogList(
            self,
            request: models.DescribeAuditLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogListResponse:
        """
        查看操作日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogMeta(
            self,
            request: models.DescribeAuditLogMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogMetaResponse:
        """
        获取审计日志元信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrencyLimitDetailList(
            self,
            request: models.DescribeConcurrencyLimitDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrencyLimitDetailListResponse:
        """
        查询并发超限明细，包含QPM/TPM超限与专属并发超限记录，返回超限发生时间、空间、应用、模型及请求内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrencyLimitDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrencyLimitDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumptionDetailList(
            self,
            request: models.DescribeConsumptionDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumptionDetailListResponse:
        """
        查询资源消耗明细，包含计费相关字段（消耗类型、消耗目标、消耗场景、套餐包及PU消耗等）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumptionDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumptionDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConversation(
            self,
            request: models.DescribeConversationRequest,
            opts: Dict = None,
    ) -> models.DescribeConversationResponse:
        """
        查看会话信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConversationList(
            self,
            request: models.DescribeConversationListRequest,
            opts: Dict = None,
    ) -> models.DescribeConversationListResponse:
        """
        获取会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConversationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConversationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConversationMessageList(
            self,
            request: models.DescribeConversationMessageListRequest,
            opts: Dict = None,
    ) -> models.DescribeConversationMessageListResponse:
        """
        获取会话历史消息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConversationMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConversationMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLatestRelease(
            self,
            request: models.DescribeLatestReleaseRequest,
            opts: Dict = None,
    ) -> models.DescribeLatestReleaseResponse:
        """
        拉取最新发布信息(包含发布时间、状态、渠道)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLatestRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLatestReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricOverviewList(
            self,
            request: models.DescribeMetricOverviewListRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricOverviewListResponse:
        """
        查询看板总览KPI卡片数据，通过resource_type区分资源看板与业务看板域，返回各域KPI指标列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricOverviewList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricOverviewListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelList(
            self,
            request: models.DescribeModelListRequest,
            opts: Dict = None,
    ) -> models.DescribeModelListResponse:
        """
        查询模型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsgRecordCategoryList(
            self,
            request: models.DescribeMsgRecordCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeMsgRecordCategoryListResponse:
        """
        查询应用的消息记录分类树，返回分类及子分类、各分类下记录数量与操作权限
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsgRecordCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsgRecordCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsgRecordList(
            self,
            request: models.DescribeMsgRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeMsgRecordListResponse:
        """
        查询应用的对话消息记录列表，支持按渠道类型、反馈类型、意图、调用结果等条件过滤，并支持游标分页与按创建时间排序
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsgRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsgRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlugin(
            self,
            request: models.DescribePluginRequest,
            opts: Dict = None,
    ) -> models.DescribePluginResponse:
        """
        获取插件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginSummaryList(
            self,
            request: models.DescribePluginSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribePluginSummaryListResponse:
        """
        获取插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseList(
            self,
            request: models.DescribeReleaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseListResponse:
        """
        发布记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseSummary(
            self,
            request: models.DescribeReleaseSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseSummaryResponse:
        """
        查询发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillCategoryList(
            self,
            request: models.DescribeSkillCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillCategoryListResponse:
        """
        查询 Skill 分类列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillDetail(
            self,
            request: models.DescribeSkillDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillDetailResponse:
        """
        查询skill详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillReferenceList(
            self,
            request: models.DescribeSkillReferenceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillReferenceListResponse:
        """
        查询某个 Skill 被引用的详情列表（按 SkillRefType 分组：OpenClaw / cloud agent / 企业助手 agent） 鉴权：同 DescribeSkillDetail（能看该 Skill 即可查）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillReferenceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillReferenceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillSummaryList(
            self,
            request: models.DescribeSkillSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillSummaryListResponse:
        """
        查询 Skill 列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceList(
            self,
            request: models.DescribeSpaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceListResponse:
        """
        获取空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemVariableList(
            self,
            request: models.DescribeSystemVariableListRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemVariableListResponse:
        """
        获取系统变量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemVariableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemVariableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsageDetailList(
            self,
            request: models.DescribeUsageDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageDetailListResponse:
        """
        查询资源调用时序明细，支持模型和插件两类资源，按时间顺序返回每条调用记录的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsageSummaryList(
            self,
            request: models.DescribeUsageSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageSummaryListResponse:
        """
        查询资源用量聚合明细，支持模型、插件、平台三类资源，按空间/应用维度聚合展示调用次数、Token消耗等指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVariable(
            self,
            request: models.DescribeVariableRequest,
            opts: Dict = None,
    ) -> models.DescribeVariableResponse:
        """
        获取参数变量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVariable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVariableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVariableList(
            self,
            request: models.DescribeVariableListRequest,
            opts: Dict = None,
    ) -> models.DescribeVariableListResponse:
        """
        获取参数变量列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVariableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVariableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FavoritePlugin(
            self,
            request: models.FavoritePluginRequest,
            opts: Dict = None,
    ) -> models.FavoritePluginResponse:
        """
        收藏插件
        """
        
        kwargs = {}
        kwargs["action"] = "FavoritePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FavoritePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FavoriteSkill(
            self,
            request: models.FavoriteSkillRequest,
            opts: Dict = None,
    ) -> models.FavoriteSkillResponse:
        """
        收藏skill
        """
        
        kwargs = {}
        kwargs["action"] = "FavoriteSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FavoriteSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgent(
            self,
            request: models.ModifyAgentRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentResponse:
        """
        修改Agent配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApp(
            self,
            request: models.ModifyAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAppResponse:
        """
        修改应用
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAppTrigger(
            self,
            request: models.ModifyAppTriggerRequest,
            opts: Dict = None,
    ) -> models.ModifyAppTriggerResponse:
        """
        ModifyAppTrigger
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAppTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConversation(
            self,
            request: models.ModifyConversationRequest,
            opts: Dict = None,
    ) -> models.ModifyConversationResponse:
        """
        修改会话信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMsgRecordCategory(
            self,
            request: models.ModifyMsgRecordCategoryRequest,
            opts: Dict = None,
    ) -> models.ModifyMsgRecordCategoryResponse:
        """
        修改指定消息记录分类的名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMsgRecordCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMsgRecordCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPlugin(
            self,
            request: models.ModifyPluginRequest,
            opts: Dict = None,
    ) -> models.ModifyPluginResponse:
        """
        修改插件
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySkill(
            self,
            request: models.ModifySkillRequest,
            opts: Dict = None,
    ) -> models.ModifySkillResponse:
        """
        Skill修改
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySpace(
            self,
            request: models.ModifySpaceRequest,
            opts: Dict = None,
    ) -> models.ModifySpaceResponse:
        """
        编辑空间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVariable(
            self,
            request: models.ModifyVariableRequest,
            opts: Dict = None,
    ) -> models.ModifyVariableResponse:
        """
        更新参数变量
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVariable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVariableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseAppTrigger(
            self,
            request: models.PauseAppTriggerRequest,
            opts: Dict = None,
    ) -> models.PauseAppTriggerResponse:
        """
        PauseAppTrigger
        """
        
        kwargs = {}
        kwargs["action"] = "PauseAppTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseAppTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseSkill(
            self,
            request: models.ReleaseSkillRequest,
            opts: Dict = None,
    ) -> models.ReleaseSkillResponse:
        """
        上架skill
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetConversation(
            self,
            request: models.ResetConversationRequest,
            opts: Dict = None,
    ) -> models.ResetConversationResponse:
        """
        重置会话
        注意：当前Claw模式应用会话不支持重置
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeAppTrigger(
            self,
            request: models.ResumeAppTriggerRequest,
            opts: Dict = None,
    ) -> models.ResumeAppTriggerResponse:
        """
        ResumeAppTrigger
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeAppTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeAppTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRelease(
            self,
            request: models.RetryReleaseRequest,
            opts: Dict = None,
    ) -> models.RetryReleaseResponse:
        """
        重试发布(发布暂停之后再次重新发布)
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackRelease(
            self,
            request: models.RollbackReleaseRequest,
            opts: Dict = None,
    ) -> models.RollbackReleaseResponse:
        """
        回滚发布
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunAppTriggerNow(
            self,
            request: models.RunAppTriggerNowRequest,
            opts: Dict = None,
    ) -> models.RunAppTriggerNowResponse:
        """
        RunAppTriggerNow
        """
        
        kwargs = {}
        kwargs["action"] = "RunAppTriggerNow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunAppTriggerNowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnfavoritePlugin(
            self,
            request: models.UnfavoritePluginRequest,
            opts: Dict = None,
    ) -> models.UnfavoritePluginResponse:
        """
        取消收藏插件
        """
        
        kwargs = {}
        kwargs["action"] = "UnfavoritePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnfavoritePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnfavoriteSkill(
            self,
            request: models.UnfavoriteSkillRequest,
            opts: Dict = None,
    ) -> models.UnfavoriteSkillResponse:
        """
        取消收藏skill
        """
        
        kwargs = {}
        kwargs["action"] = "UnfavoriteSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnfavoriteSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)