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
from tencentcloud.rce.v20260130 import models


class RceClient(AbstractClient):
    _apiVersion = '2026-01-30'
    _endpoint = 'rce.tencentcloudapi.com'
    _service = 'rce'


    def AssessDeviceRiskPremiumPro(self, request):
        r"""设备风险评估-高级版

        :param request: Request instance for AssessDeviceRiskPremiumPro.
        :type request: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskPremiumProRequest`
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskPremiumProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssessDeviceRiskPremiumPro", params, headers=headers)
            response = json.loads(body)
            model = models.AssessDeviceRiskPremiumProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssessDeviceRiskPro(self, request):
        r"""设备风险评估-基础版

        :param request: Request instance for AssessDeviceRiskPro.
        :type request: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskProRequest`
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssessDeviceRiskPro", params, headers=headers)
            response = json.loads(body)
            model = models.AssessDeviceRiskProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssessEnvironmentRisk(self, request):
        r"""环境风险评估

        :param request: Request instance for AssessEnvironmentRisk.
        :type request: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRequest`
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssessEnvironmentRisk", params, headers=headers)
            response = json.loads(body)
            model = models.AssessEnvironmentRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))