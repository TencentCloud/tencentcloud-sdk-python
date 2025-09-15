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
from tencentcloud.region.v20220627 import models


class RegionClient(AbstractClient):
    _apiVersion = '2022-06-27'
    _endpoint = 'region.tencentcloudapi.com'
    _service = 'region'


    def DescribeProducts(self, request):
        r"""本接口(DescribeProducts)用于查询各个支持地域列表查询的产品信息。

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.region.v20220627.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.region.v20220627.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        r"""本接口(DescribeRegions)用于查询各个产品支持地域信息。

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.region.v20220627.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.region.v20220627.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""本接口(DescribeZones)用于查询产品可用区信息。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.region.v20220627.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.region.v20220627.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))