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
from tencentcloud.databuddy.v20260715 import models
from typing import Dict


class DatabuddyClient(AbstractClient):
    _apiVersion = '2026-07-15'
    _endpoint = 'databuddy.tencentcloudapi.com'
    _service = 'databuddy'

    async def AddConsoleUsers(
            self,
            request: models.AddConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.AddConsoleUsersResponse:
        """
        添加控制台用户
        """
        
        kwargs = {}
        kwargs["action"] = "AddConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCatalog(
            self,
            request: models.CreateCatalogRequest,
            opts: Dict = None,
    ) -> models.CreateCatalogResponse:
        """
        创建数据目录接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsoleGroup(
            self,
            request: models.CreateConsoleGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsoleGroupResponse:
        """
        创建控制台用户组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsoleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsoleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFile(
            self,
            request: models.CreateFileRequest,
            opts: Dict = None,
    ) -> models.CreateFileResponse:
        """
        在Studio（统一开发 IDE）的工作空间文件树中新建一个文件（Notebook/SQL/Python等），创建成功后返回文件的完整元信息。

        **前置条件**
        1. WorkspaceId 对应工作空间存在，且调用方为该工作空间成员；
        2. ParentFolderPath 对应的父文件夹必须存在，且调用方对其有写权限（根目录传 `/`）；
        3. FileName 在同一父文件夹下不能重名（含后缀比较）；
        4. FileName 后缀必须与 FileType 匹配（`.ipynb`↔`NOTEBOOK_FILE`、`.sql`↔`SQL_FILE`）；
        5. 需带文件内容创建时通过 Storage 传入（大文件走 COS 中转，小文件放 Storage.Content）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFolder(
            self,
            request: models.CreateFolderRequest,
            opts: Dict = None,
    ) -> models.CreateFolderResponse:
        """
        创建文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchema(
            self,
            request: models.CreateSchemaRequest,
            opts: Dict = None,
    ) -> models.CreateSchemaResponse:
        """
        创建schema
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflow(
            self,
            request: models.CreateWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowResponse:
        """
        创建工作流
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspace(
            self,
            request: models.CreateWorkspaceRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceResponse:
        """
        创建工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspaceRole(
            self,
            request: models.CreateWorkspaceRoleRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceRoleResponse:
        """
        创建工作空间角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspaceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCatalog(
            self,
            request: models.DeleteCatalogRequest,
            opts: Dict = None,
    ) -> models.DeleteCatalogResponse:
        """
        删除catalog
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsoleGroups(
            self,
            request: models.DeleteConsoleGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteConsoleGroupsResponse:
        """
        删除控制台用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsoleGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsoleGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFile(
            self,
            request: models.DeleteFileRequest,
            opts: Dict = None,
    ) -> models.DeleteFileResponse:
        """
        将文件移入回收站（软删除），同时清理该文件的版本记录与执行结果快照。

        **前置条件**
        1. FileId 对应文件必须存在且为活跃状态；
        2. 调用方对该文件有删除权限；
        3. 文件未被工作流任务引用。

        **错误码（Module 均为 `Studio`）**

        | 错误码（Code） | InnerCode | 描述 | 处理建议 |
        | --- | --- | --- | --- |
        | `MissingParameter.WorkspaceId` | 1030001 | 缺少 WorkspaceId | 请传入 WorkspaceId |
        | `MissingParameter.FileId` | 1030003 | 缺少 FileId | 请传入 FileId  |
        | `InvalidParameterValue.FileType` | 1030102 | FileType 取值不支持 | FileType 取 FILE/NOTEBOOK_FILE/SQL_FILE |
        | `ResourceNotFound.FileNotFound` | 1030203 | 文件不存在或已删除 | 请确认 FileId |
        | `ResourceInUse.FileReferencedByTask` | 1030204 | 文件被工作流任务引用，不允许删除 | 请先解除任务引用后再删除 |
        | `UnauthorizedOperation.FileDeleteDenied` | 1030303 | 对该文件无删除权限 | 请联系文件负责人或空间管理员授权 |
        | `InternalError` | 1030900 | 服务内部异常 | 请携带 RequestId 联系支持 |
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFolder(
            self,
            request: models.DeleteFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteFolderResponse:
        """
        删除文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSchema(
            self,
            request: models.DeleteSchemaRequest,
            opts: Dict = None,
    ) -> models.DeleteSchemaResponse:
        """
        删除schema
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflow(
            self,
            request: models.DeleteWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowResponse:
        """
        删除工作流
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkspace(
            self,
            request: models.DeleteWorkspaceRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkspaceResponse:
        """
        删除工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkspaceRole(
            self,
            request: models.DeleteWorkspaceRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkspaceRoleResponse:
        """
        删除工作空间角色
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkspaceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkspaceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFile(
            self,
            request: models.GetFileRequest,
            opts: Dict = None,
    ) -> models.GetFileResponse:
        """
        获取文件的元信息，可选包含文件内容，支持按版本读取历史快照。

        **前置条件**
        1. FileId 与 FilePath 二选一，至少传一个；同时传时以 FileId 为准；
        2. 对应文件必须存在，且调用方对该文件有读权限；
        3. 传 VersionId 时该版本必须存在。

        **错误码（Module 均为 `Studio`）**

        | 错误码（Code） | InnerCode | 描述 | 处理建议 |
        | --- | --- | --- | --- |
        | `MissingParameter.WorkspaceId` | 1030001 | 缺少 WorkspaceId | 请传入 WorkspaceId |
        | `MissingParameter.FileId` | 1030003 | FileId 与 FilePath 同时为空 | FileId 与 FilePath 二选一，至少传一个 |
        | `InvalidParameterValue.FileType` | 1030102 | FileType 取值不支持 | FileType 取 FILE/NOTEBOOK_FILE/SQL_FILE |
        | `ResourceNotFound.FileNotFound` | 1030203 | 文件不存在或已删除 | 请确认 FileId 或 FilePath |
        | `ResourceNotFound.FileVersionNotFound` | 1030205 | 指定的文件版本不存在 | 请确认 VersionId，或调用 ListFileVersions 获取 |
        | `UnauthorizedOperation.FileReadDenied` | 1030304 | 对该文件无读权限 | 请联系文件负责人或空间管理员授权 |
        | `InternalError` | 1030900 | 服务内部异常 | 请携带 RequestId 联系支持 |
        """
        
        kwargs = {}
        kwargs["action"] = "GetFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFolder(
            self,
            request: models.GetFolderRequest,
            opts: Dict = None,
    ) -> models.GetFolderResponse:
        """
        获取文件夹详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflow(
            self,
            request: models.GetWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowResponse:
        """
        获取工作流详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflowRun(
            self,
            request: models.GetWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowRunResponse:
        """
        查询工作流运行详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflowTaskRun(
            self,
            request: models.GetWorkflowTaskRunRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowTaskRunResponse:
        """
        查询任务运行详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflowTaskRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowTaskRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkspace(
            self,
            request: models.GetWorkspaceRequest,
            opts: Dict = None,
    ) -> models.GetWorkspaceResponse:
        """
        查询工作空间详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillWorkflowRun(
            self,
            request: models.KillWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.KillWorkflowRunResponse:
        """
        终止工作流的运行
        """
        
        kwargs = {}
        kwargs["action"] = "KillWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleGroupUsers(
            self,
            request: models.ListConsoleGroupUsersRequest,
            opts: Dict = None,
    ) -> models.ListConsoleGroupUsersResponse:
        """
        查询控制台用户组成员列表，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleGroupUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleGroupUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleGroups(
            self,
            request: models.ListConsoleGroupsRequest,
            opts: Dict = None,
    ) -> models.ListConsoleGroupsResponse:
        """
        查询控制台用户组列表，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleRoles(
            self,
            request: models.ListConsoleRolesRequest,
            opts: Dict = None,
    ) -> models.ListConsoleRolesResponse:
        """
        查询控制台角色列表，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleUsers(
            self,
            request: models.ListConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.ListConsoleUsersResponse:
        """
        查询控制台用户列表，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFiles(
            self,
            request: models.ListFilesRequest,
            opts: Dict = None,
    ) -> models.ListFilesResponse:
        """
        获取文件夹和文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSchemas(
            self,
            request: models.ListSchemasRequest,
            opts: Dict = None,
    ) -> models.ListSchemasResponse:
        """
        获取schema列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSchemas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSchemasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowRuns(
            self,
            request: models.ListWorkflowRunsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowRunsResponse:
        """
        工作流运行列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowTaskRuns(
            self,
            request: models.ListWorkflowTaskRunsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowTaskRunsResponse:
        """
        查询工作流任务历史运行列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowTaskRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowTaskRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflows(
            self,
            request: models.ListWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowsResponse:
        """
        查询工作流列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaces(
            self,
            request: models.ListWorkspacesRequest,
            opts: Dict = None,
    ) -> models.ListWorkspacesResponse:
        """
        查询工作空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveConsoleUsers(
            self,
            request: models.RemoveConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.RemoveConsoleUsersResponse:
        """
        <p>批量移除控制台用户（单次最多10个；前置校验任一不满足整体拒绝；执行阶段单个失败不中断后续删除，成败以 SuccessUins/FailItems 为准）</p>
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RerunWorkflowRun(
            self,
            request: models.RerunWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.RerunWorkflowRunResponse:
        """
        重跑工作流
        """
        
        kwargs = {}
        kwargs["action"] = "RerunWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RerunWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunWorkflow(
            self,
            request: models.RunWorkflowRequest,
            opts: Dict = None,
    ) -> models.RunWorkflowResponse:
        """
        运行工作流
        """
        
        kwargs = {}
        kwargs["action"] = "RunWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCompute(
            self,
            request: models.StartComputeRequest,
            opts: Dict = None,
    ) -> models.StartComputeResponse:
        """
        启动计算资源
        """
        
        kwargs = {}
        kwargs["action"] = "StartCompute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartComputeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCompute(
            self,
            request: models.StopComputeRequest,
            opts: Dict = None,
    ) -> models.StopComputeResponse:
        """
        停止计算资源
        """
        
        kwargs = {}
        kwargs["action"] = "StopCompute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopComputeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindWorkflowBundle(
            self,
            request: models.UnbindWorkflowBundleRequest,
            opts: Dict = None,
    ) -> models.UnbindWorkflowBundleResponse:
        """
        解绑工作流Bundle信息
        说明：本接口语义等同于规范动词清单中的 Detach，因兼容既有产品形态保留 Unbind 命名
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindWorkflowBundle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindWorkflowBundleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConsoleGroup(
            self,
            request: models.UpdateConsoleGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateConsoleGroupResponse:
        """
        修改控制台用户组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConsoleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConsoleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConsoleUsers(
            self,
            request: models.UpdateConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.UpdateConsoleUsersResponse:
        """
        修改控制台用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFile(
            self,
            request: models.UpdateFileRequest,
            opts: Dict = None,
    ) -> models.UpdateFileResponse:
        """
        更新文件内容与运行配置（计算资源、默认 catalog/schema、参数等），返回更新后的文件元信息。

        **前置条件**
        1. FileId 对应文件必须存在且为活跃状态；
        2. 调用方对该文件有写权限；
        3. 仅更新配置时不传 Storage；仅更新内容时不传 FileConfig；
        4. FileConfig.ResourceId 非空时会校验资源类型与文件类型的匹配性。

        **错误码（Module 均为 `Studio`）**

        | 错误码（Code） | InnerCode | 描述 | 处理建议 |
        | --- | --- | --- | --- |
        | `MissingParameter.WorkspaceId` | 1030001 | 缺少 WorkspaceId | 请传入 WorkspaceId |
        | `MissingParameter.FileId` | 1030003 | 缺少 FileId | 请传入 FileId |
        | `InvalidParameterValue.FileType` | 1030102 | FileType 取值不支持 | FileType 取 FILE/NOTEBOOK_FILE/SQL_FILE |
        | `InvalidParameterValue.ResourceId` | 1030104 | 计算资源类型与文件类型不匹配 | Python/Notebook 选数据计算资源，SQL 选数据分析资源 |
        | `ResourceNotFound.FileNotFound` | 1030203 | 文件不存在或已删除 | 请确认 FileId，或调用 GetFile 校验文件状态 |
        | `UnauthorizedOperation.FileWriteDenied` | 1030302 | 对该文件无写权限 | 请联系文件负责人或空间管理员授权 |
        | `FailedOperation.FileStorageUpdateFailed` | 1030401 | 文件内容写入存储失败 | 请稍后重试，持续失败请携带 RequestId 联系支持 |
        | `InternalError` | 1030900 | 服务内部异常 | 请携带 RequestId 联系支持 |
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFolder(
            self,
            request: models.UpdateFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateFolderResponse:
        """
        更新文件夹（支持重命名+移动）
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflow(
            self,
            request: models.UpdateWorkflowRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowResponse:
        """
        更新工作流
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkspace(
            self,
            request: models.UpdateWorkspaceRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceResponse:
        """
        修改工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkspaceRole(
            self,
            request: models.UpdateWorkspaceRoleRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceRoleResponse:
        """
        更新工作空间角色
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspaceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)