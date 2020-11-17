# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.rp.v20200224 import models


class RpClient(AbstractClient):
    _apiVersion = '2020-02-24'
    _endpoint = 'rp.tencentcloudapi.com'
    _service = 'rp'


    def QueryRegisterProtection(self, request):
        """注册保护服务（RegisterProtection，RP）针对网站、APP 的线上注册场景，遇到 “恶意注册” 、“小号注册” 、“注册器注册” 等恶意行为，提供基于天御 DNA 算法的恶意防护引擎，从账号、设备、行为三个维度有效识别 “恶意注册”，从“源头”上防范业务风险。

        :param request: Request instance for QueryRegisterProtection.
        :type request: :class:`tencentcloud.rp.v20200224.models.QueryRegisterProtectionRequest`
        :rtype: :class:`tencentcloud.rp.v20200224.models.QueryRegisterProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryRegisterProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryRegisterProtectionResponse()
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