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
from tencentcloud.dataagent.v20250513 import models
from typing import Dict


class DataagentClient(AbstractClient):
    _apiVersion = '2025-05-13'
    _endpoint = 'dataagent.tencentcloudapi.com'
    _service = 'dataagent'

    async def AddChunk(
            self,
            request: models.AddChunkRequest,
            opts: Dict = None,
    ) -> models.AddChunkResponse:
        """
        文档切片新增
        """
        
        kwargs = {}
        kwargs["action"] = "AddChunk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddChunkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChatAI(
            self,
            request: models.ChatAIRequest,
            opts: Dict = None,
    ) -> models.ChatAIResponse:
        """
        提供DataAgent 产品服务API
        """
        
        kwargs = {}
        kwargs["action"] = "ChatAI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatAIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataAgentSession(
            self,
            request: models.CreateDataAgentSessionRequest,
            opts: Dict = None,
    ) -> models.CreateDataAgentSessionResponse:
        """
        生成DataAgent 会话ID
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataAgentSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataAgentSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteChunk(
            self,
            request: models.DeleteChunkRequest,
            opts: Dict = None,
    ) -> models.DeleteChunkResponse:
        """
        文档切片删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteChunk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteChunkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataAgentSession(
            self,
            request: models.DeleteDataAgentSessionRequest,
            opts: Dict = None,
    ) -> models.DeleteDataAgentSessionResponse:
        """
        删除会话
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataAgentSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataAgentSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetJobsByKnowledgeBaseId(
            self,
            request: models.GetJobsByKnowledgeBaseIdRequest,
            opts: Dict = None,
    ) -> models.GetJobsByKnowledgeBaseIdResponse:
        """
        根据知识库id查询jobs 列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetJobsByKnowledgeBaseId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetJobsByKnowledgeBaseIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetKnowledgeBaseFileList(
            self,
            request: models.GetKnowledgeBaseFileListRequest,
            opts: Dict = None,
    ) -> models.GetKnowledgeBaseFileListResponse:
        """
        获取知识库文件信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetKnowledgeBaseFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetKnowledgeBaseFileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetKnowledgeBaseList(
            self,
            request: models.GetKnowledgeBaseListRequest,
            opts: Dict = None,
    ) -> models.GetKnowledgeBaseListResponse:
        """
        获取知识库列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetKnowledgeBaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetKnowledgeBaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSessionDetails(
            self,
            request: models.GetSessionDetailsRequest,
            opts: Dict = None,
    ) -> models.GetSessionDetailsResponse:
        """
        获取用户会话记录详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetSessionDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSessionDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUploadJobDetails(
            self,
            request: models.GetUploadJobDetailsRequest,
            opts: Dict = None,
    ) -> models.GetUploadJobDetailsResponse:
        """
        查询上传任务
        """
        
        kwargs = {}
        kwargs["action"] = "GetUploadJobDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUploadJobDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyChunk(
            self,
            request: models.ModifyChunkRequest,
            opts: Dict = None,
    ) -> models.ModifyChunkResponse:
        """
        编辑修改分片
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyChunk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyChunkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKnowledgeBase(
            self,
            request: models.ModifyKnowledgeBaseRequest,
            opts: Dict = None,
    ) -> models.ModifyKnowledgeBaseResponse:
        """
        操作知识库
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKnowledgeBase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKnowledgeBaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChunkList(
            self,
            request: models.QueryChunkListRequest,
            opts: Dict = None,
    ) -> models.QueryChunkListResponse:
        """
        文档切片查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChunkList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChunkListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopChatAI(
            self,
            request: models.StopChatAIRequest,
            opts: Dict = None,
    ) -> models.StopChatAIResponse:
        """
        中断DataAgent的回答输出
        """
        
        kwargs = {}
        kwargs["action"] = "StopChatAI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopChatAIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadAndCommitFile(
            self,
            request: models.UploadAndCommitFileRequest,
            opts: Dict = None,
    ) -> models.UploadAndCommitFileResponse:
        """
        上传提交文件
        """
        
        kwargs = {}
        kwargs["action"] = "UploadAndCommitFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadAndCommitFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)