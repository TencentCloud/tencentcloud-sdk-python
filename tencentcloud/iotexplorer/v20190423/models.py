# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class CallDeviceActionAsyncRequest(AbstractModel):
    """CallDeviceActionAsync请求参数结构体

    """

    def __init__(self):
        """
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


class CallDeviceActionAsyncResponse(AbstractModel):
    """CallDeviceActionAsync返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class CallDeviceActionSyncResponse(AbstractModel):
    """CallDeviceActionSync返回参数结构体

    """

    def __init__(self):
        """
        :param ClientToken: 调用Id
        :type ClientToken: str
        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param Status: 返回状态
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
        """
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


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回信息
        :type Data: str
        :param Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic
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


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        """
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
        """
        self.ProductId = None
        self.DeviceName = None
        self.DevAddr = None
        self.AppKey = None
        self.DevEUI = None
        self.AppSKey = None
        self.NwkSKey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DevAddr = params.get("DevAddr")
        self.AppKey = params.get("AppKey")
        self.DevEUI = params.get("DevEUI")
        self.AppSKey = params.get("AppSKey")
        self.NwkSKey = params.get("NwkSKey")


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        """
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


class CreateLoRaFrequencyRequest(AbstractModel):
    """CreateLoRaFrequency请求参数结构体

    """

    def __init__(self):
        """
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


class CreateLoRaFrequencyResponse(AbstractModel):
    """CreateLoRaFrequency返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class CreateLoRaGatewayResponse(AbstractModel):
    """CreateLoRaGateway返回参数结构体

    """

    def __init__(self):
        """
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


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
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


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class CreateStudioProductResponse(AbstractModel):
    """CreateStudioProduct返回参数结构体

    """

    def __init__(self):
        """
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


class CreateTopicRuleRequest(AbstractModel):
    """CreateTopicRule请求参数结构体

    """

    def __init__(self):
        """
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


class CreateTopicRuleResponse(AbstractModel):
    """CreateTopicRule返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteLoRaFrequencyRequest(AbstractModel):
    """DeleteLoRaFrequency请求参数结构体

    """

    def __init__(self):
        """
        :param FreqId: 频点唯一ID
        :type FreqId: str
        """
        self.FreqId = None


    def _deserialize(self, params):
        self.FreqId = params.get("FreqId")


class DeleteLoRaFrequencyResponse(AbstractModel):
    """DeleteLoRaFrequency返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param GatewayId: LoRa 网关 Id
        :type GatewayId: str
        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")


class DeleteLoRaGatewayResponse(AbstractModel):
    """DeleteLoRaGateway返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteStudioProductResponse(AbstractModel):
    """DeleteStudioProduct返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param RuleName: 规则名
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DeleteTopicRuleResponse(AbstractModel):
    """DeleteTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeFirmwareTaskRequest(AbstractModel):
    """DescribeFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeFirmwareTaskResponse(AbstractModel):
    """DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeLoRaFrequencyRequest(AbstractModel):
    """DescribeLoRaFrequency请求参数结构体

    """

    def __init__(self):
        """
        :param FreqId: 频点唯一ID
        :type FreqId: str
        """
        self.FreqId = None


    def _deserialize(self, params):
        self.FreqId = params.get("FreqId")


class DescribeLoRaFrequencyResponse(AbstractModel):
    """DescribeLoRaFrequency返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeStudioProductRequest(AbstractModel):
    """DescribeStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeStudioProductResponse(AbstractModel):
    """DescribeStudioProduct返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeTopicRuleRequest(AbstractModel):
    """DescribeTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称。
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DescribeTopicRuleResponse(AbstractModel):
    """DescribeTopicRule返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        """
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


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
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


class DisableTopicRuleRequest(AbstractModel):
    """DisableTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DisableTopicRuleResponse(AbstractModel):
    """DisableTopicRule返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param RuleName: 规则名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class EnableTopicRuleResponse(AbstractModel):
    """EnableTopicRule返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        """
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
        """
        self.Version = None
        self.Md5sum = None
        self.CreateTime = None
        self.ProductName = None
        self.Name = None
        self.Description = None
        self.ProductId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Md5sum = params.get("Md5sum")
        self.CreateTime = params.get("CreateTime")
        self.ProductName = params.get("ProductName")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ProductId = params.get("ProductId")


class GetDeviceListRequest(AbstractModel):
    """GetDeviceList请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-100
        :type Limit: int
        :param FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :type FirmwareVersion: str
        :param DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.FirmwareVersion = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.DeviceName = params.get("DeviceName")


class GetDeviceListResponse(AbstractModel):
    """GetDeviceList返回参数结构体

    """

    def __init__(self):
        """
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


class GetLoRaGatewayListRequest(AbstractModel):
    """GetLoRaGatewayList请求参数结构体

    """

    def __init__(self):
        """
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


class GetLoRaGatewayListResponse(AbstractModel):
    """GetLoRaGatewayList返回参数结构体

    """

    def __init__(self):
        """
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


class GetProjectListRequest(AbstractModel):
    """GetProjectList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 个数限制
        :type Limit: int
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.Offset = None
        self.Limit = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")


class GetProjectListResponse(AbstractModel):
    """GetProjectList返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DevStatus: 产品DevStatus
        :type DevStatus: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
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


class GetStudioProductListResponse(AbstractModel):
    """GetStudioProductList返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class GetTopicRuleListResponse(AbstractModel):
    """GetTopicRuleList返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ListEventHistoryResponse(AbstractModel):
    """ListEventHistory返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ListFirmwaresResponse(AbstractModel):
    """ListFirmwares返回参数结构体

    """

    def __init__(self):
        """
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


class LoRaFrequencyEntry(AbstractModel):
    """LoRa自定义频点信息

    """

    def __init__(self):
        """
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


class LoRaGatewayItem(AbstractModel):
    """LoRa 网关信息

    """

    def __init__(self):
        """
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


class LoRaGatewayLocation(AbstractModel):
    """网关坐标

    """

    def __init__(self):
        """
        :param Accuracy: 准确度
        :type Accuracy: float
        :param Altitude: 海拔
        :type Altitude: float
        :param Latitude: 纬度
        :type Latitude: float
        :param Longitude: 精度
        :type Longitude: float
        """
        self.Accuracy = None
        self.Altitude = None
        self.Latitude = None
        self.Longitude = None


    def _deserialize(self, params):
        self.Accuracy = params.get("Accuracy")
        self.Altitude = params.get("Altitude")
        self.Latitude = params.get("Latitude")
        self.Longitude = params.get("Longitude")


class ModifyLoRaFrequencyRequest(AbstractModel):
    """ModifyLoRaFrequency请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyLoRaFrequencyResponse(AbstractModel):
    """ModifyLoRaFrequency返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ModifyLoRaGatewayResponse(AbstractModel):
    """ModifyLoRaGateway返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        """
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


class ModifyStudioProductRequest(AbstractModel):
    """ModifyStudioProduct请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyStudioProductResponse(AbstractModel):
    """ModifyStudioProduct返回参数结构体

    """

    def __init__(self):
        """
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


class ModifyTopicRuleRequest(AbstractModel):
    """ModifyTopicRule请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyTopicRuleResponse(AbstractModel):
    """ModifyTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductEntry(AbstractModel):
    """产品详情

    """

    def __init__(self):
        """
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


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        """
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


class ProjectEntry(AbstractModel):
    """项目详情

    """

    def __init__(self):
        """
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


class ProjectEntryEx(AbstractModel):
    """项目详情

    """

    def __init__(self):
        """
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


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        """
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


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct请求参数结构体

    """

    def __init__(self):
        """
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


class ReleaseStudioProductResponse(AbstractModel):
    """ReleaseStudioProduct返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct请求参数结构体

    """

    def __init__(self):
        """
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
        """
        self.ProjectId = None
        self.ProductName = None
        self.Limit = None
        self.Offset = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductName = params.get("ProductName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DevStatus = params.get("DevStatus")


class SearchStudioProductResponse(AbstractModel):
    """SearchStudioProduct返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param RuleName: 规则名
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class SearchTopicRuleResponse(AbstractModel):
    """SearchTopicRule返回参数结构体

    """

    def __init__(self):
        """
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


class TopicRule(AbstractModel):
    """TopicRule结构

    """

    def __init__(self):
        """
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


class TopicRuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        """
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


class TopicRulePayload(AbstractModel):
    """TopicRulePayload结构

    """

    def __init__(self):
        """
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


class UpdateFirmwareRequest(AbstractModel):
    """UpdateFirmware请求参数结构体

    """

    def __init__(self):
        """
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


class UpdateFirmwareResponse(AbstractModel):
    """UpdateFirmware返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Md5sum = None
        self.FileSize = None
        self.FirmwareName = None
        self.FirmwareDescription = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.Md5sum = params.get("Md5sum")
        self.FileSize = params.get("FileSize")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")


class UploadFirmwareResponse(AbstractModel):
    """UploadFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")