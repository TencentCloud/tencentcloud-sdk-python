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
        添加控制台用户，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
        """
        
        kwargs = {}
        kwargs["action"] = "AddConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddWorkspaceGroups(
            self,
            request: models.AddWorkspaceGroupsRequest,
            opts: Dict = None,
    ) -> models.AddWorkspaceGroupsResponse:
        """
        添加工作空间用户组
        """
        
        kwargs = {}
        kwargs["action"] = "AddWorkspaceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddWorkspaceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddWorkspaceUsers(
            self,
            request: models.AddWorkspaceUsersRequest,
            opts: Dict = None,
    ) -> models.AddWorkspaceUsersResponse:
        """
        创建用户组
        """
        
        kwargs = {}
        kwargs["action"] = "AddWorkspaceUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddWorkspaceUsersResponse
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
        创建控制台用户组，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
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
        
    async def CreateLocation(
            self,
            request: models.CreateLocationRequest,
            opts: Dict = None,
    ) -> models.CreateLocationResponse:
        """
        创建存储位置
        使用场景：在数据湖仓库中创建新的存储位置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModel(
            self,
            request: models.CreateModelRequest,
            opts: Dict = None,
    ) -> models.CreateModelResponse:
        """
        创建模型接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModelVersion(
            self,
            request: models.CreateModelVersionRequest,
            opts: Dict = None,
    ) -> models.CreateModelVersionResponse:
        """
        创建模型版本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelVersionResponse
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
        
    async def CreateVolume(
            self,
            request: models.CreateVolumeRequest,
            opts: Dict = None,
    ) -> models.CreateVolumeResponse:
        """
        创建数据卷接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVolumeResponse
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
        创建工作空间，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
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
        删除控制台用户组，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
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
        
    async def DeleteLocation(
            self,
            request: models.DeleteLocationRequest,
            opts: Dict = None,
    ) -> models.DeleteLocationResponse:
        """
        删除存储位置
        使用场景：删除指定的存储位置
        前置条件：存储位置名称必须存在
        错误码：MetaLakeNotFound - 存储位置不存在
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModel(
            self,
            request: models.DeleteModelRequest,
            opts: Dict = None,
    ) -> models.DeleteModelResponse:
        """
        删除模型
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelResponse
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
        
    async def DeleteTable(
            self,
            request: models.DeleteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteTableResponse:
        """
        删除table
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteView(
            self,
            request: models.DeleteViewRequest,
            opts: Dict = None,
    ) -> models.DeleteViewResponse:
        """
        删除view
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVolume(
            self,
            request: models.DeleteVolumeRequest,
            opts: Dict = None,
    ) -> models.DeleteVolumeResponse:
        """
        删除数据卷
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVolumeResponse
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
        
    async def GetCatalog(
            self,
            request: models.GetCatalogRequest,
            opts: Dict = None,
    ) -> models.GetCatalogResponse:
        """
        查询catalog详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCatalogResponse
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
        
    async def GetLocation(
            self,
            request: models.GetLocationRequest,
            opts: Dict = None,
    ) -> models.GetLocationResponse:
        """
        查询存储位置详情
        使用场景：根据存储位置名获取单个存储位置的详细信息
        前置条件：存储位置名称必须存在
        错误码：MetaLakeNotFound - 存储位置不存在
        """
        
        kwargs = {}
        kwargs["action"] = "GetLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetModel(
            self,
            request: models.GetModelRequest,
            opts: Dict = None,
    ) -> models.GetModelResponse:
        """
        获取模型详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetModelVersion(
            self,
            request: models.GetModelVersionRequest,
            opts: Dict = None,
    ) -> models.GetModelVersionResponse:
        """
        获取模型版本详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetModelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSchema(
            self,
            request: models.GetSchemaRequest,
            opts: Dict = None,
    ) -> models.GetSchemaResponse:
        """
        查询schema详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTable(
            self,
            request: models.GetTableRequest,
            opts: Dict = None,
    ) -> models.GetTableResponse:
        """
        查询table详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTables(
            self,
            request: models.GetTablesRequest,
            opts: Dict = None,
    ) -> models.GetTablesResponse:
        """
        批量获取表的元数据。使用场景：根据表的全名列表（catalogName.schemaName.tableName）批量获取表的详细元数据信息。前置条件：需要有对应workspace的读权限，仅返回当前workspace有权限的catalog下的表。权限校验：通过getAuthedCatalogNames获取有权限的catalogName进行过滤，不在权限范围内的表会被静默跳过。限制：FullNames最大支持20个表全名
        """
        
        kwargs = {}
        kwargs["action"] = "GetTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetView(
            self,
            request: models.GetViewRequest,
            opts: Dict = None,
    ) -> models.GetViewResponse:
        """
        查询view详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVolume(
            self,
            request: models.GetVolumeRequest,
            opts: Dict = None,
    ) -> models.GetVolumeResponse:
        """
        获取模型详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVolumeResponse
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
        
    async def ListCatalogNames(
            self,
            request: models.ListCatalogNamesRequest,
            opts: Dict = None,
    ) -> models.ListCatalogNamesResponse:
        """
        分页查询数据目录名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListCatalogNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCatalogNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCatalogs(
            self,
            request: models.ListCatalogsRequest,
            opts: Dict = None,
    ) -> models.ListCatalogsResponse:
        """
        分页获取数据目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListCatalogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCatalogsResponse
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
        
    async def ListFeatureTables(
            self,
            request: models.ListFeatureTablesRequest,
            opts: Dict = None,
    ) -> models.ListFeatureTablesResponse:
        """
        查询特征表列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListFeatureTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFeatureTablesResponse
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
        
    async def ListLocations(
            self,
            request: models.ListLocationsRequest,
            opts: Dict = None,
    ) -> models.ListLocationsResponse:
        """
        分页查询存储位置列表
        使用场景：分页查询数据湖仓库中的存储位置详情列表，支持模式匹配和快照分页
        """
        
        kwargs = {}
        kwargs["action"] = "ListLocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListModels(
            self,
            request: models.ListModelsRequest,
            opts: Dict = None,
    ) -> models.ListModelsResponse:
        """
        分页获取模型信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListModels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListModelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSchemaNames(
            self,
            request: models.ListSchemaNamesRequest,
            opts: Dict = None,
    ) -> models.ListSchemaNamesResponse:
        """
        分页查询数据库名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSchemaNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSchemaNamesResponse
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
        
    async def ListTableNames(
            self,
            request: models.ListTableNamesRequest,
            opts: Dict = None,
    ) -> models.ListTableNamesResponse:
        """
        分页查询数据表名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTableNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTableNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTables(
            self,
            request: models.ListTablesRequest,
            opts: Dict = None,
    ) -> models.ListTablesResponse:
        """
        获取table列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListViewNames(
            self,
            request: models.ListViewNamesRequest,
            opts: Dict = None,
    ) -> models.ListViewNamesResponse:
        """
        分页查询视图名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListViewNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListViewNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListViews(
            self,
            request: models.ListViewsRequest,
            opts: Dict = None,
    ) -> models.ListViewsResponse:
        """
        获取view列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVolumes(
            self,
            request: models.ListVolumesRequest,
            opts: Dict = None,
    ) -> models.ListVolumesResponse:
        """
        分页获取数据卷信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListVolumes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVolumesResponse
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
        
    async def ListWorkspaceGroupUsers(
            self,
            request: models.ListWorkspaceGroupUsersRequest,
            opts: Dict = None,
    ) -> models.ListWorkspaceGroupUsersResponse:
        """
        查询工作空间用户组用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaceGroupUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspaceGroupUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaceGroups(
            self,
            request: models.ListWorkspaceGroupsRequest,
            opts: Dict = None,
    ) -> models.ListWorkspaceGroupsResponse:
        """
        查询工作空间用户组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspaceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaceUsers(
            self,
            request: models.ListWorkspaceUsersRequest,
            opts: Dict = None,
    ) -> models.ListWorkspaceUsersResponse:
        """
        查询工作空间用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaceUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspaceUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaces(
            self,
            request: models.ListWorkspacesRequest,
            opts: Dict = None,
    ) -> models.ListWorkspacesResponse:
        """
        查询工作空间列表，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
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
        <p>批量移除控制台用户（单次最多10个；前置校验任一不满足整体拒绝；执行阶段单个失败不中断后续删除，成败以 SuccessUins/FailItems 为准），该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWorkspaceGroups(
            self,
            request: models.RemoveWorkspaceGroupsRequest,
            opts: Dict = None,
    ) -> models.RemoveWorkspaceGroupsResponse:
        """
        移除工作空间用户组
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWorkspaceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWorkspaceGroupsResponse
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
        
    async def SearchAsset(
            self,
            request: models.SearchAssetRequest,
            opts: Dict = None,
    ) -> models.SearchAssetResponse:
        """
        资产统一搜索
        """
        
        kwargs = {}
        kwargs["action"] = "SearchAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchAssetResponse
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
        
    async def UpdateCatalog(
            self,
            request: models.UpdateCatalogRequest,
            opts: Dict = None,
    ) -> models.UpdateCatalogResponse:
        """
        修改数据目录信息
        使用场景：修改数据目录的注释，按需传入NewComment字段
        前置条件：数据目录必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConsoleGroup(
            self,
            request: models.UpdateConsoleGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateConsoleGroupResponse:
        """
        修改控制台用户组，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
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
        修改控制台用户角色，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
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
        
    async def UpdateFunction(
            self,
            request: models.UpdateFunctionRequest,
            opts: Dict = None,
    ) -> models.UpdateFunctionResponse:
        """
        修改函数信息
        使用场景：修改函数的注释，按需传入NewComment字段
        前置条件：函数必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateLocation(
            self,
            request: models.UpdateLocationRequest,
            opts: Dict = None,
    ) -> models.UpdateLocationResponse:
        """
        修改存储位置
        使用场景：修改存储位置的名称、描述或属性信息
        前置条件：存储位置名称必须存在
        错误码：MetaLakeNotFound - 存储位置不存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateModel(
            self,
            request: models.UpdateModelRequest,
            opts: Dict = None,
    ) -> models.UpdateModelResponse:
        """
        修改模型信息
        使用场景：修改模型的名称或注释，按需传入NewName/NewComment字段
        前置条件：模型必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateModelVersion(
            self,
            request: models.UpdateModelVersionRequest,
            opts: Dict = None,
    ) -> models.UpdateModelVersionResponse:
        """
        修改模型版本信息
        使用场景：修改模型版本的别名或注释，按需传入对应字段
        前置条件：模型版本必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateModelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSchema(
            self,
            request: models.UpdateSchemaRequest,
            opts: Dict = None,
    ) -> models.UpdateSchemaResponse:
        """
        修改schema信息
        使用场景：修改schema的注释，按需传入NewComment字段
        前置条件：schema必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTable(
            self,
            request: models.UpdateTableRequest,
            opts: Dict = None,
    ) -> models.UpdateTableResponse:
        """
        修改表信息
        使用场景：修改表的名称或注释，按需传入NewName/NewComment字段
        前置条件：表必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTableColumn(
            self,
            request: models.UpdateTableColumnRequest,
            opts: Dict = None,
    ) -> models.UpdateTableColumnResponse:
        """
        修改表字段描述
        使用场景：修改表中一个或多个字段的注释
        前置条件：用户需对目标表有写权限；字段名必须存在于目标表中
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTableColumn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTableColumnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateView(
            self,
            request: models.UpdateViewRequest,
            opts: Dict = None,
    ) -> models.UpdateViewResponse:
        """
        修改视图信息
        使用场景：修改视图的名称或注释，按需传入NewName/NewComment字段
        前置条件：视图必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateVolume(
            self,
            request: models.UpdateVolumeRequest,
            opts: Dict = None,
    ) -> models.UpdateVolumeResponse:
        """
        修改数据卷信息
        使用场景：修改数据卷的名称或注释，按需传入NewName/NewComment字段
        前置条件：数据卷必须存在
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateVolumeResponse
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
        修改工作空间，该接口为控制台级接口，仅支持在中心地域调用：国内站请传入 ap-guangzhou，国际站请传入 ap-singapore；其他地域调用将返回 UnsupportedRegion。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkspaceGroupsRoles(
            self,
            request: models.UpdateWorkspaceGroupsRolesRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceGroupsRolesResponse:
        """
        更新工作空间用户组角色
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspaceGroupsRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceGroupsRolesResponse
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
        
    async def UpdateWorkspaceUsersRoles(
            self,
            request: models.UpdateWorkspaceUsersRolesRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceUsersRolesResponse:
        """
        修改工作空间用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspaceUsersRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceUsersRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)