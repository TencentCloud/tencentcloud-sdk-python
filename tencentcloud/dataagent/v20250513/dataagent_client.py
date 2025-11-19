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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dataagent.v20250513 import models


class DataagentClient(AbstractClient):
    _apiVersion = '2025-05-13'
    _endpoint = 'dataagent.tencentcloudapi.com'
    _service = 'dataagent'


    def AddChunk(self, request):
        r"""文档切片新增

        :param request: Request instance for AddChunk.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.AddChunkRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.AddChunkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddChunk", params, headers=headers)
            response = json.loads(body)
            model = models.AddChunkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatAI(self, request):
        r"""提供DataAgent 产品服务API

        :param request: Request instance for ChatAI.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.ChatAIRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.ChatAIResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatAI", params, models.ChatAIResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataAgentSession(self, request):
        r"""生成DataAgent 会话ID

        :param request: Request instance for CreateDataAgentSession.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.CreateDataAgentSessionRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.CreateDataAgentSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataAgentSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataAgentSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteChunk(self, request):
        r"""文档切片删除

        :param request: Request instance for DeleteChunk.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.DeleteChunkRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.DeleteChunkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteChunk", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteChunkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataAgentSession(self, request):
        r"""删除会话

        :param request: Request instance for DeleteDataAgentSession.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.DeleteDataAgentSessionRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.DeleteDataAgentSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataAgentSession", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataAgentSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetKnowledgeBaseList(self, request):
        r"""获取知识库列表

        :param request: Request instance for GetKnowledgeBaseList.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.GetKnowledgeBaseListRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.GetKnowledgeBaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetKnowledgeBaseList", params, headers=headers)
            response = json.loads(body)
            model = models.GetKnowledgeBaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSessionDetails(self, request):
        r"""获取用户会话记录详情列表

        :param request: Request instance for GetSessionDetails.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.GetSessionDetailsRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.GetSessionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSessionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.GetSessionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyChunk(self, request):
        r"""编辑修改分片

        :param request: Request instance for ModifyChunk.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.ModifyChunkRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.ModifyChunkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyChunk", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyChunkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKnowledgeBase(self, request):
        r"""操作知识库

        :param request: Request instance for ModifyKnowledgeBase.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.ModifyKnowledgeBaseRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.ModifyKnowledgeBaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKnowledgeBase", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKnowledgeBaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryChunkList(self, request):
        r"""文档切片查询

        :param request: Request instance for QueryChunkList.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.QueryChunkListRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.QueryChunkListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChunkList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChunkListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopChatAI(self, request):
        r"""中断DataAgent的回答输出

        :param request: Request instance for StopChatAI.
        :type request: :class:`tencentcloud.dataagent.v20250513.models.StopChatAIRequest`
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.StopChatAIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopChatAI", params, headers=headers)
            response = json.loads(body)
            model = models.StopChatAIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))