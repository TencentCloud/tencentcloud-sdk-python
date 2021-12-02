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
from tencentcloud.apm.v20210622 import models


class ApmClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'apm.tencentcloudapi.com'
    _service = 'apm'


    def CreateApmInstance(self, request):
        """业务购买APM实例，调用该接口创建

        :param request: Request instance for CreateApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.CreateApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.CreateApmInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApmInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApmInstanceResponse()
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


    def DescribeApmAgent(self, request):
        """获取Apm Agent信息

        :param request: Request instance for DescribeApmAgent.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmAgentRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmAgentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApmAgent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApmAgentResponse()
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


    def DescribeApmInstances(self, request):
        """APM实例列表拉取

        :param request: Request instance for DescribeApmInstances.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmInstancesRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApmInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApmInstancesResponse()
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