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
from tencentcloud.bh.v20230418 import models


class BhClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'bh.tencentcloudapi.com'
    _service = 'bh'


    def AccessDevices(self, request):
        """外部客户访问资产

        :param request: Request instance for AccessDevices.
        :type request: :class:`tencentcloud.bh.v20230418.models.AccessDevicesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.AccessDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AccessDevices", params, headers=headers)
            response = json.loads(body)
            model = models.AccessDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDeviceGroupMembers(self, request):
        """添加资产组成员

        :param request: Request instance for AddDeviceGroupMembers.
        :type request: :class:`tencentcloud.bh.v20230418.models.AddDeviceGroupMembersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.AddDeviceGroupMembersResponse`

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
        """添加用户组成员

        :param request: Request instance for AddUserGroupMembers.
        :type request: :class:`tencentcloud.bh.v20230418.models.AddUserGroupMembersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.AddUserGroupMembersResponse`

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
        """绑定主机账号密码

        :param request: Request instance for BindDeviceAccountPassword.
        :type request: :class:`tencentcloud.bh.v20230418.models.BindDeviceAccountPasswordRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.BindDeviceAccountPasswordResponse`

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
        """绑定主机账号私钥

        :param request: Request instance for BindDeviceAccountPrivateKey.
        :type request: :class:`tencentcloud.bh.v20230418.models.BindDeviceAccountPrivateKeyRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.BindDeviceAccountPrivateKeyResponse`

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
        """修改资产绑定的堡垒机服务

        :param request: Request instance for BindDeviceResource.
        :type request: :class:`tencentcloud.bh.v20230418.models.BindDeviceResourceRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.BindDeviceResourceResponse`

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


    def CreateAccessWhiteListRule(self, request):
        """添加访问白名单规则

        :param request: Request instance for CreateAccessWhiteListRule.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateAccessWhiteListRuleRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateAccessWhiteListRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessWhiteListRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessWhiteListRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAcl(self, request):
        """新建访问权限

        :param request: Request instance for CreateAcl.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateAclRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateAclResponse`

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
        """创建手工资产同步任务

        :param request: Request instance for CreateAssetSyncJob.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateAssetSyncJobRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateAssetSyncJobResponse`

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
        """创建修改密码任务

        :param request: Request instance for CreateChangePwdTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateChangePwdTaskResponse`

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
        """新建高危命令模板

        :param request: Request instance for CreateCmdTemplate.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateCmdTemplateRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateCmdTemplateResponse`

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
        """新建主机账号

        :param request: Request instance for CreateDeviceAccount.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateDeviceAccountRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateDeviceAccountResponse`

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
        """新建资产组

        :param request: Request instance for CreateDeviceGroup.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateDeviceGroupRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateDeviceGroupResponse`

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


    def CreateOperationTask(self, request):
        """创建运维任务

        :param request: Request instance for CreateOperationTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateOperationTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateOperationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOperationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOperationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResource(self, request):
        """创建堡垒机实例

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateResourceResponse`

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
        """新建用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateUserResponse`

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
        """新建用户组

        :param request: Request instance for CreateUserGroup.
        :type request: :class:`tencentcloud.bh.v20230418.models.CreateUserGroupRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.CreateUserGroupResponse`

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


    def DeleteAccessWhiteListRules(self, request):
        """删除访问白名单规则

        :param request: Request instance for DeleteAccessWhiteListRules.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteAccessWhiteListRulesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteAccessWhiteListRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccessWhiteListRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccessWhiteListRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAcls(self, request):
        """删除访问权限

        :param request: Request instance for DeleteAcls.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteAclsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteAclsResponse`

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
        """删除改密任务

        :param request: Request instance for DeleteChangePwdTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteChangePwdTaskResponse`

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
        """删除高危命令模板

        :param request: Request instance for DeleteCmdTemplates.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteCmdTemplatesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteCmdTemplatesResponse`

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
        """删除主机账号

        :param request: Request instance for DeleteDeviceAccounts.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteDeviceAccountsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteDeviceAccountsResponse`

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
        """删除资产组成员

        :param request: Request instance for DeleteDeviceGroupMembers.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteDeviceGroupMembersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteDeviceGroupMembersResponse`

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
        """删除资产组

        :param request: Request instance for DeleteDeviceGroups.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteDeviceGroupsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteDeviceGroupsResponse`

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
        """删除主机

        :param request: Request instance for DeleteDevices.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteDevicesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteDevicesResponse`

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


    def DeleteOperationTasks(self, request):
        """删除运维任务

        :param request: Request instance for DeleteOperationTasks.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteOperationTasksRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteOperationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOperationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOperationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserGroupMembers(self, request):
        """删除用户组成员

        :param request: Request instance for DeleteUserGroupMembers.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteUserGroupMembersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteUserGroupMembersResponse`

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
        """删除用户组

        :param request: Request instance for DeleteUserGroups.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteUserGroupsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteUserGroupsResponse`

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
        """删除用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeleteUsersResponse`

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
        """开通服务，初始化资源，只针对新购资源

        :param request: Request instance for DeployResource.
        :type request: :class:`tencentcloud.bh.v20230418.models.DeployResourceRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DeployResourceResponse`

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


    def DescribeAccessWhiteListRules(self, request):
        """查询访问白名单规则列表

        :param request: Request instance for DescribeAccessWhiteListRules.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeAccessWhiteListRulesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeAccessWhiteListRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessWhiteListRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessWhiteListRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAcls(self, request):
        """查询访问权限列表

        :param request: Request instance for DescribeAcls.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeAclsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeAclsResponse`

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
        """查询资产同步状态

        :param request: Request instance for DescribeAssetSyncStatus.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeAssetSyncStatusRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeAssetSyncStatusResponse`

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
        """查询改密任务列表

        :param request: Request instance for DescribeChangePwdTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeChangePwdTaskResponse`

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
        """查询改密任务详情

        :param request: Request instance for DescribeChangePwdTaskDetail.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeChangePwdTaskDetailRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeChangePwdTaskDetailResponse`

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
        """查询命令模板列表

        :param request: Request instance for DescribeCmdTemplates.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeCmdTemplatesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeCmdTemplatesResponse`

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


    def DescribeDeviceAccounts(self, request):
        """查询主机账号列表

        :param request: Request instance for DescribeDeviceAccounts.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeDeviceAccountsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeDeviceAccountsResponse`

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
        """查询资产组成员列表

        :param request: Request instance for DescribeDeviceGroupMembers.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeDeviceGroupMembersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeDeviceGroupMembersResponse`

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
        """查询资产组列表

        :param request: Request instance for DescribeDeviceGroups.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeDeviceGroupsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeDeviceGroupsResponse`

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
        """查询资产列表

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeDevicesResponse`

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
        """查询网络域

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeDomainsResponse`

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
        """查询登录日志

        :param request: Request instance for DescribeLoginEvent.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeLoginEventRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeLoginEventResponse`

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
        """查询操作日志

        :param request: Request instance for DescribeOperationEvent.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeOperationEventRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeOperationEventResponse`

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


    def DescribeOperationTask(self, request):
        """获取运维任务列表

        :param request: Request instance for DescribeOperationTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeOperationTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeOperationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResources(self, request):
        """查询用户购买的堡垒机服务信息，包括资源ID、授权点数、VPC、过期时间等。

        :param request: Request instance for DescribeResources.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeResourcesRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeResourcesResponse`

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
        """查询用户组成员列表

        :param request: Request instance for DescribeUserGroupMembers.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeUserGroupMembersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeUserGroupMembersResponse`

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
        """查询用户组列表

        :param request: Request instance for DescribeUserGroups.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeUserGroupsRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeUserGroupsResponse`

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
        """查询用户列表

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.bh.v20230418.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.DescribeUsersResponse`

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
        """导入外部资产信息

        :param request: Request instance for ImportExternalDevice.
        :type request: :class:`tencentcloud.bh.v20230418.models.ImportExternalDeviceRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ImportExternalDeviceResponse`

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
        """修改访问权限

        :param request: Request instance for ModifyAcl.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyAclRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyAclResponse`

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
        """更新修改密码任务

        :param request: Request instance for ModifyChangePwdTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyChangePwdTaskResponse`

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
        """修改高危命令模板

        :param request: Request instance for ModifyCmdTemplate.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyCmdTemplateRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyCmdTemplateResponse`

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
        """修改资产信息

        :param request: Request instance for ModifyDevice.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyDeviceResponse`

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
        """修改资产组

        :param request: Request instance for ModifyDeviceGroup.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyDeviceGroupRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyDeviceGroupResponse`

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
        """设置OAuth认证参数

        :param request: Request instance for ModifyOAuthSetting.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyOAuthSettingRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyOAuthSettingResponse`

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


    def ModifyOperationTask(self, request):
        """修改运维任务

        :param request: Request instance for ModifyOperationTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyOperationTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyOperationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOperationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOperationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResource(self, request):
        """资源变配

        :param request: Request instance for ModifyResource.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyResourceRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyResourceResponse`

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
        """修改用户信息

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyUserResponse`

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
        """修改用户组

        :param request: Request instance for ModifyUserGroup.
        :type request: :class:`tencentcloud.bh.v20230418.models.ModifyUserGroupRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ModifyUserGroupResponse`

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
        """清除设备账号绑定密码

        :param request: Request instance for ResetDeviceAccountPassword.
        :type request: :class:`tencentcloud.bh.v20230418.models.ResetDeviceAccountPasswordRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ResetDeviceAccountPasswordResponse`

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
        """清除设备账号绑定的密钥

        :param request: Request instance for ResetDeviceAccountPrivateKey.
        :type request: :class:`tencentcloud.bh.v20230418.models.ResetDeviceAccountPrivateKeyRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ResetDeviceAccountPrivateKeyResponse`

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
        """重置用户

        :param request: Request instance for ResetUser.
        :type request: :class:`tencentcloud.bh.v20230418.models.ResetUserRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.ResetUserResponse`

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
        """执行改密任务

        :param request: Request instance for RunChangePwdTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.RunChangePwdTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.RunChangePwdTaskResponse`

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


    def RunOperationTask(self, request):
        """执行运维任务

        :param request: Request instance for RunOperationTask.
        :type request: :class:`tencentcloud.bh.v20230418.models.RunOperationTaskRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.RunOperationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunOperationTask", params, headers=headers)
            response = json.loads(body)
            model = models.RunOperationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchAuditLog(self, request):
        """搜索审计日志

        :param request: Request instance for SearchAuditLog.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchAuditLogRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchAuditLogResponse`

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
        """命令执行检索

        :param request: Request instance for SearchCommand.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchCommandRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchCommandResponse`

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
        """根据会话Id搜索Command

        :param request: Request instance for SearchCommandBySid.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchCommandBySidRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchCommandBySidResponse`

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
        """文件传输检索

        :param request: Request instance for SearchFile.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchFileRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchFileResponse`

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
        """搜索文件传输会话下文件操作列表

        :param request: Request instance for SearchFileBySid.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchFileBySidRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchFileBySidResponse`

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
        """搜索会话

        :param request: Request instance for SearchSession.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchSessionRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchSessionResponse`

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
        """命令检索

        :param request: Request instance for SearchSessionCommand.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchSessionCommandRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchSessionCommandResponse`

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


    def SearchSubtaskResultById(self, request):
        """查询运维子任务执行结果

        :param request: Request instance for SearchSubtaskResultById.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchSubtaskResultByIdRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchSubtaskResultByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchSubtaskResultById", params, headers=headers)
            response = json.loads(body)
            model = models.SearchSubtaskResultByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchTaskResult(self, request):
        """搜索运维任务执行结果

        :param request: Request instance for SearchTaskResult.
        :type request: :class:`tencentcloud.bh.v20230418.models.SearchTaskResultRequest`
        :rtype: :class:`tencentcloud.bh.v20230418.models.SearchTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.SearchTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))