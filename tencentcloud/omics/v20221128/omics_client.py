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
from tencentcloud.omics.v20221128 import models


class OmicsClient(AbstractClient):
    _apiVersion = '2022-11-28'
    _endpoint = 'omics.tencentcloudapi.com'
    _service = 'omics'


    def DescribeRunGroups(self, request):
        """查询任务批次列表。

        :param request: Request instance for DescribeRunGroups.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeRunGroupsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeRunGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRunGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRunGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuns(self, request):
        """查询任务列表。

        :param request: Request instance for DescribeRuns.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeRunsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRunCalls(self, request):
        """查询作业详情。

        :param request: Request instance for GetRunCalls.
        :type request: :class:`tencentcloud.omics.v20221128.models.GetRunCallsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.GetRunCallsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRunCalls", params, headers=headers)
            response = json.loads(body)
            model = models.GetRunCallsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRunStatus(self, request):
        """查询任务详情。

        :param request: Request instance for GetRunStatus.
        :type request: :class:`tencentcloud.omics.v20221128.models.GetRunStatusRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.GetRunStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRunStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetRunStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportTableFile(self, request):
        """导入表格文件。

        :param request: Request instance for ImportTableFile.
        :type request: :class:`tencentcloud.omics.v20221128.models.ImportTableFileRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.ImportTableFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportTableFile", params, headers=headers)
            response = json.loads(body)
            model = models.ImportTableFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunApplication(self, request):
        """运行应用。

        :param request: Request instance for RunApplication.
        :type request: :class:`tencentcloud.omics.v20221128.models.RunApplicationRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunApplication", params, headers=headers)
            response = json.loads(body)
            model = models.RunApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)