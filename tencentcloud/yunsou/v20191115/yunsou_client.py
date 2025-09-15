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
from tencentcloud.yunsou.v20191115 import models


class YunsouClient(AbstractClient):
    _apiVersion = '2019-11-15'
    _endpoint = 'yunsou.tencentcloudapi.com'
    _service = 'yunsou'


    def DataManipulation(self, request):
        r"""上传云搜数据的API接口。

        :param request: Request instance for DataManipulation.
        :type request: :class:`tencentcloud.yunsou.v20191115.models.DataManipulationRequest`
        :rtype: :class:`tencentcloud.yunsou.v20191115.models.DataManipulationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DataManipulation", params, headers=headers)
            response = json.loads(body)
            model = models.DataManipulationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DataSearch(self, request):
        r"""用于检索云搜中的数据。

        :param request: Request instance for DataSearch.
        :type request: :class:`tencentcloud.yunsou.v20191115.models.DataSearchRequest`
        :rtype: :class:`tencentcloud.yunsou.v20191115.models.DataSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DataSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DataSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))