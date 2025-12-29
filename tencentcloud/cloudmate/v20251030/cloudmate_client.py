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
from tencentcloud.cloudmate.v20251030 import models


class CloudmateClient(AbstractClient):
    _apiVersion = '2025-10-30'
    _endpoint = 'cloudmate.tencentcloudapi.com'
    _service = 'cloudmate'


    def CloudMateAgent(self, request):
        r"""发起智能诊断对话
        注意：使用该API时，请务必设置请求域名（Endpoint）为 cloudmate.ai.tencentcloudapi.com

        :param request: Request instance for CloudMateAgent.
        :type request: :class:`tencentcloud.cloudmate.v20251030.models.CloudMateAgentRequest`
        :rtype: :class:`tencentcloud.cloudmate.v20251030.models.CloudMateAgentResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("CloudMateAgent", params, models.CloudMateAgentResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))