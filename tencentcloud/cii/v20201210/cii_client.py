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
from tencentcloud.cii.v20201210 import models


class CiiClient(AbstractClient):
    _apiVersion = '2020-12-10'
    _endpoint = 'cii.tencentcloudapi.com'
    _service = 'cii'


    def CreateStructureTask(self, request):
        r"""基于提供的客户及保单信息，启动结构化识别任务。

        :param request: Request instance for CreateStructureTask.
        :type request: :class:`tencentcloud.cii.v20201210.models.CreateStructureTaskRequest`
        :rtype: :class:`tencentcloud.cii.v20201210.models.CreateStructureTaskResponse`

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


    def DescribeStructCompareData(self, request):
        r"""结构化对比查询接口，对比结构化复核前后数据差异，查询识别正确率，召回率。

        :param request: Request instance for DescribeStructCompareData.
        :type request: :class:`tencentcloud.cii.v20201210.models.DescribeStructCompareDataRequest`
        :rtype: :class:`tencentcloud.cii.v20201210.models.DescribeStructCompareDataResponse`

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


    def DescribeStructureTaskResult(self, request):
        r"""依据任务ID获取结构化结果接口。

        :param request: Request instance for DescribeStructureTaskResult.
        :type request: :class:`tencentcloud.cii.v20201210.models.DescribeStructureTaskResultRequest`
        :rtype: :class:`tencentcloud.cii.v20201210.models.DescribeStructureTaskResultResponse`

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