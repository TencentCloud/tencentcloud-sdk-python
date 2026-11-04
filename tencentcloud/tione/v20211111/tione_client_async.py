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
        
    async def CreateDataSource(
            self,
            request: models.CreateDataSourceRequest,
            opts: Dict = None,
    ) -> models.CreateDataSourceResponse:
        """
        创建数据源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataSourceResponse
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
        
    async def CreateMountLimit(
            self,
            request: models.CreateMountLimitRequest,
            opts: Dict = None,
    ) -> models.CreateMountLimitResponse:
        """
        创建挂载限制
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMountLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMountLimitResponse
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
        
    async def CreateNotebookImage(
            self,
            request: models.CreateNotebookImageRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookImageResponse:
        """
        保存镜像
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebookImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookImageResponse
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
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        创建自定义角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
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
        
    async def DeleteDataSource(
            self,
            request: models.DeleteDataSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDataSourceResponse:
        """
        删除数据源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataSourceResponse
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
        
    async def DeleteMountLimit(
            self,
            request: models.DeleteMountLimitRequest,
            opts: Dict = None,
    ) -> models.DeleteMountLimitResponse:
        """
        删除挂载限制。注意：删除挂载限制后，该存储对应的所有数据源也会被删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMountLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMountLimitResponse
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
        
    async def DeleteRole(
            self,
            request: models.DeleteRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleResponse:
        """
        删除权限角色
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleResponse
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
        
    async def DescribeAccessRules(
            self,
            request: models.DescribeAccessRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRulesResponse:
        """
        列取访问权限规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAnnotatedTaskList(
            self,
            request: models.DescribeAnnotatedTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAnnotatedTaskListResponse:
        """
        本接口（DescribeAnnotatedTaskList）用于查询用户标注任务详细信息列表；支持各种过滤条件；
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAnnotatedTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAnnotatedTaskListResponse
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
        
    async def DescribeBillingResourceGroupAttachedWorkspaces(
            self,
            request: models.DescribeBillingResourceGroupAttachedWorkspacesRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingResourceGroupAttachedWorkspacesResponse:
        """
        查询资源组关联的工作空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingResourceGroupAttachedWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingResourceGroupAttachedWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingResourceGroups(
            self,
            request: models.DescribeBillingResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingResourceGroupsResponse:
        """
        查询资源组列表
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
        
    async def DescribeDataSource(
            self,
            request: models.DescribeDataSourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceResponse:
        """
        获取数据源详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSources(
            self,
            request: models.DescribeDataSourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourcesResponse:
        """
        获取数据源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourcesResponse
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
        
    async def DescribeMountInstance(
            self,
            request: models.DescribeMountInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeMountInstanceResponse:
        """
        DescribeMountInstance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountInstances(
            self,
            request: models.DescribeMountInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeMountInstancesResponse:
        """
        非数据源挂载时获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountLimits(
            self,
            request: models.DescribeMountLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeMountLimitsResponse:
        """
        获取挂载限制列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountLimitsResponse
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
        
    async def DescribePresetImageList(
            self,
            request: models.DescribePresetImageListRequest,
            opts: Dict = None,
    ) -> models.DescribePresetImageListResponse:
        """
        该接口用于查询内置镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePresetImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePresetImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicAlgoVersionList(
            self,
            request: models.DescribePublicAlgoVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribePublicAlgoVersionListResponse:
        """
        公共算法版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicAlgoVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicAlgoVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRole(
            self,
            request: models.DescribeRoleRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleResponse:
        """
        获取角色详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleUsers(
            self,
            request: models.DescribeRoleUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleUsersResponse:
        """
        获取角色下已授权的用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoles(
            self,
            request: models.DescribeRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRolesResponse:
        """
        获取角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubAccountLinuxUserInfos(
            self,
            request: models.DescribeSubAccountLinuxUserInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeSubAccountLinuxUserInfosResponse:
        """
        批量查询子账号Linux用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubAccountLinuxUserInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubAccountLinuxUserInfosResponse
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
        
    async def DescribeTrainingTaskPodUrl(
            self,
            request: models.DescribeTrainingTaskPodUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingTaskPodUrlResponse:
        """
        获取单个训练任务实例的登录链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingTaskPodUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingTaskPodUrlResponse
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
        
    async def DescribeWorkspace(
            self,
            request: models.DescribeWorkspaceRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspaceResponse:
        """
        查询工作空间详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaceMembers(
            self,
            request: models.DescribeWorkspaceMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspaceMembersResponse:
        """
        查询空间成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaceMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspaceMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaceQuotaUsage(
            self,
            request: models.DescribeWorkspaceQuotaUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspaceQuotaUsageResponse:
        """
        ## DescribeWorkspaceQuotaUsage 接口文档

        ### 接口描述
        查询工作空间配额用量信息。该接口用于查询指定工作空间下某个子账号的配额使用情况，支持多种配额类型（CBS存储配额、Notebook开发机数量配额、托管按量资源规格限制）。

        ### 错误码

        | 错误码 | 说明 |
        |--------|------|
        | InvalidParameterValue | 参数值无效（如必填参数为空、QuotaType不在枚举范围内） |
        | FailedOperation.QueryDatabaseFail | 数据库查询失败 |

        ### 示例

        **请求示例**：
        ```json
        {
          "QuotaType": "Notebook",
          "SupervisorUin": "100012345678",
          "SupervisorSubUin": "100012345679",
          "TiProjectId": "ti-proj-123456"
        }
        ```

        **响应示例**：
        ```json
        {
          "QuotaType": "Notebook",
          "QuotaEnabled": true,
          "TotalQuota": 10,
          "UsedQuota": 3,
        }
        ```
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaceQuotaUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspaceQuotaUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaceQuotas(
            self,
            request: models.DescribeWorkspaceQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspaceQuotasResponse:
        """
        # DescribeWorkspaceQuotas 接口文档

        ## 接口描述

        查询指定工作空间下的配额配置和配额列表。该接口用于获取主账号在某个工作空间下的配额管理配置，包括是否启用配额管理、默认配额值以及针对子账号或用户组的具体配额分配情况。

        支持三种配额类型：
        - **CBS**：CBS存储配额管理
        - **Notebook**：开发机数量配额管理
        - **PostPaySpec**：托管按量资源规格限制



        ## 请求参数

        ### 公共参数（HTTP Header）
        | 参数名 | 类型 | 必填 | 描述 |
        |--------|------|------|------|
        | X-TC-Uin | string | 是 | 主账号Uin |
        | X-TC-ProjectId | uint32 | 是 | 工作空间ID |

        ### 请求体参数
        | 参数名 | 类型 | 必填 | 描述 |
        |--------|------|------|------|
        | QuotaType | string | 是 | 配额类型，可选值：<br>- `CBS`：CBS存储配额<br>- `Notebook`：开发机数量配额<br>- `PostPaySpec`：托管按量资源规格限制 |

        ## 响应参数

        | 参数名 | 类型 | 描述 |
        |--------|------|------|
        | QuotaType | string | 配额类型 |
        | QuotaEnabled | bool | 是否启用配额管理功能 |
        | DefaultQuota | WorkspaceQuota | 默认配额配置（当QuotaEnabled为false时为空对象） |
        | Quotas | ][WorkspaceQuota | 配额列表，包含所有子账号或用户组的配额配置（仅当QuotaEnabled为true时返回） |

        ### WorkspaceQuota

        | 参数名 | 类型 | 描述 |
        |--------|------|------|
        | Id | string | 配额ID，格式：<br>- 用户配额：`{quota_type}-{uin}-{subuin}-{TiProjectId}`<br>- 用户组配额：`{quota_type}-{uin}-{groupid}-{TiProjectId}`<br>- 默认配额：`{quota_type}-{uin}-default-{TiProjectId}` |
        | QuotaType | string | 配额类型 |
        | Uin | string | 主账号Uin |
        | SubUin | string | 子账号Uin（当TargetType为USER时有值） |
        | SubUinName | string | 子账号名称（当TargetType为USER时有值） |
        | QuotaValue | uint32 | 配额值：<br>- CBS：容量（GiB），默认100，范围10-10000<br>- Notebook：数量（个），默认1，范围1-999<br>- PostPaySpec：无意义，关注QuotaData字段 |
        | QuotaData | []string | 配额数据（JSON数组格式）：<br>- 当QuotaType为PostPaySpec时，存储允许使用的规格ID列表 |
        | TargetType | string | 配额目标类型：<br>- `USER`：用户配额<br>- `USER_GROUP`：用户组配额 |
        | GroupId | string | 用户组ID（当TargetType为USER_GROUP时有值） |
        | GroupName | string | 用户组名称（当TargetType为USER_GROUP时有值） |
        | TiProjectId | string | 工作空间ID |

        ## 业务逻辑

        1. **参数校验**：验证QuotaType参数是否合法
        2. **查询配额配置**：根据主账号Uin、工作空间ID和配额类型查询配额配置
        3. **配置不存在**：
           - 返回系统默认的配额启用状态和默认配额值
           - CBS默认启用，默认值100GiB
           - Notebook默认启用，默认值1个
           - PostPaySpec默认不启用
        4. **配置存在但未启用**：
           - QuotaEnabled返回false
           - DefaultQuota返回空对象
           - Quotas不返回
        5. **配置存在且已启用**：
           - QuotaEnabled返回true
           - DefaultQuota返回配置的默认配额值
           - Quotas返回所有子账号或用户组的配额列表
           - 自动反序列化QuotaData字段（JSON数组）

        ## 使用场景

        1. **配额管理页面初始化**：获取当前工作空间的配额配置状态
        2. **配额列表展示**：展示所有子账号或用户组的配额分配情况
        3. **配额编辑前查询**：在修改配额前获取当前配置
        4. **权限控制判断**：判断是否启用了配额管理功能

        ## 错误码

        | 错误码 | 描述 | 解决方案 |
        |--------|------|----------|
        | InvalidParameterValue | 参数值错误 | 检查QuotaType参数是否为合法值（CBS/Notebook/PostPaySpec） |
        | FailedOperation.QueryDatabaseFail | 数据库查询失败 | 稍后重试或联系管理员 |

        ## 请求示例

        ```json
        {
          "QuotaType": "CBS"
        }
        ```

        **HTTP Header:**
        ```
        X-TC-Uin: 100012345678
        X-TC-ProjectId: 123456
        ```

        ## 响应示例

        ### 示例1：配额已启用且有配额列表

        ```json
        {
          "QuotaType": "CBS",
          "QuotaEnabled": true,
          "DefaultQuota": {
            "Id": "CBS-100012345678-default-123456",
            "QuotaType": "CBS",
            "Uin": "100012345678",
            "SubUin": "",
            "SubUinName": "",
            "QuotaValue": 100,
            "QuotaData": [],
            "TargetType": "",
            "GroupId": "",
            "GroupName": "",
            "TiProjectId": "123456"
          },
          "Quotas": [
            {
              "Id": "CBS-100012345678-100012345679-123456",
              "QuotaType": "CBS",
              "Uin": "100012345678",
              "SubUin": "100012345679",
              "SubUinName": "张三",
              "QuotaValue": 200,
              "QuotaData": [],
              "TargetType": "USER",
              "GroupId": "",
              "GroupName": "",
              "TiProjectId": "123456"
            },
            {
              "Id": "CBS-100012345678-group001-123456",
              "QuotaType": "CBS",
              "Uin": "100012345678",
              "SubUin": "",
              "SubUinName": "",
              "QuotaValue": 500,
              "QuotaData": [],
              "TargetType": "USER_GROUP",
              "GroupId": "group001",
              "GroupName": "开发组",
              "TiProjectId": "123456"
            }
          ]
        }
        ```

        ### 示例2：配额未启用

        ```json
        {
          "QuotaType": "PostPaySpec",
          "QuotaEnabled": false,
          "DefaultQuota": {},
          "Quotas": []
        }
        ```

        ### 示例3：PostPaySpec类型配额（带QuotaData）

        ```json
        {
          "QuotaType": "PostPaySpec",
          "QuotaEnabled": true,
          "DefaultQuota": {
            "Id": "PostPaySpec-100012345678-default-123456",
            "QuotaType": "PostPaySpec",
            "Uin": "100012345678",
            "SubUin": "",
            "SubUinName": "",
            "QuotaValue": 0,
            "QuotaData": ["spec-001", "spec-002", "spec-003"],
            "TargetType": "",
            "GroupId": "",
            "GroupName": "",
            "TiProjectId": "123456"
          },
          "Quotas": [
            {
              "Id": "PostPaySpec-100012345678-100012345679-123456",
              "QuotaType": "PostPaySpec",
              "Uin": "100012345678",
              "SubUin": "100012345679",
              "SubUinName": "李四",
              "QuotaValue": 0,
              "QuotaData": ["spec-001", "spec-002"],
              "TargetType": "USER",
              "GroupId": "",
              "GroupName": "",
              "TiProjectId": "123456"
            }
          ]
        }
        ```

        ## 注意事项

        1. **配额继承规则**：
           - 如果子账号或用户组没有单独配置配额，则使用DefaultQuota的值
           - 用户组配额优先级高于默认配额，用户配额优先级最高

        2. **QuotaData字段**：
           - 仅在QuotaType为PostPaySpec时有实际意义
           - 存储的是允许使用的规格ID列表
           - 其他类型的配额该字段为空数组

        3. **TargetType字段**：
           - DefaultQuota的TargetType为空字符串
           - Quotas列表中的每个配额都有明确的TargetType

        4. **配额值单位**：
           - CBS配额：GiB（1 GiB = 1024 MiB）
           - Notebook配额：个数

        5. **性能优化**：
           - 接口会一次性返回所有配额列表，避免多次查询
           - 建议前端做好缓存，减少重复请求
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaceQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspaceQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaces(
            self,
            request: models.DescribeWorkspacesRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspacesResponse:
        """
        查询工作空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTrainingTaskClsConfig(
            self,
            request: models.EnableTrainingTaskClsConfigRequest,
            opts: Dict = None,
    ) -> models.EnableTrainingTaskClsConfigResponse:
        """
        开启CLS日志投递
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTrainingTaskClsConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTrainingTaskClsConfigResponse
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
        
    async def ModifyNotebook(
            self,
            request: models.ModifyNotebookRequest,
            opts: Dict = None,
    ) -> models.ModifyNotebookResponse:
        """
        修改Notebook
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotebook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotebookResponse
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
        
    async def ModifyRole(
            self,
            request: models.ModifyRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRoleResponse:
        """
        修改自定义角色
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoleAccessRules(
            self,
            request: models.ModifyRoleAccessRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyRoleAccessRulesResponse:
        """
        修改自定义角色的权限规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoleAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoleAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoleUserGrant(
            self,
            request: models.ModifyRoleUserGrantRequest,
            opts: Dict = None,
    ) -> models.ModifyRoleUserGrantResponse:
        """
        修改角色下用户的授权状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoleUserGrant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoleUserGrantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceGroupWeights(
            self,
            request: models.ModifyServiceGroupWeightsRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceGroupWeightsResponse:
        """
        更新推理服务组流量分配
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceGroupWeights"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceGroupWeightsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserGrant(
            self,
            request: models.ModifyUserGrantRequest,
            opts: Dict = None,
    ) -> models.ModifyUserGrantResponse:
        """
        更新用户授权
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserGrant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserGrantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkspaceMembers(
            self,
            request: models.ModifyWorkspaceMembersRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkspaceMembersResponse:
        """
        更新空间用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkspaceMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkspaceMembersResponse
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
        
    async def UpdateDataSource(
            self,
            request: models.UpdateDataSourceRequest,
            opts: Dict = None,
    ) -> models.UpdateDataSourceResponse:
        """
        更新数据源
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateMountLimit(
            self,
            request: models.UpdateMountLimitRequest,
            opts: Dict = None,
    ) -> models.UpdateMountLimitResponse:
        """
        创建挂载限制
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateMountLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateMountLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSubAccountLinuxUserInfo(
            self,
            request: models.UpdateSubAccountLinuxUserInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateSubAccountLinuxUserInfoResponse:
        """
        更新子账号Linux用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSubAccountLinuxUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSubAccountLinuxUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)