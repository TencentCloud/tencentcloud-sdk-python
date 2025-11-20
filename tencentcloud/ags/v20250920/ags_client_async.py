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
from tencentcloud.ags.v20250920 import models
from typing import Dict


class AgsClient(AbstractClient):
    _apiVersion = '2025-09-20'
    _endpoint = 'ags.tencentcloudapi.com'
    _service = 'ags'

    async def AcquireSandboxInstanceToken(
            self,
            request: models.AcquireSandboxInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.AcquireSandboxInstanceTokenResponse:
        """
        获取访问沙箱工具时所需要使用的访问Token，创建沙箱实例后需调用此接口获取沙箱实例访问Token。
        此Token可用于调用代码沙箱实例执行代码，或浏览器沙箱实例进行浏览器操作等。
        """
        
        kwargs = {}
        kwargs["action"] = "AcquireSandboxInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcquireSandboxInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAPIKey(
            self,
            request: models.CreateAPIKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAPIKeyResponse:
        """
        创建新的API密钥，用于调用Agent Sandbox接口。相较于腾讯云Secret ID Secret Key支持调用所有接口使用，仅有部分接口支持使用API密钥调用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAPIKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAPIKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSandboxTool(
            self,
            request: models.CreateSandboxToolRequest,
            opts: Dict = None,
    ) -> models.CreateSandboxToolResponse:
        """
        创建沙箱工具
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSandboxTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSandboxToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAPIKey(
            self,
            request: models.DeleteAPIKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteAPIKeyResponse:
        """
        删除API密钥。注意区别于腾讯云Secret ID Secret Key，本接口删除的是Agent Sandbox专用API key。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAPIKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAPIKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSandboxTool(
            self,
            request: models.DeleteSandboxToolRequest,
            opts: Dict = None,
    ) -> models.DeleteSandboxToolResponse:
        """
        删除沙箱工具
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSandboxTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSandboxToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIKeyList(
            self,
            request: models.DescribeAPIKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIKeyListResponse:
        """
        获取API密钥列表，包含API密钥简略信息，包含名称、创建时间等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxInstanceList(
            self,
            request: models.DescribeSandboxInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxInstanceListResponse:
        """
        查询沙箱实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxToolList(
            self,
            request: models.DescribeSandboxToolListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxToolListResponse:
        """
        查询沙箱工具列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxToolList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxToolListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSandboxInstance(
            self,
            request: models.StartSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.StartSandboxInstanceResponse:
        """
        启动沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "StartSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSandboxInstance(
            self,
            request: models.StopSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.StopSandboxInstanceResponse:
        """
        停止沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSandboxInstance(
            self,
            request: models.UpdateSandboxInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateSandboxInstanceResponse:
        """
        更新沙箱实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSandboxInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSandboxInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSandboxTool(
            self,
            request: models.UpdateSandboxToolRequest,
            opts: Dict = None,
    ) -> models.UpdateSandboxToolResponse:
        """
        更新沙箱工具
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSandboxTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSandboxToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)