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
from tencentcloud.tione.v20211111 import models


class TioneClient(AbstractClient):
    _apiVersion = '2021-11-11'
    _endpoint = 'tione.tencentcloudapi.com'
    _service = 'tione'


    def ChatCompletion(self, request):
        r"""该接口支持与自行部署的大模型的聊天。

        使用该接口调用时需要携带腾讯云的密钥信息用于身份信息鉴权，建议通过腾讯云的云 API SDK调用，具体可以参考
        https://cloud.tencent.com/document/product/1278/85305

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


    def CreateDataSource(self, request):
        r"""创建数据源

        :param request: Request instance for CreateDataSource.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateDataSourceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateDataSourceResponse`

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


    def CreateDataset(self, request):
        r"""创建数据集

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


    def CreateExport(self, request):
        r"""创建任务式建模训练任务，Notebook，在线服务和批量预测任务日志下载任务API

        :param request: Request instance for CreateExport.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateExportRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModelService(self, request):
        r"""用于创建、发布一个新的模型服务

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


    def CreateModelServiceAuthToken(self, request):
        r"""创建一个 AuthToken

        :param request: Request instance for CreateModelServiceAuthToken.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateModelServiceAuthTokenRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateModelServiceAuthTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModelServiceAuthToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelServiceAuthTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMountLimit(self, request):
        r"""创建挂载限制

        :param request: Request instance for CreateMountLimit.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateMountLimitRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateMountLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMountLimit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMountLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotebook(self, request):
        r"""创建Notebook

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
        r"""保存镜像

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


    def CreatePresignedNotebookUrl(self, request):
        r"""生成Notebook访问链接

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


    def CreateRole(self, request):
        r"""创建自定义角色

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.tione.v20211111.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrainingModel(self, request):
        r"""导入模型

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
        r"""创建模型训练任务

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


    def DeleteDataSource(self, request):
        r"""删除数据源

        :param request: Request instance for DeleteDataSource.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteDataSourceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataset(self, request):
        r"""删除数据集

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


    def DeleteExport(self, request):
        r"""删除任务式建模训练任务，Notebook，在线服务和批量预测任务日志导出任务API

        :param request: Request instance for DeleteExport.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteExportRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelService(self, request):
        r"""根据服务id删除模型服务

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


    def DeleteModelServiceAuthToken(self, request):
        r"""删除一个 AuthToken

        :param request: Request instance for DeleteModelServiceAuthToken.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteModelServiceAuthTokenRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteModelServiceAuthTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModelServiceAuthToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelServiceAuthTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelServiceGroup(self, request):
        r"""根据服务组id删除服务组下所有模型服务

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


    def DeleteMountLimit(self, request):
        r"""删除挂载限制。注意：删除挂载限制后，该存储对应的所有数据源也会被删除

        :param request: Request instance for DeleteMountLimit.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteMountLimitRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteMountLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMountLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMountLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotebook(self, request):
        r"""删除Notebook

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


    def DeleteRole(self, request):
        r"""删除权限角色

        :param request: Request instance for DeleteRole.
        :type request: :class:`tencentcloud.tione.v20211111.models.DeleteRoleRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DeleteRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrainingModel(self, request):
        r"""删除模型

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
        r"""删除模型版本

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
        r"""删除训练任务

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


    def DescribeAccessRules(self, request):
        r"""列取访问权限规则列表

        :param request: Request instance for DescribeAccessRules.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeAccessRulesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeAccessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAnnotatedTaskList(self, request):
        r"""本接口（DescribeAnnotatedTaskList）用于查询用户标注任务详细信息列表；支持各种过滤条件；

        :param request: Request instance for DescribeAnnotatedTaskList.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeAnnotatedTaskListRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeAnnotatedTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAnnotatedTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAnnotatedTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingResourceGroup(self, request):
        r"""查询资源组节点列表

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


    def DescribeBillingResourceGroupAttachedWorkspaces(self, request):
        r"""查询资源组关联的工作空间列表

        :param request: Request instance for DescribeBillingResourceGroupAttachedWorkspaces.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceGroupAttachedWorkspacesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeBillingResourceGroupAttachedWorkspacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingResourceGroupAttachedWorkspaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingResourceGroupAttachedWorkspacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingResourceGroups(self, request):
        r"""查询资源组列表

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
        r"""查询资源组节点运行中的任务

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
        r"""本接口(DescribeBillingSpecs) 提供查询计费项列表

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
        r"""本接口(DescribeBillingSpecsPrice)用于查询按量计费计费项价格。

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


    def DescribeBuildInImages(self, request):
        r"""获取内置镜像列表

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


    def DescribeDataSource(self, request):
        r"""获取数据源详情

        :param request: Request instance for DescribeDataSource.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeDataSourceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSources(self, request):
        r"""获取数据源列表

        :param request: Request instance for DescribeDataSources.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeDataSourcesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasets(self, request):
        r"""查询数据集列表

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
        r"""获取任务式建模训练任务，Notebook，在线服务和批量预测任务的事件API

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


    def DescribeExport(self, request):
        r"""查看任务式建模训练任务，Notebook，在线服务和批量预测任务日志下载任务状态API

        :param request: Request instance for DescribeExport.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeExportRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferTemplates(self, request):
        r"""已废弃，收敛到统一接口

        查询推理镜像模板

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


    def DescribeLogs(self, request):
        r"""获取任务式建模训练任务，Notebook，在线服务和批量预测任务的日志API

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


    def DescribeModelAccelerateTask(self, request):
        r"""查询模型优化任务详情

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
        r"""模型加速之后的模型版本列表

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
        r"""查询单个服务

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
        r"""展示服务的调用信息

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
        r"""查询单个服务组

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
        r"""列举在线推理服务组

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
        r"""用于查询模型服务能否开启热更新

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


    def DescribeMountInstance(self, request):
        r"""DescribeMountInstance

        :param request: Request instance for DescribeMountInstance.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeMountInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeMountInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMountInstances(self, request):
        r"""非数据源挂载时获取实例列表

        :param request: Request instance for DescribeMountInstances.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeMountInstancesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeMountInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMountLimits(self, request):
        r"""获取挂载限制列表

        :param request: Request instance for DescribeMountLimits.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeMountLimitsRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeMountLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebook(self, request):
        r"""Notebook详情

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
        r"""Notebook列表

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


    def DescribePlatformImages(self, request):
        r"""查询平台镜像信息

        :param request: Request instance for DescribePlatformImages.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribePlatformImagesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribePlatformImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlatformImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlatformImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePresetImageList(self, request):
        r"""该接口用于查询内置镜像列表

        :param request: Request instance for DescribePresetImageList.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribePresetImageListRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribePresetImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePresetImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePresetImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicAlgoVersionList(self, request):
        r"""公共算法版本列表

        :param request: Request instance for DescribePublicAlgoVersionList.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribePublicAlgoVersionListRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribePublicAlgoVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicAlgoVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicAlgoVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRole(self, request):
        r"""获取角色详情

        :param request: Request instance for DescribeRole.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeRoleRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRole", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleUsers(self, request):
        r"""获取角色下已授权的用户列表

        :param request: Request instance for DescribeRoleUsers.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeRoleUsersRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeRoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoles(self, request):
        r"""获取角色列表

        :param request: Request instance for DescribeRoles.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeRolesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubAccountLinuxUserInfos(self, request):
        r"""批量查询子账号Linux用户信息

        :param request: Request instance for DescribeSubAccountLinuxUserInfos.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeSubAccountLinuxUserInfosRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeSubAccountLinuxUserInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubAccountLinuxUserInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubAccountLinuxUserInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingModelVersion(self, request):
        r"""查询模型版本

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
        r"""模型版本列表

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
        r"""训练任务详情

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


    def DescribeTrainingTaskPodUrl(self, request):
        r"""获取单个训练任务实例的登录链接

        :param request: Request instance for DescribeTrainingTaskPodUrl.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTaskPodUrlRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeTrainingTaskPodUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingTaskPodUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingTaskPodUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingTaskPods(self, request):
        r"""训练任务pod列表

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
        r"""训练任务列表

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


    def DescribeWorkspace(self, request):
        r"""查询工作空间详情

        :param request: Request instance for DescribeWorkspace.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceMembers(self, request):
        r"""查询空间成员列表

        :param request: Request instance for DescribeWorkspaceMembers.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceMembersRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceQuotaUsage(self, request):
        r"""## DescribeWorkspaceQuotaUsage 接口文档

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

        :param request: Request instance for DescribeWorkspaceQuotaUsage.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceQuotaUsageRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceQuotaUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceQuotaUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceQuotaUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceQuotas(self, request):
        r"""# DescribeWorkspaceQuotas 接口文档

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

        :param request: Request instance for DescribeWorkspaceQuotas.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceQuotasRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspaceQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaces(self, request):
        r"""查询工作空间列表

        :param request: Request instance for DescribeWorkspaces.
        :type request: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspacesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.DescribeWorkspacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTrainingTaskClsConfig(self, request):
        r"""开启CLS日志投递

        :param request: Request instance for EnableTrainingTaskClsConfig.
        :type request: :class:`tencentcloud.tione.v20211111.models.EnableTrainingTaskClsConfigRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.EnableTrainingTaskClsConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTrainingTaskClsConfig", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTrainingTaskClsConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModelService(self, request):
        r"""用于更新模型服务

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


    def ModifyModelServiceAuthToken(self, request):
        r"""修改一个 AuthToken

        :param request: Request instance for ModifyModelServiceAuthToken.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyModelServiceAuthTokenRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyModelServiceAuthTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModelServiceAuthToken", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelServiceAuthTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModelServiceAuthorization(self, request):
        r"""修改服务鉴权配置

        :param request: Request instance for ModifyModelServiceAuthorization.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyModelServiceAuthorizationRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyModelServiceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModelServiceAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelServiceAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotebook(self, request):
        r"""修改Notebook

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
        r"""修改Notebook标签

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


    def ModifyRole(self, request):
        r"""修改自定义角色

        :param request: Request instance for ModifyRole.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyRoleRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoleAccessRules(self, request):
        r"""修改自定义角色的权限规则

        :param request: Request instance for ModifyRoleAccessRules.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyRoleAccessRulesRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyRoleAccessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoleAccessRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoleAccessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoleUserGrant(self, request):
        r"""修改角色下用户的授权状态

        :param request: Request instance for ModifyRoleUserGrant.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyRoleUserGrantRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyRoleUserGrantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoleUserGrant", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoleUserGrantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceGroupWeights(self, request):
        r"""更新推理服务组流量分配

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


    def ModifyUserGrant(self, request):
        r"""更新用户授权

        :param request: Request instance for ModifyUserGrant.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyUserGrantRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyUserGrantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserGrant", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserGrantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkspaceMembers(self, request):
        r"""更新空间用户列表

        :param request: Request instance for ModifyWorkspaceMembers.
        :type request: :class:`tencentcloud.tione.v20211111.models.ModifyWorkspaceMembersRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModifyWorkspaceMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkspaceMembers", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkspaceMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushTrainingMetrics(self, request):
        r"""上报训练自定义指标

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


    def StartNotebook(self, request):
        r"""启动Notebook

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
        r"""启动模型训练任务

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


    def StopModelAccelerateTask(self, request):
        r"""停止模型加速任务

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
        r"""停止Notebook

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
        r"""停止模型训练任务

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


    def UpdateDataSource(self, request):
        r"""更新数据源

        :param request: Request instance for UpdateDataSource.
        :type request: :class:`tencentcloud.tione.v20211111.models.UpdateDataSourceRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.UpdateDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMountLimit(self, request):
        r"""创建挂载限制

        :param request: Request instance for UpdateMountLimit.
        :type request: :class:`tencentcloud.tione.v20211111.models.UpdateMountLimitRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.UpdateMountLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateMountLimit", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateMountLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSubAccountLinuxUserInfo(self, request):
        r"""更新子账号Linux用户信息

        :param request: Request instance for UpdateSubAccountLinuxUserInfo.
        :type request: :class:`tencentcloud.tione.v20211111.models.UpdateSubAccountLinuxUserInfoRequest`
        :rtype: :class:`tencentcloud.tione.v20211111.models.UpdateSubAccountLinuxUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSubAccountLinuxUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSubAccountLinuxUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))