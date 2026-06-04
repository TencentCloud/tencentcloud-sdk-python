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
        
    async def ResetConversation(
            self,
            request: models.ResetConversationRequest,
            opts: Dict = None,
    ) -> models.ResetConversationResponse:
        """
        重置会话
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConversationResponse
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