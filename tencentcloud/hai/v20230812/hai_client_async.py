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
from tencentcloud.hai.v20230812 import models
from typing import Dict


class HaiClient(AbstractClient):
    _apiVersion = '2023-08-12'
    _endpoint = 'hai.tencentcloudapi.com'
    _service = 'hai'

    async def CreateApplication(
            self,
            request: models.CreateApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationResponse:
        """
        本接口（CreateApplication）用于对HAI实例制作自定义应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMuskPrompt(
            self,
            request: models.CreateMuskPromptRequest,
            opts: Dict = None,
    ) -> models.CreateMuskPromptResponse:
        """
        创建musk prompt 任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMuskPrompt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMuskPromptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplications(
            self,
            request: models.DescribeApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsResponse:
        """
        本接口（DescribeApplications）用于查询应用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNetworkStatus(
            self,
            request: models.DescribeInstanceNetworkStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNetworkStatusResponse:
        """
        本接口（DescribeInstanceNetworkStatus）用于查询实例的网络配置及消耗情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNetworkStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNetworkStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        本接口（DescribeInstances）用户查询实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMuskPrompts(
            self,
            request: models.DescribeMuskPromptsRequest,
            opts: Dict = None,
    ) -> models.DescribeMuskPromptsResponse:
        """
        获取prompt任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMuskPrompts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMuskPromptsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        本接口（DescribeRegions）用于查询地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenes(
            self,
            request: models.DescribeScenesRequest,
            opts: Dict = None,
    ) -> models.DescribeScenesResponse:
        """
        本接口（DescribeScenes）用于查询场景
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceLoginSettings(
            self,
            request: models.DescribeServiceLoginSettingsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceLoginSettingsResponse:
        """
        本接口（DescribeServiceLoginSettings）用于查询服务登录配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceLoginSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceLoginSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRunInstances(
            self,
            request: models.InquirePriceRunInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRunInstancesResponse:
        """
        本接口 (InquirePriceRunInstances) 用于实例询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRunInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRunInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesPassword(
            self,
            request: models.ResetInstancesPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesPasswordResponse:
        """
        本接口 (ResetInstancesPassword) 用于重置实例的用户密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeInstanceDisk(
            self,
            request: models.ResizeInstanceDiskRequest,
            opts: Dict = None,
    ) -> models.ResizeInstanceDiskResponse:
        """
        本接口（ResizeInstanceDisk）用于对指定HAI实例进行扩容云硬盘操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeInstanceDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeInstanceDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunInstances(
            self,
            request: models.RunInstancesRequest,
            opts: Dict = None,
    ) -> models.RunInstancesResponse:
        """
        本接口 (RunInstances) 用于创建一个或多个指定配置的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RunInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstance(
            self,
            request: models.StartInstanceRequest,
            opts: Dict = None,
    ) -> models.StartInstanceResponse:
        """
        本接口 (StartInstance) 用于主动启动实例。
        ‘运行中’、‘预付费’的实例不支持启动实例
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstance(
            self,
            request: models.StopInstanceRequest,
            opts: Dict = None,
    ) -> models.StopInstanceResponse:
        """
        本接口 (StopInstance) 用于主动关闭实例。
        ‘已关机’、‘预付费’的实例不支持关机
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        本接口 (TerminateInstances) 用于主动退还实例。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)