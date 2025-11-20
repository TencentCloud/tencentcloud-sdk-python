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
from tencentcloud.mna.v20210119 import models
from typing import Dict


class MnaClient(AbstractClient):
    _apiVersion = '2021-01-19'
    _endpoint = 'mna.tencentcloudapi.com'
    _service = 'mna'

    async def ActivateHardware(
            self,
            request: models.ActivateHardwareRequest,
            opts: Dict = None,
    ) -> models.ActivateHardwareResponse:
        """
        激活硬件设备
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateHardware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateHardwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddDevice(
            self,
            request: models.AddDeviceRequest,
            opts: Dict = None,
    ) -> models.AddDeviceResponse:
        """
        新建设备记录
        """
        
        kwargs = {}
        kwargs["action"] = "AddDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddGroup(
            self,
            request: models.AddGroupRequest,
            opts: Dict = None,
    ) -> models.AddGroupResponse:
        """
        新建分组
        """
        
        kwargs = {}
        kwargs["action"] = "AddGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddHardware(
            self,
            request: models.AddHardwareRequest,
            opts: Dict = None,
    ) -> models.AddHardwareResponse:
        """
        添加硬件设备，生成未激活的硬件设备，可支持批量添加
        """
        
        kwargs = {}
        kwargs["action"] = "AddHardware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddHardwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddL3Conn(
            self,
            request: models.AddL3ConnRequest,
            opts: Dict = None,
    ) -> models.AddL3ConnResponse:
        """
        新建互通规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddL3Conn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddL3ConnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEncryptedKey(
            self,
            request: models.CreateEncryptedKeyRequest,
            opts: Dict = None,
    ) -> models.CreateEncryptedKeyResponse:
        """
        通过此接口设置和更新预置密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEncryptedKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEncryptedKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        删除设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        删除分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL3Conn(
            self,
            request: models.DeleteL3ConnRequest,
            opts: Dict = None,
    ) -> models.DeleteL3ConnResponse:
        """
        删除互通规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL3Conn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL3ConnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadActiveDeviceCount(
            self,
            request: models.DownloadActiveDeviceCountRequest,
            opts: Dict = None,
    ) -> models.DownloadActiveDeviceCountResponse:
        """
        下载活跃设备数量统计
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadActiveDeviceCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadActiveDeviceCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetActiveDeviceCount(
            self,
            request: models.GetActiveDeviceCountRequest,
            opts: Dict = None,
    ) -> models.GetActiveDeviceCountResponse:
        """
        活跃设备数量统计
        """
        
        kwargs = {}
        kwargs["action"] = "GetActiveDeviceCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetActiveDeviceCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevice(
            self,
            request: models.GetDeviceRequest,
            opts: Dict = None,
    ) -> models.GetDeviceResponse:
        """
        通过指定设备的ID查找设备详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevicePayMode(
            self,
            request: models.GetDevicePayModeRequest,
            opts: Dict = None,
    ) -> models.GetDevicePayModeResponse:
        """
        获取设备付费模式
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevicePayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDevicePayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevices(
            self,
            request: models.GetDevicesRequest,
            opts: Dict = None,
    ) -> models.GetDevicesResponse:
        """
        获取设备信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFlowAlarmInfo(
            self,
            request: models.GetFlowAlarmInfoRequest,
            opts: Dict = None,
    ) -> models.GetFlowAlarmInfoResponse:
        """
        根据AppId查询用户设置的流量告警信息，包括阈值，回调url和key
        """
        
        kwargs = {}
        kwargs["action"] = "GetFlowAlarmInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFlowAlarmInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFlowPackages(
            self,
            request: models.GetFlowPackagesRequest,
            opts: Dict = None,
    ) -> models.GetFlowPackagesResponse:
        """
        获取流量包列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetFlowPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFlowPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFlowStatistic(
            self,
            request: models.GetFlowStatisticRequest,
            opts: Dict = None,
    ) -> models.GetFlowStatisticResponse:
        """
        获取指定设备Id，指定时间点数据流量使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "GetFlowStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFlowStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFlowStatisticByGroup(
            self,
            request: models.GetFlowStatisticByGroupRequest,
            opts: Dict = None,
    ) -> models.GetFlowStatisticByGroupResponse:
        """
        获取指定分组，指定时间数据流量使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "GetFlowStatisticByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFlowStatisticByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFlowStatisticByRegion(
            self,
            request: models.GetFlowStatisticByRegionRequest,
            opts: Dict = None,
    ) -> models.GetFlowStatisticByRegionResponse:
        """
        获取指定区域，指定时间点数据流量使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "GetFlowStatisticByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFlowStatisticByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupDetail(
            self,
            request: models.GetGroupDetailRequest,
            opts: Dict = None,
    ) -> models.GetGroupDetailResponse:
        """
        查看分组详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupList(
            self,
            request: models.GetGroupListRequest,
            opts: Dict = None,
    ) -> models.GetGroupListResponse:
        """
        获取分组列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetHardwareList(
            self,
            request: models.GetHardwareListRequest,
            opts: Dict = None,
    ) -> models.GetHardwareListResponse:
        """
        获取厂商硬件列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetHardwareList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetHardwareListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetL3ConnList(
            self,
            request: models.GetL3ConnListRequest,
            opts: Dict = None,
    ) -> models.GetL3ConnListResponse:
        """
        获取互通规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetL3ConnList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetL3ConnListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMultiFlowStatistic(
            self,
            request: models.GetMultiFlowStatisticRequest,
            opts: Dict = None,
    ) -> models.GetMultiFlowStatisticResponse:
        """
        批量获取设备流量统计曲线
        """
        
        kwargs = {}
        kwargs["action"] = "GetMultiFlowStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMultiFlowStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetNetMonitor(
            self,
            request: models.GetNetMonitorRequest,
            opts: Dict = None,
    ) -> models.GetNetMonitorResponse:
        """
        获取单设备的实时流量统计指标
        """
        
        kwargs = {}
        kwargs["action"] = "GetNetMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetNetMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPublicKey(
            self,
            request: models.GetPublicKeyRequest,
            opts: Dict = None,
    ) -> models.GetPublicKeyResponse:
        """
        获取公钥用于验签
        """
        
        kwargs = {}
        kwargs["action"] = "GetPublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetStatisticData(
            self,
            request: models.GetStatisticDataRequest,
            opts: Dict = None,
    ) -> models.GetStatisticDataResponse:
        """
        在用量统计页面下载流量数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetStatisticData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetStatisticDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVendorHardware(
            self,
            request: models.GetVendorHardwareRequest,
            opts: Dict = None,
    ) -> models.GetVendorHardwareResponse:
        """
        获取厂商硬件设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetVendorHardware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVendorHardwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupAddDevice(
            self,
            request: models.GroupAddDeviceRequest,
            opts: Dict = None,
    ) -> models.GroupAddDeviceResponse:
        """
        向已存在分组中添加设备
        """
        
        kwargs = {}
        kwargs["action"] = "GroupAddDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupAddDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupDeleteDevice(
            self,
            request: models.GroupDeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.GroupDeleteDeviceResponse:
        """
        删除分组中的设备
        """
        
        kwargs = {}
        kwargs["action"] = "GroupDeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupDeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPackageRenewFlag(
            self,
            request: models.ModifyPackageRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyPackageRenewFlagResponse:
        """
        可开启/关闭流量包自动续费，不影响当前周期正在生效的流量包。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPackageRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPackageRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OrderFlowPackage(
            self,
            request: models.OrderFlowPackageRequest,
            opts: Dict = None,
    ) -> models.OrderFlowPackageResponse:
        """
        购买预付费流量包
        """
        
        kwargs = {}
        kwargs["action"] = "OrderFlowPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OrderFlowPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OrderPerLicense(
            self,
            request: models.OrderPerLicenseRequest,
            opts: Dict = None,
    ) -> models.OrderPerLicenseResponse:
        """
        购买一次性授权License
        """
        
        kwargs = {}
        kwargs["action"] = "OrderPerLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OrderPerLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportOrder(
            self,
            request: models.ReportOrderRequest,
            opts: Dict = None,
    ) -> models.ReportOrderResponse:
        """
        用户上报自定义的订单信息，多网聚合加速服务将相关信息进行保存
        """
        
        kwargs = {}
        kwargs["action"] = "ReportOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNotifyUrl(
            self,
            request: models.SetNotifyUrlRequest,
            opts: Dict = None,
    ) -> models.SetNotifyUrlResponse:
        """
        设置用户流量告警信息接口，通过该接口设置流量包告警阈值以及告警时回调的url和key
        """
        
        kwargs = {}
        kwargs["action"] = "SetNotifyUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNotifyUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDevice(
            self,
            request: models.UpdateDeviceRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceResponse:
        """
        更新设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGroup(
            self,
            request: models.UpdateGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateGroupResponse:
        """
        更新分组备注
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateHardware(
            self,
            request: models.UpdateHardwareRequest,
            opts: Dict = None,
    ) -> models.UpdateHardwareResponse:
        """
        更新硬件信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateHardware"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateHardwareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateL3Cidr(
            self,
            request: models.UpdateL3CidrRequest,
            opts: Dict = None,
    ) -> models.UpdateL3CidrResponse:
        """
        更新互通规则CIDR
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateL3Cidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateL3CidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateL3Conn(
            self,
            request: models.UpdateL3ConnRequest,
            opts: Dict = None,
    ) -> models.UpdateL3ConnResponse:
        """
        更新互通规则备注
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateL3Conn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateL3ConnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateL3Switch(
            self,
            request: models.UpdateL3SwitchRequest,
            opts: Dict = None,
    ) -> models.UpdateL3SwitchResponse:
        """
        更新互通规则开关
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateL3Switch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateL3SwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)