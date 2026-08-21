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
from tencentcloud.cloudrc.v20240606 import models


class CloudrcClient(AbstractClient):
    _apiVersion = '2024-06-06'
    _endpoint = 'cloudrc.tencentcloudapi.com'
    _service = 'cloudrc'


    def DescribeResource(self, request):
        r"""查询资源详情

        :param request: Request instance for DescribeResource.
        :type request: :class:`tencentcloud.cloudrc.v20240606.models.DescribeResourceRequest`
        :rtype: :class:`tencentcloud.cloudrc.v20240606.models.DescribeResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchResources(self, request):
        r"""搜索资源

        :param request: Request instance for SearchResources.
        :type request: :class:`tencentcloud.cloudrc.v20240606.models.SearchResourcesRequest`
        :rtype: :class:`tencentcloud.cloudrc.v20240606.models.SearchResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchResources", params, headers=headers)
            response = json.loads(body)
            model = models.SearchResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))