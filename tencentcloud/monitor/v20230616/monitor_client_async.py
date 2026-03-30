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
from tencentcloud.monitor.v20230616 import models
from typing import Dict


class MonitorClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'

    async def CreateNoticeContentTmpl(
            self,
            request: models.CreateNoticeContentTmplRequest,
            opts: Dict = None,
    ) -> models.CreateNoticeContentTmplResponse:
        """
        创建自定义通知内容模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNoticeContentTmpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNoticeContentTmplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNoticeContentTmpls(
            self,
            request: models.DeleteNoticeContentTmplsRequest,
            opts: Dict = None,
    ) -> models.DeleteNoticeContentTmplsResponse:
        """
        删除通知内容模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNoticeContentTmpls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNoticeContentTmplsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSREDigitalTwinTaskList(
            self,
            request: models.DescribeAIWorkbenchSREDigitalTwinTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSREDigitalTwinTaskListResponse:
        """
        查询AI工作台SRE数字分身任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSREDigitalTwinTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSREDigitalTwinTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSREDigitalTwinWorkLogDetail(
            self,
            request: models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse:
        """
        查询AI工作台SRE数字分身工作日志详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSREDigitalTwinWorkLogDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSREDigitalTwinWorkLogList(
            self,
            request: models.DescribeAIWorkbenchSREDigitalTwinWorkLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse:
        """
        查询AI工作台SRE数字分身任务工作日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSREDigitalTwinWorkLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotifyHistories(
            self,
            request: models.DescribeAlarmNotifyHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNotifyHistoriesResponse:
        """
        按需查询告警的通知历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotifyHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNotifyHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNoticeContentTmpl(
            self,
            request: models.DescribeNoticeContentTmplRequest,
            opts: Dict = None,
    ) -> models.DescribeNoticeContentTmplResponse:
        """
        根据查询条件获取自定义通知内容模板，若所有查询条件空，则获取账号下所有模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNoticeContentTmpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNoticeContentTmplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNoticeContentTmpl(
            self,
            request: models.ModifyNoticeContentTmplRequest,
            opts: Dict = None,
    ) -> models.ModifyNoticeContentTmplResponse:
        """
        修改通知内容模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNoticeContentTmpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNoticeContentTmplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerAIWorkbenchSREDigitalTwinTask(
            self,
            request: models.TriggerAIWorkbenchSREDigitalTwinTaskRequest,
            opts: Dict = None,
    ) -> models.TriggerAIWorkbenchSREDigitalTwinTaskResponse:
        """
        触发数字分身任务请求
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerAIWorkbenchSREDigitalTwinTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerAIWorkbenchSREDigitalTwinTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)