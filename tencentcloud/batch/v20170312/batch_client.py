# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def CreateComputeEnv(self, request):
        """用于创建计算环境

        :param request: 调用CreateComputeEnv所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateComputeEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTaskTemplate(self, request):
        """用于创建任务模板

        :param request: 调用CreateTaskTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteComputeEnv(self, request):
        """用于删除计算环境

        :param request: 调用DeleteComputeEnv所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteComputeEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteJob(self, request):
        """用于删除作业记录。
        删除作业的效果相当于删除作业相关的所有信息。删除成功后，作业相关的所有信息都无法查询。
        待删除的作业必须处于完结状态，且其内部包含的所有任务实例也必须处于完结状态，否则会禁止操作。完结状态，是指处于 SUCCEED 或 FAILED 状态。

        :param request: 调用DeleteJob所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTaskTemplates(self, request):
        """用于删除任务模板信息

        :param request: 调用DeleteTaskTemplates所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTaskTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTaskTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAvailableCvmInstanceTypes(self, request):
        """查看可用的CVM机型配置信息

        :param request: 调用DescribeAvailableCvmInstanceTypes所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableCvmInstanceTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableCvmInstanceTypesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnv(self, request):
        """用于查询计算环境的详细信息

        :param request: 调用DescribeComputeEnv所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvActivities(self, request):
        """用于查询计算环境的活动信息

        :param request: 调用DescribeComputeEnvActivities所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvActivitiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvCreateInfo(self, request):
        """查看计算环境的创建信息。

        :param request: 调用DescribeComputeEnvCreateInfo所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvCreateInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvCreateInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvCreateInfos(self, request):
        """用于查看计算环境创建信息列表，包括名称、描述、类型、环境参数、通知及期望节点数等。

        :param request: 调用DescribeComputeEnvCreateInfos所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvCreateInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvCreateInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComputeEnvs(self, request):
        """用于查看计算环境列表

        :param request: 调用DescribeComputeEnvs所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCvmZoneInstanceConfigInfos(self, request):
        """获取批量计算可用区机型配置信息

        :param request: 调用DescribeCvmZoneInstanceConfigInfos所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCvmZoneInstanceConfigInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCvmZoneInstanceConfigInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceCategories(self, request):
        """目前对CVM现有实例族划分为四类，每一类包含若干实例族。该接口用于查询实例分类信息。

        :param request: 调用DescribeInstanceCategories所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceCategories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceCategoriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJob(self, request):
        """用于查看一个作业的详细信息，包括内部任务（Task）和依赖（Dependence）信息。

        :param request: 调用DescribeJob所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJobSubmitInfo(self, request):
        """用于查询指定作业的提交信息，其返回内容包括 JobId 和 SubmitJob 接口中作为输入参数的作业提交信息

        :param request: 调用DescribeJobSubmitInfo所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJobSubmitInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobSubmitInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJobs(self, request):
        """用于查询若干个作业的概览信息

        :param request: 调用DescribeJobs所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTask(self, request):
        """用于查询指定任务的详细信息，包括任务内部的任务实例信息。

        :param request: 调用DescribeTask所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskLogs(self, request):
        """用于获取任务多个实例标准输出和标准错误日志。

        :param request: 调用DescribeTaskLogs所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskTemplates(self, request):
        """用于查询任务模板信息

        :param request: 调用DescribeTaskTemplates所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyComputeEnv(self, request):
        """用于修改计算环境属性

        :param request: 调用ModifyComputeEnv所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyComputeEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskTemplate(self, request):
        """用于修改任务模板

        :param request: 调用ModifyTaskTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTaskTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RetryJobs(self, request):
        """用于重试作业中失败的任务实例。
        当且仅当作业处于“FAILED”状态，支持重试操作。重试操作成功后，作业会按照“DAG”中指定的任务依赖关系，依次重试各个任务中失败的任务实例。任务实例的历史信息将被重置，如同首次运行一样，参与后续的调度和执行。

        :param request: 调用RetryJobs所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.RetryJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.RetryJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RetryJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RetryJobsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitJob(self, request):
        """用于提交一个作业

        :param request: 调用SubmitJob所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.SubmitJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.SubmitJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateComputeNode(self, request):
        """用于销毁计算节点。
        对于状态为CREATED、CREATION_FAILED、RUNNING和ABNORMAL的节点，允许销毁处理。

        :param request: 调用TerminateComputeNode所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateComputeNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateComputeNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateComputeNodes(self, request):
        """用于批量销毁计算节点，不允许重复销毁同一个节点。

        :param request: 调用TerminateComputeNodes所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateComputeNodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateComputeNodesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateJob(self, request):
        """用于终止作业。
        当作业处于“SUBMITTED”状态时，禁止终止操作；当作业处于“SUCCEED”状态时，终止操作不会生效。
        终止作业是一个异步过程。整个终止过程的耗时和任务总数成正比。终止的效果相当于所含的所有任务实例进行TerminateTaskInstance操作。具体效果和用法可参考TerminateTaskInstance。

        :param request: 调用TerminateJob所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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

        :param request: 调用TerminateTaskInstance所需参数的结构体。
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateTaskInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTaskInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)