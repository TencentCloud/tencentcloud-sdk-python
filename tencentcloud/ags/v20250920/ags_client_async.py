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
from tencentcloud.ags.v20250920 import models
from typing import Dict


class AgsClient(AbstractClient):
    _apiVersion = '2025-09-20'
    _endpoint = 'ags.tencentcloudapi.com'
    _service = 'ags'

    async def AcquireDeploymentToken(
            self,
            request: models.AcquireDeploymentTokenRequest,
            opts: Dict = None,
    ) -> models.AcquireDeploymentTokenResponse:
        """
        获取 Deployment 访问 Token
        """
        
        kwargs = {}
        kwargs["action"] = "AcquireDeploymentToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcquireDeploymentTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AcquireSandboxInstanceToken(
            self,
            request: models.AcquireSandboxInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.AcquireSandboxInstanceTokenResponse:
        """
        获取访问沙箱工具时所需要使用的访问Token，创建沙箱实例后需调用此接口获取沙箱实例访问Token。
        此Token可用于调用代码沙箱实例执行代码，或浏览器沙箱实例进行浏览器操作等。
        """
        
        kwargs = {}
        kwargs["action"] = "AcquireSandboxInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcquireSandboxInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AppendEvent(
            self,
            request: models.AppendEventRequest,
            opts: Dict = None,
    ) -> models.AppendEventResponse:
        """
        追加事件。

        向指定会话追加一条事件。
        """
        
        kwargs = {}
        kwargs["action"] = "AppendEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AppendEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApproveRegistryRecord(
            self,
            request: models.ApproveRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.ApproveRegistryRecordResponse:
        """
        通过 Version 审批：PENDING_APPROVAL → APPROVED。Comment 必填。
        """
        
        kwargs = {}
        kwargs["action"] = "ApproveRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApproveRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelRegistryRecord(
            self,
            request: models.CancelRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.CancelRegistryRecordResponse:
        """
        PREPARING/PENDING_APPROVAL → CANCELED。Comment 必填。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAPIKey(
            self,
            request: models.CreateAPIKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAPIKeyResponse:
        """
        创建新的API密钥，用于调用Agent Sandbox接口。相较于腾讯云Secret ID Secret Key支持调用所有接口使用，仅有部分接口支持使用API密钥调用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAPIKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAPIKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeployment(
            self,
            request: models.CreateDeploymentRequest,
            opts: Dict = None,
    ) -> models.CreateDeploymentResponse:
        """
        创建 Deployment
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePreCacheImageTask(
            self,
            request: models.CreatePreCacheImageTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePreCacheImageTaskResponse:
        """
        创建镜像预热任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePreCacheImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePreCacheImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRegistry(
            self,
            request: models.CreateRegistryRequest,
            opts: Dict = None,
    ) -> models.CreateRegistryResponse:
        """
        创建 Agent Registry（注册中心）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRegistryRecord(
            self,
            request: models.CreateRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.CreateRegistryRecordResponse:
        """
        统一创建 Registry Record（含 revision 1）。请求通过 DescriptorType 与严格内容输入 Union 选择底层类型：MCPSource / AgentSource / SkillSource / CustomDescriptors 四选一，必须与 DescriptorType 对应。不接受 RecordId 或 ChangeLog；同名 Record 返回冲突，不隐式追加 Version。追加 Version 请使用 UpdateRegistryRecord。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSandboxTool(
            self,
            request: models.CreateSandboxToolRequest,
            opts: Dict = None,
    ) -> models.CreateSandboxToolResponse:
        """
        创建沙箱工具
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSandboxTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSandboxToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSession(
            self,
            request: models.CreateSessionRequest,
            opts: Dict = None,
    ) -> models.CreateSessionResponse:
        """
        创建会话。

        为指定 Agent 和用户创建会话，创建成功后返回会话信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSessionSpace(
            self,
            request: models.CreateSessionSpaceRequest,
            opts: Dict = None,
    ) -> models.CreateSessionSpaceResponse:
        """
        创建会话空间。
        为当前应用在指定地域创建会话空间，创建成功后返回会话空间信息。会话空间用于隔离不同业务场景下的用户、会话、事件及状态数据。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSessionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSessionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAPIKey(
            self,
            request: models.DeleteAPIKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteAPIKeyResponse:
        """
        删除API密钥。注意区别于腾讯云Secret ID Secret Key，本接口删除的是Agent Sandbox专用API key。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAPIKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAPIKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeployment(
            self,
            request: models.DeleteDeploymentRequest,
            opts: Dict = None,
    ) -> models.DeleteDeploymentResponse:
        """
        删除 Deployment
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRegistry(
            self,
            request: models.DeleteRegistryRequest,
            opts: Dict = None,
    ) -> models.DeleteRegistryResponse:
        """
        删除 Registry。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRegistryRecord(
            self,
            request: models.DeleteRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteRegistryRecordResponse:
        """
        删除 Registry Record 或指定 Version。省略 VersionId 时对整个 Record 进行软删除；传入 VersionId 时只删除指定 Version（Stable 指向的 Version 不允许删除；仅剩一个 Approved Version 时不允许删除）。取代原 DeleteRegistryRecordVersion。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSandboxTool(
            self,
            request: models.DeleteSandboxToolRequest,
            opts: Dict = None,
    ) -> models.DeleteSandboxToolResponse:
        """
        删除沙箱工具
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSandboxTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSandboxToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSession(
            self,
            request: models.DeleteSessionRequest,
            opts: Dict = None,
    ) -> models.DeleteSessionResponse:
        """
        删除会话
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSessionSpace(
            self,
            request: models.DeleteSessionSpaceRequest,
            opts: Dict = None,
    ) -> models.DeleteSessionSpaceResponse:
        """
        删除会话空间。
        删除指定的会话空间。仅允许删除不包含会话、事件或用户状态数据的非默认会话空间；系统默认会话空间不能删除。删除成功后不再返回会话空间信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSessionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSessionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIKeyList(
            self,
            request: models.DescribeAPIKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIKeyListResponse:
        """
        获取API密钥列表，包含API密钥简略信息，包含名称、创建时间等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployment(
            self,
            request: models.DescribeDeploymentRequest,
            opts: Dict = None,
    ) -> models.DescribeDeploymentResponse:
        """
        查询 Deployment 信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeploymentList(
            self,
            request: models.DescribeDeploymentListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeploymentListResponse:
        """
        查询 Deployment 列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeploymentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeploymentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvents(
            self,
            request: models.DescribeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeEventsResponse:
        """
        查询事件列表。

        查询指定会话的事件流，支持按作者和起始时间筛选。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreCacheImageTask(
            self,
            request: models.DescribePreCacheImageTaskRequest,
            opts: Dict = None,
    ) -> models.DescribePreCacheImageTaskResponse:
        """
        查询镜像预热任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreCacheImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreCacheImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuotaOverview(
            self,
            request: models.DescribeQuotaOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaOverviewResponse:
        """
        查询当前调用账号的资源配额和当前总用量，以及账号下各配额组的资源配额和当前用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuotaOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistry(
            self,
            request: models.DescribeRegistryRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryResponse:
        """
        按 RegistryId 查询 Registry 详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryAuditLogList(
            self,
            request: models.DescribeRegistryAuditLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryAuditLogListResponse:
        """
        分页查询指定Registry / Record / Version的审计日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryAuditLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryAuditLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryList(
            self,
            request: models.DescribeRegistryListRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryListResponse:
        """
        分页查询当前租户可见的 Registry 列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryRecord(
            self,
            request: models.DescribeRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryRecordResponse:
        """
        查询 Record 详情和其中一个 Version。请求可通过互斥的 VersionId 或 Label 选择 Version；均省略时默认 Label=stable。取代原 DescribeRegistryRecordVersion。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryRecordList(
            self,
            request: models.DescribeRegistryRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryRecordListResponse:
        """
        分页查询 Registry 下的 Record 列表。list 类接口不接入 CAM 转发鉴权；业务侧按 CAM 二次过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryRecordVersionList(
            self,
            request: models.DescribeRegistryRecordVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryRecordVersionListResponse:
        """
        分页查询 Record 的 Version 列表。list 类接口不接入 CAM 转发鉴权。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryRecordVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryRecordVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxInstanceList(
            self,
            request: models.DescribeSandboxInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxInstanceListResponse:
        """
        查询沙箱实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxToolList(
            self,
            request: models.DescribeSandboxToolListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxToolListResponse:
        """
        查询沙箱工具列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxToolList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxToolListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSession(
            self,
            request: models.DescribeSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionResponse:
        """
        查询会话。

        查询指定会话的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionSpace(
            self,
            request: models.DescribeSessionSpaceRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionSpaceResponse:
        """
        查询会话空间详情。
        查询指定会话空间的详细信息，查询成功后返回会话空间的名称、描述、状态、所属地域及创建时间等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionSpaces(
            self,
            request: models.DescribeSessionSpacesRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionSpacesResponse:
        """
        分页查询当前应用和地域下的会话空间。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionSpaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionSpacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessions(
            self,
            request: models.DescribeSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionsResponse:
        """
        查询会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSkillPackageDownloadURL(
            self,
            request: models.GetSkillPackageDownloadURLRequest,
            opts: Dict = None,
    ) -> models.GetSkillPackageDownloadURLResponse:
        """
        获取 Skill 包下载 URL。VersionId 与 Label 互斥；均省略时使用 Stable。响应包含 ResolvedVersionId，便于调用方回填。
        """
        
        kwargs = {}
        kwargs["action"] = "GetSkillPackageDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSkillPackageDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSkillPackageUploadURL(
            self,
            request: models.GetSkillPackageUploadURLRequest,
            opts: Dict = None,
    ) -> models.GetSkillPackageUploadURLResponse:
        """
        为 FAILED / EXPIRED 的 TAR Skill Version 生成新的上传尝试；VersionId 与 Revision 保持不变。
        """
        
        kwargs = {}
        kwargs["action"] = "GetSkillPackageUploadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSkillPackageUploadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeployment(
            self,
            request: models.ModifyDeploymentRequest,
            opts: Dict = None,
    ) -> models.ModifyDeploymentResponse:
        """
        修改 Deployment
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySession(
            self,
            request: models.ModifySessionRequest,
            opts: Dict = None,
    ) -> models.ModifySessionResponse:
        """
        修改会话信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySessionSpace(
            self,
            request: models.ModifySessionSpaceRequest,
            opts: Dict = None,
    ) -> models.ModifySessionSpaceResponse:
        """
        修改会话空间。
        修改指定会话空间的名称和描述，修改成功后返回更新后的会话空间信息。默认会话空间允许修改名称和描述。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySessionSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySessionSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseSandboxInstance(
            self,
            request: models.PauseSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.PauseSandboxInstanceResponse:
        """
        暂停沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "PauseSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PreviewRegistryRecord(
            self,
            request: models.PreviewRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.PreviewRegistryRecordResponse:
        """
        对 Record 的指定 Version 或 Label 目标发起一次预览调用。VersionId 与 Label 互斥；均省略时使用 Stable。不创建 Version、不修改 Label。
        """
        
        kwargs = {}
        kwargs["action"] = "PreviewRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PreviewRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectRegistryRecord(
            self,
            request: models.RejectRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.RejectRegistryRecordResponse:
        """
        驳回 Version 审批：PENDING_APPROVAL → REJECTED。Comment 必填。
        """
        
        kwargs = {}
        kwargs["action"] = "RejectRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSandboxInstance(
            self,
            request: models.ResumeSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeSandboxInstanceResponse:
        """
        恢复沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSandboxInstance(
            self,
            request: models.StartSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.StartSandboxInstanceResponse:
        """
        启动沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "StartSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSandboxInstance(
            self,
            request: models.StopSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.StopSandboxInstanceResponse:
        """
        停止沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncRegistryRecord(
            self,
            request: models.SyncRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.SyncRegistryRecordResponse:
        """
        触发一次从远端拉取描述符 / 元数据的同步。可通过互斥的 VersionId 或 Label 指定来源 Version，均省略时默认使用 Stable。有变化时创建新 Version 并移动 Latest；来源必须 SourceType=URL_IMPORT，否则返回 UnsupportedOperation.SourceType。
        """
        
        kwargs = {}
        kwargs["action"] = "SyncRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRegistry(
            self,
            request: models.UpdateRegistryRequest,
            opts: Dict = None,
    ) -> models.UpdateRegistryResponse:
        """
        更新 Registry 的可变元数据。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRegistryRecord(
            self,
            request: models.UpdateRegistryRecordRequest,
            opts: Dict = None,
    ) -> models.UpdateRegistryRecordResponse:
        """
        更新 Registry Record。两种互斥模式：①Record 更新模式：不提交任何 Source / CustomDescriptors，可通过 Description、LabelMutations 修改元数据与 Label（至少提交一项）；②Version 创建模式：提交且仅提交一种与现有 DescriptorType 匹配的内容输入，可选 VersionName / ChangeLog，禁止 Description / LabelMutations，服务端在 Record 下创建下一个 Revision。取代原 ChangeRegistryRecordStableVersion / RollbackRegistryRecordVersion / Create*RegistryRecordVersion。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRegistryRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRegistryRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSandboxInstance(
            self,
            request: models.UpdateSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateSandboxInstanceResponse:
        """
        更新沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSandboxTool(
            self,
            request: models.UpdateSandboxToolRequest,
            opts: Dict = None,
    ) -> models.UpdateSandboxToolResponse:
        """
        更新沙箱工具
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSandboxTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSandboxToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)