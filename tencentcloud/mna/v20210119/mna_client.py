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
from tencentcloud.mna.v20210119 import models


class MnaClient(AbstractClient):
    _apiVersion = '2021-01-19'
    _endpoint = 'mna.tencentcloudapi.com'
    _service = 'mna'


    def ActivateHardware(self, request):
        """激活硬件设备

        :param request: Request instance for ActivateHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.ActivateHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.ActivateHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateHardware", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDevice(self, request):
        """新建设备记录

        :param request: Request instance for AddDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AddDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddHardware(self, request):
        """添加硬件设备，生成未激活的硬件设备，可支持批量添加

        :param request: Request instance for AddHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddHardware", params, headers=headers)
            response = json.loads(body)
            model = models.AddHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEncryptedKey(self, request):
        """通过此接口设置和更新预置密钥

        :param request: Request instance for CreateEncryptedKey.
        :type request: :class:`tencentcloud.mna.v20210119.models.CreateEncryptedKeyRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.CreateEncryptedKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEncryptedKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEncryptedKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQos(self, request):
        """移动网络发起Qos加速过程

        :param request: Request instance for CreateQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.CreateQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.CreateQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQos", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevice(self, request):
        """删除设备信息

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQos(self, request):
        """移动网络停止Qos加速过程

        :param request: Request instance for DeleteQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQos", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQos(self, request):
        """获取Qos加速状态

        :param request: Request instance for DescribeQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.DescribeQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DescribeQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevice(self, request):
        """通过指定设备的ID查找设备详细信息

        :param request: Request instance for GetDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevice", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevicePayMode(self, request):
        """获取设备付费模式

        :param request: Request instance for GetDevicePayMode.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDevicePayModeRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDevicePayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevicePayMode", params, headers=headers)
            response = json.loads(body)
            model = models.GetDevicePayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevices(self, request):
        """获取设备信息列表

        :param request: Request instance for GetDevices.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevices", params, headers=headers)
            response = json.loads(body)
            model = models.GetDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowPackages(self, request):
        """获取流量包列表

        :param request: Request instance for GetFlowPackages.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowPackagesRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowPackages", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowStatistic(self, request):
        """获取指定设备Id，指定时间点数据流量使用情况

        :param request: Request instance for GetFlowStatistic.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetHardwareList(self, request):
        """获取厂商硬件列表

        :param request: Request instance for GetHardwareList.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetHardwareListRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetHardwareListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetHardwareList", params, headers=headers)
            response = json.loads(body)
            model = models.GetHardwareListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMultiFlowStatistic(self, request):
        """批量获取设备流量统计曲线

        :param request: Request instance for GetMultiFlowStatistic.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetMultiFlowStatisticRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetMultiFlowStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMultiFlowStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.GetMultiFlowStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetNetMonitor(self, request):
        """获取单设备的实时流量统计指标

        :param request: Request instance for GetNetMonitor.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetNetMonitorRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetNetMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetNetMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.GetNetMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPublicKey(self, request):
        """获取公钥用于验签

        :param request: Request instance for GetPublicKey.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetPublicKeyRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.GetPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetStatisticData(self, request):
        """在用量统计页面下载流量数据

        :param request: Request instance for GetStatisticData.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStatisticData", params, headers=headers)
            response = json.loads(body)
            model = models.GetStatisticDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetVendorHardware(self, request):
        """获取厂商硬件设备列表

        :param request: Request instance for GetVendorHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetVendorHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetVendorHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetVendorHardware", params, headers=headers)
            response = json.loads(body)
            model = models.GetVendorHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPackageRenewFlag(self, request):
        """可开启/关闭流量包自动续费，不影响当前周期正在生效的流量包。

        :param request: Request instance for ModifyPackageRenewFlag.
        :type request: :class:`tencentcloud.mna.v20210119.models.ModifyPackageRenewFlagRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.ModifyPackageRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPackageRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPackageRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OrderFlowPackage(self, request):
        """购买预付费流量包

        :param request: Request instance for OrderFlowPackage.
        :type request: :class:`tencentcloud.mna.v20210119.models.OrderFlowPackageRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.OrderFlowPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OrderFlowPackage", params, headers=headers)
            response = json.loads(body)
            model = models.OrderFlowPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDevice(self, request):
        """更新设备信息

        :param request: Request instance for UpdateDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateHardware(self, request):
        """更新硬件信息

        :param request: Request instance for UpdateHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateHardware", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))