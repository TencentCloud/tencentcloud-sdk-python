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
from tencentcloud.lp.v20200224 import models


class LpClient(AbstractClient):
    _apiVersion = '2020-02-24'
    _endpoint = 'lp.tencentcloudapi.com'
    _service = 'lp'


    def QueryLoginProtection(self, request):
        """登录保护服务（LoginProtection，LP）针对网站和 APP 的用户登录场景，实时检测是否存在盗号、撞库等恶意登录行为，帮助开发者发现异常登录，降低恶意用户登录给业务带来的风险。

        :param request: Request instance for QueryLoginProtection.
        :type request: :class:`tencentcloud.lp.v20200224.models.QueryLoginProtectionRequest`
        :rtype: :class:`tencentcloud.lp.v20200224.models.QueryLoginProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryLoginProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryLoginProtectionResponse()
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