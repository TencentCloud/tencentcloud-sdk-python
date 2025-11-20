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
from tencentcloud.tione.v20211111 import models
from typing import Dict


class TioneClient(AbstractClient):
    _apiVersion = '2021-11-11'
    _endpoint = 'tione.tencentcloudapi.com'
    _service = 'tione'

    async def ChatCompletion(
            self,
            request: models.ChatCompletionRequest,
            opts: Dict = None,
    ) -> models.ChatCompletionResponse:
        """
        该接口支持与自行部署的大模型的聊天。

        使用该接口调用时需要携带腾讯云的密钥信息用于身份信息鉴权，建议通过腾讯云的云 API SDK调用，具体可以参考
        https://cloud.tencent.com/document/product/1278/85305
        """
        
        kwargs = {}
        kwargs["action"] = "ChatCompletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatCompletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataset(
            self,
            request: models.CreateDatasetRequest,
            opts: Dict = None,
    ) -> models.CreateDatasetResponse:
        """
        创建数据集
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatasetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExport(
            self,
            request: models.CreateExportRequest,
            opts: Dict = None,
    ) -> models.CreateExportResponse:
        """
        创建任务式建模训练任务，Notebook，在线服务和批量预测任务日志下载任务API
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModelService(
            self,
            request: models.CreateModelServiceRequest,
            opts: Dict = None,
    ) -> models.CreateModelServiceResponse:
        """
        用于创建、发布一个新的模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModelServiceAuthToken(
            self,
            request: models.CreateModelServiceAuthTokenRequest,
            opts: Dict = None,
    ) -> models.CreateModelServiceAuthTokenResponse:
        """
        创建一个 AuthToken
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModelServiceAuthToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelServiceAuthTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotebook(
            self,
            request: models.CreateNotebookRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookResponse:
        """
        创建Notebook
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePresignedNotebookUrl(
            self,
            request: models.CreatePresignedNotebookUrlRequest,
            opts: Dict = None,
    ) -> models.CreatePresignedNotebookUrlResponse:
        """
        生成Notebook访问链接
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePresignedNotebookUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePresignedNotebookUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrainingModel(
            self,
            request: models.CreateTrainingModelRequest,
            opts: Dict = None,
    ) -> models.CreateTrainingModelResponse:
        """
        导入模型
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrainingModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrainingModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrainingTask(
            self,
            request: models.CreateTrainingTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTrainingTaskResponse:
        """
        创建模型训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrainingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrainingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataset(
            self,
            request: models.DeleteDatasetRequest,
            opts: Dict = None,
    ) -> models.DeleteDatasetResponse:
        """
        删除数据集
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatasetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExport(
            self,
            request: models.DeleteExportRequest,
            opts: Dict = None,
    ) -> models.DeleteExportResponse:
        """
        删除任务式建模训练任务，Notebook，在线服务和批量预测任务日志导出任务API
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModelService(
            self,
            request: models.DeleteModelServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteModelServiceResponse:
        """
        根据服务id删除模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModelServiceAuthToken(
            self,
            request: models.DeleteModelServiceAuthTokenRequest,
            opts: Dict = None,
    ) -> models.DeleteModelServiceAuthTokenResponse:
        """
        删除一个 AuthToken
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModelServiceAuthToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelServiceAuthTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModelServiceGroup(
            self,
            request: models.DeleteModelServiceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteModelServiceGroupResponse:
        """
        根据服务组id删除服务组下所有模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModelServiceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelServiceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNotebook(
            self,
            request: models.DeleteNotebookRequest,
            opts: Dict = None,
    ) -> models.DeleteNotebookResponse:
        """
        删除Notebook
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNotebook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNotebookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrainingModel(
            self,
            request: models.DeleteTrainingModelRequest,
            opts: Dict = None,
    ) -> models.DeleteTrainingModelResponse:
        """
        删除模型
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrainingModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrainingModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrainingModelVersion(
            self,
            request: models.DeleteTrainingModelVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteTrainingModelVersionResponse:
        """
        删除模型版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrainingModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrainingModelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrainingTask(
            self,
            request: models.DeleteTrainingTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTrainingTaskResponse:
        """
        删除训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrainingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrainingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingResourceGroup(
            self,
            request: models.DescribeBillingResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingResourceGroupResponse:
        """
        查询资源组节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingResourceGroups(
            self,
            request: models.DescribeBillingResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingResourceGroupsResponse:
        """
        查询资源组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingResourceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingResourceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingResourceInstanceRunningJobs(
            self,
            request: models.DescribeBillingResourceInstanceRunningJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingResourceInstanceRunningJobsResponse:
        """
        查询资源组节点运行中的任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingResourceInstanceRunningJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingResourceInstanceRunningJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingSpecs(
            self,
            request: models.DescribeBillingSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingSpecsResponse:
        """
        本接口(DescribeBillingSpecs) 提供查询计费项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingSpecsPrice(
            self,
            request: models.DescribeBillingSpecsPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingSpecsPriceResponse:
        """
        本接口(DescribeBillingSpecsPrice)用于查询按量计费计费项价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingSpecsPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingSpecsPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBuildInImages(
            self,
            request: models.DescribeBuildInImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeBuildInImagesResponse:
        """
        获取内置镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBuildInImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBuildInImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatasets(
            self,
            request: models.DescribeDatasetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatasetsResponse:
        """
        查询数据集列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatasets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatasetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvents(
            self,
            request: models.DescribeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeEventsResponse:
        """
        获取任务式建模训练任务，Notebook，在线服务和批量预测任务的事件API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExport(
            self,
            request: models.DescribeExportRequest,
            opts: Dict = None,
    ) -> models.DescribeExportResponse:
        """
        查看任务式建模训练任务，Notebook，在线服务和批量预测任务日志下载任务状态API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferTemplates(
            self,
            request: models.DescribeInferTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeInferTemplatesResponse:
        """
        已废弃，收敛到统一接口

        查询推理镜像模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogs(
            self,
            request: models.DescribeLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogsResponse:
        """
        获取任务式建模训练任务，Notebook，在线服务和批量预测任务的日志API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelAccelerateTask(
            self,
            request: models.DescribeModelAccelerateTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeModelAccelerateTaskResponse:
        """
        查询模型优化任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelAccelerateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelAccelerateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelAccelerateVersions(
            self,
            request: models.DescribeModelAccelerateVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeModelAccelerateVersionsResponse:
        """
        模型加速之后的模型版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelAccelerateVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelAccelerateVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelService(
            self,
            request: models.DescribeModelServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceResponse:
        """
        查询单个服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelServiceCallInfo(
            self,
            request: models.DescribeModelServiceCallInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceCallInfoResponse:
        """
        展示服务的调用信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelServiceCallInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceCallInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelServiceGroup(
            self,
            request: models.DescribeModelServiceGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceGroupResponse:
        """
        查询单个服务组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelServiceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelServiceGroups(
            self,
            request: models.DescribeModelServiceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceGroupsResponse:
        """
        列举在线推理服务组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelServiceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelServiceHotUpdated(
            self,
            request: models.DescribeModelServiceHotUpdatedRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceHotUpdatedResponse:
        """
        用于查询模型服务能否开启热更新
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelServiceHotUpdated"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceHotUpdatedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebook(
            self,
            request: models.DescribeNotebookRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookResponse:
        """
        Notebook详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebooks(
            self,
            request: models.DescribeNotebooksRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebooksResponse:
        """
        Notebook列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebooks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebooksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlatformImages(
            self,
            request: models.DescribePlatformImagesRequest,
            opts: Dict = None,
    ) -> models.DescribePlatformImagesResponse:
        """
        查询平台镜像信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlatformImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlatformImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingModelVersion(
            self,
            request: models.DescribeTrainingModelVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingModelVersionResponse:
        """
        查询模型版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingModelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingModelVersions(
            self,
            request: models.DescribeTrainingModelVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingModelVersionsResponse:
        """
        模型版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingModelVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingModelVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingTask(
            self,
            request: models.DescribeTrainingTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingTaskResponse:
        """
        训练任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingTaskPods(
            self,
            request: models.DescribeTrainingTaskPodsRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingTaskPodsResponse:
        """
        训练任务pod列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingTaskPods"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingTaskPodsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingTasks(
            self,
            request: models.DescribeTrainingTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingTasksResponse:
        """
        训练任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModelService(
            self,
            request: models.ModifyModelServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyModelServiceResponse:
        """
        用于更新模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModelServiceAuthToken(
            self,
            request: models.ModifyModelServiceAuthTokenRequest,
            opts: Dict = None,
    ) -> models.ModifyModelServiceAuthTokenResponse:
        """
        修改一个 AuthToken
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModelServiceAuthToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModelServiceAuthTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModelServiceAuthorization(
            self,
            request: models.ModifyModelServiceAuthorizationRequest,
            opts: Dict = None,
    ) -> models.ModifyModelServiceAuthorizationResponse:
        """
        修改服务鉴权配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModelServiceAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModelServiceAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotebookTags(
            self,
            request: models.ModifyNotebookTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyNotebookTagsResponse:
        """
        修改Notebook标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotebookTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotebookTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PushTrainingMetrics(
            self,
            request: models.PushTrainingMetricsRequest,
            opts: Dict = None,
    ) -> models.PushTrainingMetricsResponse:
        """
        上报训练自定义指标
        """
        
        kwargs = {}
        kwargs["action"] = "PushTrainingMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PushTrainingMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartNotebook(
            self,
            request: models.StartNotebookRequest,
            opts: Dict = None,
    ) -> models.StartNotebookResponse:
        """
        启动Notebook
        """
        
        kwargs = {}
        kwargs["action"] = "StartNotebook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartNotebookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartTrainingTask(
            self,
            request: models.StartTrainingTaskRequest,
            opts: Dict = None,
    ) -> models.StartTrainingTaskResponse:
        """
        启动模型训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartTrainingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartTrainingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopModelAccelerateTask(
            self,
            request: models.StopModelAccelerateTaskRequest,
            opts: Dict = None,
    ) -> models.StopModelAccelerateTaskResponse:
        """
        停止模型加速任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopModelAccelerateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopModelAccelerateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopNotebook(
            self,
            request: models.StopNotebookRequest,
            opts: Dict = None,
    ) -> models.StopNotebookResponse:
        """
        停止Notebook
        """
        
        kwargs = {}
        kwargs["action"] = "StopNotebook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopNotebookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopTrainingTask(
            self,
            request: models.StopTrainingTaskRequest,
            opts: Dict = None,
    ) -> models.StopTrainingTaskResponse:
        """
        停止模型训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopTrainingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopTrainingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)