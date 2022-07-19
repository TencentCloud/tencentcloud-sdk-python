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
            if "Error" not in response["Response"]:
                model = models.CreateApiImportUserJobResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateFileExportUserJobResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeUserResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeUserByIdResponse()
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
            if "Error" not in response["Response"]:
                model = models.LinkAccountResponse()
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
            if "Error" not in response["Response"]:
                model = models.ListJobsResponse()
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
            if "Error" not in response["Response"]:
                model = models.ListLogMessageByConditionResponse()
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
            if "Error" not in response["Response"]:
                model = models.ListUserResponse()
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
            if "Error" not in response["Response"]:
                model = models.ListUserByPropertyResponse()
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
            if "Error" not in response["Response"]:
                model = models.ResetPasswordResponse()
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
            if "Error" not in response["Response"]:
                model = models.SetPasswordResponse()
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
            if "Error" not in response["Response"]:
                model = models.UpdateUserStatusResponse()
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