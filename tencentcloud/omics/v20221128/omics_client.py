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
from tencentcloud.omics.v20221128 import models


class OmicsClient(AbstractClient):
    _apiVersion = '2022-11-28'
    _endpoint = 'omics.tencentcloudapi.com'
    _service = 'omics'


    def CreateEnvironment(self, request):
        r"""创建组学平台计算环境。

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


    def CreateVolume(self, request):
        r"""创建缓存卷。

        :param request: Request instance for CreateVolume.
        :type request: :class:`tencentcloud.omics.v20221128.models.CreateVolumeRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.CreateVolumeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVolume", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVolumeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnvironment(self, request):
        r"""删除环境。

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


    def DeleteVolume(self, request):
        r"""删除缓存卷。

        :param request: Request instance for DeleteVolume.
        :type request: :class:`tencentcloud.omics.v20221128.models.DeleteVolumeRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DeleteVolumeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVolume", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVolumeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVolumeData(self, request):
        r"""删除缓存卷数据。

        :param request: Request instance for DeleteVolumeData.
        :type request: :class:`tencentcloud.omics.v20221128.models.DeleteVolumeDataRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DeleteVolumeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVolumeData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVolumeDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationVersions(self, request):
        r"""查询应用版本列表

        :param request: Request instance for DescribeApplicationVersions.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeApplicationVersionsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeApplicationVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplications(self, request):
        r"""查询项目应用列表

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        r"""查询环境列表。

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


    def DescribeHPCClusters(self, request):
        r"""查询HPC集群列表。

        :param request: Request instance for DescribeHPCClusters.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeHPCClustersRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeHPCClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHPCClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHPCClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHPCNodes(self, request):
        r"""查询HPC节点列表。

        :param request: Request instance for DescribeHPCNodes.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeHPCNodesRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeHPCNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHPCNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHPCNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInputTemplates(self, request):
        r"""查询运行参数模板列表

        :param request: Request instance for DescribeInputTemplates.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeInputTemplatesRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeInputTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInputTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInputTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        r"""查询项目列表

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicApplications(self, request):
        r"""查询公共应用列表。

        :param request: Request instance for DescribePublicApplications.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribePublicApplicationsRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribePublicApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRunGroups(self, request):
        r"""查询任务批次列表。

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
        r"""查询任务列表。

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
        r"""查询表格。

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
        r"""查询表格行数据。

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


    def DescribeVolumes(self, request):
        r"""查询缓存卷列表。

        :param request: Request instance for DescribeVolumes.
        :type request: :class:`tencentcloud.omics.v20221128.models.DescribeVolumesRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.DescribeVolumesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVolumes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVolumesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInputTemplateFile(self, request):
        r"""查询运行参数模板内容

        :param request: Request instance for GetInputTemplateFile.
        :type request: :class:`tencentcloud.omics.v20221128.models.GetInputTemplateFileRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.GetInputTemplateFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInputTemplateFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetInputTemplateFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRunCalls(self, request):
        r"""查询作业详情。

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


    def GetRunJobLog(self, request):
        r"""获取任务详情文件。

        :param request: Request instance for GetRunJobLog.
        :type request: :class:`tencentcloud.omics.v20221128.models.GetRunJobLogRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.GetRunJobLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRunJobLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetRunJobLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRunMetadataFile(self, request):
        r"""获取任务详情文件。

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
        r"""查询任务详情。

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


    def ImportCommonApplication(self, request):
        r"""导入公共应用到项目

        :param request: Request instance for ImportCommonApplication.
        :type request: :class:`tencentcloud.omics.v20221128.models.ImportCommonApplicationRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.ImportCommonApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportCommonApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ImportCommonApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportTableFile(self, request):
        r"""导入表格文件。

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


    def ModifyVolume(self, request):
        r"""修改缓存卷。

        :param request: Request instance for ModifyVolume.
        :type request: :class:`tencentcloud.omics.v20221128.models.ModifyVolumeRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.ModifyVolumeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVolume", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVolumeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootHPCNodes(self, request):
        r"""重启HPC节点

        :param request: Request instance for RebootHPCNodes.
        :type request: :class:`tencentcloud.omics.v20221128.models.RebootHPCNodesRequest`
        :rtype: :class:`tencentcloud.omics.v20221128.models.RebootHPCNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootHPCNodes", params, headers=headers)
            response = json.loads(body)
            model = models.RebootHPCNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRuns(self, request):
        r"""重试任务。

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
        r"""运行应用。

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
        r"""运行工作流。

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
        r"""终止任务批次。

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