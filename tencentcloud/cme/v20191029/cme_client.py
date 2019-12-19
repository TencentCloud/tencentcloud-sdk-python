# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.cme.v20191029 import models


class CmeClient(AbstractClient):
    _apiVersion = '2019-10-29'
    _endpoint = 'cme.tencentcloudapi.com'


    def CreateProject(self, request):
        """创建云剪的编辑项目，支持创建视频剪辑及直播剪辑两大类项目。

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
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


    def DeleteLoginStatus(self, request):
        """删除用户登录态，使用户登出云剪平台。

        :param request: Request instance for DeleteLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoginStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoginStatusResponse()
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


    def DeleteProject(self, request):
        """删除云剪编辑项目。

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
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


    def DescribeLoginStatus(self, request):
        """查询指定用户的登录态。

        :param request: Request instance for DescribeLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoginStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoginStatusResponse()
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


    def DescribeProjects(self, request):
        """支持根据多种条件过滤出项目列表。

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
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


    def DescribeTaskDetail(self, request):
        """获取任务详情信息，包含下面几个部分：
        <li>任务基础信息：包括任务状态、错误信息、创建时间等；</li>
        <li>导出项目输出信息：包括输出的素材 Id 等。</li>

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTasks(self, request):
        """支持各种条件筛选，返回对应的任务基础信息列表。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def ExportVideoEditProject(self, request):
        """导出视频编辑项目，支持指定输出的模板。

        :param request: Request instance for ExportVideoEditProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVideoEditProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVideoEditProjectResponse()
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


    def ImportMediaToProject(self, request):
        """将云点播中的媒资添加到素材库中，提供给后续的视频编辑。

        :param request: Request instance for ImportMediaToProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMediaToProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMediaToProjectResponse()
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


    def ModifyProject(self, request):
        """修改云剪编辑项目的信息。

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
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