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
from tencentcloud.cii.v20201210 import models
from typing import Dict


class CiiClient(AbstractClient):
    _apiVersion = '2020-12-10'
    _endpoint = 'cii.tencentcloudapi.com'
    _service = 'cii'

    async def CreateStructureTask(
            self,
            request: models.CreateStructureTaskRequest,
            opts: Dict = None,
    ) -> models.CreateStructureTaskResponse:
        """
        基于提供的客户及保单信息，启动结构化识别任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStructureTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStructureTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStructCompareData(
            self,
            request: models.DescribeStructCompareDataRequest,
            opts: Dict = None,
    ) -> models.DescribeStructCompareDataResponse:
        """
        结构化对比查询接口，对比结构化复核前后数据差异，查询识别正确率，召回率。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStructCompareData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStructCompareDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStructureTaskResult(
            self,
            request: models.DescribeStructureTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeStructureTaskResultResponse:
        """
        依据任务ID获取结构化结果接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStructureTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStructureTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)