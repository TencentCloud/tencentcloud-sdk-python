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
from tencentcloud.goosefs.v20220519 import models


class GoosefsClient(AbstractClient):
    _apiVersion = '2022-05-19'
    _endpoint = 'goosefs.tencentcloudapi.com'
    _service = 'goosefs'


    def CreateDataRepositoryTask(self, request):
        """创建数据流通任务,包括从将文件系统的数据上传到存储桶下, 以及从存储桶下载到文件系统里。

        :param request: Request instance for CreateDataRepositoryTask.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.CreateDataRepositoryTaskRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.CreateDataRepositoryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataRepositoryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataRepositoryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterClientToken(self, request):
        """查询GooseFS集群客户端凭证

        :param request: Request instance for DescribeClusterClientToken.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterClientTokenRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterClientTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterClientToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterClientTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterRoleToken(self, request):
        """查询GooseFS集群角色凭证

        :param request: Request instance for DescribeClusterRoleToken.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRoleTokenRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRoleTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRoleToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRoleTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterRoles(self, request):
        """查询GooseFS集群角色

        :param request: Request instance for DescribeClusterRoles.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRolesRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataRepositoryTaskStatus(self, request):
        """获取数据流通任务实时状态，用作客户端控制

        :param request: Request instance for DescribeDataRepositoryTaskStatus.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeDataRepositoryTaskStatusRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeDataRepositoryTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataRepositoryTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataRepositoryTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))