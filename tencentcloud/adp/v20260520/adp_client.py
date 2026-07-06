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
from tencentcloud.adp.v20260520 import models


class AdpClient(AbstractClient):
    _apiVersion = '2026-05-20'
    _endpoint = 'adp.tencentcloudapi.com'
    _service = 'adp'


    def CopyAgentFromApp(self, request):
        r"""创建Agent

        :param request: Request instance for CopyAgentFromApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.CopyAgentFromAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CopyAgentFromAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyAgentFromApp", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAgentFromAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyApp(self, request):
        r"""复制应用

        :param request: Request instance for CopyApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.CopyAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CopyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyApp", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgent(self, request):
        r"""创建Agent

        :param request: Request instance for CreateAgent.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateAgentRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApp(self, request):
        r"""创建应用

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConversation(self, request):
        r"""新建会话

        :param request: Request instance for CreateConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConversation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlugin(self, request):
        r"""获取插件详情

        :param request: Request instance for CreatePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreatePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreatePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRelease(self, request):
        r"""新增发布任务

        :param request: Request instance for CreateRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRelease", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSkill(self, request):
        r"""创建skill

        :param request: Request instance for CreateSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSkill", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSkillShare(self, request):
        r"""提交自定义Skill至企业级共享审批（两段式：提交→审批→回调创建共享任务）

        :param request: Request instance for CreateSkillShare.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSkillShareRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSkillShareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSkillShare", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSkillShareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSpace(self, request):
        r"""创建空间

        :param request: Request instance for CreateSpace.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSpaceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSpace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVariable(self, request):
        r"""创建参数变量

        :param request: Request instance for CreateVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVariable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebSocketToken(self, request):
        r"""创建 WebSocket Token

        :param request: Request instance for CreateWebSocketToken.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateWebSocketTokenRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateWebSocketTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebSocketToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebSocketTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkspaceCredential(self, request):
        r"""创建工作空间凭证

        :param request: Request instance for CreateWorkspaceCredential.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateWorkspaceCredentialRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateWorkspaceCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgent(self, request):
        r"""删除Agent

        :param request: Request instance for DeleteAgent.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteAgentRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApp(self, request):
        r"""删除应用

        :param request: Request instance for DeleteApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConversation(self, request):
        r"""删除会话

        :param request: Request instance for DeleteConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConversation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePlugin(self, request):
        r"""修改插件

        :param request: Request instance for DeletePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeletePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeletePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSkill(self, request):
        r"""删除自定义 Skill  鉴权：创建者 ∨ (编辑权限 ∧ 删除权限） 拒绝场景：非 Custom 类型 / 已共享 / 安全检测中 / 上架审批中 / 下架审批中

        :param request: Request instance for DeleteSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSkill", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSkillShare(self, request):
        r"""提交共享 Skill 下架审批（v2，两段式：提交→审批→回调下架共享 Skill） 鉴权：删除权 拒绝场景：未共享 / 上架审批中 / 下架审批中

        :param request: Request instance for DeleteSkillShare.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteSkillShareRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteSkillShareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSkillShare", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSkillShareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSpace(self, request):
        r"""删除空间

        :param request: Request instance for DeleteSpace.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteSpaceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVariable(self, request):
        r"""删除参数变量

        :param request: Request instance for DeleteVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVariable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDetail(self, request):
        r"""查询 Agent 详情

        :param request: Request instance for DescribeAgentDetail.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAgentDetailRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAgentDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentReleasePreviewList(self, request):
        r"""获取应用下 Agent 的发布预览列表

        :param request: Request instance for DescribeAgentReleasePreviewList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAgentReleasePreviewListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAgentReleasePreviewListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentReleasePreviewList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentReleasePreviewListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentSummaryList(self, request):
        r"""查询 Agent 摘要信息列表

        :param request: Request instance for DescribeAgentSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAgentSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAgentSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApp(self, request):
        r"""获取应用信息

        :param request: Request instance for DescribeApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppSummaryList(self, request):
        r"""获取应用摘要列表

        :param request: Request instance for DescribeAppSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConversation(self, request):
        r"""查看会话信息

        :param request: Request instance for DescribeConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConversationList(self, request):
        r"""获取会话列表

        :param request: Request instance for DescribeConversationList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConversationListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConversationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConversationMessageList(self, request):
        r"""获取会话历史消息

        :param request: Request instance for DescribeConversationMessageList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConversationMessageListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConversationMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversationMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLatestRelease(self, request):
        r"""拉取最新发布信息(包含发布时间、状态、渠道)

        :param request: Request instance for DescribeLatestRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeLatestReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeLatestReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLatestRelease", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLatestReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelList(self, request):
        r"""查询模型列表

        :param request: Request instance for DescribeModelList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeModelListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlugin(self, request):
        r"""获取插件详情

        :param request: Request instance for DescribePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePluginSummaryList(self, request):
        r"""获取插件列表

        :param request: Request instance for DescribePluginSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribePluginSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribePluginSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseList(self, request):
        r"""发布记录列表

        :param request: Request instance for DescribeReleaseList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseSummary(self, request):
        r"""查询发布任务

        :param request: Request instance for DescribeReleaseSummary.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseSummaryRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillCategoryList(self, request):
        r"""查询 Skill 分类列表

        :param request: Request instance for DescribeSkillCategoryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillCategoryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillDetail(self, request):
        r"""查询skill详情

        :param request: Request instance for DescribeSkillDetail.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillDetailRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillReferenceList(self, request):
        r"""查询某个 Skill 被引用的详情列表（按 SkillRefType 分组：OpenClaw / cloud agent / 企业助手 agent） 鉴权：同 DescribeSkillDetail（能看该 Skill 即可查）

        :param request: Request instance for DescribeSkillReferenceList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillReferenceListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillReferenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillReferenceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillReferenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillSummaryList(self, request):
        r"""查询 Skill 列表

        :param request: Request instance for DescribeSkillSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceList(self, request):
        r"""获取空间列表

        :param request: Request instance for DescribeSpaceList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSpaceListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSpaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemVariableList(self, request):
        r"""获取系统变量

        :param request: Request instance for DescribeSystemVariableList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSystemVariableListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSystemVariableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemVariableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemVariableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVariable(self, request):
        r"""获取参数变量

        :param request: Request instance for DescribeVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVariable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVariableList(self, request):
        r"""获取参数变量列表

        :param request: Request instance for DescribeVariableList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeVariableListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeVariableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVariableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVariableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FavoritePlugin(self, request):
        r"""收藏插件

        :param request: Request instance for FavoritePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.FavoritePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.FavoritePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FavoritePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.FavoritePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FavoriteSkill(self, request):
        r"""收藏skill

        :param request: Request instance for FavoriteSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.FavoriteSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.FavoriteSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FavoriteSkill", params, headers=headers)
            response = json.loads(body)
            model = models.FavoriteSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgent(self, request):
        r"""修改Agent配置信息

        :param request: Request instance for ModifyAgent.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyAgentRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApp(self, request):
        r"""修改应用

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConversation(self, request):
        r"""修改会话信息

        :param request: Request instance for ModifyConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConversation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPlugin(self, request):
        r"""修改插件

        :param request: Request instance for ModifyPlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyPluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySkill(self, request):
        r"""Skill修改

        :param request: Request instance for ModifySkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifySkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifySkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySkill", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySpace(self, request):
        r"""编辑空间

        :param request: Request instance for ModifySpace.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifySpaceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifySpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVariable(self, request):
        r"""更新参数变量

        :param request: Request instance for ModifyVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVariable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseSkill(self, request):
        r"""上架skill

        :param request: Request instance for ReleaseSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.ReleaseSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ReleaseSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseSkill", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetConversation(self, request):
        r"""重置会话

        :param request: Request instance for ResetConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.ResetConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ResetConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetConversation", params, headers=headers)
            response = json.loads(body)
            model = models.ResetConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRelease(self, request):
        r"""重试发布(发布暂停之后再次重新发布)

        :param request: Request instance for RetryRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.RetryReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.RetryReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRelease", params, headers=headers)
            response = json.loads(body)
            model = models.RetryReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackRelease(self, request):
        r"""回滚发布

        :param request: Request instance for RollbackRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.RollbackReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.RollbackReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackRelease", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnfavoritePlugin(self, request):
        r"""取消收藏插件

        :param request: Request instance for UnfavoritePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.UnfavoritePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.UnfavoritePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnfavoritePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.UnfavoritePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnfavoriteSkill(self, request):
        r"""取消收藏skill

        :param request: Request instance for UnfavoriteSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.UnfavoriteSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.UnfavoriteSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnfavoriteSkill", params, headers=headers)
            response = json.loads(body)
            model = models.UnfavoriteSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))