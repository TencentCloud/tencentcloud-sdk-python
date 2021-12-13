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
from tencentcloud.cii.v20210408 import models


class CiiClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'cii.tencentcloudapi.com'
    _service = 'cii'


    def CreateAutoClassifyStructureTask(self, request):
        """本接口(CreateAutoClassifyStructureTask)基于提供的客户及保单信息，创建并启动结构化识别任务。

        :param request: Request instance for CreateAutoClassifyStructureTask.
        :type request: :class:`tencentcloud.cii.v20210408.models.CreateAutoClassifyStructureTaskRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.CreateAutoClassifyStructureTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoClassifyStructureTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoClassifyStructureTaskResponse()
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


    def CreateStructureTask(self, request):
        """本接口(CreateStructureTask)基于提供的客户及保单信息，创建并启动结构化识别任务。

        :param request: Request instance for CreateStructureTask.
        :type request: :class:`tencentcloud.cii.v20210408.models.CreateStructureTaskRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.CreateStructureTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStructureTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStructureTaskResponse()
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


    def CreateUnderwriteTaskById(self, request):
        """本接口(CreateUnderwriteTaskById)用于根据结构化任务ID创建核保任务

        :param request: Request instance for CreateUnderwriteTaskById.
        :type request: :class:`tencentcloud.cii.v20210408.models.CreateUnderwriteTaskByIdRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.CreateUnderwriteTaskByIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUnderwriteTaskById", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUnderwriteTaskByIdResponse()
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


    def DescribeMachineUnderwrite(self, request):
        """本接口(DescribeMachineUnderwrite)用于查询机器核保任务数据

        :param request: Request instance for DescribeMachineUnderwrite.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeMachineUnderwriteRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeMachineUnderwriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachineUnderwrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineUnderwriteResponse()
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


    def DescribeStructCompareData(self, request):
        """结构化对比查询接口，对比结构化复核前后数据差异，查询识别正确率，召回率。

        :param request: Request instance for DescribeStructCompareData.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructCompareDataRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructCompareDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStructCompareData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStructCompareDataResponse()
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


    def DescribeStructureDifference(self, request):
        """结构化复核差异查询接口，对比结构化复核前后数据差异，返回差异的部分。

        :param request: Request instance for DescribeStructureDifference.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructureDifferenceRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructureDifferenceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStructureDifference", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStructureDifferenceResponse()
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


    def DescribeStructureResult(self, request):
        """本接口(DescribeStructureResult)用于查询结构化结果接口

        :param request: Request instance for DescribeStructureResult.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructureResultRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructureResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStructureResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStructureResultResponse()
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


    def DescribeStructureTaskResult(self, request):
        """依据任务ID获取结构化结果接口。

        :param request: Request instance for DescribeStructureTaskResult.
        :type request: :class:`tencentcloud.cii.v20210408.models.DescribeStructureTaskResultRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.DescribeStructureTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStructureTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStructureTaskResultResponse()
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


    def UploadMedicalFile(self, request):
        """上传医疗影像文件，可以用来做结构化。

        :param request: Request instance for UploadMedicalFile.
        :type request: :class:`tencentcloud.cii.v20210408.models.UploadMedicalFileRequest`
        :rtype: :class:`tencentcloud.cii.v20210408.models.UploadMedicalFileResponse`

        """
        try:
            params = request._serialize()
            options = {'IsMultipart': True, 'BinaryParams': [u'File']}
            body = self.call("UploadMedicalFile", params, options=options)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadMedicalFileResponse()
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