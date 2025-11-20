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
from tencentcloud.bm.v20180423 import models
from typing import Dict


class BmClient(AbstractClient):
    _apiVersion = '2018-04-23'
    _endpoint = 'bm.tencentcloudapi.com'
    _service = 'bm'

    async def AttachCamRole(
            self,
            request: models.AttachCamRoleRequest,
            opts: Dict = None,
    ) -> models.AttachCamRoleResponse:
        """
        服务器绑定CAM角色，该角色授权访问黑石物理服务器服务，为黑石物理服务器提供了访问资源的权限，如请求服务器的临时证书
        """
        
        kwargs = {}
        kwargs["action"] = "AttachCamRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachCamRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindPsaTag(
            self,
            request: models.BindPsaTagRequest,
            opts: Dict = None,
    ) -> models.BindPsaTagResponse:
        """
        为预授权规则绑定标签
        """
        
        kwargs = {}
        kwargs["action"] = "BindPsaTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindPsaTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BuyDevices(
            self,
            request: models.BuyDevicesRequest,
            opts: Dict = None,
    ) -> models.BuyDevicesResponse:
        """
        购买黑石物理机
        """
        
        kwargs = {}
        kwargs["action"] = "BuyDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BuyDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomImage(
            self,
            request: models.CreateCustomImageRequest,
            opts: Dict = None,
    ) -> models.CreateCustomImageResponse:
        """
        创建自定义镜像<br>
        每个AppId在每个可用区最多保留20个自定义镜像
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePsaRegulation(
            self,
            request: models.CreatePsaRegulationRequest,
            opts: Dict = None,
    ) -> models.CreatePsaRegulationResponse:
        """
        创建预授权规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePsaRegulation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePsaRegulationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSpotDevice(
            self,
            request: models.CreateSpotDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateSpotDeviceResponse:
        """
        创建黑石竞价实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSpotDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSpotDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserCmd(
            self,
            request: models.CreateUserCmdRequest,
            opts: Dict = None,
    ) -> models.CreateUserCmdResponse:
        """
        创建自定义脚本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomImages(
            self,
            request: models.DeleteCustomImagesRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomImagesResponse:
        """
        删除自定义镜像<br>
        正用于部署或重装中的镜像被删除后，镜像文件将保留一段时间，直到部署或重装结束
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePsaRegulation(
            self,
            request: models.DeletePsaRegulationRequest,
            opts: Dict = None,
    ) -> models.DeletePsaRegulationResponse:
        """
        删除预授权规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePsaRegulation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePsaRegulationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserCmds(
            self,
            request: models.DeleteUserCmdsRequest,
            opts: Dict = None,
    ) -> models.DeleteUserCmdsResponse:
        """
        删除自定义脚本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserCmds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserCmdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomImageProcess(
            self,
            request: models.DescribeCustomImageProcessRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomImageProcessResponse:
        """
        查询自定义镜像制作进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomImageProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomImageProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomImages(
            self,
            request: models.DescribeCustomImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomImagesResponse:
        """
        查看自定义镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceClass(
            self,
            request: models.DescribeDeviceClassRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceClassResponse:
        """
        获取设备类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceClassPartition(
            self,
            request: models.DescribeDeviceClassPartitionRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceClassPartitionResponse:
        """
        查询机型支持的RAID方式， 并返回系统盘的分区和逻辑盘的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceClassPartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceClassPartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceHardwareInfo(
            self,
            request: models.DescribeDeviceHardwareInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceHardwareInfoResponse:
        """
        查询设备硬件配置信息，如 CPU 型号，内存大小，磁盘大小和数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceHardwareInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceHardwareInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceInventory(
            self,
            request: models.DescribeDeviceInventoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceInventoryResponse:
        """
        查询设备库存
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceInventory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceInventoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceOperationLog(
            self,
            request: models.DescribeDeviceOperationLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceOperationLogResponse:
        """
        查询设备操作日志， 如设备重启，重装，设置密码等操作
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceOperationLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceOperationLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePartition(
            self,
            request: models.DescribeDevicePartitionRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePartitionResponse:
        """
        获取物理机的分区格式
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePosition(
            self,
            request: models.DescribeDevicePositionRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePositionResponse:
        """
        查询服务器所在的位置，如机架，上联交换机等信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePosition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePositionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePriceInfo(
            self,
            request: models.DescribeDevicePriceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePriceInfoResponse:
        """
        查询服务器价格信息，支持设备的批量查找，支持标准机型和弹性机型的混合查找
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePriceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePriceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        查询物理服务器，可以按照实例，业务IP等过滤
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHardwareSpecification(
            self,
            request: models.DescribeHardwareSpecificationRequest,
            opts: Dict = None,
    ) -> models.DescribeHardwareSpecificationResponse:
        """
        查询自定义机型部件信息，包括CpuId对应的型号，DiskTypeId对应的磁盘类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHardwareSpecification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHardwareSpecificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostedDeviceOutBandInfo(
            self,
            request: models.DescribeHostedDeviceOutBandInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHostedDeviceOutBandInfoResponse:
        """
        查询托管设备带外信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostedDeviceOutBandInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostedDeviceOutBandInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOperationResult(
            self,
            request: models.DescribeOperationResultRequest,
            opts: Dict = None,
    ) -> models.DescribeOperationResultResponse:
        """
        获取异步操作状态的完成状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOperationResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOperationResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOsInfo(
            self,
            request: models.DescribeOsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeOsInfoResponse:
        """
        查询指定机型所支持的操作系统
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePsaRegulations(
            self,
            request: models.DescribePsaRegulationsRequest,
            opts: Dict = None,
    ) -> models.DescribePsaRegulationsResponse:
        """
        获取预授权规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePsaRegulations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePsaRegulationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        查询地域以及可用区
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepairTaskConstant(
            self,
            request: models.DescribeRepairTaskConstantRequest,
            opts: Dict = None,
    ) -> models.DescribeRepairTaskConstantResponse:
        """
        维修任务配置获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepairTaskConstant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepairTaskConstantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInfo(
            self,
            request: models.DescribeTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInfoResponse:
        """
        获取用户维修任务列表及详细信息<br>
        <br>
        TaskStatus（任务状态ID）与状态中文名的对应关系如下：<br>
        1：未授权<br>
        2：处理中<br>
        3：待确认<br>
        4：未授权-暂不处理<br>
        5：已恢复<br>
        6：待确认-未恢复<br>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskOperationLog(
            self,
            request: models.DescribeTaskOperationLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskOperationLogResponse:
        """
        获取维修任务操作日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskOperationLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskOperationLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCmdTaskInfo(
            self,
            request: models.DescribeUserCmdTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCmdTaskInfoResponse:
        """
        获取自定义脚本任务详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCmdTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCmdTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCmdTasks(
            self,
            request: models.DescribeUserCmdTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCmdTasksResponse:
        """
        获取自定义脚本任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCmdTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCmdTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCmds(
            self,
            request: models.DescribeUserCmdsRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCmdsResponse:
        """
        获取自定义脚本信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCmds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCmdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachCamRole(
            self,
            request: models.DetachCamRoleRequest,
            opts: Dict = None,
    ) -> models.DetachCamRoleResponse:
        """
        服务器绑定CAM角色
        """
        
        kwargs = {}
        kwargs["action"] = "DetachCamRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachCamRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomImageAttribute(
            self,
            request: models.ModifyCustomImageAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomImageAttributeResponse:
        """
        用于修改自定义镜像名或描述
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomImageAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomImageAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceAliases(
            self,
            request: models.ModifyDeviceAliasesRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceAliasesResponse:
        """
        修改服务器名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceAliases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceAliasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceAutoRenewFlag(
            self,
            request: models.ModifyDeviceAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceAutoRenewFlagResponse:
        """
        修改物理机服务器自动续费标志
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLanIp(
            self,
            request: models.ModifyLanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyLanIpResponse:
        """
        修改物理机内网IP（不重装系统）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPayModePre2Post(
            self,
            request: models.ModifyPayModePre2PostRequest,
            opts: Dict = None,
    ) -> models.ModifyPayModePre2PostResponse:
        """
        将设备的预付费模式修改为后付费计费模式，支持批量转换。（前提是客户要加入黑石物理机后付费计费的白名单，申请黑石物理机后付费可以联系腾讯云客服）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPayModePre2Post"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPayModePre2PostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPsaRegulation(
            self,
            request: models.ModifyPsaRegulationRequest,
            opts: Dict = None,
    ) -> models.ModifyPsaRegulationResponse:
        """
        允许修改规则信息及关联故障类型
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPsaRegulation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPsaRegulationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserCmd(
            self,
            request: models.ModifyUserCmdRequest,
            opts: Dict = None,
    ) -> models.ModifyUserCmdResponse:
        """
        修改自定义脚本
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineDevices(
            self,
            request: models.OfflineDevicesRequest,
            opts: Dict = None,
    ) -> models.OfflineDevicesResponse:
        """
        销毁黑石物理机实例：可以销毁物理机列表中的竞价实例，或回收站列表中所有计费模式的实例
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootDevices(
            self,
            request: models.RebootDevicesRequest,
            opts: Dict = None,
    ) -> models.RebootDevicesResponse:
        """
        重启机器
        """
        
        kwargs = {}
        kwargs["action"] = "RebootDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverDevices(
            self,
            request: models.RecoverDevicesRequest,
            opts: Dict = None,
    ) -> models.RecoverDevicesResponse:
        """
        恢复回收站中的物理机（仅限后付费的物理机）
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReloadDeviceOs(
            self,
            request: models.ReloadDeviceOsRequest,
            opts: Dict = None,
    ) -> models.ReloadDeviceOsResponse:
        """
        重装操作系统
        """
        
        kwargs = {}
        kwargs["action"] = "ReloadDeviceOs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReloadDeviceOsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RepairTaskControl(
            self,
            request: models.RepairTaskControlRequest,
            opts: Dict = None,
    ) -> models.RepairTaskControlResponse:
        """
        此接口用于操作维修任务<br>
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
        """
        
        kwargs = {}
        kwargs["action"] = "RepairTaskControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RepairTaskControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDevicePassword(
            self,
            request: models.ResetDevicePasswordRequest,
            opts: Dict = None,
    ) -> models.ResetDevicePasswordResponse:
        """
        重置服务器密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDevicePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDevicePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReturnDevices(
            self,
            request: models.ReturnDevicesRequest,
            opts: Dict = None,
    ) -> models.ReturnDevicesResponse:
        """
        退回物理机至回收站，支持批量退还不同计费模式的物理机（包括预付费、后付费、预付费转后付费）
        """
        
        kwargs = {}
        kwargs["action"] = "ReturnDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReturnDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunUserCmd(
            self,
            request: models.RunUserCmdRequest,
            opts: Dict = None,
    ) -> models.RunUserCmdResponse:
        """
        运行自定义脚本
        """
        
        kwargs = {}
        kwargs["action"] = "RunUserCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunUserCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetOutBandVpnAuthPassword(
            self,
            request: models.SetOutBandVpnAuthPasswordRequest,
            opts: Dict = None,
    ) -> models.SetOutBandVpnAuthPasswordResponse:
        """
        设置带外VPN认证用户密码
        """
        
        kwargs = {}
        kwargs["action"] = "SetOutBandVpnAuthPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetOutBandVpnAuthPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ShutdownDevices(
            self,
            request: models.ShutdownDevicesRequest,
            opts: Dict = None,
    ) -> models.ShutdownDevicesResponse:
        """
        关闭服务器
        """
        
        kwargs = {}
        kwargs["action"] = "ShutdownDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ShutdownDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartDevices(
            self,
            request: models.StartDevicesRequest,
            opts: Dict = None,
    ) -> models.StartDevicesResponse:
        """
        开启服务器
        """
        
        kwargs = {}
        kwargs["action"] = "StartDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindPsaTag(
            self,
            request: models.UnbindPsaTagRequest,
            opts: Dict = None,
    ) -> models.UnbindPsaTagResponse:
        """
        解除标签与预授权规则的绑定
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindPsaTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindPsaTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)