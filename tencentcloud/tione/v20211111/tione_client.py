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
from tencentcloud.tione.v20211111 import models


class TioneClient(AbstractClient):
    _apiVersion = '2021-11-11'
    _endpoint = 'tione.tencentcloudapi.com'
    _service = 'tione'


    def ChatCompletion(self, request):
        """该接口支持与自行部署的大模型的聊天。

        :param request: Request instance for ChatCompletion.
        :type request: :class:`tencentcloud.tione.v20211111.models.ChatCompletionRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ChatCompletionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChatCompletion", params, headers=headers)
            response = json.loads(body)
            model = models.ChatCompletionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBatchModelAccTasks(self, request):
        """批量创建模型加速任务

        :param request: Request instance for CreateBatchModelAccTasks.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateBatchModelAccTasksRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateBatchModelAccTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatchModelAccTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchModelAccTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBatchTask(self, request):
        """创建跑批任务

        :param request: Request instance for CreateBatchTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateBatchTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateBatchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataset(self, request):
        """创建数据集

        :param request: Request instance for CreateDataset.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateDatasetRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateDatasetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModelService(self, request):
        """用于创建、发布一个新的模型服务

        :param request: Request instance for CreateModelService.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateModelServiceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModelService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotebook(self, request):
        """创建Notebook

        :param request: Request instance for CreateNotebook.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateNotebookRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateNotebookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebook", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotebookImage(self, request):
        """保存镜像

        :param request: Request instance for CreateNotebookImage.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateNotebookImageRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateNotebookImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebookImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOptimizedModel(self, request):
        """保存优化模型

        :param request: Request instance for CreateOptimizedModel.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateOptimizedModelRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateOptimizedModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOptimizedModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOptimizedModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrainingModel(self, request):
        """导入模型

        :param request: Request instance for CreateTrainingModel.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateTrainingModelRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateTrainingModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrainingModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrainingModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrainingTask(self, request):
        """创建模型训练任务

        :param request: Request instance for CreateTrainingTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateTrainingTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateTrainingTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrainingTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrainingTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBatchTask(self, request):
        """删除跑批任务

        :param request: Request instance for DeleteBatchTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteBatchTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteBatchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBatchTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBatchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataset(self, request):
        """删除数据集

        :param request: Request instance for DeleteDataset.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteDatasetRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteDatasetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatasetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelAccelerateTask(self, request):
        """删除模型加速任务

        :param request: Request instance for DeleteModelAccelerateTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteModelAccelerateTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteModelAccelerateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModelAccelerateTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelAccelerateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelService(self, request):
        """根据服务id删除模型服务

        :param request: Request instance for DeleteModelService.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteModelServiceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModelService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelServiceGroup(self, request):
        """根据服务组id删除服务组下所有模型服务

        :param request: Request instance for DeleteModelServiceGroup.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteModelServiceGroupRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteModelServiceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModelServiceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelServiceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotebook(self, request):
        """删除Notebook

        :param request: Request instance for DeleteNotebook.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteNotebookRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteNotebookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNotebook", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNotebookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotebookImageRecord(self, request):
        """删除notebook镜像保存记录

        :param request: Request instance for DeleteNotebookImageRecord.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteNotebookImageRecordRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteNotebookImageRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNotebookImageRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNotebookImageRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrainingModel(self, request):
        """删除模型

        :param request: Request instance for DeleteTrainingModel.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteTrainingModelRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteTrainingModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrainingModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrainingModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrainingModelVersion(self, request):
        """删除模型版本

        :param request: Request instance for DeleteTrainingModelVersion.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteTrainingModelVersionRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteTrainingModelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrainingModelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrainingModelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrainingTask(self, request):
        """删除训练任务

        :param request: Request instance for DeleteTrainingTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteTrainingTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteTrainingTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrainingTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrainingTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPIConfigs(self, request):
        """列举API

        :param request: Request instance for DescribeAPIConfigs.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeAPIConfigsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeAPIConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchTask(self, request):
        """查询跑批任务

        :param request: Request instance for DescribeBatchTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBatchTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBatchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchTaskInstances(self, request):
        """查询跑批实例列表

        :param request: Request instance for DescribeBatchTaskInstances.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBatchTaskInstancesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBatchTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchTasks(self, request):
        """批量预测任务列表信息

        :param request: Request instance for DescribeBatchTasks.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBatchTasksRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBatchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingResourceGroups(self, request):
        """查询资源组详情

        :param request: Request instance for DescribeBillingResourceGroups.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceGroupsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingResourceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingResourceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingResourceInstanceRunningJobs(self, request):
        """查询资源组节点运行中的任务

        :param request: Request instance for DescribeBillingResourceInstanceRunningJobs.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceInstanceRunningJobsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceInstanceRunningJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingResourceInstanceRunningJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingResourceInstanceRunningJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingSpecs(self, request):
        """本接口(DescribeBillingSpecs)用于查询计费项列表

        :param request: Request instance for DescribeBillingSpecs.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBillingSpecsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBillingSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingSpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingSpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingSpecsPrice(self, request):
        """本接口(DescribeBillingSpecsPrice)用于查询按量计费计费项价格。

        :param request: Request instance for DescribeBillingSpecsPrice.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBillingSpecsPriceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBillingSpecsPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingSpecsPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingSpecsPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasetDetailStructured(self, request):
        """查询结构化数据集详情

        :param request: Request instance for DescribeDatasetDetailStructured.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeDatasetDetailStructuredRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeDatasetDetailStructuredResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasetDetailStructured", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasetDetailStructuredResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasetDetailUnstructured(self, request):
        """查询非结构化数据集详情

        :param request: Request instance for DescribeDatasetDetailUnstructured.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeDatasetDetailUnstructuredRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeDatasetDetailUnstructuredResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasetDetailUnstructured", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasetDetailUnstructuredResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasets(self, request):
        """查询数据集列表

        :param request: Request instance for DescribeDatasets.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeDatasetsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeDatasetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvents(self, request):
        """获取任务式建模训练任务，Notebook，在线服务和批量预测任务的事件API

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeEventsResponse`

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


    def DescribeInferTemplates(self, request):
        """查询推理镜像模板

        :param request: Request instance for DescribeInferTemplates.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeInferTemplatesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeInferTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLatestTrainingMetrics(self, request):
        """查询最近上报的训练自定义指标

        :param request: Request instance for DescribeLatestTrainingMetrics.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeLatestTrainingMetricsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeLatestTrainingMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLatestTrainingMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLatestTrainingMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogs(self, request):
        """获取任务式建模训练任务，Notebook，在线服务和批量预测任务的日志API

        :param request: Request instance for DescribeLogs.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeLogsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelAccEngineVersions(self, request):
        """查询模型加速引擎版本列表

        :param request: Request instance for DescribeModelAccEngineVersions.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccEngineVersionsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccEngineVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelAccEngineVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelAccEngineVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelAccelerateTask(self, request):
        """查询模型优化任务详情

        :param request: Request instance for DescribeModelAccelerateTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccelerateTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccelerateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelAccelerateTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelAccelerateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelAccelerateTasks(self, request):
        """查询模型加速任务列表

        :param request: Request instance for DescribeModelAccelerateTasks.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccelerateTasksRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccelerateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelAccelerateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelAccelerateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelService(self, request):
        """查询单个服务

        :param request: Request instance for DescribeModelService.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServiceCallInfo(self, request):
        """展示服务的调用信息

        :param request: Request instance for DescribeModelServiceCallInfo.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceCallInfoRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceCallInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServiceCallInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceCallInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServiceGroup(self, request):
        """查询单个服务组

        :param request: Request instance for DescribeModelServiceGroup.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceGroupRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServiceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServiceGroups(self, request):
        """列举在线推理服务组

        :param request: Request instance for DescribeModelServiceGroups.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceGroupsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServiceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServiceHistory(self, request):
        """展示服务的历史版本

        :param request: Request instance for DescribeModelServiceHistory.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceHistoryRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServiceHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServiceHotUpdated(self, request):
        """用于查询模型服务能否开启热更新

        :param request: Request instance for DescribeModelServiceHotUpdated.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceHotUpdatedRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServiceHotUpdatedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServiceHotUpdated", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceHotUpdatedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServices(self, request):
        """查询多个服务

        :param request: Request instance for DescribeModelServices.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelServicesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebook(self, request):
        """Notebook详情

        :param request: Request instance for DescribeNotebook.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeNotebookRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeNotebookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebook", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookImageKernels(self, request):
        """查询镜像kernel

        :param request: Request instance for DescribeNotebookImageKernels.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeNotebookImageKernelsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeNotebookImageKernelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookImageKernels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookImageKernelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookImageRecords(self, request):
        """查看notebook镜像保存记录

        :param request: Request instance for DescribeNotebookImageRecords.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeNotebookImageRecordsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeNotebookImageRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookImageRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookImageRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebooks(self, request):
        """Notebook列表

        :param request: Request instance for DescribeNotebooks.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeNotebooksRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeNotebooksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebooks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebooksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingFrameworks(self, request):
        """训练框架列表

        :param request: Request instance for DescribeTrainingFrameworks.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingFrameworksRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingFrameworksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingFrameworks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingFrameworksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingMetrics(self, request):
        """查询训练自定义指标

        :param request: Request instance for DescribeTrainingMetrics.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingMetricsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingModelVersion(self, request):
        """查询模型版本

        :param request: Request instance for DescribeTrainingModelVersion.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingModelVersionRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingModelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingModelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingModelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingModelVersions(self, request):
        """模型版本列表

        :param request: Request instance for DescribeTrainingModelVersions.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingModelVersionsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingModelVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingModelVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingModelVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingModels(self, request):
        """模型列表

        :param request: Request instance for DescribeTrainingModels.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingModelsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingModels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingTask(self, request):
        """训练任务详情

        :param request: Request instance for DescribeTrainingTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingTaskPods(self, request):
        """训练任务pod列表

        :param request: Request instance for DescribeTrainingTaskPods.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTaskPodsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTaskPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingTaskPods", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingTaskPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingTasks(self, request):
        """训练任务列表

        :param request: Request instance for DescribeTrainingTasks.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTasksRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModelService(self, request):
        """用于更新模型服务

        :param request: Request instance for ModifyModelService.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyModelServiceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModelService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModelServicePartialConfig(self, request):
        """增量更新在线推理服务的部分配置，不更新的配置项不需要传入

        :param request: Request instance for ModifyModelServicePartialConfig.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyModelServicePartialConfigRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyModelServicePartialConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModelServicePartialConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelServicePartialConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotebook(self, request):
        """修改Notebook

        :param request: Request instance for ModifyNotebook.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyNotebookRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyNotebookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotebook", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotebookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotebookTags(self, request):
        """修改Notebook标签

        :param request: Request instance for ModifyNotebookTags.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyNotebookTagsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyNotebookTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotebookTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotebookTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceGroupWeights(self, request):
        """更新推理服务组流量分配

        :param request: Request instance for ModifyServiceGroupWeights.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyServiceGroupWeightsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyServiceGroupWeightsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceGroupWeights", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceGroupWeightsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushTrainingMetrics(self, request):
        """上报训练自定义指标

        :param request: Request instance for PushTrainingMetrics.
        :type request: :class:`tencentcloud.tione.v20211111.models.PushTrainingMetricsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.PushTrainingMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushTrainingMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.PushTrainingMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartModelAccelerateTask(self, request):
        """重启模型加速任务

        :param request: Request instance for RestartModelAccelerateTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.RestartModelAccelerateTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.RestartModelAccelerateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartModelAccelerateTask", params, headers=headers)
            response = json.loads(body)
            model = models.RestartModelAccelerateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendChatMessage(self, request):
        """这是一个供您体验大模型聊天的接口。

        :param request: Request instance for SendChatMessage.
        :type request: :class:`tencentcloud.tione.v20211111.models.SendChatMessageRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.SendChatMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendChatMessage", params, headers=headers)
            response = json.loads(body)
            model = models.SendChatMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartNotebook(self, request):
        """启动Notebook

        :param request: Request instance for StartNotebook.
        :type request: :class:`tencentcloud.tione.v20211111.models.StartNotebookRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StartNotebookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartNotebook", params, headers=headers)
            response = json.loads(body)
            model = models.StartNotebookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartTrainingTask(self, request):
        """启动模型训练任务

        :param request: Request instance for StartTrainingTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.StartTrainingTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StartTrainingTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartTrainingTask", params, headers=headers)
            response = json.loads(body)
            model = models.StartTrainingTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBatchTask(self, request):
        """停止跑批任务

        :param request: Request instance for StopBatchTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.StopBatchTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StopBatchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBatchTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopBatchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCreatingImage(self, request):
        """停止保存镜像

        :param request: Request instance for StopCreatingImage.
        :type request: :class:`tencentcloud.tione.v20211111.models.StopCreatingImageRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StopCreatingImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCreatingImage", params, headers=headers)
            response = json.loads(body)
            model = models.StopCreatingImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopModelAccelerateTask(self, request):
        """停止模型加速任务

        :param request: Request instance for StopModelAccelerateTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.StopModelAccelerateTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StopModelAccelerateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopModelAccelerateTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopModelAccelerateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopNotebook(self, request):
        """停止Notebook

        :param request: Request instance for StopNotebook.
        :type request: :class:`tencentcloud.tione.v20211111.models.StopNotebookRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StopNotebookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopNotebook", params, headers=headers)
            response = json.loads(body)
            model = models.StopNotebookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopTrainingTask(self, request):
        """停止模型训练任务

        :param request: Request instance for StopTrainingTask.
        :type request: :class:`tencentcloud.tione.v20211111.models.StopTrainingTaskRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.StopTrainingTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTrainingTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopTrainingTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))