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
from tencentcloud.ioa.v20220601 import models
from typing import Dict


class IoaClient(AbstractClient):
    _apiVersion = '2022-06-01'
    _endpoint = 'ioa.tencentcloudapi.com'
    _service = 'ioa'

    async def CreateDLPFileDetectTask(
            self,
            request: models.CreateDLPFileDetectTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDLPFileDetectTaskResponse:
        """
        创建文件鉴定任务，私有化调用path为：capi/DlpOpenApi/CreateDLPFileDetectTask
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDLPFileDetectTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDLPFileDetectTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDLPFileDetectionTask(
            self,
            request: models.CreateDLPFileDetectionTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDLPFileDetectionTaskResponse:
        """
        提交送检任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDLPFileDetectionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDLPFileDetectionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceTask(
            self,
            request: models.CreateDeviceTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceTaskResponse:
        """
        创建获取终端进程网络服务信息任务，私有化调用path为：capi/Assets/Device/DescribeDeviceInfo
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceVirtualGroup(
            self,
            request: models.CreateDeviceVirtualGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceVirtualGroupResponse:
        """
        创建终端自定义分组，私有化调用path为：/capi/Assets/Device/CreateDeviceVirtualGroup
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceVirtualGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceVirtualGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivilegeCode(
            self,
            request: models.CreatePrivilegeCodeRequest,
            opts: Dict = None,
    ) -> models.CreatePrivilegeCodeResponse:
        """
        生成特权码，私有化调用path为：capi/Assets/Device/CreatePrivilegeCode，生成的特权码、卸载码，仅对该设备当天有效
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivilegeCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivilegeCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountGroups(
            self,
            request: models.DescribeAccountGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountGroupsResponse:
        """
        以分页的方式查询账号分组列表，私有化调用path为：/capi/Assets/DescribeAccountGroups
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggrSoftCategorySoftList(
            self,
            request: models.DescribeAggrSoftCategorySoftListRequest,
            opts: Dict = None,
    ) -> models.DescribeAggrSoftCategorySoftListResponse:
        """
        聚合的分类软件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggrSoftCategorySoftList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggrSoftCategorySoftListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggrSoftDetail(
            self,
            request: models.DescribeAggrSoftDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAggrSoftDetailResponse:
        """
        聚合的软件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggrSoftDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggrSoftDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggrSoftDeviceList(
            self,
            request: models.DescribeAggrSoftDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAggrSoftDeviceListResponse:
        """
        聚合软件的已安装终端列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggrSoftDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggrSoftDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLPEdgeNodeGroups(
            self,
            request: models.DescribeDLPEdgeNodeGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDLPEdgeNodeGroupsResponse:
        """
        查询边缘节点分组，私有化调用path为：capi/Connectors/DescribeDLPEdgeNodeGroups
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLPEdgeNodeGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLPEdgeNodeGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLPEdgeNodes(
            self,
            request: models.DescribeDLPEdgeNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeDLPEdgeNodesResponse:
        """
        查询边缘节点列表，私有化调用path为：capi/DlpOpenApi/DescribeDLPEdgeNodes
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLPEdgeNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLPEdgeNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLPFileDetectResult(
            self,
            request: models.DescribeDLPFileDetectResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDLPFileDetectResultResponse:
        """
        webservice查询文件检测结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLPFileDetectResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLPFileDetectResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLPFileDetectTaskResult(
            self,
            request: models.DescribeDLPFileDetectTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDLPFileDetectTaskResultResponse:
        """
        查询文件鉴定任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLPFileDetectTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLPFileDetectTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceChildGroups(
            self,
            request: models.DescribeDeviceChildGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceChildGroupsResponse:
        """
        查询设备组子分组详情，私有化调用path为：capi/Assets/Device/DescribeDeviceChildGroups
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceChildGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceChildGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceDetailList(
            self,
            request: models.DescribeDeviceDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceDetailListResponse:
        """
        基于软件查看终端详情列表,私有化调用path为：capi/Software/DescribeDeviceDetailList
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceHardwareInfoList(
            self,
            request: models.DescribeDeviceHardwareInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceHardwareInfoListResponse:
        """
        查询满足条件的查询终端硬件信息列表，私有化调用path为：/capi/Assets/Device/DescribeDeviceHardwareInfoList
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceHardwareInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceHardwareInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceInfo(
            self,
            request: models.DescribeDeviceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceInfoResponse:
        """
        获取终端进程网络服务信息，私有化调用path为：capi/Assets/Device/DescribeDeviceInfo
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceVirtualGroups(
            self,
            request: models.DescribeDeviceVirtualGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceVirtualGroupsResponse:
        """
        查询终端自定义分组列表，私有化调用path为：/capi/Assets/Device/DescribeDeviceVirtualGroups
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceVirtualGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceVirtualGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        查询满足条件的终端数据详情，私有化调用path为：/capi/Assets/Device/DescribeDevices
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLocalAccounts(
            self,
            request: models.DescribeLocalAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeLocalAccountsResponse:
        """
        获取账号列表，支持分页，模糊搜索，私有化调用path为：/capi/Assets/Account/DescribeLocalAccounts
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLocalAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLocalAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRootAccountGroup(
            self,
            request: models.DescribeRootAccountGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeRootAccountGroupResponse:
        """
        查询账号根分组详情。对应“用户与授权管理”里内置不可见的全网根账号组，所有新建的目录，都挂在该全网根账号组下。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRootAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRootAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSoftCensusListByDevice(
            self,
            request: models.DescribeSoftCensusListByDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeSoftCensusListByDeviceResponse:
        """
        查看终端树下的软件列表,私有化调用path为：capi/Software/DescribeSoftCensusListByDevice
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSoftCensusListByDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSoftCensusListByDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSoftwareInformation(
            self,
            request: models.DescribeSoftwareInformationRequest,
            opts: Dict = None,
    ) -> models.DescribeSoftwareInformationResponse:
        """
        查看指定终端的软件详情列表,私有化调用path为：capi/Software/DescribeSoftwareInformation
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSoftwareInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSoftwareInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirtualDevices(
            self,
            request: models.DescribeVirtualDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeVirtualDevicesResponse:
        """
        展示自定义分组终端列表，私有化调用path为：/capi/Assets/DescribeVirtualDevices
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirtualDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirtualDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportDeviceDownloadTask(
            self,
            request: models.ExportDeviceDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.ExportDeviceDownloadTaskResponse:
        """
        创建终端导出任务，私有化调用path为：capi/Assets/Device/ExportDeviceDownloadTask
        """
        
        kwargs = {}
        kwargs["action"] = "ExportDeviceDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportDeviceDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportSoftwareInformationList(
            self,
            request: models.ExportSoftwareInformationListRequest,
            opts: Dict = None,
    ) -> models.ExportSoftwareInformationListResponse:
        """
        导出基于指定终端查看软件信息详情列表查询,私有化调用path为：capi/Software/ExportSoftwareInformationList
        """
        
        kwargs = {}
        kwargs["action"] = "ExportSoftwareInformationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportSoftwareInformationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirtualDeviceGroups(
            self,
            request: models.ModifyVirtualDeviceGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyVirtualDeviceGroupsResponse:
        """
        终端自定义分组增减终端，私有化调用path为：/capi/Assets/Device/ModifyVirtualDeviceGroups
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirtualDeviceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirtualDeviceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)