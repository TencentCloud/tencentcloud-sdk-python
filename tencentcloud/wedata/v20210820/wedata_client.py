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
from tencentcloud.wedata.v20210820 import models


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'


    def AddProjectUserRole(self, request):
        r"""添加项目用户角色

        :param request: Request instance for AddProjectUserRole.
        :type request: :class:`tencentcloud.wedata.v20210820.models.AddProjectUserRoleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.AddProjectUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddProjectUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.AddProjectUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateIntegrationTaskAlarms(self, request):
        r"""批量创建任务告警规则

        :param request: Request instance for BatchCreateIntegrationTaskAlarms.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchCreateIntegrationTaskAlarmsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchCreateIntegrationTaskAlarmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateIntegrationTaskAlarms", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateIntegrationTaskAlarmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateTaskVersionAsync(self, request):
        r"""异步批量创建任务版本

        :param request: Request instance for BatchCreateTaskVersionAsync.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchCreateTaskVersionAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchCreateTaskVersionAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateTaskVersionAsync", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateTaskVersionAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteIntegrationTasks(self, request):
        r"""批量删除集成任务

        :param request: Request instance for BatchDeleteIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteOpsTasks(self, request):
        r"""任务运维-批量删除任务

        :param request: Request instance for BatchDeleteOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchForceSuccessIntegrationTaskInstances(self, request):
        r"""批量置成功集成任务实例

        :param request: Request instance for BatchForceSuccessIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchForceSuccessIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchForceSuccessIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchForceSuccessIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchForceSuccessIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchKillIntegrationTaskInstances(self, request):
        r"""批量终止集成任务实例

        :param request: Request instance for BatchKillIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchKillIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchKillIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchKillIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchKillIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchMakeUpIntegrationTasks(self, request):
        r"""对集成离线任务执行批量补数据操作

        :param request: Request instance for BatchMakeUpIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchMakeUpIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchMakeUpIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchMakeUpIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchMakeUpIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyOpsOwners(self, request):
        r"""批量修改任务责任人

        :param request: Request instance for BatchModifyOpsOwners.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOpsOwnersRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOpsOwnersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyOpsOwners", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyOpsOwnersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRerunIntegrationTaskInstances(self, request):
        r"""批量重跑集成任务实例

        :param request: Request instance for BatchRerunIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchRerunIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchRerunIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRerunIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRerunIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchResumeIntegrationTasks(self, request):
        r"""批量继续执行集成实时任务

        :param request: Request instance for BatchResumeIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchResumeIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchResumeIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchResumeIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchResumeIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRunOpsTask(self, request):
        r"""任务运维-任务列表 批量启动

        :param request: Request instance for BatchRunOpsTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchRunOpsTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchRunOpsTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRunOpsTask", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRunOpsTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStartIntegrationTasks(self, request):
        r"""批量运行集成任务

        :param request: Request instance for BatchStartIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStartIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStartIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStartIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStartIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopIntegrationTasks(self, request):
        r"""批量停止集成任务

        :param request: Request instance for BatchStopIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopOpsTasks(self, request):
        r"""仅对任务状态为”调度中“和”已暂停“有效，对所选任务的任务实例进行终止，并停止调度

        :param request: Request instance for BatchStopOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopWorkflowsByIds(self, request):
        r"""批量停止工作流

        :param request: Request instance for BatchStopWorkflowsByIds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopWorkflowsByIdsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopWorkflowsByIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopWorkflowsByIds", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopWorkflowsByIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchSuspendIntegrationTasks(self, request):
        r"""批量暂停集成任务

        :param request: Request instance for BatchSuspendIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchSuspendIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchSuspendIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchSuspendIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchSuspendIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchUpdateIntegrationTasks(self, request):
        r"""批量更新集成任务（暂时仅支持批量更新责任人）

        :param request: Request instance for BatchUpdateIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchUpdateIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchUpdateIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindProjectExecutorResource(self, request):
        r"""商业化版本：执行资源组-资源包绑定项目

        :param request: Request instance for BindProjectExecutorResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BindProjectExecutorResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BindProjectExecutorResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindProjectExecutorResource", params, headers=headers)
            response = json.loads(body)
            model = models.BindProjectExecutorResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAlarmRegularNameExist(self, request):
        r"""判断告警规则重名

        :param request: Request instance for CheckAlarmRegularNameExist.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckAlarmRegularNameExistRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckAlarmRegularNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAlarmRegularNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAlarmRegularNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIntegrationNodeNameExists(self, request):
        r"""判断集成节点名称是否存在

        :param request: Request instance for CheckIntegrationNodeNameExists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationNodeNameExistsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationNodeNameExistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntegrationNodeNameExists", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntegrationNodeNameExistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIntegrationTaskNameExists(self, request):
        r"""判断集成任务名称是否存在

        :param request: Request instance for CheckIntegrationTaskNameExists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationTaskNameExistsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationTaskNameExistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntegrationTaskNameExists", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntegrationTaskNameExistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTaskNameExist(self, request):
        r"""离线任务重名校验

        :param request: Request instance for CheckTaskNameExist.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTaskNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTaskNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitIntegrationTask(self, request):
        r"""提交集成任务

        :param request: Request instance for CommitIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitRuleGroupTask(self, request):
        r"""提交规则组运行任务接口

        :param request: Request instance for CommitRuleGroupTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitRuleGroupTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitRuleGroupTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CountOpsInstanceState(self, request):
        r"""统计任务实例状态

        :param request: Request instance for CountOpsInstanceState.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CountOpsInstanceStateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CountOpsInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CountOpsInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.CountOpsInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaseProject(self, request):
        r"""创建项目 仅项目本身，不包含集群等信息

        :param request: Request instance for CreateBaseProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateBaseProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateBaseProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaseProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaseProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodeTemplate(self, request):
        r"""创建代码模版

        :param request: Request instance for CreateCodeTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateCodeTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateCodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodeTemplateVersion(self, request):
        r"""提交代码模版

        :param request: Request instance for CreateCodeTemplateVersion.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateCodeTemplateVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateCodeTemplateVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeTemplateVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeTemplateVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomFunction(self, request):
        r"""创建用户自定义函数

        :param request: Request instance for CreateCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataModel(self, request):
        r"""创建数据建模，提供给云应用使用，实现“Wedata数据建模”的下单发货

        :param request: Request instance for CreateDataModel.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateDataModelRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateDataModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataSource(self, request):
        r"""创建数据源

        :param request: Request instance for CreateDataSource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDsFolder(self, request):
        r"""编排空间-创建文件夹

        :param request: Request instance for CreateDsFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateDsFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateDsFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDsFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDsFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHiveTable(self, request):
        r"""建hive表

        :param request: Request instance for CreateHiveTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHiveTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHiveTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHiveTableByDDL(self, request):
        r"""创建hive表，返回表名称

        :param request: Request instance for CreateHiveTableByDDL.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableByDDLRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableByDDLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHiveTableByDDL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHiveTableByDDLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntegrationNode(self, request):
        r"""创建集成节点

        :param request: Request instance for CreateIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntegrationTask(self, request):
        r"""创建集成任务

        :param request: Request instance for CreateIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOfflineTask(self, request):
        r"""创建离线任务

        :param request: Request instance for CreateOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOpsMakePlan(self, request):
        r"""批量补数据（创建补录任务）

        :param request: Request instance for CreateOpsMakePlan.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOpsMakePlanRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOpsMakePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpsMakePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpsMakePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        r"""创建质量规则接口

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRuleTemplate(self, request):
        r"""创建规则模板

        :param request: Request instance for CreateRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        r"""创建任务。本接口已废弃，请使用接口CreateTaskNew。

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskResponse`

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


    def CreateTaskAlarmRegular(self, request):
        r"""创建任务告警规则

        :param request: Request instance for CreateTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFolder(self, request):
        r"""编排空间-工作流-创建任务文件夹

        :param request: Request instance for CreateTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskNew(self, request):
        r"""聚合创建任务

        :param request: Request instance for CreateTaskNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskNew", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskVersionDs(self, request):
        r"""提交任务版本

        :param request: Request instance for CreateTaskVersionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskVersionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskVersionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskVersionDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskVersionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflowDs(self, request):
        r"""创建工作流

        :param request: Request instance for CreateWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DagInstances(self, request):
        r"""拉取dag实例

        :param request: Request instance for DagInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DagInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DagInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DagInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DagInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeTemplate(self, request):
        r"""删除代码模版

        :param request: Request instance for DeleteCodeTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteCodeTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteCodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomFunction(self, request):
        r"""删除用户自定义函数

        :param request: Request instance for DeleteCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataModel(self, request):
        r"""销毁数据建模，提供给云应用使用，实现“Wedata数据建模”的销毁

        :param request: Request instance for DeleteDataModel.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDataModelRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDataModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataSources(self, request):
        r"""删除数据源

        :param request: Request instance for DeleteDataSources.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDataSourcesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDsFolder(self, request):
        r"""编排空间-删除文件夹

        :param request: Request instance for DeleteDsFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDsFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDsFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDsFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDsFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFile(self, request):
        r"""删除文件

        :param request: Request instance for DeleteFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFileResponse`

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


    def DeleteFilePath(self, request):
        r"""开发空间-批量删除目录和文件

        :param request: Request instance for DeleteFilePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFilePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFilePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFilePath", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFilePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntegrationNode(self, request):
        r"""删除集成节点

        :param request: Request instance for DeleteIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntegrationTask(self, request):
        r"""删除集成任务

        :param request: Request instance for DeleteIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLink(self, request):
        r"""删除任务连接

        :param request: Request instance for DeleteLink.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteLinkRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteLinkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLink", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLinkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOfflineTask(self, request):
        r"""删除任务

        :param request: Request instance for DeleteOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectParamDs(self, request):
        r"""删除项目参数

        :param request: Request instance for DeleteProjectParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectUsers(self, request):
        r"""删除项目用户

        :param request: Request instance for DeleteProjectUsers.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectUsersRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResource(self, request):
        r"""资源管理删除资源。本接口已废弃，请使用接口DeleteResourceFile。

        :param request: Request instance for DeleteResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceResponse()
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
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFileResponse`

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


    def DeleteResourceFiles(self, request):
        r"""资源管理-批量删除资源文件

        :param request: Request instance for DeleteResourceFiles.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFilesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        r"""删除质量规则接口

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRuleTemplate(self, request):
        r"""删除规则模板

        :param request: Request instance for DeleteRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskAlarmRegular(self, request):
        r"""删除任务告警规则

        :param request: Request instance for DeleteTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskDs(self, request):
        r"""删除编排空间任务

        :param request: Request instance for DeleteTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskLineage(self, request):
        r"""删除任务血缘信息

        :param request: Request instance for DeleteTaskLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflowById(self, request):
        r"""通过工作流Id删除工作流

        :param request: Request instance for DeleteWorkflowById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowById", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmEvents(self, request):
        r"""告警事件列表

        :param request: Request instance for DescribeAlarmEvents.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmEventsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmReceiver(self, request):
        r"""告警接收人详情

        :param request: Request instance for DescribeAlarmReceiver.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmReceiverRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllByFolderNew(self, request):
        r"""查询父目录下所有子文件夹+工作流

        :param request: Request instance for DescribeAllByFolderNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAllByFolderNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAllByFolderNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllByFolderNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllByFolderNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApproveList(self, request):
        r"""获取待审批列表

        :param request: Request instance for DescribeApproveList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApproveList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApproveListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApproveTypeList(self, request):
        r"""获取审批分类列表

        :param request: Request instance for DescribeApproveTypeList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveTypeListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApproveTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApproveTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaseBizCatalogs(self, request):
        r"""数据地图-信息配置 数据类目列表

        :param request: Request instance for DescribeBaseBizCatalogs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaseBizCatalogsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaseBizCatalogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaseBizCatalogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaseBizCatalogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchOperateTask(self, request):
        r"""批量操作页面获取任务列表

        :param request: Request instance for DescribeBatchOperateTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBatchOperateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBatchOperateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchOperateTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchOperateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeTemplateDetail(self, request):
        r"""查询代码模版具体详情

        :param request: Request instance for DescribeCodeTemplateDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeTemplateDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeTemplateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeTemplateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeTemplateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeColumnLineage(self, request):
        r"""列出字段血缘信息

        :param request: Request instance for DescribeColumnLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeColumnLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeColumnLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeColumnsMeta(self, request):
        r"""查询表的所有列元数据

        :param request: Request instance for DescribeColumnsMeta.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnsMetaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnsMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeColumnsMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeColumnsMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataCheckStat(self, request):
        r"""数据质量的概览页面数据监测情况接口

        :param request: Request instance for DescribeDataCheckStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataCheckStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataCheckStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCheckStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataCheckStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataServicePublishedApiDetail(self, request):
        r"""查询数据服务API的发布态信息

        :param request: Request instance for DescribeDataServicePublishedApiDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataServicePublishedApiDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataServicePublishedApiDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataServicePublishedApiDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataServicePublishedApiDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataServicePublishedApiList(self, request):
        r"""获取数据服务API的发布态信息列表

        :param request: Request instance for DescribeDataServicePublishedApiList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataServicePublishedApiListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataServicePublishedApiListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataServicePublishedApiList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataServicePublishedApiListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceInfoList(self, request):
        r"""获取数据源信息-数据源分页列表

        :param request: Request instance for DescribeDataSourceInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceList(self, request):
        r"""数据源详情

        :param request: Request instance for DescribeDataSourceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseInfoList(self, request):
        r"""获取数据库信息

        :param request: Request instance for DescribeDatabaseInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseMetas(self, request):
        r"""查询数据库列表

        :param request: Request instance for DescribeDatabaseMetas.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseMetasRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseMetasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseMetas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseMetasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasource(self, request):
        r"""数据源详情

        :param request: Request instance for DescribeDatasource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatasourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependOpsTasks(self, request):
        r"""根据层级查找上/下游任务节点

        :param request: Request instance for DescribeDependOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependTaskLists(self, request):
        r"""通过taskIds查询task详情列表

        :param request: Request instance for DescribeDependTaskLists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTaskListsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTaskListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependTaskLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependTaskListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDimensionScore(self, request):
        r"""质量报告-查询质量评分

        :param request: Request instance for DescribeDimensionScore.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDimensionScoreRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDimensionScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDimensionScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDimensionScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsFolderTree(self, request):
        r"""查询目录树

        :param request: Request instance for DescribeDsFolderTree.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsFolderTreeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsFolderTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsFolderTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsFolderTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsParentFolderTree(self, request):
        r"""查询父目录树，用于工作流、任务定位

        :param request: Request instance for DescribeDsParentFolderTree.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsParentFolderTreeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsParentFolderTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsParentFolderTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsParentFolderTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsTaskVersionInfo(self, request):
        r"""查看任务版本详细信息

        :param request: Request instance for DescribeDsTaskVersionInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsTaskVersionInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsTaskVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsTaskVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsTaskVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsTaskVersionList(self, request):
        r"""拉取任务版本列表

        :param request: Request instance for DescribeDsTaskVersionList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsTaskVersionListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsTaskVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsTaskVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsTaskVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDutyScheduleDetails(self, request):
        r"""获取值班日历

        :param request: Request instance for DescribeDutyScheduleDetails.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDutyScheduleDetailsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDutyScheduleDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDutyScheduleDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDutyScheduleDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDutyScheduleList(self, request):
        r"""获取值班表列表

        :param request: Request instance for DescribeDutyScheduleList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDutyScheduleListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDutyScheduleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDutyScheduleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDutyScheduleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvent(self, request):
        r"""根据项目ID和事件名称查看事件详情

        :param request: Request instance for DescribeEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventCases(self, request):
        r"""根据条件查找事件实例

        :param request: Request instance for DescribeEventCases.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventCasesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventCasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventCases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventCasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventConsumeTasks(self, request):
        r"""查看事件实例的消费任务

        :param request: Request instance for DescribeEventConsumeTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventConsumeTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventConsumeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventConsumeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventConsumeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExecStrategy(self, request):
        r"""查询规则组执行策略

        :param request: Request instance for DescribeExecStrategy.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeExecStrategyRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeExecStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExecStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExecutorGroupMetric(self, request):
        r"""商业化版本：根据id查询执行资源组指标

        :param request: Request instance for DescribeExecutorGroupMetric.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeExecutorGroupMetricRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeExecutorGroupMetricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecutorGroupMetric", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExecutorGroupMetricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFieldBasicInfo(self, request):
        r"""元数据模型-字段基础信息查询接口

        :param request: Request instance for DescribeFieldBasicInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFieldBasicInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFieldBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFieldBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFieldBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFolderWorkflowList(self, request):
        r"""根据项目id 获取项目下所有工作流列表

        :param request: Request instance for DescribeFolderWorkflowList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderWorkflowList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFolderWorkflowListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFormVersionParam(self, request):
        r"""查询模版关联的任务和可填充参数，为下一步代码模版提交做准备

        :param request: Request instance for DescribeFormVersionParam.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFormVersionParamRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFormVersionParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFormVersionParam", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFormVersionParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionKinds(self, request):
        r"""查询函数分类

        :param request: Request instance for DescribeFunctionKinds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionKindsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionKindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionKinds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionKindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionTypes(self, request):
        r"""查询函数类型

        :param request: Request instance for DescribeFunctionTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceByCycle(self, request):
        r"""根据周期类型查询所有实例

        :param request: Request instance for DescribeInstanceByCycle.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceByCycleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceByCycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceByCycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceByCycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDetailInfo(self, request):
        r"""实例详情页，返回某个实例所有生命周期信息

        :param request: Request instance for DescribeInstanceDetailInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceDetailInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLastLog(self, request):
        r"""日志获取详情页面

        :param request: Request instance for DescribeInstanceLastLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLastLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLastLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLastLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLastLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        r"""获取实例列表

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLog(self, request):
        r"""获取实例运行日志

        :param request: Request instance for DescribeInstanceLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogDetail(self, request):
        r"""获取具体实例相关日志信息

        :param request: Request instance for DescribeInstanceLogDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogFile(self, request):
        r"""下载日志文件，返回日志下载URL

        :param request: Request instance for DescribeInstanceLogFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogList(self, request):
        r"""离线任务实例运行日志列表

        :param request: Request instance for DescribeInstanceLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationNode(self, request):
        r"""查询集成节点

        :param request: Request instance for DescribeIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatistics(self, request):
        r"""数据集成大屏概览

        :param request: Request instance for DescribeIntegrationStatistics.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsInstanceTrend(self, request):
        r"""数据集成大屏实例状态统计趋势

        :param request: Request instance for DescribeIntegrationStatisticsInstanceTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsInstanceTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsInstanceTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsInstanceTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsInstanceTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsRecordsTrend(self, request):
        r"""数据集成大屏同步条数统计趋势

        :param request: Request instance for DescribeIntegrationStatisticsRecordsTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRecordsTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRecordsTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsRecordsTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsRecordsTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsTaskStatus(self, request):
        r"""数据集成大屏任务状态分布统计

        :param request: Request instance for DescribeIntegrationStatisticsTaskStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsTaskStatusTrend(self, request):
        r"""数据集成大屏任务状态统计趋势

        :param request: Request instance for DescribeIntegrationStatisticsTaskStatusTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsTaskStatusTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsTaskStatusTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationTask(self, request):
        r"""查询集成任务

        :param request: Request instance for DescribeIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationTasks(self, request):
        r"""查询集成任务列表

        :param request: Request instance for DescribeIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationVersionNodesInfo(self, request):
        r"""查询集成任务版本节点信息

        :param request: Request instance for DescribeIntegrationVersionNodesInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationVersionNodesInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationVersionNodesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationVersionNodesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationVersionNodesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeManualTriggerRecordPage(self, request):
        r"""查询手动任务触发记录

        :param request: Request instance for DescribeManualTriggerRecordPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeManualTriggerRecordPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeManualTriggerRecordPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeManualTriggerRecordPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeManualTriggerRecordPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfflineTaskToken(self, request):
        r"""获取离线任务长连接Token

        :param request: Request instance for DescribeOfflineTaskToken.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOfflineTaskTokenRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOfflineTaskTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineTaskToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineTaskTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOperateOpsTasks(self, request):
        r"""任务运维列表组合条件查询

        :param request: Request instance for DescribeOperateOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperateOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperateOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsInstanceLogList(self, request):
        r"""实例运维-获取实例日志列表

        :param request: Request instance for DescribeOpsInstanceLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsInstanceLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsInstanceLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsInstanceLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsInstanceLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsMakePlanInstances(self, request):
        r"""根据补录计划和补录任务获取补录实例列表。

        :param request: Request instance for DescribeOpsMakePlanInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsMakePlanInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsMakePlanInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsMakePlanTasks(self, request):
        r"""查看补录计划任务

        :param request: Request instance for DescribeOpsMakePlanTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsMakePlanTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsMakePlanTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsMakePlans(self, request):
        r"""根据条件分页查询补录计划

        :param request: Request instance for DescribeOpsMakePlans.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlansRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsMakePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsMakePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsWorkflows(self, request):
        r"""查询用户生产工作流列表

        :param request: Request instance for DescribeOpsWorkflows.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationalFunctions(self, request):
        r"""查询全量函数

        :param request: Request instance for DescribeOrganizationalFunctions.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOrganizationalFunctionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOrganizationalFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationalFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationalFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParentTask(self, request):
        r"""查询任务父依赖

        :param request: Request instance for DescribeParentTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeParentTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeParentTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParentTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParentTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePendingSubmitTaskList(self, request):
        r"""获取待提交任务预提交校验信息（注意：工作流编号或者任务编号列表，必须填一项）

        :param request: Request instance for DescribePendingSubmitTaskList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribePendingSubmitTaskListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribePendingSubmitTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePendingSubmitTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePendingSubmitTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProject(self, request):
        r"""获取项目信息

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectUsers(self, request):
        r"""获取项目下的用户，分页返回

        :param request: Request instance for DescribeProjectUsers.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectUsersRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityScore(self, request):
        r"""质量报告-质量评分

        :param request: Request instance for DescribeQualityScore.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityScoreTrend(self, request):
        r"""质量报告-质量分周期趋势

        :param request: Request instance for DescribeQualityScoreTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityScoreTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealTimeTaskInstanceNodeInfo(self, request):
        r"""查询实时任务实例节点信息

        :param request: Request instance for DescribeRealTimeTaskInstanceNodeInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealTimeTaskMetricOverview(self, request):
        r"""实时任务运行指标概览

        :param request: Request instance for DescribeRealTimeTaskMetricOverview.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskMetricOverviewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskMetricOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskMetricOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskMetricOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealTimeTaskSpeed(self, request):
        r"""实时任务同步速度趋势

        :param request: Request instance for DescribeRealTimeTaskSpeed.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskSpeedRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskSpeedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskSpeed", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskSpeedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealViewSchemaPage(self, request):
        r"""数据集成分页获取数据库SCHEMA信息

        :param request: Request instance for DescribeRealViewSchemaPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealViewSchemaPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealViewSchemaPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealViewSchemaPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealViewSchemaPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRelatedTasksByTaskId(self, request):
        r"""根据任务ID分页查询任务绑定监听的事件

        :param request: Request instance for DescribeRelatedTasksByTaskId.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedTasksByTaskIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedTasksByTaskIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedTasksByTaskId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelatedTasksByTaskIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportTaskDetail(self, request):
        r"""查询上报任务详情，注意：任务执行完后，任务详情上报存在10分钟的延迟，使用接口查询任务详情时需等待任务运行完10分钟后查询

        :param request: Request instance for DescribeReportTaskDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeReportTaskDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeReportTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportTaskList(self, request):
        r"""查询上报任务列表

        :param request: Request instance for DescribeReportTaskList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeReportTaskListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeReportTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceManagePathTrees(self, request):
        r"""获取资源管理目录树

        :param request: Request instance for DescribeResourceManagePathTrees.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeResourceManagePathTreesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeResourceManagePathTreesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceManagePathTrees", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceManagePathTreesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleList(self, request):
        r"""获取角色列表信息

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRule(self, request):
        r"""查询规则详情

        :param request: Request instance for DescribeRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleDimStat(self, request):
        r"""数据质量概览页面触发维度分布统计接口

        :param request: Request instance for DescribeRuleDimStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDimStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDimStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleDimStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleDimStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecDetail(self, request):
        r"""查询规则执行结果详情

        :param request: Request instance for DescribeRuleExecDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecLog(self, request):
        r"""规则执行日志查询

        :param request: Request instance for DescribeRuleExecLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecResults(self, request):
        r"""规则执行结果列表查询

        :param request: Request instance for DescribeRuleExecResults.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecResults", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecStat(self, request):
        r"""数据质量概览页面规则运行情况接口

        :param request: Request instance for DescribeRuleExecStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroup(self, request):
        r"""查询规则组详情接口

        :param request: Request instance for DescribeRuleGroup.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupExecResultsByPage(self, request):
        r"""规则组执行结果分页查询接口

        :param request: Request instance for DescribeRuleGroupExecResultsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupExecResultsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupExecResultsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupSubscription(self, request):
        r"""查询规则组订阅信息

        :param request: Request instance for DescribeRuleGroupSubscription.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupSubscriptionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupTable(self, request):
        r"""查询表绑定执行规则组信息

        :param request: Request instance for DescribeRuleGroupTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupsByPage(self, request):
        r"""【过滤条件】
        {表名称TableName,支持模糊匹配}       {表负责人TableOwnerName,支持模糊匹配}      {监控方式MonitorTypes，1.未配置 2.关联生产调度 3.离线周期检测,支持多选}  {订阅人ReceiverUin}
        【必要字段】
        {数据来源DatasourceId}

        :param request: Request instance for DescribeRuleGroupsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplate(self, request):
        r"""查询模板详情

        :param request: Request instance for DescribeRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplates(self, request):
        r"""查询规则模板列表

        :param request: Request instance for DescribeRuleTemplates.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplatesByPage(self, request):
        r"""【过滤条件】 {模板名称Name,支持模糊匹配} {模板类型type，1.系统模板 2.自定义模板} {质量检测维度QualityDims, 1.准确性 2.唯一性 3.完整性 4.一致性 5.及时性 6.有效性} 【排序字段】 { 引用数排序类型CitationOrderType，根据引用数量排序 ASC DESC}

        :param request: Request instance for DescribeRuleTemplatesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplatesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplatesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        r"""查询质量规则列表

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRulesByPage(self, request):
        r"""分页查询质量规则

        :param request: Request instance for DescribeRulesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScheduleInstances(self, request):
        r"""获取实例列表

        :param request: Request instance for DescribeScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerInstanceStatus(self, request):
        r"""运维大屏-实例状态分布

        :param request: Request instance for DescribeSchedulerInstanceStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerInstanceStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerInstanceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerInstanceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerRunTimeInstanceCntByStatus(self, request):
        r"""运维大屏-实例运行时长排行

        :param request: Request instance for DescribeSchedulerRunTimeInstanceCntByStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerRunTimeInstanceCntByStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerRunTimeInstanceCntByStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerRunTimeInstanceCntByStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerRunTimeInstanceCntByStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerTaskCntByStatus(self, request):
        r"""任务状态统计

        :param request: Request instance for DescribeSchedulerTaskCntByStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskCntByStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskCntByStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerTaskCntByStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerTaskCntByStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerTaskTypeCnt(self, request):
        r"""运维大屏-任务状态分布

        :param request: Request instance for DescribeSchedulerTaskTypeCnt.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskTypeCntRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskTypeCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerTaskTypeCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerTaskTypeCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStatisticInstanceStatusTrendOps(self, request):
        r"""任务状态趋势

        :param request: Request instance for DescribeStatisticInstanceStatusTrendOps.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStatisticInstanceStatusTrendOpsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStatisticInstanceStatusTrendOpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatisticInstanceStatusTrendOps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStatisticInstanceStatusTrendOpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamTaskLogList(self, request):
        r"""查询实时任务日志列表

        :param request: Request instance for DescribeStreamTaskLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStreamTaskLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStreamTaskLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamTaskLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamTaskLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSuccessorOpsTaskInfos(self, request):
        r"""获取下游任务信息

        :param request: Request instance for DescribeSuccessorOpsTaskInfos.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSuccessorOpsTaskInfosRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSuccessorOpsTaskInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSuccessorOpsTaskInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSuccessorOpsTaskInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSuccessorTaskInfoList(self, request):
        r"""获取下游任务信息批量

        :param request: Request instance for DescribeSuccessorTaskInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSuccessorTaskInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSuccessorTaskInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSuccessorTaskInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSuccessorTaskInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableBasicInfo(self, request):
        r"""元数据模型-表基础信息查询接口

        :param request: Request instance for DescribeTableBasicInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableBasicInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableInfoList(self, request):
        r"""获取数据表信息

        :param request: Request instance for DescribeTableInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableLineage(self, request):
        r"""列出表血缘信息

        :param request: Request instance for DescribeTableLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableLineageInfo(self, request):
        r"""列出表血缘信息

        :param request: Request instance for DescribeTableLineageInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableLineageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableLineageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableMeta(self, request):
        r"""查询表元数据详情

        :param request: Request instance for DescribeTableMeta.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableMetas(self, request):
        r"""获取表元数据list

        :param request: Request instance for DescribeTableMetas.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetasRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableMetas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableMetasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTablePartitions(self, request):
        r"""查询表的分区详情信息

        :param request: Request instance for DescribeTablePartitions.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTablePartitionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTablePartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablePartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablePartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableQualityDetails(self, request):
        r"""质量报告-查询表质量详情

        :param request: Request instance for DescribeTableQualityDetails.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableQualityDetailsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableQualityDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableQualityDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableQualityDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableSchemaInfo(self, request):
        r"""获取表schema信息

        :param request: Request instance for DescribeTableSchemaInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableSchemaInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableSchemaInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableSchemaInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableSchemaInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableScoreTrend(self, request):
        r"""查询表得分趋势

        :param request: Request instance for DescribeTableScoreTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableScoreTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableScoreTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableScoreTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableScoreTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskAlarmRegulations(self, request):
        r"""查询任务告警规则列表

        :param request: Request instance for DescribeTaskAlarmRegulations.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskAlarmRegulationsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskAlarmRegulationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskAlarmRegulations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskAlarmRegulationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByCycle(self, request):
        r"""根据周期类型 查询所有任务

        :param request: Request instance for DescribeTaskByCycle.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskByCycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskByCycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByStatusReport(self, request):
        r"""任务状态趋势

        :param request: Request instance for DescribeTaskByStatusReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByStatusReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByStatusReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskByStatusReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskByStatusReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetailDs(self, request):
        r"""查询任务具体详情【新】

        :param request: Request instance for DescribeTaskDetailDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetailDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLineage(self, request):
        r"""通过任务查询表的血缘关系

        :param request: Request instance for DescribeTaskLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLockStatus(self, request):
        r"""查看任务锁状态信息

        :param request: Request instance for DescribeTaskLockStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLockStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLockStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLockStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLockStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskParamDs(self, request):
        r"""查询任务引用参数

        :param request: Request instance for DescribeTaskParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskRunHistory(self, request):
        r"""分页查询任务运行历史

        :param request: Request instance for DescribeTaskRunHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskRunHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskRunHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskRunHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskRunHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskScript(self, request):
        r"""查询任务脚本。本接口已废弃，请使用接口GetPaginationTaskScript。

        :param request: Request instance for DescribeTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskTableMetricOverview(self, request):
        r"""查询实时任务表粒度指标概览

        :param request: Request instance for DescribeTaskTableMetricOverview.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskTableMetricOverviewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskTableMetricOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskTableMetricOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskTableMetricOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskTemplates(self, request):
        r"""查询项目下所有任务列表,包括虚拟任务

        :param request: Request instance for DescribeTaskTemplates.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasksForCodeTemplate(self, request):
        r"""分页查询引用模板的任务列表

        :param request: Request instance for DescribeTasksForCodeTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksForCodeTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksForCodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksForCodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksForCodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateDimCount(self, request):
        r"""查询规则模板维度分布情况

        :param request: Request instance for DescribeTemplateDimCount.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateDimCountRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateDimCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateDimCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateDimCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTenantProjects(self, request):
        r"""租户全局范围的项目列表，与用户查看范围无关.

        :param request: Request instance for DescribeTenantProjects.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTenantProjectsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTenantProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTenantProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTenantProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTestRunningRecord(self, request):
        r"""获取编排空间试运行历史

        :param request: Request instance for DescribeTestRunningRecord.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTestRunningRecordRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTestRunningRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTestRunningRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTestRunningRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeThirdTaskRunLog(self, request):
        r"""获取第三方运行日志

        :param request: Request instance for DescribeThirdTaskRunLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeThirdTaskRunLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeThirdTaskRunLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeThirdTaskRunLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeThirdTaskRunLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopTableStat(self, request):
        r"""数据质量概览页面表排行接口

        :param request: Request instance for DescribeTopTableStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTopTableStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTopTableStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopTableStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopTableStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrendStat(self, request):
        r"""数据质量概览页面趋势变化接口

        :param request: Request instance for DescribeTrendStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTrendStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTrendStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrendStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrendStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowByFordIds(self, request):
        r"""根据文件夹查询工作流

        :param request: Request instance for DescribeWorkflowByFordIds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowByFordIdsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowByFordIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowByFordIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowByFordIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowCanvasInfo(self, request):
        r"""查询工作流画布

        :param request: Request instance for DescribeWorkflowCanvasInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowCanvasInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowCanvasInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowExecuteById(self, request):
        r"""查询工作流画布运行起止时间

        :param request: Request instance for DescribeWorkflowExecuteById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowExecuteByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowExecuteByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowExecuteById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowExecuteByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowInfoById(self, request):
        r"""通过工作流id，查询工作流详情

        :param request: Request instance for DescribeWorkflowInfoById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowInfoByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowInfoByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowInfoById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowInfoByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowListByProjectId(self, request):
        r"""根据项目id 获取项目下所有工作流列表

        :param request: Request instance for DescribeWorkflowListByProjectId.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowListByProjectIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowListByProjectIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowListByProjectId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowListByProjectIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowSchedulerInfoDs(self, request):
        r"""获取工作流调度信息

        :param request: Request instance for DescribeWorkflowSchedulerInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowSchedulerInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowSchedulerInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowSchedulerInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowSchedulerInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowTaskCount(self, request):
        r"""查询工作流任务数

        :param request: Request instance for DescribeWorkflowTaskCount.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowTaskCountRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowTaskCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowTaskCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowTaskCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DiagnosePro(self, request):
        r"""实例诊断，用于诊断 INITIAL、DEPENDENCE、ALLOCATED、LAUNCHED、EVENT_LISTENING、BEFORE_ASPECT、EXPIRED、FAILED状态的实例

        :param request: Request instance for DiagnosePro.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DiagnoseProRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DiagnoseProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DiagnosePro", params, headers=headers)
            response = json.loads(body)
            model = models.DiagnoseProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableProject(self, request):
        r"""禁用项目

        :param request: Request instance for DisableProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DisableProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DisableProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableProject", params, headers=headers)
            response = json.loads(body)
            model = models.DisableProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadLogByLine(self, request):
        r"""按行下载日志信息

        :param request: Request instance for DownloadLogByLine.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DownloadLogByLineRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DownloadLogByLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadLogByLine", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadLogByLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DryRunDIOfflineTask(self, request):
        r"""调试运行集成任务

        :param request: Request instance for DryRunDIOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DryRunDIOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DryRunDIOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DryRunDIOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DryRunDIOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableProject(self, request):
        r"""启用项目

        :param request: Request instance for EnableProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.EnableProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.EnableProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableProject", params, headers=headers)
            response = json.loads(body)
            model = models.EnableProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FindAllFolder(self, request):
        r"""编排空间批量操作页面查找全部的文件夹

        :param request: Request instance for FindAllFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FindAllFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FindAllFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FindAllFolder", params, headers=headers)
            response = json.loads(body)
            model = models.FindAllFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeOpsTasks(self, request):
        r"""任务运维-批量暂停任务

        :param request: Request instance for FreezeOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeTasksByWorkflowIds(self, request):
        r"""暂停工作流下的所有任务

        :param request: Request instance for FreezeTasksByWorkflowIds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByWorkflowIdsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByWorkflowIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasksByWorkflowIds", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeTasksByWorkflowIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenHiveTableDDLSql(self, request):
        r"""生成建hive表的sql

        :param request: Request instance for GenHiveTableDDLSql.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GenHiveTableDDLSqlRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GenHiveTableDDLSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenHiveTableDDLSql", params, headers=headers)
            response = json.loads(body)
            model = models.GenHiveTableDDLSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetBatchDetailErrorLog(self, request):
        r"""获取批量操作错误日志

        :param request: Request instance for GetBatchDetailErrorLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetBatchDetailErrorLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetBatchDetailErrorLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBatchDetailErrorLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetBatchDetailErrorLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCosToken(self, request):
        r"""获取cos token

        :param request: Request instance for GetCosToken.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetCosTokenRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetCosTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCosToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetCosTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFileInfo(self, request):
        r"""开发空间-获取数据开发脚本信息

        :param request: Request instance for GetFileInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetFileInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetFileInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFileInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetFileInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInstanceLog(self, request):
        r"""获取实例列表

        :param request: Request instance for GetInstanceLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetInstanceLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInstanceLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetInstanceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetIntegrationNodeColumnSchema(self, request):
        r"""提取数据集成节点字段Schema

        :param request: Request instance for GetIntegrationNodeColumnSchema.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetIntegrationNodeColumnSchemaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetIntegrationNodeColumnSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetIntegrationNodeColumnSchema", params, headers=headers)
            response = json.loads(body)
            model = models.GetIntegrationNodeColumnSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetJobStatus(self, request):
        r"""获取异步任务执行结果

        :param request: Request instance for GetJobStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetJobStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetJobStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetJobStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetJobStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOfflineDIInstanceList(self, request):
        r"""获取离线任务实例列表(新)

        :param request: Request instance for GetOfflineDIInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetOfflineDIInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetOfflineDIInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOfflineDIInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetOfflineDIInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOfflineInstanceList(self, request):
        r"""获取离线任务实例

        :param request: Request instance for GetOfflineInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetOfflineInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetOfflineInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOfflineInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetOfflineInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPaginationTaskScript(self, request):
        r"""获取带分页的任务脚本

        :param request: Request instance for GetPaginationTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetPaginationTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetPaginationTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPaginationTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.GetPaginationTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskInstance(self, request):
        r"""获取实例列表

        :param request: Request instance for GetTaskInstance.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetTaskInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetTaskInstanceResponse`

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


    def JudgeResourceFile(self, request):
        r"""资源管理-判断资源文件是否存在

        :param request: Request instance for JudgeResourceFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.JudgeResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.JudgeResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("JudgeResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.JudgeResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillOpsMakePlanInstances(self, request):
        r"""按补录计划批量终止实例。

        :param request: Request instance for KillOpsMakePlanInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillOpsMakePlanInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillOpsMakePlanInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillOpsMakePlanInstances", params, headers=headers)
            response = json.loads(body)
            model = models.KillOpsMakePlanInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillScheduleInstances(self, request):
        r"""批量终止实例

        :param request: Request instance for KillScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.KillScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListBatchDetail(self, request):
        r"""获取批量操作详情列表

        :param request: Request instance for ListBatchDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ListBatchDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ListBatchDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListBatchDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListBatchDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListInstances(self, request):
        r"""获取实例列表

        :param request: Request instance for ListInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ListInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ListInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockIntegrationTask(self, request):
        r"""锁定集成任务

        :param request: Request instance for LockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.LockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.LockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.LockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApproveStatus(self, request):
        r"""修改审批单状态

        :param request: Request instance for ModifyApproveStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyApproveStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyApproveStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApproveStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApproveStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataSource(self, request):
        r"""修改数据源

        :param request: Request instance for ModifyDataSource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDimensionWeight(self, request):
        r"""质量报告-修改维度权限

        :param request: Request instance for ModifyDimensionWeight.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDimensionWeightRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDimensionWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDimensionWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDimensionWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDsFolder(self, request):
        r"""数据开发模块-文件夹更新

        :param request: Request instance for ModifyDsFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDsFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDsFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDsFolder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDsFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExecStrategy(self, request):
        r"""更新规则组执行策略

        :param request: Request instance for ModifyExecStrategy.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyExecStrategyRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyExecStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExecStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExecStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIntegrationNode(self, request):
        r"""更新集成节点

        :param request: Request instance for ModifyIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIntegrationTask(self, request):
        r"""更新集成任务

        :param request: Request instance for ModifyIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMonitorStatus(self, request):
        r"""更新监控状态

        :param request: Request instance for ModifyMonitorStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyMonitorStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyMonitorStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMonitorStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMonitorStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        r"""修改项目基础信息。

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        r"""更新质量规则接口

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleGroupSubscription(self, request):
        r"""更新规则组订阅信息

        :param request: Request instance for ModifyRuleGroupSubscription.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleGroupSubscriptionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleGroupSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleGroupSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleGroupSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleTemplate(self, request):
        r"""编辑规则模板

        :param request: Request instance for ModifyRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskAlarmRegular(self, request):
        r"""修改任务告警规则

        :param request: Request instance for ModifyTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskInfo(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        更新任务。本接口已废弃，请使用接口ModifyTaskInfoDs。

        :param request: Request instance for ModifyTaskInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskInfoDs(self, request):
        r"""更新任务Ds

        :param request: Request instance for ModifyTaskInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskLinks(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        添加父任务依赖。本接口已废弃，请使用接口ModifyTaskLinksDs。

        :param request: Request instance for ModifyTaskLinks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskLinks", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskLinksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskLinksDs(self, request):
        r"""添加父任务依赖

        :param request: Request instance for ModifyTaskLinksDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskLinksDs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskLinksDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskName(self, request):
        r"""重命名任务（任务编辑）

        :param request: Request instance for ModifyTaskName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskScript(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        修改任务脚本。本接口已废弃，请使用接口ModifyTaskInfoDs。

        :param request: Request instance for ModifyTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkflowInfo(self, request):
        r"""更新工作流信息。本接口已废弃，请使用接口UpdateWorkflowInfo。

        :param request: Request instance for ModifyWorkflowInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkflowInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkflowSchedule(self, request):
        r"""更新工作流调度。本接口已废弃，请使用接口RenewWorkflowSchedulerInfoDs。

        :param request: Request instance for ModifyWorkflowSchedule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkflowScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveTasksToFolder(self, request):
        r"""编排空间-工作流-移动任务到工作流文件夹

        :param request: Request instance for MoveTasksToFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MoveTasksToFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MoveTasksToFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveTasksToFolder", params, headers=headers)
            response = json.loads(body)
            model = models.MoveTasksToFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterDsEvent(self, request):
        r"""注册事件

        :param request: Request instance for RegisterDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterDsEventListener(self, request):
        r"""注册事件监听者

        :param request: Request instance for RegisterDsEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterDsEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterDsEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterDsEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterDsEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterEvent(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        注册事件。本接口已废弃，请使用接口RegisterDsEvent。

        :param request: Request instance for RegisterEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEvent", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterEventListener(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        注册事件监听器。本接口已废弃，请使用接口RegisterDsEventListener。

        :param request: Request instance for RegisterEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveDatabase(self, request):
        r"""移除database元数据

        :param request: Request instance for RemoveDatabase.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RemoveDatabaseRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RemoveDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveSchema(self, request):
        r"""移除schema元数据

        :param request: Request instance for RemoveSchema.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RemoveSchemaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RemoveSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveSchema", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveTable(self, request):
        r"""移除table元数据

        :param request: Request instance for RemoveTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RemoveTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RemoveTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveTable", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWorkflowDs(self, request):
        r"""删除编排空间工作流

        :param request: Request instance for RemoveWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RemoveWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RemoveWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewWorkflowOwnerDs(self, request):
        r"""批量更新工作流下任务责任人

        :param request: Request instance for RenewWorkflowOwnerDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowOwnerDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowOwnerDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewWorkflowOwnerDs", params, headers=headers)
            response = json.loads(body)
            model = models.RenewWorkflowOwnerDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewWorkflowSchedulerInfoDs(self, request):
        r"""更新工作流下任务调度信息

        :param request: Request instance for RenewWorkflowSchedulerInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowSchedulerInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowSchedulerInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewWorkflowSchedulerInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.RenewWorkflowSchedulerInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportDatabase(self, request):
        r"""上报database元数据

        :param request: Request instance for ReportDatabase.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ReportDatabaseRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ReportDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.ReportDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportSchema(self, request):
        r"""上报schema元数据

        :param request: Request instance for ReportSchema.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ReportSchemaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ReportSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportSchema", params, headers=headers)
            response = json.loads(body)
            model = models.ReportSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportTable(self, request):
        r"""上报table元数据

        :param request: Request instance for ReportTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ReportTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ReportTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportTable", params, headers=headers)
            response = json.loads(body)
            model = models.ReportTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportTaskLineage(self, request):
        r"""血缘上报接口

        :param request: Request instance for ReportTaskLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ReportTaskLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ReportTaskLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportTaskLineage", params, headers=headers)
            response = json.loads(body)
            model = models.ReportTaskLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeIntegrationTask(self, request):
        r"""继续集成任务

        :param request: Request instance for ResumeIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ResumeIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ResumeIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RobAndLockIntegrationTask(self, request):
        r"""抢占锁定集成任务

        :param request: Request instance for RobAndLockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RobAndLockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RobAndLockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RobAndLockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.RobAndLockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunForceSucScheduleInstances(self, request):
        r"""实例批量置成功

        :param request: Request instance for RunForceSucScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunForceSucScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunForceSucScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunForceSucScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunForceSucScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunRerunScheduleInstances(self, request):
        r"""实例批量重跑

        :param request: Request instance for RunRerunScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunRerunScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunRerunScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunRerunScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunRerunScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunTasksByMultiWorkflow(self, request):
        r"""批量启动工作流

        :param request: Request instance for RunTasksByMultiWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunTasksByMultiWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunTasksByMultiWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunTasksByMultiWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.RunTasksByMultiWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveCustomFunction(self, request):
        r"""保存用户自定义函数

        :param request: Request instance for SaveCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SaveCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SaveCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.SaveCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTaskAlarmNew(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        设置任务告警，新建/更新告警信息（最新）

        :param request: Request instance for SetTaskAlarmNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTaskAlarmNew", params, headers=headers)
            response = json.loads(body)
            model = models.SetTaskAlarmNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartIntegrationTask(self, request):
        r"""启动集成任务

        :param request: Request instance for StartIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StartIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StartIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StartIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopIntegrationTask(self, request):
        r"""停止集成任务

        :param request: Request instance for StopIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StopIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StopIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitCustomFunction(self, request):
        r"""提交自定义函数

        :param request: Request instance for SubmitCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitSqlTask(self, request):
        r"""即席分析提交SQL任务

        :param request: Request instance for SubmitSqlTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitSqlTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitSqlTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitSqlTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitSqlTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTask(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        提交任务。本接口已废弃，请使用接口CreateTaskVersionDs。

        :param request: Request instance for SubmitTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskResponse`

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


    def SubmitTaskTestRun(self, request):
        r"""无

        :param request: Request instance for SubmitTaskTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTaskTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitWorkflow(self, request):
        r"""提交工作流。本接口已废弃，请使用接口BatchCreateTaskVersionAsync。

        :param request: Request instance for SubmitWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SuspendIntegrationTask(self, request):
        r"""暂停集成任务

        :param request: Request instance for SuspendIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SuspendIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SuspendIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SuspendIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.SuspendIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TaskLog(self, request):
        r"""查询Inlong manager日志

        :param request: Request instance for TaskLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TaskLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TaskLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TaskLog", params, headers=headers)
            response = json.loads(body)
            model = models.TaskLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerDsEvent(self, request):
        r"""事件管理-触发事件

        :param request: Request instance for TriggerDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerEvent(self, request):
        r"""<p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        触发事件。本接口已废弃，请使用接口TriggerDsEvent。

        :param request: Request instance for TriggerEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerManualTasks(self, request):
        r"""手动任务触发运行

        :param request: Request instance for TriggerManualTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerManualTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerManualTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerManualTasks", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerManualTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnboundProjectExecutorResource(self, request):
        r"""商业化版本：执行资源组/资源包解除绑定项目

        :param request: Request instance for UnboundProjectExecutorResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UnboundProjectExecutorResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UnboundProjectExecutorResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnboundProjectExecutorResource", params, headers=headers)
            response = json.loads(body)
            model = models.UnboundProjectExecutorResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnlockIntegrationTask(self, request):
        r"""解锁集成任务

        :param request: Request instance for UnlockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UnlockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UnlockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCodeTemplate(self, request):
        r"""更新模版

        :param request: Request instance for UpdateCodeTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateCodeTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateCodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataModelRegistryInfo(self, request):
        r"""数语向wedata注册，提供自身cam角色信息，跳转域名、ip、端口信息等

        :param request: Request instance for UpdateDataModelRegistryInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateDataModelRegistryInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateDataModelRegistryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataModelRegistryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataModelRegistryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProjectUserRole(self, request):
        r"""修改项目用户角色

        :param request: Request instance for UpdateProjectUserRole.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateProjectUserRoleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateProjectUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProjectUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProjectUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflowInfo(self, request):
        r"""<p style="color:red;">[该接口为 ds 中开发]</p>
        更新工作流（包括工作流基本信息与工作流参数）

        :param request: Request instance for UpdateWorkflowInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateWorkflowInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateWorkflowInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflowInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflowOwner(self, request):
        r"""修改工作流责任人。本接口已废弃，请使用接口RenewWorkflowOwnerDs。

        :param request: Request instance for UpdateWorkflowOwner.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateWorkflowOwnerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateWorkflowOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflowOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadContent(self, request):
        r"""保存任务信息

        :param request: Request instance for UploadContent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UploadContentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UploadContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadContent", params, headers=headers)
            response = json.loads(body)
            model = models.UploadContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadResource(self, request):
        r"""资源管理-上传资源

        :param request: Request instance for UploadResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UploadResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UploadResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadResource", params, headers=headers)
            response = json.loads(body)
            model = models.UploadResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))