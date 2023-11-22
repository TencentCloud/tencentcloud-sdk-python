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
from tencentcloud.cfg.v20210820 import models


class CfgClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'cfg.tencentcloudapi.com'
    _service = 'cfg'


    def CreateTaskFromTemplate(self, request):
        """从经验库创建演练

        :param request: Request instance for CreateTaskFromTemplate.
        :type request: :class:`tencentcloud.cfg.v20210820.models.CreateTaskFromTemplateRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.CreateTaskFromTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFromTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFromTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        """删除任务

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DeleteTaskResponse`

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


    def DescribeTask(self, request):
        """查询任务

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskExecuteLogs(self, request):
        """获取演练过程中的所有日志

        :param request: Request instance for DescribeTaskExecuteLogs.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskExecuteLogsRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskExecuteLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskExecuteLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskExecuteLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskList(self, request):
        """查询任务列表

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskPolicyTriggerLog(self, request):
        """获取护栏触发日志

        :param request: Request instance for DescribeTaskPolicyTriggerLog.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskPolicyTriggerLogRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskPolicyTriggerLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskPolicyTriggerLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskPolicyTriggerLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplate(self, request):
        """查询经验库

        :param request: Request instance for DescribeTemplate.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateList(self, request):
        """查询经验库列表

        :param request: Request instance for DescribeTemplateList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteTask(self, request):
        """执行任务

        :param request: Request instance for ExecuteTask.
        :type request: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteTask", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteTaskInstance(self, request):
        """触发混沌演练任务的动作，对于实例进行演练操作

        :param request: Request instance for ExecuteTaskInstance.
        :type request: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskInstanceRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskRunStatus(self, request):
        """修改任务运行状态

        :param request: Request instance for ModifyTaskRunStatus.
        :type request: :class:`tencentcloud.cfg.v20210820.models.ModifyTaskRunStatusRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ModifyTaskRunStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskRunStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskRunStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerPolicy(self, request):
        """用于触发混沌演练护栏（类型为触发和恢复2种）

        :param request: Request instance for TriggerPolicy.
        :type request: :class:`tencentcloud.cfg.v20210820.models.TriggerPolicyRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TriggerPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))