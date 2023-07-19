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
from tencentcloud.bm.v20180423 import models


class BmClient(AbstractClient):
    _apiVersion = '2018-04-23'
    _endpoint = 'bm.tencentcloudapi.com'
    _service = 'bm'


    def AttachCamRole(self, request):
        """服务器绑定CAM角色，该角色授权访问黑石物理服务器服务，为黑石物理服务器提供了访问资源的权限，如请求服务器的临时证书

        :param request: Request instance for AttachCamRole.
        :type request: :class:`tencentcloud.bm.v20180423.models.AttachCamRoleRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.AttachCamRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachCamRole", params, headers=headers)
            response = json.loads(body)
            model = models.AttachCamRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindPsaTag(self, request):
        """为预授权规则绑定标签

        :param request: Request instance for BindPsaTag.
        :type request: :class:`tencentcloud.bm.v20180423.models.BindPsaTagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.BindPsaTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindPsaTag", params, headers=headers)
            response = json.loads(body)
            model = models.BindPsaTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BuyDevices(self, request):
        """购买黑石物理机

        :param request: Request instance for BuyDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.BuyDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.BuyDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BuyDevices", params, headers=headers)
            response = json.loads(body)
            model = models.BuyDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomImage(self, request):
        """创建自定义镜像<br>
        每个AppId在每个可用区最多保留20个自定义镜像

        :param request: Request instance for CreateCustomImage.
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateCustomImageRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateCustomImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePsaRegulation(self, request):
        """创建预授权规则

        :param request: Request instance for CreatePsaRegulation.
        :type request: :class:`tencentcloud.bm.v20180423.models.CreatePsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreatePsaRegulationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePsaRegulation", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePsaRegulationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSpotDevice(self, request):
        """创建黑石竞价实例

        :param request: Request instance for CreateSpotDevice.
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateSpotDeviceRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateSpotDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSpotDevice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSpotDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserCmd(self, request):
        """创建自定义脚本

        :param request: Request instance for CreateUserCmd.
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateUserCmdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserCmd", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserCmdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomImages(self, request):
        """删除自定义镜像<br>
        正用于部署或重装中的镜像被删除后，镜像文件将保留一段时间，直到部署或重装结束

        :param request: Request instance for DeleteCustomImages.
        :type request: :class:`tencentcloud.bm.v20180423.models.DeleteCustomImagesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeleteCustomImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomImages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePsaRegulation(self, request):
        """删除预授权规则

        :param request: Request instance for DeletePsaRegulation.
        :type request: :class:`tencentcloud.bm.v20180423.models.DeletePsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeletePsaRegulationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePsaRegulation", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePsaRegulationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserCmds(self, request):
        """删除自定义脚本

        :param request: Request instance for DeleteUserCmds.
        :type request: :class:`tencentcloud.bm.v20180423.models.DeleteUserCmdsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeleteUserCmdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserCmds", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserCmdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomImageProcess(self, request):
        """查询自定义镜像制作进度

        :param request: Request instance for DescribeCustomImageProcess.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImageProcessRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImageProcessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomImageProcess", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomImageProcessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomImages(self, request):
        """查看自定义镜像列表

        :param request: Request instance for DescribeCustomImages.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImagesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceClass(self, request):
        """获取设备类型

        :param request: Request instance for DescribeDeviceClass.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceClass", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceClassPartition(self, request):
        """查询机型支持的RAID方式， 并返回系统盘的分区和逻辑盘的列表

        :param request: Request instance for DescribeDeviceClassPartition.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassPartitionRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassPartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceClassPartition", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceClassPartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceHardwareInfo(self, request):
        """查询设备硬件配置信息，如 CPU 型号，内存大小，磁盘大小和数量

        :param request: Request instance for DescribeDeviceHardwareInfo.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceHardwareInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceHardwareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceHardwareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceHardwareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceInventory(self, request):
        """查询设备库存

        :param request: Request instance for DescribeDeviceInventory.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceInventoryRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceInventoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceInventory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceInventoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceOperationLog(self, request):
        """查询设备操作日志， 如设备重启，重装，设置密码等操作

        :param request: Request instance for DescribeDeviceOperationLog.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceOperationLogRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceOperationLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceOperationLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceOperationLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePartition(self, request):
        """获取物理机的分区格式

        :param request: Request instance for DescribeDevicePartition.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePartitionRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePartition", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePosition(self, request):
        """查询服务器所在的位置，如机架，上联交换机等信息

        :param request: Request instance for DescribeDevicePosition.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePositionRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePositionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePosition", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePositionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePriceInfo(self, request):
        """查询服务器价格信息，支持设备的批量查找，支持标准机型和弹性机型的混合查找

        :param request: Request instance for DescribeDevicePriceInfo.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePriceInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePriceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePriceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePriceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevices(self, request):
        """查询物理服务器，可以按照实例，业务IP等过滤

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicesResponse`

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


    def DescribeHardwareSpecification(self, request):
        """查询自定义机型部件信息，包括CpuId对应的型号，DiskTypeId对应的磁盘类型

        :param request: Request instance for DescribeHardwareSpecification.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeHardwareSpecificationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeHardwareSpecificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHardwareSpecification", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHardwareSpecificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostedDeviceOutBandInfo(self, request):
        """查询托管设备带外信息

        :param request: Request instance for DescribeHostedDeviceOutBandInfo.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeHostedDeviceOutBandInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeHostedDeviceOutBandInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostedDeviceOutBandInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostedDeviceOutBandInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOperationResult(self, request):
        """获取异步操作状态的完成状态

        :param request: Request instance for DescribeOperationResult.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeOperationResultRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeOperationResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperationResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperationResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOsInfo(self, request):
        """查询指定机型所支持的操作系统

        :param request: Request instance for DescribeOsInfo.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeOsInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeOsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePsaRegulations(self, request):
        """获取预授权规则列表

        :param request: Request instance for DescribePsaRegulations.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribePsaRegulationsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribePsaRegulationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePsaRegulations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePsaRegulationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """查询地域以及可用区

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepairTaskConstant(self, request):
        """维修任务配置获取

        :param request: Request instance for DescribeRepairTaskConstant.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeRepairTaskConstantRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeRepairTaskConstantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepairTaskConstant", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepairTaskConstantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInfo(self, request):
        """获取用户维修任务列表及详细信息<br>
        <br>
        TaskStatus（任务状态ID）与状态中文名的对应关系如下：<br>
        1：未授权<br>
        2：处理中<br>
        3：待确认<br>
        4：未授权-暂不处理<br>
        5：已恢复<br>
        6：待确认-未恢复<br>

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskOperationLog(self, request):
        """获取维修任务操作日志

        :param request: Request instance for DescribeTaskOperationLog.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeTaskOperationLogRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeTaskOperationLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskOperationLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskOperationLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCmdTaskInfo(self, request):
        """获取自定义脚本任务详细信息

        :param request: Request instance for DescribeUserCmdTaskInfo.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTaskInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCmdTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCmdTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCmdTasks(self, request):
        """获取自定义脚本任务列表

        :param request: Request instance for DescribeUserCmdTasks.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTasksRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCmdTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCmdTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCmds(self, request):
        """获取自定义脚本信息列表

        :param request: Request instance for DescribeUserCmds.
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCmds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCmdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachCamRole(self, request):
        """服务器绑定CAM角色

        :param request: Request instance for DetachCamRole.
        :type request: :class:`tencentcloud.bm.v20180423.models.DetachCamRoleRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DetachCamRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachCamRole", params, headers=headers)
            response = json.loads(body)
            model = models.DetachCamRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomImageAttribute(self, request):
        """用于修改自定义镜像名或描述

        :param request: Request instance for ModifyCustomImageAttribute.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyCustomImageAttributeRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyCustomImageAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomImageAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomImageAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceAliases(self, request):
        """修改服务器名称

        :param request: Request instance for ModifyDeviceAliases.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAliasesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAliasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceAliases", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceAliasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceAutoRenewFlag(self, request):
        """修改物理机服务器自动续费标志

        :param request: Request instance for ModifyDeviceAutoRenewFlag.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLanIp(self, request):
        """修改物理机内网IP（不重装系统）

        :param request: Request instance for ModifyLanIp.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyLanIpRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyLanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPayModePre2Post(self, request):
        """将设备的预付费模式修改为后付费计费模式，支持批量转换。（前提是客户要加入黑石物理机后付费计费的白名单，申请黑石物理机后付费可以联系腾讯云客服）

        :param request: Request instance for ModifyPayModePre2Post.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyPayModePre2PostRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyPayModePre2PostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPayModePre2Post", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPayModePre2PostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPsaRegulation(self, request):
        """允许修改规则信息及关联故障类型

        :param request: Request instance for ModifyPsaRegulation.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyPsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyPsaRegulationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPsaRegulation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPsaRegulationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserCmd(self, request):
        """修改自定义脚本

        :param request: Request instance for ModifyUserCmd.
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyUserCmdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserCmd", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserCmdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineDevices(self, request):
        """销毁黑石物理机实例：可以销毁物理机列表中的竞价实例，或回收站列表中所有计费模式的实例

        :param request: Request instance for OfflineDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.OfflineDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.OfflineDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineDevices", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootDevices(self, request):
        """重启机器

        :param request: Request instance for RebootDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.RebootDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RebootDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootDevices", params, headers=headers)
            response = json.loads(body)
            model = models.RebootDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverDevices(self, request):
        """恢复回收站中的物理机（仅限后付费的物理机）

        :param request: Request instance for RecoverDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.RecoverDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RecoverDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverDevices", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReloadDeviceOs(self, request):
        """重装操作系统

        :param request: Request instance for ReloadDeviceOs.
        :type request: :class:`tencentcloud.bm.v20180423.models.ReloadDeviceOsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ReloadDeviceOsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReloadDeviceOs", params, headers=headers)
            response = json.loads(body)
            model = models.ReloadDeviceOsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RepairTaskControl(self, request):
        """此接口用于操作维修任务<br>
        入参TaskId为维修任务ID<br>
        入参Operate表示对维修任务的操作，支持如下取值：<br>
        AuthorizeRepair（授权维修）<br>
        Ignore（暂不提醒）<br>
        ConfirmRecovered（维修完成后，确认故障恢复）<br>
        ConfirmUnRecovered（维修完成后，确认故障未恢复，该操作已不推荐用）<br>
        NeedRepairAgain（维修完成后，故障未恢复，需要重新维修，推荐用此操作打回）<br>
        入参OperateRemark仅在Operate为NeedRepairAgain时有效，表示打回重修原因，建议给出打回的具体原因。<br>
        <br>
        操作约束（当前任务状态(TaskStatus)->对应可执行的操作）：<br>
        未授权(1)->授权维修；暂不处理<br>
        暂不处理(4)->授权维修<br>
        待确认(3)->确认故障恢复；确认故障未恢复；需要重新维修<br>
        未恢复(6)->确认故障恢复<br>
        <br>
        对于Ping不可达故障的任务，还允许：<br>
        未授权->确认故障恢复<br>
        暂不处理->确认故障恢复<br>
        <br>
        处理中与已恢复状态的任务不允许进行操作。<br>
        <br>
        详细信息请访问：https://cloud.tencent.com/document/product/386/18190

        :param request: Request instance for RepairTaskControl.
        :type request: :class:`tencentcloud.bm.v20180423.models.RepairTaskControlRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RepairTaskControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RepairTaskControl", params, headers=headers)
            response = json.loads(body)
            model = models.RepairTaskControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDevicePassword(self, request):
        """重置服务器密码

        :param request: Request instance for ResetDevicePassword.
        :type request: :class:`tencentcloud.bm.v20180423.models.ResetDevicePasswordRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ResetDevicePasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDevicePassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDevicePasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReturnDevices(self, request):
        """退回物理机至回收站，支持批量退还不同计费模式的物理机（包括预付费、后付费、预付费转后付费）

        :param request: Request instance for ReturnDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.ReturnDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ReturnDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReturnDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ReturnDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunUserCmd(self, request):
        """运行自定义脚本

        :param request: Request instance for RunUserCmd.
        :type request: :class:`tencentcloud.bm.v20180423.models.RunUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RunUserCmdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunUserCmd", params, headers=headers)
            response = json.loads(body)
            model = models.RunUserCmdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOutBandVpnAuthPassword(self, request):
        """设置带外VPN认证用户密码

        :param request: Request instance for SetOutBandVpnAuthPassword.
        :type request: :class:`tencentcloud.bm.v20180423.models.SetOutBandVpnAuthPasswordRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.SetOutBandVpnAuthPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOutBandVpnAuthPassword", params, headers=headers)
            response = json.loads(body)
            model = models.SetOutBandVpnAuthPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ShutdownDevices(self, request):
        """关闭服务器

        :param request: Request instance for ShutdownDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.ShutdownDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ShutdownDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ShutdownDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ShutdownDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartDevices(self, request):
        """开启服务器

        :param request: Request instance for StartDevices.
        :type request: :class:`tencentcloud.bm.v20180423.models.StartDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.StartDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartDevices", params, headers=headers)
            response = json.loads(body)
            model = models.StartDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindPsaTag(self, request):
        """解除标签与预授权规则的绑定

        :param request: Request instance for UnbindPsaTag.
        :type request: :class:`tencentcloud.bm.v20180423.models.UnbindPsaTagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.UnbindPsaTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindPsaTag", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindPsaTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))