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
from tencentcloud.databuddy.v20260715 import models


class DatabuddyClient(AbstractClient):
    _apiVersion = '2026-07-15'
    _endpoint = 'databuddy.tencentcloudapi.com'
    _service = 'databuddy'


    def AddConsoleUsers(self, request):
        r"""添加控制台用户

        :param request: Request instance for AddConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.AddConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AddConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.AddConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFile(self, request):
        r"""在Studio（统一开发 IDE）的工作空间文件树中新建一个文件（Notebook/SQL/Python等），创建成功后返回文件的完整元信息。

        **前置条件**
        1. WorkspaceId 对应工作空间存在，且调用方为该工作空间成员；
        2. ParentFolderPath 对应的父文件夹必须存在，且调用方对其有写权限（根目录传 `/`）；
        3. FileName 在同一父文件夹下不能重名（含后缀比较）；
        4. FileName 后缀必须与 FileType 匹配（`.ipynb`↔`NOTEBOOK_FILE`、`.sql`↔`SQL_FILE`）；
        5. 需带文件内容创建时通过 Storage 传入（大文件走 COS 中转，小文件放 Storage.Content）。

        :param request: Request instance for CreateFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflow(self, request):
        r"""创建工作流

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFile(self, request):
        r"""将文件移入回收站（软删除），同时清理该文件的版本记录与执行结果快照。

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

        :param request: Request instance for DeleteFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflow(self, request):
        r"""删除工作流

        :param request: Request instance for DeleteWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFile(self, request):
        r"""获取文件的元信息，可选包含文件内容，支持按版本读取历史快照。

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

        :param request: Request instance for GetFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflow(self, request):
        r"""获取工作流详细信息

        :param request: Request instance for GetWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflowRun(self, request):
        r"""查询工作流运行详情

        :param request: Request instance for GetWorkflowRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflowTaskRun(self, request):
        r"""查询任务运行详情

        :param request: Request instance for GetWorkflowTaskRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowTaskRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowTaskRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflowTaskRun", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowTaskRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillWorkflowRun(self, request):
        r"""终止工作流的运行

        :param request: Request instance for KillWorkflowRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.KillWorkflowRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.KillWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.KillWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConsoleUsers(self, request):
        r"""查询控制台用户列表

        :param request: Request instance for ListConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ListConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowRuns(self, request):
        r"""工作流运行列表

        :param request: Request instance for ListWorkflowRuns.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowRunsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowTaskRuns(self, request):
        r"""查询工作流任务历史运行列表

        :param request: Request instance for ListWorkflowTaskRuns.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowTaskRunsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowTaskRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowTaskRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowTaskRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflows(self, request):
        r"""查询工作流列表

        :param request: Request instance for ListWorkflows.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveConsoleUsers(self, request):
        r"""<p>批量移除控制台用户（单次最多10个；前置校验任一不满足整体拒绝；执行阶段单个失败不中断后续删除，成败以 SuccessUins/FailItems 为准）</p>

        :param request: Request instance for RemoveConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RemoveConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RemoveConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunWorkflowRun(self, request):
        r"""重跑工作流

        :param request: Request instance for RerunWorkflowRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RerunWorkflowRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RerunWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.RerunWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunWorkflow(self, request):
        r"""运行工作流

        :param request: Request instance for RunWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RunWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RunWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.RunWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindWorkflowBundle(self, request):
        r"""解绑工作流Bundle信息
        说明：本接口语义等同于规范动词清单中的 Detach，因兼容既有产品形态保留 Unbind 命名

        :param request: Request instance for UnbindWorkflowBundle.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UnbindWorkflowBundleRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UnbindWorkflowBundleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindWorkflowBundle", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindWorkflowBundleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConsoleUsers(self, request):
        r"""修改控制台用户角色

        :param request: Request instance for UpdateConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFile(self, request):
        r"""更新文件内容与运行配置（计算资源、默认 catalog/schema、参数等），返回更新后的文件元信息。

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

        :param request: Request instance for UpdateFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflow(self, request):
        r"""更新工作流

        :param request: Request instance for UpdateWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))