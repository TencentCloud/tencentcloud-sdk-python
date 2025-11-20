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
from tencentcloud.eiam.v20210420 import models
from typing import Dict


class EiamClient(AbstractClient):
    _apiVersion = '2021-04-20'
    _endpoint = 'eiam.tencentcloudapi.com'
    _service = 'eiam'

    async def AddAccountToAccountGroup(
            self,
            request: models.AddAccountToAccountGroupRequest,
            opts: Dict = None,
    ) -> models.AddAccountToAccountGroupResponse:
        """
        账号组添加账号
        """
        
        kwargs = {}
        kwargs["action"] = "AddAccountToAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAccountToAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserToUserGroup(
            self,
            request: models.AddUserToUserGroupRequest,
            opts: Dict = None,
    ) -> models.AddUserToUserGroupResponse:
        """
        加入用户到用户组
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserToUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserToUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccountGroup(
            self,
            request: models.CreateAccountGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAccountGroupResponse:
        """
        创建账号组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAppAccount(
            self,
            request: models.CreateAppAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAppAccountResponse:
        """
        创建应用账号
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrgNode(
            self,
            request: models.CreateOrgNodeRequest,
            opts: Dict = None,
    ) -> models.CreateOrgNodeResponse:
        """
        新建一个机构节点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        新建一个用户
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
        新建用户组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccountGroup(
            self,
            request: models.DeleteAccountGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountGroupResponse:
        """
        删除账号组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppAccount(
            self,
            request: models.DeleteAppAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAppAccountResponse:
        """
        删除应用账号
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrgNode(
            self,
            request: models.DeleteOrgNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteOrgNodeResponse:
        """
        删除一个机构节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        通过用户名或用户 id 删除用户。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroup(
            self,
            request: models.DeleteUserGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupResponse:
        """
        删除一个用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        批量删除当前节点下的用户。如果出现个别用户删除错误，将不影响其余被勾选用户被删除的操作，同时提示未被删除的用户名称/用户ID。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountGroup(
            self,
            request: models.DescribeAccountGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountGroupResponse:
        """
        查询账号组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppAccount(
            self,
            request: models.DescribeAppAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeAppAccountResponse:
        """
        查询应用账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplication(
            self,
            request: models.DescribeApplicationRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationResponse:
        """
        获取一个应用的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrgNode(
            self,
            request: models.DescribeOrgNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeOrgNodeResponse:
        """
        根据机构节点ID读取机构节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrgResourcesAuthorization(
            self,
            request: models.DescribeOrgResourcesAuthorizationRequest,
            opts: Dict = None,
    ) -> models.DescribeOrgResourcesAuthorizationResponse:
        """
        查询指定机构下的资源授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrgResourcesAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrgResourcesAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicKey(
            self,
            request: models.DescribePublicKeyRequest,
            opts: Dict = None,
    ) -> models.DescribePublicKeyResponse:
        """
        获取JWT公钥信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroup(
            self,
            request: models.DescribeUserGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupResponse:
        """
        获取用户组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroupResourcesAuthorization(
            self,
            request: models.DescribeUserGroupResourcesAuthorizationRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupResourcesAuthorizationResponse:
        """
        查询指定用户组下的资源授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroupResourcesAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupResourcesAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        通过用户名或用户 id 搜索用户
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserResourcesAuthorization(
            self,
            request: models.DescribeUserResourcesAuthorizationRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResourcesAuthorizationResponse:
        """
        查询指定用户下的资源授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserResourcesAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResourcesAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserThirdPartyAccountInfo(
            self,
            request: models.DescribeUserThirdPartyAccountInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserThirdPartyAccountInfoResponse:
        """
        通过用户名或用户 id 获取用户的第三方账号绑定信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserThirdPartyAccountInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserThirdPartyAccountInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAccountInAccountGroup(
            self,
            request: models.ListAccountInAccountGroupRequest,
            opts: Dict = None,
    ) -> models.ListAccountInAccountGroupResponse:
        """
        获取账号组中的账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAccountInAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAccountInAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListApplicationAuthorizations(
            self,
            request: models.ListApplicationAuthorizationsRequest,
            opts: Dict = None,
    ) -> models.ListApplicationAuthorizationsResponse:
        """
        应用授权关系列表（含搜索条件匹配）。
        """
        
        kwargs = {}
        kwargs["action"] = "ListApplicationAuthorizations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListApplicationAuthorizationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListApplications(
            self,
            request: models.ListApplicationsRequest,
            opts: Dict = None,
    ) -> models.ListApplicationsResponse:
        """
        获取应用列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ListApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAuthorizedApplicationsToOrgNode(
            self,
            request: models.ListAuthorizedApplicationsToOrgNodeRequest,
            opts: Dict = None,
    ) -> models.ListAuthorizedApplicationsToOrgNodeResponse:
        """
        通过机构节点ID获得被授权访问的应用列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAuthorizedApplicationsToOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuthorizedApplicationsToOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAuthorizedApplicationsToUser(
            self,
            request: models.ListAuthorizedApplicationsToUserRequest,
            opts: Dict = None,
    ) -> models.ListAuthorizedApplicationsToUserResponse:
        """
        通过用户ID获得被授权访问的应用列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAuthorizedApplicationsToUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuthorizedApplicationsToUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAuthorizedApplicationsToUserGroup(
            self,
            request: models.ListAuthorizedApplicationsToUserGroupRequest,
            opts: Dict = None,
    ) -> models.ListAuthorizedApplicationsToUserGroupResponse:
        """
        通过用户组ID获得被授权访问的应用列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAuthorizedApplicationsToUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuthorizedApplicationsToUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserGroups(
            self,
            request: models.ListUserGroupsRequest,
            opts: Dict = None,
    ) -> models.ListUserGroupsResponse:
        """
        获取用户组列表信息（包含查询条件）。
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserGroupsOfUser(
            self,
            request: models.ListUserGroupsOfUserRequest,
            opts: Dict = None,
    ) -> models.ListUserGroupsOfUserResponse:
        """
        获取用户所在的用户组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserGroupsOfUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserGroupsOfUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsers(
            self,
            request: models.ListUsersRequest,
            opts: Dict = None,
    ) -> models.ListUsersResponse:
        """
        获取用户列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsersInOrgNode(
            self,
            request: models.ListUsersInOrgNodeRequest,
            opts: Dict = None,
    ) -> models.ListUsersInOrgNodeResponse:
        """
        根据机构节点ID读取节点下用户
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsersInOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersInOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsersInUserGroup(
            self,
            request: models.ListUsersInUserGroupRequest,
            opts: Dict = None,
    ) -> models.ListUsersInUserGroupResponse:
        """
        获取用户组中的用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsersInUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersInUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountGroup(
            self,
            request: models.ModifyAccountGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountGroupResponse:
        """
        修改账号组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAppAccount(
            self,
            request: models.ModifyAppAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyAppAccountResponse:
        """
        修改应用账号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        更新一个应用的信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserInfo(
            self,
            request: models.ModifyUserInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyUserInfoResponse:
        """
        通过用户名或用户 id 冻结用户
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAccountFromAccountGroup(
            self,
            request: models.RemoveAccountFromAccountGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveAccountFromAccountGroupResponse:
        """
        从账号组中移除账号
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAccountFromAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAccountFromAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserFromUserGroup(
            self,
            request: models.RemoveUserFromUserGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveUserFromUserGroupResponse:
        """
        从用户组中移除用户
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserFromUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserFromUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrgNode(
            self,
            request: models.UpdateOrgNodeRequest,
            opts: Dict = None,
    ) -> models.UpdateOrgNodeResponse:
        """
        新建一个机构节点，
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)