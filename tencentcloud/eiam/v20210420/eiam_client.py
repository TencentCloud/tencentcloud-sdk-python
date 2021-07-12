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


    def AddUserToUserGroup(self, request):
        """加入用户到用户组

        :param request: Request instance for AddUserToUserGroup.
        :type request: :class:`tencentcloud.eiam.v20210420.models.AddUserToUserGroupRequest`
        :rtype: :class:`tencentcloud.eiam.v20210420.models.AddUserToUserGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUserToUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserToUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateOrgNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOrgNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteOrgNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOrgNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeOrgNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrgNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribePublicKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeUserInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListApplicationAuthorizations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListApplicationAuthorizationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListApplicationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListAuthorizedApplicationsToOrgNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAuthorizedApplicationsToOrgNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListAuthorizedApplicationsToUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAuthorizedApplicationsToUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListAuthorizedApplicationsToUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAuthorizedApplicationsToUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListUserGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUserGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListUserGroupsOfUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUserGroupsOfUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListUsersInOrgNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersInOrgNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ListUsersInUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersInUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyUserInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RemoveUserFromUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserFromUserGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UpdateOrgNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateOrgNodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)