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
from tencentcloud.mmps.v20200710 import models
from typing import Dict


class MmpsClient(AbstractClient):
    _apiVersion = '2020-07-10'
    _endpoint = 'mmps.tencentcloudapi.com'
    _service = 'mmps'

    async def CreateAppScanTask(
            self,
            request: models.CreateAppScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAppScanTaskResponse:
        """
        创建小程序隐私合规诊断任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAppScanTaskRepeat(
            self,
            request: models.CreateAppScanTaskRepeatRequest,
            opts: Dict = None,
    ) -> models.CreateAppScanTaskRepeatResponse:
        """
        小程序隐私合规诊断重试任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppScanTaskRepeat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppScanTaskRepeatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlySecMiniAppProfessionalScanTask(
            self,
            request: models.CreateFlySecMiniAppProfessionalScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateFlySecMiniAppProfessionalScanTaskResponse:
        """
        创建小程序安全深度诊断任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlySecMiniAppProfessionalScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlySecMiniAppProfessionalScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlySecMiniAppScanTask(
            self,
            request: models.CreateFlySecMiniAppScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateFlySecMiniAppScanTaskResponse:
        """
        创建小程序翼扬安全的基础或深度诊断任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlySecMiniAppScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlySecMiniAppScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlySecMiniAppScanTaskRepeat(
            self,
            request: models.CreateFlySecMiniAppScanTaskRepeatRequest,
            opts: Dict = None,
    ) -> models.CreateFlySecMiniAppScanTaskRepeatResponse:
        """
        重新提交基础诊断任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlySecMiniAppScanTaskRepeat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlySecMiniAppScanTaskRepeatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicDiagnosisResourceUsageInfo(
            self,
            request: models.DescribeBasicDiagnosisResourceUsageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicDiagnosisResourceUsageInfoResponse:
        """
        查询翼扬安全基础诊断资源使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicDiagnosisResourceUsageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicDiagnosisResourceUsageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlySecMiniAppReportUrl(
            self,
            request: models.DescribeFlySecMiniAppReportUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeFlySecMiniAppReportUrlResponse:
        """
        获取翼扬诊断任务报告链接地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlySecMiniAppReportUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlySecMiniAppReportUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlySecMiniAppScanReportList(
            self,
            request: models.DescribeFlySecMiniAppScanReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeFlySecMiniAppScanReportListResponse:
        """
        查询指定小程序版本的翼扬诊断安全得分
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlySecMiniAppScanReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlySecMiniAppScanReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlySecMiniAppScanTaskList(
            self,
            request: models.DescribeFlySecMiniAppScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeFlySecMiniAppScanTaskListResponse:
        """
        获取翼扬安全诊断任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlySecMiniAppScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlySecMiniAppScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlySecMiniAppScanTaskParam(
            self,
            request: models.DescribeFlySecMiniAppScanTaskParamRequest,
            opts: Dict = None,
    ) -> models.DescribeFlySecMiniAppScanTaskParamResponse:
        """
        获取用户提交的基础诊断任务参数信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlySecMiniAppScanTaskParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlySecMiniAppScanTaskParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlySecMiniAppScanTaskStatus(
            self,
            request: models.DescribeFlySecMiniAppScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeFlySecMiniAppScanTaskStatusResponse:
        """
        查询翼扬安全诊断任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlySecMiniAppScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlySecMiniAppScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceUsageInfo(
            self,
            request: models.DescribeResourceUsageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceUsageInfoResponse:
        """
        查询翼扬安全资源使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceUsageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceUsageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskList(
            self,
            request: models.DescribeScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskListResponse:
        """
        获取小程序隐私合规诊断任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskReportUrl(
            self,
            request: models.DescribeScanTaskReportUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskReportUrlResponse:
        """
        获取小程序合规诊断任务报告url
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskReportUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskReportUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskStatus(
            self,
            request: models.DescribeScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskStatusResponse:
        """
        查询小程序隐私合规诊断任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)