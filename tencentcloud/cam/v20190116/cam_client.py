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
from tencentcloud.cam.v20190116 import models


class CamClient(AbstractClient):
    _apiVersion = '2019-01-16'
    _endpoint = 'cam.tencentcloudapi.com'
    _service = 'cam'


    def AddUser(self, request):
        """添加子用户

        :param request: Request instance for AddUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.AddUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AddUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserResponse()
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


    def AddUserToGroup(self, request):
        """用户加入到用户组

        :param request: Request instance for AddUserToGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.AddUserToGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AddUserToGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUserToGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserToGroupResponse()
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


    def AttachGroupPolicy(self, request):
        """本接口（AttachGroupPolicy）可用于绑定策略到用户组。

        :param request: Request instance for AttachGroupPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.AttachGroupPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AttachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachGroupPolicyResponse()
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


    def AttachRolePolicy(self, request):
        """本接口（AttachRolePolicy）用于绑定策略到角色。

        :param request: Request instance for AttachRolePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.AttachRolePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AttachRolePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachRolePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachRolePolicyResponse()
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


    def AttachUserPolicy(self, request):
        """本接口（AttachUserPolicy）可用于绑定到用户的策略。

        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.AttachUserPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachUserPolicyResponse()
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


    def ConsumeCustomMFAToken(self, request):
        """验证自定义多因子Token

        :param request: Request instance for ConsumeCustomMFAToken.
        :type request: :class:`tencentcloud.cam.v20190116.models.ConsumeCustomMFATokenRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ConsumeCustomMFATokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ConsumeCustomMFAToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ConsumeCustomMFATokenResponse()
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


    def CreateGroup(self, request):
        """创建用户组

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
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


    def CreatePolicy(self, request):
        """本接口（CreatePolicy）可用于创建策略。

        :param request: Request instance for CreatePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreatePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreatePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyResponse()
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


    def CreatePolicyVersion(self, request):
        """该接口（CreatePolicyVersion）用于新增策略版本，用户创建了一个策略版本之后可以方便的通过变更策略版本的方式来变更策略。

        :param request: Request instance for CreatePolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreatePolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreatePolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyVersionResponse()
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


    def CreateRole(self, request):
        """本接口（CreateRole）用于创建角色。

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoleResponse()
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


    def CreateSAMLProvider(self, request):
        """创建SAML身份提供商

        :param request: Request instance for CreateSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSAMLProviderResponse()
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


    def CreateServiceLinkedRole(self, request):
        """创建服务相关角色

        :param request: Request instance for CreateServiceLinkedRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateServiceLinkedRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateServiceLinkedRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceLinkedRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceLinkedRoleResponse()
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


    def DeleteGroup(self, request):
        """删除用户组

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
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


    def DeletePolicy(self, request):
        """本接口（DeletePolicy）可用于删除策略。

        :param request: Request instance for DeletePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeletePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeletePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyResponse()
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


    def DeletePolicyVersion(self, request):
        """本接口（DeletePolicyVersion）可用于删除一个策略的策略版本。

        :param request: Request instance for DeletePolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeletePolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeletePolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyVersionResponse()
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


    def DeleteRole(self, request):
        """本接口（DeleteRole）用于删除指定角色。

        :param request: Request instance for DeleteRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoleResponse()
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


    def DeleteRolePermissionsBoundary(self, request):
        """删除角色权限边界

        :param request: Request instance for DeleteRolePermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteRolePermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteRolePermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRolePermissionsBoundary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRolePermissionsBoundaryResponse()
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


    def DeleteSAMLProvider(self, request):
        """删除SAML身份提供商

        :param request: Request instance for DeleteSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSAMLProviderResponse()
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


    def DeleteServiceLinkedRole(self, request):
        """删除服务相关角色

        :param request: Request instance for DeleteServiceLinkedRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteServiceLinkedRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteServiceLinkedRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceLinkedRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceLinkedRoleResponse()
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
        """删除子用户

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteUserResponse`

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


    def DeleteUserPermissionsBoundary(self, request):
        """删除用户权限边界

        :param request: Request instance for DeleteUserPermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteUserPermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteUserPermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUserPermissionsBoundary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserPermissionsBoundaryResponse()
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


    def DescribeRoleList(self, request):
        """本接口（DescribeRoleList）用于获取账号下的角色列表。

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoleList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoleListResponse()
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


    def DescribeSafeAuthFlag(self, request):
        """查询安全设置

        :param request: Request instance for DescribeSafeAuthFlag.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSafeAuthFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSafeAuthFlagResponse()
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


    def DescribeSafeAuthFlagColl(self, request):
        """查询安全设置

        :param request: Request instance for DescribeSafeAuthFlagColl.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagCollRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagCollResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSafeAuthFlagColl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSafeAuthFlagCollResponse()
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


    def DescribeSubAccounts(self, request):
        """通过子用户UIN列表查询子用户

        :param request: Request instance for DescribeSubAccounts.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeSubAccountsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeSubAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubAccountsResponse()
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


    def DetachGroupPolicy(self, request):
        """本接口（DetachGroupPolicy）可用于解除绑定到用户组的策略。

        :param request: Request instance for DetachGroupPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DetachGroupPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DetachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachGroupPolicyResponse()
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


    def DetachRolePolicy(self, request):
        """本接口（DetachRolePolicy）用于解除绑定角色的策略。

        :param request: Request instance for DetachRolePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DetachRolePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DetachRolePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachRolePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachRolePolicyResponse()
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


    def DetachUserPolicy(self, request):
        """本接口（DetachUserPolicy）可用于解除绑定到用户的策略。

        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DetachUserPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachUserPolicyResponse()
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


    def GetCustomMFATokenInfo(self, request):
        """获取自定义多因子Token关联信息

        :param request: Request instance for GetCustomMFATokenInfo.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetCustomMFATokenInfoRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetCustomMFATokenInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCustomMFATokenInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCustomMFATokenInfoResponse()
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


    def GetGroup(self, request):
        """查询用户组详情

        :param request: Request instance for GetGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupResponse()
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


    def GetPolicy(self, request):
        """本接口（GetPolicy）可用于查询查看策略详情。

        :param request: Request instance for GetPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyResponse()
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


    def GetPolicyVersion(self, request):
        """该接口（GetPolicyVersion）用于查询策略版本详情

        :param request: Request instance for GetPolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetPolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetPolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyVersionResponse()
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


    def GetRole(self, request):
        """本接口（GetRole）用于获取指定角色的详细信息。

        :param request: Request instance for GetRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRoleResponse()
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


    def GetSAMLProvider(self, request):
        """查询SAML身份提供商详情

        :param request: Request instance for GetSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSAMLProviderResponse()
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


    def GetSecurityLastUsed(self, request):
        """获取密钥最近使用情况

        :param request: Request instance for GetSecurityLastUsed.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetSecurityLastUsedRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetSecurityLastUsedResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSecurityLastUsed", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSecurityLastUsedResponse()
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


    def GetServiceLinkedRoleDeletionStatus(self, request):
        """根据删除TaskId获取服务相关角色删除状态

        :param request: Request instance for GetServiceLinkedRoleDeletionStatus.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetServiceLinkedRoleDeletionStatusRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetServiceLinkedRoleDeletionStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetServiceLinkedRoleDeletionStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceLinkedRoleDeletionStatusResponse()
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


    def GetUser(self, request):
        """查询子用户

        :param request: Request instance for GetUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserResponse()
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


    def ListAccessKeys(self, request):
        """列出指定CAM用户的访问密钥

        :param request: Request instance for ListAccessKeys.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAccessKeysRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAccessKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAccessKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAccessKeysResponse()
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


    def ListAttachedGroupPolicies(self, request):
        """本接口（ListAttachedGroupPolicies）可用于查询用户组关联的策略列表。

        :param request: Request instance for ListAttachedGroupPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedGroupPoliciesResponse()
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


    def ListAttachedRolePolicies(self, request):
        """本接口（ListAttachedRolePolicies）用于获取角色绑定的策略列表。

        :param request: Request instance for ListAttachedRolePolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedRolePoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedRolePoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedRolePolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedRolePoliciesResponse()
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


    def ListAttachedUserPolicies(self, request):
        """本接口（ListAttachedUserPolicies）可用于查询子账号关联的策略列表。

        :param request: Request instance for ListAttachedUserPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedUserPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedUserPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedUserPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedUserPoliciesResponse()
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


    def ListCollaborators(self, request):
        """获取协作者列表

        :param request: Request instance for ListCollaborators.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListCollaboratorsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListCollaboratorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListCollaborators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCollaboratorsResponse()
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


    def ListEntitiesForPolicy(self, request):
        """本接口（ListEntitiesForPolicy）可用于查询策略关联的实体列表。

        :param request: Request instance for ListEntitiesForPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListEntitiesForPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListEntitiesForPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEntitiesForPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEntitiesForPolicyResponse()
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


    def ListGroups(self, request):
        """查询用户组列表

        :param request: Request instance for ListGroups.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListGroupsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsResponse()
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


    def ListGroupsForUser(self, request):
        """列出用户关联的用户组

        :param request: Request instance for ListGroupsForUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListGroupsForUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListGroupsForUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListGroupsForUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsForUserResponse()
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


    def ListPolicies(self, request):
        """本接口（ListPolicies）可用于查询策略列表。

        :param request: Request instance for ListPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPoliciesResponse()
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


    def ListPoliciesGrantingServiceAccess(self, request):
        """获取所有已授权服务

        :param request: Request instance for ListPoliciesGrantingServiceAccess.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListPoliciesGrantingServiceAccessRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListPoliciesGrantingServiceAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListPoliciesGrantingServiceAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPoliciesGrantingServiceAccessResponse()
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


    def ListPolicyVersions(self, request):
        """该接口（ListPolicyVersions）用于获取策略版本列表

        :param request: Request instance for ListPolicyVersions.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListPolicyVersionsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListPolicyVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListPolicyVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPolicyVersionsResponse()
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


    def ListSAMLProviders(self, request):
        """查询SAML身份提供商列表

        :param request: Request instance for ListSAMLProviders.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListSAMLProvidersRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListSAMLProvidersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSAMLProviders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSAMLProvidersResponse()
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
        """拉取子用户

        :param request: Request instance for ListUsers.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListUsersRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListUsersResponse`

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


    def ListUsersForGroup(self, request):
        """查询用户组关联的用户列表

        :param request: Request instance for ListUsersForGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListUsersForGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListUsersForGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListUsersForGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersForGroupResponse()
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


    def ListWeChatWorkSubAccounts(self, request):
        """获取企业微信子用户列表

        :param request: Request instance for ListWeChatWorkSubAccounts.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListWeChatWorkSubAccountsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListWeChatWorkSubAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListWeChatWorkSubAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListWeChatWorkSubAccountsResponse()
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


    def PutRolePermissionsBoundary(self, request):
        """设置角色权限边界

        :param request: Request instance for PutRolePermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.PutRolePermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.PutRolePermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutRolePermissionsBoundary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutRolePermissionsBoundaryResponse()
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


    def PutUserPermissionsBoundary(self, request):
        """设置用户权限边界

        :param request: Request instance for PutUserPermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.PutUserPermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.PutUserPermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutUserPermissionsBoundary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutUserPermissionsBoundaryResponse()
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


    def RemoveUserFromGroup(self, request):
        """从用户组删除用户

        :param request: Request instance for RemoveUserFromGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.RemoveUserFromGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.RemoveUserFromGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUserFromGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserFromGroupResponse()
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


    def SetDefaultPolicyVersion(self, request):
        """本接口（SetDefaultPolicyVersion）可用于设置生效的策略版本。

        :param request: Request instance for SetDefaultPolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.SetDefaultPolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.SetDefaultPolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetDefaultPolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetDefaultPolicyVersionResponse()
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


    def SetMfaFlag(self, request):
        """设置子用户的登录保护和敏感操作校验方式

        :param request: Request instance for SetMfaFlag.
        :type request: :class:`tencentcloud.cam.v20190116.models.SetMfaFlagRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.SetMfaFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetMfaFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetMfaFlagResponse()
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


    def UpdateAssumeRolePolicy(self, request):
        """本接口（UpdateAssumeRolePolicy）用于修改角色信任策略的策略文档。

        :param request: Request instance for UpdateAssumeRolePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateAssumeRolePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateAssumeRolePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAssumeRolePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAssumeRolePolicyResponse()
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


    def UpdateGroup(self, request):
        """更新用户组

        :param request: Request instance for UpdateGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGroupResponse()
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


    def UpdatePolicy(self, request):
        """本接口（UpdatePolicy ）可用于更新策略。
        如果已存在策略版本，本接口会直接更新策略的默认版本，不会创建新版本，如果不存在任何策略版本，则直接创建一个默认版本。

        :param request: Request instance for UpdatePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdatePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdatePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdatePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePolicyResponse()
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


    def UpdateRoleConsoleLogin(self, request):
        """本接口（UpdateRoleConsoleLogin）用于修改角色是否可登录。

        :param request: Request instance for UpdateRoleConsoleLogin.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateRoleConsoleLoginRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateRoleConsoleLoginResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRoleConsoleLogin", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRoleConsoleLoginResponse()
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


    def UpdateRoleDescription(self, request):
        """本接口（UpdateRoleDescription）用于修改角色的描述信息。

        :param request: Request instance for UpdateRoleDescription.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateRoleDescriptionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateRoleDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRoleDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRoleDescriptionResponse()
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


    def UpdateSAMLProvider(self, request):
        """更新SAML身份提供商信息

        :param request: Request instance for UpdateSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSAMLProviderResponse()
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


    def UpdateUser(self, request):
        """更新子用户

        :param request: Request instance for UpdateUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUserResponse()
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