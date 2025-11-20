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
from tencentcloud.cii.v20210408 import models
from typing import Dict


class CiiClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'cii.tencentcloudapi.com'
    _service = 'cii'

    async def AddSubStructureTasks(
            self,
            request: models.AddSubStructureTasksRequest,
            opts: Dict = None,
    ) -> models.AddSubStructureTasksResponse:
        """
        如果主任务下的报告不满足需求，可以基于主任务批量添加子任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddSubStructureTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSubStructureTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoClassifyStructureTask(
            self,
            request: models.CreateAutoClassifyStructureTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAutoClassifyStructureTaskResponse:
        """
        本接口(CreateAutoClassifyStructureTask)基于提供的客户及保单信息，创建并启动结构化识别任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoClassifyStructureTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoClassifyStructureTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStructureTask(
            self,
            request: models.CreateStructureTaskRequest,
            opts: Dict = None,
    ) -> models.CreateStructureTaskResponse:
        """
        本接口(CreateStructureTask)基于提供的客户及保单信息，创建并启动结构化识别任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStructureTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStructureTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUnderwriteTaskById(
            self,
            request: models.CreateUnderwriteTaskByIdRequest,
            opts: Dict = None,
    ) -> models.CreateUnderwriteTaskByIdResponse:
        """
        本接口(CreateUnderwriteTaskById)用于根据结构化任务ID创建核保任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUnderwriteTaskById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUnderwriteTaskByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineUnderwrite(
            self,
            request: models.DescribeMachineUnderwriteRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineUnderwriteResponse:
        """
        本接口(DescribeMachineUnderwrite)用于查询机器核保任务数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineUnderwrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineUnderwriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityScore(
            self,
            request: models.DescribeQualityScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityScoreResponse:
        """
        获取图片质量分
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        kwargs["opts"].update({"IsMultipart": True, "BinaryParams": [u'File']})
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportClassify(
            self,
            request: models.DescribeReportClassifyRequest,
            opts: Dict = None,
    ) -> models.DescribeReportClassifyResponse:
        """
        辅助用户对批量报告自动分类
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportClassify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportClassifyResponse
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
        
    async def DescribeStructureDifference(
            self,
            request: models.DescribeStructureDifferenceRequest,
            opts: Dict = None,
    ) -> models.DescribeStructureDifferenceResponse:
        """
        结构化复核差异查询接口，对比结构化复核前后数据差异，返回差异的部分。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStructureDifference"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStructureDifferenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStructureResult(
            self,
            request: models.DescribeStructureResultRequest,
            opts: Dict = None,
    ) -> models.DescribeStructureResultResponse:
        """
        本接口(DescribeStructureResult)用于查询结构化结果接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStructureResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStructureResultResponse
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
        
    async def DescribeUnderwriteTask(
            self,
            request: models.DescribeUnderwriteTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeUnderwriteTaskResponse:
        """
        本接口(DescribeUnderwriteTask)用于查询核保任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnderwriteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnderwriteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadMedicalFile(
            self,
            request: models.UploadMedicalFileRequest,
            opts: Dict = None,
    ) -> models.UploadMedicalFileResponse:
        """
        上传医疗影像文件，可以用来做结构化。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadMedicalFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadMedicalFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        kwargs["opts"].update({"IsMultipart": True, "BinaryParams": [u'File']})
        
        return await self.call_and_deserialize(**kwargs)