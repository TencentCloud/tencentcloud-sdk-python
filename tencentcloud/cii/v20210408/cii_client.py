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
from tencentcloud.cii.v20210408 import models


class CiiClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'cii.tencentcloudapi.com'
    _service = 'cii'


    def AddSubStructureTasks(self, request):
        r"""如果主任务下的报告不满足需求，可以基于主任务批量添加子任务

        :param request: Request instance for AddSubStructureTasks.
        :type request: :class:`tencentcloud.cii.v20210408.models.AddSubStructureTasksRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.AddSubStructureTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSubStructureTasks", params, headers=headers)
            response = json.loads(body)
            model = models.AddSubStructureTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoClassifyStructureTask(self, request):
        r"""本接口(CreateAutoClassifyStructureTask)基于提供的客户及保单信息，创建并启动结构化识别任务。

        :param request: Request instance for CreateAutoClassifyStructureTask.
        :type request: :class:`tencentcloud.cii.v20210408.models.CreateAutoClassifyStructureTaskRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.CreateAutoClassifyStructureTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoClassifyStructureTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoClassifyStructureTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStructureTask(self, request):
        r"""本接口(CreateStructureTask)基于提供的客户及保单信息，创建并启动结构化识别任务。

        :param request: Request instance for CreateStructureTask.
        :type request: :class:`tencentcloud.cii.v20210408.models.CreateStructureTaskRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.CreateStructureTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStructureTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStructureTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUnderwriteTaskById(self, request):
        r"""本接口(CreateUnderwriteTaskById)用于根据结构化任务ID创建核保任务

        :param request: Request instance for CreateUnderwriteTaskById.
        :type request: :class:`tencentcloud.cii.v20210408.models.CreateUnderwriteTaskByIdRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.CreateUnderwriteTaskByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUnderwriteTaskById", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUnderwriteTaskByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineUnderwrite(self, request):
        r"""本接口(DescribeMachineUnderwrite)用于查询机器核保任务数据

        :param request: Request instance for DescribeMachineUnderwrite.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeMachineUnderwriteRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeMachineUnderwriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineUnderwrite", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineUnderwriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityScore(self, request):
        r"""获取图片质量分

        :param request: Request instance for DescribeQualityScore.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeQualityScoreRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeQualityScoreResponse`

        """
        try:
            params = request._serialize()
            options = {'IsMultipart': True, 'BinaryParams': [u'File']}
            headers = request.headers
            body = self.call("DescribeQualityScore", params, options=options, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportClassify(self, request):
        r"""辅助用户对批量报告自动分类

        :param request: Request instance for DescribeReportClassify.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeReportClassifyRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeReportClassifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportClassify", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportClassifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStructCompareData(self, request):
        r"""结构化对比查询接口，对比结构化复核前后数据差异，查询识别正确率，召回率。

        :param request: Request instance for DescribeStructCompareData.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructCompareDataRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructCompareDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStructCompareData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStructCompareDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStructureDifference(self, request):
        r"""结构化复核差异查询接口，对比结构化复核前后数据差异，返回差异的部分。

        :param request: Request instance for DescribeStructureDifference.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructureDifferenceRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructureDifferenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStructureDifference", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStructureDifferenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStructureResult(self, request):
        r"""本接口(DescribeStructureResult)用于查询结构化结果接口

        :param request: Request instance for DescribeStructureResult.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructureResultRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructureResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStructureResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStructureResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStructureTaskResult(self, request):
        r"""依据任务ID获取结构化结果接口。

        :param request: Request instance for DescribeStructureTaskResult.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructureTaskResultRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructureTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStructureTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStructureTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnderwriteTask(self, request):
        r"""本接口(DescribeUnderwriteTask)用于查询核保任务结果

        :param request: Request instance for DescribeUnderwriteTask.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeUnderwriteTaskRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeUnderwriteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnderwriteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnderwriteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadMedicalFile(self, request):
        r"""上传医疗影像文件，可以用来做结构化。

        :param request: Request instance for UploadMedicalFile.
        :type request: :class:`tencentcloud.cii.v20210408.models.UploadMedicalFileRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.UploadMedicalFileResponse`

        """
        try:
            params = request._serialize()
            options = {'IsMultipart': True, 'BinaryParams': [u'File']}
            headers = request.headers
            body = self.call("UploadMedicalFile", params, options=options, headers=headers)
            response = json.loads(body)
            model = models.UploadMedicalFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))