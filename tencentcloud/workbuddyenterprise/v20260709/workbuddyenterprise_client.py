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
from tencentcloud.workbuddyenterprise.v20260709 import models


class WorkbuddyenterpriseClient(AbstractClient):
    _apiVersion = '2026-07-09'
    _endpoint = 'workbuddyenterprise.tencentcloudapi.com'
    _service = 'workbuddyenterprise'


    def BindExternalAgent(self, request):
        r"""把外部 agent 绑定到某 managed agent

        :param request: Request instance for BindExternalAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.BindExternalAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.BindExternalAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindExternalAgent", params, headers=headers)
            response = json.loads(body)
            model = models.BindExternalAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgent(self, request):
        r"""创建一个新的 Managed Agent，同时自动生成 default 版本。配置采用 Manifest v2.0。

        :param request: Request instance for CreateAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentResponse`

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


    def CreateAgentSession(self, request):
        r"""为指定 Agent 创建新的会话，返回会话 ID 和聊天凭证。

        :param request: Request instance for CreateAgentSession.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentSessionRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentVersion(self, request):
        r"""完全新建版本：外部准备完整 Manifest 后直接传入，不引用任何已有版本。

        :param request: Request instance for CreateAgentVersion.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentVersionRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentVersionFromSource(self, request):
        r"""基于源版本创建新版本：Manifest / Model / Description 传入即整体覆盖，未传则沿用源版本。

        :param request: Request instance for CreateAgentVersionFromSource.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentVersionFromSourceRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.CreateAgentVersionFromSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentVersionFromSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentVersionFromSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgent(self, request):
        r"""删除指定的 Agent 及其所有版本。删除后不可恢复。

        :param request: Request instance for DeleteAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DeleteAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DeleteAgentResponse`

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


    def DescribeAgent(self, request):
        r"""查询单个 Agent 的详细信息，包括基础配置和路由配置。

        :param request: Request instance for DescribeAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentList(self, request):
        r"""查询当前企业的 Agent 列表，支持分页、过滤和排序。

        :param request: Request instance for DescribeAgentList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentSession(self, request):
        r"""查询单个 Agent 会话详情：返回会话基础信息（会话名称 / Agent / 版本 / 状态 / 来源 / 发起人）与可用的聊天接入点列表（EndpointSet）。数据面鉴权走 DescribeUserAccessToken 的用户级访问令牌。

        :param request: Request instance for DescribeAgentSession.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentSessionRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentSessionList(self, request):
        r"""分页查询企业下所有会话（跨 Agent）：支持按 SessionId / Status / AgentId / UserId 过滤，按创建 / 更新时间排序，返回会话摘要列表。

        :param request: Request instance for DescribeAgentSessionList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentSessionListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentVersion(self, request):
        r"""查询单个版本的详细信息，包括 Manifest、Model、状态等。

        :param request: Request instance for DescribeAgentVersion.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentVersionRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentVersionList(self, request):
        r"""查询指定 Agent 下的版本列表，支持分页和版本类型过滤。

        :param request: Request instance for DescribeAgentVersionList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentVersionListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeAgentVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBuiltinModelList(self, request):
        r"""查询当前企业的内置模型列表，支持分页与过滤。内置模型由平台预置，企业可按需启用/停用。过滤字段支持：ModelId（模型ID，模糊）、Name（模型名称，模糊）、Vendor（供应商，模糊）、Status（状态，精确：enabled/disabled）。

        :param request: Request instance for DescribeBuiltinModelList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeBuiltinModelListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeBuiltinModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBuiltinModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBuiltinModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConnectorList(self, request):
        r"""查询指定企业下的连接器列表（PageNumber/PageSize 分页，支持名称模糊与状态、来源过滤）。

        :param request: Request instance for DescribeConnectorList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeConnectorListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeConnectorListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConnectorList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConnectorListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertList(self, request):
        r"""分页查询 Expert 列表，支持关键词、分类、发布状态过滤。

        :param request: Request instance for DescribeExpertList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeExpertListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeExpertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExternalAgent(self, request):
        r"""查询某 managed agent 绑定的单个外部 agent 详情

        :param request: Request instance for DescribeExternalAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeExternalAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeExternalAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExternalAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExternalAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExternalAgentList(self, request):
        r"""列某 managed agent 绑定的外部 agent 列表

        :param request: Request instance for DescribeExternalAgentList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeExternalAgentListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeExternalAgentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExternalAgentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExternalAgentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageEventList(self, request):
        r"""按 Session 分页查询消息事件

        :param request: Request instance for DescribeMessageEventList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeMessageEventListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeMessageEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillList(self, request):
        r"""分页查询 Skill 列表，支持关键词、分类、发布状态过滤。

        :param request: Request instance for DescribeSkillList.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeSkillListRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.DescribeSkillListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigrateAgentSession(self, request):
        r"""将指定会话迁移到目标版本。SessionID / RuntimeID 保持不变，通过 AgentOS UpdateSession 在原沙箱上更新 manifest 到新版本；AgentId 必须与原 Session 一致（禁止跨 Agent 迁移）；ChatToken 复用旧值不轮转。

        :param request: Request instance for MigrateAgentSession.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.MigrateAgentSessionRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.MigrateAgentSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateAgentSession", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateAgentSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgent(self, request):
        r"""修改 Agent 基础信息（名称、描述、头像）。AgentName / Description / AvatarUrl 均为可选，仅传递需要更新的字段。

        :param request: Request instance for ModifyAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentResponse`

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


    def ModifyAgentA2AConfig(self, request):
        r"""修改 Agent 的 A2A 配置。A2AEnabled 是 Agent 级唯一开关，与具体版本和流量分发策略无关。

        :param request: Request instance for ModifyAgentA2AConfig.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentA2AConfigRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentA2AConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentA2AConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentA2AConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentRouting(self, request):
        r"""覆盖式写入 Agent 路由配置（版本权重）。所有 VersionId 必须属于同一 Agent 且未弃用；允许空数组（下线 Agent 对外流量）；非空时权重总和须等于 1。

        :param request: Request instance for ModifyAgentRouting.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentRoutingRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentRoutingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentRouting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentRoutingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentVersion(self, request):
        r"""原地更新 default 或 test 版本的 Manifest / Model / Description / SandboxTemplateId / ConnectorSet（prod 版本冻结不可修改），五个可选字段至少提供一个。ConnectorSet 为全量覆盖语义：缺省表示不改动连接器绑定；空数组表示解绑全部连接器。

        :param request: Request instance for ModifyAgentVersion.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentVersionRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ModifyAgentVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindExternalAgent(self, request):
        r"""解除外部 agent 与 managed agent 的绑定

        :param request: Request instance for UnbindExternalAgent.
        :type request: :class:`tencentcloud.workbuddyenterprise.v20260709.models.UnbindExternalAgentRequest`
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.UnbindExternalAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindExternalAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindExternalAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))