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
from tencentcloud.smh.v20210712 import models


class SmhClient(AbstractClient):
    _apiVersion = '2021-07-12'
    _endpoint = 'smh.tencentcloudapi.com'
    _service = 'smh'


    def CreateLibrary(self, request):
        """创建 PaaS 服务媒体库

        :param request: Request instance for CreateLibrary.
        :type request: :class:`tencentcloud.smh.v20210712.models.CreateLibraryRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.CreateLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """新建用户。

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.smh.v20210712.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.CreateUserResponse`

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


    def CreateUserLifecycle(self, request):
        """设置用户生命周期。如果指定的用户已经设置了生命周期，重复调用此接口将覆盖已有的设置。也可用于清除指定用户的生命周期。

        :param request: Request instance for CreateUserLifecycle.
        :type request: :class:`tencentcloud.smh.v20210712.models.CreateUserLifecycleRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.CreateUserLifecycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserLifecycle", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserLifecycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLibrary(self, request):
        """删除 PaaS 服务媒体库

        :param request: Request instance for DeleteLibrary.
        :type request: :class:`tencentcloud.smh.v20210712.models.DeleteLibraryRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DeleteLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """一次删除多个用户。

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.smh.v20210712.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DeleteUserResponse`

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


    def DescribeLibraries(self, request):
        """查询 PaaS 服务媒体库列表

        :param request: Request instance for DescribeLibraries.
        :type request: :class:`tencentcloud.smh.v20210712.models.DescribeLibrariesRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DescribeLibrariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLibraries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLibrariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLibrarySecret(self, request):
        """查询 PaaS 服务媒体库密钥

        :param request: Request instance for DescribeLibrarySecret.
        :type request: :class:`tencentcloud.smh.v20210712.models.DescribeLibrarySecretRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DescribeLibrarySecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLibrarySecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLibrarySecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfficialInstances(self, request):
        """查询官方云盘实例

        :param request: Request instance for DescribeOfficialInstances.
        :type request: :class:`tencentcloud.smh.v20210712.models.DescribeOfficialInstancesRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DescribeOfficialInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfficialInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfficialInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfficialOverview(self, request):
        """查询官方云盘实例概览数据

        :param request: Request instance for DescribeOfficialOverview.
        :type request: :class:`tencentcloud.smh.v20210712.models.DescribeOfficialOverviewRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DescribeOfficialOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfficialOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfficialOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrafficPackages(self, request):
        """查询流量资源包

        :param request: Request instance for DescribeTrafficPackages.
        :type request: :class:`tencentcloud.smh.v20210712.models.DescribeTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DescribeTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserLifecycle(self, request):
        """查询用户生命周期。

        :param request: Request instance for DescribeUserLifecycle.
        :type request: :class:`tencentcloud.smh.v20210712.models.DescribeUserLifecycleRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.DescribeUserLifecycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserLifecycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserLifecycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLibrary(self, request):
        """修改 PaaS 服务媒体库配置项

        :param request: Request instance for ModifyLibrary.
        :type request: :class:`tencentcloud.smh.v20210712.models.ModifyLibraryRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.ModifyLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        """更新用户信息。

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.smh.v20210712.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.ModifyUserResponse`

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


    def SendSmsCode(self, request):
        """发送用于换绑官方云盘实例的超级管理员账号的短信验证码

        :param request: Request instance for SendSmsCode.
        :type request: :class:`tencentcloud.smh.v20210712.models.SendSmsCodeRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.SendSmsCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendSmsCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendSmsCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifySmsCode(self, request):
        """验证短信验证码以换绑官方云盘实例的超级管理员账号

        :param request: Request instance for VerifySmsCode.
        :type request: :class:`tencentcloud.smh.v20210712.models.VerifySmsCodeRequest`
        :rtype: :class:`tencentcloud.smh.v20210712.models.VerifySmsCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifySmsCode", params, headers=headers)
            response = json.loads(body)
            model = models.VerifySmsCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))