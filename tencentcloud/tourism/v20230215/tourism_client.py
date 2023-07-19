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
from tencentcloud.tourism.v20230215 import models


class TourismClient(AbstractClient):
    _apiVersion = '2023-02-15'
    _endpoint = 'tourism.tencentcloudapi.com'
    _service = 'tourism'


    def DescribeDrawResourceList(self, request):
        """依据客户的Uin查询开通的资源列表

        :param request: Request instance for DescribeDrawResourceList.
        :type request: :class:`tencentcloud.tourism.v20230215.models.DescribeDrawResourceListRequest`
        :rtype: :class:`tencentcloud.tourism.v20230215.models.DescribeDrawResourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrawResourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrawResourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))