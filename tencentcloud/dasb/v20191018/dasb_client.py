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
from tencentcloud.dasb.v20191018 import models


class DasbClient(AbstractClient):
    _apiVersion = '2019-10-18'
    _endpoint = 'dasb.tencentcloudapi.com'
    _service = 'dasb'


    def AddDeviceGroupMembers(self, request):
        """添加资产组成员

        :param request: Request instance for AddDeviceGroupMembers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.AddDeviceGroupMembersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.AddDeviceGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDeviceGroupMembers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDeviceGroupMembersResponse()
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


    def AddUserGroupMembers(self, request):
        """添加用户组成员

        :param request: Request instance for AddUserGroupMembers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.AddUserGroupMembersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.AddUserGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserGroupMembers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserGroupMembersResponse()
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


    def BindDeviceResource(self, request):
        """修改资产绑定的堡垒机服务

        :param request: Request instance for BindDeviceResource.
        :type request: :class:`tencentcloud.dasb.v20191018.models.BindDeviceResourceRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.BindDeviceResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDeviceResource", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindDeviceResourceResponse()
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


    def CreateAcl(self, request):
        """新建访问权限

        :param request: Request instance for CreateAcl.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateAclRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAclResponse()
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


    def CreateDeviceGroup(self, request):
        """新建资产组

        :param request: Request instance for CreateDeviceGroup.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateDeviceGroupRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceGroupResponse()
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
        """新建用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
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
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateUserGroupRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserGroup", params, headers=headers)
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


    def DeleteAcls(self, request):
        """删除访问权限

        :param request: Request instance for DeleteAcls.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteAclsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAclsResponse()
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


    def DeleteDeviceGroupMembers(self, request):
        """删除资产组成员

        :param request: Request instance for DeleteDeviceGroupMembers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteDeviceGroupMembersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteDeviceGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceGroupMembers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceGroupMembersResponse()
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


    def DeleteDeviceGroups(self, request):
        """删除资产组

        :param request: Request instance for DeleteDeviceGroups.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteDeviceGroupsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteDeviceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceGroupsResponse()
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


    def DeleteUserGroupMembers(self, request):
        """删除用户组成员

        :param request: Request instance for DeleteUserGroupMembers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteUserGroupMembersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteUserGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserGroupMembers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserGroupMembersResponse()
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


    def DeleteUserGroups(self, request):
        """删除用户组

        :param request: Request instance for DeleteUserGroups.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteUserGroupsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteUserGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserGroupsResponse()
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


    def DeleteUsers(self, request):
        """删除用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUsersResponse()
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


    def DescribeAcls(self, request):
        """查询访问权限列表

        :param request: Request instance for DescribeAcls.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeAclsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAclsResponse()
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


    def DescribeDasbImageIds(self, request):
        """获取镜像列表

        :param request: Request instance for DescribeDasbImageIds.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDasbImageIdsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDasbImageIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDasbImageIds", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDasbImageIdsResponse()
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


    def DescribeDeviceGroupMembers(self, request):
        """查询资产组成员列表

        :param request: Request instance for DescribeDeviceGroupMembers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDeviceGroupMembersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDeviceGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceGroupMembers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceGroupMembersResponse()
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


    def DescribeDeviceGroups(self, request):
        """查询资产组列表

        :param request: Request instance for DescribeDeviceGroups.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDeviceGroupsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDeviceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceGroupsResponse()
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


    def DescribeDevices(self, request):
        """查询资产列表

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
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


    def DescribeResources(self, request):
        """查询用户购买的堡垒机服务信息，包括资源ID、授权点数、VPC、过期时间等。

        :param request: Request instance for DescribeResources.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeResourcesRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResources", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesResponse()
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


    def DescribeUserGroupMembers(self, request):
        """查询用户组成员列表

        :param request: Request instance for DescribeUserGroupMembers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeUserGroupMembersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeUserGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroupMembers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserGroupMembersResponse()
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


    def DescribeUserGroups(self, request):
        """查询用户组列表

        :param request: Request instance for DescribeUserGroups.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeUserGroupsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeUserGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserGroupsResponse()
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


    def DescribeUsers(self, request):
        """查询用户列表

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsersResponse()
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


    def ModifyAcl(self, request):
        """修改访问权限

        :param request: Request instance for ModifyAcl.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyAclRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAclResponse()
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


    def ModifyUser(self, request):
        """修改用户信息

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserResponse()
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