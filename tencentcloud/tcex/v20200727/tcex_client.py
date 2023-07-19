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
from tencentcloud.tcex.v20200727 import models


class TcexClient(AbstractClient):
    _apiVersion = '2020-07-27'
    _endpoint = 'tcex.tencentcloudapi.com'
    _service = 'tcex'


    def DescribeInvocationResult(self, request):
        """产品控制台已经下线

        获取服务调用结果。和InvokeService接口配置合适，其InvokeId参数为InvokeService接口返回的RequestId。

        :param request: Request instance for DescribeInvocationResult.
        :type request: :class:`tencentcloud.tcex.v20200727.models.DescribeInvocationResultRequest`
        :rtype: :class:`tencentcloud.tcex.v20200727.models.DescribeInvocationResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeService(self, request):
        """产品控制台已经下线

        通过传入文档url，测试服务算法。此接口需要和DescribeInvocationResult接口配置使用，该接口使用InvokeService返回的RequestId作为InvokeId参数，用于查询调用结果。

        :param request: Request instance for InvokeService.
        :type request: :class:`tencentcloud.tcex.v20200727.models.InvokeServiceRequest`
        :rtype: :class:`tencentcloud.tcex.v20200727.models.InvokeServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeService", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))