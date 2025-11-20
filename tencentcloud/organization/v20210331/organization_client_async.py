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
from tencentcloud.organization.v20210331 import models
from typing import Dict


class OrganizationClient(AbstractClient):
    _apiVersion = '2021-03-31'
    _endpoint = 'organization.tencentcloudapi.com'
    _service = 'organization'

    async def AcceptJoinShareUnitInvitation(
            self,
            request: models.AcceptJoinShareUnitInvitationRequest,
            opts: Dict = None,
    ) -> models.AcceptJoinShareUnitInvitationResponse:
        """
        接受加入共享单元邀请。
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptJoinShareUnitInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptJoinShareUnitInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddExternalSAMLIdPCertificate(
            self,
            request: models.AddExternalSAMLIdPCertificateRequest,
            opts: Dict = None,
    ) -> models.AddExternalSAMLIdPCertificateResponse:
        """
        添加SAML签名证书
        """
        
        kwargs = {}
        kwargs["action"] = "AddExternalSAMLIdPCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddExternalSAMLIdPCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganizationMemberEmail(
            self,
            request: models.AddOrganizationMemberEmailRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationMemberEmailResponse:
        """
        添加组织成员邮箱
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganizationMemberEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationMemberEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganizationNode(
            self,
            request: models.AddOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationNodeResponse:
        """
        添加企业组织节点
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddPermissionPolicyToRoleConfiguration(
            self,
            request: models.AddPermissionPolicyToRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.AddPermissionPolicyToRoleConfigurationResponse:
        """
        为权限配置添加策略
        """
        
        kwargs = {}
        kwargs["action"] = "AddPermissionPolicyToRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddPermissionPolicyToRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShareUnit(
            self,
            request: models.AddShareUnitRequest,
            opts: Dict = None,
    ) -> models.AddShareUnitResponse:
        """
        创建共享单元。
        """
        
        kwargs = {}
        kwargs["action"] = "AddShareUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShareUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShareUnitMembers(
            self,
            request: models.AddShareUnitMembersRequest,
            opts: Dict = None,
    ) -> models.AddShareUnitMembersResponse:
        """
        添加共享单元成员
        """
        
        kwargs = {}
        kwargs["action"] = "AddShareUnitMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShareUnitMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShareUnitResources(
            self,
            request: models.AddShareUnitResourcesRequest,
            opts: Dict = None,
    ) -> models.AddShareUnitResourcesResponse:
        """
        添加共享单元资源
        """
        
        kwargs = {}
        kwargs["action"] = "AddShareUnitResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShareUnitResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserToGroup(
            self,
            request: models.AddUserToGroupRequest,
            opts: Dict = None,
    ) -> models.AddUserToGroupResponse:
        """
        为用户组添加用户
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserToGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserToGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachPolicy(
            self,
            request: models.AttachPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachPolicyResponse:
        """
        绑定策略
        """
        
        kwargs = {}
        kwargs["action"] = "AttachPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindOrganizationMemberAuthAccount(
            self,
            request: models.BindOrganizationMemberAuthAccountRequest,
            opts: Dict = None,
    ) -> models.BindOrganizationMemberAuthAccountResponse:
        """
        绑定组织成员和组织管理员子账号的授权关系
        """
        
        kwargs = {}
        kwargs["action"] = "BindOrganizationMemberAuthAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindOrganizationMemberAuthAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindOrganizationPolicySubAccount(
            self,
            request: models.BindOrganizationPolicySubAccountRequest,
            opts: Dict = None,
    ) -> models.BindOrganizationPolicySubAccountResponse:
        """
        绑定成员访问授权策略和组织管理员子账号
        """
        
        kwargs = {}
        kwargs["action"] = "BindOrganizationPolicySubAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindOrganizationPolicySubAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelOrganizationMemberAuthAccount(
            self,
            request: models.CancelOrganizationMemberAuthAccountRequest,
            opts: Dict = None,
    ) -> models.CancelOrganizationMemberAuthAccountResponse:
        """
        取消组织成员和组织管理员子账号的授权关系
        """
        
        kwargs = {}
        kwargs["action"] = "CancelOrganizationMemberAuthAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelOrganizationMemberAuthAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelOrganizationPolicySubAccount(
            self,
            request: models.CancelOrganizationPolicySubAccountRequest,
            opts: Dict = None,
    ) -> models.CancelOrganizationPolicySubAccountResponse:
        """
        解绑成员访问授权策略和组织管理员子账号
        """
        
        kwargs = {}
        kwargs["action"] = "CancelOrganizationPolicySubAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelOrganizationPolicySubAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAccountDelete(
            self,
            request: models.CheckAccountDeleteRequest,
            opts: Dict = None,
    ) -> models.CheckAccountDeleteResponse:
        """
        成员账号删除检查
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAccountDelete"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAccountDeleteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearExternalSAMLIdentityProvider(
            self,
            request: models.ClearExternalSAMLIdentityProviderRequest,
            opts: Dict = None,
    ) -> models.ClearExternalSAMLIdentityProviderResponse:
        """
        清空SAML身份提供商配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "ClearExternalSAMLIdentityProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearExternalSAMLIdentityProviderResponse
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
        
    async def CreateOrgServiceAssign(
            self,
            request: models.CreateOrgServiceAssignRequest,
            opts: Dict = None,
    ) -> models.CreateOrgServiceAssignResponse:
        """
        添加集团服务委派管理员
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrgServiceAssign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrgServiceAssignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganization(
            self,
            request: models.CreateOrganizationRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationResponse:
        """
        创建企业组织
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationIdentity(
            self,
            request: models.CreateOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationIdentityResponse:
        """
        添加组织身份
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMember(
            self,
            request: models.CreateOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMemberResponse:
        """
        创建组织成员
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMemberAuthIdentity(
            self,
            request: models.CreateOrganizationMemberAuthIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMemberAuthIdentityResponse:
        """
        添加组织成员访问授权
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMemberAuthIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMemberAuthIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMemberPolicy(
            self,
            request: models.CreateOrganizationMemberPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMemberPolicyResponse:
        """
        创建组织成员访问授权策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMemberPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMemberPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMembersPolicy(
            self,
            request: models.CreateOrganizationMembersPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMembersPolicyResponse:
        """
        创建组织成员访问策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMembersPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMembersPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicy(
            self,
            request: models.CreatePolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyResponse:
        """
        创建一个特殊类型的策略，您可以关联到企业组织Root节点、企业部门节点或者企业的成员账号。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoleAssignment(
            self,
            request: models.CreateRoleAssignmentRequest,
            opts: Dict = None,
    ) -> models.CreateRoleAssignmentResponse:
        """
        在成员账号上授权
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoleAssignment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleAssignmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoleConfiguration(
            self,
            request: models.CreateRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.CreateRoleConfigurationResponse:
        """
        创建权限配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSCIMCredential(
            self,
            request: models.CreateSCIMCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateSCIMCredentialResponse:
        """
        创建SCIM密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSCIMCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSCIMCredentialResponse
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
        
    async def CreateUserSyncProvisioning(
            self,
            request: models.CreateUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.CreateUserSyncProvisioningResponse:
        """
        创建子用户同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        删除成员账号
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
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
        
    async def DeleteOrgServiceAssign(
            self,
            request: models.DeleteOrgServiceAssignRequest,
            opts: Dict = None,
    ) -> models.DeleteOrgServiceAssignResponse:
        """
        删除集团服务委派管理员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrgServiceAssign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrgServiceAssignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganization(
            self,
            request: models.DeleteOrganizationRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationResponse:
        """
        删除企业组织
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationIdentity(
            self,
            request: models.DeleteOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationIdentityResponse:
        """
        删除组织身份
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMemberAuthIdentity(
            self,
            request: models.DeleteOrganizationMemberAuthIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMemberAuthIdentityResponse:
        """
        删除组织成员访问授权
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMemberAuthIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMemberAuthIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMembers(
            self,
            request: models.DeleteOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMembersResponse:
        """
        从组织中移除成员账号，不会删除账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMembersPolicy(
            self,
            request: models.DeleteOrganizationMembersPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMembersPolicyResponse:
        """
        删除组织成员访问策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMembersPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMembersPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationNodes(
            self,
            request: models.DeleteOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationNodesResponse:
        """
        批量删除企业组织节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicy(
            self,
            request: models.DeletePolicyRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyResponse:
        """
        删除策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoleAssignment(
            self,
            request: models.DeleteRoleAssignmentRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleAssignmentResponse:
        """
        移除成员账号上的授权
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoleAssignment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleAssignmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoleConfiguration(
            self,
            request: models.DeleteRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleConfigurationResponse:
        """
        删除权限配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSCIMCredential(
            self,
            request: models.DeleteSCIMCredentialRequest,
            opts: Dict = None,
    ) -> models.DeleteSCIMCredentialResponse:
        """
        删除SCIM密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSCIMCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSCIMCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareUnit(
            self,
            request: models.DeleteShareUnitRequest,
            opts: Dict = None,
    ) -> models.DeleteShareUnitResponse:
        """
        删除共享单元。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareUnitMembers(
            self,
            request: models.DeleteShareUnitMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteShareUnitMembersResponse:
        """
        删除共享单元成员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareUnitMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareUnitMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareUnitResources(
            self,
            request: models.DeleteShareUnitResourcesRequest,
            opts: Dict = None,
    ) -> models.DeleteShareUnitResourcesResponse:
        """
        删除共享单元资源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareUnitResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareUnitResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserSyncProvisioning(
            self,
            request: models.DeleteUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.DeleteUserSyncProvisioningResponse:
        """
        删除子用户同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEffectivePolicy(
            self,
            request: models.DescribeEffectivePolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeEffectivePolicyResponse:
        """
        查询目标关联的有效策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEffectivePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEffectivePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdentityCenter(
            self,
            request: models.DescribeIdentityCenterRequest,
            opts: Dict = None,
    ) -> models.DescribeIdentityCenterResponse:
        """
        获取集团账号身份中心服务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdentityCenter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdentityCenterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganization(
            self,
            request: models.DescribeOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationResponse:
        """
        获取企业组织信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationAuthNode(
            self,
            request: models.DescribeOrganizationAuthNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationAuthNodeResponse:
        """
        获取已设置管理员的互信主体关系列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationAuthNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationAuthNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationFinancialByMember(
            self,
            request: models.DescribeOrganizationFinancialByMemberRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationFinancialByMemberResponse:
        """
        以成员维度获取组织财务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationFinancialByMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationFinancialByMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationFinancialByMonth(
            self,
            request: models.DescribeOrganizationFinancialByMonthRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationFinancialByMonthResponse:
        """
        以月维度获取组织财务信息趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationFinancialByMonth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationFinancialByMonthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationFinancialByProduct(
            self,
            request: models.DescribeOrganizationFinancialByProductRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationFinancialByProductResponse:
        """
        以产品维度获取组织财务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationFinancialByProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationFinancialByProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberAuthAccounts(
            self,
            request: models.DescribeOrganizationMemberAuthAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberAuthAccountsResponse:
        """
        获取组织成员被绑定授权关系的子账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberAuthAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberAuthAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberAuthIdentities(
            self,
            request: models.DescribeOrganizationMemberAuthIdentitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberAuthIdentitiesResponse:
        """
        获取组织成员访问授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberAuthIdentities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberAuthIdentitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberEmailBind(
            self,
            request: models.DescribeOrganizationMemberEmailBindRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberEmailBindResponse:
        """
        查询成员邮箱绑定详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberEmailBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberEmailBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberPolicies(
            self,
            request: models.DescribeOrganizationMemberPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberPoliciesResponse:
        """
        获取组织成员的授权策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMembers(
            self,
            request: models.DescribeOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMembersResponse:
        """
        获取企业组织成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMembersAuthPolicy(
            self,
            request: models.DescribeOrganizationMembersAuthPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMembersAuthPolicyResponse:
        """
        查询组织成员访问策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMembersAuthPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMembersAuthPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationNodes(
            self,
            request: models.DescribeOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationNodesResponse:
        """
        获取组织节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicy(
            self,
            request: models.DescribePolicyRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyResponse:
        """
        本接口（DescribePolicy）可用于查询查看策略详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyConfig(
            self,
            request: models.DescribePolicyConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyConfigResponse:
        """
        本接口（DescribePolicyConfig）可用于查询企业组织策略配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceToShareMember(
            self,
            request: models.DescribeResourceToShareMemberRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceToShareMemberResponse:
        """
        获取与我共享的资源列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceToShareMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceToShareMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareAreas(
            self,
            request: models.DescribeShareAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeShareAreasResponse:
        """
        获取可共享地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareUnitMembers(
            self,
            request: models.DescribeShareUnitMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeShareUnitMembersResponse:
        """
        获取共享单元成员列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareUnitMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareUnitMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareUnitResources(
            self,
            request: models.DescribeShareUnitResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeShareUnitResourcesResponse:
        """
        获取共享单元资源列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareUnitResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareUnitResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareUnits(
            self,
            request: models.DescribeShareUnitsRequest,
            opts: Dict = None,
    ) -> models.DescribeShareUnitsResponse:
        """
        获取共享单元列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareUnits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareUnitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachPolicy(
            self,
            request: models.DetachPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachPolicyResponse:
        """
        解绑策略
        """
        
        kwargs = {}
        kwargs["action"] = "DetachPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisablePolicyType(
            self,
            request: models.DisablePolicyTypeRequest,
            opts: Dict = None,
    ) -> models.DisablePolicyTypeResponse:
        """
        禁用策略类型
        """
        
        kwargs = {}
        kwargs["action"] = "DisablePolicyType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisablePolicyTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DismantleRoleConfiguration(
            self,
            request: models.DismantleRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.DismantleRoleConfigurationResponse:
        """
        解除权限配置在成员账号上的部署
        """
        
        kwargs = {}
        kwargs["action"] = "DismantleRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DismantleRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnablePolicyType(
            self,
            request: models.EnablePolicyTypeRequest,
            opts: Dict = None,
    ) -> models.EnablePolicyTypeResponse:
        """
        启用策略类型
        """
        
        kwargs = {}
        kwargs["action"] = "EnablePolicyType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnablePolicyTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetExternalSAMLIdentityProvider(
            self,
            request: models.GetExternalSAMLIdentityProviderRequest,
            opts: Dict = None,
    ) -> models.GetExternalSAMLIdentityProviderResponse:
        """
        查询SAML身份提供商配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetExternalSAMLIdentityProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetExternalSAMLIdentityProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroup(
            self,
            request: models.GetGroupRequest,
            opts: Dict = None,
    ) -> models.GetGroupResponse:
        """
        查询用户组信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProvisioningTaskStatus(
            self,
            request: models.GetProvisioningTaskStatusRequest,
            opts: Dict = None,
    ) -> models.GetProvisioningTaskStatusResponse:
        """
        查询用户同步异步任务的状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetProvisioningTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProvisioningTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRoleConfiguration(
            self,
            request: models.GetRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.GetRoleConfigurationResponse:
        """
        查询权限配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSCIMSynchronizationStatus(
            self,
            request: models.GetSCIMSynchronizationStatusRequest,
            opts: Dict = None,
    ) -> models.GetSCIMSynchronizationStatusResponse:
        """
        获取SCIM同步状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetSCIMSynchronizationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSCIMSynchronizationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskStatus(
            self,
            request: models.GetTaskStatusRequest,
            opts: Dict = None,
    ) -> models.GetTaskStatusResponse:
        """
        查询异步任务的状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUser(
            self,
            request: models.GetUserRequest,
            opts: Dict = None,
    ) -> models.GetUserResponse:
        """
        查询用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserSyncProvisioning(
            self,
            request: models.GetUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.GetUserSyncProvisioningResponse:
        """
        查询CAM用户同步
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetZoneSAMLServiceProviderInfo(
            self,
            request: models.GetZoneSAMLServiceProviderInfoRequest,
            opts: Dict = None,
    ) -> models.GetZoneSAMLServiceProviderInfoResponse:
        """
        查询SAML服务提供商配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetZoneSAMLServiceProviderInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetZoneSAMLServiceProviderInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetZoneStatistics(
            self,
            request: models.GetZoneStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetZoneStatisticsResponse:
        """
        查询空间的统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetZoneStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetZoneStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InviteOrganizationMember(
            self,
            request: models.InviteOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.InviteOrganizationMemberResponse:
        """
        邀请组织成员
        """
        
        kwargs = {}
        kwargs["action"] = "InviteOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InviteOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListExternalSAMLIdPCertificates(
            self,
            request: models.ListExternalSAMLIdPCertificatesRequest,
            opts: Dict = None,
    ) -> models.ListExternalSAMLIdPCertificatesResponse:
        """
        查询SAML签名证书列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListExternalSAMLIdPCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListExternalSAMLIdPCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroupMembers(
            self,
            request: models.ListGroupMembersRequest,
            opts: Dict = None,
    ) -> models.ListGroupMembersResponse:
        """
        查询用户组中的用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupMembersResponse
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
        
    async def ListJoinedGroupsForUser(
            self,
            request: models.ListJoinedGroupsForUserRequest,
            opts: Dict = None,
    ) -> models.ListJoinedGroupsForUserResponse:
        """
        查询用户加入的用户组
        """
        
        kwargs = {}
        kwargs["action"] = "ListJoinedGroupsForUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListJoinedGroupsForUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListNonCompliantResource(
            self,
            request: models.ListNonCompliantResourceRequest,
            opts: Dict = None,
    ) -> models.ListNonCompliantResourceResponse:
        """
        获取成员标签检测不合规资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListNonCompliantResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListNonCompliantResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrgServiceAssignMember(
            self,
            request: models.ListOrgServiceAssignMemberRequest,
            opts: Dict = None,
    ) -> models.ListOrgServiceAssignMemberResponse:
        """
        获取集团服务委派管理员列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrgServiceAssignMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrgServiceAssignMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationIdentity(
            self,
            request: models.ListOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationIdentityResponse:
        """
        获取组织成员访问身份列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationService(
            self,
            request: models.ListOrganizationServiceRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationServiceResponse:
        """
        获取集团服务设置列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPermissionPoliciesInRoleConfiguration(
            self,
            request: models.ListPermissionPoliciesInRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.ListPermissionPoliciesInRoleConfigurationResponse:
        """
        获取权限配置中的策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListPermissionPoliciesInRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPermissionPoliciesInRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPolicies(
            self,
            request: models.ListPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListPoliciesResponse:
        """
        本接口（ListPolicies）可用于查询查看策略列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "ListPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPoliciesForTarget(
            self,
            request: models.ListPoliciesForTargetRequest,
            opts: Dict = None,
    ) -> models.ListPoliciesForTargetResponse:
        """
        本接口（ListPoliciesForTarget）查询目标关联的策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListPoliciesForTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPoliciesForTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRoleAssignments(
            self,
            request: models.ListRoleAssignmentsRequest,
            opts: Dict = None,
    ) -> models.ListRoleAssignmentsResponse:
        """
        查询授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRoleAssignments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRoleAssignmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRoleConfigurationProvisionings(
            self,
            request: models.ListRoleConfigurationProvisioningsRequest,
            opts: Dict = None,
    ) -> models.ListRoleConfigurationProvisioningsResponse:
        """
        查询权限配置部署列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRoleConfigurationProvisionings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRoleConfigurationProvisioningsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRoleConfigurations(
            self,
            request: models.ListRoleConfigurationsRequest,
            opts: Dict = None,
    ) -> models.ListRoleConfigurationsResponse:
        """
        查询权限配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRoleConfigurations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRoleConfigurationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSCIMCredentials(
            self,
            request: models.ListSCIMCredentialsRequest,
            opts: Dict = None,
    ) -> models.ListSCIMCredentialsResponse:
        """
        查询用户SCIM密钥列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSCIMCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSCIMCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTargetsForPolicy(
            self,
            request: models.ListTargetsForPolicyRequest,
            opts: Dict = None,
    ) -> models.ListTargetsForPolicyResponse:
        """
        本接口（ListTargetsForPolicy）查询某个指定策略关联的目标列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTargetsForPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTargetsForPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTasks(
            self,
            request: models.ListTasksRequest,
            opts: Dict = None,
    ) -> models.ListTasksResponse:
        """
        查询异步任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserSyncProvisionings(
            self,
            request: models.ListUserSyncProvisioningsRequest,
            opts: Dict = None,
    ) -> models.ListUserSyncProvisioningsResponse:
        """
        查询CAM用户同步列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserSyncProvisionings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserSyncProvisioningsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsers(
            self,
            request: models.ListUsersRequest,
            opts: Dict = None,
    ) -> models.ListUsersResponse:
        """
        查询用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveOrganizationNodeMembers(
            self,
            request: models.MoveOrganizationNodeMembersRequest,
            opts: Dict = None,
    ) -> models.MoveOrganizationNodeMembersResponse:
        """
        移动成员到指定企业组织节点
        """
        
        kwargs = {}
        kwargs["action"] = "MoveOrganizationNodeMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveOrganizationNodeMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenIdentityCenter(
            self,
            request: models.OpenIdentityCenterRequest,
            opts: Dict = None,
    ) -> models.OpenIdentityCenterResponse:
        """
        开通身份中心服务（CIC）
        """
        
        kwargs = {}
        kwargs["action"] = "OpenIdentityCenter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenIdentityCenterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProvisionRoleConfiguration(
            self,
            request: models.ProvisionRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.ProvisionRoleConfigurationResponse:
        """
        将权限配置部署到成员账号上
        """
        
        kwargs = {}
        kwargs["action"] = "ProvisionRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProvisionRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuitOrganization(
            self,
            request: models.QuitOrganizationRequest,
            opts: Dict = None,
    ) -> models.QuitOrganizationResponse:
        """
        退出企业组织
        """
        
        kwargs = {}
        kwargs["action"] = "QuitOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuitOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectJoinShareUnitInvitation(
            self,
            request: models.RejectJoinShareUnitInvitationRequest,
            opts: Dict = None,
    ) -> models.RejectJoinShareUnitInvitationResponse:
        """
        拒绝加入共享单元邀请。
        """
        
        kwargs = {}
        kwargs["action"] = "RejectJoinShareUnitInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectJoinShareUnitInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveExternalSAMLIdPCertificate(
            self,
            request: models.RemoveExternalSAMLIdPCertificateRequest,
            opts: Dict = None,
    ) -> models.RemoveExternalSAMLIdPCertificateResponse:
        """
        移除SAML签名证书
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveExternalSAMLIdPCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveExternalSAMLIdPCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemovePermissionPolicyFromRoleConfiguration(
            self,
            request: models.RemovePermissionPolicyFromRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.RemovePermissionPolicyFromRoleConfigurationResponse:
        """
        为权限配置移除策略
        """
        
        kwargs = {}
        kwargs["action"] = "RemovePermissionPolicyFromRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemovePermissionPolicyFromRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserFromGroup(
            self,
            request: models.RemoveUserFromGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveUserFromGroupResponse:
        """
        从用户组中移除用户
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserFromGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserFromGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendOrgMemberAccountBindEmail(
            self,
            request: models.SendOrgMemberAccountBindEmailRequest,
            opts: Dict = None,
    ) -> models.SendOrgMemberAccountBindEmailResponse:
        """
        重新发送成员绑定邮箱激活邮件
        """
        
        kwargs = {}
        kwargs["action"] = "SendOrgMemberAccountBindEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendOrgMemberAccountBindEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetExternalSAMLIdentityProvider(
            self,
            request: models.SetExternalSAMLIdentityProviderRequest,
            opts: Dict = None,
    ) -> models.SetExternalSAMLIdentityProviderResponse:
        """
        配置SAML身份提供商信息
        """
        
        kwargs = {}
        kwargs["action"] = "SetExternalSAMLIdentityProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetExternalSAMLIdentityProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCustomPolicyForRoleConfiguration(
            self,
            request: models.UpdateCustomPolicyForRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpdateCustomPolicyForRoleConfigurationResponse:
        """
        为权限配置修改自定义策略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCustomPolicyForRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCustomPolicyForRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGroup(
            self,
            request: models.UpdateGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateGroupResponse:
        """
        修改用户组信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationIdentity(
            self,
            request: models.UpdateOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationIdentityResponse:
        """
        更新组织身份
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMember(
            self,
            request: models.UpdateOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMemberResponse:
        """
        更新组织成员信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMemberEmailBind(
            self,
            request: models.UpdateOrganizationMemberEmailBindRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMemberEmailBindResponse:
        """
        修改绑定成员邮箱
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMemberEmailBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMemberEmailBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMembersPolicy(
            self,
            request: models.UpdateOrganizationMembersPolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMembersPolicyResponse:
        """
        修改组织成员访问策略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMembersPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMembersPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationNode(
            self,
            request: models.UpdateOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationNodeResponse:
        """
        更新企业组织节点
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePolicy(
            self,
            request: models.UpdatePolicyRequest,
            opts: Dict = None,
    ) -> models.UpdatePolicyResponse:
        """
        编辑策略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleConfiguration(
            self,
            request: models.UpdateRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleConfigurationResponse:
        """
        修改权限配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSCIMCredentialStatus(
            self,
            request: models.UpdateSCIMCredentialStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateSCIMCredentialStatusResponse:
        """
        启用/禁用SCIM密钥
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSCIMCredentialStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSCIMCredentialStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSCIMSynchronizationStatus(
            self,
            request: models.UpdateSCIMSynchronizationStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateSCIMSynchronizationStatusResponse:
        """
        启用/禁用用户SCIM同步
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSCIMSynchronizationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSCIMSynchronizationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateShareUnit(
            self,
            request: models.UpdateShareUnitRequest,
            opts: Dict = None,
    ) -> models.UpdateShareUnitResponse:
        """
        更新共享单元。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateShareUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateShareUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUser(
            self,
            request: models.UpdateUserRequest,
            opts: Dict = None,
    ) -> models.UpdateUserResponse:
        """
        修改用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserStatus(
            self,
            request: models.UpdateUserStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateUserStatusResponse:
        """
        修改用户状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserSyncProvisioning(
            self,
            request: models.UpdateUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.UpdateUserSyncProvisioningResponse:
        """
        创建子用户同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateZone(
            self,
            request: models.UpdateZoneRequest,
            opts: Dict = None,
    ) -> models.UpdateZoneResponse:
        """
        更新用户空间名
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)