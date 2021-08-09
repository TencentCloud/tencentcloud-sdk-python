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


class CallDeviceActionAsyncRequest(AbstractModel):
    """CallDeviceActionAsync请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义\n        :type ActionId: str\n        :param InputParams: 输入参数\n        :type InputParams: str\n        """
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
        """
        :param ClientToken: 调用Id\n        :type ClientToken: str\n        :param Status: 异步调用状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义\n        :type ActionId: str\n        :param InputParams: 输入参数\n        :type InputParams: str\n        """
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
        """
        :param ClientToken: 调用Id\n        :type ClientToken: str\n        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputParams: str\n        :param Status: 返回状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Data: 属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义\n        :type Data: str\n        :param Method: 请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性\n        :type Method: str\n        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName , 通常情况不需要填写\n        :type DeviceId: str\n        :param DataTimestamp: 上报数据UNIX时间戳(毫秒), 仅对Method:reported有效\n        :type DataTimestamp: int\n        """
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
        """
        :param Data: 返回信息\n        :type Data: str\n        :param Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。\n        :type DeviceName: str\n        :param DevAddr: LoRaWAN 设备地址\n        :type DevAddr: str\n        :param AppKey: LoRaWAN 应用密钥\n        :type AppKey: str\n        :param DevEUI: LoRaWAN 设备唯一标识\n        :type DevEUI: str\n        :param AppSKey: LoRaWAN 应用会话密钥\n        :type AppSKey: str\n        :param NwkSKey: LoRaWAN 网络会话密钥\n        :type NwkSKey: str\n        """
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
        """
        :param Data: 设备参数描述。\n        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FreqName: 频点配置名称\n        :type FreqName: str\n        :param ChannelsDataUp: 数据上行信道\n        :type ChannelsDataUp: list of int non-negative\n        :param ChannelsDataRX1: 数据下行RX1信道\n        :type ChannelsDataRX1: list of int non-negative\n        :param ChannelsDataRX2: 数据下行RX2信道\n        :type ChannelsDataRX2: list of int non-negative\n        :param ChannelsJoinUp: 入网上行信道\n        :type ChannelsJoinUp: list of int non-negative\n        :param ChannelsJoinRX1: 入网下行RX1信道\n        :type ChannelsJoinRX1: list of int non-negative\n        :param ChannelsJoinRX2: 入网下行RX2信道\n        :type ChannelsJoinRX2: list of int non-negative\n        :param Description: 频点配置描述\n        :type Description: str\n        """
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
        """
        :param Data: LoRa频点信息\n        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayId: LoRa 网关Id\n        :type GatewayId: str\n        :param Name: 网关名称\n        :type Name: str\n        :param Description: 详情描述\n        :type Description: str\n        :param Location: 位置坐标\n        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`\n        :param Position: 位置信息\n        :type Position: str\n        :param PositionDetails: 位置详情\n        :type PositionDetails: str\n        :param IsPublic: 是否公开\n        :type IsPublic: bool\n        :param FrequencyId: 频点ID\n        :type FrequencyId: str\n        """
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
        """
        :param Gateway: LoRa 网关信息\n        :type Gateway: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectDesc: 项目描述\n        :type ProjectDesc: str\n        :param InstanceId: 实例ID，不带实例ID，默认为公共实例\n        :type InstanceId: str\n        """
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
        """
        :param Project: 返回信息\n        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}\n        :type ProductName: str\n        :param CategoryId: 产品分组模板ID , ( 自定义模板填写1 , 控制台调用会使用预置的其他ID)\n        :type CategoryId: int\n        :param ProductType: 产品类型 填写 ( 0 普通产品 )\n        :type ProductType: int\n        :param EncryptionType: 加密类型 加密类型，1表示证书认证，2表示签名认证。\n        :type EncryptionType: str\n        :param NetType: 连接类型 可以填写 wifi cellular else\n        :type NetType: str\n        :param DataProtocol: 数据协议 (1 使用物模型 2 为自定义)\n        :type DataProtocol: int\n        :param ProductDesc: 产品描述\n        :type ProductDesc: str\n        :param ProjectId: 产品的项目ID\n        :type ProjectId: str\n        """
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
        """
        :param Product: 产品描述\n        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleName: 规则名称\n        :type RuleName: str\n        :param TopicRulePayload: 规则内容\n        :type TopicRulePayload: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param DeviceName: 设备名称。\n        :type DeviceName: str\n        :param ForceDelete: 是否删除绑定设备\n        :type ForceDelete: bool\n        """
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
        """
        :param ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultCode: str\n        :param ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FreqId: 频点唯一ID\n        :type FreqId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoRaGatewayRequest(AbstractModel):
    """DeleteLoRaGateway请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: LoRa 网关 Id\n        :type GatewayId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStudioProductRequest(AbstractModel):
    """DeleteStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRuleRequest(AbstractModel):
    """DeleteTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名\n        :type RuleName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 区间开始时间（Unix 时间戳，毫秒级）\n        :type MinTime: int\n        :param MaxTime: 区间结束时间（Unix 时间戳，毫秒级）\n        :type MaxTime: int\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符\n        :type FieldName: str\n        :param Limit: 返回条数\n        :type Limit: int\n        :param Context: 检索上下文\n        :type Context: str\n        """
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
        """
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。\n        :type FieldName: str\n        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listover: bool\n        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Context: str\n        :param Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Results: list of DeviceDataHistoryItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName\n        :type DeviceId: str\n        """
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
        """
        :param Data: 设备数据\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName\n        :type DeviceId: str\n        """
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
        """
        :param Device: 设备信息\n        :type Device: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件任务ID\n        :type TaskId: int\n        """
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
        """
        :param TaskId: 固件任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        :param Status: 固件任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param CreateTime: 固件任务创建时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductName: str\n        :param UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradeMode: str\n        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalVersion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FreqId: 频点唯一ID\n        :type FreqId: str\n        """
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
        """
        :param Data: 返回详情项
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        """
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
        """
        :param Model: 产品数据模板\n        :type Model: :class:`tencentcloud.iotexplorer.v20190423.models.ProductModelDefinition`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        """
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
        """
        :param Project: 返回信息\n        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntryEx`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        """
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
        """
        :param Product: 产品详情\n        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleName: 规则名称。\n        :type RuleName: str\n        """
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
        """
        :param Rule: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rule: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRule`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceCert: str\n        :param DeviceName: 设备名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceName: str\n        :param DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DevicePrivateKey: str\n        :param DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DevicePsk: str\n        """
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
        """
        :param Time: 时间点，毫秒时间戳\n        :type Time: str\n        :param Value: 字段取值\n        :type Value: str\n        """
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
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param Status: 0: 离线, 1: 在线, 2: 获取失败, 3 未激活\n        :type Status: int\n        :param DevicePsk: 设备密钥，密钥加密的设备返回\n        :type DevicePsk: str\n        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstOnlineTime: int\n        :param LoginTime: 最后一次上线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoginTime: int\n        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param Version: 设备固件版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param DeviceCert: 设备证书
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceCert: str\n        :param LogLevel: 日志级别
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogLevel: int\n        :param DevAddr: LoRaWAN 设备地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type DevAddr: str\n        :param AppKey: LoRaWAN 应用密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppKey: str\n        :param DevEUI: LoRaWAN 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type DevEUI: str\n        :param AppSKey: LoRaWAN 应用会话密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppSKey: str\n        :param NwkSKey: LoRaWAN 网络会话密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type NwkSKey: str\n        :param CreateUserId: 创建人Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUserId: int\n        :param CreatorNickName: 创建人昵称
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatorNickName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableTopicRuleRequest(AbstractModel):
    """DisableTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称\n        :type RuleName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableTopicRuleRequest(AbstractModel):
    """EnableTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称\n        :type RuleName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        """
        :param TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeStamp: int\n        :param ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceName: str\n        :param EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type EventId: str\n        :param Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: str\n        """
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
        


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        """
        :param Version: 固件版本\n        :type Version: str\n        :param Md5sum: 固件MD5值\n        :type Md5sum: str\n        :param CreateTime: 固件创建时间\n        :type CreateTime: int\n        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductName: str\n        :param Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param FwType: 固件升级模块
注意：此字段可能返回 null，表示取不到有效值。\n        :type FwType: str\n        :param CreateUserId: 创建者子 uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUserId: int\n        :param CreatorNickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatorNickName: str\n        """
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
        


class GetCOSURLRequest(AbstractModel):
    """GetCOSURL请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本\n        :type FirmwareVersion: str\n        :param FileSize: 文件大小\n        :type FileSize: int\n        """
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
        """
        :param Url: 固件URL\n        :type Url: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class GetDeviceListRequest(AbstractModel):
    """GetDeviceList请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID\n        :type ProductId: str\n        :param Offset: 分页偏移\n        :type Offset: int\n        :param Limit: 分页的大小，数值范围 10-100\n        :type Limit: int\n        :param FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备\n        :type FirmwareVersion: str\n        :param DeviceName: 需要过滤的设备名称\n        :type DeviceName: str\n        """
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
        """
        :param Devices: 返回的设备列表, 注意列表设备的 DevicePsk 为空, 要获取设备的 DevicePsk 请使用 DescribeDevice
注意：此字段可能返回 null，表示取不到有效值。\n        :type Devices: list of DeviceInfo\n        :param Total: 产品下的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param IsCommunity: 是否是社区网关\n        :type IsCommunity: bool\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制个数\n        :type Limit: int\n        """
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
        """
        :param Total: 返回总数\n        :type Total: int\n        :param Gateways: 返回详情项
注意：此字段可能返回 null，表示取不到有效值。\n        :type Gateways: list of LoRaGatewayItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 个数限制\n        :type Limit: int\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param ProjectId: 按项目D搜索\n        :type ProjectId: str\n        :param ProductId: 按产品ID搜索\n        :type ProductId: str\n        :param Includes: 加载 ProductCount、DeviceCount、ApplicationCount，可选值：ProductCount、DeviceCount、ApplicationCount，可多选\n        :type Includes: list of str\n        :param ProjectName: 按项目名称搜索\n        :type ProjectName: str\n        """
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
        """
        :param Projects: 项目列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Projects: list of ProjectEntryEx\n        :param Total: 列表项个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param DevStatus: 产品DevStatus\n        :type DevStatus: str\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Limit\n        :type Limit: int\n        """
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
        """
        :param Products: 产品列表\n        :type Products: list of ProductEntry\n        :param Total: 产品数量\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PageNum: 请求的页数\n        :type PageNum: int\n        :param PageSize: 分页的大小\n        :type PageSize: int\n        """
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
        """
        :param TotalCnt: 规则总数量\n        :type TotalCnt: int\n        :param Rules: 规则列表\n        :type Rules: list of TopicRuleInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件\n        :type Type: str\n        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h\n        :type StartTime: int\n        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间\n        :type EndTime: int\n        :param Context: 搜索上下文, 用作查询游标\n        :type Context: str\n        :param Size: 单次获取的历史数据项目的最大数量, 缺省10\n        :type Size: int\n        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。\n        :type EventId: str\n        """
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
        """
        :param Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。\n        :type Context: str\n        :param Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listover: bool\n        :param EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。\n        :type EventHistory: list of EventHistoryItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PageNum: 获取的页数\n        :type PageNum: int\n        :param PageSize: 分页的大小\n        :type PageSize: int\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Filters: 搜索过滤条件\n        :type Filters: list of SearchKeyword\n        """
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
        """
        :param TotalCount: 固件总数\n        :type TotalCount: int\n        :param Firmwares: 固件列表\n        :type Firmwares: list of FirmwareInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FreqId: 频点唯一ID\n        :type FreqId: str\n        :param FreqName: 频点名称\n        :type FreqName: str\n        :param Description: 频点描述\n        :type Description: str\n        :param ChannelsDataUp: 数据上行信道\n        :type ChannelsDataUp: list of int non-negative\n        :param ChannelsDataRX1: 数据下行信道RX1\n        :type ChannelsDataRX1: list of int non-negative\n        :param ChannelsDataRX2: 数据下行信道RX2\n        :type ChannelsDataRX2: list of int non-negative\n        :param ChannelsJoinUp: 入网上行信道\n        :type ChannelsJoinUp: list of int non-negative\n        :param ChannelsJoinRX1: 入网下行RX1信道\n        :type ChannelsJoinRX1: list of int non-negative\n        :param ChannelsJoinRX2: 入网下行RX2信道\n        :type ChannelsJoinRX2: list of int non-negative\n        :param CreateTime: 创建时间\n        :type CreateTime: int\n        """
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
        """
        :param GatewayId: LoRa 网关Id\n        :type GatewayId: str\n        :param IsPublic: 是否是公开网关\n        :type IsPublic: bool\n        :param Description: 网关描述\n        :type Description: str\n        :param Name: 网关名称\n        :type Name: str\n        :param Position: 网关位置信息\n        :type Position: str\n        :param PositionDetails: 网关位置详情\n        :type PositionDetails: str\n        :param Location: LoRa 网关位置坐标\n        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`\n        :param UpdatedAt: 最后更新时间\n        :type UpdatedAt: str\n        :param CreatedAt: 创建时间\n        :type CreatedAt: str\n        :param LastSeenAt: 最后上报时间\n        :type LastSeenAt: str\n        :param FrequencyId: 频点ID\n        :type FrequencyId: str\n        """
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
        """
        :param Accuracy: 准确度\n        :type Accuracy: float\n        :param Altitude: 海拔\n        :type Altitude: float\n        :param Latitude: 纬度\n        :type Latitude: float\n        :param Longitude: 精度\n        :type Longitude: float\n        """
        self.Accuracy = None
        self.Altitude = None
        self.Latitude = None
        self.Longitude = None


    def _deserialize(self, params):
        self.Accuracy = params.get("Accuracy")
        self.Altitude = params.get("Altitude")
        self.Latitude = params.get("Latitude")
        self.Longitude = params.get("Longitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoRaFrequencyRequest(AbstractModel):
    """ModifyLoRaFrequency请求参数结构体

    """

    def __init__(self):
        """
        :param FreqId: 频点唯一ID\n        :type FreqId: str\n        :param FreqName: 频点名称\n        :type FreqName: str\n        :param Description: 频点描述\n        :type Description: str\n        :param ChannelsDataUp: 数据上行信道\n        :type ChannelsDataUp: list of int non-negative\n        :param ChannelsDataRX1: 数据下行信道RX1\n        :type ChannelsDataRX1: list of int non-negative\n        :param ChannelsDataRX2: 数据下行信道RX2\n        :type ChannelsDataRX2: list of int non-negative\n        :param ChannelsJoinUp: 入网上行信道\n        :type ChannelsJoinUp: list of int non-negative\n        :param ChannelsJoinRX1: 入网下行信道RX1\n        :type ChannelsJoinRX1: list of int non-negative\n        :param ChannelsJoinRX2: 入网下行信道RX2\n        :type ChannelsJoinRX2: list of int non-negative\n        """
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
        """
        :param Data: 频点信息\n        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Description: 描述信息\n        :type Description: str\n        :param GatewayId: LoRa网关Id\n        :type GatewayId: str\n        :param Location: LoRa网关位置坐标\n        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`\n        :param Name: LoRa网关名称\n        :type Name: str\n        :param IsPublic: 是否公开可见\n        :type IsPublic: bool\n        :param Position: 位置信息\n        :type Position: str\n        :param PositionDetails: 位置详情\n        :type PositionDetails: str\n        :param FrequencyId: 频点ID\n        :type FrequencyId: str\n        """
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
        """
        :param Gateway: 返回网关数据\n        :type Gateway: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ModelSchema: 数据模板定义\n        :type ModelSchema: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectDesc: 项目描述\n        :type ProjectDesc: str\n        """
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
        """
        :param Project: 项目详情\n        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param ProductDesc: 产品描述\n        :type ProductDesc: str\n        :param ModuleId: 模型ID\n        :type ModuleId: int\n        :param EnableProductScript: 是否打开二进制转Json功能, 取值为字符串 true/false\n        :type EnableProductScript: str\n        """
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
        """
        :param Product: 产品描述\n        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleName: 规则名称\n        :type RuleName: str\n        :param TopicRulePayload: 替换的规则包体\n        :type TopicRulePayload: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductEntry(AbstractModel):
    """产品详情

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param CategoryId: 产品分组模板ID\n        :type CategoryId: int\n        :param EncryptionType: 加密类型\n        :type EncryptionType: str\n        :param NetType: 连接类型\n        :type NetType: str\n        :param DataProtocol: 数据协议\n        :type DataProtocol: int\n        :param ProductDesc: 产品描述\n        :type ProductDesc: str\n        :param DevStatus: 状态\n        :type DevStatus: str\n        :param CreateTime: 创建时间\n        :type CreateTime: int\n        :param UpdateTime: 更新时间\n        :type UpdateTime: int\n        :param Region: 区域\n        :type Region: str\n        :param ProductType: 产品类型\n        :type ProductType: int\n        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ModuleId: 产品ModuleId\n        :type ModuleId: int\n        :param EnableProductScript: 是否使用脚本进行二进制转json功能 可以取值 true / false
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableProductScript: str\n        :param CreateUserId: 创建人 UinId
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUserId: int\n        :param CreatorNickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatorNickName: str\n        """
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
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ModelDefine: 模型定义\n        :type ModelDefine: str\n        :param UpdateTime: 更新时间，秒级时间戳\n        :type UpdateTime: int\n        :param CreateTime: 创建时间，秒级时间戳\n        :type CreateTime: int\n        :param CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。\n        :type CategoryModel: str\n        :param NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetTypeModel: str\n        """
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
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectDesc: 项目描述\n        :type ProjectDesc: str\n        :param CreateTime: 创建时间，unix时间戳\n        :type CreateTime: int\n        :param UpdateTime: 更新时间，unix时间戳\n        :type UpdateTime: int\n        """
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
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectDesc: 项目描述\n        :type ProjectDesc: str\n        :param CreateTime: 项目创建时间，unix时间戳\n        :type CreateTime: int\n        :param UpdateTime: 项目更新时间，unix时间戳\n        :type UpdateTime: int\n        :param ProductCount: 产品数量\n        :type ProductCount: int\n        :param NativeAppCount: NativeApp数量\n        :type NativeAppCount: int\n        :param WebAppCount: WebApp数量\n        :type WebAppCount: int\n        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param ApplicationCount: 应用数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationCount: int\n        :param DeviceCount: 设备注册总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceCount: int\n        """
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
        


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Topic: 消息发往的主题\n        :type Topic: str\n        :param Payload: 云端下发到设备的控制报文\n        :type Payload: str\n        :param Qos: 消息服务质量等级，取值为0或1\n        :type Qos: int\n        :param PayloadEncoding: Payload的内容编码格式，取值为base64或空。base64表示云端将接收到的base64编码后的报文再转换成二进制报文下发至设备，为空表示不作转换，透传下发至设备\n        :type PayloadEncoding: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DevStatus: 产品DevStatus\n        :type DevStatus: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchKeyword(AbstractModel):
    """搜索关键词

    """

    def __init__(self):
        """
        :param Key: 搜索条件的Key\n        :type Key: str\n        :param Value: 搜索条件的值\n        :type Value: str\n        """
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
        


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param Limit: 列表Limit\n        :type Limit: int\n        :param Offset: 列表Offset\n        :type Offset: int\n        :param DevStatus: 产品Status\n        :type DevStatus: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        """
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
        """
        :param Products: 产品列表\n        :type Products: list of ProductEntry\n        :param Total: 产品数量\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleName: 规则名\n        :type RuleName: str\n        """
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
        """
        :param TotalCnt: 搜索到的规则总数\n        :type TotalCnt: int\n        :param Rules: 规则信息列表\n        :type Rules: list of TopicRuleInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleName: 规则名称。\n        :type RuleName: str\n        :param Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==\n        :type Sql: str\n        :param Description: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param Actions: 行为的JSON字符串。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Actions: str\n        :param RuleDisabled: 是否禁用规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleDisabled: bool\n        """
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
        """
        :param RuleName: 规则名称\n        :type RuleName: str\n        :param Description: 规则描述\n        :type Description: str\n        :param CreatedAt: 创建时间\n        :type CreatedAt: int\n        :param RuleDisabled: 规则是否禁用\n        :type RuleDisabled: bool\n        """
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
        """
        :param Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==\n        :type Sql: str\n        :param Actions: 行为的JSON字符串，大部分种类举例如下：
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
]\n        :type Actions: str\n        :param Description: 规则描述\n        :type Description: str\n        :param RuleDisabled: 是否禁用规则\n        :type RuleDisabled: bool\n        """
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
        


class UpdateFirmwareRequest(AbstractModel):
    """UpdateFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param FirmwareVersion: 固件新的版本号\n        :type FirmwareVersion: str\n        :param FirmwareOriVersion: 固件原版本号\n        :type FirmwareOriVersion: str\n        :param UpgradeMethod: 固件升级方式；0 静默升级 1 用户确认升级   不填默认静默升级\n        :type UpgradeMethod: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UploadFirmwareRequest(AbstractModel):
    """UploadFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param Md5sum: 固件的MD5值\n        :type Md5sum: str\n        :param FileSize: 固件的大小\n        :type FileSize: int\n        :param FirmwareName: 固件名称\n        :type FirmwareName: str\n        :param FirmwareDescription: 固件描述\n        :type FirmwareDescription: str\n        :param FwType: 固件升级模块；可选值 mcu|moudule\n        :type FwType: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")