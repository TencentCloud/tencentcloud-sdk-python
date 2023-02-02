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
from tencentcloud.eiam.v20210420 import models


class EiamClient(AbstractClient):
    _apiVersion = '2021-04-20'
    _endpoint = 'eiam.tencentcloudapi.com'
    _service = 'eiam'


    def AddAccountToAccountGroup(self, request):
        """账号组添加账号

        :param request: Request instance for AddAccountToAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.AddAccountToAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.AddAccountToAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAccountToAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddAccountToAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddUserToUserGroup(self, request):
        """加入用户到用户组

        :param request: Request instance for AddUserToUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.AddUserToUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.AddUserToUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserToUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserToUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccountGroup(self, request):
        """创建账号组

        :param request: Request instance for CreateAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.CreateAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.CreateAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAppAccount(self, request):
        """创建应用账号

        :param request: Request instance for CreateAppAccount.
        :type request: :class:`tencentcloud.eiam.v20210420.models.CreateAppAccountRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.CreateAppAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOrgNode(self, request):
        """新建一个机构节点

        :param request: Request instance for CreateOrgNode.
        :type request: :class:`tencentcloud.eiam.v20210420.models.CreateOrgNodeRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.CreateOrgNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrgNode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrgNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUser(self, request):
        """新建一个用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.eiam.v20210420.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.CreateUserResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUserGroup(self, request):
        """新建用户组

        :param request: Request instance for CreateUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.CreateUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.CreateUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccountGroup(self, request):
        """删除账号组

        :param request: Request instance for DeleteAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DeleteAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DeleteAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAppAccount(self, request):
        """删除应用账号

        :param request: Request instance for DeleteAppAccount.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DeleteAppAccountRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DeleteAppAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAppAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteOrgNode(self, request):
        """删除一个机构节点

        :param request: Request instance for DeleteOrgNode.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DeleteOrgNodeRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DeleteOrgNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrgNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrgNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUser(self, request):
        """通过用户名或用户 id 删除用户。

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DeleteUserResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUserGroup(self, request):
        """删除一个用户组

        :param request: Request instance for DeleteUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DeleteUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DeleteUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUsers(self, request):
        """批量删除当前节点下的用户。如果出现个别用户删除错误，将不影响其余被勾选用户被删除的操作，同时提示未被删除的用户名称/用户ID。

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountGroup(self, request):
        """查询账号组列表

        :param request: Request instance for DescribeAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppAccount(self, request):
        """查询应用账号列表

        :param request: Request instance for DescribeAppAccount.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeAppAccountRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeAppAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplication(self, request):
        """获取一个应用的信息。

        :param request: Request instance for DescribeApplication.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeApplicationRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrgNode(self, request):
        """根据机构节点ID读取机构节点信息

        :param request: Request instance for DescribeOrgNode.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeOrgNodeRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeOrgNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrgNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrgNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrgResourcesAuthorization(self, request):
        """查询指定机构下的资源授权列表

        :param request: Request instance for DescribeOrgResourcesAuthorization.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeOrgResourcesAuthorizationRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeOrgResourcesAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrgResourcesAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrgResourcesAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePublicKey(self, request):
        """获取JWT公钥信息。

        :param request: Request instance for DescribePublicKey.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribePublicKeyRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribePublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserGroup(self, request):
        """获取用户组信息

        :param request: Request instance for DescribeUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserGroupResourcesAuthorization(self, request):
        """查询指定用户组下的资源授权列表

        :param request: Request instance for DescribeUserGroupResourcesAuthorization.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeUserGroupResourcesAuthorizationRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeUserGroupResourcesAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroupResourcesAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserGroupResourcesAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserInfo(self, request):
        """通过用户名或用户 id 搜索用户

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserResourcesAuthorization(self, request):
        """查询指定用户下的资源授权列表

        :param request: Request instance for DescribeUserResourcesAuthorization.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeUserResourcesAuthorizationRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeUserResourcesAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserResourcesAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResourcesAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserThirdPartyAccountInfo(self, request):
        """通过用户名或用户 id 获取用户的第三方账号绑定信息。

        :param request: Request instance for DescribeUserThirdPartyAccountInfo.
        :type request: :class:`tencentcloud.eiam.v20210420.models.DescribeUserThirdPartyAccountInfoRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.DescribeUserThirdPartyAccountInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserThirdPartyAccountInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserThirdPartyAccountInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAccountInAccountGroup(self, request):
        """获取账号组中的账号列表

        :param request: Request instance for ListAccountInAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListAccountInAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListAccountInAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAccountInAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ListAccountInAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListApplicationAuthorizations(self, request):
        """应用授权关系列表（含搜索条件匹配）。

        :param request: Request instance for ListApplicationAuthorizations.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListApplicationAuthorizationsRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListApplicationAuthorizationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListApplicationAuthorizations", params, headers=headers)
            response = json.loads(body)
            model = models.ListApplicationAuthorizationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListApplications(self, request):
        """获取应用列表信息。

        :param request: Request instance for ListApplications.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListApplicationsRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListApplications", params, headers=headers)
            response = json.loads(body)
            model = models.ListApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAuthorizedApplicationsToOrgNode(self, request):
        """通过机构节点ID获得被授权访问的应用列表。

        :param request: Request instance for ListAuthorizedApplicationsToOrgNode.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListAuthorizedApplicationsToOrgNodeRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListAuthorizedApplicationsToOrgNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAuthorizedApplicationsToOrgNode", params, headers=headers)
            response = json.loads(body)
            model = models.ListAuthorizedApplicationsToOrgNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAuthorizedApplicationsToUser(self, request):
        """通过用户ID获得被授权访问的应用列表。

        :param request: Request instance for ListAuthorizedApplicationsToUser.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListAuthorizedApplicationsToUserRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListAuthorizedApplicationsToUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAuthorizedApplicationsToUser", params, headers=headers)
            response = json.loads(body)
            model = models.ListAuthorizedApplicationsToUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAuthorizedApplicationsToUserGroup(self, request):
        """通过用户组ID获得被授权访问的应用列表。

        :param request: Request instance for ListAuthorizedApplicationsToUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListAuthorizedApplicationsToUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListAuthorizedApplicationsToUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAuthorizedApplicationsToUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ListAuthorizedApplicationsToUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListUserGroups(self, request):
        """获取用户组列表信息（包含查询条件）。

        :param request: Request instance for ListUserGroups.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListUserGroupsRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListUserGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListUserGroupsOfUser(self, request):
        """获取用户所在的用户组列表

        :param request: Request instance for ListUserGroupsOfUser.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListUserGroupsOfUserRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListUserGroupsOfUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserGroupsOfUser", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserGroupsOfUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListUsers(self, request):
        """获取用户列表信息。

        :param request: Request instance for ListUsers.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListUsersRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListUsersResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def ListUsersInOrgNode(self, request):
        """根据机构节点ID读取节点下用户

        :param request: Request instance for ListUsersInOrgNode.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListUsersInOrgNodeRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListUsersInOrgNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsersInOrgNode", params, headers=headers)
            response = json.loads(body)
            model = models.ListUsersInOrgNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListUsersInUserGroup(self, request):
        """获取用户组中的用户列表

        :param request: Request instance for ListUsersInUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ListUsersInUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ListUsersInUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsersInUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ListUsersInUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccountGroup(self, request):
        """修改账号组

        :param request: Request instance for ModifyAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ModifyAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ModifyAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAppAccount(self, request):
        """修改应用账号

        :param request: Request instance for ModifyAppAccount.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ModifyAppAccountRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ModifyAppAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAppAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplication(self, request):
        """更新一个应用的信息

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUserInfo(self, request):
        """通过用户名或用户 id 冻结用户

        :param request: Request instance for ModifyUserInfo.
        :type request: :class:`tencentcloud.eiam.v20210420.models.ModifyUserInfoRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.ModifyUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveAccountFromAccountGroup(self, request):
        """从账号组中移除账号

        :param request: Request instance for RemoveAccountFromAccountGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.RemoveAccountFromAccountGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.RemoveAccountFromAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveAccountFromAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveAccountFromAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveUserFromUserGroup(self, request):
        """从用户组中移除用户

        :param request: Request instance for RemoveUserFromUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.RemoveUserFromUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.RemoveUserFromUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserFromUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserFromUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateOrgNode(self, request):
        """新建一个机构节点，

        :param request: Request instance for UpdateOrgNode.
        :type request: :class:`tencentcloud.eiam.v20210420.models.UpdateOrgNodeRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.UpdateOrgNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrgNode", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrgNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)