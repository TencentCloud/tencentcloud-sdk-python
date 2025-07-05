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
from tencentcloud.msp.v20180319 import models


class MspClient(AbstractClient):
    _apiVersion = '2018-03-19'
    _endpoint = 'msp.tencentcloudapi.com'
    _service = 'msp'


    def DeregisterMigrationTask(self, request):
        """接口已经废弃不再使用

        取消注册迁移任务

        :param request: Request instance for DeregisterMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.DeregisterMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.DeregisterMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationTask(self, request):
        """获取指定迁移任务详情

        :param request: Request instance for DescribeMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.DescribeMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.DescribeMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListMigrationProject(self, request):
        """获取迁移项目名称列表

        :param request: Request instance for ListMigrationProject.
        :type request: :class:`tencentcloud.msp.v20180319.models.ListMigrationProjectRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ListMigrationProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListMigrationProject", params, headers=headers)
            response = json.loads(body)
            model = models.ListMigrationProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListMigrationTask(self, request):
        """获取迁移任务列表

        :param request: Request instance for ListMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.ListMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ListMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ListMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrationTaskBelongToProject(self, request):
        """更改迁移任务所属项目

        :param request: Request instance for ModifyMigrationTaskBelongToProject.
        :type request: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskBelongToProjectRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskBelongToProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrationTaskBelongToProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrationTaskBelongToProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrationTaskStatus(self, request):
        """更新迁移任务状态

        :param request: Request instance for ModifyMigrationTaskStatus.
        :type request: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskStatusRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrationTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrationTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterMigrationTask(self, request):
        """注册迁移任务

        :param request: Request instance for RegisterMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.RegisterMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.RegisterMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))