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
from tencentcloud.ciam.v20220331 import models
from typing import Dict


class CiamClient(AbstractClient):
    _apiVersion = '2022-03-31'
    _endpoint = 'ciam.tencentcloudapi.com'
    _service = 'ciam'

    async def CreateApiImportUserJob(
            self,
            request: models.CreateApiImportUserJobRequest,
            opts: Dict = None,
    ) -> models.CreateApiImportUserJobResponse:
        """
        新建接口导入用户任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiImportUserJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiImportUserJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileExportUserJob(
            self,
            request: models.CreateFileExportUserJobRequest,
            opts: Dict = None,
    ) -> models.CreateFileExportUserJobResponse:
        """
        新建文件导出用户任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileExportUserJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileExportUserJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        创建用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserGroup(
            self,
            request: models.CreateUserGroupRequest,
            opts: Dict = None,
    ) -> models.CreateUserGroupResponse:
        """
        创建用户组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserStore(
            self,
            request: models.CreateUserStoreRequest,
            opts: Dict = None,
    ) -> models.CreateUserStoreResponse:
        """
        创建用户目录
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroups(
            self,
            request: models.DeleteUserGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupsResponse:
        """
        批量删除用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserStore(
            self,
            request: models.DeleteUserStoreRequest,
            opts: Dict = None,
    ) -> models.DeleteUserStoreResponse:
        """
        删除用户目录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        批量删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        多条件查询用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserById(
            self,
            request: models.DescribeUserByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeUserByIdResponse:
        """
        根据ID查询用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LinkAccount(
            self,
            request: models.LinkAccountRequest,
            opts: Dict = None,
    ) -> models.LinkAccountResponse:
        """
        账号融合
        """
        
        kwargs = {}
        kwargs["action"] = "LinkAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LinkAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListJobs(
            self,
            request: models.ListJobsRequest,
            opts: Dict = None,
    ) -> models.ListJobsResponse:
        """
        查询任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLogMessageByCondition(
            self,
            request: models.ListLogMessageByConditionRequest,
            opts: Dict = None,
    ) -> models.ListLogMessageByConditionResponse:
        """
        查询日志信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListLogMessageByCondition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLogMessageByConditionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUser(
            self,
            request: models.ListUserRequest,
            opts: Dict = None,
    ) -> models.ListUserResponse:
        """
        查询用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserByProperty(
            self,
            request: models.ListUserByPropertyRequest,
            opts: Dict = None,
    ) -> models.ListUserByPropertyResponse:
        """
        根据属性查询用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserByProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserByPropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserGroups(
            self,
            request: models.ListUserGroupsRequest,
            opts: Dict = None,
    ) -> models.ListUserGroupsResponse:
        """
        查询用户组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserStore(
            self,
            request: models.ListUserStoreRequest,
            opts: Dict = None,
    ) -> models.ListUserStoreResponse:
        """
        查询用户目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        重置用户密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetPassword(
            self,
            request: models.SetPasswordRequest,
            opts: Dict = None,
    ) -> models.SetPasswordResponse:
        """
        设置用户密码
        """
        
        kwargs = {}
        kwargs["action"] = "SetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUser(
            self,
            request: models.UpdateUserRequest,
            opts: Dict = None,
    ) -> models.UpdateUserResponse:
        """
        更新用户
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserGroup(
            self,
            request: models.UpdateUserGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateUserGroupResponse:
        """
        更新用户组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserStatus(
            self,
            request: models.UpdateUserStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateUserStatusResponse:
        """
        更新用户状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserStore(
            self,
            request: models.UpdateUserStoreRequest,
            opts: Dict = None,
    ) -> models.UpdateUserStoreResponse:
        """
        更新用户目录
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)