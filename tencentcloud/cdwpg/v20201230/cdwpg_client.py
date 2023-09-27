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
from tencentcloud.cdwpg.v20201230 import models


class CdwpgClient(AbstractClient):
    _apiVersion = '2020-12-30'
    _endpoint = 'cdwpg.tencentcloudapi.com'
    _service = 'cdwpg'


    def CreateInstanceByApi(self, request):
        """创建集群

        :param request: Request instance for CreateInstanceByApi.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.CreateInstanceByApiRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CreateInstanceByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceByApi", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyInstanceByApi(self, request):
        """销毁集群

        :param request: Request instance for DestroyInstanceByApi.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DestroyInstanceByApiRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DestroyInstanceByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstanceByApi", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))