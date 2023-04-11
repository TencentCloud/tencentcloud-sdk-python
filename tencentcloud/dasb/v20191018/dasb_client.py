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
            model = models.AddDeviceGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.AddUserGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindDeviceAccountPassword(self, request):
        """绑定主机账号密码

        :param request: Request instance for BindDeviceAccountPassword.
        :type request: :class:`tencentcloud.dasb.v20191018.models.BindDeviceAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.BindDeviceAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDeviceAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.BindDeviceAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindDeviceAccountPrivateKey(self, request):
        """绑定主机账号私钥

        :param request: Request instance for BindDeviceAccountPrivateKey.
        :type request: :class:`tencentcloud.dasb.v20191018.models.BindDeviceAccountPrivateKeyRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.BindDeviceAccountPrivateKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDeviceAccountPrivateKey", params, headers=headers)
            response = json.loads(body)
            model = models.BindDeviceAccountPrivateKeyResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.BindDeviceResourceResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.CreateAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetSyncJob(self, request):
        """创建手工资产同步任务

        :param request: Request instance for CreateAssetSyncJob.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateAssetSyncJobRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateAssetSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCmdTemplate(self, request):
        """新建高危命令模板

        :param request: Request instance for CreateCmdTemplate.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateCmdTemplateRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateCmdTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmdTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCmdTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDeviceAccount(self, request):
        """新建主机账号

        :param request: Request instance for CreateDeviceAccount.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateDeviceAccountRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateDeviceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceAccountResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.CreateDeviceGroupResponse()
            model._deserialize(response["Response"])
            return model
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
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateUserGroupRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateUserGroupResponse`

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
            model = models.DeleteAclsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCmdTemplates(self, request):
        """删除高危命令模板

        :param request: Request instance for DeleteCmdTemplates.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteCmdTemplatesRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteCmdTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmdTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCmdTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDeviceAccounts(self, request):
        """删除主机账号

        :param request: Request instance for DeleteDeviceAccounts.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteDeviceAccountsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteDeviceAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceAccountsResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DeleteDeviceGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DeleteDeviceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDevices(self, request):
        """删除主机

        :param request: Request instance for DeleteDevices.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteDevicesRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDevicesResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DeleteUserGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DeleteUserGroupsResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DeleteUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeployResource(self, request):
        """开通服务，初始化资源，只针对新购资源

        :param request: Request instance for DeployResource.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeployResourceRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeployResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeployResourceResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeAclsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetSyncStatus(self, request):
        """查询资产同步状态

        :param request: Request instance for DescribeAssetSyncStatus.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeAssetSyncStatusRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeAssetSyncStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSyncStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSyncStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCmdTemplates(self, request):
        """查询命令模板列表

        :param request: Request instance for DescribeCmdTemplates.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeCmdTemplatesRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeCmdTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmdTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmdTemplatesResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeDasbImageIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceAccounts(self, request):
        """查询主机账号列表

        :param request: Request instance for DescribeDeviceAccounts.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDeviceAccountsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDeviceAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceAccountsResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeDeviceGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeDeviceGroupsResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoginEvent(self, request):
        """查询登录日志

        :param request: Request instance for DescribeLoginEvent.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeLoginEventRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeLoginEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOperationEvent(self, request):
        """查询操作日志

        :param request: Request instance for DescribeOperationEvent.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeOperationEventRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeOperationEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperationEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperationEventResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeResourcesResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeUserGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeUserGroupsResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportExternalDevice(self, request):
        """导入外部资产信息

        :param request: Request instance for ImportExternalDevice.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ImportExternalDeviceRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ImportExternalDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportExternalDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ImportExternalDeviceResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.ModifyAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDevice(self, request):
        """修改资产信息

        :param request: Request instance for ModifyDevice.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDeviceGroup(self, request):
        """修改资产组

        :param request: Request instance for ModifyDeviceGroup.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyDeviceGroupRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceGroupResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetDeviceAccountPassword(self, request):
        """清除设备账号绑定密码

        :param request: Request instance for ResetDeviceAccountPassword.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ResetDeviceAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ResetDeviceAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDeviceAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDeviceAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetDeviceAccountPrivateKey(self, request):
        """清除设备账号绑定的密钥

        :param request: Request instance for ResetDeviceAccountPrivateKey.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ResetDeviceAccountPrivateKeyRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ResetDeviceAccountPrivateKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDeviceAccountPrivateKey", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDeviceAccountPrivateKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetUser(self, request):
        """重置用户

        :param request: Request instance for ResetUser.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ResetUserRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ResetUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetUser", params, headers=headers)
            response = json.loads(body)
            model = models.ResetUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchAuditLog(self, request):
        """搜索审计日志

        :param request: Request instance for SearchAuditLog.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchAuditLogRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchAuditLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchAuditLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchAuditLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchCommand(self, request):
        """命令执行检索

        :param request: Request instance for SearchCommand.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchCommandRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchCommand", params, headers=headers)
            response = json.loads(body)
            model = models.SearchCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchCommandBySid(self, request):
        """根据会话Id搜索Command

        :param request: Request instance for SearchCommandBySid.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchCommandBySidRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchCommandBySidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchCommandBySid", params, headers=headers)
            response = json.loads(body)
            model = models.SearchCommandBySidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchFile(self, request):
        """文件传输检索

        :param request: Request instance for SearchFile.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchFileRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchFile", params, headers=headers)
            response = json.loads(body)
            model = models.SearchFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchFileBySid(self, request):
        """搜索文件传输会话下文件操作列表

        :param request: Request instance for SearchFileBySid.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchFileBySidRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchFileBySidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchFileBySid", params, headers=headers)
            response = json.loads(body)
            model = models.SearchFileBySidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchSession(self, request):
        """搜索会话

        :param request: Request instance for SearchSession.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchSessionRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchSession", params, headers=headers)
            response = json.loads(body)
            model = models.SearchSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchSessionCommand(self, request):
        """命令检索

        :param request: Request instance for SearchSessionCommand.
        :type request: :class:`tencentcloud.dasb.v20191018.models.SearchSessionCommandRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.SearchSessionCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchSessionCommand", params, headers=headers)
            response = json.loads(body)
            model = models.SearchSessionCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)