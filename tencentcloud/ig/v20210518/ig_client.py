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
from tencentcloud.ig.v20210518 import models


class IgClient(AbstractClient):
    _apiVersion = '2021-05-18'
    _endpoint = 'ig.tencentcloudapi.com'
    _service = 'ig'


    def DescribeIgOrderList(self, request):
        r"""查询智能导诊订单列表

        :param request: Request instance for DescribeIgOrderList.
        :type request: :class:`tencentcloud.ig.v20210518.models.DescribeIgOrderListRequest`
        :rtype: :class:`tencentcloud.ig.v20210518.models.DescribeIgOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLLMDiagnosisDrug(self, request):
        r"""大模型问药拍药盒

        :param request: Request instance for GetLLMDiagnosisDrug.
        :type request: :class:`tencentcloud.ig.v20210518.models.GetLLMDiagnosisDrugRequest`
        :rtype: :class:`tencentcloud.ig.v20210518.models.GetLLMDiagnosisDrugResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetLLMDiagnosisDrug", params, models.GetLLMDiagnosisDrugResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLLMDiagnosisDrugChat(self, request):
        r"""大模型问药问答

        :param request: Request instance for GetLLMDiagnosisDrugChat.
        :type request: :class:`tencentcloud.ig.v20210518.models.GetLLMDiagnosisDrugChatRequest`
        :rtype: :class:`tencentcloud.ig.v20210518.models.GetLLMDiagnosisDrugChatResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetLLMDiagnosisDrugChat", params, models.GetLLMDiagnosisDrugChatResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLLMDiagnosisHealth(self, request):
        r"""大模型健康自诊

        :param request: Request instance for GetLLMDiagnosisHealth.
        :type request: :class:`tencentcloud.ig.v20210518.models.GetLLMDiagnosisHealthRequest`
        :rtype: :class:`tencentcloud.ig.v20210518.models.GetLLMDiagnosisHealthResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetLLMDiagnosisHealth", params, models.GetLLMDiagnosisHealthResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLLMReportInterpretation(self, request):
        r"""大模型报告解读

        :param request: Request instance for GetLLMReportInterpretation.
        :type request: :class:`tencentcloud.ig.v20210518.models.GetLLMReportInterpretationRequest`
        :rtype: :class:`tencentcloud.ig.v20210518.models.GetLLMReportInterpretationResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetLLMReportInterpretation", params, models.GetLLMReportInterpretationResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDrugInstructions(self, request):
        r"""查询药品说明书

        :param request: Request instance for QueryDrugInstructions.
        :type request: :class:`tencentcloud.ig.v20210518.models.QueryDrugInstructionsRequest`
        :rtype: :class:`tencentcloud.ig.v20210518.models.QueryDrugInstructionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDrugInstructions", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDrugInstructionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))