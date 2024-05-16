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
from tencentcloud.rce.v20201103 import models


class RceClient(AbstractClient):
    _apiVersion = '2020-11-03'
    _endpoint = 'rce.tencentcloudapi.com'
    _service = 'rce'


    def ManageMarketingRisk(self, request):
        """全栈式风控引擎（RiskControlEngine，RCE）是基于人工智能技术和腾讯20年风控实战沉淀，依托腾讯海量业务构建的风控引擎，以轻量级的 SaaS 服务方式接入，帮助您快速解决注册、登录、营销活动等关键场景遇到的欺诈问题，实时防御黑灰产作恶。

        :param request: Request instance for ManageMarketingRisk.
        :type request: :class:`tencentcloud.rce.v20201103.models.ManageMarketingRiskRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.ManageMarketingRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageMarketingRisk", params, headers=headers)
            response = json.loads(body)
            model = models.ManageMarketingRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))