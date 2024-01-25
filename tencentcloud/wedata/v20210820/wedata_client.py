# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def AcquireLock(self, request):
        """获取协同编辑资源锁

        :param request: Request instance for AcquireLock.
        :type request: :class:`tencentcloud.wedata.v20210820.models.AcquireLockRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.AcquireLockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcquireLock", params, headers=headers)
            response = json.loads(body)
            model = models.AcquireLockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AnalyzeDependentTasks(self, request):
        """上游依赖自动解析

        :param request: Request instance for AnalyzeDependentTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.AnalyzeDependentTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.AnalyzeDependentTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AnalyzeDependentTasks", params, headers=headers)
            response = json.loads(body)
            model = models.AnalyzeDependentTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateIntegrationTaskAlarms(self, request):
        """批量创建任务告警规则

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
        """异步批量创建任务版本

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


    def BatchCreateTaskVersionDs(self, request):
        """批量创建任务版本Ds

        :param request: Request instance for BatchCreateTaskVersionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchCreateTaskVersionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchCreateTaskVersionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateTaskVersionDs", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateTaskVersionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateVirtualTaskDs(self, request):
        """批量创建虚拟任务, 用于新建跨工作流任务场景中新增跨工作流任务操作

        :param request: Request instance for BatchCreateVirtualTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchCreateVirtualTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchCreateVirtualTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateVirtualTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateVirtualTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteIntegrationTasks(self, request):
        """批量删除集成任务

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
        """智能运维-批量删除任务

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


    def BatchDeleteTasksDs(self, request):
        """Ds批量删除任务，仅对任务状态为”已停止“有效；

        :param request: Request instance for BatchDeleteTasksDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteTasksDs", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteTasksDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteTasksDsAsync(self, request):
        """Ds批量删除任务，仅对任务状态为”已停止“有效；

        :param request: Request instance for BatchDeleteTasksDsAsync.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksDsAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksDsAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteTasksDsAsync", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteTasksDsAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量删除任务，仅对任务状态为”已停止“有效；

        :param request: Request instance for BatchDeleteTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchForceSuccessIntegrationTaskInstances(self, request):
        """批量置成功集成任务实例

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
        """批量终止集成任务实例

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
        """对集成离线任务执行批量补数据操作

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
        """批量修改任务责任人

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


    def BatchModifyOwnersNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量修改任务责任人

        :param request: Request instance for BatchModifyOwnersNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOwnersNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOwnersNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyOwnersNew", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyOwnersNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRerunIntegrationTaskInstances(self, request):
        """批量重跑集成任务实例

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
        """批量继续执行集成实时任务

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
        """任务运维-任务列表 批量运行

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


    def BatchRunTasksDs(self, request):
        """批量运行任务, 用于工作流-任务配置-运行、工作流-任务右键-运行、任务运维-任务管理-更多操作-运行、任务运维-任务管理-选择任务-批量运行等场景。
        1. 任务运行预判断
        2. 更新db中任务状态
        3. 通知scheduler进行运行操作

        :param request: Request instance for BatchRunTasksDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchRunTasksDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchRunTasksDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRunTasksDs", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRunTasksDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStartIntegrationTasks(self, request):
        """批量运行集成任务

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
        """批量停止集成任务

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
        """仅对任务状态为”调度中“和”已暂停“有效，对所选任务的任务实例进行终止，并停止调度

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


    def BatchStopTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        仅对任务状态为”调度中“和”已暂停“有效，对所选任务的任务实例进行终止，并停止调度

        :param request: Request instance for BatchStopTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopWorkflowsByIds(self, request):
        """批量停止工作流

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
        """批量暂停集成任务

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
        """批量更新集成任务（暂时仅支持批量更新责任人）

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


    def BatchUpdateTasksDs(self, request):
        """批量更新任务Ds

        :param request: Request instance for BatchUpdateTasksDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateTasksDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateTasksDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchUpdateTasksDs", params, headers=headers)
            response = json.loads(body)
            model = models.BatchUpdateTasksDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAlarmRegularNameExist(self, request):
        """判断告警规则重名

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


    def CheckCustomFunctionPremise(self, request):
        """新建用户自定义函数组件检查

        :param request: Request instance for CheckCustomFunctionPremise.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckCustomFunctionPremiseRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckCustomFunctionPremiseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCustomFunctionPremise", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCustomFunctionPremiseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDuplicateRuleName(self, request):
        """检查规则名称是否重复

        :param request: Request instance for CheckDuplicateRuleName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateRuleNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateRuleNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDuplicateRuleName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDuplicateRuleNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDuplicateTemplateName(self, request):
        """检查规则模板名称是否重复

        :param request: Request instance for CheckDuplicateTemplateName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateTemplateNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateTemplateNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDuplicateTemplateName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDuplicateTemplateNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIntegrationNodeNameExists(self, request):
        """判断集成节点名称是否存在

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
        """判断集成任务名称是否存在

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
        """离线任务重名校验

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


    def CheckTaskNameExistDs(self, request):
        """检查任务名称是否重复

        :param request: Request instance for CheckTaskNameExistDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTaskNameExistDs", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTaskNameExistDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTaskPriorityDs(self, request):
        """检查操作用户对所选任务是否有操作权限, 用于新建跨工作流任务场景中展示审批提示操作

        :param request: Request instance for CheckTaskPriorityDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckTaskPriorityDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckTaskPriorityDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTaskPriorityDs", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTaskPriorityDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearRecycleTask(self, request):
        """清空回收站任务

        :param request: Request instance for ClearRecycleTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ClearRecycleTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ClearRecycleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearRecycleTask", params, headers=headers)
            response = json.loads(body)
            model = models.ClearRecycleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitExportTask(self, request):
        """提交数据导出任务

        :param request: Request instance for CommitExportTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitExportTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitIntegrationTask(self, request):
        """提交集成任务

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


    def CommitRuleGroupExecResult(self, request):
        """Runner 规则检测结果上报

        :param request: Request instance for CommitRuleGroupExecResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupExecResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupExecResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitRuleGroupExecResult", params, headers=headers)
            response = json.loads(body)
            model = models.CommitRuleGroupExecResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitRuleGroupTask(self, request):
        """提交规则组运行任务接口

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


    def CommitWorkflow(self, request):
        """工作流版本提交

        :param request: Request instance for CommitWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CommitWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareDsTaskVersionInfo(self, request):
        """对比任务版本

        :param request: Request instance for CompareDsTaskVersionInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CompareDsTaskVersionInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CompareDsTaskVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompareDsTaskVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.CompareDsTaskVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyTaskDs(self, request):
        """复制任务Ds

        :param request: Request instance for CopyTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CopyTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CopyTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.CopyTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyWorkflowDs(self, request):
        """复制工作流

        :param request: Request instance for CopyWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CopyWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CopyWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.CopyWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CountOpsInstanceState(self, request):
        """统计任务实例状态

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


    def CreateBaseline(self, request):
        """创建基线

        :param request: Request instance for CreateBaseline.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateBaselineRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBrowsingHistory(self, request):
        """创建用户数据开发浏览历史

        :param request: Request instance for CreateBrowsingHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateBrowsingHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateBrowsingHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBrowsingHistory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBrowsingHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomFunction(self, request):
        """创建用户自定义函数

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


    def CreateDataSource(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建数据源

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
        """编排空间-创建文件夹

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


    def CreateFileVersion(self, request):
        """创建开发空间版本

        :param request: Request instance for CreateFileVersion.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateFileVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateFileVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建文件夹

        :param request: Request instance for CreateFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHiveTable(self, request):
        """建hive表

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
        """创建hive表，返回表名称

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


    def CreateInLongAgent(self, request):
        """注册采集器

        :param request: Request instance for CreateInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntegrationNode(self, request):
        """创建集成节点

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
        """创建集成任务

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


    def CreateLink(self, request):
        """创建任务连接

        :param request: Request instance for CreateLink.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateLinkRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateLinkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLink", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLinkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOfflineTask(self, request):
        """创建离线任务

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
        """补录任务

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


    def CreateOrUpdateResource(self, request):
        """资源管理需要先将资源上传到cos中，然后调用该接口，将cos资源绑定到wedata

        :param request: Request instance for CreateOrUpdateResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOrUpdateResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOrUpdateResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrUpdateResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrUpdateResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePath(self, request):
        """新建文件夹

        :param request: Request instance for CreatePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreatePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreatePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePath", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProjectParamDs(self, request):
        """创建项目参数

        :param request: Request instance for CreateProjectParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateProjectParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateProjectParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProjectParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceDirectory(self, request):
        """资源管理-创建资源目录

        :param request: Request instance for CreateResourceDirectory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateResourceDirectoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateResourceDirectoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceDirectory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceDirectoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourcePath(self, request):
        """文件路径的根目录为 /datastudio/resource，如果要在根目录下创建 aaa 文件夹，FilePath的值应该为 /datastudio/resource，如果根目录下已经创建了 aaa 文件夹，要在 aaa 下创建  bbb 文件夹，FilePath的值应该为 /datastudio/resource/aaa

        :param request: Request instance for CreateResourcePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateResourcePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateResourcePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourcePath", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourcePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """创建质量规则接口

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
        """创建规则模版

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


    def CreateScriptsImportTasksDs(self, request):
        """编排空间导入开发空间脚本。

        :param request: Request instance for CreateScriptsImportTasksDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateScriptsImportTasksDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateScriptsImportTasksDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScriptsImportTasksDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScriptsImportTasksDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建任务

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
        """创建任务告警规则

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


    def CreateTaskDs(self, request):
        """创建任务Ds

        :param request: Request instance for CreateTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFolder(self, request):
        """编排空间-工作流-创建任务文件夹

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


    def CreateTaskInParamDs(self, request):
        """设置任务输入参数

        :param request: Request instance for CreateTaskInParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskInParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskInParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskInParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskInParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskOutParamDs(self, request):
        """设置任务输出参数

        :param request: Request instance for CreateTaskOutParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskOutParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskOutParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskOutParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskOutParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskOutputRegistries(self, request):
        """批量创建登记项

        :param request: Request instance for CreateTaskOutputRegistries.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskOutputRegistriesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskOutputRegistriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskOutputRegistries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskOutputRegistriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskOutputRegistry(self, request):
        """新增或编辑产出登记项

        :param request: Request instance for CreateTaskOutputRegistry.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskOutputRegistryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskOutputRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskOutputRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskOutputRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskParamDs(self, request):
        """任务引用参数

        :param request: Request instance for CreateTaskParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskVersionDs(self, request):
        """创建任务版本

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


    def CreateWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建工作流

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowResponse`

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


    def CreateWorkflowDs(self, request):
        """创建工作流

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
        """拉取dag实例

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


    def DeleteBaseline(self, request):
        """DeleteBaseline

        :param request: Request instance for DeleteBaseline.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteBaselineRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBatchWorkflowDs(self, request):
        """批量删除工作流

        :param request: Request instance for DeleteBatchWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteBatchWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteBatchWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBatchWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBatchWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomFunction(self, request):
        """删除用户自定义函数

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


    def DeleteDataSources(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除数据源

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


    def DeleteDsEvent(self, request):
        """删除事件

        :param request: Request instance for DeleteDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDsEventListener(self, request):
        """删除事件监听者

        :param request: Request instance for DeleteDsEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDsEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDsEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDsEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDsEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDsEventPublisher(self, request):
        """删除事件发布者

        :param request: Request instance for DeleteDsEventPublisher.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDsEventPublisherRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDsEventPublisherResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDsEventPublisher", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDsEventPublisherResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDsFolder(self, request):
        """编排空间-删除文件夹

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


    def DeleteEventListenerByTaskId(self, request):
        """通过任务ID删除所有事件

        :param request: Request instance for DeleteEventListenerByTaskId.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteEventListenerByTaskIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteEventListenerByTaskIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEventListenerByTaskId", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEventListenerByTaskIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFile(self, request):
        """删除文件

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
        """开发空间-批量删除目录和文件

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


    def DeleteFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除文件夹

        :param request: Request instance for DeleteFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInLongAgent(self, request):
        """删除采集器

        :param request: Request instance for DeleteInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntegrationNode(self, request):
        """删除集成节点

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
        """删除集成任务

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
        """删除任务连接

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
        """删除任务

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
        """删除项目参数

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


    def DeleteProjectParamVersionDs(self, request):
        """删除项目参数版本

        :param request: Request instance for DeleteProjectParamVersionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectParamVersionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectParamVersionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectParamVersionDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectParamVersionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectUsers(self, request):
        """删除项目用户

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


    def DeleteRecordList(self, request):
        """批量删除任务提交记录列表

        :param request: Request instance for DeleteRecordList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRecordListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecycleTask(self, request):
        """删除回收站任务

        :param request: Request instance for DeleteRecycleTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRecycleTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRecycleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecycleTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecycleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResource(self, request):
        """资源管理删除资源

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
        """资源管理-删除资源文件

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
        """资源管理-批量删除资源文件

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


    def DeleteResourcePath(self, request):
        """资源管理-删除资源目录

        :param request: Request instance for DeleteResourcePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourcePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourcePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourcePath", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourcePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """删除质量规则接口

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
        """删除规则模版

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
        """删除任务告警规则

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
        """删除任务Ds

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


    def DeleteTaskFolder(self, request):
        """编排空间-工作流-删除任务文件夹

        :param request: Request instance for DeleteTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskInParamDs(self, request):
        """删除任务输入参数

        :param request: Request instance for DeleteTaskInParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskInParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskInParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskInParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskInParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskOutParamDs(self, request):
        """删除任务输出参数

        :param request: Request instance for DeleteTaskOutParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskOutParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskOutParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskOutParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskOutParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskOutputRegistry(self, request):
        """删除产出登记项

        :param request: Request instance for DeleteTaskOutputRegistry.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskOutputRegistryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskOutputRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskOutputRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskOutputRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflowById(self, request):
        """通过工作流Id删除工作流

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


    def DeleteWorkflowNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除工作流

        :param request: Request instance for DeleteWorkflowNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowNew", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmEvents(self, request):
        """告警事件列表

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
        """告警接收人详情

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
        """查询父目录下所有子文件夹+工作流

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


    def DescribeAllParamDs(self, request):
        """查询所有参数

        :param request: Request instance for DescribeAllParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAllParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAllParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllTaskType(self, request):
        """获取所有任务类型

        :param request: Request instance for DescribeAllTaskType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAllTaskTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAllTaskTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllTaskType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllTaskTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllUsedVersionSon(self, request):
        """根据任务Id查找生产态子任务

        :param request: Request instance for DescribeAllUsedVersionSon.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAllUsedVersionSonRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAllUsedVersionSonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllUsedVersionSon", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllUsedVersionSonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApproveList(self, request):
        """获取待审批列表

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
        """获取审批分类列表

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


    def DescribeBaselineAllTaskDag(self, request):
        """查询基线DAG

        :param request: Request instance for DescribeBaselineAllTaskDag.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineAllTaskDagRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineAllTaskDagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAllTaskDag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAllTaskDagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineById(self, request):
        """基线列表

        :param request: Request instance for DescribeBaselineById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineInstanceDag(self, request):
        """查询基线实例DAG

        :param request: Request instance for DescribeBaselineInstanceDag.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineInstanceDagRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineInstanceDagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineInstanceDag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineInstanceDagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineInstanceGantt(self, request):
        """查询基线实例关键任务实例甘特图

        :param request: Request instance for DescribeBaselineInstanceGantt.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineInstanceGanttRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineInstanceGanttResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineInstanceGantt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineInstanceGanttResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineInstances(self, request):
        """查询基线实例列表

        :param request: Request instance for DescribeBaselineInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselineInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselines(self, request):
        """基线列表

        :param request: Request instance for DescribeBaselines.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselinesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBaselinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchOperateTask(self, request):
        """批量操作任务列表

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


    def DescribeBatchTestRun(self, request):
        """批量获取etl测试运行任务执行状态和日志

        :param request: Request instance for DescribeBatchTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBatchTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBatchTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBelongTo(self, request):
        """智能运维-事件列表-所属任务/基线过滤列表

        :param request: Request instance for DescribeBelongTo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBelongToRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBelongToResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBelongTo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBelongToResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBrowsingHistories(self, request):
        """查询用户数据开发浏览历史

        :param request: Request instance for DescribeBrowsingHistories.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBrowsingHistoriesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBrowsingHistoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBrowsingHistories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBrowsingHistoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChildrenDs(self, request):
        """查询子任务信息Ds

        :param request: Request instance for DescribeChildrenDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeChildrenDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeChildrenDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChildrenDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChildrenDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChildrenPathTrees(self, request):
        """开发空间-拉取指定路径目录树

        :param request: Request instance for DescribeChildrenPathTrees.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeChildrenPathTreesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeChildrenPathTreesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChildrenPathTrees", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChildrenPathTreesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNamespaceList(self, request):
        """获取集群命名空间列表

        :param request: Request instance for DescribeClusterNamespaceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeClusterNamespaceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeClusterNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeDetail(self, request):
        """查询文件或任务详情

        :param request: Request instance for DescribeCodeDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeDetailV2(self, request):
        """全局搜索查询文件或任务详情

        :param request: Request instance for DescribeCodeDetailV2.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeDetailV2Request`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeDetailV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeDetailV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeDetailV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeSearchAuditInfo(self, request):
        """查询最近5条代码搜索审计日志

        :param request: Request instance for DescribeCodeSearchAuditInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchAuditInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchAuditInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeSearchAuditInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeSearchAuditInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeSearchAuditInfoV2(self, request):
        """获取代码搜索最近n条关键字搜索信息

        :param request: Request instance for DescribeCodeSearchAuditInfoV2.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchAuditInfoV2Request`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchAuditInfoV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeSearchAuditInfoV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeSearchAuditInfoV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeSearchCount(self, request):
        """代码搜索结果的统计信息

        :param request: Request instance for DescribeCodeSearchCount.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchCountRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeSearchCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeSearchCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeSearchInfo(self, request):
        """根据条件搜索代码

        :param request: Request instance for DescribeCodeSearchInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeSearchInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeSearchInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeSearchInfoV2(self, request):
        """全局搜索根据条件搜索代码

        :param request: Request instance for DescribeCodeSearchInfoV2.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchInfoV2Request`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCodeSearchInfoV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeSearchInfoV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeSearchInfoV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeColumnLineage(self, request):
        """列出字段血缘信息

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
        """查询表的所有列元数据

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


    def DescribeCrontabTopNDs(self, request):
        """获取 crontab topN 个数据时间周期

        :param request: Request instance for DescribeCrontabTopNDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCrontabTopNDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCrontabTopNDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrontabTopNDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrontabTopNDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomFunctionVersionList(self, request):
        """查询函数版本列表

        :param request: Request instance for DescribeCustomFunctionVersionList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeCustomFunctionVersionListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeCustomFunctionVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomFunctionVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomFunctionVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataBases(self, request):
        """查询数据来源列表

        :param request: Request instance for DescribeDataBases.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataBasesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataBasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataBases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataBasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataCheckStat(self, request):
        """数据质量的概览页面数据监测情况接口

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


    def DescribeDataDevelopTaskType(self, request):
        """获取数据开发任务类型

        :param request: Request instance for DescribeDataDevelopTaskType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataDevelopTaskTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataDevelopTaskTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataDevelopTaskType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataDevelopTaskTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataObjects(self, request):
        """查询规则组数据对象列表

        :param request: Request instance for DescribeDataObjects.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataObjectsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceInfoList(self, request):
        """获取数据源信息-数据源分页列表

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        数据源详情

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


    def DescribeDataSourceWithoutInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        数据源列表

        :param request: Request instance for DescribeDataSourceWithoutInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceWithoutInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceWithoutInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceWithoutInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceWithoutInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataTableImportProgress(self, request):
        """获取数据表导入状态

        :param request: Request instance for DescribeDataTableImportProgress.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataTableImportProgressRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataTableImportProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataTableImportProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataTableImportProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataTypes(self, request):
        """获取字段类型列表

        :param request: Request instance for DescribeDataTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseInfoList(self, request):
        """获取数据库信息

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
        """查询数据库列表

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        数据源详情

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


    def DescribeDependOpsTaskList(self, request):
        """根据任务id获取下游依赖任务列表

        :param request: Request instance for DescribeDependOpsTaskList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependOpsTaskListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependOpsTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependOpsTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependOpsTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependOpsTasks(self, request):
        """根据层级查找上/下游任务节点

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
        """通过taskIds查询task详情列表

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


    def DescribeDependTasksDevDs(self, request):
        """根据层级查找开发态上下游任务节点

        :param request: Request instance for DescribeDependTasksDevDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksDevDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksDevDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependTasksDevDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependTasksDevDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        根据层级查找上/下游任务节点

        :param request: Request instance for DescribeDependTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependencyTasksForProjectClone(self, request):
        """【项目克隆任务模式】依赖任务信息查询

        :param request: Request instance for DescribeDependencyTasksForProjectClone.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependencyTasksForProjectCloneRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependencyTasksForProjectCloneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependencyTasksForProjectClone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependencyTasksForProjectCloneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependencyWorkflowForProjectClone(self, request):
        """查询依赖工作流信息查询-项目克隆使用

        :param request: Request instance for DescribeDependencyWorkflowForProjectClone.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependencyWorkflowForProjectCloneRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependencyWorkflowForProjectCloneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependencyWorkflowForProjectClone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependencyWorkflowForProjectCloneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevelopmentSpaceSupportType(self, request):
        """获取开发空间支持的脚本类型

        :param request: Request instance for DescribeDevelopmentSpaceSupportType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDevelopmentSpaceSupportTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDevelopmentSpaceSupportTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevelopmentSpaceSupportType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevelopmentSpaceSupportTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiagnosticInfoByBaselineId(self, request):
        """查询基线诊断信息

        :param request: Request instance for DescribeDiagnosticInfoByBaselineId.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDiagnosticInfoByBaselineIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDiagnosticInfoByBaselineIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiagnosticInfoByBaselineId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiagnosticInfoByBaselineIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDimensionScore(self, request):
        """质量报告-查询质量评分

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


    def DescribeDrInstancePage(self, request):
        """分页查询试运行实例列表

        :param request: Request instance for DescribeDrInstancePage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDrInstancePageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDrInstancePageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrInstancePage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrInstancePageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrInstanceScriptContent(self, request):
        """查询试运行实例执行内容

        :param request: Request instance for DescribeDrInstanceScriptContent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDrInstanceScriptContentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDrInstanceScriptContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrInstanceScriptContent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrInstanceScriptContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrSonInstance(self, request):
        """查询试运行实例子实例列表

        :param request: Request instance for DescribeDrSonInstance.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDrSonInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDrSonInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrSonInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrSonInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsEvent(self, request):
        """分页查询事件

        :param request: Request instance for DescribeDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsEventDetail(self, request):
        """事件管理-查询事件详情

        :param request: Request instance for DescribeDsEventDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsEventListener(self, request):
        """查询事件监听者信息

        :param request: Request instance for DescribeDsEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsEventListenerList(self, request):
        """查询事件监听者列表

        :param request: Request instance for DescribeDsEventListenerList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventListenerListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventListenerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsEventListenerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsEventListenerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsEventPublisher(self, request):
        """查询事件发布者信息

        :param request: Request instance for DescribeDsEventPublisher.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventPublisherRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventPublisherResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsEventPublisher", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsEventPublisherResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsEventPublisherList(self, request):
        """查询事件发布者列表

        :param request: Request instance for DescribeDsEventPublisherList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventPublisherListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsEventPublisherListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsEventPublisherList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsEventPublisherListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsFolderTree(self, request):
        """查询目录树

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


    def DescribeDsKettleServerFolderTree(self, request):
        """查询 kettle 资源服务器目录树

        :param request: Request instance for DescribeDsKettleServerFolderTree.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsKettleServerFolderTreeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsKettleServerFolderTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsKettleServerFolderTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsKettleServerFolderTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsLatestTaskVersionInfo(self, request):
        """获取任务最新版本

        :param request: Request instance for DescribeDsLatestTaskVersionInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsLatestTaskVersionInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsLatestTaskVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsLatestTaskVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsLatestTaskVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsNotSubmitTasksAndCanRunByWorkflow(self, request):
        """根据工作流id查询保存未提交任务

        :param request: Request instance for DescribeDsNotSubmitTasksAndCanRunByWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsNotSubmitTasksAndCanRunByWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsNotSubmitTasksAndCanRunByWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsNotSubmitTasksAndCanRunByWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsNotSubmitTasksAndCanRunByWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsParentFolderTree(self, request):
        """查询父目录树，用于工作流、任务定位

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
        """查看任务版本详细信息

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
        """拉取任务版本列表

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


    def DescribeEtlTaskType(self, request):
        """获取数据同步任务类型

        :param request: Request instance for DescribeEtlTaskType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEtlTaskTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEtlTaskTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEtlTaskType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEtlTaskTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvent(self, request):
        """根据项目ID和事件名称查看事件详情

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
        """根据条件查找事件实例

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
        """查看事件实例的消费任务

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


    def DescribeEventDetail(self, request):
        """智能运维事件详情1

        :param request: Request instance for DescribeEventDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventIsAlarmTypes(self, request):
        """事件是否告警过滤条件

        :param request: Request instance for DescribeEventIsAlarmTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventIsAlarmTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventIsAlarmTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventIsAlarmTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventIsAlarmTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventListenerByTaskId(self, request):
        """根据任务ID获取任务监听事件

        :param request: Request instance for DescribeEventListenerByTaskId.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventListenerByTaskIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventListenerByTaskIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventListenerByTaskId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventListenerByTaskIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventListenerTask(self, request):
        """事件管理-查询事件关联任务

        :param request: Request instance for DescribeEventListenerTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventListenerTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventListenerTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventListenerTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventListenerTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventTypes(self, request):
        """查询事件类型列表

        :param request: Request instance for DescribeEventTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvents(self, request):
        """智能运维事件查询列表

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventsResponse`

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


    def DescribeExecStrategy(self, request):
        """查询规则组执行策略

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


    def DescribeExecutionLog(self, request):
        """获取执行日志

        :param request: Request instance for DescribeExecutionLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeExecutionLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeExecutionLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecutionLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExecutionLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFatherDatasourceInfoDs(self, request):
        """查询父任务数据源信息Ds

        :param request: Request instance for DescribeFatherDatasourceInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFatherDatasourceInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFatherDatasourceInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFatherDatasourceInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFatherDatasourceInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFathers(self, request):
        """获取关联父实例

        :param request: Request instance for DescribeFathers.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFathersRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFathersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFathers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFathersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFieldBasicInfo(self, request):
        """元数据模型-字段基础信息查询接口

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


    def DescribeFileVersions(self, request):
        """查询开发空间版本列表

        :param request: Request instance for DescribeFileVersions.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFileVersionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFileVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFolderList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        拉取文件夹目录

        :param request: Request instance for DescribeFolderList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFolderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFolderWorkflowList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        拉取文件夹下的工作流

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


    def DescribeFunctionKinds(self, request):
        """查询函数分类

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
        """查询函数类型

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


    def DescribeGlobalWorkflowDs(self, request):
        """获取全局工作流信息，用于跨工作流节点拉取租户所有工作流列表

        :param request: Request instance for DescribeGlobalWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeGlobalWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeGlobalWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImportableOfflineTask(self, request):
        """查询可导入的集成任务

        :param request: Request instance for DescribeImportableOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeImportableOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeImportableOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImportableOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImportableOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInLongAgentList(self, request):
        """获取采集器列表

        :param request: Request instance for DescribeInLongAgentList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongAgentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongAgentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInLongAgentTaskList(self, request):
        """查询采集器关联的任务列表

        :param request: Request instance for DescribeInLongAgentTaskList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentTaskListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongAgentTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongAgentTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInLongAgentVpcList(self, request):
        """获取采集器所在集群的VPC列表

        :param request: Request instance for DescribeInLongAgentVpcList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentVpcListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentVpcListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongAgentVpcList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongAgentVpcListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInLongTkeClusterList(self, request):
        """获取TKE集群列表

        :param request: Request instance for DescribeInLongTkeClusterList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongTkeClusterListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongTkeClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongTkeClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongTkeClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInfoTransByTypeIdDs(self, request):
        """基于任务类型获取任务信息Ds

        :param request: Request instance for DescribeInfoTransByTypeIdDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInfoTransByTypeIdDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInfoTransByTypeIdDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInfoTransByTypeIdDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInfoTransByTypeIdDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceByCycle(self, request):
        """根据周期类型查询所有实例

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


    def DescribeInstanceByCycleReport(self, request):
        """实例状态周期增长趋势

        :param request: Request instance for DescribeInstanceByCycleReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceByCycleReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceByCycleReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceByCycleReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceByCycleReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLastLog(self, request):
        """日志获取详情页面

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
        """获取实例列表

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
        """获取实例运行日志

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
        """获取具体实例相关日志信息

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
        """下载日志文件，返回日志URL

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
        """离线任务实例运行日志列表

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


    def DescribeInstanceLogs(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        获取实例日志列表

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """数据质量，查询调度任务的实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesInfoWithTaskInfo(self, request):
        """拉取实例列表，join task表一些信息

        :param request: Request instance for DescribeInstancesInfoWithTaskInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstancesInfoWithTaskInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstancesInfoWithTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesInfoWithTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesInfoWithTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationNode(self, request):
        """查询集成节点

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
        """数据集成大屏概览

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


    def DescribeIntegrationStatisticsAgentStatus(self, request):
        """数据集成大屏采集器状态分布统计

        :param request: Request instance for DescribeIntegrationStatisticsAgentStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsAgentStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsAgentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsAgentStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsAgentStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsInstanceTrend(self, request):
        """数据集成大屏实例状态统计趋势

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
        """数据集成大屏同步条数统计趋势

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
        """数据集成大屏任务状态分布统计

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
        """数据集成大屏任务状态统计趋势

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
        """查询集成任务

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
        """查询集成任务列表

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
        """查询集成任务版本节点信息

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


    def DescribeLock(self, request):
        """获取协同编辑资源锁

        :param request: Request instance for DescribeLock.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeLockRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeLockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLock", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonitorsByPage(self, request):
        """分页查询质量监控组

        :param request: Request instance for DescribeMonitorsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeMonitorsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeMonitorsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNewSqlTaskResult(self, request):
        """新获取SQL执行结果

        :param request: Request instance for DescribeNewSqlTaskResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeNewSqlTaskResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeNewSqlTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNewSqlTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNewSqlTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfflineTaskToken(self, request):
        """获取离线任务长连接Token

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


    def DescribeOperateOpsTaskDatasource(self, request):
        """任务运维搜索 查询生产态任务数据源列表

        :param request: Request instance for DescribeOperateOpsTaskDatasource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTaskDatasourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTaskDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperateOpsTaskDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperateOpsTaskDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOperateOpsTaskDatasourceType(self, request):
        """任务运维-查询生产态任务数据源类型列表

        :param request: Request instance for DescribeOperateOpsTaskDatasourceType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTaskDatasourceTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTaskDatasourceTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperateOpsTaskDatasourceType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperateOpsTaskDatasourceTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOperateOpsTasks(self, request):
        """任务运维列表组合条件查询

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


    def DescribeOperateTasks(self, request):
        """任务运维列表组合条件查询

        :param request: Request instance for DescribeOperateTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsInstanceLogList(self, request):
        """实例运维-获取实例日志列表

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
        """根据补录计划和补录任务获取补录实例列表。

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
        """查看补录计划任务

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
        """根据条件分页查询补录计划

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
        """查询用户生产工作流列表

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
        """查询全量函数

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
        """查询任务父依赖

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


    def DescribePathTrees(self, request):
        """开发空间-拉取完整目录树

        :param request: Request instance for DescribePathTrees.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribePathTreesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribePathTreesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePathTrees", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePathTreesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProdTasks(self, request):
        """数据质量获取生产调度任务列表

        :param request: Request instance for DescribeProdTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProdTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProdTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProdTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProdTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProdWorkflowCanvasInfoDs(self, request):
        """获取工作流画布信息

        :param request: Request instance for DescribeProdWorkflowCanvasInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProdWorkflowCanvasInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProdWorkflowCanvasInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProdWorkflowCanvasInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProdWorkflowCanvasInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProject(self, request):
        """获取项目信息

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


    def DescribeProjectParamDs(self, request):
        """查询项目全局参数

        :param request: Request instance for DescribeProjectParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectParamDsPage(self, request):
        """查询项目全局参数

        :param request: Request instance for DescribeProjectParamDsPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamDsPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamDsPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectParamDsPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectParamDsPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectParamVersionDs(self, request):
        """查询项目参数历史版本

        :param request: Request instance for DescribeProjectParamVersionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamVersionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamVersionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectParamVersionDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectParamVersionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectParamVersionInfoDs(self, request):
        """拉取项目参数版本详情

        :param request: Request instance for DescribeProjectParamVersionInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamVersionInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectParamVersionInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectParamVersionInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectParamVersionInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityScore(self, request):
        """质量报告-质量评分

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
        """质量报告-质量分周期趋势

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
        """查询实时任务实例节点信息

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
        """实时任务运行指标概览

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
        """实时任务同步速度趋势

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


    def DescribeRecordList(self, request):
        """即席分析-获取任务列表

        :param request: Request instance for DescribeRecordList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRecordListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecycleTaskDetail(self, request):
        """获取回收站任务详情

        :param request: Request instance for DescribeRecycleTaskDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRecycleTaskDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRecycleTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecycleTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecycleTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecycleTaskList(self, request):
        """查询回收站任务列表

        :param request: Request instance for DescribeRecycleTaskList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRecycleTaskListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRecycleTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecycleTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecycleTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRelatedInstances(self, request):
        """查询任务实例的关联实例列表

        :param request: Request instance for DescribeRelatedInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelatedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceManagePathTrees(self, request):
        """获取资源管理目录树

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


    def DescribeRule(self, request):
        """查询规则详情

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


    def DescribeRuleDataSources(self, request):
        """查询质量规则数据源

        :param request: Request instance for DescribeRuleDataSources.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDataSourcesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleDimStat(self, request):
        """数据质量概览页面触发维度分布统计接口

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
        """查询规则执行结果详情

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


    def DescribeRuleExecExportResult(self, request):
        """查询规则执行导出结果

        :param request: Request instance for DescribeRuleExecExportResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecExportResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecExportResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecExportResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecExportResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecHistory(self, request):
        """查询规则执行历史， 最近30条

        :param request: Request instance for DescribeRuleExecHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecLog(self, request):
        """规则执行日志查询

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
        """规则执行结果列表查询

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


    def DescribeRuleExecResultsByPage(self, request):
        """分页查询规则执行结果列表

        :param request: Request instance for DescribeRuleExecResultsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecResultsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecResultsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecStat(self, request):
        """数据质量概览页面规则运行情况接口

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
        """查询规则组详情接口

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
        """规则组执行结果分页查询接口

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


    def DescribeRuleGroupExecResultsByPageWithoutAuth(self, request):
        """规则组执行结果分页查询接口不带鉴权

        :param request: Request instance for DescribeRuleGroupExecResultsByPageWithoutAuth.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageWithoutAuthRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageWithoutAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupExecResultsByPageWithoutAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupExecResultsByPageWithoutAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupSubscription(self, request):
        """查询规则组订阅信息

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
        """查询表绑定执行规则组信息

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
        """【过滤条件】
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


    def DescribeRuleHistoryByPage(self, request):
        """过滤条件【必要字段】{ruleId}

        :param request: Request instance for DescribeRuleHistoryByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleHistoryByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleHistoryByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleHistoryByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleHistoryByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTablesByPage(self, request):
        """获取表列表

        :param request: Request instance for DescribeRuleTablesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTablesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTablesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTablesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTablesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplate(self, request):
        """查询模板详情

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
        """查询规则模版列表

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
        """过滤条件】 {模版名称Name,支持模糊匹配} {模版类型type，1.系统模版 2.自定义模版} {质量检测维度QualityDims, 1.准确性 2.唯一性 3.完整性 4.一致性 5.及时性 6.有效性} 【排序字段】 { 引用数排序类型CitationOrderType，根据引用数量排序 ASC DESC}

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
        """查询质量规则列表

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
        """分页查询质量规则

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


    def DescribeScheduleInstance(self, request):
        """在基线系统内查询单个调度任务实例

        :param request: Request instance for DescribeScheduleInstance.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeScheduleInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeScheduleInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScheduleInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScheduleInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScheduleInstances(self, request):
        """获取实例列表

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
        """运维大屏-实例状态分布

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
        """运维大屏-实例运行时长排行

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
        """任务状态统计

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
        """运维大屏-任务状态分布

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


    def DescribeScriptsImportTaskType(self, request):
        """获取脚本导出任务类型

        :param request: Request instance for DescribeScriptsImportTaskType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeScriptsImportTaskTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeScriptsImportTaskTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScriptsImportTaskType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScriptsImportTaskTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSonInstances(self, request):
        """获取关联子实例

        :param request: Request instance for DescribeSonInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSonInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSonInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSonInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSonInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSqlTaskResult(self, request):
        """获取SQL执行结果

        :param request: Request instance for DescribeSqlTaskResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSqlTaskResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSqlTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSqlTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSqlTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStandardRuleDetailInfoList(self, request):
        """获取数据标准规则详情

        :param request: Request instance for DescribeStandardRuleDetailInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStandardRuleDetailInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStandardRuleDetailInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStandardRuleDetailInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStandardRuleDetailInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStatisticInstanceStatusTrendOps(self, request):
        """任务状态趋势

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
        """查询实时任务日志列表

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
        """获取下游任务信息

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


    def DescribeTableBasicInfo(self, request):
        """元数据模型-表基础信息查询接口

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
        """获取数据表信息

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
        """列出表血缘信息

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
        """列出表血缘信息

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
        """查询表元数据详情

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
        """获取表元数据list

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


    def DescribeTableQualityDetails(self, request):
        """质量报告-查询表质量详情

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
        """获取表schema信息

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
        """查询表得分趋势

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
        """查询任务告警规则列表

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


    def DescribeTaskBindVirtualTask(self, request):
        """获取任务绑定的虚拟任务

        :param request: Request instance for DescribeTaskBindVirtualTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskBindVirtualTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskBindVirtualTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskBindVirtualTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskBindVirtualTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByCycle(self, request):
        """根据周期类型 查询所有任务

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


    def DescribeTaskByCycleReport(self, request):
        """任务状态周期增长趋势

        :param request: Request instance for DescribeTaskByCycleReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskByCycleReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskByCycleReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByStatusReport(self, request):
        """任务状态趋势

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


    def DescribeTaskDetail(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        查询任务具体详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetailDs(self, request):
        """查询任务具体详情Ds

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


    def DescribeTaskInParamDs(self, request):
        """查询任务输入参数

        :param request: Request instance for DescribeTaskInParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInstance(self, request):
        """离线任务实例详情

        :param request: Request instance for DescribeTaskInstance.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInstanceReportDetail(self, request):
        """离线任务实例统计明细

        :param request: Request instance for DescribeTaskInstanceReportDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceReportDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceReportDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstanceReportDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInstanceReportDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInstances(self, request):
        """查询任务实例列表

        :param request: Request instance for DescribeTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLatestRunTime(self, request):
        """通过指定基准时间，计算出最近一次任务基于该基准时间的运行时间

        :param request: Request instance for DescribeTaskLatestRunTime.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLatestRunTimeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLatestRunTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLatestRunTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLatestRunTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskListByConditionDs(self, request):
        """基于条件翻页获取任务列表, 用于新建跨工作流任务场景中展示工作流列表操作

        :param request: Request instance for DescribeTaskListByConditionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskListByConditionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskListByConditionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskListByConditionDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskListByConditionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLockStatus(self, request):
        """查看任务锁状态信息

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


    def DescribeTaskOutParamDs(self, request):
        """查询任务输出参数

        :param request: Request instance for DescribeTaskOutParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskOutParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskOutParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskOutParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskOutParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskOutputRegistries(self, request):
        """获取指定任务产出登记列表

        :param request: Request instance for DescribeTaskOutputRegistries.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskOutputRegistriesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskOutputRegistriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskOutputRegistries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskOutputRegistriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskParamDs(self, request):
        """查询任务引用参数

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


    def DescribeTaskParentRunTime(self, request):
        """基于当前任务的数据时间计算依赖的上游任务数据时间

        :param request: Request instance for DescribeTaskParentRunTime.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskParentRunTimeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskParentRunTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskParentRunTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskParentRunTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskReport(self, request):
        """按起止日期统计离线任务的所有实例的运行指标总和

        :param request: Request instance for DescribeTaskReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskReportDetailList(self, request):
        """离线任务周期统计明细

        :param request: Request instance for DescribeTaskReportDetailList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportDetailListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskReportDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskReportDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskRunHistory(self, request):
        """分页查询任务运行历史

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        查询任务脚本

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


    def DescribeTaskTypeByScriptType(self, request):
        """根据脚本类型获取任务类型

        :param request: Request instance for DescribeTaskTypeByScriptType.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskTypeByScriptTypeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskTypeByScriptTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskTypeByScriptType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskTypeByScriptTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasksByPage(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        根据工作流分页查询任务

        :param request: Request instance for DescribeTasksByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasksForProjectClone(self, request):
        """任务信息查询-项目克隆使用

        :param request: Request instance for DescribeTasksForProjectClone.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksForProjectCloneRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksForProjectCloneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksForProjectClone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksForProjectCloneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateDimCount(self, request):
        """查询规则模板维度分布情况

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


    def DescribeTemplateHistory(self, request):
        """查询规则模板操作记录

        :param request: Request instance for DescribeTemplateHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTestRun(self, request):
        """获取etl测试运行任务执行状态和日志

        :param request: Request instance for DescribeTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeThirdTaskRunLog(self, request):
        """获取第三方运行日志

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


    def DescribeToken(self, request):
        """获取长连接Token

        :param request: Request instance for DescribeToken.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTokenRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopTableStat(self, request):
        """数据质量概览页面表排行接口

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
        """数据质量概览页面趋势变化接口

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
        """根据文件夹查询工作流

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
        """查询工作流画布

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


    def DescribeWorkflowCanvasInfoDs(self, request):
        """数据开发-获取工作流画布信息

        :param request: Request instance for DescribeWorkflowCanvasInfoDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasInfoDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasInfoDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowCanvasInfoDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowCanvasInfoDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowCanvasOpLogs(self, request):
        """获取工作流操作日志

        :param request: Request instance for DescribeWorkflowCanvasOpLogs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasOpLogsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasOpLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowCanvasOpLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowCanvasOpLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowCanvasOperators(self, request):
        """获取工作流画布操作人列表

        :param request: Request instance for DescribeWorkflowCanvasOperators.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasOperatorsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasOperatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowCanvasOperators", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowCanvasOperatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowExecuteById(self, request):
        """查询工作流画布运行起止时间

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


    def DescribeWorkflowForProjectClone(self, request):
        """工作流信息查询-项目克隆使用

        :param request: Request instance for DescribeWorkflowForProjectClone.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowForProjectCloneRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowForProjectCloneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowForProjectClone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowForProjectCloneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowInfoById(self, request):
        """通过工作流id，查询工作流详情

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
        """根据项目id 获取项目下所有工作流列表

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


    def DescribeWorkflowOpsCanvasInfo(self, request):
        """查询运维画布信息，只需要获取边和节点

        :param request: Request instance for DescribeWorkflowOpsCanvasInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowOpsCanvasInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowOpsCanvasInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowOpsCanvasInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowOpsCanvasInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowParamDs(self, request):
        """查询工作流全局参数

        :param request: Request instance for DescribeWorkflowParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowSchedulerInfoDs(self, request):
        """获取工作流调度信息

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
        """查询工作流任务数

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


    def DescribeWorkflowTasksForProjectClone(self, request):
        """工作流任务信息查询-项目克隆使用

        :param request: Request instance for DescribeWorkflowTasksForProjectClone.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowTasksForProjectCloneRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowTasksForProjectCloneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowTasksForProjectClone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowTasksForProjectCloneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DiagnosePlus(self, request):
        """实例诊断信息

        :param request: Request instance for DiagnosePlus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DiagnosePlusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DiagnosePlusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DiagnosePlus", params, headers=headers)
            response = json.loads(body)
            model = models.DiagnosePlusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadNewSqlResult(self, request):
        """下载SQL执行结果

        :param request: Request instance for DownloadNewSqlResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DownloadNewSqlResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DownloadNewSqlResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadNewSqlResult", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadNewSqlResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadSqlResult(self, request):
        """下载SQL执行结果

        :param request: Request instance for DownloadSqlResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DownloadSqlResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DownloadSqlResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadSqlResult", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadSqlResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DryRunDIOfflineTask(self, request):
        """调试运行集成任务

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


    def EditBaseline(self, request):
        """编辑基线

        :param request: Request instance for EditBaseline.
        :type request: :class:`tencentcloud.wedata.v20210820.models.EditBaselineRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.EditBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.EditBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportDsEvent(self, request):
        """事件管理-导出事件

        :param request: Request instance for ExportDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ExportDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ExportDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ExportDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportFiles(self, request):
        """批量导出文件

        :param request: Request instance for ExportFiles.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ExportFilesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ExportFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ExportFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportProjectParamDs(self, request):
        """导出项目参数

        :param request: Request instance for ExportProjectParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ExportProjectParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ExportProjectParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportProjectParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.ExportProjectParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportWorkflowXml(self, request):
        """导出工作流(XML格式)，导出的文件存储在 cos 中(私有化 csp)，请自行下载，相关的下载信息在返回值中可以获取到

        :param request: Request instance for ExportWorkflowXml.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ExportWorkflowXmlRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ExportWorkflowXmlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportWorkflowXml", params, headers=headers)
            response = json.loads(body)
            model = models.ExportWorkflowXmlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportWorkflowZip(self, request):
        """导出工作流到 Zip 文件，导出的文件存储在 cos 中(私有化 csp)，请自行下载，相关的下载信息在返回值中可以获取到

        :param request: Request instance for ExportWorkflowZip.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ExportWorkflowZipRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ExportWorkflowZipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportWorkflowZip", params, headers=headers)
            response = json.loads(body)
            model = models.ExportWorkflowZipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FindAllFolder(self, request):
        """查找全部的文件夹

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


    def FindDependTaskListDs(self, request):
        """拉取下游依赖的任务列表Ds

        :param request: Request instance for FindDependTaskListDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FindDependTaskListDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FindDependTaskListDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FindDependTaskListDs", params, headers=headers)
            response = json.loads(body)
            model = models.FindDependTaskListDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FindDependTaskListsDs(self, request):
        """批量拉取下游依赖的任务列表Ds

        :param request: Request instance for FindDependTaskListsDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FindDependTaskListsDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FindDependTaskListsDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FindDependTaskListsDs", params, headers=headers)
            response = json.loads(body)
            model = models.FindDependTaskListsDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FindFuzzyTasksDs(self, request):
        """编排空间-根据项目名称和任务名称模糊查询所有任务

        :param request: Request instance for FindFuzzyTasksDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FindFuzzyTasksDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FindFuzzyTasksDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FindFuzzyTasksDs", params, headers=headers)
            response = json.loads(body)
            model = models.FindFuzzyTasksDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FindTaskByRemotePath(self, request):
        """远端路径寻找任务

        :param request: Request instance for FindTaskByRemotePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FindTaskByRemotePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FindTaskByRemotePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FindTaskByRemotePath", params, headers=headers)
            response = json.loads(body)
            model = models.FindTaskByRemotePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForceSucInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量置成功

        :param request: Request instance for ForceSucInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ForceSucInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ForceSucInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForceSucInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ForceSucInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForceSucScheduleInstances(self, request):
        """实例强制成功

        :param request: Request instance for ForceSucScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ForceSucScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ForceSucScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForceSucScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ForceSucScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeOpsTasks(self, request):
        """任务运维-批量冻结任务

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


    def FreezeTasks(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量冻结任务

        :param request: Request instance for FreezeTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeTasksByMultiWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        基于多个工作流进行批量冻结任务操作

        :param request: Request instance for FreezeTasksByMultiWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByMultiWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByMultiWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasksByMultiWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeTasksByMultiWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeTasksByWorkflowIds(self, request):
        """暂停工作流下的所有任务

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
        """生成建hive表的sql

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


    def GetAdvanceRunParams(self, request):
        """获取高级运行参数

        :param request: Request instance for GetAdvanceRunParams.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetAdvanceRunParamsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetAdvanceRunParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAdvanceRunParams", params, headers=headers)
            response = json.loads(body)
            model = models.GetAdvanceRunParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetBatchDetailErrorLog(self, request):
        """获取批量操作错误日志

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
        """获取cos token

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
        """开发空间-获取数据开发脚本信息

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


    def GetIntegrationNodeColumnSchema(self, request):
        """提取数据集成节点字段Schema

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


    def GetLatestAnalyseInfo(self, request):
        """开发空间获取最近一次测试运行记录信息

        :param request: Request instance for GetLatestAnalyseInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetLatestAnalyseInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetLatestAnalyseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLatestAnalyseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetLatestAnalyseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLatestTestRunInfo(self, request):
        """编排空间获取最近一次测试运行记录信息

        :param request: Request instance for GetLatestTestRunInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetLatestTestRunInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetLatestTestRunInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLatestTestRunInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetLatestTestRunInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOfflineDIInstanceList(self, request):
        """获取离线任务实例列表(新)

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
        """获取离线任务实例

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


    def GetPathTrees(self, request):
        """回收站脚本文件目录树

        :param request: Request instance for GetPathTrees.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetPathTreesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetPathTreesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPathTrees", params, headers=headers)
            response = json.loads(body)
            model = models.GetPathTreesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceCosPath(self, request):
        """资源管理-获取资源上传的可用 cos 路径

        :param request: Request instance for GetResourceCosPath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetResourceCosPathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetResourceCosPathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceCosPath", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceCosPathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourcePathTree(self, request):
        """资源管理-拉取资源目录树

        :param request: Request instance for GetResourcePathTree.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetResourcePathTreeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetResourcePathTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourcePathTree", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourcePathTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRunSonListDs(self, request):
        """获取工作流运行任务下游Ds

        :param request: Request instance for GetRunSonListDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetRunSonListDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetRunSonListDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRunSonListDs", params, headers=headers)
            response = json.loads(body)
            model = models.GetRunSonListDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTestRunTaskInstancesStatusInfo(self, request):
        """获取调试任务实例状态信息

        :param request: Request instance for GetTestRunTaskInstancesStatusInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetTestRunTaskInstancesStatusInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetTestRunTaskInstancesStatusInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTestRunTaskInstancesStatusInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetTestRunTaskInstancesStatusInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HeartBeat(self, request):
        """协同编辑资源锁心跳

        :param request: Request instance for HeartBeat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.HeartBeatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.HeartBeatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HeartBeat", params, headers=headers)
            response = json.loads(body)
            model = models.HeartBeatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportDsEvent(self, request):
        """事件管理-导入事件

        :param request: Request instance for ImportDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ImportDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportFiles(self, request):
        """批量导入文件

        :param request: Request instance for ImportFiles.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportFilesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ImportFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportOfflineTask(self, request):
        """异步导入集成任务

        :param request: Request instance for ImportOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.ImportOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportProjectParamDs(self, request):
        """导入项目参数

        :param request: Request instance for ImportProjectParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportProjectParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportProjectParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportProjectParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.ImportProjectParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportTableData(self, request):
        """创建数据表：HIVE

        :param request: Request instance for ImportTableData.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportTableDataRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportTableDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportTableData", params, headers=headers)
            response = json.loads(body)
            model = models.ImportTableDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportWorkflowXml(self, request):
        """工作流导入（XML）

        :param request: Request instance for ImportWorkflowXml.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportWorkflowXmlRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportWorkflowXmlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportWorkflowXml", params, headers=headers)
            response = json.loads(body)
            model = models.ImportWorkflowXmlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportWorkflowZip(self, request):
        """工作流导入（ZIP）

        :param request: Request instance for ImportWorkflowZip.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ImportWorkflowZipRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ImportWorkflowZipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportWorkflowZip", params, headers=headers)
            response = json.loads(body)
            model = models.ImportWorkflowZipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def JudgeResourceFile(self, request):
        """资源管理-判断资源文件是否存在

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


    def JudgeTaskListenEvent(self, request):
        """任务是否存在监听事件

        :param request: Request instance for JudgeTaskListenEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.JudgeTaskListenEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.JudgeTaskListenEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("JudgeTaskListenEvent", params, headers=headers)
            response = json.loads(body)
            model = models.JudgeTaskListenEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量终止操作

        :param request: Request instance for KillInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillInstances", params, headers=headers)
            response = json.loads(body)
            model = models.KillInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillOpsMakePlanInstances(self, request):
        """按补录计划批量终止实例。

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
        """批量kill实例

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


    def KillTasksTestRun(self, request):
        """停止试运行任务（多个）

        :param request: Request instance for KillTasksTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillTasksTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillTasksTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillTasksTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.KillTasksTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListBatchDetail(self, request):
        """获取操作详情列表

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


    def ListBatchJob(self, request):
        """获取操作历史列表

        :param request: Request instance for ListBatchJob.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ListBatchJobRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ListBatchJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListBatchJob", params, headers=headers)
            response = json.loads(body)
            model = models.ListBatchJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockIntegrationTask(self, request):
        """锁定集成任务

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


    def MakeUpOpsTasks(self, request):
        """任务批量补录，调度状态任务才可以补录；

        :param request: Request instance for MakeUpOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.MakeUpOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MakeUpTasksByWorkflow(self, request):
        """工作流补数据

        :param request: Request instance for MakeUpTasksByWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksByWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksByWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpTasksByWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.MakeUpTasksByWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MakeUpTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        任务批量补录，调度状态任务才可以补录；



        :param request: Request instance for MakeUpTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.MakeUpTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MakeUpWorkflowNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        工作流下所有任务的补录

        :param request: Request instance for MakeUpWorkflowNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpWorkflowNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpWorkflowNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpWorkflowNew", params, headers=headers)
            response = json.loads(body)
            model = models.MakeUpWorkflowNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApproveStatus(self, request):
        """修改审批单状态

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


    def ModifyBaselineAlarmStatus(self, request):
        """编辑基线告警状态

        :param request: Request instance for ModifyBaselineAlarmStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyBaselineAlarmStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyBaselineAlarmStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineAlarmStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineAlarmStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineTaskAlarmStatus(self, request):
        """编辑基线实例中任务告警状态

        :param request: Request instance for ModifyBaselineTaskAlarmStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyBaselineTaskAlarmStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyBaselineTaskAlarmStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineTaskAlarmStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineTaskAlarmStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataSource(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        修改数据源

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
        """质量报告-修改维度权限

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
        """数据开发模块-文件夹更新

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
        """更新规则组执行策略

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


    def ModifyFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        文件夹更新

        :param request: Request instance for ModifyFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFolder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIntegrationNode(self, request):
        """更新集成节点

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
        """更新集成任务

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
        """更新监控状态

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


    def ModifyRule(self, request):
        """更新质量规则接口

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
        """更新规则组订阅信息

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
        """编辑规则模板

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
        """修改任务告警规则

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


    def ModifyTaskFolder(self, request):
        """编排空间-工作流-创建任务文件夹

        :param request: Request instance for ModifyTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新任务

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
        """更新任务Ds

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        添加父任务依赖

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
        """添加父任务依赖

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
        """重命名任务（任务编辑）

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        修改任务脚本

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


    def ModifyTaskScriptDs(self, request):
        """修改任务脚本Ds

        :param request: Request instance for ModifyTaskScriptDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskScriptDs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskScriptDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkflowInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新工作流

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新工作流调度

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


    def MoveFile(self, request):
        """移动文件

        :param request: Request instance for MoveFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MoveFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MoveFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveFile", params, headers=headers)
            response = json.loads(body)
            model = models.MoveFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveTasksToFolder(self, request):
        """编排空间-工作流-移动任务到工作流文件夹

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


    def PreviewDataTableCsv(self, request):
        """库表管理-新建数据表-csv预览，最多支持500行预览

        :param request: Request instance for PreviewDataTableCsv.
        :type request: :class:`tencentcloud.wedata.v20210820.models.PreviewDataTableCsvRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.PreviewDataTableCsvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewDataTableCsv", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewDataTableCsvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryWorkflowVersion(self, request):
        """查询工作流版本信息

        :param request: Request instance for QueryWorkflowVersion.
        :type request: :class:`tencentcloud.wedata.v20210820.models.QueryWorkflowVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.QueryWorkflowVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryWorkflowVersion", params, headers=headers)
            response = json.loads(body)
            model = models.QueryWorkflowVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterDsEvent(self, request):
        """注册事件

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
        """注册事件监听者

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


    def RegisterDsEventPublisher(self, request):
        """注册事件发布者

        :param request: Request instance for RegisterDsEventPublisher.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterDsEventPublisherRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterDsEventPublisherResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterDsEventPublisher", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterDsEventPublisherResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterEvent(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        注册事件

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        注册事件监听器

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


    def ReleaseLock(self, request):
        """释放协同编辑资源锁

        :param request: Request instance for ReleaseLock.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ReleaseLockRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ReleaseLockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseLock", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseLockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWorkflowDs(self, request):
        """删除编排空间工作流

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


    def RenameFile(self, request):
        """重命名文件

        :param request: Request instance for RenameFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenameFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenameFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameFile", params, headers=headers)
            response = json.loads(body)
            model = models.RenameFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameResource(self, request):
        """资源管理-重命名资源

        :param request: Request instance for RenameResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenameResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenameResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameResource", params, headers=headers)
            response = json.loads(body)
            model = models.RenameResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameResourceFile(self, request):
        """资源管理-重命名资源文件

        :param request: Request instance for RenameResourceFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenameResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenameResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.RenameResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameResourcePath(self, request):
        """资源管理-重命名资源目录

        :param request: Request instance for RenameResourcePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenameResourcePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenameResourcePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameResourcePath", params, headers=headers)
            response = json.loads(body)
            model = models.RenameResourcePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameTaskDs(self, request):
        """RenameTaskDs

        :param request: Request instance for RenameTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenameTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenameTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.RenameTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewWorkflowDs(self, request):
        """更新工作流

        :param request: Request instance for RenewWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.RenewWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewWorkflowFolderDs(self, request):
        """移动文件夹

        :param request: Request instance for RenewWorkflowFolderDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowFolderDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RenewWorkflowFolderDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewWorkflowFolderDs", params, headers=headers)
            response = json.loads(body)
            model = models.RenewWorkflowFolderDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewWorkflowOwnerDs(self, request):
        """批量更新工作流下任务责任人

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
        """更新工作流下任务调度信息

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


    def ReplaceProjectParamVersionDs(self, request):
        """替换项目参数历史版本

        :param request: Request instance for ReplaceProjectParamVersionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ReplaceProjectParamVersionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ReplaceProjectParamVersionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceProjectParamVersionDs", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceProjectParamVersionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量重跑

        :param request: Request instance for RerunInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RerunInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RerunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RerunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunOpsMakePlanInstances(self, request):
        """按补录计划批量重跑/选择补录计划→补录任务→补录实例，点击重跑

        :param request: Request instance for RerunOpsMakePlanInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RerunOpsMakePlanInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RerunOpsMakePlanInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunOpsMakePlanInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RerunOpsMakePlanInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunScheduleInstances(self, request):
        """实例批量重跑

        :param request: Request instance for RerunScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RerunScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RerunScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RerunScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInLongAgent(self, request):
        """重启采集器

        :param request: Request instance for RestartInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RestartInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RestartInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreRecycleTask(self, request):
        """还原任务

        :param request: Request instance for RestoreRecycleTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RestoreRecycleTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RestoreRecycleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreRecycleTask", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreRecycleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeIntegrationTask(self, request):
        """继续集成任务

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
        """抢占锁定集成任务

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


    def RollbackCustomFunctionVersion(self, request):
        """回滚自定义函数版本

        :param request: Request instance for RollbackCustomFunctionVersion.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RollbackCustomFunctionVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RollbackCustomFunctionVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackCustomFunctionVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackCustomFunctionVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunForceSucScheduleInstances(self, request):
        """实例强制成功

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
        """实例批量重跑

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


    def RunTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        运行任务

        :param request: Request instance for RunTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunTask", params, headers=headers)
            response = json.loads(body)
            model = models.RunTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunTasksByMultiWorkflow(self, request):
        """批量启动工作流

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
        """保存用户自定义函数

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


    def SavePositionsDs(self, request):
        """批量保存任务位置

        :param request: Request instance for SavePositionsDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SavePositionsDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SavePositionsDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SavePositionsDs", params, headers=headers)
            response = json.loads(body)
            model = models.SavePositionsDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScriptUsedByOtherTaskDs(self, request):
        """判断脚本文件是否被任务列表所引用

        :param request: Request instance for ScriptUsedByOtherTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ScriptUsedByOtherTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ScriptUsedByOtherTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScriptUsedByOtherTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.ScriptUsedByOtherTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTaskAlarmNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
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
        """启动集成任务

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


    def StopAdhocTask(self, request):
        """即席分析终止任务接口

        :param request: Request instance for StopAdhocTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StopAdhocTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StopAdhocTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAdhocTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopAdhocTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBaseline(self, request):
        """提交基线

        :param request: Request instance for StopBaseline.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StopBaselineRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StopBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.StopBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopIntegrationTask(self, request):
        """停止集成任务

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


    def StopTestRun(self, request):
        """终止etl测试运行任务

        :param request: Request instance for StopTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StopTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StopTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.StopTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitBaseline(self, request):
        """提交基线

        :param request: Request instance for SubmitBaseline.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitBaselineRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitBatchTestRun(self, request):
        """批量提交etl测试运行任务

        :param request: Request instance for SubmitBatchTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitBatchTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitBatchTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitBatchTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitBatchTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitCustomFunction(self, request):
        """提交自定义函数

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


    def SubmitIntegrationTask(self, request):
        """即席分析提交数据集成任务

        :param request: Request instance for SubmitIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitPySparkTask(self, request):
        """即席分析提交PySpark任务

        :param request: Request instance for SubmitPySparkTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitPySparkTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitPySparkTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitPySparkTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitPySparkTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitPythonTask(self, request):
        """即席分析提交PYTHON任务

        :param request: Request instance for SubmitPythonTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitPythonTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitPythonTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitPythonTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitPythonTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitShellTask(self, request):
        """即席分析提交SHELL任务

        :param request: Request instance for SubmitShellTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitShellTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitShellTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitShellTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitShellTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitSqlTask(self, request):
        """即席分析提交SQL任务

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        提交任务

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
        """无

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


    def SubmitTestRun(self, request):
        """提交etl测试运行任务

        :param request: Request instance for SubmitTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        提交工作流

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
        """暂停集成任务

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
        """查询Inlong manager日志

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
        """事件管理-触发事件

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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        触发事件

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


    def UnlockIntegrationTask(self, request):
        """解锁集成任务

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


    def UpdateBatchTaskAdvancedSettings(self, request):
        """批量更新高级设置

        :param request: Request instance for UpdateBatchTaskAdvancedSettings.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskAdvancedSettingsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskAdvancedSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskAdvancedSettings", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskAdvancedSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBatchTaskDatasource(self, request):
        """批量更新数据源

        :param request: Request instance for UpdateBatchTaskDatasource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskDatasourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBatchTaskInCharge(self, request):
        """批量修改责任人

        :param request: Request instance for UpdateBatchTaskInCharge.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskInChargeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskInChargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskInCharge", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskInChargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBatchTaskParameter(self, request):
        """批量修改参数

        :param request: Request instance for UpdateBatchTaskParameter.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskParameterRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskParameterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskParameter", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskParameterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBatchTaskParams(self, request):
        """批量更新调度参数

        :param request: Request instance for UpdateBatchTaskParams.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskParamsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskParams", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBatchTaskResourceGroup(self, request):
        """批量修改资源组

        :param request: Request instance for UpdateBatchTaskResourceGroup.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskResourceGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBatchTaskSchedule(self, request):
        """批量更新调度周期设置

        :param request: Request instance for UpdateBatchTaskSchedule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskScheduleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateBatchTaskScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBatchTaskSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBatchTaskScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDsEvent(self, request):
        """更新事件

        :param request: Request instance for UpdateDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEventListener(self, request):
        """更新事件监听

        :param request: Request instance for UpdateEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateInLongAgent(self, request):
        """更新采集器

        :param request: Request instance for UpdateInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTaskDs(self, request):
        """更新任务Ds

        :param request: Request instance for UpdateTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflowInfo(self, request):
        """<p style="color:red;">[该接口为 ds 中开发]</p>
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
        """修改工作流责任人

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


    def UploadAdvanceRunParams(self, request):
        """保存高级运行用户自定义参数

        :param request: Request instance for UploadAdvanceRunParams.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UploadAdvanceRunParamsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UploadAdvanceRunParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadAdvanceRunParams", params, headers=headers)
            response = json.loads(body)
            model = models.UploadAdvanceRunParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadContent(self, request):
        """保存任务信息

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


    def UploadFilesDs(self, request):
        """文件上传需要先获取文件上传所需要的秘钥，文件位置等信息，因为文件名字可能会出现冲突，所以需要传入将要写入的文件，如果检测到文件名冲突，WeData 后端会在文件名上加入随机字符串。

        :param request: Request instance for UploadFilesDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UploadFilesDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UploadFilesDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFilesDs", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFilesDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadResource(self, request):
        """资源管理-上传资源

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