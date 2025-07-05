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
from tencentcloud.tione.v20191022 import models


class TioneClient(AbstractClient):
    _apiVersion = '2019-10-22'
    _endpoint = 'tione.tencentcloudapi.com'
    _service = 'tione'


    def CreateCodeRepository(self, request):
        """创建存储库

        :param request: Request instance for CreateCodeRepository.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreateCodeRepositoryRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreateCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeRepository", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotebookInstance(self, request):
        """创建Notebook实例

        :param request: Request instance for CreateNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreateNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreateNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebookInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotebookLifecycleScript(self, request):
        """创建Notebook生命周期脚本

        :param request: Request instance for CreateNotebookLifecycleScript.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreateNotebookLifecycleScriptRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreateNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebookLifecycleScript", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookLifecycleScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePresignedNotebookInstanceUrl(self, request):
        """创建Notebook授权Url

        :param request: Request instance for CreatePresignedNotebookInstanceUrl.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreatePresignedNotebookInstanceUrlRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreatePresignedNotebookInstanceUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePresignedNotebookInstanceUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePresignedNotebookInstanceUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrainingJob(self, request):
        """创建训练任务

        :param request: Request instance for CreateTrainingJob.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreateTrainingJobRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreateTrainingJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrainingJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrainingJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeRepository(self, request):
        """删除存储库

        :param request: Request instance for DeleteCodeRepository.
        :type request: :class:`tencentcloud.tione.v20191022.models.DeleteCodeRepositoryRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DeleteCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotebookInstance(self, request):
        """删除notebook实例

        :param request: Request instance for DeleteNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.DeleteNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DeleteNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNotebookInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNotebookInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotebookLifecycleScript(self, request):
        """删除Notebook生命周期脚本

        :param request: Request instance for DeleteNotebookLifecycleScript.
        :type request: :class:`tencentcloud.tione.v20191022.models.DeleteNotebookLifecycleScriptRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DeleteNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNotebookLifecycleScript", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNotebookLifecycleScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeRepositories(self, request):
        """查询存储库列表

        :param request: Request instance for DescribeCodeRepositories.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeCodeRepositoriesRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeCodeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeRepositories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeRepositoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeRepository(self, request):
        """查询存储库详情

        :param request: Request instance for DescribeCodeRepository.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeCodeRepositoryRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookInstance(self, request):
        """查询Notebook实例详情

        :param request: Request instance for DescribeNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookInstances(self, request):
        """查询Notebook实例列表

        :param request: Request instance for DescribeNotebookInstances.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstancesRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookLifecycleScript(self, request):
        """查看notebook生命周期脚本详情

        :param request: Request instance for DescribeNotebookLifecycleScript.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookLifecycleScript", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookLifecycleScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookLifecycleScripts(self, request):
        """查看notebook生命周期脚本列表

        :param request: Request instance for DescribeNotebookLifecycleScripts.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptsRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookLifecycleScripts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookLifecycleScriptsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookSummary(self, request):
        """查询Notebook概览数据

        :param request: Request instance for DescribeNotebookSummary.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookSummaryRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingJob(self, request):
        """查询训练任务

        :param request: Request instance for DescribeTrainingJob.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeTrainingJobRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeTrainingJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingJobs(self, request):
        """查询训练任务列表

        :param request: Request instance for DescribeTrainingJobs.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeTrainingJobsRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeTrainingJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartNotebookInstance(self, request):
        """启动Notebook实例

        :param request: Request instance for StartNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.StartNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.StartNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartNotebookInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StartNotebookInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopNotebookInstance(self, request):
        """停止Notebook实例

        :param request: Request instance for StopNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.StopNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.StopNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopNotebookInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StopNotebookInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopTrainingJob(self, request):
        """停止训练任务

        :param request: Request instance for StopTrainingJob.
        :type request: :class:`tencentcloud.tione.v20191022.models.StopTrainingJobRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.StopTrainingJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTrainingJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopTrainingJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCodeRepository(self, request):
        """更新存储库

        :param request: Request instance for UpdateCodeRepository.
        :type request: :class:`tencentcloud.tione.v20191022.models.UpdateCodeRepositoryRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.UpdateCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCodeRepository", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCodeRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateNotebookInstance(self, request):
        """更新Notebook实例

        :param request: Request instance for UpdateNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.UpdateNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.UpdateNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNotebookInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateNotebookInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))