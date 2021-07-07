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
from tencentcloud.yunsou.v20180504 import models


class YunsouClient(AbstractClient):
    _apiVersion = '2018-05-04'
    _endpoint = 'yunsou.tencentcloudapi.com'
    _service = 'yunsou'


    def DataManipulation(self, request):
        """上传云搜数据的API接口

        :param request: Request instance for DataManipulation.
        :type request: :class:`tencentcloud.yunsou.v20180504.models.DataManipulationRequest`
        :rtype: :class:`tencentcloud.yunsou.v20180504.models.DataManipulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DataManipulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DataManipulationResponse()
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


    def DataSearch(self, request):
        """用于检索云搜中的数据

        :param request: Request instance for DataSearch.
        :type request: :class:`tencentcloud.yunsou.v20180504.models.DataSearchRequest`
        :rtype: :class:`tencentcloud.yunsou.v20180504.models.DataSearchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DataSearch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DataSearchResponse()
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