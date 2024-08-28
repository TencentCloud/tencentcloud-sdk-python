# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.organization.v20210331 import models


class OrganizationClient(AbstractClient):
    _apiVersion = '2021-03-31'
    _endpoint = 'organization.tencentcloudapi.com'
    _service = 'organization'


    def AcceptJoinShareUnitInvitation(self, request):
        """接受加入共享单元邀请。

        :param request: Request instance for AcceptJoinShareUnitInvitation.
        :type request: :class:`tencentcloud.organization.v20210331.models.AcceptJoinShareUnitInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AcceptJoinShareUnitInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptJoinShareUnitInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptJoinShareUnitInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddExternalSAMLIdPCertificate(self, request):
        """添加SAML签名证书

        :param request: Request instance for AddExternalSAMLIdPCertificate.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddExternalSAMLIdPCertificateRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddExternalSAMLIdPCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddExternalSAMLIdPCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.AddExternalSAMLIdPCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganizationMemberEmail(self, request):
        """添加组织成员邮箱

        :param request: Request instance for AddOrganizationMemberEmail.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddOrganizationMemberEmailRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddOrganizationMemberEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganizationMemberEmail", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationMemberEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganizationNode(self, request):
        """添加企业组织节点

        :param request: Request instance for AddOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddOrganizationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganizationNode", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddPermissionPolicyToRoleConfiguration(self, request):
        """为权限配置添加策略

        :param request: Request instance for AddPermissionPolicyToRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddPermissionPolicyToRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddPermissionPolicyToRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddPermissionPolicyToRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.AddPermissionPolicyToRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddShareUnit(self, request):
        """创建共享单元。

        :param request: Request instance for AddShareUnit.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddShareUnitRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddShareUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShareUnit", params, headers=headers)
            response = json.loads(body)
            model = models.AddShareUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddShareUnitMembers(self, request):
        """添加共享单元成员

        :param request: Request instance for AddShareUnitMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddShareUnitMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddShareUnitMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShareUnitMembers", params, headers=headers)
            response = json.loads(body)
            model = models.AddShareUnitMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddShareUnitResources(self, request):
        """添加共享单元资源

        :param request: Request instance for AddShareUnitResources.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddShareUnitResourcesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddShareUnitResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShareUnitResources", params, headers=headers)
            response = json.loads(body)
            model = models.AddShareUnitResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUserToGroup(self, request):
        """为用户组添加用户

        :param request: Request instance for AddUserToGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddUserToGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddUserToGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserToGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserToGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachPolicy(self, request):
        """绑定策略

        :param request: Request instance for AttachPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.AttachPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AttachPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AttachPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindOrganizationMemberAuthAccount(self, request):
        """绑定组织成员和组织管理员子账号的授权关系

        :param request: Request instance for BindOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindOrganizationMemberAuthAccount", params, headers=headers)
            response = json.loads(body)
            model = models.BindOrganizationMemberAuthAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelOrganizationMemberAuthAccount(self, request):
        """取消组织成员和组织管理员子账号的授权关系

        :param request: Request instance for CancelOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.CancelOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CancelOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelOrganizationMemberAuthAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CancelOrganizationMemberAuthAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAccountDelete(self, request):
        """成员账号删除检查

        :param request: Request instance for CheckAccountDelete.
        :type request: :class:`tencentcloud.organization.v20210331.models.CheckAccountDeleteRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CheckAccountDeleteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAccountDelete", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAccountDeleteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearExternalSAMLIdentityProvider(self, request):
        """清空SAML身份提供商配置信息

        :param request: Request instance for ClearExternalSAMLIdentityProvider.
        :type request: :class:`tencentcloud.organization.v20210331.models.ClearExternalSAMLIdentityProviderRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ClearExternalSAMLIdentityProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearExternalSAMLIdentityProvider", params, headers=headers)
            response = json.loads(body)
            model = models.ClearExternalSAMLIdentityProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroup(self, request):
        """创建用户组

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrgServiceAssign(self, request):
        """添加集团服务委派管理员

        :param request: Request instance for CreateOrgServiceAssign.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrgServiceAssignRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrgServiceAssignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrgServiceAssign", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrgServiceAssignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganization(self, request):
        """创建企业组织

        :param request: Request instance for CreateOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationIdentity(self, request):
        """添加组织身份

        :param request: Request instance for CreateOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMember(self, request):
        """创建组织成员

        :param request: Request instance for CreateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMemberAuthIdentity(self, request):
        """添加组织成员访问授权

        :param request: Request instance for CreateOrganizationMemberAuthIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberAuthIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberAuthIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMemberAuthIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberAuthIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMemberPolicy(self, request):
        """创建组织成员访问授权策略

        :param request: Request instance for CreateOrganizationMemberPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMemberPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMembersPolicy(self, request):
        """创建组织成员访问策略

        :param request: Request instance for CreateOrganizationMembersPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMembersPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMembersPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMembersPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMembersPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePolicy(self, request):
        """创建一个特殊类型的策略，您可以关联到企业组织Root节点、企业部门节点或者企业的成员账号。

        :param request: Request instance for CreatePolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreatePolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreatePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoleAssignment(self, request):
        """在成员账号上授权

        :param request: Request instance for CreateRoleAssignment.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateRoleAssignmentRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateRoleAssignmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoleAssignment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleAssignmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoleConfiguration(self, request):
        """创建权限配置

        :param request: Request instance for CreateRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """创建用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserSyncProvisioning(self, request):
        """创建子用户同步任务

        :param request: Request instance for CreateUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccount(self, request):
        """删除成员账号

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """删除用户组

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrgServiceAssign(self, request):
        """删除集团服务委派管理员

        :param request: Request instance for DeleteOrgServiceAssign.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrgServiceAssignRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrgServiceAssignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrgServiceAssign", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrgServiceAssignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganization(self, request):
        """删除企业组织

        :param request: Request instance for DeleteOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationIdentity(self, request):
        """删除组织身份

        :param request: Request instance for DeleteOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMemberAuthIdentity(self, request):
        """删除组织成员访问授权

        :param request: Request instance for DeleteOrganizationMemberAuthIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMemberAuthIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMemberAuthIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMemberAuthIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMemberAuthIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMembers(self, request):
        """从组织中移除成员账号，不会删除账号。

        :param request: Request instance for DeleteOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMembersPolicy(self, request):
        """删除组织成员访问策略

        :param request: Request instance for DeleteOrganizationMembersPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMembersPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMembersPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationNodes(self, request):
        """批量删除企业组织节点

        :param request: Request instance for DeleteOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePolicy(self, request):
        """删除策略

        :param request: Request instance for DeletePolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeletePolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeletePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoleAssignment(self, request):
        """移除成员账号上的授权

        :param request: Request instance for DeleteRoleAssignment.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteRoleAssignmentRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteRoleAssignmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoleAssignment", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleAssignmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoleConfiguration(self, request):
        """删除权限配置信息

        :param request: Request instance for DeleteRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareUnit(self, request):
        """删除共享单元。

        :param request: Request instance for DeleteShareUnit.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareUnit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareUnitMembers(self, request):
        """删除共享单元成员

        :param request: Request instance for DeleteShareUnitMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareUnitMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareUnitMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareUnitResources(self, request):
        """删除共享单元资源

        :param request: Request instance for DeleteShareUnitResources.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitResourcesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareUnitResources", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareUnitResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """删除用户

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserSyncProvisioning(self, request):
        """删除子用户同步任务

        :param request: Request instance for DeleteUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEffectivePolicy(self, request):
        """查询目标关联的有效策略

        :param request: Request instance for DescribeEffectivePolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeEffectivePolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeEffectivePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEffectivePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEffectivePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdentityCenter(self, request):
        """获取集团账号身份中心服务信息

        :param request: Request instance for DescribeIdentityCenter.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeIdentityCenterRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeIdentityCenterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentityCenter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentityCenterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganization(self, request):
        """获取企业组织信息

        :param request: Request instance for DescribeOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationAuthNode(self, request):
        """获取已设置管理员的互信主体关系列表

        :param request: Request instance for DescribeOrganizationAuthNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationAuthNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationAuthNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationAuthNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationAuthNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationFinancialByMember(self, request):
        """以成员维度获取组织财务信息

        :param request: Request instance for DescribeOrganizationFinancialByMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationFinancialByMember", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationFinancialByMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationFinancialByMonth(self, request):
        """以月维度获取组织财务信息趋势

        :param request: Request instance for DescribeOrganizationFinancialByMonth.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMonthRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMonthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationFinancialByMonth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationFinancialByMonthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationFinancialByProduct(self, request):
        """以产品维度获取组织财务信息

        :param request: Request instance for DescribeOrganizationFinancialByProduct.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByProductRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationFinancialByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationFinancialByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberAuthAccounts(self, request):
        """获取组织成员被绑定授权关系的子账号列表

        :param request: Request instance for DescribeOrganizationMemberAuthAccounts.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthAccountsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberAuthAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberAuthAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberAuthIdentities(self, request):
        """获取组织成员访问授权列表

        :param request: Request instance for DescribeOrganizationMemberAuthIdentities.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthIdentitiesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberAuthIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberAuthIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberEmailBind(self, request):
        """查询成员邮箱绑定详细信息

        :param request: Request instance for DescribeOrganizationMemberEmailBind.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberEmailBindRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberEmailBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberEmailBind", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberEmailBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberPolicies(self, request):
        """获取组织成员的授权策略列表

        :param request: Request instance for DescribeOrganizationMemberPolicies.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberPoliciesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMembers(self, request):
        """获取企业组织成员列表

        :param request: Request instance for DescribeOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationNodes(self, request):
        """获取组织节点列表

        :param request: Request instance for DescribeOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicy(self, request):
        """本接口（DescribePolicy）可用于查询查看策略详情。

        :param request: Request instance for DescribePolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribePolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicyConfig(self, request):
        """本接口（DescribePolicyConfig）可用于查询企业组织策略配置

        :param request: Request instance for DescribePolicyConfig.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribePolicyConfigRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribePolicyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareAreas(self, request):
        """获取可共享地域列表

        :param request: Request instance for DescribeShareAreas.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareAreasRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareUnitMembers(self, request):
        """获取共享单元成员列表。

        :param request: Request instance for DescribeShareUnitMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareUnitMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareUnitMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareUnitResources(self, request):
        """获取共享单元资源列表。

        :param request: Request instance for DescribeShareUnitResources.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitResourcesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareUnitResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareUnitResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareUnits(self, request):
        """获取共享单元列表。

        :param request: Request instance for DescribeShareUnits.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareUnits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareUnitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachPolicy(self, request):
        """解绑策略

        :param request: Request instance for DetachPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DetachPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DetachPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DetachPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisablePolicyType(self, request):
        """禁用策略类型

        :param request: Request instance for DisablePolicyType.
        :type request: :class:`tencentcloud.organization.v20210331.models.DisablePolicyTypeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DisablePolicyTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisablePolicyType", params, headers=headers)
            response = json.loads(body)
            model = models.DisablePolicyTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismantleRoleConfiguration(self, request):
        """解除权限配置在成员账号上的部署

        :param request: Request instance for DismantleRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.DismantleRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DismantleRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismantleRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DismantleRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnablePolicyType(self, request):
        """启用策略类型

        :param request: Request instance for EnablePolicyType.
        :type request: :class:`tencentcloud.organization.v20210331.models.EnablePolicyTypeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.EnablePolicyTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnablePolicyType", params, headers=headers)
            response = json.loads(body)
            model = models.EnablePolicyTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetExternalSAMLIdentityProvider(self, request):
        """查询SAML身份提供商配置信息

        :param request: Request instance for GetExternalSAMLIdentityProvider.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetExternalSAMLIdentityProviderRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetExternalSAMLIdentityProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetExternalSAMLIdentityProvider", params, headers=headers)
            response = json.loads(body)
            model = models.GetExternalSAMLIdentityProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroup(self, request):
        """查询用户组信息

        :param request: Request instance for GetGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProvisioningTaskStatus(self, request):
        """查询用户同步异步任务的状态

        :param request: Request instance for GetProvisioningTaskStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetProvisioningTaskStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetProvisioningTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProvisioningTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetProvisioningTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRoleConfiguration(self, request):
        """查询权限配置信息

        :param request: Request instance for GetRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskStatus(self, request):
        """查询异步任务的状态

        :param request: Request instance for GetTaskStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetTaskStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUser(self, request):
        """查询用户信息

        :param request: Request instance for GetUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUserSyncProvisioning(self, request):
        """查询CAM用户同步

        :param request: Request instance for GetUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.GetUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetZoneSAMLServiceProviderInfo(self, request):
        """查询SAML服务提供商配置信息

        :param request: Request instance for GetZoneSAMLServiceProviderInfo.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetZoneSAMLServiceProviderInfoRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetZoneSAMLServiceProviderInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetZoneSAMLServiceProviderInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetZoneSAMLServiceProviderInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetZoneStatistics(self, request):
        """查询空间的统计信息

        :param request: Request instance for GetZoneStatistics.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetZoneStatisticsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetZoneStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetZoneStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetZoneStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListExternalSAMLIdPCertificates(self, request):
        """查询SAML签名证书列表

        :param request: Request instance for ListExternalSAMLIdPCertificates.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListExternalSAMLIdPCertificatesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListExternalSAMLIdPCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListExternalSAMLIdPCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.ListExternalSAMLIdPCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListGroupMembers(self, request):
        """查询用户组中的用户列表

        :param request: Request instance for ListGroupMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListGroupMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGroupMembers", params, headers=headers)
            response = json.loads(body)
            model = models.ListGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListGroups(self, request):
        """查询用户组列表

        :param request: Request instance for ListGroups.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListGroupsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJoinedGroupsForUser(self, request):
        """查询用户加入的用户组

        :param request: Request instance for ListJoinedGroupsForUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListJoinedGroupsForUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListJoinedGroupsForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJoinedGroupsForUser", params, headers=headers)
            response = json.loads(body)
            model = models.ListJoinedGroupsForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListNonCompliantResource(self, request):
        """获取成员标签检测不合规资源列表

        :param request: Request instance for ListNonCompliantResource.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListNonCompliantResourceRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListNonCompliantResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListNonCompliantResource", params, headers=headers)
            response = json.loads(body)
            model = models.ListNonCompliantResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrgServiceAssignMember(self, request):
        """获取集团服务委派管理员列表

        :param request: Request instance for ListOrgServiceAssignMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrgServiceAssignMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrgServiceAssignMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrgServiceAssignMember", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrgServiceAssignMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationIdentity(self, request):
        """获取组织成员访问身份列表

        :param request: Request instance for ListOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationService(self, request):
        """获取集团服务设置列表

        :param request: Request instance for ListOrganizationService.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrganizationServiceRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrganizationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationService", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPermissionPoliciesInRoleConfiguration(self, request):
        """获取权限配置中的策略列表

        :param request: Request instance for ListPermissionPoliciesInRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListPermissionPoliciesInRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListPermissionPoliciesInRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPermissionPoliciesInRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ListPermissionPoliciesInRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPolicies(self, request):
        """本接口（ListPolicies）可用于查询查看策略列表数据

        :param request: Request instance for ListPolicies.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListPoliciesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ListPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPoliciesForTarget(self, request):
        """本接口（ListPoliciesForTarget）查询目标关联的策略列表

        :param request: Request instance for ListPoliciesForTarget.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListPoliciesForTargetRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListPoliciesForTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPoliciesForTarget", params, headers=headers)
            response = json.loads(body)
            model = models.ListPoliciesForTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRoleAssignments(self, request):
        """查询授权列表

        :param request: Request instance for ListRoleAssignments.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListRoleAssignmentsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListRoleAssignmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRoleAssignments", params, headers=headers)
            response = json.loads(body)
            model = models.ListRoleAssignmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRoleConfigurationProvisionings(self, request):
        """查询权限配置部署列表

        :param request: Request instance for ListRoleConfigurationProvisionings.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationProvisioningsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationProvisioningsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRoleConfigurationProvisionings", params, headers=headers)
            response = json.loads(body)
            model = models.ListRoleConfigurationProvisioningsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRoleConfigurations(self, request):
        """查询权限配置列表

        :param request: Request instance for ListRoleConfigurations.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRoleConfigurations", params, headers=headers)
            response = json.loads(body)
            model = models.ListRoleConfigurationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTargetsForPolicy(self, request):
        """本接口（ListTargetsForPolicy）查询某个指定策略关联的目标列表

        :param request: Request instance for ListTargetsForPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListTargetsForPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListTargetsForPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTargetsForPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ListTargetsForPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTasks(self, request):
        """查询异步任务列表

        :param request: Request instance for ListTasks.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListTasksRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUserSyncProvisionings(self, request):
        """查询CAM用户同步列表

        :param request: Request instance for ListUserSyncProvisionings.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListUserSyncProvisioningsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListUserSyncProvisioningsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserSyncProvisionings", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserSyncProvisioningsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUsers(self, request):
        """查询用户列表

        :param request: Request instance for ListUsers.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListUsersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ListUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveOrganizationNodeMembers(self, request):
        """移动成员到指定企业组织节点

        :param request: Request instance for MoveOrganizationNodeMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.MoveOrganizationNodeMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.MoveOrganizationNodeMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveOrganizationNodeMembers", params, headers=headers)
            response = json.loads(body)
            model = models.MoveOrganizationNodeMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenIdentityCenter(self, request):
        """开通身份中心服务（CIC）

        :param request: Request instance for OpenIdentityCenter.
        :type request: :class:`tencentcloud.organization.v20210331.models.OpenIdentityCenterRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.OpenIdentityCenterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenIdentityCenter", params, headers=headers)
            response = json.loads(body)
            model = models.OpenIdentityCenterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProvisionRoleConfiguration(self, request):
        """将权限配置部署到成员账号上

        :param request: Request instance for ProvisionRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.ProvisionRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ProvisionRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProvisionRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ProvisionRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QuitOrganization(self, request):
        """退出企业组织

        :param request: Request instance for QuitOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.QuitOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.QuitOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QuitOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.QuitOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectJoinShareUnitInvitation(self, request):
        """拒绝加入共享单元邀请。

        :param request: Request instance for RejectJoinShareUnitInvitation.
        :type request: :class:`tencentcloud.organization.v20210331.models.RejectJoinShareUnitInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RejectJoinShareUnitInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectJoinShareUnitInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.RejectJoinShareUnitInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveExternalSAMLIdPCertificate(self, request):
        """移除SAML签名证书

        :param request: Request instance for RemoveExternalSAMLIdPCertificate.
        :type request: :class:`tencentcloud.organization.v20210331.models.RemoveExternalSAMLIdPCertificateRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RemoveExternalSAMLIdPCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveExternalSAMLIdPCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveExternalSAMLIdPCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemovePermissionPolicyFromRoleConfiguration(self, request):
        """为权限配置移除策略

        :param request: Request instance for RemovePermissionPolicyFromRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.RemovePermissionPolicyFromRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RemovePermissionPolicyFromRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemovePermissionPolicyFromRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.RemovePermissionPolicyFromRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUserFromGroup(self, request):
        """从用户组中移除用户

        :param request: Request instance for RemoveUserFromGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.RemoveUserFromGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RemoveUserFromGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserFromGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserFromGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendOrgMemberAccountBindEmail(self, request):
        """重新发送成员绑定邮箱激活邮件

        :param request: Request instance for SendOrgMemberAccountBindEmail.
        :type request: :class:`tencentcloud.organization.v20210331.models.SendOrgMemberAccountBindEmailRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.SendOrgMemberAccountBindEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendOrgMemberAccountBindEmail", params, headers=headers)
            response = json.loads(body)
            model = models.SendOrgMemberAccountBindEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetExternalSAMLIdentityProvider(self, request):
        """配置SAML身份提供商信息

        :param request: Request instance for SetExternalSAMLIdentityProvider.
        :type request: :class:`tencentcloud.organization.v20210331.models.SetExternalSAMLIdentityProviderRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.SetExternalSAMLIdentityProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetExternalSAMLIdentityProvider", params, headers=headers)
            response = json.loads(body)
            model = models.SetExternalSAMLIdentityProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGroup(self, request):
        """修改用户组信息

        :param request: Request instance for UpdateGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationIdentity(self, request):
        """更新组织身份

        :param request: Request instance for UpdateOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationMember(self, request):
        """更新组织成员信息

        :param request: Request instance for UpdateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationMemberEmailBind(self, request):
        """修改绑定成员邮箱

        :param request: Request instance for UpdateOrganizationMemberEmailBind.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberEmailBindRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberEmailBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationMemberEmailBind", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationMemberEmailBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationNode(self, request):
        """更新企业组织节点

        :param request: Request instance for UpdateOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationNode", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePolicy(self, request):
        """编辑策略

        :param request: Request instance for UpdatePolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdatePolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdatePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRoleConfiguration(self, request):
        """修改权限配置信息

        :param request: Request instance for UpdateRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateShareUnit(self, request):
        """更新共享单元。

        :param request: Request instance for UpdateShareUnit.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateShareUnitRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateShareUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateShareUnit", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateShareUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUser(self, request):
        """修改用户信息

        :param request: Request instance for UpdateUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUser", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserStatus(self, request):
        """修改用户状态

        :param request: Request instance for UpdateUserStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateUserStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateUserStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserSyncProvisioning(self, request):
        """创建子用户同步任务

        :param request: Request instance for UpdateUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateZone(self, request):
        """更新用户空间名

        :param request: Request instance for UpdateZone.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateZoneRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateZone", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))