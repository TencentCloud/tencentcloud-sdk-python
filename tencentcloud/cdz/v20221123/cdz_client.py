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
from tencentcloud.cdz.v20221123 import models


class CdzClient(AbstractClient):
    _apiVersion = '2022-11-23'
    _endpoint = 'cdz.tencentcloudapi.com'
    _service = 'cdz'


    def DescribeCloudDedicatedZoneHosts(self, request):
        r"""查询可用区的Host和Host上部署的实例

        :param request: Request instance for DescribeCloudDedicatedZoneHosts.
        :type request: :class:`tencentcloud.cdz.v20221123.models.DescribeCloudDedicatedZoneHostsRequest`
        :rtype: :class:`tencentcloud.cdz.v20221123.models.DescribeCloudDedicatedZoneHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudDedicatedZoneHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudDedicatedZoneHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudDedicatedZoneResourceSummary(self, request):
        r"""查询专属可用区各个垂直产品的资源使用情况

        :param request: Request instance for DescribeCloudDedicatedZoneResourceSummary.
        :type request: :class:`tencentcloud.cdz.v20221123.models.DescribeCloudDedicatedZoneResourceSummaryRequest`
        :rtype: :class:`tencentcloud.cdz.v20221123.models.DescribeCloudDedicatedZoneResourceSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudDedicatedZoneResourceSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudDedicatedZoneResourceSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))