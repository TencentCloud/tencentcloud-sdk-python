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
        


class BindProductInfo(AbstractModel):
    """子产品信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名\n        :type ProductName: str\n        """
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
        


class CertInfo(AbstractModel):
    """X509证书信息

    """

    def __init__(self):
        """
        :param CertName: 证书名称\n        :type CertName: str\n        :param CertSN: 证书的序列号，16进制编码\n        :type CertSN: str\n        :param IssuerName: 证书颁发着名称\n        :type IssuerName: str\n        :param Subject: 证书主题\n        :type Subject: str\n        :param CreateTime: 证书创建时间，秒级时间戳\n        :type CreateTime: int\n        :param EffectiveTime: 证书生效时间，秒级时间戳\n        :type EffectiveTime: int\n        :param ExpireTime: 证书失效时间，秒级时间戳\n        :type ExpireTime: int\n        :param CertText: X509证书内容\n        :type CertText: str\n        """
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
        """
        :param ProductId: 产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID\n        :type ProductId: str\n        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。\n        :type DeviceName: str\n        :param Attribute: 设备属性\n        :type Attribute: :class:`tencentcloud.iotcloud.v20210408.models.Attribute`\n        :param DefinedPsk: 是否使用自定义PSK，默认不使用\n        :type DefinedPsk: str\n        :param Isp: 运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通\n        :type Isp: int\n        :param Imei: IMEI，当产品是NB-IoT产品时，此字段必填\n        :type Imei: str\n        :param LoraDevEui: LoRa设备的DevEui，当创建LoRa时，此字段必填\n        :type LoraDevEui: str\n        :param LoraMoteType: LoRa设备的MoteType\n        :type LoraMoteType: int\n        :param Skey: 创建LoRa设备需要skey\n        :type Skey: str\n        :param LoraAppKey: LoRa设备的AppKey\n        :type LoraAppKey: str\n        :param TlsCrt: 私有CA创建的设备证书\n        :type TlsCrt: str\n        """
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


class CreatePrivateCARequest(AbstractModel):
    """CreatePrivateCA请求参数结构体

    """

    def __init__(self):
        """
        :param CertName: CA证书名称\n        :type CertName: str\n        :param CertText: CA证书内容\n        :type CertText: str\n        :param VerifyCertText: 校验CA证书的证书内容\n        :type VerifyCertText: str\n        """
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


class DeletePrivateCARequest(AbstractModel):
    """DeletePrivateCA请求参数结构体

    """

    def __init__(self):
        """
        :param CertName: 私有CA证书名称\n        :type CertName: str\n        """
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


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

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


class DescribePrivateCABindedProductsRequest(AbstractModel):
    """DescribePrivateCABindedProducts请求参数结构体

    """

    def __init__(self):
        """
        :param CertName: 证书名称\n        :type CertName: str\n        :param Offset: 查询偏移量\n        :type Offset: int\n        :param Limit: 查询的数据量，默认为20， 最大为200\n        :type Limit: int\n        """
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
        """
        :param Products: 私有CA绑定的产品列表\n        :type Products: list of BindProductInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CertName: 私有化CA名称\n        :type CertName: str\n        """
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
        """
        :param CA: 私有化CA详情\n        :type CA: :class:`tencentcloud.iotcloud.v20210408.models.CertInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CAs: 私有CA证书列表\n        :type CAs: list of CertInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        


class DescribeProductCAResponse(AbstractModel):
    """DescribeProductCA返回参数结构体

    """

    def __init__(self):
        """
        :param CAs: CA证书列表\n        :type CAs: list of CertInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名\n        :type ProductName: str\n        :param ProductMetadata: 产品元数据\n        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`\n        :param ProductProperties: 产品属性\n        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
0 普通产品，2 NB-IoT产品，4 LoRa产品，3 LoRa网关产品，5 普通网关产品   默认值是0\n        :type ProductType: int\n        :param Format: 数据格式，取值为json或者custom，默认值是json\n        :type Format: str\n        :param Platform: 产品所属平台，默认值是0\n        :type Platform: str\n        :param Appeui: LoRa产品运营侧APPEUI，只有LoRa产品需要填写\n        :type Appeui: str\n        :param ModelId: 产品绑定的物模型ID，-1表示不绑定\n        :type ModelId: str\n        :param ModelName: 产品绑定的物模型名称\n        :type ModelName: str\n        :param ProductKey: 产品密钥，suite产品才会有\n        :type ProductKey: str\n        :param RegisterType: 动态注册类型 0-关闭, 1-预定义设备名 2-动态定义设备名\n        :type RegisterType: int\n        :param ProductSecret: 动态注册产品秘钥\n        :type ProductSecret: str\n        :param RegisterLimit: RegisterType为2时，设备动态创建的限制数量\n        :type RegisterLimit: int\n        :param OriginProductId: 划归的产品，展示为源产品ID，其余为空\n        :type OriginProductId: str\n        :param PrivateCAName: 私有CA名称\n        :type PrivateCAName: str\n        :param OriginUserId: 划归的产品，展示为源用户ID，其余为空\n        :type OriginUserId: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceLogLevelRequest(AbstractModel):
    """UpdateDeviceLogLevel请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param LogLevel: 日志级别，0：关闭，1：错误，2：告警，3：信息，4：调试\n        :type LogLevel: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品id\n        :type ProductId: str\n        :param DeviceNames: 设备名称集合\n        :type DeviceNames: list of str\n        :param Status: 要设置的设备状态，1为启用，0为禁用\n        :type Status: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePrivateCARequest(AbstractModel):
    """UpdatePrivateCA请求参数结构体

    """

    def __init__(self):
        """
        :param CertName: CA证书名称\n        :type CertName: str\n        :param CertText: CA证书内容\n        :type CertText: str\n        :param VerifyCertText: 校验CA证书的证书内容\n        :type VerifyCertText: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")