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
        :param _Tags: 属性列表
        :type Tags: list of DeviceTag
        """
        self._Tags = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareRequest(AbstractModel):
    """BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件新版本号
        :type FirmwareVersion: str
        :param _FirmwareOriVersion: 固件原版本号，根据文件列表升级固件不需要填写此参数
        :type FirmwareOriVersion: str
        :param _UpgradeMethod: 升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式
        :type UpgradeMethod: int
        :param _FileName: 设备列表文件名称，根据文件列表升级固件需要填写此参数
        :type FileName: str
        :param _FileMd5: 设备列表的文件md5值
        :type FileMd5: str
        :param _FileSize: 设备列表的文件大小值
        :type FileSize: int
        :param _DeviceNames: 需要升级的设备名称列表
        :type DeviceNames: list of str
        :param _TimeoutInterval: 固件升级任务，默认超时时间。 最小取值60秒，最大为3600秒
        :type TimeoutInterval: int
        :param _Type: 固件升级任务类型，默认静态升级值为空或1，动态升级值为7。
        :type Type: int
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._FirmwareOriVersion = None
        self._UpgradeMethod = None
        self._FileName = None
        self._FileMd5 = None
        self._FileSize = None
        self._DeviceNames = None
        self._TimeoutInterval = None
        self._Type = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareOriVersion(self):
        return self._FirmwareOriVersion

    @FirmwareOriVersion.setter
    def FirmwareOriVersion(self, FirmwareOriVersion):
        self._FirmwareOriVersion = FirmwareOriVersion

    @property
    def UpgradeMethod(self):
        return self._UpgradeMethod

    @UpgradeMethod.setter
    def UpgradeMethod(self, UpgradeMethod):
        self._UpgradeMethod = UpgradeMethod

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def TimeoutInterval(self):
        return self._TimeoutInterval

    @TimeoutInterval.setter
    def TimeoutInterval(self, TimeoutInterval):
        self._TimeoutInterval = TimeoutInterval

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareOriVersion = params.get("FirmwareOriVersion")
        self._UpgradeMethod = params.get("UpgradeMethod")
        self._FileName = params.get("FileName")
        self._FileMd5 = params.get("FileMd5")
        self._FileSize = params.get("FileSize")
        self._DeviceNames = params.get("DeviceNames")
        self._TimeoutInterval = params.get("TimeoutInterval")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareResponse(AbstractModel):
    """BatchUpdateFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindDeviceInfo(AbstractModel):
    """子设备信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Tags: 设备Tag
        :type Tags: list of DeviceTag
        :param _BindTime: 子设备绑定时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BindTime: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Tags = None
        self._BindTime = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BindTime(self):
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._BindTime = params.get("BindTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDevicesRequest(AbstractModel):
    """BindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param _ProductId: 被绑定设备的产品ID
        :type ProductId: str
        :param _DeviceNames: 被绑定的多个设备名
        :type DeviceNames: list of str
        :param _Skey: 中兴CLAA设备的绑定需要skey，普通的设备不需要
        :type Skey: str
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._ProductId = None
        self._DeviceNames = None
        self._Skey = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDevicesResponse(AbstractModel):
    """BindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BindProductInfo(AbstractModel):
    """子产品信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名
        :type ProductName: str
        """
        self._ProductId = None
        self._ProductName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrokerSubscribe(AbstractModel):
    """代理订阅信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CLSLogItem(AbstractModel):
    """CLS日志

    """

    def __init__(self):
        r"""
        :param _Content: 日志内容
        :type Content: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _RequestId: 请求ID
        :type RequestId: str
        :param _Result: 结果
        :type Result: str
        :param _Scene: 模块
        :type Scene: str
        :param _Time: 日志时间
        :type Time: str
        :param _Userid: 腾讯云账号
        :type Userid: str
        :param _UserId: 腾讯云账号
        :type UserId: str
        """
        self._Content = None
        self._DeviceName = None
        self._ProductId = None
        self._RequestId = None
        self._Result = None
        self._Scene = None
        self._Time = None
        self._Userid = None
        self._UserId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Userid(self):
        warnings.warn("parameter `Userid` is deprecated", DeprecationWarning) 

        return self._Userid

    @Userid.setter
    def Userid(self, Userid):
        warnings.warn("parameter `Userid` is deprecated", DeprecationWarning) 

        self._Userid = Userid

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._DeviceName = params.get("DeviceName")
        self._ProductId = params.get("ProductId")
        self._RequestId = params.get("RequestId")
        self._Result = params.get("Result")
        self._Scene = params.get("Scene")
        self._Time = params.get("Time")
        self._Userid = params.get("Userid")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDeviceFirmwareTaskRequest(AbstractModel):
    """CancelDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDeviceFirmwareTaskResponse(AbstractModel):
    """CancelDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CertInfo(AbstractModel):
    """X509证书信息

    """

    def __init__(self):
        r"""
        :param _CertName: 证书名称
        :type CertName: str
        :param _CertSN: 证书的序列号，16进制编码
        :type CertSN: str
        :param _IssuerName: 证书颁发着名称
        :type IssuerName: str
        :param _Subject: 证书主题
        :type Subject: str
        :param _CreateTime: 证书创建时间，秒级时间戳
        :type CreateTime: int
        :param _EffectiveTime: 证书生效时间，秒级时间戳
        :type EffectiveTime: int
        :param _ExpireTime: 证书失效时间，秒级时间戳
        :type ExpireTime: int
        :param _CertText: X509证书内容
        :type CertText: str
        """
        self._CertName = None
        self._CertSN = None
        self._IssuerName = None
        self._Subject = None
        self._CreateTime = None
        self._EffectiveTime = None
        self._ExpireTime = None
        self._CertText = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertSN(self):
        return self._CertSN

    @CertSN.setter
    def CertSN(self, CertSN):
        self._CertSN = CertSN

    @property
    def IssuerName(self):
        return self._IssuerName

    @IssuerName.setter
    def IssuerName(self, IssuerName):
        self._IssuerName = IssuerName

    @property
    def Subject(self):
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EffectiveTime(self):
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CertText(self):
        return self._CertText

    @CertText.setter
    def CertText(self, CertText):
        self._CertText = CertText


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertSN = params.get("CertSN")
        self._IssuerName = params.get("IssuerName")
        self._Subject = params.get("Subject")
        self._CreateTime = params.get("CreateTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CertText = params.get("CertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param _DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param _Attribute: 设备属性
        :type Attribute: :class:`tencentcloud.iotcloud.v20210408.models.Attribute`
        :param _DefinedPsk: 是否使用自定义PSK，默认不使用
        :type DefinedPsk: str
        :param _Isp: 运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通
        :type Isp: int
        :param _Imei: IMEI，当产品是NB-IoT产品时，此字段必填
        :type Imei: str
        :param _LoraDevEui: LoRa设备的DevEui，当创建LoRa时，此字段必填
        :type LoraDevEui: str
        :param _LoraMoteType: LoRa设备的MoteType
        :type LoraMoteType: int
        :param _Skey: 创建LoRa设备需要skey
        :type Skey: str
        :param _LoraAppKey: LoRa设备的AppKey
        :type LoraAppKey: str
        :param _TlsCrt: 私有CA创建的设备证书
        :type TlsCrt: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Attribute = None
        self._DefinedPsk = None
        self._Isp = None
        self._Imei = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._Skey = None
        self._LoraAppKey = None
        self._TlsCrt = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Attribute(self):
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def DefinedPsk(self):
        return self._DefinedPsk

    @DefinedPsk.setter
    def DefinedPsk(self, DefinedPsk):
        self._DefinedPsk = DefinedPsk

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def LoraAppKey(self):
        return self._LoraAppKey

    @LoraAppKey.setter
    def LoraAppKey(self, LoraAppKey):
        self._LoraAppKey = LoraAppKey

    @property
    def TlsCrt(self):
        return self._TlsCrt

    @TlsCrt.setter
    def TlsCrt(self, TlsCrt):
        self._TlsCrt = TlsCrt


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self._Attribute = Attribute()
            self._Attribute._deserialize(params.get("Attribute"))
        self._DefinedPsk = params.get("DefinedPsk")
        self._Isp = params.get("Isp")
        self._Imei = params.get("Imei")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._Skey = params.get("Skey")
        self._LoraAppKey = params.get("LoraAppKey")
        self._TlsCrt = params.get("TlsCrt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数
        :type DevicePsk: str
        :param _DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数
        :type DeviceCert: str
        :param _DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数
        :type DevicePrivateKey: str
        :param _LoraDevEui: LoRa设备的DevEui，当设备是LoRa设备时，会返回该字段
        :type LoraDevEui: str
        :param _LoraMoteType: LoRa设备的MoteType，当设备是LoRa设备时，会返回该字段
        :type LoraMoteType: int
        :param _LoraAppKey: LoRa设备的AppKey，当设备是LoRa设备时，会返回该字段
        :type LoraAppKey: str
        :param _LoraNwkKey: LoRa设备的NwkKey，当设备是LoRa设备时，会返回该字段
        :type LoraNwkKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceName = None
        self._DevicePsk = None
        self._DeviceCert = None
        self._DevicePrivateKey = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._LoraAppKey = None
        self._LoraNwkKey = None
        self._RequestId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePrivateKey(self):
        return self._DevicePrivateKey

    @DevicePrivateKey.setter
    def DevicePrivateKey(self, DevicePrivateKey):
        self._DevicePrivateKey = DevicePrivateKey

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def LoraAppKey(self):
        return self._LoraAppKey

    @LoraAppKey.setter
    def LoraAppKey(self, LoraAppKey):
        self._LoraAppKey = LoraAppKey

    @property
    def LoraNwkKey(self):
        return self._LoraNwkKey

    @LoraNwkKey.setter
    def LoraNwkKey(self, LoraNwkKey):
        self._LoraNwkKey = LoraNwkKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._DevicePsk = params.get("DevicePsk")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePrivateKey = params.get("DevicePrivateKey")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._LoraAppKey = params.get("LoraAppKey")
        self._LoraNwkKey = params.get("LoraNwkKey")
        self._RequestId = params.get("RequestId")


class CreateMultiDevicesTaskRequest(AbstractModel):
    """CreateMultiDevicesTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ParametersType: 参数类型 cosfile-文件上传 random-随机创建
        :type ParametersType: str
        :param _FileName: 文件上传类型时文件名
        :type FileName: str
        :param _FileSize: 文件上传类型时文件大小
        :type FileSize: int
        :param _BatchCount: 随机创建时设备创建个数
        :type BatchCount: int
        :param _Hash: 文件上传类型时文件md5值
        :type Hash: str
        """
        self._ProductId = None
        self._ParametersType = None
        self._FileName = None
        self._FileSize = None
        self._BatchCount = None
        self._Hash = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParametersType(self):
        return self._ParametersType

    @ParametersType.setter
    def ParametersType(self, ParametersType):
        self._ParametersType = ParametersType

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def BatchCount(self):
        return self._BatchCount

    @BatchCount.setter
    def BatchCount(self, BatchCount):
        self._BatchCount = BatchCount

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParametersType = params.get("ParametersType")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._BatchCount = params.get("BatchCount")
        self._Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiDevicesTaskResponse(AbstractModel):
    """CreateMultiDevicesTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreatePrivateCARequest(AbstractModel):
    """CreatePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertName: CA证书名称
        :type CertName: str
        :param _CertText: CA证书内容
        :type CertText: str
        :param _VerifyCertText: 校验CA证书的证书内容
        :type VerifyCertText: str
        """
        self._CertName = None
        self._CertText = None
        self._VerifyCertText = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertText(self):
        return self._CertText

    @CertText.setter
    def CertText(self, CertText):
        self._CertText = CertText

    @property
    def VerifyCertText(self):
        return self._VerifyCertText

    @VerifyCertText.setter
    def VerifyCertText(self, VerifyCertText):
        self._VerifyCertText = VerifyCertText


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertText = params.get("CertText")
        self._VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateCAResponse(AbstractModel):
    """CreatePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param _Skey: 创建CLAA产品时，需要Skey
        :type Skey: str
        """
        self._ProductName = None
        self._ProductProperties = None
        self._Skey = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductId: 产品 ID，腾讯云生成全局唯一 ID
        :type ProductId: str
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductName = None
        self._ProductId = None
        self._ProductProperties = None
        self._RequestId = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._ProductId = params.get("ProductId")
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        self._RequestId = params.get("RequestId")


class CreateTaskFileUrlRequest(AbstractModel):
    """CreateTaskFileUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFileUrlResponse(AbstractModel):
    """CreateTaskFileUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 任务文件上传链接
        :type Url: str
        :param _FileName: 任务文件名
        :type FileName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._FileName = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileName = params.get("FileName")
        self._RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品自身ID
        :type ProductId: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _Privilege: Topic权限，1发布，2订阅，3订阅和发布
        :type Privilege: int
        :param _BrokerSubscribe: 代理订阅信息，网关产品为绑定的子产品创建topic时需要填写，内容为子产品的ID和设备信息。
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20210408.models.BrokerSubscribe`
        """
        self._ProductId = None
        self._TopicName = None
        self._Privilege = None
        self._BrokerSubscribe = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def BrokerSubscribe(self):
        return self._BrokerSubscribe

    @BrokerSubscribe.setter
    def BrokerSubscribe(self, BrokerSubscribe):
        self._BrokerSubscribe = BrokerSubscribe


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        self._Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self._BrokerSubscribe = BrokerSubscribe()
            self._BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicPolicyResponse(AbstractModel):
    """CreateTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateTopicRuleRequest(AbstractModel):
    """CreateTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _TopicRulePayload: 规则内容
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20210408.models.TopicRulePayload`
        """
        self._RuleName = None
        self._TopicRulePayload = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def TopicRulePayload(self):
        return self._TopicRulePayload

    @TopicRulePayload.setter
    def TopicRulePayload(self, TopicRulePayload):
        self._TopicRulePayload = TopicRulePayload


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self._TopicRulePayload = TopicRulePayload()
            self._TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicRuleResponse(AbstractModel):
    """CreateTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 设备所属的产品 ID
        :type ProductId: str
        :param _DeviceName: 需要删除的设备名称
        :type DeviceName: str
        :param _Skey: 删除LoRa设备以及LoRa网关设备需要skey
        :type Skey: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Skey = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResourceRequest(AbstractModel):
    """DeleteDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Name: 资源名称
        :type Name: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductID = None
        self._Name = None
        self._DeviceName = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResourceResponse(AbstractModel):
    """DeleteDeviceResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDeviceShadowRequest(AbstractModel):
    """DeleteDeviceShadow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceShadowResponse(AbstractModel):
    """DeleteDeviceShadow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePrivateCARequest(AbstractModel):
    """DeletePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertName: 私有CA证书名称
        :type CertName: str
        """
        self._CertName = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateCAResponse(AbstractModel):
    """DeletePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProductPrivateCARequest(AbstractModel):
    """DeleteProductPrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductPrivateCAResponse(AbstractModel):
    """DeleteProductPrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 需要删除的产品 ID
        :type ProductId: str
        :param _Skey: 删除LoRa产品需要skey
        :type Skey: str
        """
        self._ProductId = None
        self._Skey = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTopicRuleRequest(AbstractModel):
    """DeleteTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicRuleResponse(AbstractModel):
    """DeleteTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceClientKeyRequest(AbstractModel):
    """DescribeDeviceClientKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 所属产品的Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceClientKeyResponse(AbstractModel):
    """DescribeDeviceClientKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientKey: 设备的私钥
        :type ClientKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientKey = None
        self._RequestId = None

    @property
    def ClientKey(self):
        return self._ClientKey

    @ClientKey.setter
    def ClientKey(self, ClientKey):
        self._ClientKey = ClientKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClientKey = params.get("ClientKey")
        self._RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResourceRequest(AbstractModel):
    """DescribeDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Name: 具体的设备资源名称
        :type Name: str
        """
        self._DeviceName = None
        self._ProductID = None
        self._Name = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResourceResponse(AbstractModel):
    """DescribeDeviceResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备资源详情
        :type Result: :class:`tencentcloud.iotcloud.v20210408.models.DeviceResourceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DeviceResourceInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceResourcesRequest(AbstractModel):
    """DescribeDeviceResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        :param _StartTime: 资源搜索开始时间
        :type StartTime: str
        :param _EndTime: 资源搜索结束时间
        :type EndTime: str
        """
        self._Offset = None
        self._Limit = None
        self._ProductID = None
        self._DeviceName = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResourcesResponse(AbstractModel):
    """DescribeDeviceResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源总数
        :type TotalCount: int
        :param _Result: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of DeviceResourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Result = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = DeviceResourceInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Online: 设备是否在线，0不在线，1在线，3未激活
        :type Online: int
        :param _LoginTime: 设备登录时间
        :type LoginTime: int
        :param _Version: 设备固件版本
        :type Version: str
        :param _LastUpdateTime: 设备最后更新时间
        :type LastUpdateTime: int
        :param _DeviceCert: 设备证书
        :type DeviceCert: str
        :param _DevicePsk: 设备密钥
        :type DevicePsk: str
        :param _Tags: 设备属性
        :type Tags: list of DeviceTag
        :param _DeviceType: 设备类型
        :type DeviceType: int
        :param _Imei: 国际移动设备识别码 IMEI
        :type Imei: str
        :param _Isp: 运营商类型
        :type Isp: int
        :param _ConnIP: IP地址
        :type ConnIP: int
        :param _NbiotDeviceID: NB IoT运营商处的DeviceID
        :type NbiotDeviceID: str
        :param _LoraDevEui: Lora设备的dev eui
        :type LoraDevEui: str
        :param _LoraMoteType: Lora设备的mote type
        :type LoraMoteType: int
        :param _LogLevel: 设备的sdk日志等级
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param _FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param _LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param _CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _CertState: 设备证书获取状态，0 未获取过设备密钥, 1 已获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        :param _EnableState: 设备启用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param _Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        :param _ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param _FirmwareUpdateTime: 设备固件更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirmwareUpdateTime: int
        :param _CreateUserId: 创建者账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _NBIoTDeviceID: NB IoT运营商处的DeviceID
        :type NBIoTDeviceID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceName = None
        self._Online = None
        self._LoginTime = None
        self._Version = None
        self._LastUpdateTime = None
        self._DeviceCert = None
        self._DevicePsk = None
        self._Tags = None
        self._DeviceType = None
        self._Imei = None
        self._Isp = None
        self._ConnIP = None
        self._NbiotDeviceID = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._LogLevel = None
        self._FirstOnlineTime = None
        self._LastOfflineTime = None
        self._CreateTime = None
        self._CertState = None
        self._EnableState = None
        self._Labels = None
        self._ClientIP = None
        self._FirmwareUpdateTime = None
        self._CreateUserId = None
        self._NBIoTDeviceID = None
        self._RequestId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def ConnIP(self):
        return self._ConnIP

    @ConnIP.setter
    def ConnIP(self, ConnIP):
        self._ConnIP = ConnIP

    @property
    def NbiotDeviceID(self):
        warnings.warn("parameter `NbiotDeviceID` is deprecated", DeprecationWarning) 

        return self._NbiotDeviceID

    @NbiotDeviceID.setter
    def NbiotDeviceID(self, NbiotDeviceID):
        warnings.warn("parameter `NbiotDeviceID` is deprecated", DeprecationWarning) 

        self._NbiotDeviceID = NbiotDeviceID

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def FirstOnlineTime(self):
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LastOfflineTime(self):
        return self._LastOfflineTime

    @LastOfflineTime.setter
    def LastOfflineTime(self, LastOfflineTime):
        self._LastOfflineTime = LastOfflineTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CertState(self):
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def FirmwareUpdateTime(self):
        return self._FirmwareUpdateTime

    @FirmwareUpdateTime.setter
    def FirmwareUpdateTime(self, FirmwareUpdateTime):
        self._FirmwareUpdateTime = FirmwareUpdateTime

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def NBIoTDeviceID(self):
        return self._NBIoTDeviceID

    @NBIoTDeviceID.setter
    def NBIoTDeviceID(self, NBIoTDeviceID):
        self._NBIoTDeviceID = NBIoTDeviceID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Online = params.get("Online")
        self._LoginTime = params.get("LoginTime")
        self._Version = params.get("Version")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeviceType = params.get("DeviceType")
        self._Imei = params.get("Imei")
        self._Isp = params.get("Isp")
        self._ConnIP = params.get("ConnIP")
        self._NbiotDeviceID = params.get("NbiotDeviceID")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._LogLevel = params.get("LogLevel")
        self._FirstOnlineTime = params.get("FirstOnlineTime")
        self._LastOfflineTime = params.get("LastOfflineTime")
        self._CreateTime = params.get("CreateTime")
        self._CertState = params.get("CertState")
        self._EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._ClientIP = params.get("ClientIP")
        self._FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        self._CreateUserId = params.get("CreateUserId")
        self._NBIoTDeviceID = params.get("NBIoTDeviceID")
        self._RequestId = params.get("RequestId")


class DescribeDeviceShadowRequest(AbstractModel):
    """DescribeDeviceShadow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,60}
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceShadowResponse(AbstractModel):
    """DescribeDeviceShadow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备影子数据
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param _FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :type FirmwareVersion: str
        :param _DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        :param _EnableState: 设备是否启用，0禁用状态1启用状态，默认不区分
        :type EnableState: int
        """
        self._ProductId = None
        self._Offset = None
        self._Limit = None
        self._FirmwareVersion = None
        self._DeviceName = None
        self._EnableState = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._DeviceName = params.get("DeviceName")
        self._EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 设备总数
        :type TotalCount: int
        :param _Devices: 设备详细信息列表
        :type Devices: list of DeviceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareRequest(AbstractModel):
    """DescribeFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self._ProductId = None
        self._FirmwareVersion = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareResponse(AbstractModel):
    """DescribeFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 固件版本号
        :type Version: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Md5sum: 固件Md5值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5sum: str
        :param _Createtime: 固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Createtime: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _FwType: 固件类型。选项：mcu、module
        :type FwType: str
        :param _UserDefined: 固件用户自定义配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefined: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._ProductId = None
        self._Name = None
        self._Description = None
        self._Md5sum = None
        self._Createtime = None
        self._ProductName = None
        self._FwType = None
        self._UserDefined = None
        self._RequestId = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Md5sum(self):
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def FwType(self):
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def UserDefined(self):
        return self._UserDefined

    @UserDefined.setter
    def UserDefined(self, UserDefined):
        self._UserDefined = UserDefined

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._ProductId = params.get("ProductId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Md5sum = params.get("Md5sum")
        self._Createtime = params.get("Createtime")
        self._ProductName = params.get("ProductName")
        self._FwType = params.get("FwType")
        self._UserDefined = params.get("UserDefined")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskDevicesRequest(AbstractModel):
    """DescribeFirmwareTaskDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param _Filters: 筛选条件
        :type Filters: list of SearchKeyword
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询的数量
        :type Limit: int
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDevicesResponse(AbstractModel):
    """DescribeFirmwareTaskDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Devices: 固件升级任务的设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceUpdateStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Devices = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceUpdateStatus()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskDistributionRequest(AbstractModel):
    """DescribeFirmwareTaskDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDistributionResponse(AbstractModel):
    """DescribeFirmwareTaskDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatusInfos: 固件升级任务状态分布信息
        :type StatusInfos: list of StatusStatistic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatusInfos = None
        self._RequestId = None

    @property
    def StatusInfos(self):
        return self._StatusInfos

    @StatusInfos.setter
    def StatusInfos(self, StatusInfos):
        self._StatusInfos = StatusInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatusInfos") is not None:
            self._StatusInfos = []
            for item in params.get("StatusInfos"):
                obj = StatusStatistic()
                obj._deserialize(item)
                self._StatusInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskRequest(AbstractModel):
    """DescribeFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件任务ID
        :type TaskId: int
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskResponse(AbstractModel):
    """DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 固件任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _Status: 固件任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 固件任务创建时间，单位:秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeMode: str
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _OriginalVersion: 升级前版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._CreateTime = None
        self._Type = None
        self._ProductName = None
        self._UpgradeMode = None
        self._ProductId = None
        self._OriginalVersion = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def UpgradeMode(self):
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OriginalVersion(self):
        return self._OriginalVersion

    @OriginalVersion.setter
    def OriginalVersion(self, OriginalVersion):
        self._OriginalVersion = OriginalVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Type = params.get("Type")
        self._ProductName = params.get("ProductName")
        self._UpgradeMode = params.get("UpgradeMode")
        self._ProductId = params.get("ProductId")
        self._OriginalVersion = params.get("OriginalVersion")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self._ProductId = None
        self._FirmwareVersion = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskStatisticsResponse(AbstractModel):
    """DescribeFirmwareTaskStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessTotal: 升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotal: int
        :param _FailureTotal: 升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureTotal: int
        :param _UpgradingTotal: 正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradingTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessTotal = None
        self._FailureTotal = None
        self._UpgradingTotal = None
        self._RequestId = None

    @property
    def SuccessTotal(self):
        return self._SuccessTotal

    @SuccessTotal.setter
    def SuccessTotal(self, SuccessTotal):
        self._SuccessTotal = SuccessTotal

    @property
    def FailureTotal(self):
        return self._FailureTotal

    @FailureTotal.setter
    def FailureTotal(self, FailureTotal):
        self._FailureTotal = FailureTotal

    @property
    def UpgradingTotal(self):
        return self._UpgradingTotal

    @UpgradingTotal.setter
    def UpgradingTotal(self, UpgradingTotal):
        self._UpgradingTotal = UpgradingTotal

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessTotal = params.get("SuccessTotal")
        self._FailureTotal = params.get("FailureTotal")
        self._UpgradingTotal = params.get("UpgradingTotal")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTasksRequest(AbstractModel):
    """DescribeFirmwareTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 返回查询结果条数
        :type Limit: int
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTasksResponse(AbstractModel):
    """DescribeFirmwareTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfos: 固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfos: list of FirmwareTaskInfo
        :param _Total: 固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfos = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeGatewayBindDevicesRequest(AbstractModel):
    """DescribeGatewayBindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页的页大小
        :type Limit: int
        :param _ProductId: LoRa产品的ID
        :type ProductId: str
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._Offset = None
        self._Limit = None
        self._ProductId = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayBindDevicesResponse(AbstractModel):
    """DescribeGatewayBindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 子设备总数
        :type TotalCount: int
        :param _Devices: 子设备信息
        :type Devices: list of BindDeviceInfo
        :param _ProductName: 子设备所属的产品名
        :type ProductName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._ProductName = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = BindDeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._ProductName = params.get("ProductName")
        self._RequestId = params.get("RequestId")


class DescribePrivateCABindedProductsRequest(AbstractModel):
    """DescribePrivateCABindedProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertName: 证书名称
        :type CertName: str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询的数据量，默认为20， 最大为200
        :type Limit: int
        """
        self._CertName = None
        self._Offset = None
        self._Limit = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCABindedProductsResponse(AbstractModel):
    """DescribePrivateCABindedProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 私有CA绑定的产品列表
        :type Products: list of BindProductInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateCARequest(AbstractModel):
    """DescribePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertName: 私有化CA名称
        :type CertName: str
        """
        self._CertName = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCAResponse(AbstractModel):
    """DescribePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CA: 私有化CA详情
        :type CA: :class:`tencentcloud.iotcloud.v20210408.models.CertInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CA = None
        self._RequestId = None

    @property
    def CA(self):
        return self._CA

    @CA.setter
    def CA(self, CA):
        self._CA = CA

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CA") is not None:
            self._CA = CertInfo()
            self._CA._deserialize(params.get("CA"))
        self._RequestId = params.get("RequestId")


class DescribePrivateCAsRequest(AbstractModel):
    """DescribePrivateCAs请求参数结构体

    """


class DescribePrivateCAsResponse(AbstractModel):
    """DescribePrivateCAs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CAs: 私有CA证书列表
        :type CAs: list of CertInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CAs = None
        self._RequestId = None

    @property
    def CAs(self):
        return self._CAs

    @CAs.setter
    def CAs(self, CAs):
        self._CAs = CAs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self._CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CAs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductCARequest(AbstractModel):
    """DescribeProductCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductCAResponse(AbstractModel):
    """DescribeProductCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CAs: CA证书列表
        :type CAs: list of CertInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CAs = None
        self._RequestId = None

    @property
    def CAs(self):
        return self._CAs

    @CAs.setter
    def CAs(self, CAs):
        self._CAs = CAs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self._CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CAs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResourceRequest(AbstractModel):
    """DescribeProductResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 需要查看资源列表的产品 ID
        :type ProductID: str
        :param _Name: 需要过滤的资源名称
        :type Name: str
        """
        self._ProductID = None
        self._Name = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResourceResponse(AbstractModel):
    """DescribeProductResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 资源详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.iotcloud.v20210408.models.ProductResourceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ProductResourceInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeProductResourcesRequest(AbstractModel):
    """DescribeProductResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param _ProductID: 需要查看资源列表的产品 ID
        :type ProductID: str
        :param _Name: 需要过滤的资源名称
        :type Name: str
        """
        self._Offset = None
        self._Limit = None
        self._ProductID = None
        self._Name = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResourcesResponse(AbstractModel):
    """DescribeProductResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源总数
        :type TotalCount: int
        :param _Result: 资源详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of ProductResourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Result = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ProductResourceInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名
        :type ProductName: str
        :param _ProductMetadata: 产品元数据
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductMetadata = None
        self._ProductProperties = None
        self._RequestId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductMetadata(self):
        return self._ProductMetadata

    @ProductMetadata.setter
    def ProductMetadata(self, ProductMetadata):
        self._ProductMetadata = ProductMetadata

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self._ProductMetadata = ProductMetadata()
            self._ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        self._RequestId = params.get("RequestId")


class DescribeProductTaskRequest(AbstractModel):
    """DescribeProductTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._ProductId = None
        self._TaskId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductTaskResponse(AbstractModel):
    """DescribeProductTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfo: 产品任务详细信息
        :type TaskInfo: :class:`tencentcloud.iotcloud.v20210408.models.ProductTaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfo = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self._TaskInfo = ProductTaskInfo()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeProductTasksRequest(AbstractModel):
    """DescribeProductTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Offset: 产品级别任务列表偏移量
        :type Offset: int
        :param _Limit: 产品级别任务列表拉取个数
        :type Limit: int
        """
        self._ProductId = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductTasksResponse(AbstractModel):
    """DescribeProductTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的任务总个数
        :type TotalCount: int
        :param _TaskInfos: 任务详细信息列表
        :type TaskInfos: list of ProductTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = ProductTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页大小，当前页面中显示的最大数量，值范围 10-250。
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 产品总数
        :type TotalCount: int
        :param _Products: 产品详细信息列表
        :type Products: list of ProductInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Products = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePushResourceTaskStatisticsRequest(AbstractModel):
    """DescribePushResourceTaskStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Name: 资源名称
        :type Name: str
        """
        self._ProductID = None
        self._Name = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushResourceTaskStatisticsResponse(AbstractModel):
    """DescribePushResourceTaskStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessTotal: 推送成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotal: int
        :param _FailureTotal: 推送失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureTotal: int
        :param _UpgradingTotal: 正在推送的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradingTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessTotal = None
        self._FailureTotal = None
        self._UpgradingTotal = None
        self._RequestId = None

    @property
    def SuccessTotal(self):
        return self._SuccessTotal

    @SuccessTotal.setter
    def SuccessTotal(self, SuccessTotal):
        self._SuccessTotal = SuccessTotal

    @property
    def FailureTotal(self):
        return self._FailureTotal

    @FailureTotal.setter
    def FailureTotal(self, FailureTotal):
        self._FailureTotal = FailureTotal

    @property
    def UpgradingTotal(self):
        return self._UpgradingTotal

    @UpgradingTotal.setter
    def UpgradingTotal(self, UpgradingTotal):
        self._UpgradingTotal = UpgradingTotal

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessTotal = params.get("SuccessTotal")
        self._FailureTotal = params.get("FailureTotal")
        self._UpgradingTotal = params.get("UpgradingTotal")
        self._RequestId = params.get("RequestId")


class DescribeResourceTasksRequest(AbstractModel):
    """DescribeResourceTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Name: 资源名称
        :type Name: str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 返回查询结果条数
        :type Limit: int
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._ProductID = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTasksResponse(AbstractModel):
    """DescribeResourceTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfos: 资源任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfos: list of FirmwareTaskInfo
        :param _Total: 资源任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfos = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Online: 设备是否在线，0不在线，1在线
        :type Online: int
        :param _LoginTime: 设备登录时间
        :type LoginTime: int
        :param _Version: 设备版本
        :type Version: str
        :param _DeviceCert: 设备证书，证书加密的设备返回
        :type DeviceCert: str
        :param _DevicePsk: 设备密钥，密钥加密的设备返回
        :type DevicePsk: str
        :param _Tags: 设备属性
        :type Tags: list of DeviceTag
        :param _DeviceType: 设备类型
        :type DeviceType: int
        :param _Imei: 国际移动设备识别码 IMEI
        :type Imei: str
        :param _Isp: 运营商类型
        :type Isp: int
        :param _NbiotDeviceID: NB IOT运营商处的DeviceID
        :type NbiotDeviceID: str
        :param _ConnIP: IP地址
        :type ConnIP: int
        :param _LastUpdateTime: 设备最后更新时间
        :type LastUpdateTime: int
        :param _LoraDevEui: LoRa设备的dev eui
        :type LoraDevEui: str
        :param _LoraMoteType: LoRa设备的Mote type
        :type LoraMoteType: int
        :param _FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param _LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param _CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _LogLevel: 设备日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param _CertState: 设备证书获取状态, 1 已获取过设备密钥，0 未获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        :param _EnableState: 设备可用状态，0禁用，1启用
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param _Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        :param _ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param _FirmwareUpdateTime: ota最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirmwareUpdateTime: int
        :param _CreateUserId: 创建者 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _NBIoTDeviceID: NB IOT运营商处的DeviceID
        :type NBIoTDeviceID: str
        """
        self._DeviceName = None
        self._Online = None
        self._LoginTime = None
        self._Version = None
        self._DeviceCert = None
        self._DevicePsk = None
        self._Tags = None
        self._DeviceType = None
        self._Imei = None
        self._Isp = None
        self._NbiotDeviceID = None
        self._ConnIP = None
        self._LastUpdateTime = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._FirstOnlineTime = None
        self._LastOfflineTime = None
        self._CreateTime = None
        self._LogLevel = None
        self._CertState = None
        self._EnableState = None
        self._Labels = None
        self._ClientIP = None
        self._FirmwareUpdateTime = None
        self._CreateUserId = None
        self._NBIoTDeviceID = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def NbiotDeviceID(self):
        warnings.warn("parameter `NbiotDeviceID` is deprecated", DeprecationWarning) 

        return self._NbiotDeviceID

    @NbiotDeviceID.setter
    def NbiotDeviceID(self, NbiotDeviceID):
        warnings.warn("parameter `NbiotDeviceID` is deprecated", DeprecationWarning) 

        self._NbiotDeviceID = NbiotDeviceID

    @property
    def ConnIP(self):
        return self._ConnIP

    @ConnIP.setter
    def ConnIP(self, ConnIP):
        self._ConnIP = ConnIP

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def FirstOnlineTime(self):
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LastOfflineTime(self):
        return self._LastOfflineTime

    @LastOfflineTime.setter
    def LastOfflineTime(self, LastOfflineTime):
        self._LastOfflineTime = LastOfflineTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def CertState(self):
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def FirmwareUpdateTime(self):
        return self._FirmwareUpdateTime

    @FirmwareUpdateTime.setter
    def FirmwareUpdateTime(self, FirmwareUpdateTime):
        self._FirmwareUpdateTime = FirmwareUpdateTime

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def NBIoTDeviceID(self):
        return self._NBIoTDeviceID

    @NBIoTDeviceID.setter
    def NBIoTDeviceID(self, NBIoTDeviceID):
        self._NBIoTDeviceID = NBIoTDeviceID


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Online = params.get("Online")
        self._LoginTime = params.get("LoginTime")
        self._Version = params.get("Version")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeviceType = params.get("DeviceType")
        self._Imei = params.get("Imei")
        self._Isp = params.get("Isp")
        self._NbiotDeviceID = params.get("NbiotDeviceID")
        self._ConnIP = params.get("ConnIP")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._FirstOnlineTime = params.get("FirstOnlineTime")
        self._LastOfflineTime = params.get("LastOfflineTime")
        self._CreateTime = params.get("CreateTime")
        self._LogLevel = params.get("LogLevel")
        self._CertState = params.get("CertState")
        self._EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._ClientIP = params.get("ClientIP")
        self._FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        self._CreateUserId = params.get("CreateUserId")
        self._NBIoTDeviceID = params.get("NBIoTDeviceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLabel(AbstractModel):
    """设备标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签标识
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceResourceInfo(AbstractModel):
    """设备资源详细信息

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _ProductName: 产品名
        :type ProductName: str
        :param _Name: 资源名称
        :type Name: str
        :param _Md5: 资源文件md5
        :type Md5: str
        :param _Size: 资源文件大小
        :type Size: int
        :param _UpdateTime: 资源更新时间
        :type UpdateTime: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Status: 设备资源上传状态
        :type Status: int
        :param _Percent: 设备资源上传百分比
        :type Percent: int
        """
        self._ProductID = None
        self._ProductName = None
        self._Name = None
        self._Md5 = None
        self._Size = None
        self._UpdateTime = None
        self._DeviceName = None
        self._Status = None
        self._Percent = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._ProductName = params.get("ProductName")
        self._Name = params.get("Name")
        self._Md5 = params.get("Md5")
        self._Size = params.get("Size")
        self._UpdateTime = params.get("UpdateTime")
        self._DeviceName = params.get("DeviceName")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTag(AbstractModel):
    """设备属性

    """

    def __init__(self):
        r"""
        :param _Tag: 属性名称
        :type Tag: str
        :param _Type: 属性值的类型，1 int，2 string
        :type Type: int
        :param _Value: 属性的值
        :type Value: str
        :param _Name: 属性描述名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Tag = None
        self._Type = None
        self._Value = None
        self._Name = None

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUpdateStatus(AbstractModel):
    """设备固件更新状态

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _LastProcessTime: 最后处理时间
        :type LastProcessTime: int
        :param _Status: 状态
        :type Status: int
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _Retcode: 返回码
        :type Retcode: int
        :param _DstVersion: 目标更新版本
        :type DstVersion: str
        :param _Percent: 下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _OriVersion: 原版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriVersion: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        """
        self._DeviceName = None
        self._LastProcessTime = None
        self._Status = None
        self._ErrMsg = None
        self._Retcode = None
        self._DstVersion = None
        self._Percent = None
        self._OriVersion = None
        self._TaskId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LastProcessTime(self):
        return self._LastProcessTime

    @LastProcessTime.setter
    def LastProcessTime(self, LastProcessTime):
        self._LastProcessTime = LastProcessTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Retcode(self):
        return self._Retcode

    @Retcode.setter
    def Retcode(self, Retcode):
        self._Retcode = Retcode

    @property
    def DstVersion(self):
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def OriVersion(self):
        return self._OriVersion

    @OriVersion.setter
    def OriVersion(self, OriVersion):
        self._OriVersion = OriVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._LastProcessTime = params.get("LastProcessTime")
        self._Status = params.get("Status")
        self._ErrMsg = params.get("ErrMsg")
        self._Retcode = params.get("Retcode")
        self._DstVersion = params.get("DstVersion")
        self._Percent = params.get("Percent")
        self._OriVersion = params.get("OriVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableTopicRuleRequest(AbstractModel):
    """DisableTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableTopicRuleResponse(AbstractModel):
    """DisableTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DownloadDeviceResourceRequest(AbstractModel):
    """DownloadDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Name: 资源名称
        :type Name: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductID = None
        self._Name = None
        self._DeviceName = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Name = params.get("Name")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadDeviceResourceResponse(AbstractModel):
    """DownloadDeviceResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 设备资源的cos链接
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class EditFirmwareRequest(AbstractModel):
    """EditFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号。
        :type FirmwareVersion: str
        :param _FirmwareName: 固件名称。
        :type FirmwareName: str
        :param _FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        :param _FirmwareUserDefined: 固件用户自定义配置信息
        :type FirmwareUserDefined: str
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._FirmwareName = None
        self._FirmwareDescription = None
        self._FirmwareUserDefined = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareName(self):
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription

    @property
    def FirmwareUserDefined(self):
        return self._FirmwareUserDefined

    @FirmwareUserDefined.setter
    def FirmwareUserDefined(self, FirmwareUserDefined):
        self._FirmwareUserDefined = FirmwareUserDefined


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        self._FirmwareUserDefined = params.get("FirmwareUserDefined")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditFirmwareResponse(AbstractModel):
    """EditFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableTopicRuleRequest(AbstractModel):
    """EnableTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableTopicRuleResponse(AbstractModel):
    """EnableTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        r"""
        :param _Version: 固件版本
        :type Version: str
        :param _Md5sum: 固件MD5值
        :type Md5sum: str
        :param _CreateTime: 固件创建时间
        :type CreateTime: int
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _FwType: 固件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FwType: str
        :param _CreateUserId: 创建者 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _UserDefined: 固件用户自定义配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefined: str
        """
        self._Version = None
        self._Md5sum = None
        self._CreateTime = None
        self._ProductName = None
        self._Name = None
        self._Description = None
        self._ProductId = None
        self._FwType = None
        self._CreateUserId = None
        self._UserDefined = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Md5sum(self):
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FwType(self):
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def UserDefined(self):
        return self._UserDefined

    @UserDefined.setter
    def UserDefined(self, UserDefined):
        self._UserDefined = UserDefined


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Md5sum = params.get("Md5sum")
        self._CreateTime = params.get("CreateTime")
        self._ProductName = params.get("ProductName")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ProductId = params.get("ProductId")
        self._FwType = params.get("FwType")
        self._CreateUserId = params.get("CreateUserId")
        self._UserDefined = params.get("UserDefined")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareTaskInfo(AbstractModel):
    """固件升级任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        """
        self._TaskId = None
        self._Status = None
        self._Type = None
        self._CreateTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAllVersionRequest(AbstractModel):
    """GetAllVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAllVersionResponse(AbstractModel):
    """GetAllVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 版本号列表
        :type Version: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class GetCOSURLRequest(AbstractModel):
    """GetCOSURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param _FileSize: 固件版本大小
        :type FileSize: int
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._FileSize = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCOSURLResponse(AbstractModel):
    """GetCOSURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 固件URL
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class GetUserResourceInfoRequest(AbstractModel):
    """GetUserResourceInfo请求参数结构体

    """


class GetUserResourceInfoResponse(AbstractModel):
    """GetUserResourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsedSize: 已使用的资源字节数
        :type UsedSize: int
        :param _Limit: 可以使用资源的总大小
        :type Limit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsedSize = None
        self._Limit = None
        self._RequestId = None

    @property
    def UsedSize(self):
        return self._UsedSize

    @UsedSize.setter
    def UsedSize(self, UsedSize):
        self._UsedSize = UsedSize

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UsedSize = params.get("UsedSize")
        self._Limit = params.get("Limit")
        self._RequestId = params.get("RequestId")


class ListFirmwaresRequest(AbstractModel):
    """ListFirmwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 获取的页数
        :type PageNum: int
        :param _PageSize: 分页的大小
        :type PageSize: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._PageNum = None
        self._PageSize = None
        self._ProductId = None
        self._Filters = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProductId = params.get("ProductId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFirmwaresResponse(AbstractModel):
    """ListFirmwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 固件总数
        :type TotalCount: int
        :param _Firmwares: 固件列表
        :type Firmwares: list of FirmwareInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Firmwares = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Firmwares(self):
        return self._Firmwares

    @Firmwares.setter
    def Firmwares(self, Firmwares):
        self._Firmwares = Firmwares

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Firmwares") is not None:
            self._Firmwares = []
            for item in params.get("Firmwares"):
                obj = FirmwareInfo()
                obj._deserialize(item)
                self._Firmwares.append(obj)
        self._RequestId = params.get("RequestId")


class ListLogPayloadRequest(AbstractModel):
    """ListLogPayload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 日志开始时间，毫秒级时间戳
        :type MinTime: int
        :param _MaxTime: 日志结束时间，毫秒级时间戳
        :type MaxTime: int
        :param _Keywords: 查询关键字，可以同时支持键值查询和文本查询，例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。键值或文本可以包含多个，以空格隔开。其中可以索引的key比如：RequestID、ProductID、DeviceName等。
一个典型的查询示例：ProductID:ABCDE12345 DeviceName:test publish
        :type Keywords: str
        :param _Context: 日志检索上下文
        :type Context: str
        :param _MaxNum: 日志最大条数
        :type MaxNum: int
        """
        self._MinTime = None
        self._MaxTime = None
        self._Keywords = None
        self._Context = None
        self._MaxNum = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._Keywords = params.get("Keywords")
        self._Context = params.get("Context")
        self._MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogPayloadResponse(AbstractModel):
    """ListLogPayload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 日志上下文
        :type Context: str
        :param _Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param _Results: 日志列表
        :type Results: list of PayloadLogItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = PayloadLogItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class ListLogRequest(AbstractModel):
    """ListLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 日志开始时间，毫秒级时间戳
        :type MinTime: int
        :param _MaxTime: 日志结束时间，毫秒级时间戳
        :type MaxTime: int
        :param _Keywords: 查询关键字，可以同时支持键值查询和文本查询，例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。键值或文本可以包含多个，以空格隔开。其中可以索引的key包括：requestid、productid、devicename、scene、content。
一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW content:Device%20connect publish
        :type Keywords: str
        :param _Context: 日志检索上下文
        :type Context: str
        :param _MaxNum: 查询条数
        :type MaxNum: int
        """
        self._MinTime = None
        self._MaxTime = None
        self._Keywords = None
        self._Context = None
        self._MaxNum = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._Keywords = params.get("Keywords")
        self._Context = params.get("Context")
        self._MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogResponse(AbstractModel):
    """ListLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 日志上下文
        :type Context: str
        :param _Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param _Results: 日志列表
        :type Results: list of CLSLogItem
        :param _TotalCount: 日志总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = CLSLogItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListSDKLogRequest(AbstractModel):
    """ListSDKLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 日志开始时间
        :type MinTime: int
        :param _MaxTime: 日志结束时间
        :type MaxTime: int
        :param _Keywords: 查询关键字，可以同时支持键值查询和文本查询，
例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。
键值或文本可以包含多个，以空格隔开。
其中可以索引的key包括：productid、devicename、loglevel
一个典型的查询示例：productid:7JK1G72JNE devicename:name publish loglevel:WARN一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW publish
        :type Keywords: str
        :param _Context: 日志检索上下文
        :type Context: str
        :param _MaxNum: 查询条数
        :type MaxNum: int
        """
        self._MinTime = None
        self._MaxTime = None
        self._Keywords = None
        self._Context = None
        self._MaxNum = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._Keywords = params.get("Keywords")
        self._Context = params.get("Context")
        self._MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSDKLogResponse(AbstractModel):
    """ListSDKLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 日志检索上下文
        :type Context: str
        :param _Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param _Results: 日志列表
        :type Results: list of SDKLogItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = SDKLogItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopicRulesRequest(AbstractModel):
    """ListTopicRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 请求的页数
        :type PageNum: int
        :param _PageSize: 分页的大小
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopicRulesResponse(AbstractModel):
    """ListTopicRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 规则总数量
        :type TotalCnt: int
        :param _Rules: 规则列表
        :type Rules: list of TopicRuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._Rules = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = TopicRuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class PayloadLogItem(AbstractModel):
    """内容日志项

    """

    def __init__(self):
        r"""
        :param _Uin: 账号id
        :type Uin: str
        :param _ProductId: 产品id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _SrcType: 来源类型
        :type SrcType: str
        :param _SrcName: 来源名称
        :type SrcName: str
        :param _Topic: 消息topic
        :type Topic: str
        :param _PayloadFormatType: 内容格式类型
        :type PayloadFormatType: str
        :param _Payload: 内容信息
        :type Payload: str
        :param _RequestId: 请求ID
        :type RequestId: str
        :param _DateTime: 日期时间
        :type DateTime: str
        """
        self._Uin = None
        self._ProductId = None
        self._DeviceName = None
        self._SrcType = None
        self._SrcName = None
        self._Topic = None
        self._PayloadFormatType = None
        self._Payload = None
        self._RequestId = None
        self._DateTime = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def SrcType(self):
        return self._SrcType

    @SrcType.setter
    def SrcType(self, SrcType):
        self._SrcType = SrcType

    @property
    def SrcName(self):
        return self._SrcName

    @SrcName.setter
    def SrcName(self, SrcName):
        self._SrcName = SrcName

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def PayloadFormatType(self):
        return self._PayloadFormatType

    @PayloadFormatType.setter
    def PayloadFormatType(self, PayloadFormatType):
        self._PayloadFormatType = PayloadFormatType

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def DateTime(self):
        return self._DateTime

    @DateTime.setter
    def DateTime(self, DateTime):
        self._DateTime = DateTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._SrcType = params.get("SrcType")
        self._SrcName = params.get("SrcName")
        self._Topic = params.get("Topic")
        self._PayloadFormatType = params.get("PayloadFormatType")
        self._Payload = params.get("Payload")
        self._RequestId = params.get("RequestId")
        self._DateTime = params.get("DateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """产品详细信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名
        :type ProductName: str
        :param _ProductMetadata: 产品元数据
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductMetadata = None
        self._ProductProperties = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductMetadata(self):
        return self._ProductMetadata

    @ProductMetadata.setter
    def ProductMetadata(self, ProductMetadata):
        self._ProductMetadata = ProductMetadata

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self._ProductMetadata = ProductMetadata()
            self._ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductMetadata(AbstractModel):
    """产品元数据

    """

    def __init__(self):
        r"""
        :param _CreationDate: 产品创建时间
        :type CreationDate: int
        :param _CreateUserId: 创建者 Uin
        :type CreateUserId: int
        :param _UserId: 账号 Uin
        :type UserId: int
        """
        self._CreationDate = None
        self._CreateUserId = None
        self._UserId = None

    @property
    def CreationDate(self):
        return self._CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self._CreationDate = CreationDate

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._CreationDate = params.get("CreationDate")
        self._CreateUserId = params.get("CreateUserId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductProperties(AbstractModel):
    """产品属性

    """

    def __init__(self):
        r"""
        :param _ProductDescription: 产品描述
        :type ProductDescription: str
        :param _EncryptionType: 加密类型，1表示证书认证，2表示签名认证。如不填写，默认值是1
        :type EncryptionType: str
        :param _Region: 产品所属区域，目前只支持广州（gz）
        :type Region: str
        :param _ProductType: 产品类型，各个类型值代表的节点-类型如下：
0 普通产品，2 NB-IoT产品，4 LoRa产品，3 LoRa网关产品，5 普通网关产品   默认值是0
        :type ProductType: int
        :param _Format: 数据格式，取值为json或者custom，默认值是json
        :type Format: str
        :param _Platform: 产品所属平台，默认值是0
        :type Platform: str
        :param _Appeui: LoRa产品运营侧APPEUI，只有LoRa产品需要填写
        :type Appeui: str
        :param _ModelId: 产品绑定的物模型ID，-1表示不绑定
        :type ModelId: str
        :param _ModelName: 产品绑定的物模型名称
        :type ModelName: str
        :param _ProductKey: 产品密钥，suite产品才会有
        :type ProductKey: str
        :param _RegisterType: 动态注册类型 0-关闭, 1-预定义设备名 2-动态定义设备名
        :type RegisterType: int
        :param _ProductSecret: 动态注册产品密钥
        :type ProductSecret: str
        :param _RegisterLimit: RegisterType为2时，设备动态创建的限制数量
        :type RegisterLimit: int
        :param _OriginProductId: 划归的产品，展示为源产品ID，其余为空
        :type OriginProductId: str
        :param _PrivateCAName: 私有CA名称
        :type PrivateCAName: str
        :param _OriginUserId: 划归的产品，展示为源用户ID，其余为空
        :type OriginUserId: int
        :param _DeviceLimit: 设备限制
        :type DeviceLimit: int
        :param _ForbiddenStatus: 产品禁用状态
        :type ForbiddenStatus: int
        :param _AppEUI: LoRa产品运营侧APPEUI，只有LoRa产品需要填写
        :type AppEUI: str
        """
        self._ProductDescription = None
        self._EncryptionType = None
        self._Region = None
        self._ProductType = None
        self._Format = None
        self._Platform = None
        self._Appeui = None
        self._ModelId = None
        self._ModelName = None
        self._ProductKey = None
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._OriginProductId = None
        self._PrivateCAName = None
        self._OriginUserId = None
        self._DeviceLimit = None
        self._ForbiddenStatus = None
        self._AppEUI = None

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def EncryptionType(self):
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Appeui(self):
        warnings.warn("parameter `Appeui` is deprecated", DeprecationWarning) 

        return self._Appeui

    @Appeui.setter
    def Appeui(self, Appeui):
        warnings.warn("parameter `Appeui` is deprecated", DeprecationWarning) 

        self._Appeui = Appeui

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ProductKey(self):
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def OriginProductId(self):
        return self._OriginProductId

    @OriginProductId.setter
    def OriginProductId(self, OriginProductId):
        self._OriginProductId = OriginProductId

    @property
    def PrivateCAName(self):
        return self._PrivateCAName

    @PrivateCAName.setter
    def PrivateCAName(self, PrivateCAName):
        self._PrivateCAName = PrivateCAName

    @property
    def OriginUserId(self):
        return self._OriginUserId

    @OriginUserId.setter
    def OriginUserId(self, OriginUserId):
        self._OriginUserId = OriginUserId

    @property
    def DeviceLimit(self):
        return self._DeviceLimit

    @DeviceLimit.setter
    def DeviceLimit(self, DeviceLimit):
        self._DeviceLimit = DeviceLimit

    @property
    def ForbiddenStatus(self):
        return self._ForbiddenStatus

    @ForbiddenStatus.setter
    def ForbiddenStatus(self, ForbiddenStatus):
        self._ForbiddenStatus = ForbiddenStatus

    @property
    def AppEUI(self):
        return self._AppEUI

    @AppEUI.setter
    def AppEUI(self, AppEUI):
        self._AppEUI = AppEUI


    def _deserialize(self, params):
        self._ProductDescription = params.get("ProductDescription")
        self._EncryptionType = params.get("EncryptionType")
        self._Region = params.get("Region")
        self._ProductType = params.get("ProductType")
        self._Format = params.get("Format")
        self._Platform = params.get("Platform")
        self._Appeui = params.get("Appeui")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ProductKey = params.get("ProductKey")
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._OriginProductId = params.get("OriginProductId")
        self._PrivateCAName = params.get("PrivateCAName")
        self._OriginUserId = params.get("OriginUserId")
        self._DeviceLimit = params.get("DeviceLimit")
        self._ForbiddenStatus = params.get("ForbiddenStatus")
        self._AppEUI = params.get("AppEUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductResourceInfo(AbstractModel):
    """产品资源详细信息

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _ProductName: 产品名
        :type ProductName: str
        :param _Name: 资源名称
        :type Name: str
        :param _Md5: 资源文件md5
        :type Md5: str
        :param _Size: 资源文件大小
        :type Size: int
        :param _Description: 资源文件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 资源创建时间
        :type CreateTime: str
        """
        self._ProductID = None
        self._ProductName = None
        self._Name = None
        self._Md5 = None
        self._Size = None
        self._Description = None
        self._CreateTime = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._ProductName = params.get("ProductName")
        self._Name = params.get("Name")
        self._Md5 = params.get("Md5")
        self._Size = params.get("Size")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductTaskInfo(AbstractModel):
    """产品级任务详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: int
        :param _Type: 任务类型 0-批量创建设备类型
        :type Type: int
        :param _State: 任务状态 0-创建中 1-待执行 2-执行中 3-执行失败 4-子任务部分失败 5-执行成功
        :type State: int
        :param _ParametersType: 任务参数类型 cosfile-文件输入 random-随机生成
        :type ParametersType: str
        :param _Parameters: 任务参数
        :type Parameters: str
        :param _ResultType: 任务执行结果类型 cosfile-文件输出 errmsg-错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param _Result: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _BatchCount: 子任务总个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchCount: int
        :param _BatchOffset: 子任务已执行个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchOffset: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: int
        :param _UpdateTime: 任务更新时间
        :type UpdateTime: int
        :param _CompleteTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteTime: int
        """
        self._Id = None
        self._Type = None
        self._State = None
        self._ParametersType = None
        self._Parameters = None
        self._ResultType = None
        self._Result = None
        self._BatchCount = None
        self._BatchOffset = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CompleteTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ParametersType(self):
        return self._ParametersType

    @ParametersType.setter
    def ParametersType(self, ParametersType):
        self._ParametersType = ParametersType

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def ResultType(self):
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def BatchCount(self):
        return self._BatchCount

    @BatchCount.setter
    def BatchCount(self, BatchCount):
        self._BatchCount = BatchCount

    @property
    def BatchOffset(self):
        return self._BatchOffset

    @BatchOffset.setter
    def BatchOffset(self, BatchOffset):
        self._BatchOffset = BatchOffset

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CompleteTime(self):
        return self._CompleteTime

    @CompleteTime.setter
    def CompleteTime(self, CompleteTime):
        self._CompleteTime = CompleteTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._State = params.get("State")
        self._ParametersType = params.get("ParametersType")
        self._Parameters = params.get("Parameters")
        self._ResultType = params.get("ResultType")
        self._Result = params.get("Result")
        self._BatchCount = params.get("BatchCount")
        self._BatchOffset = params.get("BatchOffset")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CompleteTime = params.get("CompleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishBroadcastMessageRequest(AbstractModel):
    """PublishBroadcastMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Payload: 消息内容
        :type Payload: str
        :param _Qos: 消息质量等级
        :type Qos: int
        :param _PayloadEncoding: Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
        :type PayloadEncoding: str
        """
        self._ProductId = None
        self._Payload = None
        self._Qos = None
        self._PayloadEncoding = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        return self._PayloadEncoding

    @PayloadEncoding.setter
    def PayloadEncoding(self, PayloadEncoding):
        self._PayloadEncoding = PayloadEncoding


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Payload = params.get("Payload")
        self._Qos = params.get("Qos")
        self._PayloadEncoding = params.get("PayloadEncoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishBroadcastMessageResponse(AbstractModel):
    """PublishBroadcastMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 广播消息任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: 消息发往的主题。命名规则：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}
        :type Topic: str
        :param _Payload: 消息内容
        :type Payload: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Qos: 服务质量等级，取值为0或1
        :type Qos: int
        :param _PayloadEncoding: Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
        :type PayloadEncoding: str
        """
        self._Topic = None
        self._Payload = None
        self._ProductId = None
        self._DeviceName = None
        self._Qos = None
        self._PayloadEncoding = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        return self._PayloadEncoding

    @PayloadEncoding.setter
    def PayloadEncoding(self, PayloadEncoding):
        self._PayloadEncoding = PayloadEncoding


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Qos = params.get("Qos")
        self._PayloadEncoding = params.get("PayloadEncoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PublishRRPCMessageRequest(AbstractModel):
    """PublishRRPCMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Payload: 消息内容，utf8编码
        :type Payload: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Payload = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishRRPCMessageResponse(AbstractModel):
    """PublishRRPCMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: RRPC消息ID
        :type MessageId: int
        :param _PayloadBase64: 设备回复的消息内容，采用base64编码
        :type PayloadBase64: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._PayloadBase64 = None
        self._RequestId = None

    @property
    def MessageId(self):
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def PayloadBase64(self):
        return self._PayloadBase64

    @PayloadBase64.setter
    def PayloadBase64(self, PayloadBase64):
        self._PayloadBase64 = PayloadBase64

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._PayloadBase64 = params.get("PayloadBase64")
        self._RequestId = params.get("RequestId")


class ReplaceTopicRuleRequest(AbstractModel):
    """ReplaceTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _TopicRulePayload: 替换的规则包体
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20210408.models.TopicRulePayload`
        """
        self._RuleName = None
        self._TopicRulePayload = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def TopicRulePayload(self):
        return self._TopicRulePayload

    @TopicRulePayload.setter
    def TopicRulePayload(self, TopicRulePayload):
        self._TopicRulePayload = TopicRulePayload


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self._TopicRulePayload = TopicRulePayload()
            self._TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceTopicRuleResponse(AbstractModel):
    """ReplaceTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetDeviceResult(AbstractModel):
    """重置设备状态结果

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Success: 是否成功
        :type Success: bool
        :param _Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._DeviceName = None
        self._Success = None
        self._Reason = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Success = params.get("Success")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceStateRequest(AbstractModel):
    """ResetDeviceState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceNames: 设备名称
        :type DeviceNames: list of str
        """
        self._ProductId = None
        self._DeviceNames = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceStateResponse(AbstractModel):
    """ResetDeviceState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessCount: 批量重置设备成功数
        :type SuccessCount: int
        :param _ResetDeviceResults: 批量重置设备结果
        :type ResetDeviceResults: list of ResetDeviceResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessCount = None
        self._ResetDeviceResults = None
        self._RequestId = None

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def ResetDeviceResults(self):
        return self._ResetDeviceResults

    @ResetDeviceResults.setter
    def ResetDeviceResults(self, ResetDeviceResults):
        self._ResetDeviceResults = ResetDeviceResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessCount = params.get("SuccessCount")
        if params.get("ResetDeviceResults") is not None:
            self._ResetDeviceResults = []
            for item in params.get("ResetDeviceResults"):
                obj = ResetDeviceResult()
                obj._deserialize(item)
                self._ResetDeviceResults.append(obj)
        self._RequestId = params.get("RequestId")


class RetryDeviceFirmwareTaskRequest(AbstractModel):
    """RetryDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDeviceFirmwareTaskResponse(AbstractModel):
    """RetryDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SDKLogItem(AbstractModel):
    """SDK日志项

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Level: 日志等级
        :type Level: str
        :param _DateTime: 日志时间
        :type DateTime: str
        :param _Content: 日志内容
        :type Content: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Level = None
        self._DateTime = None
        self._Content = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def DateTime(self):
        return self._DateTime

    @DateTime.setter
    def DateTime(self, DateTime):
        self._DateTime = DateTime

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Level = params.get("Level")
        self._DateTime = params.get("DateTime")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKeyword(AbstractModel):
    """搜索关键词

    """

    def __init__(self):
        r"""
        :param _Key: 搜索条件的Key
        :type Key: str
        :param _Value: 搜索条件的值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusRequest(AbstractModel):
    """SetProductsForbiddenStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 要设置禁用状态的产品列表
        :type ProductId: list of str
        :param _Status: 0启用，1禁用
        :type Status: int
        """
        self._ProductId = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusResponse(AbstractModel):
    """SetProductsForbiddenStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StatusStatistic(AbstractModel):
    """状态统计信息

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Total: 统计总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._Status = None
        self._Total = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRuleInfo(AbstractModel):
    """规则详细信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Description: 规则描述
        :type Description: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: int
        :param _RuleDisabled: 不生效
        :type RuleDisabled: bool
        :param _TopicPattern: 规则模式
        :type TopicPattern: str
        """
        self._RuleName = None
        self._Description = None
        self._CreatedAt = None
        self._RuleDisabled = None
        self._TopicPattern = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RuleDisabled(self):
        return self._RuleDisabled

    @RuleDisabled.setter
    def RuleDisabled(self, RuleDisabled):
        self._RuleDisabled = RuleDisabled

    @property
    def TopicPattern(self):
        return self._TopicPattern

    @TopicPattern.setter
    def TopicPattern(self, TopicPattern):
        self._TopicPattern = TopicPattern


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        self._CreatedAt = params.get("CreatedAt")
        self._RuleDisabled = params.get("RuleDisabled")
        self._TopicPattern = params.get("TopicPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRulePayload(AbstractModel):
    """创建规则请求包体

    """

    def __init__(self):
        r"""
        :param _Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param _Actions: 行为的JSON字符串，大部分种类举例如下：
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
        :param _Description: 规则描述
        :type Description: str
        :param _RuleDisabled: 是否禁用规则
        :type RuleDisabled: bool
        """
        self._Sql = None
        self._Actions = None
        self._Description = None
        self._RuleDisabled = None

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleDisabled(self):
        return self._RuleDisabled

    @RuleDisabled.setter
    def RuleDisabled(self, RuleDisabled):
        self._RuleDisabled = RuleDisabled


    def _deserialize(self, params):
        self._Sql = params.get("Sql")
        self._Actions = params.get("Actions")
        self._Description = params.get("Description")
        self._RuleDisabled = params.get("RuleDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDevicesRequest(AbstractModel):
    """UnbindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceNames: 多个设备名
        :type DeviceNames: list of str
        :param _Skey: 中兴CLAA设备的解绑需要Skey，普通设备不需要
        :type Skey: str
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._ProductId = None
        self._DeviceNames = None
        self._Skey = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDevicesResponse(AbstractModel):
    """UnbindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateDeviceAvailableStateRequest(AbstractModel):
    """UpdateDeviceAvailableState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 设备所属产品id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _EnableState: 要设置的设备状态，1为启用，0为禁用
        :type EnableState: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._EnableState = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceAvailableStateResponse(AbstractModel):
    """UpdateDeviceAvailableState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateDeviceLogLevelRequest(AbstractModel):
    """UpdateDeviceLogLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _LogLevel: 日志级别，0：关闭，1：错误，2：告警，3：信息，4：调试
        :type LogLevel: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._LogLevel = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceLogLevelResponse(AbstractModel):
    """UpdateDeviceLogLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateDevicePSKRequest(AbstractModel):
    """UpdateDevicePSK请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品名
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Psk: 设备的psk
        :type Psk: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Psk = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Psk(self):
        return self._Psk

    @Psk.setter
    def Psk(self, Psk):
        self._Psk = Psk


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Psk = params.get("Psk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicePSKResponse(AbstractModel):
    """UpdateDevicePSK返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateDeviceShadowRequest(AbstractModel):
    """UpdateDeviceShadow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _State: 虚拟设备的状态，JSON字符串格式，由desired结构组成
        :type State: str
        :param _ShadowVersion: 当前版本号，需要和后台的version保持一致，才能更新成功
        :type ShadowVersion: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._State = None
        self._ShadowVersion = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ShadowVersion(self):
        return self._ShadowVersion

    @ShadowVersion.setter
    def ShadowVersion(self, ShadowVersion):
        self._ShadowVersion = ShadowVersion


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._State = params.get("State")
        self._ShadowVersion = params.get("ShadowVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceShadowResponse(AbstractModel):
    """UpdateDeviceShadow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备影子数据，JSON字符串格式
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 设备所属产品id
        :type ProductId: str
        :param _DeviceNames: 设备名称集合
        :type DeviceNames: list of str
        :param _Status: 要设置的设备状态，1为启用，0为禁用
        :type Status: int
        """
        self._ProductId = None
        self._DeviceNames = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicesEnableStateResponse(AbstractModel):
    """UpdateDevicesEnableState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateOtaTaskStatusRequest(AbstractModel):
    """UpdateOtaTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        :param _Status: 固件任务取消状态
        :type Status: int
        """
        self._ProductId = None
        self._TaskId = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOtaTaskStatusResponse(AbstractModel):
    """UpdateOtaTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdatePrivateCARequest(AbstractModel):
    """UpdatePrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertName: CA证书名称
        :type CertName: str
        :param _CertText: CA证书内容
        :type CertText: str
        :param _VerifyCertText: 校验CA证书的证书内容
        :type VerifyCertText: str
        """
        self._CertName = None
        self._CertText = None
        self._VerifyCertText = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertText(self):
        return self._CertText

    @CertText.setter
    def CertText(self, CertText):
        self._CertText = CertText

    @property
    def VerifyCertText(self):
        return self._VerifyCertText

    @VerifyCertText.setter
    def VerifyCertText(self, VerifyCertText):
        self._VerifyCertText = VerifyCertText


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertText = params.get("CertText")
        self._VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrivateCAResponse(AbstractModel):
    """UpdatePrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateProductDynamicRegisterRequest(AbstractModel):
    """UpdateProductDynamicRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param _RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        """
        self._ProductId = None
        self._RegisterType = None
        self._RegisterLimit = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._RegisterType = params.get("RegisterType")
        self._RegisterLimit = params.get("RegisterLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductDynamicRegisterResponse(AbstractModel):
    """UpdateProductDynamicRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param _ProductSecret: 动态注册产品密钥
        :type ProductSecret: str
        :param _RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._RequestId = None

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._RequestId = params.get("RequestId")


class UpdateProductPrivateCARequest(AbstractModel):
    """UpdateProductPrivateCA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _CertName: 私有CA证书名称
        :type CertName: str
        """
        self._ProductId = None
        self._CertName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductPrivateCAResponse(AbstractModel):
    """UpdateProductPrivateCA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateTopicPolicyRequest(AbstractModel):
    """UpdateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TopicName: 更新前Topic名
        :type TopicName: str
        :param _NewTopicName: 更新后Topic名
        :type NewTopicName: str
        :param _Privilege: Topic权限
        :type Privilege: int
        :param _BrokerSubscribe: 代理订阅信息
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20210408.models.BrokerSubscribe`
        """
        self._ProductId = None
        self._TopicName = None
        self._NewTopicName = None
        self._Privilege = None
        self._BrokerSubscribe = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def NewTopicName(self):
        return self._NewTopicName

    @NewTopicName.setter
    def NewTopicName(self, NewTopicName):
        self._NewTopicName = NewTopicName

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def BrokerSubscribe(self):
        return self._BrokerSubscribe

    @BrokerSubscribe.setter
    def BrokerSubscribe(self, BrokerSubscribe):
        self._BrokerSubscribe = BrokerSubscribe


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        self._NewTopicName = params.get("NewTopicName")
        self._Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self._BrokerSubscribe = BrokerSubscribe()
            self._BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTopicPolicyResponse(AbstractModel):
    """UpdateTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UploadFirmwareRequest(AbstractModel):
    """UploadFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _Md5sum: 固件的MD5值
        :type Md5sum: str
        :param _FileSize: 固件的大小
        :type FileSize: int
        :param _FirmwareName: 固件名称
        :type FirmwareName: str
        :param _FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        :param _FirmwareUserDefined: 固件用户自定义配置信息
        :type FirmwareUserDefined: str
        """
        self._ProductId = None
        self._FirmwareVersion = None
        self._Md5sum = None
        self._FileSize = None
        self._FirmwareName = None
        self._FirmwareDescription = None
        self._FirmwareUserDefined = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Md5sum(self):
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FirmwareName(self):
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription

    @property
    def FirmwareUserDefined(self):
        return self._FirmwareUserDefined

    @FirmwareUserDefined.setter
    def FirmwareUserDefined(self, FirmwareUserDefined):
        self._FirmwareUserDefined = FirmwareUserDefined


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._Md5sum = params.get("Md5sum")
        self._FileSize = params.get("FileSize")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        self._FirmwareUserDefined = params.get("FirmwareUserDefined")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFirmwareResponse(AbstractModel):
    """UploadFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")