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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dasb.v20191018 import models


class DasbClient(AbstractClient):
    _apiVersion = '2019-10-18'
    _endpoint = 'dasb.tencentcloudapi.com'
    _service = 'dasb'


    def AddDeviceGroupMembers(self, request):
        r"""添加资产组成员

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUserGroupMembers(self, request):
        r"""添加用户组成员

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDeviceAccountPassword(self, request):
        r"""绑定主机账号密码

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDeviceAccountPrivateKey(self, request):
        r"""绑定主机账号私钥

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDeviceResource(self, request):
        r"""修改资产绑定的堡垒机服务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAcl(self, request):
        r"""新建访问权限

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetSyncJob(self, request):
        r"""创建手工资产同步任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChangePwdTask(self, request):
        r"""创建修改密码任务

        :param request: Request instance for CreateChangePwdTask.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateChangePwdTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChangePwdTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChangePwdTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCmdTemplate(self, request):
        r"""新建高危命令模板

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceAccount(self, request):
        r"""新建主机账号

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceGroup(self, request):
        r"""新建资产组

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResource(self, request):
        r"""创建堡垒机实例

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""新建用户

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserGroup(self, request):
        r"""新建用户组

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAcls(self, request):
        r"""删除访问权限

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteChangePwdTask(self, request):
        r"""删除改密任务

        :param request: Request instance for DeleteChangePwdTask.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteChangePwdTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteChangePwdTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteChangePwdTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCmdTemplates(self, request):
        r"""删除高危命令模板

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceAccounts(self, request):
        r"""删除主机账号

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceGroupMembers(self, request):
        r"""删除资产组成员

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceGroups(self, request):
        r"""删除资产组

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevices(self, request):
        r"""删除主机

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserGroupMembers(self, request):
        r"""删除用户组成员

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserGroups(self, request):
        r"""删除用户组

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsers(self, request):
        r"""删除用户

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployResource(self, request):
        r"""开通服务，初始化资源，只针对新购资源

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAcls(self, request):
        r"""查询访问权限列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSyncStatus(self, request):
        r"""查询资产同步状态

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChangePwdTask(self, request):
        r"""查询改密任务列表

        :param request: Request instance for DescribeChangePwdTask.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeChangePwdTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChangePwdTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChangePwdTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChangePwdTaskDetail(self, request):
        r"""查询改密任务详情

        :param request: Request instance for DescribeChangePwdTaskDetail.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeChangePwdTaskDetailRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeChangePwdTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChangePwdTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChangePwdTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmdTemplates(self, request):
        r"""查询命令模板列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDasbImageIds(self, request):
        r"""获取镜像列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceAccounts(self, request):
        r"""查询主机账号列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceGroupMembers(self, request):
        r"""查询资产组成员列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceGroups(self, request):
        r"""查询资产组列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevices(self, request):
        r"""查询资产列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        r"""查询网络域

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginEvent(self, request):
        r"""查询登录日志

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOperationEvent(self, request):
        r"""查询操作日志

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResources(self, request):
        r"""查询用户购买的堡垒机服务信息，包括资源ID、授权点数、VPC、过期时间等。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserGroupMembers(self, request):
        r"""查询用户组成员列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserGroups(self, request):
        r"""查询用户组列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsers(self, request):
        r"""查询用户列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportExternalDevice(self, request):
        r"""导入外部资产信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAcl(self, request):
        r"""修改访问权限

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyChangePwdTask(self, request):
        r"""更新修改密码任务

        :param request: Request instance for ModifyChangePwdTask.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyChangePwdTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyChangePwdTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyChangePwdTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCmdTemplate(self, request):
        r"""修改高危命令模板

        :param request: Request instance for ModifyCmdTemplate.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyCmdTemplateRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyCmdTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmdTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCmdTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDevice(self, request):
        r"""修改资产信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceGroup(self, request):
        r"""修改资产组

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOAuthSetting(self, request):
        r"""设置OAuth认证参数

        :param request: Request instance for ModifyOAuthSetting.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyOAuthSettingRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyOAuthSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOAuthSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOAuthSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResource(self, request):
        r"""资源变配

        :param request: Request instance for ModifyResource.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyResourceRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""修改用户信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserGroup(self, request):
        r"""修改用户组

        :param request: Request instance for ModifyUserGroup.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyUserGroupRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDeviceAccountPassword(self, request):
        r"""清除设备账号绑定密码

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDeviceAccountPrivateKey(self, request):
        r"""清除设备账号绑定的密钥

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetUser(self, request):
        r"""重置用户

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunChangePwdTask(self, request):
        r"""执行改密任务

        :param request: Request instance for RunChangePwdTask.
        :type request: :class:`tencentcloud.dasb.v20191018.models.RunChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.RunChangePwdTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunChangePwdTask", params, headers=headers)
            response = json.loads(body)
            model = models.RunChangePwdTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchAuditLog(self, request):
        r"""搜索审计日志

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchCommand(self, request):
        r"""命令执行检索

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchCommandBySid(self, request):
        r"""根据会话Id搜索Command

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchFile(self, request):
        r"""文件传输检索

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchFileBySid(self, request):
        r"""搜索文件传输会话下文件操作列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchSession(self, request):
        r"""搜索会话

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchSessionCommand(self, request):
        r"""命令检索

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
                raise TencentCloudSDKException(type(e).__name__, str(e))