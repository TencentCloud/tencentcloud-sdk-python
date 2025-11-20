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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.omics.v20221128 import models
from typing import Dict


class OmicsClient(AbstractClient):
    _apiVersion = '2022-11-28'
    _endpoint = 'omics.tencentcloudapi.com'
    _service = 'omics'

    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        创建组学平台计算环境。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVolume(
            self,
            request: models.CreateVolumeRequest,
            opts: Dict = None,
    ) -> models.CreateVolumeResponse:
        """
        创建缓存卷。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVolumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironment(
            self,
            request: models.DeleteEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentResponse:
        """
        删除环境。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVolume(
            self,
            request: models.DeleteVolumeRequest,
            opts: Dict = None,
    ) -> models.DeleteVolumeResponse:
        """
        删除缓存卷。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVolumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVolumeData(
            self,
            request: models.DeleteVolumeDataRequest,
            opts: Dict = None,
    ) -> models.DeleteVolumeDataResponse:
        """
        删除缓存卷数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVolumeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVolumeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        查询环境列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRunGroups(
            self,
            request: models.DescribeRunGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeRunGroupsResponse:
        """
        查询任务批次列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRunGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRunGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuns(
            self,
            request: models.DescribeRunsRequest,
            opts: Dict = None,
    ) -> models.DescribeRunsResponse:
        """
        查询任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        查询表格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablesRows(
            self,
            request: models.DescribeTablesRowsRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesRowsResponse:
        """
        查询表格行数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablesRows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesRowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVolumes(
            self,
            request: models.DescribeVolumesRequest,
            opts: Dict = None,
    ) -> models.DescribeVolumesResponse:
        """
        查询缓存卷列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVolumes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVolumesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRunCalls(
            self,
            request: models.GetRunCallsRequest,
            opts: Dict = None,
    ) -> models.GetRunCallsResponse:
        """
        查询作业详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRunCalls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRunCallsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRunMetadataFile(
            self,
            request: models.GetRunMetadataFileRequest,
            opts: Dict = None,
    ) -> models.GetRunMetadataFileResponse:
        """
        获取任务详情文件。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRunMetadataFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRunMetadataFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRunStatus(
            self,
            request: models.GetRunStatusRequest,
            opts: Dict = None,
    ) -> models.GetRunStatusResponse:
        """
        查询任务详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRunStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRunStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportTableFile(
            self,
            request: models.ImportTableFileRequest,
            opts: Dict = None,
    ) -> models.ImportTableFileResponse:
        """
        导入表格文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportTableFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportTableFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVolume(
            self,
            request: models.ModifyVolumeRequest,
            opts: Dict = None,
    ) -> models.ModifyVolumeResponse:
        """
        修改缓存卷。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVolumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRuns(
            self,
            request: models.RetryRunsRequest,
            opts: Dict = None,
    ) -> models.RetryRunsResponse:
        """
        重试任务。
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunApplication(
            self,
            request: models.RunApplicationRequest,
            opts: Dict = None,
    ) -> models.RunApplicationResponse:
        """
        运行应用。
        """
        
        kwargs = {}
        kwargs["action"] = "RunApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunWorkflow(
            self,
            request: models.RunWorkflowRequest,
            opts: Dict = None,
    ) -> models.RunWorkflowResponse:
        """
        运行工作流。
        """
        
        kwargs = {}
        kwargs["action"] = "RunWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateRunGroup(
            self,
            request: models.TerminateRunGroupRequest,
            opts: Dict = None,
    ) -> models.TerminateRunGroupResponse:
        """
        终止任务批次。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateRunGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateRunGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)