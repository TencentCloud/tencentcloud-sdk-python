# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.ie.v20200304 import models


class IeClient(AbstractClient):
    _apiVersion = '2020-03-04'
    _endpoint = 'ie.tencentcloudapi.com'


    def CreateEditingTask(self, request):
        """创建智能编辑任务，可以同时选择视频标签识别、分类识别、智能拆条、智能集锦、智能封面和片头片尾识别中的一项或者多项能力。

        :param request: Request instance for CreateEditingTask.
        :type request: :class:`tencentcloud.ie.v20200304.models.CreateEditingTaskRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.CreateEditingTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEditingTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEditingTaskResponse()
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


    def DescribeEditingTaskResult(self, request):
        """获取智能编辑任务结果。

        :param request: Request instance for DescribeEditingTaskResult.
        :type request: :class:`tencentcloud.ie.v20200304.models.DescribeEditingTaskResultRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.DescribeEditingTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEditingTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEditingTaskResultResponse()
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