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
from tencentcloud.tia.v20180226 import models


class TiaClient(AbstractClient):
    _apiVersion = '2018-02-26'
    _endpoint = 'tia.tencentcloudapi.com'
    _service = 'tia'


    def CreateJob(self, request):
        """创建训练任务

        :param request: Request instance for CreateJob.
        :type request: :class:`tencentcloud.tia.v20180226.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModel(self, request):
        """部署模型，用以对外提供服务。有两种部署模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。

        :param request: Request instance for CreateModel.
        :type request: :class:`tencentcloud.tia.v20180226.models.CreateModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.CreateModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJob(self, request):
        """删除训练任务

        :param request: Request instance for DeleteJob.
        :type request: :class:`tencentcloud.tia.v20180226.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DeleteJobResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModel(self, request):
        """删除指定的部署模型。模型有两种部署模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。

        :param request: Request instance for DeleteModel.
        :type request: :class:`tencentcloud.tia.v20180226.models.DeleteModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJob(self, request):
        """获取训练任务详情

        :param request: Request instance for DescribeJob.
        :type request: :class:`tencentcloud.tia.v20180226.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DescribeJobResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModel(self, request):
        """描述已经部署的某个模型。而模型部署有两种模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。

        :param request: Request instance for DescribeModel.
        :type request: :class:`tencentcloud.tia.v20180226.models.DescribeModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DescribeModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallAgent(self, request):
        """安装agent

        :param request: Request instance for InstallAgent.
        :type request: :class:`tencentcloud.tia.v20180226.models.InstallAgentRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.InstallAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallAgent", params, headers=headers)
            response = json.loads(body)
            model = models.InstallAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJobs(self, request):
        """列举训练任务

        :param request: Request instance for ListJobs.
        :type request: :class:`tencentcloud.tia.v20180226.models.ListJobsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.ListJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJobs", params, headers=headers)
            response = json.loads(body)
            model = models.ListJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListModels(self, request):
        """用以列举已经部署的模型。而部署有两种模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。不同部署模式下的模型分开列出。

        :param request: Request instance for ListModels.
        :type request: :class:`tencentcloud.tia.v20180226.models.ListModelsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.ListModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListModels", params, headers=headers)
            response = json.loads(body)
            model = models.ListModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryLogs(self, request):
        """查询 TI-A 训练任务的日志

        :param request: Request instance for QueryLogs.
        :type request: :class:`tencentcloud.tia.v20180226.models.QueryLogsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.QueryLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryLogs", params, headers=headers)
            response = json.loads(body)
            model = models.QueryLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))