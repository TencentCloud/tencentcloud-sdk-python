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
from tencentcloud.acp.v20220105 import models
from typing import Dict


class AcpClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'acp.tencentcloudapi.com'
    _service = 'acp'

    async def CreateAppScanTask(
            self,
            request: models.CreateAppScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAppScanTaskResponse:
        """
        创建应用合规隐私诊断任务
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
        App应用合规隐私诊断重试任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppScanTaskRepeat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppScanTaskRepeatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChannelTaskReportUrl(
            self,
            request: models.DescribeChannelTaskReportUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeChannelTaskReportUrlResponse:
        """
        获取子渠道的App合规诊断任务报告url
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChannelTaskReportUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChannelTaskReportUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTicket(
            self,
            request: models.DescribeFileTicketRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTicketResponse:
        """
        获取应用合规文件上传凭证，用于上传诊断文件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTicket"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTicketResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceUsageInfo(
            self,
            request: models.DescribeResourceUsageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceUsageInfoResponse:
        """
        查询应用合规平台用户资源的使用情况
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
        获取App隐私合规诊断任务列表
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
        获取App合规诊断任务报告url
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
        查询App隐私合规诊断任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)