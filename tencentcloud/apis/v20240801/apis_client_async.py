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
from tencentcloud.apis.v20240801 import models
from typing import Dict


class ApisClient(AbstractClient):
    _apiVersion = '2024-08-01'
    _endpoint = 'apis.tencentcloudapi.com'
    _service = 'apis'

    async def CreateAgentApp(
            self,
            request: models.CreateAgentAppRequest,
            opts: Dict = None,
    ) -> models.CreateAgentAppResponse:
        """
        创建app
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentAppMcpServers(
            self,
            request: models.CreateAgentAppMcpServersRequest,
            opts: Dict = None,
    ) -> models.CreateAgentAppMcpServersResponse:
        """
        创建app的mcp server关联
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentAppMcpServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentAppMcpServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentAppModelServices(
            self,
            request: models.CreateAgentAppModelServicesRequest,
            opts: Dict = None,
    ) -> models.CreateAgentAppModelServicesResponse:
        """
        创建app的model service关联
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentAppModelServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentAppModelServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentAppServices(
            self,
            request: models.CreateAgentAppServicesRequest,
            opts: Dict = None,
    ) -> models.CreateAgentAppServicesResponse:
        """
        应用关联API
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentAppServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentAppServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentCredential(
            self,
            request: models.CreateAgentCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateAgentCredentialResponse:
        """
        创建Credential
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMcpServer(
            self,
            request: models.CreateMcpServerRequest,
            opts: Dict = None,
    ) -> models.CreateMcpServerResponse:
        """
        创建mcp server
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMcpServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMcpServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModel(
            self,
            request: models.CreateModelRequest,
            opts: Dict = None,
    ) -> models.CreateModelResponse:
        """
        创建模型
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModelService(
            self,
            request: models.CreateModelServiceRequest,
            opts: Dict = None,
    ) -> models.CreateModelServiceResponse:
        """
        创建模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateService(
            self,
            request: models.CreateServiceRequest,
            opts: Dict = None,
    ) -> models.CreateServiceResponse:
        """
        创建服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentApp(
            self,
            request: models.DeleteAgentAppRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentAppResponse:
        """
        删除app
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentAppMcpServers(
            self,
            request: models.DeleteAgentAppMcpServersRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentAppMcpServersResponse:
        """
        删除app的mcp server
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentAppMcpServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentAppMcpServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentAppModelServices(
            self,
            request: models.DeleteAgentAppModelServicesRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentAppModelServicesResponse:
        """
        删除app的model service关联
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentAppModelServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentAppModelServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentAppServices(
            self,
            request: models.DeleteAgentAppServicesRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentAppServicesResponse:
        """
        应用API关联解除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentAppServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentAppServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentCredential(
            self,
            request: models.DeleteAgentCredentialRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentCredentialResponse:
        """
        删除Credential
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMcpServer(
            self,
            request: models.DeleteMcpServerRequest,
            opts: Dict = None,
    ) -> models.DeleteMcpServerResponse:
        """
        删除mcp server
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMcpServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMcpServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModel(
            self,
            request: models.DeleteModelRequest,
            opts: Dict = None,
    ) -> models.DeleteModelResponse:
        """
        删除模型
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModelService(
            self,
            request: models.DeleteModelServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteModelServiceResponse:
        """
        删除模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteService(
            self,
            request: models.DeleteServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceResponse:
        """
        删除服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentApp(
            self,
            request: models.DescribeAgentAppRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentAppResponse:
        """
        查询app详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentAppMcpServers(
            self,
            request: models.DescribeAgentAppMcpServersRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentAppMcpServersResponse:
        """
        查询app mcpServer关联列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentAppMcpServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentAppMcpServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentAppModelServices(
            self,
            request: models.DescribeAgentAppModelServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentAppModelServicesResponse:
        """
        查询app modelService关联列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentAppModelServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentAppModelServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentAppServices(
            self,
            request: models.DescribeAgentAppServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentAppServicesResponse:
        """
        创建app
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentAppServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentAppServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentApps(
            self,
            request: models.DescribeAgentAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentAppsResponse:
        """
        查询app列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentCredential(
            self,
            request: models.DescribeAgentCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentCredentialResponse:
        """
        查询Credential详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentCredentials(
            self,
            request: models.DescribeAgentCredentialsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentCredentialsResponse:
        """
        查询Credential列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMcpServer(
            self,
            request: models.DescribeMcpServerRequest,
            opts: Dict = None,
    ) -> models.DescribeMcpServerResponse:
        """
        查询mcp server详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMcpServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMcpServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMcpServers(
            self,
            request: models.DescribeMcpServersRequest,
            opts: Dict = None,
    ) -> models.DescribeMcpServersResponse:
        """
        查询mcp server列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMcpServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMcpServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModel(
            self,
            request: models.DescribeModelRequest,
            opts: Dict = None,
    ) -> models.DescribeModelResponse:
        """
        查询模型详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelService(
            self,
            request: models.DescribeModelServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceResponse:
        """
        查询模型服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelServices(
            self,
            request: models.DescribeModelServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServicesResponse:
        """
        查询模型服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModels(
            self,
            request: models.DescribeModelsRequest,
            opts: Dict = None,
    ) -> models.DescribeModelsResponse:
        """
        查询模型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeService(
            self,
            request: models.DescribeServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceResponse:
        """
        查询服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServices(
            self,
            request: models.DescribeServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeServicesResponse:
        """
        查询服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentApp(
            self,
            request: models.ModifyAgentAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentAppResponse:
        """
        修改app
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentAppModelServices(
            self,
            request: models.ModifyAgentAppModelServicesRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentAppModelServicesResponse:
        """
        编辑app的model service关联
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentAppModelServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentAppModelServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentCredential(
            self,
            request: models.ModifyAgentCredentialRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentCredentialResponse:
        """
        修改Credential
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMcpServer(
            self,
            request: models.ModifyMcpServerRequest,
            opts: Dict = None,
    ) -> models.ModifyMcpServerResponse:
        """
        修改mcp server
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMcpServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMcpServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModel(
            self,
            request: models.ModifyModelRequest,
            opts: Dict = None,
    ) -> models.ModifyModelResponse:
        """
        修改模型
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModelService(
            self,
            request: models.ModifyModelServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyModelServiceResponse:
        """
        修改模型服务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModelService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModelServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyService(
            self,
            request: models.ModifyServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceResponse:
        """
        修改服务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)