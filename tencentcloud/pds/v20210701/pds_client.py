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
from tencentcloud.pds.v20210701 import models


class PdsClient(AbstractClient):
    _apiVersion = '2021-07-01'
    _endpoint = 'pds.tencentcloudapi.com'
    _service = 'pds'


    def DescribeNewUserAcquisition(self, request):
        """判断新用户信誉值

        :param request: Request instance for DescribeNewUserAcquisition.
        :type request: :class:`tencentcloud.pds.v20210701.models.DescribeNewUserAcquisitionRequest`
        :rtype: :class:`tencentcloud.pds.v20210701.models.DescribeNewUserAcquisitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNewUserAcquisition", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNewUserAcquisitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStockEstimation(self, request):
        """查询存量判断服务

        :param request: Request instance for DescribeStockEstimation.
        :type request: :class:`tencentcloud.pds.v20210701.models.DescribeStockEstimationRequest`
        :rtype: :class:`tencentcloud.pds.v20210701.models.DescribeStockEstimationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStockEstimation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStockEstimationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))