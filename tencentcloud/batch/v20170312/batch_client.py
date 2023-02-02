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
from tencentcloud.batch.v20170312 import models


class BatchClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'batch.tencentcloudapi.com'
    _service = 'batch'


    def AttachInstances(self, request):
        """此接口可将已存在实例添加到计算环境中。
        实例需要满足如下条件：<br/>
        1.实例不在批量计算系统中。<br/>
        2.实例状态要求处于运行中。<br/>
        3.支持预付费实例，按小时后付费实例，专享子机实例。不支持竞价实例。<br/>

        此接口会将加入到计算环境中的实例重设UserData和重装操作系统。

        :param request: Request instance for AttachInstances.
        :type request: :class:`tencentcloud.batch.v20170312.models.AttachInstancesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateComputeEnv(self, request):
        """用于创建计算环境

        :param request: Request instance for CreateComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCpmComputeEnv(self, request):
        """创建黑石计算环境

        :param request: Request instance for CreateCpmComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateCpmComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateCpmComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCpmComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCpmComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTaskTemplate(self, request):
        """用于创建任务模板

        :param request: Request instance for CreateTaskTemplate.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteComputeEnv(self, request):
        """用于删除计算环境

        :param request: Request instance for DeleteComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteJob(self, request):
        """用于删除作业记录。
        删除作业的效果相当于删除作业相关的所有信息。删除成功后，作业相关的所有信息都无法查询。
        待删除的作业必须处于完结状态，且其内部包含的所有任务实例也必须处于完结状态，否则会禁止操作。完结状态，是指处于 SUCCEED 或 FAILED 状态。

        :param request: Request instance for DeleteJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJob", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTaskTemplates(self, request):
        """用于删除任务模板信息

        :param request: Request instance for DeleteTaskTemplates.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAvailableCvmInstanceTypes(self, request):
        """查看可用的CVM机型配置信息

        :param request: Request instance for DescribeAvailableCvmInstanceTypes.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableCvmInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableCvmInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnv(self, request):
        """用于查询计算环境的详细信息

        :param request: Request instance for DescribeComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvActivities(self, request):
        """用于查询计算环境的活动信息

        :param request: Request instance for DescribeComputeEnvActivities.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvCreateInfo(self, request):
        """查看计算环境的创建信息。

        :param request: Request instance for DescribeComputeEnvCreateInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvCreateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvCreateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvCreateInfos(self, request):
        """用于查看计算环境创建信息列表，包括名称、描述、类型、环境参数、通知及期望节点数等。

        :param request: Request instance for DescribeComputeEnvCreateInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvCreateInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvCreateInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvs(self, request):
        """用于查看计算环境列表

        :param request: Request instance for DescribeComputeEnvs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCpmOsInfo(self, request):
        """创建黑石计算环境时，查询批量计算环境支持的黑石操作系统信息

        :param request: Request instance for DescribeCpmOsInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeCpmOsInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeCpmOsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCpmOsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCpmOsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCvmZoneInstanceConfigInfos(self, request):
        """获取批量计算可用区机型配置信息

        :param request: Request instance for DescribeCvmZoneInstanceConfigInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmZoneInstanceConfigInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCvmZoneInstanceConfigInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceCategories(self, request):
        """目前对CVM现有实例族分类，每一类包含若干实例族。该接口用于查询实例分类信息。

        :param request: Request instance for DescribeInstanceCategories.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceCategories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceCategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJob(self, request):
        """用于查看一个作业的详细信息，包括内部任务（Task）和依赖（Dependence）信息。

        :param request: Request instance for DescribeJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJobSubmitInfo(self, request):
        """用于查询指定作业的提交信息，其返回内容包括 JobId 和 SubmitJob 接口中作为输入参数的作业提交信息

        :param request: Request instance for DescribeJobSubmitInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobSubmitInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobSubmitInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJobs(self, request):
        """用于查询若干个作业的概览信息

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTask(self, request):
        """用于查询指定任务的详细信息，包括任务内部的任务实例信息。

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskLogs(self, request):
        """用于获取任务多个实例标准输出和标准错误日志。

        :param request: Request instance for DescribeTaskLogs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskTemplates(self, request):
        """用于查询任务模板信息

        :param request: Request instance for DescribeTaskTemplates.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DetachInstances(self, request):
        """将添加到计算环境中的实例从计算环境中移出。若是由批量计算自动创建的计算节点实例则不允许移出。

        :param request: Request instance for DetachInstances.
        :type request: :class:`tencentcloud.batch.v20170312.models.DetachInstancesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyComputeEnv(self, request):
        """用于修改计算环境属性

        :param request: Request instance for ModifyComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskTemplate(self, request):
        """用于修改任务模板

        :param request: Request instance for ModifyTaskTemplate.
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RetryJobs(self, request):
        """用于重试作业中失败的任务实例。
        当且仅当作业处于“FAILED”状态，支持重试操作。重试操作成功后，作业会按照“DAG”中指定的任务依赖关系，依次重试各个任务中失败的任务实例。任务实例的历史信息将被重置，如同首次运行一样，参与后续的调度和执行。

        :param request: Request instance for RetryJobs.
        :type request: :class:`tencentcloud.batch.v20170312.models.RetryJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.RetryJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryJobs", params, headers=headers)
            response = json.loads(body)
            model = models.RetryJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitJob(self, request):
        """用于提交一个作业

        :param request: Request instance for SubmitJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.SubmitJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.SubmitJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateComputeNode(self, request):
        """用于销毁计算节点。
        对于状态为CREATED、CREATION_FAILED、RUNNING和ABNORMAL的节点，允许销毁处理。

        :param request: Request instance for TerminateComputeNode.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateComputeNode", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateComputeNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateComputeNodes(self, request):
        """用于批量销毁计算节点，不允许重复销毁同一个节点。

        :param request: Request instance for TerminateComputeNodes.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateComputeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateComputeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateJob(self, request):
        """用于终止作业。
        当作业处于“SUBMITTED”状态时，禁止终止操作；当作业处于“SUCCEED”状态时，终止操作不会生效。
        终止作业是一个异步过程。整个终止过程的耗时和任务总数成正比。终止的效果相当于所含的所有任务实例进行TerminateTaskInstance操作。具体效果和用法可参考TerminateTaskInstance。

        :param request: Request instance for TerminateJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateJob", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateTaskInstance(self, request):
        """用于终止任务实例。
        对于状态已经为“SUCCEED”和“FAILED”的任务实例，不做处理。
        对于状态为“SUBMITTED”、“PENDING”、“RUNNABLE”的任务实例，状态将置为“FAILED”状态。
        对于状态为“STARTING”、“RUNNING”、“FAILED_INTERRUPTED”的任务实例，分区两种情况：如果未显示指定计算环境，会先销毁CVM服务器，然后将状态置为“FAILED”，具有一定耗时；如果指定了计算环境EnvId，任务实例状态置为“FAILED”，并重启执行该任务的CVM服务器，具有一定的耗时。
        对于状态为“FAILED_INTERRUPTED”的任务实例，终止操作实际成功之后，相关资源和配额才会释放。

        :param request: Request instance for TerminateTaskInstance.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)