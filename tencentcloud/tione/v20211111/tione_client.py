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


    def CreatePresignedNotebookUrl(self, request):
        """生成Notebook访问链接

        :param request: Request instance for CreatePresignedNotebookUrl.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreatePresignedNotebookUrlRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreatePresignedNotebookUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePresignedNotebookUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePresignedNotebookUrlResponse()
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


    def DescribeBillingResourceGroup(self, request):
        """查询资源组节点列表

        :param request: Request instance for DescribeBillingResourceGroup.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceGroupRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingResourceGroupResponse()
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


    def DescribeBuildInImages(self, request):
        """获取内置镜像列表

        :param request: Request instance for DescribeBuildInImages.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBuildInImagesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBuildInImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBuildInImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBuildInImagesResponse()
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


    def DescribeModelAccelerateVersions(self, request):
        """模型加速之后的模型版本列表

        :param request: Request instance for DescribeModelAccelerateVersions.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccelerateVersionsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeModelAccelerateVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelAccelerateVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelAccelerateVersionsResponse()
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