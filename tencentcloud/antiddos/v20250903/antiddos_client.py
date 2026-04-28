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
from tencentcloud.antiddos.v20250903 import models


class AntiddosClient(AbstractClient):
    _apiVersion = '2025-09-03'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'


    def DescribeDDoSBlockRecords(self, request):
        r"""查询封堵解封记录和解封配额信息。

        :param request: Request instance for DescribeDDoSBlockRecords.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DescribeDDoSBlockRecordsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DescribeDDoSBlockRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSBlockRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSBlockRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnblockResources(self, request):
        r"""申请解封资源，可通过 DescribeDDoSBlockRecords 接口获取资源的封堵解封状态。

        :param request: Request instance for UnblockResources.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.UnblockResourcesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.UnblockResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnblockResources", params, headers=headers)
            response = json.loads(body)
            model = models.UnblockResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))