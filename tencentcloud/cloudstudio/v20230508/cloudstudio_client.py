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
from tencentcloud.cloudstudio.v20230508 import models


class CloudstudioClient(AbstractClient):
    _apiVersion = '2023-05-08'
    _endpoint = 'cloudstudio.tencentcloudapi.com'
    _service = 'cloudstudio'


    def CreateWorkspace(self, request):
        """创建工作空间

        :param request: Request instance for CreateWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.CreateWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.CreateWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkspaceToken(self, request):
        """创建工作空间临时访问凭证，重复调用会创建新的 Token，旧的 Token 将会自动失效

        :param request: Request instance for CreateWorkspaceToken.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.CreateWorkspaceTokenRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.CreateWorkspaceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfig(self, request):
        """获取用户配置

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImages(self, request):
        """获取基础镜像列表

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaces(self, request):
        """获取用户工作空间列表

        :param request: Request instance for DescribeWorkspaces.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.DescribeWorkspacesRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.DescribeWorkspacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkspace(self, request):
        """修改工作空间

        :param request: Request instance for ModifyWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.ModifyWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.ModifyWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWorkspace(self, request):
        """删除工作空间

        :param request: Request instance for RemoveWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.RemoveWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.RemoveWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunWorkspace(self, request):
        """运行空间

        :param request: Request instance for RunWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.RunWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.RunWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.RunWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopWorkspace(self, request):
        """停止运行空间

        :param request: Request instance for StopWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20230508.models.StopWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.StopWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.StopWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))