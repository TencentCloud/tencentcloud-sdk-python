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
from tencentcloud.cloudstudio.v20230508 import models
from typing import Dict


class CloudstudioClient(AbstractClient):
    _apiVersion = '2023-05-08'
    _endpoint = 'cloudstudio.tencentcloudapi.com'
    _service = 'cloudstudio'

    async def CreateWorkspace(
            self,
            request: models.CreateWorkspaceRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceResponse:
        """
        创建工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspaceToken(
            self,
            request: models.CreateWorkspaceTokenRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceTokenResponse:
        """
        创建工作空间临时访问凭证，重复调用会创建新的 Token，旧的 Token 将会自动失效
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspaceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfig(
            self,
            request: models.DescribeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigResponse:
        """
        获取用户配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        获取基础镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaces(
            self,
            request: models.DescribeWorkspacesRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspacesResponse:
        """
        获取用户工作空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkspace(
            self,
            request: models.ModifyWorkspaceRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkspaceResponse:
        """
        修改工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWorkspace(
            self,
            request: models.RemoveWorkspaceRequest,
            opts: Dict = None,
    ) -> models.RemoveWorkspaceResponse:
        """
        删除工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunWorkspace(
            self,
            request: models.RunWorkspaceRequest,
            opts: Dict = None,
    ) -> models.RunWorkspaceResponse:
        """
        运行空间
        """
        
        kwargs = {}
        kwargs["action"] = "RunWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopWorkspace(
            self,
            request: models.StopWorkspaceRequest,
            opts: Dict = None,
    ) -> models.StopWorkspaceResponse:
        """
        停止运行空间
        """
        
        kwargs = {}
        kwargs["action"] = "StopWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)