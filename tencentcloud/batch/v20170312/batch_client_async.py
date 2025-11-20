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
from tencentcloud.batch.v20170312 import models
from typing import Dict


class BatchClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'batch.tencentcloudapi.com'
    _service = 'batch'

    async def AttachInstances(
            self,
            request: models.AttachInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachInstancesResponse:
        """
        此接口可将已存在实例添加到计算环境中。
        实例需要满足如下条件：<br/>
        1.实例不在批量计算系统中。<br/>
        2.实例状态要求处于运行中。<br/>
        3.支持预付费实例，按小时后付费实例，专享子机实例。不支持竞价实例。<br/>

        此接口会将加入到计算环境中的实例重设UserData和重装操作系统。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComputeEnv(
            self,
            request: models.CreateComputeEnvRequest,
            opts: Dict = None,
    ) -> models.CreateComputeEnvResponse:
        """
        用于创建计算环境
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskTemplate(
            self,
            request: models.CreateTaskTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTaskTemplateResponse:
        """
        用于创建任务模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteComputeEnv(
            self,
            request: models.DeleteComputeEnvRequest,
            opts: Dict = None,
    ) -> models.DeleteComputeEnvResponse:
        """
        用于删除计算环境
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJob(
            self,
            request: models.DeleteJobRequest,
            opts: Dict = None,
    ) -> models.DeleteJobResponse:
        """
        用于删除作业记录。
        删除作业的效果相当于删除作业相关的所有信息。删除成功后，作业相关的所有信息都无法查询。
        待删除的作业必须处于完结状态，且其内部包含的所有任务实例也必须处于完结状态，否则会禁止操作。完结状态，是指处于 SUCCEED 或 FAILED 状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskTemplates(
            self,
            request: models.DeleteTaskTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskTemplatesResponse:
        """
        用于删除任务模板信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableCvmInstanceTypes(
            self,
            request: models.DescribeAvailableCvmInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableCvmInstanceTypesResponse:
        """
        查看可用的CVM机型配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableCvmInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableCvmInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnv(
            self,
            request: models.DescribeComputeEnvRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvResponse:
        """
        用于查询计算环境的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvActivities(
            self,
            request: models.DescribeComputeEnvActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvActivitiesResponse:
        """
        用于查询计算环境的活动信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvCreateInfo(
            self,
            request: models.DescribeComputeEnvCreateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvCreateInfoResponse:
        """
        查看计算环境的创建信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvCreateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvCreateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvCreateInfos(
            self,
            request: models.DescribeComputeEnvCreateInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvCreateInfosResponse:
        """
        用于查看计算环境创建信息列表，包括名称、描述、类型、环境参数、通知及期望节点数等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvCreateInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvCreateInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvs(
            self,
            request: models.DescribeComputeEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvsResponse:
        """
        用于查看计算环境列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCvmZoneInstanceConfigInfos(
            self,
            request: models.DescribeCvmZoneInstanceConfigInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCvmZoneInstanceConfigInfosResponse:
        """
        获取批量计算可用区机型配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCvmZoneInstanceConfigInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCvmZoneInstanceConfigInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceCategories(
            self,
            request: models.DescribeInstanceCategoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceCategoriesResponse:
        """
        目前对CVM现有实例族分类，每一类包含若干实例族。该接口用于查询实例分类信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceCategories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceCategoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJob(
            self,
            request: models.DescribeJobRequest,
            opts: Dict = None,
    ) -> models.DescribeJobResponse:
        """
        用于查看一个作业的详细信息，包括内部任务（Task）和依赖（Dependence）信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobMonitorData(
            self,
            request: models.DescribeJobMonitorDataRequest,
            opts: Dict = None,
    ) -> models.DescribeJobMonitorDataResponse:
        """
        查询作业任务实例的资源使用监控信息。当前只支持查询弹性节点任务并且Job未删除；暂不支持计算环境类任务；该接口只支持查询作业实例时间范围之内的资源使用情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobSubmitInfo(
            self,
            request: models.DescribeJobSubmitInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJobSubmitInfoResponse:
        """
        用于查询指定作业的提交信息，其返回内容包括 JobId 和 SubmitJob 接口中作为输入参数的作业提交信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobSubmitInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobSubmitInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        用于查询若干个作业的概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        用于查询指定任务的详细信息，包括任务内部的任务实例信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogs(
            self,
            request: models.DescribeTaskLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogsResponse:
        """
        用于获取任务多个实例标准输出和标准错误日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskTemplates(
            self,
            request: models.DescribeTaskTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskTemplatesResponse:
        """
        用于查询任务模板信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachInstances(
            self,
            request: models.DetachInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachInstancesResponse:
        """
        将添加到计算环境中的实例从计算环境中移出。若是由批量计算自动创建的计算节点实例则不允许移出。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyComputeEnv(
            self,
            request: models.ModifyComputeEnvRequest,
            opts: Dict = None,
    ) -> models.ModifyComputeEnvResponse:
        """
        用于修改计算环境属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskTemplate(
            self,
            request: models.ModifyTaskTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskTemplateResponse:
        """
        用于修改任务模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryJobs(
            self,
            request: models.RetryJobsRequest,
            opts: Dict = None,
    ) -> models.RetryJobsResponse:
        """
        用于重试作业中失败的任务实例。
        仅当作业处于“FAILED”状态，支持重试操作。重试操作成功后，作业会按照有向无环图中指定的任务依赖关系，依次重试各个任务中失败的任务实例。任务实例的历史信息将被重置，如同首次运行一样，参与后续的调度和执行。
        """
        
        kwargs = {}
        kwargs["action"] = "RetryJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitJob(
            self,
            request: models.SubmitJobRequest,
            opts: Dict = None,
    ) -> models.SubmitJobResponse:
        """
        用于提交一个作业
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateComputeNode(
            self,
            request: models.TerminateComputeNodeRequest,
            opts: Dict = None,
    ) -> models.TerminateComputeNodeResponse:
        """
        用于销毁计算节点。
        对于状态为CREATED、CREATION_FAILED、RUNNING和ABNORMAL的节点，允许销毁处理。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateComputeNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateComputeNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateComputeNodes(
            self,
            request: models.TerminateComputeNodesRequest,
            opts: Dict = None,
    ) -> models.TerminateComputeNodesResponse:
        """
        用于批量销毁计算节点，不允许重复销毁同一个节点。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateComputeNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateComputeNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateJob(
            self,
            request: models.TerminateJobRequest,
            opts: Dict = None,
    ) -> models.TerminateJobResponse:
        """
        用于终止作业。
        当作业处于“SUBMITTED”状态时，禁止终止操作；当作业处于“SUCCEED”状态时，终止操作不会生效。
        终止作业是一个异步过程。整个终止过程的耗时和任务总数成正比。终止的效果相当于所含的所有任务实例进行[TerminateTaskInstance](https://cloud.tencent.com/document/product/599/15908)操作。具体效果和用法可参考[TerminateTaskInstance](https://cloud.tencent.com/document/product/599/15908)。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateTaskInstance(
            self,
            request: models.TerminateTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateTaskInstanceResponse:
        """
        用于终止任务实例。
        对于状态已经为“SUCCEED”和“FAILED”的任务实例，不做处理。
        对于状态为“SUBMITTED”、“PENDING”、“RUNNABLE”的任务实例，状态将置为“FAILED”状态。
        对于状态为“STARTING”、“RUNNING”、“FAILED_INTERRUPTED”的任务实例，区分两种情况：如果未显示指定计算环境，会先销毁CVM服务器，然后将状态置为“FAILED”，具有一定耗时；如果指定了计算环境EnvId，任务实例状态置为“FAILED”，并重启执行该任务的CVM服务器，具有一定的耗时。
        对于状态为“FAILED_INTERRUPTED”的任务实例，终止操作实际成功之后，相关资源和配额才会释放。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)