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
        r"""
        :param Tags: 属性列表
        :type Tags: list of DeviceTag
        """
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
        


class BatchUpdateFirmwareRequest(AbstractModel):
    """BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件新版本号
        :type FirmwareVersion: str
        :param FirmwareOriVersion: 固件原版本号，根据文件列表升级固件不需要填写此参数
        :type FirmwareOriVersion: str
        :param UpgradeMethod: 升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式
        :type UpgradeMethod: int
        :param FileName: 设备列表文件名称，根据文件列表升级固件需要填写此参数
        :type FileName: str
        :param FileMd5: 设备列表的文件md5值
        :type FileMd5: str
        :param FileSize: 设备列表的文件大小值
        :type FileSize: int
        :param DeviceNames: 需要升级的设备名称列表
        :type DeviceNames: list of str
        :param TimeoutInterval: 固件升级任务，默认超时时间。 最小取值60秒，最大为3600秒
        :type TimeoutInterval: int
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.FirmwareOriVersion = None
        self.UpgradeMethod = None
        self.FileName = None
        self.FileMd5 = None
        self.FileSize = None
        self.DeviceNames = None
        self.TimeoutInterval = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindDeviceInfo(AbstractModel):
    """子设备信息

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Tags: 设备Tag
        :type Tags: list of DeviceTag
        :param BindTime: 子设备绑定时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BindTime: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Tags = None
        self.BindTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BindTime = params.get("BindTime")
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
        :param GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param ProductId: 被绑定设备的产品ID
        :type ProductId: str
        :param DeviceNames: 被绑定的多个设备名
        :type DeviceNames: list of str
        :param Skey: 中兴CLAA设备的绑定需要skey，普通的设备不需要
        :type Skey: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindProductInfo(AbstractModel):
    """子产品信息

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名
        :type ProductName: str
        """
        self.ProductId = None
        self.ProductName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrokerSubscribe(AbstractModel):
    """代理订阅信息

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
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
        


class CLSLogItem(AbstractModel):
    """CLS日志

    """

    def __init__(self):
        r"""
        :param Content: 日志内容
        :type Content: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param RequestId: 请求ID
        :type RequestId: str
        :param Result: 结果
        :type Result: str
        :param Scene: 模块
        :type Scene: str
        :param Time: 日志时间
        :type Time: str
        :param Userid: 腾讯云账号
        :type Userid: str
        """
        self.Content = None
        self.DeviceName = None
        self.ProductId = None
        self.RequestId = None
        self.Result = None
        self.Scene = None
        self.Time = None
        self.Userid = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.DeviceName = params.get("DeviceName")
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")
        self.Result = params.get("Result")
        self.Scene = params.get("Scene")
        self.Time = params.get("Time")
        self.Userid = params.get("Userid")
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CertInfo(AbstractModel):
    """X509证书信息

    """

    def __init__(self):
        r"""
        :param CertName: 证书名称
        :type CertName: str
        :param CertSN: 证书的序列号，16进制编码
        :type CertSN: str
        :param IssuerName: 证书颁发着名称
        :type IssuerName: str
        :param Subject: 证书主题
        :type Subject: str
        :param CreateTime: 证书创建时间，秒级时间戳
        :type CreateTime: int
        :param EffectiveTime: 证书生效时间，秒级时间戳
        :type EffectiveTime: int
        :param ExpireTime: 证书失效时间，秒级时间戳
        :type ExpireTime: int
        :param CertText: X509证书内容
        :type CertText: str
        """
        self.CertName = None
        self.CertSN = None
        self.IssuerName = None
        self.Subject = None
        self.CreateTime = None
        self.EffectiveTime = None
        self.ExpireTime = None
        self.CertText = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertSN = params.get("CertSN")
        self.IssuerName = params.get("IssuerName")
        self.Subject = params.get("Subject")
        self.CreateTime = params.get("CreateTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.ExpireTime = params.get("ExpireTime")
        self.CertText = params.get("CertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param Attribute: 设备属性
        :type Attribute: :class:`tencentcloud.iotcloud.v20210408.models.Attribute`
        :param DefinedPsk: 是否使用自定义PSK，默认不使用
        :type DefinedPsk: str
        :param Isp: 运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通
        :type Isp: int
        :param Imei: IMEI，当产品是NB-IoT产品时，此字段必填
        :type Imei: str
        :param LoraDevEui: LoRa设备的DevEui，当创建LoRa时，此字段必填
        :type LoraDevEui: str
        :param LoraMoteType: LoRa设备的MoteType
        :type LoraMoteType: int
        :param Skey: 创建LoRa设备需要skey
        :type Skey: str
        :param LoraAppKey: LoRa设备的AppKey
        :type LoraAppKey: str
        :param TlsCrt: 私有CA创建的设备证书
        :type TlsCrt: str
        """
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
        self.TlsCrt = None


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
        self.TlsCrt = params.get("TlsCrt")
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
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数
        :type DevicePsk: str
        :param DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数
        :type DeviceCert: str
        :param DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数
        :type DevicePrivateKey: str
        :param LoraDevEui: LoRa设备的DevEui，当设备是LoRa设备时，会返回该字段
        :type LoraDevEui: str
        :param LoraMoteType: LoRa设备的MoteType，当设备是LoRa设备时，会返回该字段
        :type LoraMoteType: int
        :param LoraAppKey: LoRa设备的AppKey，当设备是LoRa设备时，会返回该字段
        :type LoraAppKey: str
        :param LoraNwkKey: LoRa设备的NwkKey，当设备是LoRa设备时，会返回该字段
        :type LoraNwkKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class CreateMultiDevicesTaskRequest(AbstractModel):
    """CreateMultiDevicesTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ParametersType: 参数类型 cosfile-文件上传 random-随机创建
        :type ParametersType: str
        :param FileName: 文件上传类型时文件名
        :type FileName: str
        :param FileSize: 文件上传类型时文件大小
        :type FileSize: int
        :param BatchCount: 随机创建时设备创建个数
        :type BatchCount: int
        :param Hash: 文件上传类型时文件md5值
        :type Hash: str
        """
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
        r"""
        :param Id: 任务ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreatePrivateCARequest(AbstractModel):
    """CreatePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertName: CA证书名称
        :type CertName: str
        :param CertText: CA证书内容
        :type CertText: str
        :param VerifyCertText: 校验CA证书的证书内容
        :type VerifyCertText: str
        """
        self.CertName = None
        self.CertText = None
        self.VerifyCertText = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertText = params.get("CertText")
        self.VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateCAResponse(AbstractModel):
    """CreatePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param Skey: 创建CLAA产品时，需要Skey
        :type Skey: str
        """
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
        r"""
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductId: 产品 ID，腾讯云生成全局唯一 ID
        :type ProductId: str
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        


class CreateTaskFileUrlResponse(AbstractModel):
    """CreateTaskFileUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 任务文件上传链接
        :type Url: str
        :param FileName: 任务文件名
        :type FileName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.FileName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileName = params.get("FileName")
        self.RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品自身ID
        :type ProductId: str
        :param TopicName: Topic名称
        :type TopicName: str
        :param Privilege: Topic权限，1发布，2订阅，3订阅和发布
        :type Privilege: int
        :param BrokerSubscribe: 代理订阅信息，网关产品为绑定的子产品创建topic时需要填写，内容为子产品的ID和设备信息。
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20210408.models.BrokerSubscribe`
        """
        self.ProductId = None
        self.TopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20210408.models.TopicRulePayload`
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
        :param ProductId: 设备所属的产品 ID
        :type ProductId: str
        :param DeviceName: 需要删除的设备名称
        :type DeviceName: str
        :param Skey: 删除LoRa设备以及LoRa网关设备需要skey
        :type Skey: str
        """
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
        


class DeleteDeviceResourceRequest(AbstractModel):
    """DeleteDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param Name: 资源名称
        :type Name: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductID = None
        self.Name = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResourceResponse(AbstractModel):
    """DeleteDeviceResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceShadowRequest(AbstractModel):
    """DeleteDeviceShadow请求参数结构体

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
        


class DeleteDeviceShadowResponse(AbstractModel):
    """DeleteDeviceShadow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivateCARequest(AbstractModel):
    """DeletePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertName: 私有CA证书名称
        :type CertName: str
        """
        self.CertName = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateCAResponse(AbstractModel):
    """DeletePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProductPrivateCARequest(AbstractModel):
    """DeleteProductPrivateCA请求参数结构体

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
        


class DeleteProductPrivateCAResponse(AbstractModel):
    """DeleteProductPrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 需要删除的产品 ID
        :type ProductId: str
        :param Skey: 删除LoRa产品需要skey
        :type Skey: str
        """
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


class DescribeDeviceClientKeyRequest(AbstractModel):
    """DescribeDeviceClientKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 所属产品的Id
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
        


class DescribeDeviceClientKeyResponse(AbstractModel):
    """DescribeDeviceClientKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClientKey: 设备的私钥
        :type ClientKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientKey = params.get("ClientKey")
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
        


class DescribeDeviceResourceRequest(AbstractModel):
    """DescribeDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param Name: 具体的设备资源名称
        :type Name: str
        """
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
        r"""
        :param Result: 设备资源详情
        :type Result: :class:`tencentcloud.iotcloud.v20210408.models.DeviceResourceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param ProductID: 产品ID
        :type ProductID: str
        :param DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        :param StartTime: 资源搜索开始时间
        :type StartTime: str
        :param EndTime: 资源搜索结束时间
        :type EndTime: str
        """
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
        r"""
        :param TotalCount: 资源总数
        :type TotalCount: int
        :param Result: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of DeviceResourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线
        :type Online: int
        :param LoginTime: 设备登录时间
        :type LoginTime: int
        :param Version: 设备固件版本
        :type Version: str
        :param LastUpdateTime: 设备最后更新时间
        :type LastUpdateTime: int
        :param DeviceCert: 设备证书
        :type DeviceCert: str
        :param DevicePsk: 设备密钥
        :type DevicePsk: str
        :param Tags: 设备属性
        :type Tags: list of DeviceTag
        :param DeviceType: 设备类型
        :type DeviceType: int
        :param Imei: 国际移动设备识别码 IMEI
        :type Imei: str
        :param Isp: 运营商类型
        :type Isp: int
        :param ConnIP: IP地址
        :type ConnIP: int
        :param NbiotDeviceID: NB IoT运营商处的DeviceID
        :type NbiotDeviceID: str
        :param LoraDevEui: Lora设备的dev eui
        :type LoraDevEui: str
        :param LoraMoteType: Lora设备的mote type
        :type LoraMoteType: int
        :param LogLevel: 设备的sdk日志等级
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param CertState: 设备证书获取状态，0 未获取过设备密钥, 1 已获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        :param EnableState: 设备启用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        :param ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param FirmwareUpdateTime: 设备固件更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirmwareUpdateTime: int
        :param CreateUserId: 创建者账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        self.CreateUserId = None
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
        self.CreateUserId = params.get("CreateUserId")
        self.RequestId = params.get("RequestId")


class DescribeDeviceShadowRequest(AbstractModel):
    """DescribeDeviceShadow请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品 ID
        :type ProductId: str
        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,60}
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
        


class DescribeDeviceShadowResponse(AbstractModel):
    """DescribeDeviceShadow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 设备影子数据
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :type FirmwareVersion: str
        :param DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        :param EnableState: 设备是否启用，0禁用状态1启用状态，默认不区分
        :type EnableState: int
        """
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
        r"""
        :param TotalCount: 设备总数
        :type TotalCount: int
        :param Devices: 设备详细信息列表
        :type Devices: list of DeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self.ProductId = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param Version: 固件版本号
        :type Version: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Md5sum: 固件Md5值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5sum: str
        :param Createtime: 固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Createtime: int
        :param ProductName: 产品名称
        :type ProductName: str
        :param FwType: 固件类型。选项：mcu、module
        :type FwType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param Filters: 筛选条件
        :type Filters: list of SearchKeyword
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询的数量
        :type Limit: int
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param Total: 固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Devices: 固件升级任务的设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceUpdateStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param StatusInfos: 固件升级任务状态分布信息
        :type StatusInfos: list of StatusStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件任务ID
        :type TaskId: int
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        :param CreateTime: 固件任务创建时间，单位:秒
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
        :param OriginalVersion: 升级前版本号
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


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self.ProductId = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param SuccessTotal: 升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotal: int
        :param FailureTotal: 升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureTotal: int
        :param UpgradingTotal: 正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradingTotal: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 返回查询结果条数
        :type Limit: int
        :param Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param TaskInfos: 固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfos: list of FirmwareTaskInfo
        :param Total: 固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeGatewayBindDevicesRequest(AbstractModel):
    """DescribeGatewayBindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页的页大小
        :type Limit: int
        :param ProductId: LoRa产品的ID
        :type ProductId: str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.Offset = None
        self.Limit = None
        self.ProductId = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProductId = params.get("ProductId")
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
        :param TotalCount: 子设备总数
        :type TotalCount: int
        :param Devices: 子设备信息
        :type Devices: list of BindDeviceInfo
        :param ProductName: 子设备所属的产品名
        :type ProductName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Devices = None
        self.ProductName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = BindDeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.ProductName = params.get("ProductName")
        self.RequestId = params.get("RequestId")


class DescribePrivateCABindedProductsRequest(AbstractModel):
    """DescribePrivateCABindedProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertName: 证书名称
        :type CertName: str
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询的数据量，默认为20， 最大为200
        :type Limit: int
        """
        self.CertName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCABindedProductsResponse(AbstractModel):
    """DescribePrivateCABindedProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 私有CA绑定的产品列表
        :type Products: list of BindProductInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateCARequest(AbstractModel):
    """DescribePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertName: 私有化CA名称
        :type CertName: str
        """
        self.CertName = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCAResponse(AbstractModel):
    """DescribePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param CA: 私有化CA详情
        :type CA: :class:`tencentcloud.iotcloud.v20210408.models.CertInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CA = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CA") is not None:
            self.CA = CertInfo()
            self.CA._deserialize(params.get("CA"))
        self.RequestId = params.get("RequestId")


class DescribePrivateCAsRequest(AbstractModel):
    """DescribePrivateCAs请求参数结构体

    """


class DescribePrivateCAsResponse(AbstractModel):
    """DescribePrivateCAs返回参数结构体

    """

    def __init__(self):
        r"""
        :param CAs: 私有CA证书列表
        :type CAs: list of CertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CAs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self.CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CAs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductCARequest(AbstractModel):
    """DescribeProductCA请求参数结构体

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
        


class DescribeProductCAResponse(AbstractModel):
    """DescribeProductCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param CAs: CA证书列表
        :type CAs: list of CertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CAs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self.CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CAs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

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
        


class DescribeProductResourceRequest(AbstractModel):
    """DescribeProductResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 需要查看资源列表的产品 ID
        :type ProductID: str
        :param Name: 需要过滤的资源名称
        :type Name: str
        """
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
        r"""
        :param Result: 资源详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.iotcloud.v20210408.models.ProductResourceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param ProductID: 需要查看资源列表的产品 ID
        :type ProductID: str
        :param Name: 需要过滤的资源名称
        :type Name: str
        """
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
        r"""
        :param TotalCount: 资源总数
        :type TotalCount: int
        :param Result: 资源详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of ProductResourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名
        :type ProductName: str
        :param ProductMetadata: 产品元数据
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductMetadata = None
        self.ProductProperties = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self.ProductMetadata = ProductMetadata()
            self.ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.RequestId = params.get("RequestId")


class DescribeProductTaskRequest(AbstractModel):
    """DescribeProductTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param TaskId: 任务ID
        :type TaskId: int
        """
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
        r"""
        :param TaskInfo: 产品任务详细信息
        :type TaskInfo: :class:`tencentcloud.iotcloud.v20210408.models.ProductTaskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param Offset: 产品级别任务列表偏移量
        :type Offset: int
        :param Limit: 产品级别任务列表拉取个数
        :type Limit: int
        """
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
        r"""
        :param TotalCount: 符合条件的任务总个数
        :type TotalCount: int
        :param TaskInfos: 任务详细信息列表
        :type TaskInfos: list of ProductTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页大小，当前页面中显示的最大数量，值范围 10-250。
        :type Limit: int
        """
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
        r"""
        :param TotalCount: 产品总数
        :type TotalCount: int
        :param Products: 产品详细信息列表
        :type Products: list of ProductInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param Name: 资源名称
        :type Name: str
        """
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
        r"""
        :param SuccessTotal: 推送成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotal: int
        :param FailureTotal: 推送失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureTotal: int
        :param UpgradingTotal: 正在推送的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradingTotal: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param Name: 资源名称
        :type Name: str
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 返回查询结果条数
        :type Limit: int
        :param Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
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
        r"""
        :param TaskInfos: 资源任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfos: list of FirmwareTaskInfo
        :param Total: 资源任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线
        :type Online: int
        :param LoginTime: 设备登录时间
        :type LoginTime: int
        :param Version: 设备版本
        :type Version: str
        :param DeviceCert: 设备证书，证书加密的设备返回
        :type DeviceCert: str
        :param DevicePsk: 设备密钥，密钥加密的设备返回
        :type DevicePsk: str
        :param Tags: 设备属性
        :type Tags: list of DeviceTag
        :param DeviceType: 设备类型
        :type DeviceType: int
        :param Imei: 国际移动设备识别码 IMEI
        :type Imei: str
        :param Isp: 运营商类型
        :type Isp: int
        :param NbiotDeviceID: NB IOT运营商处的DeviceID
        :type NbiotDeviceID: str
        :param ConnIP: IP地址
        :type ConnIP: int
        :param LastUpdateTime: 设备最后更新时间
        :type LastUpdateTime: int
        :param LoraDevEui: LoRa设备的dev eui
        :type LoraDevEui: str
        :param LoraMoteType: LoRa设备的Mote type
        :type LoraMoteType: int
        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LogLevel: 设备日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param CertState: 设备证书获取状态, 1 已获取过设备密钥，0 未获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        :param EnableState: 设备可用状态，0禁用，1启用
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        :param ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param FirmwareUpdateTime: ota最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirmwareUpdateTime: int
        """
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
        r"""
        :param Key: 标签标识
        :type Key: str
        :param Value: 标签值
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
        


class DeviceResourceInfo(AbstractModel):
    """设备资源详细信息

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param ProductName: 产品名
        :type ProductName: str
        :param Name: 资源名称
        :type Name: str
        :param Md5: 资源文件md5
        :type Md5: str
        :param Size: 资源文件大小
        :type Size: int
        :param UpdateTime: 资源更新时间
        :type UpdateTime: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Status: 设备资源上传状态
        :type Status: int
        :param Percent: 设备资源上传百分比
        :type Percent: int
        """
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
        r"""
        :param Tag: 属性名称
        :type Tag: str
        :param Type: 属性值的类型，1 int，2 string
        :type Type: int
        :param Value: 属性的值
        :type Value: str
        :param Name: 属性描述名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
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
        r"""
        :param DeviceName: 设备名
        :type DeviceName: str
        :param LastProcessTime: 最后处理时间
        :type LastProcessTime: int
        :param Status: 状态
        :type Status: int
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param Retcode: 返回码
        :type Retcode: int
        :param DstVersion: 目标更新版本
        :type DstVersion: str
        :param Percent: 下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param OriVersion: 原版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriVersion: str
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        """
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


class DownloadDeviceResourceRequest(AbstractModel):
    """DownloadDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param Name: 资源名称
        :type Name: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductID = None
        self.Name = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Name = params.get("Name")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadDeviceResourceResponse(AbstractModel):
    """DownloadDeviceResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 设备资源的cos链接
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class EditFirmwareRequest(AbstractModel):
    """EditFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID。
        :type ProductId: str
        :param FirmwareVersion: 固件版本号。
        :type FirmwareVersion: str
        :param FirmwareName: 固件名称。
        :type FirmwareName: str
        :param FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.FirmwareName = None
        self.FirmwareDescription = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareTaskInfo(AbstractModel):
    """固件升级任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        """
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
        


class GetAllVersionRequest(AbstractModel):
    """GetAllVersion请求参数结构体

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
        


class GetAllVersionResponse(AbstractModel):
    """GetAllVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param Version: 版本号列表
        :type Version: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Version = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.RequestId = params.get("RequestId")


class GetCOSURLRequest(AbstractModel):
    """GetCOSURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param FileSize: 固件版本大小
        :type FileSize: int
        """
        self.ProductId = None
        self.FirmwareVersion = None
        self.FileSize = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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


class GetUserResourceInfoRequest(AbstractModel):
    """GetUserResourceInfo请求参数结构体

    """


class GetUserResourceInfoResponse(AbstractModel):
    """GetUserResourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param UsedSize: 已使用的资源字节数
        :type UsedSize: int
        :param Limit: 可以使用资源的总大小
        :type Limit: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UsedSize = None
        self.Limit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UsedSize = params.get("UsedSize")
        self.Limit = params.get("Limit")
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
        :param ProductId: 产品ID
        :type ProductId: str
        :param Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self.PageNum = None
        self.PageSize = None
        self.ProductId = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.ProductId = params.get("ProductId")
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


class ListLogPayloadRequest(AbstractModel):
    """ListLogPayload请求参数结构体

    """

    def __init__(self):
        r"""
        :param MinTime: 日志开始时间，毫秒级时间戳
        :type MinTime: int
        :param MaxTime: 日志结束时间，毫秒级时间戳
        :type MaxTime: int
        :param Keywords: 查询关键字，可以同时支持键值查询和文本查询，例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。键值或文本可以包含多个，以空格隔开。其中可以索引的key比如：RequestID、ProductID、DeviceName等。
一个典型的查询示例：ProductID:ABCDE12345 DeviceName:test publish
        :type Keywords: str
        :param Context: 日志检索上下文
        :type Context: str
        :param MaxNum: 日志最大条数
        :type MaxNum: int
        """
        self.MinTime = None
        self.MaxTime = None
        self.Keywords = None
        self.Context = None
        self.MaxNum = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.Keywords = params.get("Keywords")
        self.Context = params.get("Context")
        self.MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogPayloadResponse(AbstractModel):
    """ListLogPayload返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 日志上下文
        :type Context: str
        :param Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param Results: 日志列表
        :type Results: list of PayloadLogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Listover = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = PayloadLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class ListLogRequest(AbstractModel):
    """ListLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param MinTime: 日志开始时间，毫秒级时间戳
        :type MinTime: int
        :param MaxTime: 日志结束时间，毫秒级时间戳
        :type MaxTime: int
        :param Keywords: 查询关键字，可以同时支持键值查询和文本查询，例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。键值或文本可以包含多个，以空格隔开。其中可以索引的key包括：requestid、productid、devicename、scene、content。
一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW content:Device%20connect publish
        :type Keywords: str
        :param Context: 日志检索上下文
        :type Context: str
        :param MaxNum: 查询条数
        :type MaxNum: int
        """
        self.MinTime = None
        self.MaxTime = None
        self.Keywords = None
        self.Context = None
        self.MaxNum = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.Keywords = params.get("Keywords")
        self.Context = params.get("Context")
        self.MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogResponse(AbstractModel):
    """ListLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 日志上下文
        :type Context: str
        :param Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param Results: 日志列表
        :type Results: list of CLSLogItem
        :param TotalCount: 日志总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Listover = None
        self.Results = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = CLSLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListSDKLogRequest(AbstractModel):
    """ListSDKLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param MinTime: 日志开始时间
        :type MinTime: int
        :param MaxTime: 日志结束时间
        :type MaxTime: int
        :param Keywords: 查询关键字，可以同时支持键值查询和文本查询，
例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。
键值或文本可以包含多个，以空格隔开。
其中可以索引的key包括：productid、devicename、loglevel
一个典型的查询示例：productid:7JK1G72JNE devicename:name publish loglevel:WARN一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW publish
        :type Keywords: str
        :param Context: 日志检索上下文
        :type Context: str
        :param MaxNum: 查询条数
        :type MaxNum: int
        """
        self.MinTime = None
        self.MaxTime = None
        self.Keywords = None
        self.Context = None
        self.MaxNum = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.Keywords = params.get("Keywords")
        self.Context = params.get("Context")
        self.MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSDKLogResponse(AbstractModel):
    """ListSDKLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 日志检索上下文
        :type Context: str
        :param Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param Results: 日志列表
        :type Results: list of SDKLogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Listover = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = SDKLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class ListTopicRulesRequest(AbstractModel):
    """ListTopicRules请求参数结构体

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
        


class ListTopicRulesResponse(AbstractModel):
    """ListTopicRules返回参数结构体

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


class PayloadLogItem(AbstractModel):
    """内容日志项

    """

    def __init__(self):
        r"""
        :param Uin: 账号id
        :type Uin: str
        :param ProductId: 产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param SrcType: 来源类型
        :type SrcType: str
        :param SrcName: 来源名称
        :type SrcName: str
        :param Topic: 消息topic
        :type Topic: str
        :param PayloadFormatType: 内容格式类型
        :type PayloadFormatType: str
        :param Payload: 内容信息
        :type Payload: str
        :param RequestId: 请求ID
        :type RequestId: str
        :param DateTime: 日期时间
        :type DateTime: str
        """
        self.Uin = None
        self.ProductId = None
        self.DeviceName = None
        self.SrcType = None
        self.SrcName = None
        self.Topic = None
        self.PayloadFormatType = None
        self.Payload = None
        self.RequestId = None
        self.DateTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.SrcType = params.get("SrcType")
        self.SrcName = params.get("SrcName")
        self.Topic = params.get("Topic")
        self.PayloadFormatType = params.get("PayloadFormatType")
        self.Payload = params.get("Payload")
        self.RequestId = params.get("RequestId")
        self.DateTime = params.get("DateTime")
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名
        :type ProductName: str
        :param ProductMetadata: 产品元数据
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        """
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
        r"""
        :param CreationDate: 产品创建时间
        :type CreationDate: int
        :param CreateUserId: 创建者 Uin
        :type CreateUserId: int
        :param UserId: 账号 Uin
        :type UserId: int
        """
        self.CreationDate = None
        self.CreateUserId = None
        self.UserId = None


    def _deserialize(self, params):
        self.CreationDate = params.get("CreationDate")
        self.CreateUserId = params.get("CreateUserId")
        self.UserId = params.get("UserId")
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
        r"""
        :param ProductDescription: 产品描述
        :type ProductDescription: str
        :param EncryptionType: 加密类型，1表示证书认证，2表示签名认证。如不填写，默认值是1
        :type EncryptionType: str
        :param Region: 产品所属区域，目前只支持广州（gz）
        :type Region: str
        :param ProductType: 产品类型，各个类型值代表的节点-类型如下：
0 普通产品，2 NB-IoT产品，4 LoRa产品，3 LoRa网关产品，5 普通网关产品   默认值是0
        :type ProductType: int
        :param Format: 数据格式，取值为json或者custom，默认值是json
        :type Format: str
        :param Platform: 产品所属平台，默认值是0
        :type Platform: str
        :param Appeui: LoRa产品运营侧APPEUI，只有LoRa产品需要填写
        :type Appeui: str
        :param ModelId: 产品绑定的物模型ID，-1表示不绑定
        :type ModelId: str
        :param ModelName: 产品绑定的物模型名称
        :type ModelName: str
        :param ProductKey: 产品密钥，suite产品才会有
        :type ProductKey: str
        :param RegisterType: 动态注册类型 0-关闭, 1-预定义设备名 2-动态定义设备名
        :type RegisterType: int
        :param ProductSecret: 动态注册产品密钥
        :type ProductSecret: str
        :param RegisterLimit: RegisterType为2时，设备动态创建的限制数量
        :type RegisterLimit: int
        :param OriginProductId: 划归的产品，展示为源产品ID，其余为空
        :type OriginProductId: str
        :param PrivateCAName: 私有CA名称
        :type PrivateCAName: str
        :param OriginUserId: 划归的产品，展示为源用户ID，其余为空
        :type OriginUserId: int
        :param DeviceLimit: 设备限制
        :type DeviceLimit: int
        :param ForbiddenStatus: 产品禁用状态
        :type ForbiddenStatus: int
        """
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
        self.OriginProductId = None
        self.PrivateCAName = None
        self.OriginUserId = None
        self.DeviceLimit = None
        self.ForbiddenStatus = None


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
        self.OriginProductId = params.get("OriginProductId")
        self.PrivateCAName = params.get("PrivateCAName")
        self.OriginUserId = params.get("OriginUserId")
        self.DeviceLimit = params.get("DeviceLimit")
        self.ForbiddenStatus = params.get("ForbiddenStatus")
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
        r"""
        :param ProductID: 产品ID
        :type ProductID: str
        :param ProductName: 产品名
        :type ProductName: str
        :param Name: 资源名称
        :type Name: str
        :param Md5: 资源文件md5
        :type Md5: str
        :param Size: 资源文件大小
        :type Size: int
        :param Description: 资源文件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 资源创建时间
        :type CreateTime: str
        """
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
        r"""
        :param Id: 任务ID
        :type Id: int
        :param Type: 任务类型 0-批量创建设备类型
        :type Type: int
        :param State: 任务状态 0-创建中 1-待执行 2-执行中 3-执行失败 4-子任务部分失败 5-执行成功
        :type State: int
        :param ParametersType: 任务参数类型 cosfile-文件输入 random-随机生成
        :type ParametersType: str
        :param Parameters: 任务参数
        :type Parameters: str
        :param ResultType: 任务执行结果类型 cosfile-文件输出 errmsg-错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param Result: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param BatchCount: 子任务总个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchCount: int
        :param BatchOffset: 子任务已执行个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchOffset: int
        :param CreateTime: 任务创建时间
        :type CreateTime: int
        :param UpdateTime: 任务更新时间
        :type UpdateTime: int
        :param CompleteTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteTime: int
        """
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
        :param PayloadEncoding: Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
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
        :param TaskId: 广播消息任务ID
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
        :param Topic: 消息发往的主题。命名规则：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}
        :type Topic: str
        :param Payload: 消息内容
        :type Payload: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Qos: 服务质量等级，取值为0或1
        :type Qos: int
        :param PayloadEncoding: Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
        :type PayloadEncoding: str
        """
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
        :type MessageId: int
        :param PayloadBase64: 设备回复的消息内容，采用base64编码
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


class ReplaceTopicRuleRequest(AbstractModel):
    """ReplaceTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        :param TopicRulePayload: 替换的规则包体
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20210408.models.TopicRulePayload`
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
        


class ReplaceTopicRuleResponse(AbstractModel):
    """ReplaceTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceResult(AbstractModel):
    """重置设备状态结果

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Success: 是否成功
        :type Success: bool
        :param Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceNames: 设备名称
        :type DeviceNames: list of str
        """
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
        r"""
        :param SuccessCount: 批量重置设备成功数
        :type SuccessCount: int
        :param ResetDeviceResults: 批量重置设备结果
        :type ResetDeviceResults: list of ResetDeviceResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SDKLogItem(AbstractModel):
    """SDK日志项

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Level: 日志等级
        :type Level: str
        :param DateTime: 日志时间
        :type DateTime: str
        :param Content: 日志内容
        :type Content: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Level = None
        self.DateTime = None
        self.Content = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Level = params.get("Level")
        self.DateTime = params.get("DateTime")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class SetProductsForbiddenStatusRequest(AbstractModel):
    """SetProductsForbiddenStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 要设置禁用状态的产品列表
        :type ProductId: list of str
        :param Status: 0启用，1禁用
        :type Status: int
        """
        self.ProductId = None
        self.Status = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusResponse(AbstractModel):
    """SetProductsForbiddenStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StatusStatistic(AbstractModel):
    """状态统计信息

    """

    def __init__(self):
        r"""
        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Total: 统计总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
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
        


class TopicRuleInfo(AbstractModel):
    """规则详细信息

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        :param Description: 规则描述
        :type Description: str
        :param CreatedAt: 创建时间
        :type CreatedAt: int
        :param RuleDisabled: 不生效
        :type RuleDisabled: bool
        :param TopicPattern: 规则模式
        :type TopicPattern: str
        """
        self.RuleName = None
        self.Description = None
        self.CreatedAt = None
        self.RuleDisabled = None
        self.TopicPattern = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Description = params.get("Description")
        self.CreatedAt = params.get("CreatedAt")
        self.RuleDisabled = params.get("RuleDisabled")
        self.TopicPattern = params.get("TopicPattern")
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
        :param DeviceNames: 多个设备名
        :type DeviceNames: list of str
        :param Skey: 中兴CLAA设备的解绑需要Skey，普通设备不需要
        :type Skey: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceAvailableStateRequest(AbstractModel):
    """UpdateDeviceAvailableState请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 设备所属产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param EnableState: 要设置的设备状态，1为启用，0为禁用
        :type EnableState: int
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceLogLevelRequest(AbstractModel):
    """UpdateDeviceLogLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param LogLevel: 日志级别，0：关闭，1：错误，2：告警，3：信息，4：调试
        :type LogLevel: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.LogLevel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceLogLevelResponse(AbstractModel):
    """UpdateDeviceLogLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDevicePSKRequest(AbstractModel):
    """UpdateDevicePSK请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品名
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Psk: 设备的psk
        :type Psk: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Psk = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Psk = params.get("Psk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicePSKResponse(AbstractModel):
    """UpdateDevicePSK返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceShadowRequest(AbstractModel):
    """UpdateDeviceShadow请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param State: 虚拟设备的状态，JSON字符串格式，由desired结构组成
        :type State: str
        :param ShadowVersion: 当前版本号，需要和后台的version保持一致，才能更新成功
        :type ShadowVersion: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.State = None
        self.ShadowVersion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.State = params.get("State")
        self.ShadowVersion = params.get("ShadowVersion")
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
        r"""
        :param Data: 设备影子数据，JSON字符串格式
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 设备所属产品id
        :type ProductId: str
        :param DeviceNames: 设备名称集合
        :type DeviceNames: list of str
        :param Status: 要设置的设备状态，1为启用，0为禁用
        :type Status: int
        """
        self.ProductId = None
        self.DeviceNames = None
        self.Status = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePrivateCARequest(AbstractModel):
    """UpdatePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertName: CA证书名称
        :type CertName: str
        :param CertText: CA证书内容
        :type CertText: str
        :param VerifyCertText: 校验CA证书的证书内容
        :type VerifyCertText: str
        """
        self.CertName = None
        self.CertText = None
        self.VerifyCertText = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertText = params.get("CertText")
        self.VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrivateCAResponse(AbstractModel):
    """UpdatePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateProductDynamicRegisterRequest(AbstractModel):
    """UpdateProductDynamicRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品Id
        :type ProductId: str
        :param RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        """
        self.ProductId = None
        self.RegisterType = None
        self.RegisterLimit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.RegisterType = params.get("RegisterType")
        self.RegisterLimit = params.get("RegisterLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductDynamicRegisterResponse(AbstractModel):
    """UpdateProductDynamicRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param ProductSecret: 动态注册产品密钥
        :type ProductSecret: str
        :param RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegisterType = None
        self.ProductSecret = None
        self.RegisterLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegisterType = params.get("RegisterType")
        self.ProductSecret = params.get("ProductSecret")
        self.RegisterLimit = params.get("RegisterLimit")
        self.RequestId = params.get("RequestId")


class UpdateProductPrivateCARequest(AbstractModel):
    """UpdateProductPrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 产品ID
        :type ProductId: str
        :param CertName: 私有CA证书名称
        :type CertName: str
        """
        self.ProductId = None
        self.CertName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductPrivateCAResponse(AbstractModel):
    """UpdateProductPrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateTopicPolicyRequest(AbstractModel):
    """UpdateTopicPolicy请求参数结构体

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
        :param BrokerSubscribe: 代理订阅信息
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20210408.models.BrokerSubscribe`
        """
        self.ProductId = None
        self.TopicName = None
        self.NewTopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
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
        :param ProductId: 产品ID
        :type ProductId: str
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
        self.ProductId = None
        self.FirmwareVersion = None
        self.Md5sum = None
        self.FileSize = None
        self.FirmwareName = None
        self.FirmwareDescription = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.Md5sum = params.get("Md5sum")
        self.FileSize = params.get("FileSize")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")
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