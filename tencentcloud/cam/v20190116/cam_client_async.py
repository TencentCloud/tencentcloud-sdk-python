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
from tencentcloud.cam.v20190116 import models
from typing import Dict


class CamClient(AbstractClient):
    _apiVersion = '2019-01-16'
    _endpoint = 'cam.tencentcloudapi.com'
    _service = 'cam'

    async def AddUser(
            self,
            request: models.AddUserRequest,
            opts: Dict = None,
    ) -> models.AddUserResponse:
        """
        创建子用户
        """
        
        kwargs = {}
        kwargs["action"] = "AddUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserToGroup(
            self,
            request: models.AddUserToGroupRequest,
            opts: Dict = None,
    ) -> models.AddUserToGroupResponse:
        """
        用户加入到用户组
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserToGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserToGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachGroupPolicy(
            self,
            request: models.AttachGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachGroupPolicyResponse:
        """
        本接口（AttachGroupPolicy）可用于绑定策略到用户组。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachRolePolicy(
            self,
            request: models.AttachRolePolicyRequest,
            opts: Dict = None,
    ) -> models.AttachRolePolicyResponse:
        """
        本接口（AttachRolePolicy）用于绑定策略到角色。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachRolePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachRolePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachUserPolicy(
            self,
            request: models.AttachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachUserPolicyResponse:
        """
        本接口（AttachUserPolicy）可用于绑定到用户的策略。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BuildDataFlowAuthToken(
            self,
            request: models.BuildDataFlowAuthTokenRequest,
            opts: Dict = None,
    ) -> models.BuildDataFlowAuthTokenResponse:
        """
        获取数据流认证Token
        """
        
        kwargs = {}
        kwargs["action"] = "BuildDataFlowAuthToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BuildDataFlowAuthTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConsumeCustomMFAToken(
            self,
            request: models.ConsumeCustomMFATokenRequest,
            opts: Dict = None,
    ) -> models.ConsumeCustomMFATokenResponse:
        """
        验证自定义多因子Token
        """
        
        kwargs = {}
        kwargs["action"] = "ConsumeCustomMFAToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConsumeCustomMFATokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKey(
            self,
            request: models.CreateAccessKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeyResponse:
        """
        为CAM用户创建访问密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroup(
            self,
            request: models.CreateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupResponse:
        """
        创建用户组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMessageReceiver(
            self,
            request: models.CreateMessageReceiverRequest,
            opts: Dict = None,
    ) -> models.CreateMessageReceiverResponse:
        """
        创建消息接收人接口：仅允许已完成实名认证的用户访问消息接收人接口，并对每个用户限制每天最多请求10次。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMessageReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMessageReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOIDCConfig(
            self,
            request: models.CreateOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.CreateOIDCConfigResponse:
        """
        创建角色OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicy(
            self,
            request: models.CreatePolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyResponse:
        """
        本接口（CreatePolicy）可用于创建策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicyVersion(
            self,
            request: models.CreatePolicyVersionRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyVersionResponse:
        """
        该接口（CreatePolicyVersion）用于新增策略版本，用户创建了一个策略版本之后可以方便的通过变更策略版本的方式来变更策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        本接口（CreateRole）用于创建角色。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSAMLProvider(
            self,
            request: models.CreateSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.CreateSAMLProviderResponse:
        """
        创建SAML身份提供商
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceLinkedRole(
            self,
            request: models.CreateServiceLinkedRoleRequest,
            opts: Dict = None,
    ) -> models.CreateServiceLinkedRoleResponse:
        """
        创建服务相关角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceLinkedRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceLinkedRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubAccountLoginIpPolicy(
            self,
            request: models.CreateSubAccountLoginIpPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSubAccountLoginIpPolicyResponse:
        """
        增加子账号登录IP策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubAccountLoginIpPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubAccountLoginIpPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserOIDCConfig(
            self,
            request: models.CreateUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.CreateUserOIDCConfigResponse:
        """
        创建用户OIDC配置。只能创建一个用户OIDC身份提供商，并且创建用户OIDC配置之后会自动关闭用户SAML SSO身份提供商。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserSAMLConfig(
            self,
            request: models.CreateUserSAMLConfigRequest,
            opts: Dict = None,
    ) -> models.CreateUserSAMLConfigResponse:
        """
        创建用户SAML配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserSAMLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserSAMLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessKey(
            self,
            request: models.DeleteAccessKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessKeyResponse:
        """
        为CAM用户删除访问密钥。
        此接口属于高风险操作，删除密钥后不可恢复，腾讯云将永久拒绝此密钥的所有请求，请谨慎使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        删除用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMessageReceiver(
            self,
            request: models.DeleteMessageReceiverRequest,
            opts: Dict = None,
    ) -> models.DeleteMessageReceiverResponse:
        """
        删除消息接收人
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMessageReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMessageReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOIDCConfig(
            self,
            request: models.DeleteOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteOIDCConfigResponse:
        """
        删除OIDC身份提供商
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicy(
            self,
            request: models.DeletePolicyRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyResponse:
        """
        本接口（DeletePolicy）可用于删除策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicyVersion(
            self,
            request: models.DeletePolicyVersionRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyVersionResponse:
        """
        本接口（DeletePolicyVersion）可用于删除一个策略的策略版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRole(
            self,
            request: models.DeleteRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleResponse:
        """
        本接口（DeleteRole）用于删除指定角色。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRolePermissionsBoundary(
            self,
            request: models.DeleteRolePermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.DeleteRolePermissionsBoundaryResponse:
        """
        删除角色权限边界
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRolePermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRolePermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSAMLProvider(
            self,
            request: models.DeleteSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.DeleteSAMLProviderResponse:
        """
        删除SAML身份提供商
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceLinkedRole(
            self,
            request: models.DeleteServiceLinkedRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceLinkedRoleResponse:
        """
        删除服务相关角色
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceLinkedRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceLinkedRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        删除子用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserPermissionsBoundary(
            self,
            request: models.DeleteUserPermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.DeleteUserPermissionsBoundaryResponse:
        """
        删除用户权限边界
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserPermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserPermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOIDCConfig(
            self,
            request: models.DescribeOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeOIDCConfigResponse:
        """
        查询角色OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        本接口（DescribeRoleList）用于获取账号下的角色列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeAuthFlag(
            self,
            request: models.DescribeSafeAuthFlagRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeAuthFlagResponse:
        """
        查询用户安全设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeAuthFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeAuthFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeAuthFlagColl(
            self,
            request: models.DescribeSafeAuthFlagCollRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeAuthFlagCollResponse:
        """
        获取子账号安全设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeAuthFlagColl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeAuthFlagCollResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeAuthFlagIntl(
            self,
            request: models.DescribeSafeAuthFlagIntlRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeAuthFlagIntlResponse:
        """
        查询安全设置(国际站)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeAuthFlagIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeAuthFlagIntlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubAccounts(
            self,
            request: models.DescribeSubAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubAccountsResponse:
        """
        通过子用户UIN列表查询子用户
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserOIDCConfig(
            self,
            request: models.DescribeUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserOIDCConfigResponse:
        """
        查询用户OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSAMLConfig(
            self,
            request: models.DescribeUserSAMLConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSAMLConfigResponse:
        """
        查询用户SAML配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSAMLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSAMLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachGroupPolicy(
            self,
            request: models.DetachGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachGroupPolicyResponse:
        """
        本接口（DetachGroupPolicy）可用于解除绑定到用户组的策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachRolePolicy(
            self,
            request: models.DetachRolePolicyRequest,
            opts: Dict = None,
    ) -> models.DetachRolePolicyResponse:
        """
        本接口（DetachRolePolicy）用于解除绑定角色的策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachRolePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachRolePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachUserPolicy(
            self,
            request: models.DetachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachUserPolicyResponse:
        """
        本接口（DetachUserPolicy）可用于解除绑定到用户的策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableUserSSO(
            self,
            request: models.DisableUserSSORequest,
            opts: Dict = None,
    ) -> models.DisableUserSSOResponse:
        """
        禁用用户SSO
        """
        
        kwargs = {}
        kwargs["action"] = "DisableUserSSO"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableUserSSOResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAccountSummary(
            self,
            request: models.GetAccountSummaryRequest,
            opts: Dict = None,
    ) -> models.GetAccountSummaryResponse:
        """
        查询账户摘要
        """
        
        kwargs = {}
        kwargs["action"] = "GetAccountSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAccountSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCustomMFATokenInfo(
            self,
            request: models.GetCustomMFATokenInfoRequest,
            opts: Dict = None,
    ) -> models.GetCustomMFATokenInfoResponse:
        """
        获取自定义多因子Token关联信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetCustomMFATokenInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCustomMFATokenInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroup(
            self,
            request: models.GetGroupRequest,
            opts: Dict = None,
    ) -> models.GetGroupResponse:
        """
        查询用户组详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPolicy(
            self,
            request: models.GetPolicyRequest,
            opts: Dict = None,
    ) -> models.GetPolicyResponse:
        """
        本接口（GetPolicy）可用于查询查看策略详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPolicyVersion(
            self,
            request: models.GetPolicyVersionRequest,
            opts: Dict = None,
    ) -> models.GetPolicyVersionResponse:
        """
        该接口（GetPolicyVersion）用于查询策略版本详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetPolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRole(
            self,
            request: models.GetRoleRequest,
            opts: Dict = None,
    ) -> models.GetRoleResponse:
        """
        本接口（GetRole）用于获取指定角色的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRolePermissionBoundary(
            self,
            request: models.GetRolePermissionBoundaryRequest,
            opts: Dict = None,
    ) -> models.GetRolePermissionBoundaryResponse:
        """
        获取角色权限边界
        """
        
        kwargs = {}
        kwargs["action"] = "GetRolePermissionBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRolePermissionBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSAMLProvider(
            self,
            request: models.GetSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.GetSAMLProviderResponse:
        """
        查询SAML身份提供商详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSecurityLastUsed(
            self,
            request: models.GetSecurityLastUsedRequest,
            opts: Dict = None,
    ) -> models.GetSecurityLastUsedResponse:
        """
        获取密钥最近使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "GetSecurityLastUsed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSecurityLastUsedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetServiceLinkedRoleDeletionStatus(
            self,
            request: models.GetServiceLinkedRoleDeletionStatusRequest,
            opts: Dict = None,
    ) -> models.GetServiceLinkedRoleDeletionStatusResponse:
        """
        根据删除TaskId获取服务相关角色删除状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetServiceLinkedRoleDeletionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetServiceLinkedRoleDeletionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUser(
            self,
            request: models.GetUserRequest,
            opts: Dict = None,
    ) -> models.GetUserResponse:
        """
        查询子用户
        """
        
        kwargs = {}
        kwargs["action"] = "GetUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserAppId(
            self,
            request: models.GetUserAppIdRequest,
            opts: Dict = None,
    ) -> models.GetUserAppIdResponse:
        """
        获取用户AppId
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserAppId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserAppIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserPermissionBoundary(
            self,
            request: models.GetUserPermissionBoundaryRequest,
            opts: Dict = None,
    ) -> models.GetUserPermissionBoundaryResponse:
        """
        获取用户权限边界
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserPermissionBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserPermissionBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAccessKeys(
            self,
            request: models.ListAccessKeysRequest,
            opts: Dict = None,
    ) -> models.ListAccessKeysResponse:
        """
        列出指定CAM用户的访问密钥
        """
        
        kwargs = {}
        kwargs["action"] = "ListAccessKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAccessKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedGroupPolicies(
            self,
            request: models.ListAttachedGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedGroupPoliciesResponse:
        """
        本接口（ListAttachedGroupPolicies）可用于查询用户组关联的策略列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedRolePolicies(
            self,
            request: models.ListAttachedRolePoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedRolePoliciesResponse:
        """
        本接口（ListAttachedRolePolicies）用于获取角色绑定的策略列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedRolePolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedRolePoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedUserAllPolicies(
            self,
            request: models.ListAttachedUserAllPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedUserAllPoliciesResponse:
        """
        列出用户关联的策略（包括随组关联）
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedUserAllPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedUserAllPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedUserPolicies(
            self,
            request: models.ListAttachedUserPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedUserPoliciesResponse:
        """
        本接口（ListAttachedUserPolicies）可用于查询子账号关联的策略列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedUserPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedUserPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCollaborators(
            self,
            request: models.ListCollaboratorsRequest,
            opts: Dict = None,
    ) -> models.ListCollaboratorsResponse:
        """
        获取协作者列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListCollaborators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCollaboratorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEntitiesForPolicy(
            self,
            request: models.ListEntitiesForPolicyRequest,
            opts: Dict = None,
    ) -> models.ListEntitiesForPolicyResponse:
        """
        本接口（ListEntitiesForPolicy）可用于查询策略关联的实体列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListEntitiesForPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEntitiesForPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroups(
            self,
            request: models.ListGroupsRequest,
            opts: Dict = None,
    ) -> models.ListGroupsResponse:
        """
        查询用户组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroupsForUser(
            self,
            request: models.ListGroupsForUserRequest,
            opts: Dict = None,
    ) -> models.ListGroupsForUserResponse:
        """
        列出用户关联的用户组
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroupsForUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupsForUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPolicies(
            self,
            request: models.ListPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListPoliciesResponse:
        """
        本接口（ListPolicies）可用于查询策略列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPoliciesGrantingServiceAccess(
            self,
            request: models.ListPoliciesGrantingServiceAccessRequest,
            opts: Dict = None,
    ) -> models.ListPoliciesGrantingServiceAccessResponse:
        """
        获取所有已授权服务
        """
        
        kwargs = {}
        kwargs["action"] = "ListPoliciesGrantingServiceAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPoliciesGrantingServiceAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPolicyVersions(
            self,
            request: models.ListPolicyVersionsRequest,
            opts: Dict = None,
    ) -> models.ListPolicyVersionsResponse:
        """
        该接口（ListPolicyVersions）用于获取策略版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListPolicyVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPolicyVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReceiver(
            self,
            request: models.ListReceiverRequest,
            opts: Dict = None,
    ) -> models.ListReceiverResponse:
        """
        获取消息接收人列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSAMLProviders(
            self,
            request: models.ListSAMLProvidersRequest,
            opts: Dict = None,
    ) -> models.ListSAMLProvidersResponse:
        """
        查询SAML身份提供商列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSAMLProviders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSAMLProvidersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsers(
            self,
            request: models.ListUsersRequest,
            opts: Dict = None,
    ) -> models.ListUsersResponse:
        """
        拉取子用户
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsersForGroup(
            self,
            request: models.ListUsersForGroupRequest,
            opts: Dict = None,
    ) -> models.ListUsersForGroupResponse:
        """
        查询用户组关联的用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsersForGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersForGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWeChatWorkSubAccounts(
            self,
            request: models.ListWeChatWorkSubAccountsRequest,
            opts: Dict = None,
    ) -> models.ListWeChatWorkSubAccountsResponse:
        """
        获取企业微信子用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWeChatWorkSubAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWeChatWorkSubAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutRolePermissionsBoundary(
            self,
            request: models.PutRolePermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.PutRolePermissionsBoundaryResponse:
        """
        设置角色权限边界
        """
        
        kwargs = {}
        kwargs["action"] = "PutRolePermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutRolePermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutUserPermissionsBoundary(
            self,
            request: models.PutUserPermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.PutUserPermissionsBoundaryResponse:
        """
        设置用户权限边界
        """
        
        kwargs = {}
        kwargs["action"] = "PutUserPermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutUserPermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserFromGroup(
            self,
            request: models.RemoveUserFromGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveUserFromGroupResponse:
        """
        从用户组删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserFromGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserFromGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDefaultPolicyVersion(
            self,
            request: models.SetDefaultPolicyVersionRequest,
            opts: Dict = None,
    ) -> models.SetDefaultPolicyVersionResponse:
        """
        本接口（SetDefaultPolicyVersion）可用于设置生效的策略版本。
        """
        
        kwargs = {}
        kwargs["action"] = "SetDefaultPolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDefaultPolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetMfaFlag(
            self,
            request: models.SetMfaFlagRequest,
            opts: Dict = None,
    ) -> models.SetMfaFlagResponse:
        """
        设置子用户的登录保护和敏感操作校验方式
        """
        
        kwargs = {}
        kwargs["action"] = "SetMfaFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetMfaFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TagRole(
            self,
            request: models.TagRoleRequest,
            opts: Dict = None,
    ) -> models.TagRoleResponse:
        """
        角色绑定标签
        """
        
        kwargs = {}
        kwargs["action"] = "TagRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TagRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntagRole(
            self,
            request: models.UntagRoleRequest,
            opts: Dict = None,
    ) -> models.UntagRoleResponse:
        """
        角色解绑标签。
        """
        
        kwargs = {}
        kwargs["action"] = "UntagRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntagRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKey(
            self,
            request: models.UpdateAccessKeyRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyResponse:
        """
        为CAM用户更新访问密钥
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAssumeRolePolicy(
            self,
            request: models.UpdateAssumeRolePolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateAssumeRolePolicyResponse:
        """
        本接口（UpdateAssumeRolePolicy）用于修改角色信任策略的策略文档。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAssumeRolePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAssumeRolePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGroup(
            self,
            request: models.UpdateGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateGroupResponse:
        """
        更新用户组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOIDCConfig(
            self,
            request: models.UpdateOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateOIDCConfigResponse:
        """
        修改角色OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePolicy(
            self,
            request: models.UpdatePolicyRequest,
            opts: Dict = None,
    ) -> models.UpdatePolicyResponse:
        """
        本接口（UpdatePolicy ）可用于更新策略。
        如果已存在策略版本，本接口会直接更新策略的默认版本，不会创建新版本，如果不存在任何策略版本，则直接创建一个默认版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleConsoleLogin(
            self,
            request: models.UpdateRoleConsoleLoginRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleConsoleLoginResponse:
        """
        本接口（UpdateRoleConsoleLogin）用于修改角色是否可登录。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleConsoleLogin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleConsoleLoginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleDescription(
            self,
            request: models.UpdateRoleDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleDescriptionResponse:
        """
        本接口（UpdateRoleDescription）用于修改角色的描述信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleSessionDuration(
            self,
            request: models.UpdateRoleSessionDurationRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleSessionDurationResponse:
        """
        修改角色会话时长
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleSessionDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleSessionDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSAMLProvider(
            self,
            request: models.UpdateSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.UpdateSAMLProviderResponse:
        """
        更新SAML身份提供商信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUser(
            self,
            request: models.UpdateUserRequest,
            opts: Dict = None,
    ) -> models.UpdateUserResponse:
        """
        更新子用户
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserOIDCConfig(
            self,
            request: models.UpdateUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUserOIDCConfigResponse:
        """
        修改用户OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserSAMLConfig(
            self,
            request: models.UpdateUserSAMLConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUserSAMLConfigResponse:
        """
        修改用户SAML配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserSAMLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserSAMLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)