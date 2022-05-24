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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AppDeviceInfo(AbstractModel):
    """云api直接绑定设备出参

    """

    def __init__(self):
        r"""
        :param DeviceId: 产品ID/设备名
        :type DeviceId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param AliasName: 设备别名
        :type AliasName: str
        :param IconUrl: icon地址
        :type IconUrl: str
        :param FamilyId: 家庭ID
        :type FamilyId: str
        :param RoomId: 房间ID
        :type RoomId: str
        :param DeviceType: 设备类型
        :type DeviceType: int
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        """
        self.DeviceId = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None
        self.IconUrl = None
        self.FamilyId = None
        self.RoomId = None
        self.DeviceType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")
        self.IconUrl = params.get("IconUrl")
        self.FamilyId = params.get("FamilyId")
        self.RoomId = params.get("RoomId")
        self.DeviceType = params.get("DeviceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchProductionInfo(AbstractModel):
    """获取返回列表的详情。

    """

    def __init__(self):
        r"""
        :param BatchProductionId: 量产ID
        :type BatchProductionId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param BurnMethod: 烧录方式
        :type BurnMethod: int
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param ProductName: 产品名称
        :type ProductName: str
        """
        self.BatchProductionId = None
        self.ProductId = None
        self.BurnMethod = None
        self.CreateTime = None
        self.ProductName = None


    def _deserialize(self, params):
        self.BatchProductionId = params.get("BatchProductionId")
        self.ProductId = params.get("ProductId")
        self.BurnMethod = params.get("BurnMethod")
        self.CreateTime = params.get("CreateTime")
        self.ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceInfo(AbstractModel):
    """BindDeviceInfo

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDevicesRequest(AbstractModel):
    """BindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关设备的产品ID。
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名。
        :type GatewayDeviceName: str
        :param ProductId: 被绑定设备的产品ID。
        :type ProductId: str
        :param DeviceNames: 被绑定的多个设备名。
        :type DeviceNames: list of str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDevicesResponse(AbstractModel):
    """BindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindProductInfo(AbstractModel):
    """绑定、未绑定产品详细信息

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID。
        :type ProductId: str
        :param ProductName: 产品名称。
        :type ProductName: str
        :param ProjectId: 产品所属项目ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param DataProtocol: 物模型类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataProtocol: int
        :param CategoryId: 产品分组模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryId: int
        :param ProductType: 产品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductType: int
        :param NetType: 连接类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        :param DevStatus: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DevStatus: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProjectId = None
        self.DataProtocol = None
        self.CategoryId = None
        self.ProductType = None
        self.NetType = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProjectId = params.get("ProjectId")
        self.DataProtocol = params.get("DataProtocol")
        self.CategoryId = params.get("CategoryId")
        self.ProductType = params.get("ProductType")
        self.NetType = params.get("NetType")
        self.DevStatus = params.get("DevStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindProductsRequest(AbstractModel):
    """BindProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID。
        :type GatewayProductId: str
        :param ProductIds: 待绑定的子产品ID数组。
        :type ProductIds: list of str
        """
        self.GatewayProductId = None
        self.ProductIds = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindProductsResponse(AbstractModel):
    """BindProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallDeviceActionAsyncRequest(AbstractModel):
    """CallDeviceActionAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :type ActionId: str
        :param InputParams: 输入参数
        :type InputParams: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.ActionId = None
        self.InputParams = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.InputParams = params.get("InputParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDeviceActionAsyncResponse(AbstractModel):
    """CallDeviceActionAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClientToken: 调用Id
        :type ClientToken: str
        :param Status: 异步调用状态
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientToken = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CallDeviceActionSyncRequest(AbstractModel):
    """CallDeviceActionSync请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :type ActionId: str
        :param InputParams: 输入参数
        :type InputParams: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.ActionId = None
        self.InputParams = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.InputParams = params.get("InputParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDeviceActionSyncResponse(AbstractModel):
    """CallDeviceActionSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClientToken: 调用Id
        :type ClientToken: str
        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param Status: 返回状态，当设备不在线等部分情况，会通过该 Status 返回。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientToken = None
        self.OutputParams = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.OutputParams = params.get("OutputParams")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Data: 属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义
        :type Data: str
        :param Method: 请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性
        :type Method: str
        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName , 通常情况不需要填写
        :type DeviceId: str
        :param DataTimestamp: 上报数据UNIX时间戳(毫秒), 仅对Method:reported有效
        :type DataTimestamp: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Data = None
        self.Method = None
        self.DeviceId = None
        self.DataTimestamp = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")
        self.Method = params.get("Method")
        self.DeviceId = params.get("DeviceId")
        self.DataTimestamp = params.get("DataTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回信息
        :type Data: str
        :param Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic.
pushResult 是表示发送结果，其中 0 表示成功， 23101 表示设备未在线或没有订阅相关的 MQTT Topic。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateBatchProductionRequest(AbstractModel):
    """CreateBatchProduction请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param BurnMethod: 烧录方式，0为直接烧录，1为动态注册。
        :type BurnMethod: int
        :param GenerationMethod: 生成方式，0为系统生成，1为文件上传。
        :type GenerationMethod: int
        :param UploadUrl: 文件上传URL，用于文件上传时填写。
        :type UploadUrl: str
        :param BatchCnt: 量产数量，用于系统生成时填写。
        :type BatchCnt: int
        :param GenerationQRCode: 是否生成二维码,0为不生成，1为生成。
        :type GenerationQRCode: int
        """
        self.ProjectId = None
        self.ProductId = None
        self.BurnMethod = None
        self.GenerationMethod = None
        self.UploadUrl = None
        self.BatchCnt = None
        self.GenerationQRCode = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductId = params.get("ProductId")
        self.BurnMethod = params.get("BurnMethod")
        self.GenerationMethod = params.get("GenerationMethod")
        self.UploadUrl = params.get("UploadUrl")
        self.BatchCnt = params.get("BatchCnt")
        self.GenerationQRCode = params.get("GenerationQRCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchProductionResponse(AbstractModel):
    """CreateBatchProduction返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param BatchProductionId: 量产id
        :type BatchProductionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.ProductId = None
        self.BatchProductionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductId = params.get("ProductId")
        self.BatchProductionId = params.get("BatchProductionId")
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param DevAddr: LoRaWAN 设备地址
        :type DevAddr: str
        :param AppKey: LoRaWAN 应用密钥
        :type AppKey: str
        :param DevEUI: LoRaWAN 设备唯一标识
        :type DevEUI: str
        :param AppSKey: LoRaWAN 应用会话密钥
        :type AppSKey: str
        :param NwkSKey: LoRaWAN 网络会话密钥
        :type NwkSKey: str
        :param DefinedPsk: 手动指定设备的PSK密钥
        :type DefinedPsk: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DevAddr = None
        self.AppKey = None
        self.DevEUI = None
        self.AppSKey = None
        self.NwkSKey = None
        self.DefinedPsk = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DevAddr = params.get("DevAddr")
        self.AppKey = params.get("AppKey")
        self.DevEUI = params.get("DevEUI")
        self.AppSKey = params.get("AppSKey")
        self.NwkSKey = params.get("NwkSKey")
        self.DefinedPsk = params.get("DefinedPsk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 设备参数描述。
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DeviceData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateFenceBindRequest(AbstractModel):
    """CreateFenceBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param FenceId: 围栏Id
        :type FenceId: int
        :param Items: 围栏绑定的产品列表
        :type Items: list of FenceBindProductItem
        """
        self.FenceId = None
        self.Items = None


    def _deserialize(self, params):
        self.FenceId = params.get("FenceId")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFenceBindResponse(AbstractModel):
    """CreateFenceBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLoRaFrequencyRequest(AbstractModel):
    """CreateLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param FreqName: 频点配置名称
        :type FreqName: str
        :param ChannelsDataUp: 数据上行信道
        :type ChannelsDataUp: list of int non-negative
        :param ChannelsDataRX1: 数据下行RX1信道
        :type ChannelsDataRX1: list of int non-negative
        :param ChannelsDataRX2: 数据下行RX2信道
        :type ChannelsDataRX2: list of int non-negative
        :param ChannelsJoinUp: 入网上行信道
        :type ChannelsJoinUp: list of int non-negative
        :param ChannelsJoinRX1: 入网下行RX1信道
        :type ChannelsJoinRX1: list of int non-negative
        :param ChannelsJoinRX2: 入网下行RX2信道
        :type ChannelsJoinRX2: list of int non-negative
        :param Description: 频点配置描述
        :type Description: str
        """
        self.FreqName = None
        self.ChannelsDataUp = None
        self.ChannelsDataRX1 = None
        self.ChannelsDataRX2 = None
        self.ChannelsJoinUp = None
        self.ChannelsJoinRX1 = None
        self.ChannelsJoinRX2 = None
        self.Description = None


    def _deserialize(self, params):
        self.FreqName = params.get("FreqName")
        self.ChannelsDataUp = params.get("ChannelsDataUp")
        self.ChannelsDataRX1 = params.get("ChannelsDataRX1")
        self.ChannelsDataRX2 = params.get("ChannelsDataRX2")
        self.ChannelsJoinUp = params.get("ChannelsJoinUp")
        self.ChannelsJoinRX1 = params.get("ChannelsJoinRX1")
        self.ChannelsJoinRX2 = params.get("ChannelsJoinRX2")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoRaFrequencyResponse(AbstractModel):
    """CreateLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: LoRa频点信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = LoRaFrequencyEntry()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateLoRaGatewayRequest(AbstractModel):
    """CreateLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayId: LoRa 网关Id
        :type GatewayId: str
        :param Name: 网关名称
        :type Name: str
        :param Description: 详情描述
        :type Description: str
        :param Location: 位置坐标
        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        :param Position: 位置信息
        :type Position: str
        :param PositionDetails: 位置详情
        :type PositionDetails: str
        :param IsPublic: 是否公开
        :type IsPublic: bool
        :param FrequencyId: 频点ID
        :type FrequencyId: str
        """
        self.GatewayId = None
        self.Name = None
        self.Description = None
        self.Location = None
        self.Position = None
        self.PositionDetails = None
        self.IsPublic = None
        self.FrequencyId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Location") is not None:
            self.Location = LoRaGatewayLocation()
            self.Location._deserialize(params.get("Location"))
        self.Position = params.get("Position")
        self.PositionDetails = params.get("PositionDetails")
        self.IsPublic = params.get("IsPublic")
        self.FrequencyId = params.get("FrequencyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoRaGatewayResponse(AbstractModel):
    """CreateLoRaGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param Gateway: LoRa 网关信息
        :type Gateway: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Gateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Gateway") is not None:
            self.Gateway = LoRaGatewayItem()
            self.Gateway._deserialize(params.get("Gateway"))
        self.RequestId = params.get("RequestId")


class CreatePositionFenceRequest(AbstractModel):
    """CreatePositionFence请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param FenceName: 围栏名称
        :type FenceName: str
        :param FenceArea: 围栏区域信息，采用 GeoJSON 格式
        :type FenceArea: str
        :param FenceDesc: 围栏描述
        :type FenceDesc: str
        """
        self.SpaceId = None
        self.FenceName = None
        self.FenceArea = None
        self.FenceDesc = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.FenceName = params.get("FenceName")
        self.FenceArea = params.get("FenceArea")
        self.FenceDesc = params.get("FenceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePositionFenceResponse(AbstractModel):
    """CreatePositionFence返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePositionSpaceRequest(AbstractModel):
    """CreatePositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param SpaceName: 空间名称
        :type SpaceName: str
        :param AuthorizeType: 授权类型，0：只读 1：读写
        :type AuthorizeType: int
        :param ProductIdList: 产品列表
        :type ProductIdList: list of str
        :param Description: 描述
        :type Description: str
        :param Icon: 缩略图
        :type Icon: str
        """
        self.ProjectId = None
        self.SpaceName = None
        self.AuthorizeType = None
        self.ProductIdList = None
        self.Description = None
        self.Icon = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SpaceName = params.get("SpaceName")
        self.AuthorizeType = params.get("AuthorizeType")
        self.ProductIdList = params.get("ProductIdList")
        self.Description = params.get("Description")
        self.Icon = params.get("Icon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePositionSpaceResponse(AbstractModel):
    """CreatePositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 空间Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpaceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param InstanceId: 实例ID，不带实例ID，默认为公共实例
        :type InstanceId: str
        """
        self.ProjectName = None
        self.ProjectDesc = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Project: 返回信息
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class CreateStudioProductRequest(AbstractModel):
    """CreateStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param CategoryId: 产品分组模板ID , ( 自定义模板填写1 , 控制台调用会使用预置的其他ID)
        :type CategoryId: int
        :param ProductType: 产品类型 填写 ( 0 普通产品 )
        :type ProductType: int
        :param EncryptionType: 加密类型 加密类型，1表示证书认证，2表示签名认证。
        :type EncryptionType: str
        :param NetType: 连接类型 可以填写 wifi cellular else
        :type NetType: str
        :param DataProtocol: 数据协议 (1 使用物模型 2 为自定义)
        :type DataProtocol: int
        :param ProductDesc: 产品描述
        :type ProductDesc: str
        :param ProjectId: 产品的项目ID
        :type ProjectId: str
        """
        self.ProductName = None
        self.CategoryId = None
        self.ProductType = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.ProductType = params.get("ProductType")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStudioProductResponse(AbstractModel):
    """CreateStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 产品描述
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param TopicName: Topic名称
        :type TopicName: str
        :param Privilege: Topic权限，1发布，2订阅，3订阅和发布
        :type Privilege: int
        """
        self.ProductId = None
        self.TopicName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicPolicyResponse(AbstractModel):
    """CreateTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTopicRuleRequest(AbstractModel):
    """CreateTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        :param TopicRulePayload: 规则内容
        :type TopicRulePayload: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`
        """
        self.RuleName = None
        self.TopicRulePayload = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicRuleResponse(AbstractModel):
    """CreateTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。
        :type DeviceName: str
        :param ForceDelete: 是否删除绑定设备
        :type ForceDelete: bool
        """
        self.ProductId = None
        self.DeviceName = None
        self.ForceDelete = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ForceDelete = params.get("ForceDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCode = None
        self.ResultMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCode = params.get("ResultCode")
        self.ResultMessage = params.get("ResultMessage")
        self.RequestId = params.get("RequestId")


class DeleteDevicesRequest(AbstractModel):
    """DeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param DevicesItems: 多个设备标识
        :type DevicesItems: list of DevicesItem
        """
        self.DevicesItems = None


    def _deserialize(self, params):
        if params.get("DevicesItems") is not None:
            self.DevicesItems = []
            for item in params.get("DevicesItems"):
                obj = DevicesItem()
                obj._deserialize(item)
                self.DevicesItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDevicesResponse(AbstractModel):
    """DeleteDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCode = None
        self.ResultMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCode = params.get("ResultCode")
        self.ResultMessage = params.get("ResultMessage")
        self.RequestId = params.get("RequestId")


class DeleteFenceBindRequest(AbstractModel):
    """DeleteFenceBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param FenceId: 围栏Id
        :type FenceId: int
        :param Items: 围栏绑定的产品信息
        :type Items: list of FenceBindProductItem
        """
        self.FenceId = None
        self.Items = None


    def _deserialize(self, params):
        self.FenceId = params.get("FenceId")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFenceBindResponse(AbstractModel):
    """DeleteFenceBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoRaFrequencyRequest(AbstractModel):
    """DeleteLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param FreqId: 频点唯一ID
        :type FreqId: str
        """
        self.FreqId = None


    def _deserialize(self, params):
        self.FreqId = params.get("FreqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoRaFrequencyResponse(AbstractModel):
    """DeleteLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoRaGatewayRequest(AbstractModel):
    """DeleteLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayId: LoRa 网关 Id
        :type GatewayId: str
        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoRaGatewayResponse(AbstractModel):
    """DeleteLoRaGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePositionFenceRequest(AbstractModel):
    """DeletePositionFence请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param FenceId: 围栏Id
        :type FenceId: int
        """
        self.SpaceId = None
        self.FenceId = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.FenceId = params.get("FenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePositionFenceResponse(AbstractModel):
    """DeletePositionFence返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePositionSpaceRequest(AbstractModel):
    """DeletePositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        """
        self.SpaceId = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePositionSpaceResponse(AbstractModel):
    """DeletePositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStudioProductRequest(AbstractModel):
    """DeleteStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStudioProductResponse(AbstractModel):
    """DeleteStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicPolicyRequest(AbstractModel):
    """DeleteTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param TopicName: Topic名称
        :type TopicName: str
        """
        self.ProductId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicPolicyResponse(AbstractModel):
    """DeleteTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRuleRequest(AbstractModel):
    """DeleteTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicRuleResponse(AbstractModel):
    """DeleteTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBatchProductionRequest(AbstractModel):
    """DescribeBatchProduction请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param BatchProductionId: 量产ID
        :type BatchProductionId: str
        """
        self.ProductId = None
        self.BatchProductionId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.BatchProductionId = params.get("BatchProductionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchProductionResponse(AbstractModel):
    """DescribeBatchProduction返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchCnt: 量产数量。
        :type BatchCnt: int
        :param BurnMethod: 烧录方式。
        :type BurnMethod: int
        :param CreateTime: 创建时间。
        :type CreateTime: int
        :param DownloadUrl: 下载URL。
        :type DownloadUrl: str
        :param GenerationMethod: 生成方式。
        :type GenerationMethod: int
        :param UploadUrl: 上传URL。
        :type UploadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchCnt = None
        self.BurnMethod = None
        self.CreateTime = None
        self.DownloadUrl = None
        self.GenerationMethod = None
        self.UploadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchCnt = params.get("BatchCnt")
        self.BurnMethod = params.get("BurnMethod")
        self.CreateTime = params.get("CreateTime")
        self.DownloadUrl = params.get("DownloadUrl")
        self.GenerationMethod = params.get("GenerationMethod")
        self.UploadUrl = params.get("UploadUrl")
        self.RequestId = params.get("RequestId")


class DescribeBindedProductsRequest(AbstractModel):
    """DescribeBindedProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param Offset: 分页偏移量
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        """
        self.GatewayProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindedProductsResponse(AbstractModel):
    """DescribeBindedProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 当前分页的子产品数组
        :type Products: list of BindProductInfo
        :param Total: 绑定的子产品总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDeviceBindGatewayRequest(AbstractModel):
    """DescribeDeviceBindGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceBindGatewayResponse(AbstractModel):
    """DescribeDeviceBindGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备名
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayDeviceName: str
        :param GatewayName: 网关产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.GatewayName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.GatewayName = params.get("GatewayName")
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param MinTime: 区间开始时间（Unix 时间戳，毫秒级）
        :type MinTime: int
        :param MaxTime: 区间结束时间（Unix 时间戳，毫秒级）
        :type MaxTime: int
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
        :type FieldName: str
        :param Limit: 返回条数
        :type Limit: int
        :param Context: 检索上下文
        :type Context: str
        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.FieldName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FieldName = params.get("FieldName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FieldName = None
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 设备数据
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDevicePositionListRequest(AbstractModel):
    """DescribeDevicePositionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductIdList: 产品标识列表
        :type ProductIdList: list of str
        :param CoordinateType: 坐标类型
        :type CoordinateType: int
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小
        :type Limit: int
        """
        self.ProductIdList = None
        self.CoordinateType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductIdList = params.get("ProductIdList")
        self.CoordinateType = params.get("CoordinateType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePositionListResponse(AbstractModel):
    """DescribeDevicePositionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Positions: 产品设备位置信息列表
        :type Positions: list of ProductDevicesPositionItem
        :param Total: 产品设备位置信息的数目
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Positions = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Positions") is not None:
            self.Positions = []
            for item in params.get("Positions"):
                obj = ProductDevicesPositionItem()
                obj._deserialize(item)
                self.Positions.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Device: 设备信息
        :type Device: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = DeviceInfo()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class DescribeFenceBindListRequest(AbstractModel):
    """DescribeFenceBindList请求参数结构体

    """

    def __init__(self):
        r"""
        :param FenceId: 围栏Id
        :type FenceId: int
        :param Offset: 翻页偏移量，0起始
        :type Offset: int
        :param Limit: 最大返回结果数
        :type Limit: int
        """
        self.FenceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FenceId = params.get("FenceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFenceBindListResponse(AbstractModel):
    """DescribeFenceBindList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 围栏绑定的产品设备列表
        :type List: list of FenceBindProductItem
        :param Total: 围栏绑定的设备总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeFenceEventListRequest(AbstractModel):
    """DescribeFenceEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 围栏告警信息的查询起始时间，Unix时间，单位为毫秒
        :type StartTime: int
        :param EndTime: 围栏告警信息的查询结束时间，Unix时间，单位为毫秒
        :type EndTime: int
        :param FenceId: 围栏Id
        :type FenceId: int
        :param Offset: 翻页偏移量，0起始
        :type Offset: int
        :param Limit: 最大返回结果数
        :type Limit: int
        :param ProductId: 告警对应的产品Id
        :type ProductId: str
        :param DeviceName: 告警对应的设备名称
        :type DeviceName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.FenceId = None
        self.Offset = None
        self.Limit = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.FenceId = params.get("FenceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFenceEventListResponse(AbstractModel):
    """DescribeFenceEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 围栏告警事件列表
        :type List: list of FenceEventItem
        :param Total: 围栏告警事件总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = FenceEventItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskRequest(AbstractModel):
    """DescribeFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件任务ID
        :type TaskId: int
        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskResponse(AbstractModel):
    """DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 固件任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param Status: 固件任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 固件任务创建时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeMode: str
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Status = None
        self.CreateTime = None
        self.Type = None
        self.ProductName = None
        self.UpgradeMode = None
        self.ProductId = None
        self.OriginalVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Type = params.get("Type")
        self.ProductName = params.get("ProductName")
        self.UpgradeMode = params.get("UpgradeMode")
        self.ProductId = params.get("ProductId")
        self.OriginalVersion = params.get("OriginalVersion")
        self.RequestId = params.get("RequestId")


class DescribeGatewayBindDevicesRequest(AbstractModel):
    """DescribeGatewayBindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param ProductId: 子产品的ID
        :type ProductId: str
        :param Offset: 分页的偏移
        :type Offset: int
        :param Limit: 分页的页大小
        :type Limit: int
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayBindDevicesResponse(AbstractModel):
    """DescribeGatewayBindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param Devices: 子设备信息。
        :type Devices: list of BindDeviceInfo
        :param Total: 子设备总数。
        :type Total: int
        :param ProductName: 子设备所属的产品名。
        :type ProductName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.ProductName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = BindDeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.ProductName = params.get("ProductName")
        self.RequestId = params.get("RequestId")


class DescribeGatewaySubDeviceListRequest(AbstractModel):
    """DescribeGatewaySubDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备名称
        :type GatewayDeviceName: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小
        :type Limit: int
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewaySubDeviceListResponse(AbstractModel):
    """DescribeGatewaySubDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 设备的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param DeviceList: 设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: list of FamilySubDevice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.DeviceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DeviceList") is not None:
            self.DeviceList = []
            for item in params.get("DeviceList"):
                obj = FamilySubDevice()
                obj._deserialize(item)
                self.DeviceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGatewaySubProductsRequest(AbstractModel):
    """DescribeGatewaySubProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param Offset: 分页的偏移量
        :type Offset: int
        :param Limit: 分页的大小
        :type Limit: int
        :param ProjectId: 项目Id
        :type ProjectId: str
        """
        self.GatewayProductId = None
        self.Offset = None
        self.Limit = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewaySubProductsResponse(AbstractModel):
    """DescribeGatewaySubProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 当前分页的可绑定或解绑的产品信息。
        :type Products: list of BindProductInfo
        :param Total: 可绑定或解绑的产品总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeLoRaFrequencyRequest(AbstractModel):
    """DescribeLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param FreqId: 频点唯一ID
        :type FreqId: str
        """
        self.FreqId = None


    def _deserialize(self, params):
        self.FreqId = params.get("FreqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoRaFrequencyResponse(AbstractModel):
    """DescribeLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回详情项
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = LoRaFrequencyEntry()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        r"""
        :param Model: 产品数据模板
        :type Model: :class:`tencentcloud.iotexplorer.v20190423.models.ProductModelDefinition`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DescribePositionFenceListRequest(AbstractModel):
    """DescribePositionFenceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param Offset: 翻页偏移量，0起始
        :type Offset: int
        :param Limit: 最大返回结果数
        :type Limit: int
        """
        self.SpaceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePositionFenceListResponse(AbstractModel):
    """DescribePositionFenceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 围栏列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PositionFenceInfo
        :param Total: 围栏数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PositionFenceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Project: 返回信息
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntryEx`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntryEx()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class DescribeSpaceFenceEventListRequest(AbstractModel):
    """DescribeSpaceFenceEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param StartTime: 围栏告警信息的查询起始时间，Unix时间，单位为毫秒
        :type StartTime: int
        :param EndTime: 围栏告警信息的查询结束时间，Unix时间，单位为毫秒
        :type EndTime: int
        :param Offset: 翻页偏移量，0起始
        :type Offset: int
        :param Limit: 最大返回结果数
        :type Limit: int
        """
        self.SpaceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceFenceEventListResponse(AbstractModel):
    """DescribeSpaceFenceEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 围栏告警事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of FenceEventItem
        :param Total: 围栏告警事件总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = FenceEventItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeStudioProductRequest(AbstractModel):
    """DescribeStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStudioProductResponse(AbstractModel):
    """DescribeStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 产品详情
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DescribeTopicPolicyRequest(AbstractModel):
    """DescribeTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param TopicName: Topic名字
        :type TopicName: str
        """
        self.ProductId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicPolicyResponse(AbstractModel):
    """DescribeTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param TopicName: Topic名称
        :type TopicName: str
        :param Privilege: Topic权限
        :type Privilege: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductId = None
        self.TopicName = None
        self.Privilege = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")
        self.Privilege = params.get("Privilege")
        self.RequestId = params.get("RequestId")


class DescribeTopicRuleRequest(AbstractModel):
    """DescribeTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称。
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicRuleResponse(AbstractModel):
    """DescribeTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Rule: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = TopicRule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")


class DeviceData(AbstractModel):
    """DeviceData

    """

    def __init__(self):
        r"""
        :param DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param DeviceName: 设备名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevicePrivateKey: str
        :param DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevicePsk: str
        """
        self.DeviceCert = None
        self.DeviceName = None
        self.DevicePrivateKey = None
        self.DevicePsk = None


    def _deserialize(self, params):
        self.DeviceCert = params.get("DeviceCert")
        self.DeviceName = params.get("DeviceName")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.DevicePsk = params.get("DevicePsk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        r"""
        :param Time: 时间点，毫秒时间戳
        :type Time: str
        :param Value: 字段取值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Status: 0: 离线, 1: 在线, 2: 获取失败, 3 未激活
        :type Status: int
        :param DevicePsk: 设备密钥，密钥加密的设备返回
        :type DevicePsk: str
        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LoginTime: 最后一次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginTime: int
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param Version: 设备固件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param DeviceCert: 设备证书
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param LogLevel: 日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param DevAddr: LoRaWAN 设备地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DevAddr: str
        :param AppKey: LoRaWAN 应用密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param DevEUI: LoRaWAN 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DevEUI: str
        :param AppSKey: LoRaWAN 应用会话密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AppSKey: str
        :param NwkSKey: LoRaWAN 网络会话密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type NwkSKey: str
        :param CreateUserId: 创建人Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param CreatorNickName: 创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
        :param EnableState: 启用/禁用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param DeviceType: 设备类型（设备、子设备、网关）
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        """
        self.DeviceName = None
        self.Status = None
        self.DevicePsk = None
        self.FirstOnlineTime = None
        self.LoginTime = None
        self.CreateTime = None
        self.Version = None
        self.DeviceCert = None
        self.LogLevel = None
        self.DevAddr = None
        self.AppKey = None
        self.DevEUI = None
        self.AppSKey = None
        self.NwkSKey = None
        self.CreateUserId = None
        self.CreatorNickName = None
        self.EnableState = None
        self.ProductId = None
        self.ProductName = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.DevicePsk = params.get("DevicePsk")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LoginTime = params.get("LoginTime")
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")
        self.LogLevel = params.get("LogLevel")
        self.DevAddr = params.get("DevAddr")
        self.AppKey = params.get("AppKey")
        self.DevEUI = params.get("DevEUI")
        self.AppSKey = params.get("AppSKey")
        self.NwkSKey = params.get("NwkSKey")
        self.CreateUserId = params.get("CreateUserId")
        self.CreatorNickName = params.get("CreatorNickName")
        self.EnableState = params.get("EnableState")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePositionItem(AbstractModel):
    """设备位置详情

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param CreateTime: 位置信息时间
        :type CreateTime: int
        :param Longitude: 设备经度信息
        :type Longitude: float
        :param Latitude: 设备纬度信息
        :type Latitude: float
        """
        self.DeviceName = None
        self.CreateTime = None
        self.Longitude = None
        self.Latitude = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.CreateTime = params.get("CreateTime")
        self.Longitude = params.get("Longitude")
        self.Latitude = params.get("Latitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSignatureInfo(AbstractModel):
    """设备签名

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名
        :type DeviceName: str
        :param DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self.DeviceName = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUser(AbstractModel):
    """设备的用户

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param Role: 用户角色 1所有者，0：其他分享者
        :type Role: int
        """
        self.UserId = None
        self.Role = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesItem(AbstractModel):
    """ProductId -> DeviceName

    """

    def __init__(self):
        r"""
        :param ProductId: 产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectBindDeviceInFamilyRequest(AbstractModel):
    """DirectBindDeviceInFamily请求参数结构体

    """

    def __init__(self):
        r"""
        :param IotAppID: 小程序appid
        :type IotAppID: str
        :param UserID: 用户ID
        :type UserID: str
        :param FamilyId: 家庭ID
        :type FamilyId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param RoomId: 房间ID
        :type RoomId: str
        """
        self.IotAppID = None
        self.UserID = None
        self.FamilyId = None
        self.ProductId = None
        self.DeviceName = None
        self.RoomId = None


    def _deserialize(self, params):
        self.IotAppID = params.get("IotAppID")
        self.UserID = params.get("UserID")
        self.FamilyId = params.get("FamilyId")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectBindDeviceInFamilyResponse(AbstractModel):
    """DirectBindDeviceInFamily返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppDeviceInfo: 返回设备信息
        :type AppDeviceInfo: :class:`tencentcloud.iotexplorer.v20190423.models.AppDeviceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppDeviceInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDeviceInfo") is not None:
            self.AppDeviceInfo = AppDeviceInfo()
            self.AppDeviceInfo._deserialize(params.get("AppDeviceInfo"))
        self.RequestId = params.get("RequestId")


class DisableTopicRuleRequest(AbstractModel):
    """DisableTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableTopicRuleResponse(AbstractModel):
    """DisableTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableTopicRuleRequest(AbstractModel):
    """EnableTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableTopicRuleResponse(AbstractModel):
    """EnableTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        r"""
        :param TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self.TimeStamp = None
        self.ProductId = None
        self.DeviceName = None
        self.EventId = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.TimeStamp = params.get("TimeStamp")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EventId = params.get("EventId")
        self.Type = params.get("Type")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilySubDevice(AbstractModel):
    """子设备详情

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param AliasName: 设备别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param FamilyId: 设备绑定的家庭ID
        :type FamilyId: str
        :param RoomId: 设备所在的房间ID，默认"0"
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: str
        :param IconUrl: 图标
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param IconUrlGrid: grid图标
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrlGrid: str
        :param CreateTime: 设备绑定时间戳
        :type CreateTime: int
        :param UpdateTime: 设备更新时间戳
        :type UpdateTime: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceId = None
        self.AliasName = None
        self.FamilyId = None
        self.RoomId = None
        self.IconUrl = None
        self.IconUrlGrid = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceId = params.get("DeviceId")
        self.AliasName = params.get("AliasName")
        self.FamilyId = params.get("FamilyId")
        self.RoomId = params.get("RoomId")
        self.IconUrl = params.get("IconUrl")
        self.IconUrlGrid = params.get("IconUrlGrid")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceAlarmPoint(AbstractModel):
    """围栏告警位置点

    """

    def __init__(self):
        r"""
        :param AlarmTime: 围栏告警时间
        :type AlarmTime: int
        :param Longitude: 围栏告警位置的经度
        :type Longitude: float
        :param Latitude: 围栏告警位置的纬度
        :type Latitude: float
        """
        self.AlarmTime = None
        self.Longitude = None
        self.Latitude = None


    def _deserialize(self, params):
        self.AlarmTime = params.get("AlarmTime")
        self.Longitude = params.get("Longitude")
        self.Latitude = params.get("Latitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceBindDeviceItem(AbstractModel):
    """围栏绑定的设备信息

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param AlertCondition: 告警条件(In，进围栏报警；Out，出围栏报警；InOrOut，进围栏或者出围栏均报警)
        :type AlertCondition: str
        :param FenceEnable: 是否使能围栏(true，使能；false，禁用)
        :type FenceEnable: bool
        :param Method: 告警处理方法
        :type Method: str
        """
        self.DeviceName = None
        self.AlertCondition = None
        self.FenceEnable = None
        self.Method = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.AlertCondition = params.get("AlertCondition")
        self.FenceEnable = params.get("FenceEnable")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceBindProductItem(AbstractModel):
    """围栏绑定的产品信息

    """

    def __init__(self):
        r"""
        :param Devices: 围栏绑定的设备信息
        :type Devices: list of FenceBindDeviceItem
        :param ProductId: 围栏绑定的产品Id
        :type ProductId: str
        """
        self.Devices = None
        self.ProductId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = FenceBindDeviceItem()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceEventItem(AbstractModel):
    """围栏事件详情

    """

    def __init__(self):
        r"""
        :param ProductId: 围栏事件的产品Id
        :type ProductId: str
        :param DeviceName: 围栏事件的设备名称
        :type DeviceName: str
        :param FenceId: 围栏Id
        :type FenceId: int
        :param AlertType: 围栏事件的告警类型（In，进围栏报警；Out，出围栏报警；InOrOut，进围栏或者出围栏均报警）
        :type AlertType: str
        :param Data: 围栏事件的设备位置信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.FenceAlarmPoint`
        """
        self.ProductId = None
        self.DeviceName = None
        self.FenceId = None
        self.AlertType = None
        self.Data = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FenceId = params.get("FenceId")
        self.AlertType = params.get("AlertType")
        if params.get("Data") is not None:
            self.Data = FenceAlarmPoint()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        r"""
        :param Version: 固件版本
        :type Version: str
        :param Md5sum: 固件MD5值
        :type Md5sum: str
        :param CreateTime: 固件创建时间
        :type CreateTime: int
        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param FwType: 固件升级模块
注意：此字段可能返回 null，表示取不到有效值。
        :type FwType: str
        :param CreateUserId: 创建者子 uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param CreatorNickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
        """
        self.Version = None
        self.Md5sum = None
        self.CreateTime = None
        self.ProductName = None
        self.Name = None
        self.Description = None
        self.ProductId = None
        self.FwType = None
        self.CreateUserId = None
        self.CreatorNickName = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Md5sum = params.get("Md5sum")
        self.CreateTime = params.get("CreateTime")
        self.ProductName = params.get("ProductName")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ProductId = params.get("ProductId")
        self.FwType = params.get("FwType")
        self.CreateUserId = params.get("CreateUserId")
        self.CreatorNickName = params.get("CreatorNickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicRequest(AbstractModel):
    """GenSingleDeviceSignatureOfPublic请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 设备所属的产品ID
        :type ProductId: str
        :param DeviceName: 需要绑定的设备
        :type DeviceName: str
        :param Expire: 设备绑定签名的有效时间,以秒为单位。取值范围：0 < Expire <= 86400，Expire == -1（十年）
        :type Expire: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Expire = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicResponse(AbstractModel):
    """GenSingleDeviceSignatureOfPublic返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceSignature: 设备签名
        :type DeviceSignature: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceSignatureInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceSignature = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceSignature") is not None:
            self.DeviceSignature = DeviceSignatureInfo()
            self.DeviceSignature._deserialize(params.get("DeviceSignature"))
        self.RequestId = params.get("RequestId")


class GetBatchProductionsListRequest(AbstractModel):
    """GetBatchProductionsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量限制
        :type Limit: int
        """
        self.ProjectId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBatchProductionsListResponse(AbstractModel):
    """GetBatchProductionsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchProductions: 返回详情信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchProductions: list of BatchProductionInfo
        :param TotalCnt: 返回数量。
        :type TotalCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchProductions = None
        self.TotalCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BatchProductions") is not None:
            self.BatchProductions = []
            for item in params.get("BatchProductions"):
                obj = BatchProductionInfo()
                obj._deserialize(item)
                self.BatchProductions.append(obj)
        self.TotalCnt = params.get("TotalCnt")
        self.RequestId = params.get("RequestId")


class GetCOSURLRequest(AbstractModel):
    """GetCOSURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param FileSize: 文件大小
        :type FileSize: int
        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.FileSize = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCOSURLResponse(AbstractModel):
    """GetCOSURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 固件URL
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class GetDeviceListRequest(AbstractModel):
    """GetDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 需要查看设备列表的产品ID, -1代表ProjectId来筛选
        :type ProductId: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-100
        :type Limit: int
        :param FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :type FirmwareVersion: str
        :param DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        :param ProjectId: 项目ID。产品 ID 为 -1 时，该参数必填
        :type ProjectId: str
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.FirmwareVersion = None
        self.DeviceName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.DeviceName = params.get("DeviceName")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceListResponse(AbstractModel):
    """GetDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Devices: 返回的设备列表, 注意列表设备的 DevicePsk 为空, 要获取设备的 DevicePsk 请使用 DescribeDevice
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceInfo
        :param Total: 产品下的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetDeviceLocationHistoryRequest(AbstractModel):
    """GetDeviceLocationHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param StartTime: 查询起始时间，Unix时间，单位为毫秒
        :type StartTime: int
        :param EndTime: 查询结束时间，Unix时间，单位为毫秒
        :type EndTime: int
        :param CoordinateType: 坐标类型
        :type CoordinateType: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.StartTime = None
        self.EndTime = None
        self.CoordinateType = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CoordinateType = params.get("CoordinateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLocationHistoryResponse(AbstractModel):
    """GetDeviceLocationHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Positions: 历史位置列表
        :type Positions: list of PositionItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Positions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Positions") is not None:
            self.Positions = []
            for item in params.get("Positions"):
                obj = PositionItem()
                obj._deserialize(item)
                self.Positions.append(obj)
        self.RequestId = params.get("RequestId")


class GetFamilyDeviceUserListRequest(AbstractModel):
    """GetFamilyDeviceUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFamilyDeviceUserListResponse(AbstractModel):
    """GetFamilyDeviceUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserList: 设备的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of DeviceUser
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = DeviceUser()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class GetGatewaySubDeviceListRequest(AbstractModel):
    """GetGatewaySubDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备名称
        :type GatewayDeviceName: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小
        :type Limit: int
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGatewaySubDeviceListResponse(AbstractModel):
    """GetGatewaySubDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 设备的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param DeviceList: 设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: :class:`tencentcloud.iotexplorer.v20190423.models.FamilySubDevice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.DeviceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DeviceList") is not None:
            self.DeviceList = FamilySubDevice()
            self.DeviceList._deserialize(params.get("DeviceList"))
        self.RequestId = params.get("RequestId")


class GetLoRaGatewayListRequest(AbstractModel):
    """GetLoRaGatewayList请求参数结构体

    """

    def __init__(self):
        r"""
        :param IsCommunity: 是否是社区网关
        :type IsCommunity: bool
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制个数
        :type Limit: int
        """
        self.IsCommunity = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.IsCommunity = params.get("IsCommunity")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLoRaGatewayListResponse(AbstractModel):
    """GetLoRaGatewayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回总数
        :type Total: int
        :param Gateways: 返回详情项
注意：此字段可能返回 null，表示取不到有效值。
        :type Gateways: list of LoRaGatewayItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Gateways = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Gateways") is not None:
            self.Gateways = []
            for item in params.get("Gateways"):
                obj = LoRaGatewayItem()
                obj._deserialize(item)
                self.Gateways.append(obj)
        self.RequestId = params.get("RequestId")


class GetPositionSpaceListRequest(AbstractModel):
    """GetPositionSpaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param Offset: 翻页偏移量，0起始
        :type Offset: int
        :param Limit: 最大返回结果数
        :type Limit: int
        """
        self.ProjectId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPositionSpaceListResponse(AbstractModel):
    """GetPositionSpaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 位置空间列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PositionSpaceInfo
        :param Total: 位置空间数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PositionSpaceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetProjectListRequest(AbstractModel):
    """GetProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 个数限制
        :type Limit: int
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProjectId: 按项目ID搜索
        :type ProjectId: str
        :param ProductId: 按产品ID搜索
        :type ProductId: str
        :param Includes: 加载 ProductCount、DeviceCount、ApplicationCount，可选值：ProductCount、DeviceCount、ApplicationCount，可多选
        :type Includes: list of str
        :param ProjectName: 按项目名称搜索
        :type ProjectName: str
        """
        self.Offset = None
        self.Limit = None
        self.InstanceId = None
        self.ProjectId = None
        self.ProductId = None
        self.Includes = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")
        self.ProjectId = params.get("ProjectId")
        self.ProductId = params.get("ProductId")
        self.Includes = params.get("Includes")
        self.ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProjectListResponse(AbstractModel):
    """GetProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Projects: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Projects: list of ProjectEntryEx
        :param Total: 列表项个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = ProjectEntryEx()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetStudioProductListRequest(AbstractModel):
    """GetStudioProductList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DevStatus: 产品DevStatus
        :type DevStatus: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        """
        self.ProjectId = None
        self.DevStatus = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DevStatus = params.get("DevStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStudioProductListResponse(AbstractModel):
    """GetStudioProductList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 产品列表
        :type Products: list of ProductEntry
        :param Total: 产品数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetTopicRuleListRequest(AbstractModel):
    """GetTopicRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNum: 请求的页数
        :type PageNum: int
        :param PageSize: 分页的大小
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicRuleListResponse(AbstractModel):
    """GetTopicRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCnt: 规则总数量
        :type TotalCnt: int
        :param Rules: 规则列表
        :type Rules: list of TopicRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCnt = None
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = TopicRuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class ListEventHistoryRequest(AbstractModel):
    """ListEventHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件
        :type Type: str
        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param Size: 单次获取的历史数据项目的最大数量, 缺省10
        :type Size: int
        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None
        self.EventId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Context = params.get("Context")
        self.Size = params.get("Size")
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventHistoryResponse(AbstractModel):
    """ListEventHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Total = None
        self.Listover = None
        self.EventHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Total = params.get("Total")
        self.Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self.EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self.EventHistory.append(obj)
        self.RequestId = params.get("RequestId")


class ListFirmwaresRequest(AbstractModel):
    """ListFirmwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNum: 获取的页数
        :type PageNum: int
        :param PageSize: 分页的大小
        :type PageSize: int
        :param ProductID: 产品ID
        :type ProductID: str
        :param Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self.PageNum = None
        self.PageSize = None
        self.ProductID = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.ProductID = params.get("ProductID")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFirmwaresResponse(AbstractModel):
    """ListFirmwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 固件总数
        :type TotalCount: int
        :param Firmwares: 固件列表
        :type Firmwares: list of FirmwareInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Firmwares = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Firmwares") is not None:
            self.Firmwares = []
            for item in params.get("Firmwares"):
                obj = FirmwareInfo()
                obj._deserialize(item)
                self.Firmwares.append(obj)
        self.RequestId = params.get("RequestId")


class ListTopicPolicyRequest(AbstractModel):
    """ListTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopicPolicyResponse(AbstractModel):
    """ListTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Topics: Topic列表
        :type Topics: list of TopicItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = TopicItem()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")


class LoRaFrequencyEntry(AbstractModel):
    """LoRa自定义频点信息

    """

    def __init__(self):
        r"""
        :param FreqId: 频点唯一ID
        :type FreqId: str
        :param FreqName: 频点名称
        :type FreqName: str
        :param Description: 频点描述
        :type Description: str
        :param ChannelsDataUp: 数据上行信道
        :type ChannelsDataUp: list of int non-negative
        :param ChannelsDataRX1: 数据下行信道RX1
        :type ChannelsDataRX1: list of int non-negative
        :param ChannelsDataRX2: 数据下行信道RX2
        :type ChannelsDataRX2: list of int non-negative
        :param ChannelsJoinUp: 入网上行信道
        :type ChannelsJoinUp: list of int non-negative
        :param ChannelsJoinRX1: 入网下行RX1信道
        :type ChannelsJoinRX1: list of int non-negative
        :param ChannelsJoinRX2: 入网下行RX2信道
        :type ChannelsJoinRX2: list of int non-negative
        :param CreateTime: 创建时间
        :type CreateTime: int
        """
        self.FreqId = None
        self.FreqName = None
        self.Description = None
        self.ChannelsDataUp = None
        self.ChannelsDataRX1 = None
        self.ChannelsDataRX2 = None
        self.ChannelsJoinUp = None
        self.ChannelsJoinRX1 = None
        self.ChannelsJoinRX2 = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.FreqId = params.get("FreqId")
        self.FreqName = params.get("FreqName")
        self.Description = params.get("Description")
        self.ChannelsDataUp = params.get("ChannelsDataUp")
        self.ChannelsDataRX1 = params.get("ChannelsDataRX1")
        self.ChannelsDataRX2 = params.get("ChannelsDataRX2")
        self.ChannelsJoinUp = params.get("ChannelsJoinUp")
        self.ChannelsJoinRX1 = params.get("ChannelsJoinRX1")
        self.ChannelsJoinRX2 = params.get("ChannelsJoinRX2")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoRaGatewayItem(AbstractModel):
    """LoRa 网关信息

    """

    def __init__(self):
        r"""
        :param GatewayId: LoRa 网关Id
        :type GatewayId: str
        :param IsPublic: 是否是公开网关
        :type IsPublic: bool
        :param Description: 网关描述
        :type Description: str
        :param Name: 网关名称
        :type Name: str
        :param Position: 网关位置信息
        :type Position: str
        :param PositionDetails: 网关位置详情
        :type PositionDetails: str
        :param Location: LoRa 网关位置坐标
        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        :param UpdatedAt: 最后更新时间
        :type UpdatedAt: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param LastSeenAt: 最后上报时间
        :type LastSeenAt: str
        :param FrequencyId: 频点ID
        :type FrequencyId: str
        """
        self.GatewayId = None
        self.IsPublic = None
        self.Description = None
        self.Name = None
        self.Position = None
        self.PositionDetails = None
        self.Location = None
        self.UpdatedAt = None
        self.CreatedAt = None
        self.LastSeenAt = None
        self.FrequencyId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.IsPublic = params.get("IsPublic")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Position = params.get("Position")
        self.PositionDetails = params.get("PositionDetails")
        if params.get("Location") is not None:
            self.Location = LoRaGatewayLocation()
            self.Location._deserialize(params.get("Location"))
        self.UpdatedAt = params.get("UpdatedAt")
        self.CreatedAt = params.get("CreatedAt")
        self.LastSeenAt = params.get("LastSeenAt")
        self.FrequencyId = params.get("FrequencyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoRaGatewayLocation(AbstractModel):
    """网关坐标

    """

    def __init__(self):
        r"""
        :param Latitude: 纬度
        :type Latitude: float
        :param Longitude: 精度
        :type Longitude: float
        :param Accuracy: 准确度
        :type Accuracy: float
        :param Altitude: 海拔
        :type Altitude: float
        """
        self.Latitude = None
        self.Longitude = None
        self.Accuracy = None
        self.Altitude = None


    def _deserialize(self, params):
        self.Latitude = params.get("Latitude")
        self.Longitude = params.get("Longitude")
        self.Accuracy = params.get("Accuracy")
        self.Altitude = params.get("Altitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFenceBindRequest(AbstractModel):
    """ModifyFenceBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param FenceId: 围栏Id
        :type FenceId: int
        :param Items: 围栏绑定的产品列表
        :type Items: list of FenceBindProductItem
        """
        self.FenceId = None
        self.Items = None


    def _deserialize(self, params):
        self.FenceId = params.get("FenceId")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFenceBindResponse(AbstractModel):
    """ModifyFenceBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoRaFrequencyRequest(AbstractModel):
    """ModifyLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param FreqId: 频点唯一ID
        :type FreqId: str
        :param FreqName: 频点名称
        :type FreqName: str
        :param Description: 频点描述
        :type Description: str
        :param ChannelsDataUp: 数据上行信道
        :type ChannelsDataUp: list of int non-negative
        :param ChannelsDataRX1: 数据下行信道RX1
        :type ChannelsDataRX1: list of int non-negative
        :param ChannelsDataRX2: 数据下行信道RX2
        :type ChannelsDataRX2: list of int non-negative
        :param ChannelsJoinUp: 入网上行信道
        :type ChannelsJoinUp: list of int non-negative
        :param ChannelsJoinRX1: 入网下行信道RX1
        :type ChannelsJoinRX1: list of int non-negative
        :param ChannelsJoinRX2: 入网下行信道RX2
        :type ChannelsJoinRX2: list of int non-negative
        """
        self.FreqId = None
        self.FreqName = None
        self.Description = None
        self.ChannelsDataUp = None
        self.ChannelsDataRX1 = None
        self.ChannelsDataRX2 = None
        self.ChannelsJoinUp = None
        self.ChannelsJoinRX1 = None
        self.ChannelsJoinRX2 = None


    def _deserialize(self, params):
        self.FreqId = params.get("FreqId")
        self.FreqName = params.get("FreqName")
        self.Description = params.get("Description")
        self.ChannelsDataUp = params.get("ChannelsDataUp")
        self.ChannelsDataRX1 = params.get("ChannelsDataRX1")
        self.ChannelsDataRX2 = params.get("ChannelsDataRX2")
        self.ChannelsJoinUp = params.get("ChannelsJoinUp")
        self.ChannelsJoinRX1 = params.get("ChannelsJoinRX1")
        self.ChannelsJoinRX2 = params.get("ChannelsJoinRX2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoRaFrequencyResponse(AbstractModel):
    """ModifyLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 频点信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = LoRaFrequencyEntry()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyLoRaGatewayRequest(AbstractModel):
    """ModifyLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param Description: 描述信息
        :type Description: str
        :param GatewayId: LoRa网关Id
        :type GatewayId: str
        :param Location: LoRa网关位置坐标
        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        :param Name: LoRa网关名称
        :type Name: str
        :param IsPublic: 是否公开可见
        :type IsPublic: bool
        :param Position: 位置信息
        :type Position: str
        :param PositionDetails: 位置详情
        :type PositionDetails: str
        :param FrequencyId: 频点ID
        :type FrequencyId: str
        """
        self.Description = None
        self.GatewayId = None
        self.Location = None
        self.Name = None
        self.IsPublic = None
        self.Position = None
        self.PositionDetails = None
        self.FrequencyId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.GatewayId = params.get("GatewayId")
        if params.get("Location") is not None:
            self.Location = LoRaGatewayLocation()
            self.Location._deserialize(params.get("Location"))
        self.Name = params.get("Name")
        self.IsPublic = params.get("IsPublic")
        self.Position = params.get("Position")
        self.PositionDetails = params.get("PositionDetails")
        self.FrequencyId = params.get("FrequencyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoRaGatewayResponse(AbstractModel):
    """ModifyLoRaGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param Gateway: 返回网关数据
        :type Gateway: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Gateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Gateway") is not None:
            self.Gateway = LoRaGatewayItem()
            self.Gateway._deserialize(params.get("Gateway"))
        self.RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPositionFenceRequest(AbstractModel):
    """ModifyPositionFence请求参数结构体

    """


class ModifyPositionFenceResponse(AbstractModel):
    """ModifyPositionFence返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPositionSpaceRequest(AbstractModel):
    """ModifyPositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param SpaceName: 位置空间名称
        :type SpaceName: str
        :param AuthorizeType: 授权类型
        :type AuthorizeType: int
        :param ProductIdList: 产品列表
        :type ProductIdList: list of str
        :param Description: 位置空间描述
        :type Description: str
        :param Icon: 缩略图
        :type Icon: str
        """
        self.SpaceId = None
        self.SpaceName = None
        self.AuthorizeType = None
        self.ProductIdList = None
        self.Description = None
        self.Icon = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.SpaceName = params.get("SpaceName")
        self.AuthorizeType = params.get("AuthorizeType")
        self.ProductIdList = params.get("ProductIdList")
        self.Description = params.get("Description")
        self.Icon = params.get("Icon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPositionSpaceResponse(AbstractModel):
    """ModifyPositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Project: 项目详情
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class ModifySpacePropertyRequest(AbstractModel):
    """ModifySpaceProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param Data: 产品属性
        :type Data: str
        """
        self.SpaceId = None
        self.ProductId = None
        self.Data = None


    def _deserialize(self, params):
        self.SpaceId = params.get("SpaceId")
        self.ProductId = params.get("ProductId")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySpacePropertyResponse(AbstractModel):
    """ModifySpaceProperty返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStudioProductRequest(AbstractModel):
    """ModifyStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductDesc: 产品描述
        :type ProductDesc: str
        :param ModuleId: 模型ID
        :type ModuleId: int
        :param EnableProductScript: 是否打开二进制转Json功能, 取值为字符串 true/false
        :type EnableProductScript: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDesc = None
        self.ModuleId = None
        self.EnableProductScript = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDesc = params.get("ProductDesc")
        self.ModuleId = params.get("ModuleId")
        self.EnableProductScript = params.get("EnableProductScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStudioProductResponse(AbstractModel):
    """ModifyStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 产品描述
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class ModifyTopicPolicyRequest(AbstractModel):
    """ModifyTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param TopicName: 更新前Topic名
        :type TopicName: str
        :param NewTopicName: 更新后Topic名
        :type NewTopicName: str
        :param Privilege: Topic权限
        :type Privilege: int
        """
        self.ProductId = None
        self.TopicName = None
        self.NewTopicName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")
        self.NewTopicName = params.get("NewTopicName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicPolicyResponse(AbstractModel):
    """ModifyTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicRuleRequest(AbstractModel):
    """ModifyTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        :param TopicRulePayload: 替换的规则包体
        :type TopicRulePayload: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`
        """
        self.RuleName = None
        self.TopicRulePayload = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicRuleResponse(AbstractModel):
    """ModifyTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PositionFenceInfo(AbstractModel):
    """围栏详细信息(包含创建时间及更新时间)

    """

    def __init__(self):
        r"""
        :param GeoFence: 围栏信息
        :type GeoFence: :class:`tencentcloud.iotexplorer.v20190423.models.PositionFenceItem`
        :param CreateTime: 围栏创建时间
        :type CreateTime: int
        :param UpdateTime: 围栏更新时间
        :type UpdateTime: int
        """
        self.GeoFence = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        if params.get("GeoFence") is not None:
            self.GeoFence = PositionFenceItem()
            self.GeoFence._deserialize(params.get("GeoFence"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionFenceItem(AbstractModel):
    """围栏信息

    """

    def __init__(self):
        r"""
        :param FenceId: 围栏Id
        :type FenceId: int
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param FenceName: 围栏名称
        :type FenceName: str
        :param FenceDesc: 围栏描述
        :type FenceDesc: str
        :param FenceArea: 围栏区域信息，采用 GeoJSON 格式
        :type FenceArea: str
        """
        self.FenceId = None
        self.SpaceId = None
        self.FenceName = None
        self.FenceDesc = None
        self.FenceArea = None


    def _deserialize(self, params):
        self.FenceId = params.get("FenceId")
        self.SpaceId = params.get("SpaceId")
        self.FenceName = params.get("FenceName")
        self.FenceDesc = params.get("FenceDesc")
        self.FenceArea = params.get("FenceArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionItem(AbstractModel):
    """位置点

    """

    def __init__(self):
        r"""
        :param CreateTime: 位置点的时间
        :type CreateTime: int
        :param Longitude: 位置点的经度
        :type Longitude: float
        :param Latitude: 位置点的纬度
        :type Latitude: float
        :param LocationType: 位置点的定位类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationType: str
        :param Accuracy: 位置点的精度预估，单位为米
注意：此字段可能返回 null，表示取不到有效值。
        :type Accuracy: float
        """
        self.CreateTime = None
        self.Longitude = None
        self.Latitude = None
        self.LocationType = None
        self.Accuracy = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.Longitude = params.get("Longitude")
        self.Latitude = params.get("Latitude")
        self.LocationType = params.get("LocationType")
        self.Accuracy = params.get("Accuracy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionSpaceInfo(AbstractModel):
    """位置空间详情

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param SpaceId: 位置空间Id
        :type SpaceId: str
        :param SpaceName: 位置空间名称
        :type SpaceName: str
        :param AuthorizeType: 授权类型
        :type AuthorizeType: int
        :param Description: 描述备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param ProductIdList: 产品列表
        :type ProductIdList: list of str
        :param Icon: 缩略图
        :type Icon: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        :param Zoom: 用户自定义地图缩放
        :type Zoom: int
        """
        self.ProjectId = None
        self.SpaceId = None
        self.SpaceName = None
        self.AuthorizeType = None
        self.Description = None
        self.ProductIdList = None
        self.Icon = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Zoom = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SpaceId = params.get("SpaceId")
        self.SpaceName = params.get("SpaceName")
        self.AuthorizeType = params.get("AuthorizeType")
        self.Description = params.get("Description")
        self.ProductIdList = params.get("ProductIdList")
        self.Icon = params.get("Icon")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Zoom = params.get("Zoom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductDevicesPositionItem(AbstractModel):
    """产品设备位置信息

    """

    def __init__(self):
        r"""
        :param Items: 设备位置列表
        :type Items: list of DevicePositionItem
        :param ProductId: 产品标识
        :type ProductId: str
        :param Total: 设备位置数量
        :type Total: int
        """
        self.Items = None
        self.ProductId = None
        self.Total = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DevicePositionItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.ProductId = params.get("ProductId")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductEntry(AbstractModel):
    """产品详情

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param CategoryId: 产品分组模板ID
        :type CategoryId: int
        :param EncryptionType: 加密类型
        :type EncryptionType: str
        :param NetType: 连接类型
        :type NetType: str
        :param DataProtocol: 数据协议
        :type DataProtocol: int
        :param ProductDesc: 产品描述
        :type ProductDesc: str
        :param DevStatus: 状态
        :type DevStatus: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        :param Region: 区域
        :type Region: str
        :param ProductType: 产品类型
        :type ProductType: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ModuleId: 产品ModuleId
        :type ModuleId: int
        :param EnableProductScript: 是否使用脚本进行二进制转json功能 可以取值 true / false
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableProductScript: str
        :param CreateUserId: 创建人 UinId
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param CreatorNickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
        """
        self.ProductId = None
        self.ProductName = None
        self.CategoryId = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.DevStatus = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Region = None
        self.ProductType = None
        self.ProjectId = None
        self.ModuleId = None
        self.EnableProductScript = None
        self.CreateUserId = None
        self.CreatorNickName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.DevStatus = params.get("DevStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.ProjectId = params.get("ProjectId")
        self.ModuleId = params.get("ModuleId")
        self.EnableProductScript = params.get("EnableProductScript")
        self.CreateUserId = params.get("CreateUserId")
        self.CreatorNickName = params.get("CreatorNickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelDefine: 模型定义
        :type ModelDefine: str
        :param UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        :param CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        :param NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypeModel: str
        """
        self.ProductId = None
        self.ModelDefine = None
        self.UpdateTime = None
        self.CreateTime = None
        self.CategoryModel = None
        self.NetTypeModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelDefine = params.get("ModelDefine")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.CategoryModel = params.get("CategoryModel")
        self.NetTypeModel = params.get("NetTypeModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectEntry(AbstractModel):
    """项目详情

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param CreateTime: 创建时间，unix时间戳
        :type CreateTime: int
        :param UpdateTime: 更新时间，unix时间戳
        :type UpdateTime: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectEntryEx(AbstractModel):
    """项目详情

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param CreateTime: 项目创建时间，unix时间戳
        :type CreateTime: int
        :param UpdateTime: 项目更新时间，unix时间戳
        :type UpdateTime: int
        :param ProductCount: 产品数量
        :type ProductCount: int
        :param NativeAppCount: NativeApp数量
        :type NativeAppCount: int
        :param WebAppCount: WebApp数量
        :type WebAppCount: int
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ApplicationCount: 应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationCount: int
        :param DeviceCount: 设备注册总数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCount: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ProductCount = None
        self.NativeAppCount = None
        self.WebAppCount = None
        self.InstanceId = None
        self.ApplicationCount = None
        self.DeviceCount = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ProductCount = params.get("ProductCount")
        self.NativeAppCount = params.get("NativeAppCount")
        self.WebAppCount = params.get("WebAppCount")
        self.InstanceId = params.get("InstanceId")
        self.ApplicationCount = params.get("ApplicationCount")
        self.DeviceCount = params.get("DeviceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishBroadcastMessageRequest(AbstractModel):
    """PublishBroadcastMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param Payload: 消息内容
        :type Payload: str
        :param Qos: 消息质量等级
        :type Qos: int
        :param PayloadEncoding: ayload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
        :type PayloadEncoding: str
        """
        self.ProductId = None
        self.Payload = None
        self.Qos = None
        self.PayloadEncoding = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Payload = params.get("Payload")
        self.Qos = params.get("Qos")
        self.PayloadEncoding = params.get("PayloadEncoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishBroadcastMessageResponse(AbstractModel):
    """PublishBroadcastMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 广播消息任务Id
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Topic: 消息发往的主题
        :type Topic: str
        :param Payload: 云端下发到设备的控制报文
        :type Payload: str
        :param Qos: 消息服务质量等级，取值为0或1
        :type Qos: int
        :param PayloadEncoding: Payload的内容编码格式，取值为base64或空。base64表示云端将接收到的base64编码后的报文再转换成二进制报文下发至设备，为空表示不作转换，透传下发至设备
        :type PayloadEncoding: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Topic = None
        self.Payload = None
        self.Qos = None
        self.PayloadEncoding = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.Qos = params.get("Qos")
        self.PayloadEncoding = params.get("PayloadEncoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PublishRRPCMessageRequest(AbstractModel):
    """PublishRRPCMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Payload: 消息内容，utf8编码
        :type Payload: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishRRPCMessageResponse(AbstractModel):
    """PublishRRPCMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param MessageId: RRPC消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: int
        :param PayloadBase64: 设备回复的消息内容，采用base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type PayloadBase64: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MessageId = None
        self.PayloadBase64 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.PayloadBase64 = params.get("PayloadBase64")
        self.RequestId = params.get("RequestId")


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DevStatus: 产品DevStatus
        :type DevStatus: str
        """
        self.ProductId = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DevStatus = params.get("DevStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseStudioProductResponse(AbstractModel):
    """ReleaseStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchKeyword(AbstractModel):
    """搜索关键词

    """

    def __init__(self):
        r"""
        :param Key: 搜索条件的Key
        :type Key: str
        :param Value: 搜索条件的值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPositionSpaceRequest(AbstractModel):
    """SearchPositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: str
        :param SpaceName: 位置空间名字
        :type SpaceName: str
        :param Offset: 偏移量，从0开始
        :type Offset: int
        :param Limit: 最大获取数量
        :type Limit: int
        """
        self.ProjectId = None
        self.SpaceName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SpaceName = params.get("SpaceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPositionSpaceResponse(AbstractModel):
    """SearchPositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 位置空间列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PositionSpaceInfo
        :param Total: 符合条件的位置空间个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PositionSpaceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param Limit: 列表Limit
        :type Limit: int
        :param Offset: 列表Offset
        :type Offset: int
        :param DevStatus: 产品Status
        :type DevStatus: str
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProjectId = None
        self.ProductName = None
        self.Limit = None
        self.Offset = None
        self.DevStatus = None
        self.ProductId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductName = params.get("ProductName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DevStatus = params.get("DevStatus")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchStudioProductResponse(AbstractModel):
    """SearchStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 产品列表
        :type Products: list of ProductEntry
        :param Total: 产品数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class SearchTopicRuleRequest(AbstractModel):
    """SearchTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTopicRuleResponse(AbstractModel):
    """SearchTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCnt: 搜索到的规则总数
        :type TotalCnt: int
        :param Rules: 规则信息列表
        :type Rules: list of TopicRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCnt = None
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = TopicRuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class TopicItem(AbstractModel):
    """Topic信息, 包括Topic名字和权限

    """

    def __init__(self):
        r"""
        :param TopicName: Topic名称
        :type TopicName: str
        :param Privilege: Topic权限 , 1上报  2下发
        :type Privilege: int
        """
        self.TopicName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRule(AbstractModel):
    """TopicRule结构

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称。
        :type RuleName: str
        :param Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param Description: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Actions: 行为的JSON字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: str
        :param RuleDisabled: 是否禁用规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDisabled: bool
        """
        self.RuleName = None
        self.Sql = None
        self.Description = None
        self.Actions = None
        self.RuleDisabled = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Sql = params.get("Sql")
        self.Description = params.get("Description")
        self.Actions = params.get("Actions")
        self.RuleDisabled = params.get("RuleDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        :param Description: 规则描述
        :type Description: str
        :param CreatedAt: 创建时间
        :type CreatedAt: int
        :param RuleDisabled: 规则是否禁用
        :type RuleDisabled: bool
        """
        self.RuleName = None
        self.Description = None
        self.CreatedAt = None
        self.RuleDisabled = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Description = params.get("Description")
        self.CreatedAt = params.get("CreatedAt")
        self.RuleDisabled = params.get("RuleDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRulePayload(AbstractModel):
    """TopicRulePayload结构

    """

    def __init__(self):
        r"""
        :param Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param Actions: 行为的JSON字符串，大部分种类举例如下：
[
{
"republish": {
"topic": "TEST/test"
}
},
{
"forward": {
"api": "http://test.com:8080"
}
},
{
"ckafka": {
"instance": {
"id": "ckafka-test",
"name": ""
},
"topic": {
"id": "topic-test",
"name": "test"
},
"region": "gz"
}
},
{
"cmqqueue": {
"queuename": "queue-test-TEST",
"region": "gz"
}
},
{
"mysql": {
"instanceid": "cdb-test",
"region": "gz",
"username": "test",
"userpwd": "*****",
"dbname": "d_mqtt",
"tablename": "t_test",
"fieldpairs": [
{
"field": "test",
"value": "test"
}
],
"devicetype": "CUSTOM"
}
}
]
        :type Actions: str
        :param Description: 规则描述
        :type Description: str
        :param RuleDisabled: 是否禁用规则
        :type RuleDisabled: bool
        """
        self.Sql = None
        self.Actions = None
        self.Description = None
        self.RuleDisabled = None


    def _deserialize(self, params):
        self.Sql = params.get("Sql")
        self.Actions = params.get("Actions")
        self.Description = params.get("Description")
        self.RuleDisabled = params.get("RuleDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDevicesRequest(AbstractModel):
    """UnbindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceNames: 设备名列表
        :type DeviceNames: list of str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDevicesResponse(AbstractModel):
    """UnbindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindProductsRequest(AbstractModel):
    """UnbindProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param ProductIds: 待解绑的子产品ID数组
        :type ProductIds: list of str
        """
        self.GatewayProductId = None
        self.ProductIds = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindProductsResponse(AbstractModel):
    """UnbindProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayDeviceNames: 绑定了待解绑的LoRa产品下的设备的网关设备列表
        :type GatewayDeviceNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GatewayDeviceNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GatewayDeviceNames = params.get("GatewayDeviceNames")
        self.RequestId = params.get("RequestId")


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState请求参数结构体

    """

    def __init__(self):
        r"""
        :param DevicesItems: 多个设备标识
        :type DevicesItems: list of DevicesItem
        :param Status: 1：启用；0：禁用
        :type Status: int
        """
        self.DevicesItems = None
        self.Status = None


    def _deserialize(self, params):
        if params.get("DevicesItems") is not None:
            self.DevicesItems = []
            for item in params.get("DevicesItems"):
                obj = DevicesItem()
                obj._deserialize(item)
                self.DevicesItems.append(obj)
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicesEnableStateResponse(AbstractModel):
    """UpdateDevicesEnableState返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCode = None
        self.ResultMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCode = params.get("ResultCode")
        self.ResultMessage = params.get("ResultMessage")
        self.RequestId = params.get("RequestId")


class UpdateFirmwareRequest(AbstractModel):
    """UpdateFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param FirmwareVersion: 固件新的版本号
        :type FirmwareVersion: str
        :param FirmwareOriVersion: 固件原版本号
        :type FirmwareOriVersion: str
        :param UpgradeMethod: 固件升级方式；0 静默升级 1 用户确认升级   不填默认静默升级
        :type UpgradeMethod: int
        """
        self.ProductID = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.FirmwareOriVersion = None
        self.UpgradeMethod = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FirmwareOriVersion = params.get("FirmwareOriVersion")
        self.UpgradeMethod = params.get("UpgradeMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFirmwareResponse(AbstractModel):
    """UpdateFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UploadFirmwareRequest(AbstractModel):
    """UploadFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param Md5sum: 固件的MD5值
        :type Md5sum: str
        :param FileSize: 固件的大小
        :type FileSize: int
        :param FirmwareName: 固件名称
        :type FirmwareName: str
        :param FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        :param FwType: 固件升级模块；可选值 mcu|moudule
        :type FwType: str
        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Md5sum = None
        self.FileSize = None
        self.FirmwareName = None
        self.FirmwareDescription = None
        self.FwType = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.Md5sum = params.get("Md5sum")
        self.FileSize = params.get("FileSize")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")
        self.FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFirmwareResponse(AbstractModel):
    """UploadFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")