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
from tencentcloud.wedata.v20250806 import models


class WedataClient(AbstractClient):
    _apiVersion = '2025-08-06'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'


    def CreateCodeFile(self, request):
        r"""新建代码文件

        :param request: Request instance for CreateCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodeFolder(self, request):
        r"""新建代码文件夹

        :param request: Request instance for CreateCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataBackfillPlan(self, request):
        r"""创建数据补录计划

        :param request: Request instance for CreateDataBackfillPlan.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateDataBackfillPlanRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateDataBackfillPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataBackfillPlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataBackfillPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOpsAlarmRule(self, request):
        r"""设置告警规则

        :param request: Request instance for CreateOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceFile(self, request):
        r"""创建资源文件

        :param request: Request instance for CreateResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceFolder(self, request):
        r"""创建资源文件文件夹

        :param request: Request instance for CreateResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSQLFolder(self, request):
        r"""创建数据探索脚本文件夹

        :param request: Request instance for CreateSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSQLScript(self, request):
        r"""新增SQL脚本

        :param request: Request instance for CreateSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        r"""创建任务接口

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
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
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowResponse`

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


    def CreateWorkflowFolder(self, request):
        r"""创建文件夹

        :param request: Request instance for CreateWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeFile(self, request):
        r"""删除代码文件

        :param request: Request instance for DeleteCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeFolder(self, request):
        r"""数据探索删除文件夹

        :param request: Request instance for DeleteCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOpsAlarmRule(self, request):
        r"""删除告警规则

        :param request: Request instance for DeleteOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceFile(self, request):
        r"""资源管理-删除资源文件

        :param request: Request instance for DeleteResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceFolder(self, request):
        r"""删除资源文件文件夹

        :param request: Request instance for DeleteResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSQLFolder(self, request):
        r"""删除SQL文件夹

        :param request: Request instance for DeleteSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSQLScript(self, request):
        r"""删除探索脚本

        :param request: Request instance for DeleteSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        r"""删除编排空间任务

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
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
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowResponse`

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


    def DeleteWorkflowFolder(self, request):
        r"""删除数据开发文件夹

        :param request: Request instance for DeleteWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlarmMessage(self, request):
        r"""查询告警信息详情

        :param request: Request instance for GetAlarmMessage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetAlarmMessageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetAlarmMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlarmMessage", params, headers=headers)
            response = json.loads(body)
            model = models.GetAlarmMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCodeFile(self, request):
        r"""查看代码文件详情

        :param request: Request instance for GetCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsAlarmRule(self, request):
        r"""根据告警规则id/名称查询单个告警规则信息

        :param request: Request instance for GetOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsAsyncJob(self, request):
        r"""查询运维中心异步操作详情

        :param request: Request instance for GetOpsAsyncJob.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsAsyncJobRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsAsyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsAsyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsAsyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsTask(self, request):
        r"""获取任务详情

        :param request: Request instance for GetOpsTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsTask", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsTaskCode(self, request):
        r"""获取任务代码

        :param request: Request instance for GetOpsTaskCode.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskCodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsTaskCode", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsTaskCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsWorkflow(self, request):
        r"""根据工作流id，获取工作流调度详情。

        :param request: Request instance for GetOpsWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceFile(self, request):
        r"""获取资源文件详情

        :param request: Request instance for GetResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSQLScript(self, request):
        r"""查询脚本详情

        :param request: Request instance for GetSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.GetSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTask(self, request):
        r"""创建任务接口

        :param request: Request instance for GetTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTask", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskCode(self, request):
        r"""获取任务代码

        :param request: Request instance for GetTaskCode.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskCodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskCode", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskInstance(self, request):
        r"""调度实例详情

        :param request: Request instance for GetTaskInstance.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskInstanceLog(self, request):
        r"""获取实例列表

        :param request: Request instance for GetTaskInstanceLog.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskInstanceLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskInstanceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskVersion(self, request):
        r"""拉取任务版本列表

        :param request: Request instance for GetTaskVersion.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflow(self, request):
        r"""获取工作流信息

        :param request: Request instance for GetWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetWorkflowResponse`

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


    def KillTaskInstancesAsync(self, request):
        r"""实例批量终止操作-异步操作

        :param request: Request instance for KillTaskInstancesAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.KillTaskInstancesAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.KillTaskInstancesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillTaskInstancesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.KillTaskInstancesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAlarmMessages(self, request):
        r"""获取告警信息列表

        :param request: Request instance for ListAlarmMessages.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessagesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAlarmMessages", params, headers=headers)
            response = json.loads(body)
            model = models.ListAlarmMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCodeFolderContents(self, request):
        r"""获取文件夹内容

        :param request: Request instance for ListCodeFolderContents.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListCodeFolderContentsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListCodeFolderContentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCodeFolderContents", params, headers=headers)
            response = json.loads(body)
            model = models.ListCodeFolderContentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDataBackfillInstances(self, request):
        r"""获取单次补录的所有实例详情

        :param request: Request instance for ListDataBackfillInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDataBackfillInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDataBackfillInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDataBackfillInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListDataBackfillInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamOpsTasks(self, request):
        r"""获取任务直接下游详情

        :param request: Request instance for ListDownstreamOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamTaskInstances(self, request):
        r"""获取实例直接上游

        :param request: Request instance for ListDownstreamTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamTasks(self, request):
        r"""获取任务直接下游详情

        :param request: Request instance for ListDownstreamTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsAlarmRules(self, request):
        r"""查询告警规则列表

        :param request: Request instance for ListOpsAlarmRules.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsAlarmRulesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsAlarmRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsAlarmRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsAlarmRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsTasks(self, request):
        r"""根据项目id获取任务列表

        :param request: Request instance for ListOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsWorkflows(self, request):
        r"""根据项目ID获取项目下工作流

        :param request: Request instance for ListOpsWorkflows.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceFiles(self, request):
        r"""获取资源文件列表

        :param request: Request instance for ListResourceFiles.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListResourceFilesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListResourceFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceFolders(self, request):
        r"""查询资源文件文件夹列表

        :param request: Request instance for ListResourceFolders.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListResourceFoldersRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListResourceFoldersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceFolders", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceFoldersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSQLFolderContents(self, request):
        r"""查询数据探索文件夹树，包括文件夹下的脚本

        :param request: Request instance for ListSQLFolderContents.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListSQLFolderContentsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListSQLFolderContentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSQLFolderContents", params, headers=headers)
            response = json.loads(body)
            model = models.ListSQLFolderContentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSQLScriptRuns(self, request):
        r"""查询SQL运行记录

        :param request: Request instance for ListSQLScriptRuns.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListSQLScriptRunsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListSQLScriptRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSQLScriptRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListSQLScriptRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskInstanceExecutions(self, request):
        r"""调度实例详情

        :param request: Request instance for ListTaskInstanceExecutions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstanceExecutionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstanceExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskInstanceExecutions", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskInstanceExecutionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskInstances(self, request):
        r"""获取实例列表

        :param request: Request instance for ListTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskVersions(self, request):
        r"""任务保存版本列表

        :param request: Request instance for ListTaskVersions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskVersions", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTasks(self, request):
        r"""查询任务分页信息

        :param request: Request instance for ListTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamOpsTasks(self, request):
        r"""获取任务直接上游

        :param request: Request instance for ListUpstreamOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamTaskInstances(self, request):
        r"""获取实例直接上游

        :param request: Request instance for ListUpstreamTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamTasks(self, request):
        r"""获取任务直接上游

        :param request: Request instance for ListUpstreamTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowFolders(self, request):
        r"""查询文件夹列表

        :param request: Request instance for ListWorkflowFolders.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowFoldersRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowFoldersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowFolders", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowFoldersResponse()
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
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowsResponse`

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


    def PauseOpsTasksAsync(self, request):
        r"""异步批量暂停任务

        :param request: Request instance for PauseOpsTasksAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.PauseOpsTasksAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.PauseOpsTasksAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseOpsTasksAsync", params, headers=headers)
            response = json.loads(body)
            model = models.PauseOpsTasksAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunTaskInstancesAsync(self, request):
        r"""实例批量重跑-异步

        :param request: Request instance for RerunTaskInstancesAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RerunTaskInstancesAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RerunTaskInstancesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunTaskInstancesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.RerunTaskInstancesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunSQLScript(self, request):
        r"""运行SQL脚本

        :param request: Request instance for RunSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RunSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RunSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.RunSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetSuccessTaskInstancesAsync(self, request):
        r"""实例批量置成功-异步

        :param request: Request instance for SetSuccessTaskInstancesAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.SetSuccessTaskInstancesAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SetSuccessTaskInstancesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetSuccessTaskInstancesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.SetSuccessTaskInstancesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopOpsTasksAsync(self, request):
        r"""异步批量下线任务

        :param request: Request instance for StopOpsTasksAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.StopOpsTasksAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.StopOpsTasksAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopOpsTasksAsync", params, headers=headers)
            response = json.loads(body)
            model = models.StopOpsTasksAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSQLScriptRun(self, request):
        r"""停止运行SQL脚本

        :param request: Request instance for StopSQLScriptRun.
        :type request: :class:`tencentcloud.wedata.v20250806.models.StopSQLScriptRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.StopSQLScriptRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSQLScriptRun", params, headers=headers)
            response = json.loads(body)
            model = models.StopSQLScriptRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTask(self, request):
        r"""提交任务。

        :param request: Request instance for SubmitTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCodeFile(self, request):
        r"""更新代码文件

        :param request: Request instance for UpdateCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCodeFolder(self, request):
        r"""重命名代码文件夹

        :param request: Request instance for UpdateCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOpsAlarmRule(self, request):
        r"""修改告警规则

        :param request: Request instance for UpdateOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOpsTasksOwner(self, request):
        r"""修改任务负责人

        :param request: Request instance for UpdateOpsTasksOwner.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsTasksOwnerRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsTasksOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOpsTasksOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOpsTasksOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceFile(self, request):
        r"""更新资源文件

        :param request: Request instance for UpdateResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceFolder(self, request):
        r"""创建资源文件文件夹

        :param request: Request instance for UpdateResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSQLFolder(self, request):
        r"""重命名SQL文件夹

        :param request: Request instance for UpdateSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSQLScript(self, request):
        r"""保存探索脚本内容

        :param request: Request instance for UpdateSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTask(self, request):
        r"""创建任务接口

        :param request: Request instance for UpdateTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTask", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflow(self, request):
        r"""更新工作流（包括工作流基本信息与工作流参数）

        :param request: Request instance for UpdateWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowResponse`

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


    def UpdateWorkflowFolder(self, request):
        r"""创建文件夹

        :param request: Request instance for UpdateWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))