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
from tencentcloud.ioa.v20220601 import models


class IoaClient(AbstractClient):
    _apiVersion = '2022-06-01'
    _endpoint = 'ioa.tencentcloudapi.com'
    _service = 'ioa'


    def CreateDLPFileDetectTask(self, request):
        r"""创建文件鉴定任务，私有化调用path为：capi/DlpOpenApi/CreateDLPFileDetectTask

        :param request: Request instance for CreateDLPFileDetectTask.
        :type request: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectTaskRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDLPFileDetectTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDLPFileDetectTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDLPFileDetectionTask(self, request):
        r"""提交送检任务

        :param request: Request instance for CreateDLPFileDetectionTask.
        :type request: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectionTaskRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectionTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDLPFileDetectionTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDLPFileDetectionTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceTask(self, request):
        r"""创建获取终端进程网络服务信息任务，私有化调用path为：capi/Assets/Device/DescribeDeviceInfo

        :param request: Request instance for CreateDeviceTask.
        :type request: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceTaskRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeviceVirtualGroup(self, request):
        r"""创建终端自定义分组，私有化调用path为：/capi/Assets/Device/CreateDeviceVirtualGroup

        :param request: Request instance for CreateDeviceVirtualGroup.
        :type request: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceVirtualGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceVirtualGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivilegeCode(self, request):
        r"""生成特权码，私有化调用path为：capi/Assets/Device/CreatePrivilegeCode，生成的特权码、卸载码，仅对该设备当天有效

        :param request: Request instance for CreatePrivilegeCode.
        :type request: :class:`tencentcloud.ioa.v20220601.models.CreatePrivilegeCodeRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreatePrivilegeCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivilegeCode", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivilegeCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountGroups(self, request):
        r"""以分页的方式查询账号分组列表，私有化调用path为：/capi/Assets/DescribeAccountGroups

        :param request: Request instance for DescribeAccountGroups.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggrSoftCategorySoftList(self, request):
        r"""聚合的分类软件列表

        :param request: Request instance for DescribeAggrSoftCategorySoftList.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftCategorySoftListRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftCategorySoftListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggrSoftCategorySoftList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggrSoftCategorySoftListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggrSoftDetail(self, request):
        r"""聚合的软件详情

        :param request: Request instance for DescribeAggrSoftDetail.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDetailRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggrSoftDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggrSoftDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggrSoftDeviceList(self, request):
        r"""聚合软件的已安装终端列表

        :param request: Request instance for DescribeAggrSoftDeviceList.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDeviceListRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggrSoftDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggrSoftDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLPEdgeNodeGroups(self, request):
        r"""查询边缘节点分组，私有化调用path为：capi/Connectors/DescribeDLPEdgeNodeGroups

        :param request: Request instance for DescribeDLPEdgeNodeGroups.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodeGroupsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodeGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLPEdgeNodeGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLPEdgeNodeGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLPEdgeNodes(self, request):
        r"""查询边缘节点列表，私有化调用path为：capi/DlpOpenApi/DescribeDLPEdgeNodes

        :param request: Request instance for DescribeDLPEdgeNodes.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodesRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLPEdgeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLPEdgeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLPFileDetectResult(self, request):
        r"""webservice查询文件检测结果

        :param request: Request instance for DescribeDLPFileDetectResult.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectResultRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLPFileDetectResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLPFileDetectResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLPFileDetectTaskResult(self, request):
        r"""查询文件鉴定任务结果

        :param request: Request instance for DescribeDLPFileDetectTaskResult.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectTaskResultRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLPFileDetectTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLPFileDetectTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceChildGroups(self, request):
        r"""查询设备组子分组详情，私有化调用path为：capi/Assets/Device/DescribeDeviceChildGroups

        :param request: Request instance for DescribeDeviceChildGroups.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceChildGroupsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceChildGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceChildGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceChildGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceDetailList(self, request):
        r"""基于软件查看终端详情列表,私有化调用path为：capi/Software/DescribeDeviceDetailList

        :param request: Request instance for DescribeDeviceDetailList.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceDetailListRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceHardwareInfoList(self, request):
        r"""查询满足条件的查询终端硬件信息列表，私有化调用path为：/capi/Assets/Device/DescribeDeviceHardwareInfoList

        :param request: Request instance for DescribeDeviceHardwareInfoList.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceHardwareInfoListRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceHardwareInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceHardwareInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceHardwareInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceInfo(self, request):
        r"""获取终端进程网络服务信息，私有化调用path为：capi/Assets/Device/DescribeDeviceInfo

        :param request: Request instance for DescribeDeviceInfo.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceInfoRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceVirtualGroups(self, request):
        r"""查询终端自定义分组列表，私有化调用path为：/capi/Assets/Device/DescribeDeviceVirtualGroups

        :param request: Request instance for DescribeDeviceVirtualGroups.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceVirtualGroupsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceVirtualGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceVirtualGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceVirtualGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevices(self, request):
        r"""查询满足条件的终端数据详情，私有化调用path为：/capi/Assets/Device/DescribeDevices

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLocalAccounts(self, request):
        r"""获取账号列表，支持分页，模糊搜索，私有化调用path为：/capi/Assets/Account/DescribeLocalAccounts

        :param request: Request instance for DescribeLocalAccounts.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLocalAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLocalAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRootAccountGroup(self, request):
        r"""查询账号根分组详情。对应“用户与授权管理”里内置不可见的全网根账号组，所有新建的目录，都挂在该全网根账号组下。

        :param request: Request instance for DescribeRootAccountGroup.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeRootAccountGroupRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeRootAccountGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRootAccountGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRootAccountGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSoftCensusListByDevice(self, request):
        r"""查看终端树下的软件列表,私有化调用path为：capi/Software/DescribeSoftCensusListByDevice

        :param request: Request instance for DescribeSoftCensusListByDevice.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftCensusListByDeviceRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftCensusListByDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSoftCensusListByDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSoftCensusListByDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSoftwareInformation(self, request):
        r"""查看指定终端的软件详情列表,私有化调用path为：capi/Software/DescribeSoftwareInformation

        :param request: Request instance for DescribeSoftwareInformation.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftwareInformationRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftwareInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSoftwareInformation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSoftwareInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirtualDevices(self, request):
        r"""展示自定义分组终端列表，私有化调用path为：/capi/Assets/DescribeVirtualDevices

        :param request: Request instance for DescribeVirtualDevices.
        :type request: :class:`tencentcloud.ioa.v20220601.models.DescribeVirtualDevicesRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeVirtualDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirtualDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirtualDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportDeviceDownloadTask(self, request):
        r"""创建终端导出任务，私有化调用path为：capi/Assets/Device/ExportDeviceDownloadTask

        :param request: Request instance for ExportDeviceDownloadTask.
        :type request: :class:`tencentcloud.ioa.v20220601.models.ExportDeviceDownloadTaskRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.ExportDeviceDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportDeviceDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.ExportDeviceDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportSoftwareInformationList(self, request):
        r"""导出基于指定终端查看软件信息详情列表查询,私有化调用path为：capi/Software/ExportSoftwareInformationList

        :param request: Request instance for ExportSoftwareInformationList.
        :type request: :class:`tencentcloud.ioa.v20220601.models.ExportSoftwareInformationListRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.ExportSoftwareInformationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportSoftwareInformationList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportSoftwareInformationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirtualDeviceGroups(self, request):
        r"""终端自定义分组增减终端，私有化调用path为：/capi/Assets/Device/ModifyVirtualDeviceGroups

        :param request: Request instance for ModifyVirtualDeviceGroups.
        :type request: :class:`tencentcloud.ioa.v20220601.models.ModifyVirtualDeviceGroupsRequest`
        :rtype: :class:`tencentcloud.ioa.v20220601.models.ModifyVirtualDeviceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirtualDeviceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirtualDeviceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))