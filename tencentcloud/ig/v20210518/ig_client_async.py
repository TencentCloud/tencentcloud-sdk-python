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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ig.v20210518 import models
from typing import Dict


class IgClient(AbstractClient):
    _apiVersion = '2021-05-18'
    _endpoint = 'ig.tencentcloudapi.com'
    _service = 'ig'

    async def DescribeIgOrderList(
            self,
            request: models.DescribeIgOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeIgOrderListResponse:
        """
        查询智能导诊订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLLMDiagnosisDrug(
            self,
            request: models.GetLLMDiagnosisDrugRequest,
            opts: Dict = None,
    ) -> models.GetLLMDiagnosisDrugResponse:
        """
        大模型问药拍药盒
        """
        
        kwargs = {}
        kwargs["action"] = "GetLLMDiagnosisDrug"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLLMDiagnosisDrugResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLLMDiagnosisDrugChat(
            self,
            request: models.GetLLMDiagnosisDrugChatRequest,
            opts: Dict = None,
    ) -> models.GetLLMDiagnosisDrugChatResponse:
        """
        大模型问药问答
        """
        
        kwargs = {}
        kwargs["action"] = "GetLLMDiagnosisDrugChat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLLMDiagnosisDrugChatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLLMDiagnosisHealth(
            self,
            request: models.GetLLMDiagnosisHealthRequest,
            opts: Dict = None,
    ) -> models.GetLLMDiagnosisHealthResponse:
        """
        大模型健康自诊
        """
        
        kwargs = {}
        kwargs["action"] = "GetLLMDiagnosisHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLLMDiagnosisHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLLMReportInterpretation(
            self,
            request: models.GetLLMReportInterpretationRequest,
            opts: Dict = None,
    ) -> models.GetLLMReportInterpretationResponse:
        """
        大模型报告解读
        """
        
        kwargs = {}
        kwargs["action"] = "GetLLMReportInterpretation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLLMReportInterpretationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDrugInstructions(
            self,
            request: models.QueryDrugInstructionsRequest,
            opts: Dict = None,
    ) -> models.QueryDrugInstructionsResponse:
        """
        查询药品说明书
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDrugInstructions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDrugInstructionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)