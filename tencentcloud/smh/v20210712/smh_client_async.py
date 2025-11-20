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
from tencentcloud.smh.v20210712 import models
from typing import Dict


class SmhClient(AbstractClient):
    _apiVersion = '2021-07-12'
    _endpoint = 'smh.tencentcloudapi.com'
    _service = 'smh'

    async def CreateLibrary(
            self,
            request: models.CreateLibraryRequest,
            opts: Dict = None,
    ) -> models.CreateLibraryResponse:
        """
        创建 PaaS 服务媒体库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        新建用户。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserLifecycle(
            self,
            request: models.CreateUserLifecycleRequest,
            opts: Dict = None,
    ) -> models.CreateUserLifecycleResponse:
        """
        设置用户生命周期。如果指定的用户已经设置了生命周期，重复调用此接口将覆盖已有的设置。也可用于清除指定用户的生命周期。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserLifecycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserLifecycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLibrary(
            self,
            request: models.DeleteLibraryRequest,
            opts: Dict = None,
    ) -> models.DeleteLibraryResponse:
        """
        删除 PaaS 服务媒体库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        一次删除多个用户。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLibraries(
            self,
            request: models.DescribeLibrariesRequest,
            opts: Dict = None,
    ) -> models.DescribeLibrariesResponse:
        """
        查询 PaaS 服务媒体库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLibraries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLibrariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLibrarySecret(
            self,
            request: models.DescribeLibrarySecretRequest,
            opts: Dict = None,
    ) -> models.DescribeLibrarySecretResponse:
        """
        查询 PaaS 服务媒体库密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLibrarySecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLibrarySecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfficialInstances(
            self,
            request: models.DescribeOfficialInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeOfficialInstancesResponse:
        """
        查询官方云盘实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfficialInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfficialInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfficialOverview(
            self,
            request: models.DescribeOfficialOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeOfficialOverviewResponse:
        """
        查询官方云盘实例概览数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfficialOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfficialOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficPackages(
            self,
            request: models.DescribeTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficPackagesResponse:
        """
        查询流量资源包
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserLifecycle(
            self,
            request: models.DescribeUserLifecycleRequest,
            opts: Dict = None,
    ) -> models.DescribeUserLifecycleResponse:
        """
        查询用户生命周期。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserLifecycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserLifecycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLibrary(
            self,
            request: models.ModifyLibraryRequest,
            opts: Dict = None,
    ) -> models.ModifyLibraryResponse:
        """
        修改 PaaS 服务媒体库配置项
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        更新用户信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendSmsCode(
            self,
            request: models.SendSmsCodeRequest,
            opts: Dict = None,
    ) -> models.SendSmsCodeResponse:
        """
        发送用于换绑官方云盘实例的超级管理员账号的短信验证码
        """
        
        kwargs = {}
        kwargs["action"] = "SendSmsCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendSmsCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifySmsCode(
            self,
            request: models.VerifySmsCodeRequest,
            opts: Dict = None,
    ) -> models.VerifySmsCodeResponse:
        """
        验证短信验证码以换绑官方云盘实例的超级管理员账号
        """
        
        kwargs = {}
        kwargs["action"] = "VerifySmsCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifySmsCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)