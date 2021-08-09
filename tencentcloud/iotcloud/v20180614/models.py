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


class Attribute(AbstractModel):
    """设备属性

    """

    def __init__(self):
        """
        :param Tags: 属性列表\n        :type Tags: list of DeviceTag\n        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchPublishMessage(AbstractModel):
    """批量发消息请求

    """

    def __init__(self):
        """
        :param Topic: 消息发往的主题。为 Topic 权限中去除 ProductID 和 DeviceName 的部分，如 “event”\n        :type Topic: str\n        :param Payload: 消息内容\n        :type Payload: str\n        """
        self.Topic = None
        self.Payload = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareRequest(AbstractModel):
    """BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件新版本号\n        :type FirmwareVersion: str\n        :param FirmwareOriVersion: 固件原版本号，根据文件列表升级固件不需要填写此参数\n        :type FirmwareOriVersion: str\n        :param UpgradeMethod: 升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式\n        :type UpgradeMethod: int\n        :param FileName: 设备列表文件名称，根据文件列表升级固件需要填写此参数\n        :type FileName: str\n        :param FileMd5: 设备列表的文件md5值\n        :type FileMd5: str\n        :param FileSize: 设备列表的文件大小值\n        :type FileSize: int\n        :param DeviceNames: 需要升级的设备名称列表\n        :type DeviceNames: list of str\n        :param TimeoutInterval: 固件升级任务，默认超时时间。 最小取值60秒，最大为3600秒\n        :type TimeoutInterval: int\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.FirmwareOriVersion = None
        self.UpgradeMethod = None
        self.FileName = None
        self.FileMd5 = None
        self.FileSize = None
        self.DeviceNames = None
        self.TimeoutInterval = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FirmwareOriVersion = params.get("FirmwareOriVersion")
        self.UpgradeMethod = params.get("UpgradeMethod")
        self.FileName = params.get("FileName")
        self.FileMd5 = params.get("FileMd5")
        self.FileSize = params.get("FileSize")
        self.DeviceNames = params.get("DeviceNames")
        self.TimeoutInterval = params.get("TimeoutInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareResponse(AbstractModel):
    """BatchUpdateFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BatchUpdateShadow(AbstractModel):
    """批量更新设备影子任务

    """

    def __init__(self):
        """
        :param Desired: 设备影子的期望状态，格式为 Json 对象序列化之后的字符串\n        :type Desired: str\n        """
        self.Desired = None


    def _deserialize(self, params):
        self.Desired = params.get("Desired")
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
        """
        :param GatewayProductId: 网关设备的产品ID\n        :type GatewayProductId: str\n        :param GatewayDeviceName: 网关设备的设备名\n        :type GatewayDeviceName: str\n        :param ProductId: 被绑定设备的产品ID\n        :type ProductId: str\n        :param DeviceNames: 被绑定的多个设备名\n        :type DeviceNames: list of str\n        :param Skey: 中兴CLAA设备的绑定需要skey，普通的设备不需要\n        :type Skey: str\n        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None
        self.Skey = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Skey = params.get("Skey")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BrokerSubscribe(AbstractModel):
    """代理订阅信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名\n        :type DeviceName: str\n        """
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
        


class CancelDeviceFirmwareTaskRequest(AbstractModel):
    """CancelDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件升级任务ID\n        :type TaskId: int\n        """
        self.ProductID = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDeviceFirmwareTaskResponse(AbstractModel):
    """CancelDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务 ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID\n        :type ProductId: str\n        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。\n        :type DeviceName: str\n        :param Attribute: 设备属性\n        :type Attribute: :class:`tencentcloud.iotcloud.v20180614.models.Attribute`\n        :param DefinedPsk: 是否使用自定义PSK，默认不使用\n        :type DefinedPsk: str\n        :param Isp: 运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通\n        :type Isp: int\n        :param Imei: IMEI，当产品是NB-IoT产品时，此字段必填\n        :type Imei: str\n        :param LoraDevEui: LoRa设备的DevEui，当创建LoRa时，此字段必填\n        :type LoraDevEui: str\n        :param LoraMoteType: LoRa设备的MoteType\n        :type LoraMoteType: int\n        :param Skey: 创建LoRa设备需要skey\n        :type Skey: str\n        :param LoraAppKey: LoRa设备的AppKey\n        :type LoraAppKey: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Attribute = None
        self.DefinedPsk = None
        self.Isp = None
        self.Imei = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.Skey = None
        self.LoraAppKey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self.Attribute = Attribute()
            self.Attribute._deserialize(params.get("Attribute"))
        self.DefinedPsk = params.get("DefinedPsk")
        self.Isp = params.get("Isp")
        self.Imei = params.get("Imei")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.Skey = params.get("Skey")
        self.LoraAppKey = params.get("LoraAppKey")
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
        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数\n        :type DevicePsk: str\n        :param DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数\n        :type DeviceCert: str\n        :param DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数\n        :type DevicePrivateKey: str\n        :param LoraDevEui: LoRa设备的DevEui，当设备是LoRa设备时，会返回该字段\n        :type LoraDevEui: str\n        :param LoraMoteType: LoRa设备的MoteType，当设备是LoRa设备时，会返回该字段\n        :type LoraMoteType: int\n        :param LoraAppKey: LoRa设备的AppKey，当设备是LoRa设备时，会返回该字段\n        :type LoraAppKey: str\n        :param LoraNwkKey: LoRa设备的NwkKey，当设备是LoRa设备时，会返回该字段\n        :type LoraNwkKey: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LoraAppKey = None
        self.LoraNwkKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LoraAppKey = params.get("LoraAppKey")
        self.LoraNwkKey = params.get("LoraNwkKey")
        self.RequestId = params.get("RequestId")


class CreateLoraDeviceRequest(AbstractModel):
    """CreateLoraDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id ，创建产品时腾讯云为用户分配全局唯一的Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param DeviceType: 设备类型 ，目前支持A、B、C三种\n        :type DeviceType: str\n        :param AppEui: LoRa应用UUID\n        :type AppEui: str\n        :param DeviceEui: LoRa设备UUID\n        :type DeviceEui: str\n        :param AppKey: LoRa应用密钥\n        :type AppKey: str\n        :param AuthKey: LoRa设备验证密钥\n        :type AuthKey: str\n        :param Memo: 设备备注\n        :type Memo: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceType = None
        self.AppEui = None
        self.DeviceEui = None
        self.AppKey = None
        self.AuthKey = None
        self.Memo = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceType = params.get("DeviceType")
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.AppKey = params.get("AppKey")
        self.AuthKey = params.get("AuthKey")
        self.Memo = params.get("Memo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoraDeviceResponse(AbstractModel):
    """CreateLoraDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppEui: LoRa应用UUID\n        :type AppEui: str\n        :param DeviceEui: LoRa设备UUID\n        :type DeviceEui: str\n        :param ClassType: 设备类型,目前支持A、B、C三种\n        :type ClassType: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AppEui = None
        self.DeviceEui = None
        self.ClassType = None
        self.DeviceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.ClassType = params.get("ClassType")
        self.DeviceName = params.get("DeviceName")
        self.RequestId = params.get("RequestId")


class CreateMultiDeviceRequest(AbstractModel):
    """CreateMultiDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID。创建产品时腾讯云为用户分配全局唯一的 ID\n        :type ProductId: str\n        :param DeviceNames: 批量创建的设备名数组，单次最多创建 100 个设备。命名规则：[a-zA-Z0-9:_-]{1,48}\n        :type DeviceNames: list of str\n        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiDeviceResponse(AbstractModel):
    """CreateMultiDevice返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，腾讯云生成全局唯一的任务 ID，有效期一个月，一个月之后任务失效。可以调用获取创建多设备任务状态接口获取该任务的执行状态，当状态为成功时，可以调用获取创建多设备任务结果接口获取该任务的结果\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateMultiDevicesTaskRequest(AbstractModel):
    """CreateMultiDevicesTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ParametersType: 参数类型 cosfile-文件上传 random-随机创建\n        :type ParametersType: str\n        :param FileName: 文件上传类型时文件名\n        :type FileName: str\n        :param FileSize: 文件上传类型时文件大小\n        :type FileSize: int\n        :param BatchCount: 随机创建时设备创建个数\n        :type BatchCount: int\n        :param Hash: 文件上传类型时文件md5值\n        :type Hash: str\n        """
        self.ProductId = None
        self.ParametersType = None
        self.FileName = None
        self.FileSize = None
        self.BatchCount = None
        self.Hash = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ParametersType = params.get("ParametersType")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.BatchCount = params.get("BatchCount")
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiDevicesTaskResponse(AbstractModel):
    """CreateMultiDevicesTask返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务ID\n        :type Id: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}\n        :type ProductName: str\n        :param ProductProperties: 产品属性\n        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`\n        :param Skey: 创建CLAA产品时，需要Skey\n        :type Skey: str\n        """
        self.ProductName = None
        self.ProductProperties = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称\n        :type ProductName: str\n        :param ProductId: 产品 ID，腾讯云生成全局唯一 ID\n        :type ProductId: str\n        :param ProductProperties: 产品属性\n        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProductName = None
        self.ProductId = None
        self.ProductProperties = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.ProductId = params.get("ProductId")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.RequestId = params.get("RequestId")


class CreateTaskFileUrlRequest(AbstractModel):
    """CreateTaskFileUrl请求参数结构体

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
        


class CreateTaskFileUrlResponse(AbstractModel):
    """CreateTaskFileUrl返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 任务文件上传链接\n        :type Url: str\n        :param FileName: 任务文件名\n        :type FileName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Url = None
        self.FileName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileName = params.get("FileName")
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，取值为 “UpdateShadow” 或者 “PublishMessage”\n        :type TaskType: str\n        :param ProductId: 执行任务的产品ID\n        :type ProductId: str\n        :param DeviceNameFilter: 执行任务的设备名的正则表达式\n        :type DeviceNameFilter: str\n        :param ScheduleTimeInSeconds: 任务开始执行的时间。 取值为 Unix 时间戳，单位秒，且需大于等于当前时间时间戳，0为系统当前时间时间戳，即立即执行，最大为当前时间86400秒后，超过则取值为当前时间86400秒后\n        :type ScheduleTimeInSeconds: int\n        :param Tasks: 任务描述细节，描述见下 Task\n        :type Tasks: :class:`tencentcloud.iotcloud.v20180614.models.Task`\n        :param MaxExecutionTimeInSeconds: 最长执行时间，单位秒，被调度后超过此时间仍未有结果则视为任务失败。取值为0-86400，默认为86400\n        :type MaxExecutionTimeInSeconds: int\n        """
        self.TaskType = None
        self.ProductId = None
        self.DeviceNameFilter = None
        self.ScheduleTimeInSeconds = None
        self.Tasks = None
        self.MaxExecutionTimeInSeconds = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProductId = params.get("ProductId")
        self.DeviceNameFilter = params.get("DeviceNameFilter")
        self.ScheduleTimeInSeconds = params.get("ScheduleTimeInSeconds")
        if params.get("Tasks") is not None:
            self.Tasks = Task()
            self.Tasks._deserialize(params.get("Tasks"))
        self.MaxExecutionTimeInSeconds = params.get("MaxExecutionTimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 创建的任务ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品自身ID\n        :type ProductID: str\n        :param TopicName: Topic名称\n        :type TopicName: str\n        :param Privilege: Topic权限，1发布，2订阅，3订阅和发布\n        :type Privilege: int\n        :param BrokerSubscribe: 代理订阅信息，网关产品为绑定的子产品创建topic时需要填写，内容为子产品的ID和设备信息。\n        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`\n        """
        self.ProductID = None
        self.TopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.TopicName = params.get("TopicName")
        self.Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self.BrokerSubscribe = BrokerSubscribe()
            self.BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTopicRuleRequest(AbstractModel):
    """CreateTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称\n        :type RuleName: str\n        :param TopicRulePayload: 规则内容\n        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`\n        """
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
        :param ProductId: 设备所属的产品 ID\n        :type ProductId: str\n        :param DeviceName: 需要删除的设备名称\n        :type DeviceName: str\n        :param Skey: 删除LoRa设备以及LoRa网关设备需要skey\n        :type Skey: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Skey = params.get("Skey")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoraDeviceRequest(AbstractModel):
    """DeleteLoraDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        


class DeleteLoraDeviceResponse(AbstractModel):
    """DeleteLoraDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要删除的产品 ID\n        :type ProductId: str\n        :param Skey: 删除LoRa产品需要skey\n        :type Skey: str\n        """
        self.ProductId = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

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


class DescribeAllDevicesRequest(AbstractModel):
    """DescribeAllDevices请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 查询偏移量。\n        :type Offset: int\n        :param Limit: 查询设备数量。最大支持250个\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllDevicesResponse(AbstractModel):
    """DescribeAllDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 设备总数。\n        :type TotalCount: int\n        :param Devices: 查询的设备列表信息。\n        :type Devices: list of DeviceProperty\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceProperty()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceClientKeyRequest(AbstractModel):
    """DescribeDeviceClientKey请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 所属产品的Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        


class DescribeDeviceClientKeyResponse(AbstractModel):
    """DescribeDeviceClientKey返回参数结构体

    """

    def __init__(self):
        """
        :param ClientKey: 设备的私钥\n        :type ClientKey: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClientKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientKey = params.get("ClientKey")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名\n        :type DeviceName: str\n        """
        self.ProductID = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResourceRequest(AbstractModel):
    """DescribeDeviceResource请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Name: 具体的设备资源名称\n        :type Name: str\n        """
        self.DeviceName = None
        self.ProductID = None
        self.Name = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResourceResponse(AbstractModel):
    """DescribeDeviceResource返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 设备资源详情\n        :type Result: :class:`tencentcloud.iotcloud.v20180614.models.DeviceResourceInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DeviceResourceInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeDeviceResourcesRequest(AbstractModel):
    """DescribeDeviceResources请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，数值范围 10-250\n        :type Limit: int\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 需要过滤的设备名称\n        :type DeviceName: str\n        :param StartTime: 资源搜索开始时间\n        :type StartTime: str\n        :param EndTime: 资源搜索结束时间\n        :type EndTime: str\n        """
        self.Offset = None
        self.Limit = None
        self.ProductID = None
        self.DeviceName = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResourcesResponse(AbstractModel):
    """DescribeDeviceResources返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 资源总数\n        :type TotalCount: int\n        :param Result: 资源列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: list of DeviceResourceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = DeviceResourceInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param Online: 设备是否在线，0不在线，1在线\n        :type Online: int\n        :param LoginTime: 设备登录时间\n        :type LoginTime: int\n        :param Version: 设备固件版本\n        :type Version: str\n        :param LastUpdateTime: 设备最后更新时间\n        :type LastUpdateTime: int\n        :param DeviceCert: 设备证书\n        :type DeviceCert: str\n        :param DevicePsk: 设备密钥\n        :type DevicePsk: str\n        :param Tags: 设备属性\n        :type Tags: list of DeviceTag\n        :param DeviceType: 设备类型\n        :type DeviceType: int\n        :param Imei: 国际移动设备识别码 IMEI\n        :type Imei: str\n        :param Isp: 运营商类型\n        :type Isp: int\n        :param ConnIP: IP地址\n        :type ConnIP: int\n        :param NbiotDeviceID: NB IoT运营商处的DeviceID\n        :type NbiotDeviceID: str\n        :param LoraDevEui: Lora设备的dev eui\n        :type LoraDevEui: str\n        :param LoraMoteType: Lora设备的mote type\n        :type LoraMoteType: int\n        :param LogLevel: 设备的sdk日志等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogLevel: int\n        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstOnlineTime: int\n        :param LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastOfflineTime: int\n        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param CertState: 设备证书获取状态，0 未获取过设备密钥, 1 已获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertState: int\n        :param EnableState: 设备启用状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableState: int\n        :param Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Labels: list of DeviceLabel\n        :param ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientIP: str\n        :param FirmwareUpdateTime: 设备固件更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirmwareUpdateTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.LastUpdateTime = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.ConnIP = None
        self.NbiotDeviceID = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LogLevel = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None
        self.ClientIP = None
        self.FirmwareUpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.ConnIP = params.get("ConnIP")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LogLevel = params.get("LogLevel")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.ClientIP = params.get("ClientIP")
        self.FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        self.RequestId = params.get("RequestId")


class DescribeDeviceShadowRequest(AbstractModel):
    """DescribeDeviceShadow请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID\n        :type ProductId: str\n        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}\n        :type DeviceName: str\n        """
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
        


class DescribeDeviceShadowResponse(AbstractModel):
    """DescribeDeviceShadow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备影子数据\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID\n        :type ProductId: str\n        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，数值范围 10-250\n        :type Limit: int\n        :param FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备\n        :type FirmwareVersion: str\n        :param DeviceName: 需要过滤的设备名称\n        :type DeviceName: str\n        :param EnableState: 设备是否启用，0禁用状态1启用状态，默认不区分\n        :type EnableState: int\n        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.FirmwareVersion = None
        self.DeviceName = None
        self.EnableState = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.DeviceName = params.get("DeviceName")
        self.EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 设备总数\n        :type TotalCount: int\n        :param Devices: 设备详细信息列表\n        :type Devices: list of DeviceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFirmwareRequest(AbstractModel):
    """DescribeFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareResponse(AbstractModel):
    """DescribeFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param Version: 固件版本号\n        :type Version: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param Md5sum: 固件Md5值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Md5sum: str\n        :param Createtime: 固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type Createtime: int\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param FwType: 固件类型。选项：mcu、module\n        :type FwType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Version = None
        self.ProductId = None
        self.Name = None
        self.Description = None
        self.Md5sum = None
        self.Createtime = None
        self.ProductName = None
        self.FwType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.ProductId = params.get("ProductId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Md5sum = params.get("Md5sum")
        self.Createtime = params.get("Createtime")
        self.ProductName = params.get("ProductName")
        self.FwType = params.get("FwType")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskDevicesRequest(AbstractModel):
    """DescribeFirmwareTaskDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本\n        :type FirmwareVersion: str\n        :param Filters: 筛选条件\n        :type Filters: list of SearchKeyword\n        :param Offset: 查询偏移量\n        :type Offset: int\n        :param Limit: 查询的数量\n        :type Limit: int\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDevicesResponse(AbstractModel):
    """DescribeFirmwareTaskDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param Devices: 固件升级任务的设备列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Devices: list of DeviceUpdateStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceUpdateStatus()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskDistributionRequest(AbstractModel):
    """DescribeFirmwareTaskDistribution请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件升级任务ID\n        :type TaskId: int\n        """
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
        


class DescribeFirmwareTaskDistributionResponse(AbstractModel):
    """DescribeFirmwareTaskDistribution返回参数结构体

    """

    def __init__(self):
        """
        :param StatusInfos: 固件升级任务状态分布信息\n        :type StatusInfos: list of StatusStatistic\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StatusInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatusInfos") is not None:
            self.StatusInfos = []
            for item in params.get("StatusInfos"):
                obj = StatusStatistic()
                obj._deserialize(item)
                self.StatusInfos.append(obj)
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param CreateTime: 固件任务创建时间，单位:秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductName: str\n        :param UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradeMode: str\n        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.Status = None
        self.CreateTime = None
        self.Type = None
        self.ProductName = None
        self.UpgradeMode = None
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Type = params.get("Type")
        self.ProductName = params.get("ProductName")
        self.UpgradeMode = params.get("UpgradeMode")
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskStatisticsResponse(AbstractModel):
    """DescribeFirmwareTaskStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessTotal: 升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessTotal: int\n        :param FailureTotal: 升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailureTotal: int\n        :param UpgradingTotal: 正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradingTotal: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessTotal = None
        self.FailureTotal = None
        self.UpgradingTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessTotal = params.get("SuccessTotal")
        self.FailureTotal = params.get("FailureTotal")
        self.UpgradingTotal = params.get("UpgradingTotal")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTasksRequest(AbstractModel):
    """DescribeFirmwareTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param Offset: 查询偏移量\n        :type Offset: int\n        :param Limit: 返回查询结果条数\n        :type Limit: int\n        :param Filters: 搜索过滤条件\n        :type Filters: list of SearchKeyword\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeFirmwareTasksResponse(AbstractModel):
    """DescribeFirmwareTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfos: 固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskInfos: list of FirmwareTaskInfo\n        :param Total: 固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskInfos = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeLoraDeviceRequest(AbstractModel):
    """DescribeLoraDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        


class DescribeLoraDeviceResponse(AbstractModel):
    """DescribeLoraDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param AppEui: LoRa应用UUID\n        :type AppEui: str\n        :param DeviceEui: LoRa设备UUID\n        :type DeviceEui: str\n        :param AppKey: LoRa应用密钥\n        :type AppKey: str\n        :param ClassType: 设备类型,目前支持A、B、C三种\n        :type ClassType: str\n        :param ProductId: 设备所属产品id\n        :type ProductId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeviceName = None
        self.AppEui = None
        self.DeviceEui = None
        self.AppKey = None
        self.ClassType = None
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.AppKey = params.get("AppKey")
        self.ClassType = params.get("ClassType")
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class DescribeMultiDevTaskRequest(AbstractModel):
    """DescribeMultiDevTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID，由批量创建设备接口返回\n        :type TaskId: str\n        :param ProductId: 产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID\n        :type ProductId: str\n        """
        self.TaskId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMultiDevTaskResponse(AbstractModel):
    """DescribeMultiDevTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID\n        :type TaskId: str\n        :param TaskStatus: 任务是否完成。0 代表任务未开始，1 代表任务正在执行，2 代表任务已完成\n        :type TaskStatus: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeMultiDevicesRequest(AbstractModel):
    """DescribeMultiDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID\n        :type ProductId: str\n        :param TaskId: 任务 ID，由批量创建设备接口返回\n        :type TaskId: str\n        :param Offset: 分页偏移\n        :type Offset: int\n        :param Limit: 分页大小，每页返回的设备个数\n        :type Limit: int\n        """
        self.ProductId = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMultiDevicesResponse(AbstractModel):
    """DescribeMultiDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID，由批量创建设备接口返回\n        :type TaskId: str\n        :param DevicesInfo: 设备详细信息列表\n        :type DevicesInfo: list of MultiDevicesInfo\n        :param TotalDevNum: 该任务创建设备的总数\n        :type TotalDevNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.DevicesInfo = None
        self.TotalDevNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("DevicesInfo") is not None:
            self.DevicesInfo = []
            for item in params.get("DevicesInfo"):
                obj = MultiDevicesInfo()
                obj._deserialize(item)
                self.DevicesInfo.append(obj)
        self.TotalDevNum = params.get("TotalDevNum")
        self.RequestId = params.get("RequestId")


class DescribeProductResourceRequest(AbstractModel):
    """DescribeProductResource请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 需要查看资源列表的产品 ID\n        :type ProductID: str\n        :param Name: 需要过滤的资源名称\n        :type Name: str\n        """
        self.ProductID = None
        self.Name = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResourceResponse(AbstractModel):
    """DescribeProductResource返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 资源详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.iotcloud.v20180614.models.ProductResourceInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ProductResourceInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeProductResourcesRequest(AbstractModel):
    """DescribeProductResources请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，数值范围 10-250\n        :type Limit: int\n        :param ProductID: 需要查看资源列表的产品 ID\n        :type ProductID: str\n        :param Name: 需要过滤的资源名称\n        :type Name: str\n        """
        self.Offset = None
        self.Limit = None
        self.ProductID = None
        self.Name = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResourcesResponse(AbstractModel):
    """DescribeProductResources返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 资源总数\n        :type TotalCount: int\n        :param Result: 资源详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: list of ProductResourceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ProductResourceInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductTaskRequest(AbstractModel):
    """DescribeProductTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param TaskId: 任务ID\n        :type TaskId: int\n        """
        self.ProductId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductTaskResponse(AbstractModel):
    """DescribeProductTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfo: 产品任务详细信息\n        :type TaskInfo: :class:`tencentcloud.iotcloud.v20180614.models.ProductTaskInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = ProductTaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.RequestId = params.get("RequestId")


class DescribeProductTasksRequest(AbstractModel):
    """DescribeProductTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Offset: 产品级别任务列表偏移量\n        :type Offset: int\n        :param Limit: 产品级别任务列表拉取个数\n        :type Limit: int\n        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductTasksResponse(AbstractModel):
    """DescribeProductTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的任务总个数\n        :type TotalCount: int\n        :param TaskInfos: 任务详细信息列表\n        :type TaskInfos: list of ProductTaskInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TaskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = ProductTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param Limit: 分页大小，当前页面中显示的最大数量，值范围 10-250。\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 产品总数\n        :type TotalCount: int\n        :param Products: 产品详细信息列表\n        :type Products: list of ProductInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePushResourceTaskStatisticsRequest(AbstractModel):
    """DescribePushResourceTaskStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Name: 资源名称\n        :type Name: str\n        """
        self.ProductID = None
        self.Name = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushResourceTaskStatisticsResponse(AbstractModel):
    """DescribePushResourceTaskStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessTotal: 推送成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessTotal: int\n        :param FailureTotal: 推送失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailureTotal: int\n        :param UpgradingTotal: 正在推送的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradingTotal: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessTotal = None
        self.FailureTotal = None
        self.UpgradingTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessTotal = params.get("SuccessTotal")
        self.FailureTotal = params.get("FailureTotal")
        self.UpgradingTotal = params.get("UpgradingTotal")
        self.RequestId = params.get("RequestId")


class DescribeResourceTasksRequest(AbstractModel):
    """DescribeResourceTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Name: 资源名称\n        :type Name: str\n        :param Offset: 查询偏移量\n        :type Offset: int\n        :param Limit: 返回查询结果条数\n        :type Limit: int\n        :param Filters: 搜索过滤条件\n        :type Filters: list of SearchKeyword\n        """
        self.ProductID = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeResourceTasksResponse(AbstractModel):
    """DescribeResourceTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfos: 资源任务列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskInfos: list of FirmwareTaskInfo\n        :param Total: 资源任务总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskInfos = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        """
        :param Type: 任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”\n        :type Type: str\n        :param Id: 任务 ID\n        :type Id: str\n        :param ProductId: 产品 ID\n        :type ProductId: str\n        :param Status: 状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消\n        :type Status: int\n        :param CreateTime: 任务创建时间，Unix 时间戳\n        :type CreateTime: int\n        :param UpdateTime: 最后任务更新时间，Unix 时间戳\n        :type UpdateTime: int\n        :param DoneTime: 任务完成时间，Unix 时间戳\n        :type DoneTime: int\n        :param ScheduleTime: 被调度时间，Unix 时间戳\n        :type ScheduleTime: int\n        :param RetCode: 返回的错误码\n        :type RetCode: int\n        :param ErrMsg: 返回的错误信息\n        :type ErrMsg: str\n        :param Percent: 完成任务的设备比例\n        :type Percent: int\n        :param AllDeviceCnt: 匹配到的需执行任务的设备数目\n        :type AllDeviceCnt: int\n        :param DoneDeviceCnt: 已完成任务的设备数目\n        :type DoneDeviceCnt: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Type = None
        self.Id = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DoneTime = None
        self.ScheduleTime = None
        self.RetCode = None
        self.ErrMsg = None
        self.Percent = None
        self.AllDeviceCnt = None
        self.DoneDeviceCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DoneTime = params.get("DoneTime")
        self.ScheduleTime = params.get("ScheduleTime")
        self.RetCode = params.get("RetCode")
        self.ErrMsg = params.get("ErrMsg")
        self.Percent = params.get("Percent")
        self.AllDeviceCnt = params.get("AllDeviceCnt")
        self.DoneDeviceCnt = params.get("DoneDeviceCnt")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，数值范围 1-250\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 用户一个月内创建的任务总数\n        :type TotalCount: int\n        :param Tasks: 此页任务对象的数组，按创建时间排序\n        :type Tasks: list of TaskInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param Online: 设备是否在线，0不在线，1在线\n        :type Online: int\n        :param LoginTime: 设备登录时间\n        :type LoginTime: int\n        :param Version: 设备版本\n        :type Version: str\n        :param DeviceCert: 设备证书，证书加密的设备返回\n        :type DeviceCert: str\n        :param DevicePsk: 设备密钥，密钥加密的设备返回\n        :type DevicePsk: str\n        :param Tags: 设备属性\n        :type Tags: list of DeviceTag\n        :param DeviceType: 设备类型\n        :type DeviceType: int\n        :param Imei: 国际移动设备识别码 IMEI\n        :type Imei: str\n        :param Isp: 运营商类型\n        :type Isp: int\n        :param NbiotDeviceID: NB IOT运营商处的DeviceID\n        :type NbiotDeviceID: str\n        :param ConnIP: IP地址\n        :type ConnIP: int\n        :param LastUpdateTime: 设备最后更新时间\n        :type LastUpdateTime: int\n        :param LoraDevEui: LoRa设备的dev eui\n        :type LoraDevEui: str\n        :param LoraMoteType: LoRa设备的Mote type\n        :type LoraMoteType: int\n        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstOnlineTime: int\n        :param LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastOfflineTime: int\n        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param LogLevel: 设备日志级别
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogLevel: int\n        :param CertState: 设备证书获取状态, 1 已获取过设备密钥，0 未获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertState: int\n        :param EnableState: 设备可用状态，0禁用，1启用
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableState: int\n        :param Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Labels: list of DeviceLabel\n        :param ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientIP: str\n        :param FirmwareUpdateTime: ota最后更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirmwareUpdateTime: int\n        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.NbiotDeviceID = None
        self.ConnIP = None
        self.LastUpdateTime = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.LogLevel = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None
        self.ClientIP = None
        self.FirmwareUpdateTime = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.ConnIP = params.get("ConnIP")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.LogLevel = params.get("LogLevel")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.ClientIP = params.get("ClientIP")
        self.FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLabel(AbstractModel):
    """设备标签

    """

    def __init__(self):
        """
        :param Key: 标签标识\n        :type Key: str\n        :param Value: 标签值\n        :type Value: str\n        """
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
        


class DeviceProperty(AbstractModel):
    """设备资源信息。

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param ProductName: 产品名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductName: str\n        :param DeviceName: 设备名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceName: str\n        :param ResourceId: 设备资源ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceId: str\n        """
        self.ProductId = None
        self.ProductName = None
        self.DeviceName = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.DeviceName = params.get("DeviceName")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceResourceInfo(AbstractModel):
    """设备资源详细信息

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param ProductName: 产品名\n        :type ProductName: str\n        :param Name: 资源名称\n        :type Name: str\n        :param Md5: 资源文件md5\n        :type Md5: str\n        :param Size: 资源文件大小\n        :type Size: int\n        :param UpdateTime: 资源更新时间\n        :type UpdateTime: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Status: 设备资源上传状态\n        :type Status: int\n        :param Percent: 设备资源上传百分比\n        :type Percent: int\n        """
        self.ProductID = None
        self.ProductName = None
        self.Name = None
        self.Md5 = None
        self.Size = None
        self.UpdateTime = None
        self.DeviceName = None
        self.Status = None
        self.Percent = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.ProductName = params.get("ProductName")
        self.Name = params.get("Name")
        self.Md5 = params.get("Md5")
        self.Size = params.get("Size")
        self.UpdateTime = params.get("UpdateTime")
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTag(AbstractModel):
    """设备属性

    """

    def __init__(self):
        """
        :param Tag: 属性名称\n        :type Tag: str\n        :param Type: 属性值的类型，1 int，2 string\n        :type Type: int\n        :param Value: 属性的值\n        :type Value: str\n        :param Name: 属性描述名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
        self.Tag = None
        self.Type = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUpdateStatus(AbstractModel):
    """设备固件更新状态

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param LastProcessTime: 最后处理时间\n        :type LastProcessTime: int\n        :param Status: 状态\n        :type Status: int\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param Retcode: 返回码\n        :type Retcode: int\n        :param DstVersion: 目标更新版本\n        :type DstVersion: str\n        :param Percent: 下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Percent: int\n        :param OriVersion: 原版本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriVersion: str\n        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        """
        self.DeviceName = None
        self.LastProcessTime = None
        self.Status = None
        self.ErrMsg = None
        self.Retcode = None
        self.DstVersion = None
        self.Percent = None
        self.OriVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.LastProcessTime = params.get("LastProcessTime")
        self.Status = params.get("Status")
        self.ErrMsg = params.get("ErrMsg")
        self.Retcode = params.get("Retcode")
        self.DstVersion = params.get("DstVersion")
        self.Percent = params.get("Percent")
        self.OriVersion = params.get("OriVersion")
        self.TaskId = params.get("TaskId")
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


class EditFirmwareRequest(AbstractModel):
    """EditFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID。\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号。\n        :type FirmwareVersion: str\n        :param FirmwareName: 固件名称。\n        :type FirmwareName: str\n        :param FirmwareDescription: 固件描述\n        :type FirmwareDescription: str\n        :param FwType: 固件类型：选填 mcu、moudule。默认：mcu\n        :type FwType: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.FirmwareName = None
        self.FirmwareDescription = None
        self.FwType = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")
        self.FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditFirmwareResponse(AbstractModel):
    """EditFirmware返回参数结构体

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


class FirmwareTaskInfo(AbstractModel):
    """固件升级任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        """
        self.TaskId = None
        self.Status = None
        self.Type = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
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
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
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


class GetUserResourceInfoRequest(AbstractModel):
    """GetUserResourceInfo请求参数结构体

    """


class GetUserResourceInfoResponse(AbstractModel):
    """GetUserResourceInfo返回参数结构体

    """

    def __init__(self):
        """
        :param UsedSize: 已使用的资源字节数\n        :type UsedSize: int\n        :param Limit: 可以使用资源的总大小\n        :type Limit: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.UsedSize = None
        self.Limit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UsedSize = params.get("UsedSize")
        self.Limit = params.get("Limit")
        self.RequestId = params.get("RequestId")


class MultiDevicesInfo(AbstractModel):
    """创建设备时返回的设备信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param DevicePsk: 对称加密密钥，base64 编码，采用对称加密时返回该参数\n        :type DevicePsk: str\n        :param DeviceCert: 设备证书，采用非对称加密时返回该参数\n        :type DeviceCert: str\n        :param DevicePrivateKey: 设备私钥，采用非对称加密时返回该参数，腾讯云为用户缓存起来，其生命周期与任务生命周期一致\n        :type DevicePrivateKey: str\n        :param Result: 错误码\n        :type Result: int\n        :param ErrMsg: 错误信息\n        :type ErrMsg: str\n        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.Result = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """产品详细信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名\n        :type ProductName: str\n        :param ProductMetadata: 产品元数据\n        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20180614.models.ProductMetadata`\n        :param ProductProperties: 产品属性\n        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`\n        """
        self.ProductId = None
        self.ProductName = None
        self.ProductMetadata = None
        self.ProductProperties = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self.ProductMetadata = ProductMetadata()
            self.ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductMetadata(AbstractModel):
    """产品元数据

    """

    def __init__(self):
        """
        :param CreationDate: 产品创建时间\n        :type CreationDate: int\n        """
        self.CreationDate = None


    def _deserialize(self, params):
        self.CreationDate = params.get("CreationDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductProperties(AbstractModel):
    """产品属性

    """

    def __init__(self):
        """
        :param ProductDescription: 产品描述\n        :type ProductDescription: str\n        :param EncryptionType: 加密类型，1表示证书认证，2表示签名认证。如不填写，默认值是1\n        :type EncryptionType: str\n        :param Region: 产品所属区域，目前只支持广州（gz）\n        :type Region: str\n        :param ProductType: 产品类型，各个类型值代表的节点-类型如下：
0 普通产品，2 NB-IoT产品，4 LoRa产品，3 LoRa网关产品，5 普通网关产品   默认值是0\n        :type ProductType: int\n        :param Format: 数据格式，取值为json或者custom，默认值是json\n        :type Format: str\n        :param Platform: 产品所属平台，默认值是0\n        :type Platform: str\n        :param Appeui: LoRa产品运营侧APPEUI，只有LoRa产品需要填写\n        :type Appeui: str\n        :param ModelId: 产品绑定的物模型ID，-1表示不绑定\n        :type ModelId: str\n        :param ModelName: 产品绑定的物模型名称\n        :type ModelName: str\n        :param ProductKey: 产品密钥，suite产品才会有\n        :type ProductKey: str\n        :param RegisterType: 动态注册类型 0-关闭, 1-预定义设备名 2-动态定义设备名\n        :type RegisterType: int\n        :param ProductSecret: 动态注册产品秘钥\n        :type ProductSecret: str\n        :param RegisterLimit: RegisterType为2时，设备动态创建的限制数量\n        :type RegisterLimit: int\n        """
        self.ProductDescription = None
        self.EncryptionType = None
        self.Region = None
        self.ProductType = None
        self.Format = None
        self.Platform = None
        self.Appeui = None
        self.ModelId = None
        self.ModelName = None
        self.ProductKey = None
        self.RegisterType = None
        self.ProductSecret = None
        self.RegisterLimit = None


    def _deserialize(self, params):
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.Format = params.get("Format")
        self.Platform = params.get("Platform")
        self.Appeui = params.get("Appeui")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ProductKey = params.get("ProductKey")
        self.RegisterType = params.get("RegisterType")
        self.ProductSecret = params.get("ProductSecret")
        self.RegisterLimit = params.get("RegisterLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductResourceInfo(AbstractModel):
    """产品资源详细信息

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param ProductName: 产品名\n        :type ProductName: str\n        :param Name: 资源名称\n        :type Name: str\n        :param Md5: 资源文件md5\n        :type Md5: str\n        :param Size: 资源文件大小\n        :type Size: int\n        :param Description: 资源文件描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param CreateTime: 资源创建时间\n        :type CreateTime: str\n        """
        self.ProductID = None
        self.ProductName = None
        self.Name = None
        self.Md5 = None
        self.Size = None
        self.Description = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.ProductName = params.get("ProductName")
        self.Name = params.get("Name")
        self.Md5 = params.get("Md5")
        self.Size = params.get("Size")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductTaskInfo(AbstractModel):
    """产品级任务详细信息

    """

    def __init__(self):
        """
        :param Id: 任务ID\n        :type Id: int\n        :param Type: 任务类型 0-批量创建设备类型\n        :type Type: int\n        :param State: 任务状态 0-创建中 1-待执行 2-执行中 3-执行失败 4-子任务部分失败 5-执行成功\n        :type State: int\n        :param ParametersType: 任务参数类型 cosfile-文件输入 random-随机生成\n        :type ParametersType: str\n        :param Parameters: 任务参数\n        :type Parameters: str\n        :param ResultType: 任务执行结果类型 cosfile-文件输出 errmsg-错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultType: str\n        :param Result: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param BatchCount: 子任务总个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchCount: int\n        :param BatchOffset: 子任务已执行个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchOffset: int\n        :param CreateTime: 任务创建时间\n        :type CreateTime: int\n        :param UpdateTime: 任务更新时间\n        :type UpdateTime: int\n        :param CompleteTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CompleteTime: int\n        """
        self.Id = None
        self.Type = None
        self.State = None
        self.ParametersType = None
        self.Parameters = None
        self.ResultType = None
        self.Result = None
        self.BatchCount = None
        self.BatchOffset = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CompleteTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.State = params.get("State")
        self.ParametersType = params.get("ParametersType")
        self.Parameters = params.get("Parameters")
        self.ResultType = params.get("ResultType")
        self.Result = params.get("Result")
        self.BatchCount = params.get("BatchCount")
        self.BatchOffset = params.get("BatchOffset")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CompleteTime = params.get("CompleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishAsDeviceRequest(AbstractModel):
    """PublishAsDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Port: LoRa 设备端口\n        :type Port: int\n        :param Payload: 消息内容\n        :type Payload: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Port = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Port = params.get("Port")
        self.Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishAsDeviceResponse(AbstractModel):
    """PublishAsDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PublishBroadcastMessageRequest(AbstractModel):
    """PublishBroadcastMessage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Payload: 消息内容\n        :type Payload: str\n        :param Qos: 消息质量等级\n        :type Qos: int\n        :param PayloadEncoding: Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备\n        :type PayloadEncoding: str\n        """
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
        """
        :param TaskId: 广播消息任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: 消息发往的主题。命名规则：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}\n        :type Topic: str\n        :param Payload: 消息内容\n        :type Payload: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Qos: 服务质量等级，取值为0或1\n        :type Qos: int\n        :param PayloadEncoding: Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备\n        :type PayloadEncoding: str\n        """
        self.Topic = None
        self.Payload = None
        self.ProductId = None
        self.DeviceName = None
        self.Qos = None
        self.PayloadEncoding = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
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


class PublishRRPCMessageRequest(AbstractModel):
    """PublishRRPCMessage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Payload: 消息内容，utf8编码\n        :type Payload: str\n        """
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
        """
        :param MessageId: RRPC消息ID\n        :type MessageId: int\n        :param PayloadBase64: 设备回复的消息内容，采用base64编码\n        :type PayloadBase64: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MessageId = None
        self.PayloadBase64 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.PayloadBase64 = params.get("PayloadBase64")
        self.RequestId = params.get("RequestId")


class PublishToDeviceRequest(AbstractModel):
    """PublishToDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Port: LoRa 端口\n        :type Port: int\n        :param Payload: 消息内容\n        :type Payload: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Port = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Port = params.get("Port")
        self.Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishToDeviceResponse(AbstractModel):
    """PublishToDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceTopicRuleRequest(AbstractModel):
    """ReplaceTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称\n        :type RuleName: str\n        :param TopicRulePayload: 替换的规则包体\n        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`\n        :param ModifyType: 修改类型，0：其他，1：创建行为，2：更新行为，3：删除行为\n        :type ModifyType: int\n        :param ActionIndex: action增删改变更填对应topicRulePayload里面第几个action\n        :type ActionIndex: int\n        """
        self.RuleName = None
        self.TopicRulePayload = None
        self.ModifyType = None
        self.ActionIndex = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        self.ModifyType = params.get("ModifyType")
        self.ActionIndex = params.get("ActionIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceTopicRuleResponse(AbstractModel):
    """ReplaceTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceResult(AbstractModel):
    """重置设备状态结果

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param Success: 是否成功\n        :type Success: bool\n        :param Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        """
        self.DeviceName = None
        self.Success = None
        self.Reason = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Success = params.get("Success")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceStateRequest(AbstractModel):
    """ResetDeviceState请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceNames: 设备名称\n        :type DeviceNames: list of str\n        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceStateResponse(AbstractModel):
    """ResetDeviceState返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessCount: 批量重置设备成功数\n        :type SuccessCount: int\n        :param ResetDeviceResults: 批量重置设备结果\n        :type ResetDeviceResults: list of ResetDeviceResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessCount = None
        self.ResetDeviceResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        if params.get("ResetDeviceResults") is not None:
            self.ResetDeviceResults = []
            for item in params.get("ResetDeviceResults"):
                obj = ResetDeviceResult()
                obj._deserialize(item)
                self.ResetDeviceResults.append(obj)
        self.RequestId = params.get("RequestId")


class RetryDeviceFirmwareTaskRequest(AbstractModel):
    """RetryDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件升级任务ID\n        :type TaskId: int\n        """
        self.ProductID = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDeviceFirmwareTaskResponse(AbstractModel):
    """RetryDeviceFirmwareTask返回参数结构体

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
        


class StatusStatistic(AbstractModel):
    """状态统计信息

    """

    def __init__(self):
        """
        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param Total: 统计总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        """
        self.Status = None
        self.Total = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务描述细节

    """

    def __init__(self):
        """
        :param UpdateShadowTask: 批量更新影子任务的描述细节，当 taskType 取值为 “UpdateShadow” 时，此字段必填。描述见下 BatchUpdateShadow\n        :type UpdateShadowTask: :class:`tencentcloud.iotcloud.v20180614.models.BatchUpdateShadow`\n        :param PublishMessageTask: 批量下发消息任务的描述细节，当 taskType 取值为 “PublishMessage” 时，此字段必填。描述见下 BatchPublishMessage\n        :type PublishMessageTask: :class:`tencentcloud.iotcloud.v20180614.models.BatchPublishMessage`\n        """
        self.UpdateShadowTask = None
        self.PublishMessageTask = None


    def _deserialize(self, params):
        if params.get("UpdateShadowTask") is not None:
            self.UpdateShadowTask = BatchUpdateShadow()
            self.UpdateShadowTask._deserialize(params.get("UpdateShadowTask"))
        if params.get("PublishMessageTask") is not None:
            self.PublishMessageTask = BatchPublishMessage()
            self.PublishMessageTask._deserialize(params.get("PublishMessageTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """任务列表详细信息

    """

    def __init__(self):
        """
        :param Type: 任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”\n        :type Type: str\n        :param Id: 任务 ID\n        :type Id: str\n        :param ProductId: 产品 ID\n        :type ProductId: str\n        :param Status: 状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消\n        :type Status: int\n        :param CreateTime: 任务创建时间，Unix 时间戳\n        :type CreateTime: int\n        :param UpdateTime: 最后任务更新时间，Unix 时间戳\n        :type UpdateTime: int\n        :param RetCode: 返回的错误码\n        :type RetCode: int\n        :param ErrMsg: 返回的错误信息\n        :type ErrMsg: str\n        """
        self.Type = None
        self.Id = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.RetCode = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.RetCode = params.get("RetCode")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRulePayload(AbstractModel):
    """创建规则请求包体

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
            "api": "http://127.0.0.1:8080",
            "token":"xxx"
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
        


class UnbindDevicesRequest(AbstractModel):
    """UnbindDevices请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayProductId: 网关设备的产品ID\n        :type GatewayProductId: str\n        :param GatewayDeviceName: 网关设备的设备名\n        :type GatewayDeviceName: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceNames: 多个设备名\n        :type DeviceNames: list of str\n        :param Skey: 中兴CLAA设备的解绑需要Skey，普通设备不需要\n        :type Skey: str\n        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None
        self.Skey = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Skey = params.get("Skey")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceAvailableStateRequest(AbstractModel):
    """UpdateDeviceAvailableState请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param EnableState: 要设置的设备状态，1为启用，0为禁用\n        :type EnableState: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.EnableState = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceAvailableStateResponse(AbstractModel):
    """UpdateDeviceAvailableState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceShadowRequest(AbstractModel):
    """UpdateDeviceShadow请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param State: 虚拟设备的状态，JSON字符串格式，由desired结构组成\n        :type State: str\n        :param ShadowVersion: 当前版本号，需要和后台的version保持一致，才能更新成功\n        :type ShadowVersion: int\n        :param Prefix: 下发delta消息的topic前缀，可选类型: "$shadow","$template"。不填写默认"$shadow"。\n        :type Prefix: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.State = None
        self.ShadowVersion = None
        self.Prefix = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.State = params.get("State")
        self.ShadowVersion = params.get("ShadowVersion")
        self.Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceShadowResponse(AbstractModel):
    """UpdateDeviceShadow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备影子数据，JSON字符串格式\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UpdateTopicPolicyRequest(AbstractModel):
    """UpdateTopicPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param TopicName: 更新前Topic名\n        :type TopicName: str\n        :param NewTopicName: 更新后Topic名\n        :type NewTopicName: str\n        :param Privilege: Topic权限\n        :type Privilege: int\n        :param BrokerSubscribe: 代理订阅信息\n        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`\n        """
        self.ProductID = None
        self.TopicName = None
        self.NewTopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.TopicName = params.get("TopicName")
        self.NewTopicName = params.get("NewTopicName")
        self.Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self.BrokerSubscribe = BrokerSubscribe()
            self.BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTopicPolicyResponse(AbstractModel):
    """UpdateTopicPolicy返回参数结构体

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
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param Md5sum: 固件的MD5值\n        :type Md5sum: str\n        :param FileSize: 固件的大小\n        :type FileSize: int\n        :param FirmwareName: 固件名称\n        :type FirmwareName: str\n        :param FirmwareDescription: 固件描述\n        :type FirmwareDescription: str\n        :param FwType: 固件类型：选填 mcu、moudule。默认：mcu\n        :type FwType: str\n        """
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