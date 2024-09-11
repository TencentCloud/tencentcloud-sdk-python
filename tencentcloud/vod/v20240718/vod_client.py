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
from tencentcloud.vod.v20240718 import models


class VodClient(AbstractClient):
    _apiVersion = '2024-07-18'
    _endpoint = 'vod.tencentcloudapi.com'
    _service = 'vod'


    def CreateStorageCredentials(self, request):
        """用于按指定策略，生成专业版应用的临时访问凭证，比如生成用于客户端上传的临时凭证。

        :param request: Request instance for CreateStorageCredentials.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateStorageCredentialsRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateStorageCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorageCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))