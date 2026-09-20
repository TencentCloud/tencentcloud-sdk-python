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
from tencentcloud.ags.v20250920 import models


class AgsClient(AbstractClient):
    _apiVersion = '2025-09-20'
    _endpoint = 'ags.tencentcloudapi.com'
    _service = 'ags'


    def AcquireDeploymentToken(self, request):
        r"""获取 Deployment 访问 Token

        :param request: Request instance for AcquireDeploymentToken.
        :type request: :class:`tencentcloud.ags.v20250920.models.AcquireDeploymentTokenRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.AcquireDeploymentTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcquireDeploymentToken", params, headers=headers)
            response = json.loads(body)
            model = models.AcquireDeploymentTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AcquireSandboxInstanceToken(self, request):
        r"""获取访问沙箱工具时所需要使用的访问Token，创建沙箱实例后需调用此接口获取沙箱实例访问Token。
        此Token可用于调用代码沙箱实例执行代码，或浏览器沙箱实例进行浏览器操作等。

        :param request: Request instance for AcquireSandboxInstanceToken.
        :type request: :class:`tencentcloud.ags.v20250920.models.AcquireSandboxInstanceTokenRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.AcquireSandboxInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcquireSandboxInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.AcquireSandboxInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AppendEvent(self, request):
        r"""追加事件。

        向指定会话追加一条事件。

        :param request: Request instance for AppendEvent.
        :type request: :class:`tencentcloud.ags.v20250920.models.AppendEventRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.AppendEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AppendEvent", params, headers=headers)
            response = json.loads(body)
            model = models.AppendEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApproveRegistryRecord(self, request):
        r"""通过 Version 审批：PENDING_APPROVAL → APPROVED。Comment 必填。

        :param request: Request instance for ApproveRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.ApproveRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.ApproveRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApproveRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ApproveRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelRegistryRecord(self, request):
        r"""PREPARING/PENDING_APPROVAL → CANCELED。Comment 必填。

        :param request: Request instance for CancelRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.CancelRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CancelRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CancelRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAPIKey(self, request):
        r"""创建新的API密钥，用于调用Agent Sandbox接口。相较于腾讯云Secret ID Secret Key支持调用所有接口使用，仅有部分接口支持使用API密钥调用。

        :param request: Request instance for CreateAPIKey.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateAPIKeyRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateAPIKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAPIKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAPIKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeployment(self, request):
        r"""创建 Deployment

        :param request: Request instance for CreateDeployment.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateDeploymentRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePreCacheImageTask(self, request):
        r"""创建镜像预热任务

        :param request: Request instance for CreatePreCacheImageTask.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreatePreCacheImageTaskRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreatePreCacheImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePreCacheImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePreCacheImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRegistry(self, request):
        r"""创建 Agent Registry（注册中心）。

        :param request: Request instance for CreateRegistry.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateRegistryRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRegistryRecord(self, request):
        r"""统一创建 Registry Record（含 revision 1）。请求通过 DescriptorType 与严格内容输入 Union 选择底层类型：MCPSource / AgentSource / SkillSource / CustomDescriptors 四选一，必须与 DescriptorType 对应。不接受 RecordId 或 ChangeLog；同名 Record 返回冲突，不隐式追加 Version。追加 Version 请使用 UpdateRegistryRecord。

        :param request: Request instance for CreateRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxTool(self, request):
        r"""创建沙箱工具

        :param request: Request instance for CreateSandboxTool.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateSandboxToolRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateSandboxToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxTool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSession(self, request):
        r"""创建会话。

        为指定 Agent 和用户创建会话，创建成功后返回会话信息。

        :param request: Request instance for CreateSession.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateSessionRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSessionSpace(self, request):
        r"""创建会话空间。
        为当前应用在指定地域创建会话空间，创建成功后返回会话空间信息。会话空间用于隔离不同业务场景下的用户、会话、事件及状态数据。

        :param request: Request instance for CreateSessionSpace.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateSessionSpaceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateSessionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSessionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSessionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAPIKey(self, request):
        r"""删除API密钥。注意区别于腾讯云Secret ID Secret Key，本接口删除的是Agent Sandbox专用API key。

        :param request: Request instance for DeleteAPIKey.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteAPIKeyRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteAPIKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAPIKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAPIKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeployment(self, request):
        r"""删除 Deployment

        :param request: Request instance for DeleteDeployment.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteDeploymentRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRegistry(self, request):
        r"""删除 Registry。

        :param request: Request instance for DeleteRegistry.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteRegistryRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRegistryRecord(self, request):
        r"""删除 Registry Record 或指定 Version。省略 VersionId 时对整个 Record 进行软删除；传入 VersionId 时只删除指定 Version（Stable 指向的 Version 不允许删除；仅剩一个 Approved Version 时不允许删除）。取代原 DeleteRegistryRecordVersion。

        :param request: Request instance for DeleteRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxTool(self, request):
        r"""删除沙箱工具

        :param request: Request instance for DeleteSandboxTool.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteSandboxToolRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteSandboxToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxTool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSession(self, request):
        r"""删除会话

        :param request: Request instance for DeleteSession.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteSessionRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSession", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSessionSpace(self, request):
        r"""删除会话空间。
        删除指定的会话空间。仅允许删除不包含会话、事件或用户状态数据的非默认会话空间；系统默认会话空间不能删除。删除成功后不再返回会话空间信息。

        :param request: Request instance for DeleteSessionSpace.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteSessionSpaceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteSessionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSessionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSessionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPIKeyList(self, request):
        r"""获取API密钥列表，包含API密钥简略信息，包含名称、创建时间等。

        :param request: Request instance for DescribeAPIKeyList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeAPIKeyListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeAPIKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeployment(self, request):
        r"""查询 Deployment 信息

        :param request: Request instance for DescribeDeployment.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeDeploymentRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeploymentList(self, request):
        r"""查询 Deployment 列表

        :param request: Request instance for DescribeDeploymentList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeDeploymentListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeDeploymentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeploymentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeploymentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvents(self, request):
        r"""查询事件列表。

        查询指定会话的事件流，支持按作者和起始时间筛选。

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreCacheImageTask(self, request):
        r"""查询镜像预热任务信息

        :param request: Request instance for DescribePreCacheImageTask.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribePreCacheImageTaskRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribePreCacheImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreCacheImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreCacheImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotaOverview(self, request):
        r"""查询当前调用账号的资源配额和当前总用量，以及账号下各配额组的资源配额和当前用量

        :param request: Request instance for DescribeQuotaOverview.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeQuotaOverviewRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeQuotaOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotaOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistry(self, request):
        r"""按 RegistryId 查询 Registry 详情。

        :param request: Request instance for DescribeRegistry.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryAuditLogList(self, request):
        r"""分页查询指定Registry / Record / Version的审计日志。

        :param request: Request instance for DescribeRegistryAuditLogList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryAuditLogListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryAuditLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryAuditLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryAuditLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryList(self, request):
        r"""分页查询当前租户可见的 Registry 列表。

        :param request: Request instance for DescribeRegistryList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryRecord(self, request):
        r"""查询 Record 详情和其中一个 Version。请求可通过互斥的 VersionId 或 Label 选择 Version；均省略时默认 Label=stable。取代原 DescribeRegistryRecordVersion。

        :param request: Request instance for DescribeRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryRecordList(self, request):
        r"""分页查询 Registry 下的 Record 列表。list 类接口不接入 CAM 转发鉴权；业务侧按 CAM 二次过滤。

        :param request: Request instance for DescribeRegistryRecordList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRecordListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryRecordVersionList(self, request):
        r"""分页查询 Record 的 Version 列表。list 类接口不接入 CAM 转发鉴权。

        :param request: Request instance for DescribeRegistryRecordVersionList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRecordVersionListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeRegistryRecordVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryRecordVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryRecordVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxInstanceList(self, request):
        r"""查询沙箱实例列表

        :param request: Request instance for DescribeSandboxInstanceList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxInstanceListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxToolList(self, request):
        r"""查询沙箱工具列表

        :param request: Request instance for DescribeSandboxToolList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxToolListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxToolListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxToolList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxToolListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSession(self, request):
        r"""查询会话。

        查询指定会话的信息。

        :param request: Request instance for DescribeSession.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSessionRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionSpace(self, request):
        r"""查询会话空间详情。
        查询指定会话空间的详细信息，查询成功后返回会话空间的名称、描述、状态、所属地域及创建时间等信息。

        :param request: Request instance for DescribeSessionSpace.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSessionSpaceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSessionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionSpaces(self, request):
        r"""分页查询当前应用和地域下的会话空间。

        :param request: Request instance for DescribeSessionSpaces.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSessionSpacesRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSessionSpacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionSpaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionSpacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessions(self, request):
        r"""查询会话列表

        :param request: Request instance for DescribeSessions.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSessionsRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSkillPackageDownloadURL(self, request):
        r"""获取 Skill 包下载 URL。VersionId 与 Label 互斥；均省略时使用 Stable。响应包含 ResolvedVersionId，便于调用方回填。

        :param request: Request instance for GetSkillPackageDownloadURL.
        :type request: :class:`tencentcloud.ags.v20250920.models.GetSkillPackageDownloadURLRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.GetSkillPackageDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSkillPackageDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.GetSkillPackageDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSkillPackageUploadURL(self, request):
        r"""为 FAILED / EXPIRED 的 TAR Skill Version 生成新的上传尝试；VersionId 与 Revision 保持不变。

        :param request: Request instance for GetSkillPackageUploadURL.
        :type request: :class:`tencentcloud.ags.v20250920.models.GetSkillPackageUploadURLRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.GetSkillPackageUploadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSkillPackageUploadURL", params, headers=headers)
            response = json.loads(body)
            model = models.GetSkillPackageUploadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeployment(self, request):
        r"""修改 Deployment

        :param request: Request instance for ModifyDeployment.
        :type request: :class:`tencentcloud.ags.v20250920.models.ModifyDeploymentRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.ModifyDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySession(self, request):
        r"""修改会话信息

        :param request: Request instance for ModifySession.
        :type request: :class:`tencentcloud.ags.v20250920.models.ModifySessionRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.ModifySessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySession", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySessionSpace(self, request):
        r"""修改会话空间。
        修改指定会话空间的名称和描述，修改成功后返回更新后的会话空间信息。默认会话空间允许修改名称和描述。

        :param request: Request instance for ModifySessionSpace.
        :type request: :class:`tencentcloud.ags.v20250920.models.ModifySessionSpaceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.ModifySessionSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySessionSpace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySessionSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseSandboxInstance(self, request):
        r"""暂停沙箱实例

        :param request: Request instance for PauseSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.PauseSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.PauseSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.PauseSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PreviewRegistryRecord(self, request):
        r"""对 Record 的指定 Version 或 Label 目标发起一次预览调用。VersionId 与 Label 互斥；均省略时使用 Stable。不创建 Version、不修改 Label。

        :param request: Request instance for PreviewRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.PreviewRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.PreviewRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectRegistryRecord(self, request):
        r"""驳回 Version 审批：PENDING_APPROVAL → REJECTED。Comment 必填。

        :param request: Request instance for RejectRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.RejectRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.RejectRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.RejectRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeSandboxInstance(self, request):
        r"""恢复沙箱实例

        :param request: Request instance for ResumeSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.ResumeSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.ResumeSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartSandboxInstance(self, request):
        r"""启动沙箱实例

        :param request: Request instance for StartSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.StartSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.StartSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StartSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSandboxInstance(self, request):
        r"""停止沙箱实例

        :param request: Request instance for StopSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.StopSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.StopSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StopSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncRegistryRecord(self, request):
        r"""触发一次从远端拉取描述符 / 元数据的同步。可通过互斥的 VersionId 或 Label 指定来源 Version，均省略时默认使用 Stable。有变化时创建新 Version 并移动 Latest；来源必须 SourceType=URL_IMPORT，否则返回 UnsupportedOperation.SourceType。

        :param request: Request instance for SyncRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.SyncRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.SyncRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.SyncRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRegistry(self, request):
        r"""更新 Registry 的可变元数据。

        :param request: Request instance for UpdateRegistry.
        :type request: :class:`tencentcloud.ags.v20250920.models.UpdateRegistryRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.UpdateRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRegistryRecord(self, request):
        r"""更新 Registry Record。两种互斥模式：①Record 更新模式：不提交任何 Source / CustomDescriptors，可通过 Description、LabelMutations 修改元数据与 Label（至少提交一项）；②Version 创建模式：提交且仅提交一种与现有 DescriptorType 匹配的内容输入，可选 VersionName / ChangeLog，禁止 Description / LabelMutations，服务端在 Record 下创建下一个 Revision。取代原 ChangeRegistryRecordStableVersion / RollbackRegistryRecordVersion / Create*RegistryRecordVersion。

        :param request: Request instance for UpdateRegistryRecord.
        :type request: :class:`tencentcloud.ags.v20250920.models.UpdateRegistryRecordRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.UpdateRegistryRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRegistryRecord", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRegistryRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSandboxInstance(self, request):
        r"""更新沙箱实例

        :param request: Request instance for UpdateSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSandboxTool(self, request):
        r"""更新沙箱工具

        :param request: Request instance for UpdateSandboxTool.
        :type request: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxToolRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSandboxTool", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSandboxToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))