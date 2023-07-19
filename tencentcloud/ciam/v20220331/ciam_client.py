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
from tencentcloud.ciam.v20220331 import models


class CiamClient(AbstractClient):
    _apiVersion = '2022-03-31'
    _endpoint = 'ciam.tencentcloudapi.com'
    _service = 'ciam'


    def CreateApiImportUserJob(self, request):
        """新建接口导入用户任务

        :param request: Request instance for CreateApiImportUserJob.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateApiImportUserJobRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateApiImportUserJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiImportUserJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiImportUserJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileExportUserJob(self, request):
        """新建文件导出用户任务

        :param request: Request instance for CreateFileExportUserJob.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateFileExportUserJobRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateFileExportUserJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileExportUserJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileExportUserJobResponse()
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
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateUserResponse`

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
        """创建用户组

        :param request: Request instance for CreateUserGroup.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateUserGroupRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateUserGroupResponse`

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


    def CreateUserStore(self, request):
        """创建用户目录

        :param request: Request instance for CreateUserStore.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateUserStoreRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateUserStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserStore", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserGroups(self, request):
        """批量删除用户组

        :param request: Request instance for DeleteUserGroups.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DeleteUserGroupsRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DeleteUserGroupsResponse`

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


    def DeleteUserStore(self, request):
        """删除用户目录

        :param request: Request instance for DeleteUserStore.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DeleteUserStoreRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DeleteUserStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserStore", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsers(self, request):
        """批量删除用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DeleteUsersResponse`

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


    def DescribeUser(self, request):
        """多条件查询用户信息

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserById(self, request):
        """根据ID查询用户信息

        :param request: Request instance for DescribeUserById.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DescribeUserByIdRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DescribeUserByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LinkAccount(self, request):
        """账号融合

        :param request: Request instance for LinkAccount.
        :type request: :class:`tencentcloud.ciam.v20220331.models.LinkAccountRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.LinkAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LinkAccount", params, headers=headers)
            response = json.loads(body)
            model = models.LinkAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJobs(self, request):
        """查询任务详情

        :param request: Request instance for ListJobs.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListJobsRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJobs", params, headers=headers)
            response = json.loads(body)
            model = models.ListJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLogMessageByCondition(self, request):
        """查询日志信息

        :param request: Request instance for ListLogMessageByCondition.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListLogMessageByConditionRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListLogMessageByConditionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLogMessageByCondition", params, headers=headers)
            response = json.loads(body)
            model = models.ListLogMessageByConditionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUser(self, request):
        """查询用户列表

        :param request: Request instance for ListUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUser", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUserByProperty(self, request):
        """根据属性查询用户列表

        :param request: Request instance for ListUserByProperty.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListUserByPropertyRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListUserByPropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserByProperty", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserByPropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUserGroups(self, request):
        """查询用户组列表

        :param request: Request instance for ListUserGroups.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListUserGroupsRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListUserGroupsResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUserStore(self, request):
        """查询用户目录列表

        :param request: Request instance for ListUserStore.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListUserStoreRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListUserStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserStore", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetPassword(self, request):
        """重置用户密码

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetPassword(self, request):
        """设置用户密码

        :param request: Request instance for SetPassword.
        :type request: :class:`tencentcloud.ciam.v20220331.models.SetPasswordRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.SetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.SetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUser(self, request):
        """更新用户

        :param request: Request instance for UpdateUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.UpdateUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UpdateUserResponse`

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


    def UpdateUserGroup(self, request):
        """更新用户组

        :param request: Request instance for UpdateUserGroup.
        :type request: :class:`tencentcloud.ciam.v20220331.models.UpdateUserGroupRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UpdateUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserStatus(self, request):
        """更新用户状态

        :param request: Request instance for UpdateUserStatus.
        :type request: :class:`tencentcloud.ciam.v20220331.models.UpdateUserStatusRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UpdateUserStatusResponse`

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


    def UpdateUserStore(self, request):
        """更新用户目录

        :param request: Request instance for UpdateUserStore.
        :type request: :class:`tencentcloud.ciam.v20220331.models.UpdateUserStoreRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UpdateUserStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserStore", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))