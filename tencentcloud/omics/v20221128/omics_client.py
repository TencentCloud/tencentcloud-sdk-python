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


    def CreateEnvironment(self, request):
        """创建组学平台计算环境。

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.omics.v20221128.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnvironment(self, request):
        """删除环境。

        :param request: Request instance for DeleteEnvironment.
        :type request: :class:`tencentcloud.omics.v20221128.models.DeleteEnvironmentRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DeleteEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        """查询环境列表。

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        """查询表格。

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTablesRows(self, request):
        """查询表格行数据。

        :param request: Request instance for DescribeTablesRows.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeTablesRowsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeTablesRowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablesRows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesRowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRunMetadataFile(self, request):
        """查询任务详情文件。

        :param request: Request instance for GetRunMetadataFile.
        :type request: :class:`tencentcloud.omics.v20221128.models.GetRunMetadataFileRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.GetRunMetadataFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRunMetadataFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetRunMetadataFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRuns(self, request):
        """重试任务。

        :param request: Request instance for RetryRuns.
        :type request: :class:`tencentcloud.omics.v20221128.models.RetryRunsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.RetryRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRuns", params, headers=headers)
            response = json.loads(body)
            model = models.RetryRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunWorkflow(self, request):
        """运行工作流。

        :param request: Request instance for RunWorkflow.
        :type request: :class:`tencentcloud.omics.v20221128.models.RunWorkflowRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.RunWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateRunGroup(self, request):
        """终止任务批次。

        :param request: Request instance for TerminateRunGroup.
        :type request: :class:`tencentcloud.omics.v20221128.models.TerminateRunGroupRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.TerminateRunGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateRunGroup", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateRunGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))