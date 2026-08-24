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


    def AssessRisk(self, request):
        r"""事件风险评估。用于实时获取事件的风险信息，您可以在业务的关键事件中获取到我们根据设备风险、环境风险、账号风险、行为风险以及历史上报的事件信息评估出来的风险决策结果、风险评分和风险标签等。

        :param request: Request instance for AssessRisk.
        :type request: :class:`tencentcloud.rce.v20260130.models.AssessRiskRequest`
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssessRisk", params, headers=headers)
            response = json.loads(body)
            model = models.AssessRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportEvent(self, request):
        r"""事件信息上报。用于上报您业务中无需实时决策的事件，我们会通过引擎计算、机器学习挖掘风险特征用于实时事件风险评估。

        :param request: Request instance for ReportEvent.
        :type request: :class:`tencentcloud.rce.v20260130.models.ReportEventRequest`
        :rtype: :class:`tencentcloud.rce.v20260130.models.ReportEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ReportEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))