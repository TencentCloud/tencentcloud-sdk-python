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
        """属性列表
        :rtype: list of DeviceTag
        """
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
        


class BatchPublishMessage(AbstractModel):
    """批量发消息请求

    """

    def __init__(self):
        r"""
        :param _Topic: 消息发往的主题。为 Topic 权限中去除 ProductID 和 DeviceName 的部分，如 “event”
        :type Topic: str
        :param _Payload: 消息内容
        :type Payload: str
        """
        self._Topic = None
        self._Payload = None

    @property
    def Topic(self):
        """消息发往的主题。为 Topic 权限中去除 ProductID 和 DeviceName 的部分，如 “event”
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        """消息内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
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
        :param _ProductID: 产品ID
        :type ProductID: str
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
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FirmwareOriVersion = None
        self._UpgradeMethod = None
        self._FileName = None
        self._FileMd5 = None
        self._FileSize = None
        self._DeviceNames = None
        self._TimeoutInterval = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件新版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareOriVersion(self):
        """固件原版本号，根据文件列表升级固件不需要填写此参数
        :rtype: str
        """
        return self._FirmwareOriVersion

    @FirmwareOriVersion.setter
    def FirmwareOriVersion(self, FirmwareOriVersion):
        self._FirmwareOriVersion = FirmwareOriVersion

    @property
    def UpgradeMethod(self):
        """升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式
        :rtype: int
        """
        return self._UpgradeMethod

    @UpgradeMethod.setter
    def UpgradeMethod(self, UpgradeMethod):
        self._UpgradeMethod = UpgradeMethod

    @property
    def FileName(self):
        """设备列表文件名称，根据文件列表升级固件需要填写此参数
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        """设备列表的文件md5值
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileSize(self):
        """设备列表的文件大小值
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DeviceNames(self):
        """需要升级的设备名称列表
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def TimeoutInterval(self):
        """固件升级任务，默认超时时间。 最小取值60秒，最大为3600秒
        :rtype: int
        """
        return self._TimeoutInterval

    @TimeoutInterval.setter
    def TimeoutInterval(self, TimeoutInterval):
        self._TimeoutInterval = TimeoutInterval


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareOriVersion = params.get("FirmwareOriVersion")
        self._UpgradeMethod = params.get("UpgradeMethod")
        self._FileName = params.get("FileName")
        self._FileMd5 = params.get("FileMd5")
        self._FileSize = params.get("FileSize")
        self._DeviceNames = params.get("DeviceNames")
        self._TimeoutInterval = params.get("TimeoutInterval")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BatchUpdateShadow(AbstractModel):
    """批量更新设备影子任务

    """

    def __init__(self):
        r"""
        :param _Desired: 设备影子的期望状态，格式为 Json 对象序列化之后的字符串
        :type Desired: str
        """
        self._Desired = None

    @property
    def Desired(self):
        """设备影子的期望状态，格式为 Json 对象序列化之后的字符串
        :rtype: str
        """
        return self._Desired

    @Desired.setter
    def Desired(self, Desired):
        self._Desired = Desired


    def _deserialize(self, params):
        self._Desired = params.get("Desired")
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
        """网关设备的产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        """网关设备的设备名
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        """被绑定设备的产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        """被绑定的多个设备名
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Skey(self):
        """中兴CLAA设备的绑定需要skey，普通的设备不需要
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名
        :rtype: str
        """
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
        :param _Devicename: 设备名称
        :type Devicename: str
        :param _Productid: 产品ID
        :type Productid: str
        :param _Requestid: 请求ID
        :type Requestid: str
        :param _Result: 结果
        :type Result: str
        :param _Scene: 模块
        :type Scene: str
        :param _Time: 日志时间
        :type Time: str
        :param _Userid: 腾讯云账号
        :type Userid: str
        """
        self._Content = None
        self._Devicename = None
        self._Productid = None
        self._Requestid = None
        self._Result = None
        self._Scene = None
        self._Time = None
        self._Userid = None

    @property
    def Content(self):
        """日志内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Devicename(self):
        """设备名称
        :rtype: str
        """
        return self._Devicename

    @Devicename.setter
    def Devicename(self, Devicename):
        self._Devicename = Devicename

    @property
    def Productid(self):
        """产品ID
        :rtype: str
        """
        return self._Productid

    @Productid.setter
    def Productid(self, Productid):
        self._Productid = Productid

    @property
    def Requestid(self):
        """请求ID
        :rtype: str
        """
        return self._Requestid

    @Requestid.setter
    def Requestid(self, Requestid):
        self._Requestid = Requestid

    @property
    def Result(self):
        """结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Scene(self):
        """模块
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Time(self):
        """日志时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Userid(self):
        """腾讯云账号
        :rtype: str
        """
        return self._Userid

    @Userid.setter
    def Userid(self, Userid):
        self._Userid = Userid


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Devicename = params.get("Devicename")
        self._Productid = params.get("Productid")
        self._Requestid = params.get("Requestid")
        self._Result = params.get("Result")
        self._Scene = params.get("Scene")
        self._Time = params.get("Time")
        self._Userid = params.get("Userid")
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        """固件升级任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 任务 ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """任务 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


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
        :type Attribute: :class:`tencentcloud.iotcloud.v20180614.models.Attribute`
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

    @property
    def ProductId(self):
        """产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Attribute(self):
        """设备属性
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.Attribute`
        """
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def DefinedPsk(self):
        """是否使用自定义PSK，默认不使用
        :rtype: str
        """
        return self._DefinedPsk

    @DefinedPsk.setter
    def DefinedPsk(self, DefinedPsk):
        self._DefinedPsk = DefinedPsk

    @property
    def Isp(self):
        """运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通
        :rtype: int
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Imei(self):
        """IMEI，当产品是NB-IoT产品时，此字段必填
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def LoraDevEui(self):
        """LoRa设备的DevEui，当创建LoRa时，此字段必填
        :rtype: str
        """
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        """LoRa设备的MoteType
        :rtype: int
        """
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def Skey(self):
        """创建LoRa设备需要skey
        :rtype: str
        """
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def LoraAppKey(self):
        """LoRa设备的AppKey
        :rtype: str
        """
        return self._LoraAppKey

    @LoraAppKey.setter
    def LoraAppKey(self, LoraAppKey):
        self._LoraAppKey = LoraAppKey


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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevicePsk(self):
        """对称加密密钥，base64编码。采用对称加密时返回该参数
        :rtype: str
        """
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def DeviceCert(self):
        """设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数
        :rtype: str
        """
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePrivateKey(self):
        """设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数
        :rtype: str
        """
        return self._DevicePrivateKey

    @DevicePrivateKey.setter
    def DevicePrivateKey(self, DevicePrivateKey):
        self._DevicePrivateKey = DevicePrivateKey

    @property
    def LoraDevEui(self):
        """LoRa设备的DevEui，当设备是LoRa设备时，会返回该字段
        :rtype: str
        """
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        """LoRa设备的MoteType，当设备是LoRa设备时，会返回该字段
        :rtype: int
        """
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def LoraAppKey(self):
        """LoRa设备的AppKey，当设备是LoRa设备时，会返回该字段
        :rtype: str
        """
        return self._LoraAppKey

    @LoraAppKey.setter
    def LoraAppKey(self, LoraAppKey):
        self._LoraAppKey = LoraAppKey

    @property
    def LoraNwkKey(self):
        """LoRa设备的NwkKey，当设备是LoRa设备时，会返回该字段
        :rtype: str
        """
        return self._LoraNwkKey

    @LoraNwkKey.setter
    def LoraNwkKey(self, LoraNwkKey):
        self._LoraNwkKey = LoraNwkKey

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class CreateLoraDeviceRequest(AbstractModel):
    """CreateLoraDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id ，创建产品时腾讯云为用户分配全局唯一的Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceType: 设备类型 ，目前支持A、B、C三种
        :type DeviceType: str
        :param _AppEui: LoRa应用UUID
        :type AppEui: str
        :param _DeviceEui: LoRa设备UUID
        :type DeviceEui: str
        :param _AppKey: LoRa应用密钥
        :type AppKey: str
        :param _AuthKey: LoRa设备验证密钥
        :type AuthKey: str
        :param _Memo: 设备备注
        :type Memo: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._DeviceType = None
        self._AppEui = None
        self._DeviceEui = None
        self._AppKey = None
        self._AuthKey = None
        self._Memo = None

    @property
    def ProductId(self):
        """产品Id ，创建产品时腾讯云为用户分配全局唯一的Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceType(self):
        """设备类型 ，目前支持A、B、C三种
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def AppEui(self):
        """LoRa应用UUID
        :rtype: str
        """
        return self._AppEui

    @AppEui.setter
    def AppEui(self, AppEui):
        self._AppEui = AppEui

    @property
    def DeviceEui(self):
        """LoRa设备UUID
        :rtype: str
        """
        return self._DeviceEui

    @DeviceEui.setter
    def DeviceEui(self, DeviceEui):
        self._DeviceEui = DeviceEui

    @property
    def AppKey(self):
        """LoRa应用密钥
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AuthKey(self):
        """LoRa设备验证密钥
        :rtype: str
        """
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey

    @property
    def Memo(self):
        """设备备注
        :rtype: str
        """
        return self._Memo

    @Memo.setter
    def Memo(self, Memo):
        self._Memo = Memo


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceType = params.get("DeviceType")
        self._AppEui = params.get("AppEui")
        self._DeviceEui = params.get("DeviceEui")
        self._AppKey = params.get("AppKey")
        self._AuthKey = params.get("AuthKey")
        self._Memo = params.get("Memo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoraDeviceResponse(AbstractModel):
    """CreateLoraDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppEui: LoRa应用UUID
        :type AppEui: str
        :param _DeviceEui: LoRa设备UUID
        :type DeviceEui: str
        :param _ClassType: 设备类型,目前支持A、B、C三种
        :type ClassType: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppEui = None
        self._DeviceEui = None
        self._ClassType = None
        self._DeviceName = None
        self._RequestId = None

    @property
    def AppEui(self):
        """LoRa应用UUID
        :rtype: str
        """
        return self._AppEui

    @AppEui.setter
    def AppEui(self, AppEui):
        self._AppEui = AppEui

    @property
    def DeviceEui(self):
        """LoRa设备UUID
        :rtype: str
        """
        return self._DeviceEui

    @DeviceEui.setter
    def DeviceEui(self, DeviceEui):
        self._DeviceEui = DeviceEui

    @property
    def ClassType(self):
        """设备类型,目前支持A、B、C三种
        :rtype: str
        """
        return self._ClassType

    @ClassType.setter
    def ClassType(self, ClassType):
        self._ClassType = ClassType

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppEui = params.get("AppEui")
        self._DeviceEui = params.get("DeviceEui")
        self._ClassType = params.get("ClassType")
        self._DeviceName = params.get("DeviceName")
        self._RequestId = params.get("RequestId")


class CreateMultiDeviceRequest(AbstractModel):
    """CreateMultiDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID。创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param _DeviceNames: 批量创建的设备名数组，单次最多创建 100 个设备。命名规则：[a-zA-Z0-9:_-]{1,48}
        :type DeviceNames: list of str
        """
        self._ProductId = None
        self._DeviceNames = None

    @property
    def ProductId(self):
        """产品 ID。创建产品时腾讯云为用户分配全局唯一的 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        """批量创建的设备名数组，单次最多创建 100 个设备。命名规则：[a-zA-Z0-9:_-]{1,48}
        :rtype: list of str
        """
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
        


class CreateMultiDeviceResponse(AbstractModel):
    """CreateMultiDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，腾讯云生成全局唯一的任务 ID，有效期一个月，一个月之后任务失效。可以调用获取创建多设备任务状态接口获取该任务的执行状态，当状态为成功时，可以调用获取创建多设备任务结果接口获取该任务的结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID，腾讯云生成全局唯一的任务 ID，有效期一个月，一个月之后任务失效。可以调用获取创建多设备任务状态接口获取该任务的执行状态，当状态为成功时，可以调用获取创建多设备任务结果接口获取该任务的结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParametersType(self):
        """参数类型 cosfile-文件上传 random-随机创建
        :rtype: str
        """
        return self._ParametersType

    @ParametersType.setter
    def ParametersType(self, ParametersType):
        self._ParametersType = ParametersType

    @property
    def FileName(self):
        """文件上传类型时文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """文件上传类型时文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def BatchCount(self):
        """随机创建时设备创建个数
        :rtype: int
        """
        return self._BatchCount

    @BatchCount.setter
    def BatchCount(self, BatchCount):
        self._BatchCount = BatchCount

    @property
    def Hash(self):
        """文件上传类型时文件md5值
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        :param _Skey: 创建CLAA产品时，需要Skey
        :type Skey: str
        """
        self._ProductName = None
        self._ProductProperties = None
        self._Skey = None

    @property
    def ProductName(self):
        """产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductProperties(self):
        """产品属性
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def Skey(self):
        """创建CLAA产品时，需要Skey
        :rtype: str
        """
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
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductName = None
        self._ProductId = None
        self._ProductProperties = None
        self._RequestId = None

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductId(self):
        """产品 ID，腾讯云生成全局唯一 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductProperties(self):
        """产品属性
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._FileName = None
        self._RequestId = None

    @property
    def Url(self):
        """任务文件上传链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileName(self):
        """任务文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileName = params.get("FileName")
        self._RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskType: 任务类型，取值为 “UpdateShadow” 或者 “PublishMessage”
        :type TaskType: str
        :param _ProductId: 执行任务的产品ID
        :type ProductId: str
        :param _DeviceNameFilter: 执行任务的设备名的正则表达式
        :type DeviceNameFilter: str
        :param _ScheduleTimeInSeconds: 任务开始执行的时间。 取值为 Unix 时间戳，单位秒，且需大于等于当前时间时间戳，0为系统当前时间时间戳，即立即执行，最大为当前时间86400秒后，超过则取值为当前时间86400秒后
        :type ScheduleTimeInSeconds: int
        :param _Tasks: 任务描述细节，描述见下 Task
        :type Tasks: :class:`tencentcloud.iotcloud.v20180614.models.Task`
        :param _MaxExecutionTimeInSeconds: 最长执行时间，单位秒，被调度后超过此时间仍未有结果则视为任务失败。取值为0-86400，默认为86400
        :type MaxExecutionTimeInSeconds: int
        """
        self._TaskType = None
        self._ProductId = None
        self._DeviceNameFilter = None
        self._ScheduleTimeInSeconds = None
        self._Tasks = None
        self._MaxExecutionTimeInSeconds = None

    @property
    def TaskType(self):
        """任务类型，取值为 “UpdateShadow” 或者 “PublishMessage”
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ProductId(self):
        """执行任务的产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNameFilter(self):
        """执行任务的设备名的正则表达式
        :rtype: str
        """
        return self._DeviceNameFilter

    @DeviceNameFilter.setter
    def DeviceNameFilter(self, DeviceNameFilter):
        self._DeviceNameFilter = DeviceNameFilter

    @property
    def ScheduleTimeInSeconds(self):
        """任务开始执行的时间。 取值为 Unix 时间戳，单位秒，且需大于等于当前时间时间戳，0为系统当前时间时间戳，即立即执行，最大为当前时间86400秒后，超过则取值为当前时间86400秒后
        :rtype: int
        """
        return self._ScheduleTimeInSeconds

    @ScheduleTimeInSeconds.setter
    def ScheduleTimeInSeconds(self, ScheduleTimeInSeconds):
        self._ScheduleTimeInSeconds = ScheduleTimeInSeconds

    @property
    def Tasks(self):
        """任务描述细节，描述见下 Task
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.Task`
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def MaxExecutionTimeInSeconds(self):
        """最长执行时间，单位秒，被调度后超过此时间仍未有结果则视为任务失败。取值为0-86400，默认为86400
        :rtype: int
        """
        return self._MaxExecutionTimeInSeconds

    @MaxExecutionTimeInSeconds.setter
    def MaxExecutionTimeInSeconds(self, MaxExecutionTimeInSeconds):
        self._MaxExecutionTimeInSeconds = MaxExecutionTimeInSeconds


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._ProductId = params.get("ProductId")
        self._DeviceNameFilter = params.get("DeviceNameFilter")
        self._ScheduleTimeInSeconds = params.get("ScheduleTimeInSeconds")
        if params.get("Tasks") is not None:
            self._Tasks = Task()
            self._Tasks._deserialize(params.get("Tasks"))
        self._MaxExecutionTimeInSeconds = params.get("MaxExecutionTimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 创建的任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """创建的任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品自身ID
        :type ProductID: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _Privilege: Topic权限，1发布，2订阅，3订阅和发布
        :type Privilege: int
        :param _BrokerSubscribe: 代理订阅信息，网关产品为绑定的子产品创建topic时需要填写，内容为子产品的ID和设备信息。
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        self._ProductID = None
        self._TopicName = None
        self._Privilege = None
        self._BrokerSubscribe = None

    @property
    def ProductID(self):
        """产品自身ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def TopicName(self):
        """Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Privilege(self):
        """Topic权限，1发布，2订阅，3订阅和发布
        :rtype: int
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def BrokerSubscribe(self):
        """代理订阅信息，网关产品为绑定的子产品创建topic时需要填写，内容为子产品的ID和设备信息。
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        return self._BrokerSubscribe

    @BrokerSubscribe.setter
    def BrokerSubscribe(self, BrokerSubscribe):
        self._BrokerSubscribe = BrokerSubscribe


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`
        """
        self._RuleName = None
        self._TopicRulePayload = None

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def TopicRulePayload(self):
        """规则内容
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """设备所属的产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """需要删除的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Skey(self):
        """删除LoRa设备以及LoRa网关设备需要skey
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoraDeviceRequest(AbstractModel):
    """DeleteLoraDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 设备所属产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        """设备所属产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
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
        


class DeleteLoraDeviceResponse(AbstractModel):
    """DeleteLoraDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """需要删除的产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Skey(self):
        """删除LoRa产品需要skey
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """规则名
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAllDevicesRequest(AbstractModel):
    """DescribeAllDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询偏移量。
        :type Offset: int
        :param _Limit: 查询设备数量。最大支持250个
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """查询偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询设备数量。最大支持250个
        :rtype: int
        """
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
        


class DescribeAllDevicesResponse(AbstractModel):
    """DescribeAllDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 设备总数。
        :type TotalCount: int
        :param _Devices: 查询的设备列表信息。
        :type Devices: list of DeviceProperty
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """设备总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        """查询的设备列表信息。
        :rtype: list of DeviceProperty
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceProperty()
                obj._deserialize(item)
                self._Devices.append(obj)
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
        """所属产品的Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientKey = None
        self._RequestId = None

    @property
    def ClientKey(self):
        """设备的私钥
        :rtype: str
        """
        return self._ClientKey

    @ClientKey.setter
    def ClientKey(self, ClientKey):
        self._ClientKey = ClientKey

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        """
        self._ProductID = None
        self._DeviceName = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """具体的设备资源名称
        :rtype: str
        """
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
        :type Result: :class:`tencentcloud.iotcloud.v20180614.models.DeviceResourceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备资源详情
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.DeviceResourceInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """偏移量，Offset从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页的大小，数值范围 10-250
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        """需要过滤的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def StartTime(self):
        """资源搜索开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """资源搜索结束时间
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Result = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """资源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Result(self):
        """资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceResourceInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _Online: 设备是否在线，0不在线，1在线
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = None

    @property
    def DeviceName(self):
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        """设备是否在线，0不在线，1在线
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        """设备登录时间
        :rtype: int
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Version(self):
        """设备固件版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastUpdateTime(self):
        """设备最后更新时间
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def DeviceCert(self):
        """设备证书
        :rtype: str
        """
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePsk(self):
        """设备密钥
        :rtype: str
        """
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def Tags(self):
        """设备属性
        :rtype: list of DeviceTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        """设备类型
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Imei(self):
        """国际移动设备识别码 IMEI
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Isp(self):
        """运营商类型
        :rtype: int
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def ConnIP(self):
        """IP地址
        :rtype: int
        """
        return self._ConnIP

    @ConnIP.setter
    def ConnIP(self, ConnIP):
        self._ConnIP = ConnIP

    @property
    def NbiotDeviceID(self):
        """NB IoT运营商处的DeviceID
        :rtype: str
        """
        return self._NbiotDeviceID

    @NbiotDeviceID.setter
    def NbiotDeviceID(self, NbiotDeviceID):
        self._NbiotDeviceID = NbiotDeviceID

    @property
    def LoraDevEui(self):
        """Lora设备的dev eui
        :rtype: str
        """
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        """Lora设备的mote type
        :rtype: int
        """
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def LogLevel(self):
        """设备的sdk日志等级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def FirstOnlineTime(self):
        """首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LastOfflineTime(self):
        """最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastOfflineTime

    @LastOfflineTime.setter
    def LastOfflineTime(self, LastOfflineTime):
        self._LastOfflineTime = LastOfflineTime

    @property
    def CreateTime(self):
        """设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CertState(self):
        """设备证书获取状态，0 未获取过设备密钥, 1 已获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState

    @property
    def EnableState(self):
        """设备启用状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def Labels(self):
        """设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def ClientIP(self):
        """MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def FirmwareUpdateTime(self):
        """设备固件更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirmwareUpdateTime

    @FirmwareUpdateTime.setter
    def FirmwareUpdateTime(self, FirmwareUpdateTime):
        self._FirmwareUpdateTime = FirmwareUpdateTime

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        self._RequestId = params.get("RequestId")


class DescribeDeviceShadowRequest(AbstractModel):
    """DescribeDeviceShadow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        """产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备影子数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """需要查看设备列表的产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        """偏移量，Offset从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页的大小，数值范围 10-250
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FirmwareVersion(self):
        """设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def DeviceName(self):
        """需要过滤的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EnableState(self):
        """设备是否启用，0禁用状态1启用状态，默认不区分
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """设备总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        """设备详细信息列表
        :rtype: list of DeviceInfo
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = None

    @property
    def Version(self):
        """固件版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Name(self):
        """固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Md5sum(self):
        """固件Md5值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def Createtime(self):
        """固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def FwType(self):
        """固件类型。选项：mcu、module
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskDevicesRequest(AbstractModel):
    """DescribeFirmwareTaskDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param _Filters: 筛选条件
        :type Filters: list of SearchKeyword
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询的数量
        :type Limit: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Filters(self):
        """筛选条件
        :rtype: list of SearchKeyword
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询的数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Devices = None
        self._RequestId = None

    @property
    def Total(self):
        """固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Devices(self):
        """固件升级任务的设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceUpdateStatus
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        """固件升级任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatusInfos = None
        self._RequestId = None

    @property
    def StatusInfos(self):
        """固件升级任务状态分布信息
        :rtype: list of StatusStatistic
        """
        return self._StatusInfos

    @StatusInfos.setter
    def StatusInfos(self, StatusInfos):
        self._StatusInfos = StatusInfos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        """固件任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._CreateTime = None
        self._Type = None
        self._ProductName = None
        self._UpgradeMode = None
        self._ProductId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """固件任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """固件任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """固件任务创建时间，单位:秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Type(self):
        """固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProductName(self):
        """产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def UpgradeMode(self):
        """固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def ProductId(self):
        """产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessTotal = None
        self._FailureTotal = None
        self._UpgradingTotal = None
        self._RequestId = None

    @property
    def SuccessTotal(self):
        """升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessTotal

    @SuccessTotal.setter
    def SuccessTotal(self, SuccessTotal):
        self._SuccessTotal = SuccessTotal

    @property
    def FailureTotal(self):
        """升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailureTotal

    @FailureTotal.setter
    def FailureTotal(self, FailureTotal):
        self._FailureTotal = FailureTotal

    @property
    def UpgradingTotal(self):
        """正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpgradingTotal

    @UpgradingTotal.setter
    def UpgradingTotal(self, UpgradingTotal):
        self._UpgradingTotal = UpgradingTotal

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 返回查询结果条数
        :type Limit: int
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Offset(self):
        """查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回查询结果条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """搜索过滤条件
        :rtype: list of SearchKeyword
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfos = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskInfos(self):
        """固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FirmwareTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def Total(self):
        """固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeLoraDeviceRequest(AbstractModel):
    """DescribeLoraDevice请求参数结构体

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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
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
        


class DescribeLoraDeviceResponse(AbstractModel):
    """DescribeLoraDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _AppEui: LoRa应用UUID
        :type AppEui: str
        :param _DeviceEui: LoRa设备UUID
        :type DeviceEui: str
        :param _AppKey: LoRa应用密钥
        :type AppKey: str
        :param _ClassType: 设备类型,目前支持A、B、C三种
        :type ClassType: str
        :param _ProductId: 设备所属产品id
        :type ProductId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceName = None
        self._AppEui = None
        self._DeviceEui = None
        self._AppKey = None
        self._ClassType = None
        self._ProductId = None
        self._RequestId = None

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AppEui(self):
        """LoRa应用UUID
        :rtype: str
        """
        return self._AppEui

    @AppEui.setter
    def AppEui(self, AppEui):
        self._AppEui = AppEui

    @property
    def DeviceEui(self):
        """LoRa设备UUID
        :rtype: str
        """
        return self._DeviceEui

    @DeviceEui.setter
    def DeviceEui(self, DeviceEui):
        self._DeviceEui = DeviceEui

    @property
    def AppKey(self):
        """LoRa应用密钥
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def ClassType(self):
        """设备类型,目前支持A、B、C三种
        :rtype: str
        """
        return self._ClassType

    @ClassType.setter
    def ClassType(self, ClassType):
        self._ClassType = ClassType

    @property
    def ProductId(self):
        """设备所属产品id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._AppEui = params.get("AppEui")
        self._DeviceEui = params.get("DeviceEui")
        self._AppKey = params.get("AppKey")
        self._ClassType = params.get("ClassType")
        self._ProductId = params.get("ProductId")
        self._RequestId = params.get("RequestId")


class DescribeMultiDevTaskRequest(AbstractModel):
    """DescribeMultiDevTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID，由批量创建设备接口返回
        :type TaskId: str
        :param _ProductId: 产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        """
        self._TaskId = None
        self._ProductId = None

    @property
    def TaskId(self):
        """任务 ID，由批量创建设备接口返回
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProductId(self):
        """产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMultiDevTaskResponse(AbstractModel):
    """DescribeMultiDevTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _TaskStatus: 任务是否完成。0 代表任务未开始，1 代表任务正在执行，2 代表任务已完成
        :type TaskStatus: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskStatus = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskStatus(self):
        """任务是否完成。0 代表任务未开始，1 代表任务正在执行，2 代表任务已完成
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._RequestId = params.get("RequestId")


class DescribeMultiDevicesRequest(AbstractModel):
    """DescribeMultiDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param _TaskId: 任务 ID，由批量创建设备接口返回
        :type TaskId: str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页大小，每页返回的设备个数
        :type Limit: int
        """
        self._ProductId = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductId(self):
        """产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TaskId(self):
        """任务 ID，由批量创建设备接口返回
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，每页返回的设备个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMultiDevicesResponse(AbstractModel):
    """DescribeMultiDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID，由批量创建设备接口返回
        :type TaskId: str
        :param _DevicesInfo: 设备详细信息列表
        :type DevicesInfo: list of MultiDevicesInfo
        :param _TotalDevNum: 该任务创建设备的总数
        :type TotalDevNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._DevicesInfo = None
        self._TotalDevNum = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务 ID，由批量创建设备接口返回
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DevicesInfo(self):
        """设备详细信息列表
        :rtype: list of MultiDevicesInfo
        """
        return self._DevicesInfo

    @DevicesInfo.setter
    def DevicesInfo(self, DevicesInfo):
        self._DevicesInfo = DevicesInfo

    @property
    def TotalDevNum(self):
        """该任务创建设备的总数
        :rtype: int
        """
        return self._TotalDevNum

    @TotalDevNum.setter
    def TotalDevNum(self, TotalDevNum):
        self._TotalDevNum = TotalDevNum

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("DevicesInfo") is not None:
            self._DevicesInfo = []
            for item in params.get("DevicesInfo"):
                obj = MultiDevicesInfo()
                obj._deserialize(item)
                self._DevicesInfo.append(obj)
        self._TotalDevNum = params.get("TotalDevNum")
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
        """产品ID
        :rtype: str
        """
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
        """需要查看资源列表的产品 ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """需要过滤的资源名称
        :rtype: str
        """
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
        :type Result: :class:`tencentcloud.iotcloud.v20180614.models.ProductResourceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """资源详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductResourceInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """偏移量，Offset从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页的大小，数值范围 10-250
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductID(self):
        """需要查看资源列表的产品 ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """需要过滤的资源名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Result = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """资源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Result(self):
        """资源详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProductResourceInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20180614.models.ProductMetadata`
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductMetadata = None
        self._ProductProperties = None
        self._RequestId = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductMetadata(self):
        """产品元数据
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductMetadata`
        """
        return self._ProductMetadata

    @ProductMetadata.setter
    def ProductMetadata(self, ProductMetadata):
        self._ProductMetadata = ProductMetadata

    @property
    def ProductProperties(self):
        """产品属性
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
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
        :type TaskInfo: :class:`tencentcloud.iotcloud.v20180614.models.ProductTaskInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfo = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        """产品任务详细信息
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductTaskInfo`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        """产品级别任务列表偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """产品级别任务列表拉取个数
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的任务总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInfos(self):
        """任务详细信息列表
        :rtype: list of ProductTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """偏移量，Offset从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，当前页面中显示的最大数量，值范围 10-250。
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Products = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """产品总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Products(self):
        """产品详细信息列表
        :rtype: list of ProductInfo
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessTotal = None
        self._FailureTotal = None
        self._UpgradingTotal = None
        self._RequestId = None

    @property
    def SuccessTotal(self):
        """推送成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessTotal

    @SuccessTotal.setter
    def SuccessTotal(self, SuccessTotal):
        self._SuccessTotal = SuccessTotal

    @property
    def FailureTotal(self):
        """推送失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailureTotal

    @FailureTotal.setter
    def FailureTotal(self, FailureTotal):
        self._FailureTotal = FailureTotal

    @property
    def UpgradingTotal(self):
        """正在推送的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpgradingTotal

    @UpgradingTotal.setter
    def UpgradingTotal(self, UpgradingTotal):
        self._UpgradingTotal = UpgradingTotal

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回查询结果条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """搜索过滤条件
        :rtype: list of SearchKeyword
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfos = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskInfos(self):
        """资源任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FirmwareTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def Total(self):
        """资源任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """任务ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”
        :type Type: str
        :param _Id: 任务 ID
        :type Id: str
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _Status: 状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消
        :type Status: int
        :param _CreateTime: 任务创建时间，Unix 时间戳
        :type CreateTime: int
        :param _UpdateTime: 最后任务更新时间，Unix 时间戳
        :type UpdateTime: int
        :param _DoneTime: 任务完成时间，Unix 时间戳
        :type DoneTime: int
        :param _ScheduleTime: 被调度时间，Unix 时间戳
        :type ScheduleTime: int
        :param _RetCode: 返回的错误码
        :type RetCode: int
        :param _ErrMsg: 返回的错误信息
        :type ErrMsg: str
        :param _Percent: 完成任务的设备比例
        :type Percent: int
        :param _AllDeviceCnt: 匹配到的需执行任务的设备数目
        :type AllDeviceCnt: int
        :param _DoneDeviceCnt: 已完成任务的设备数目
        :type DoneDeviceCnt: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Type = None
        self._Id = None
        self._ProductId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DoneTime = None
        self._ScheduleTime = None
        self._RetCode = None
        self._ErrMsg = None
        self._Percent = None
        self._AllDeviceCnt = None
        self._DoneDeviceCnt = None
        self._RequestId = None

    @property
    def Type(self):
        """任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """任务 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProductId(self):
        """产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        """状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """任务创建时间，Unix 时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后任务更新时间，Unix 时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DoneTime(self):
        """任务完成时间，Unix 时间戳
        :rtype: int
        """
        return self._DoneTime

    @DoneTime.setter
    def DoneTime(self, DoneTime):
        self._DoneTime = DoneTime

    @property
    def ScheduleTime(self):
        """被调度时间，Unix 时间戳
        :rtype: int
        """
        return self._ScheduleTime

    @ScheduleTime.setter
    def ScheduleTime(self, ScheduleTime):
        self._ScheduleTime = ScheduleTime

    @property
    def RetCode(self):
        """返回的错误码
        :rtype: int
        """
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def ErrMsg(self):
        """返回的错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Percent(self):
        """完成任务的设备比例
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def AllDeviceCnt(self):
        """匹配到的需执行任务的设备数目
        :rtype: int
        """
        return self._AllDeviceCnt

    @AllDeviceCnt.setter
    def AllDeviceCnt(self, AllDeviceCnt):
        self._AllDeviceCnt = AllDeviceCnt

    @property
    def DoneDeviceCnt(self):
        """已完成任务的设备数目
        :rtype: int
        """
        return self._DoneDeviceCnt

    @DoneDeviceCnt.setter
    def DoneDeviceCnt(self, DoneDeviceCnt):
        self._DoneDeviceCnt = DoneDeviceCnt

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DoneTime = params.get("DoneTime")
        self._ScheduleTime = params.get("ScheduleTime")
        self._RetCode = params.get("RetCode")
        self._ErrMsg = params.get("ErrMsg")
        self._Percent = params.get("Percent")
        self._AllDeviceCnt = params.get("AllDeviceCnt")
        self._DoneDeviceCnt = params.get("DoneDeviceCnt")
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页的大小，数值范围 1-250
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页的大小，数值范围 1-250
        :rtype: int
        """
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
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 用户一个月内创建的任务总数
        :type TotalCount: int
        :param _Tasks: 此页任务对象的数组，按创建时间排序
        :type Tasks: list of TaskInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """用户一个月内创建的任务总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """此页任务对象的数组，按创建时间排序
        :rtype: list of TaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
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

    @property
    def DeviceName(self):
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        """设备是否在线，0不在线，1在线
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        """设备登录时间
        :rtype: int
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Version(self):
        """设备版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def DeviceCert(self):
        """设备证书，证书加密的设备返回
        :rtype: str
        """
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePsk(self):
        """设备密钥，密钥加密的设备返回
        :rtype: str
        """
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def Tags(self):
        """设备属性
        :rtype: list of DeviceTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        """设备类型
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Imei(self):
        """国际移动设备识别码 IMEI
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Isp(self):
        """运营商类型
        :rtype: int
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def NbiotDeviceID(self):
        """NB IOT运营商处的DeviceID
        :rtype: str
        """
        return self._NbiotDeviceID

    @NbiotDeviceID.setter
    def NbiotDeviceID(self, NbiotDeviceID):
        self._NbiotDeviceID = NbiotDeviceID

    @property
    def ConnIP(self):
        """IP地址
        :rtype: int
        """
        return self._ConnIP

    @ConnIP.setter
    def ConnIP(self, ConnIP):
        self._ConnIP = ConnIP

    @property
    def LastUpdateTime(self):
        """设备最后更新时间
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def LoraDevEui(self):
        """LoRa设备的dev eui
        :rtype: str
        """
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        """LoRa设备的Mote type
        :rtype: int
        """
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def FirstOnlineTime(self):
        """首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LastOfflineTime(self):
        """最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastOfflineTime

    @LastOfflineTime.setter
    def LastOfflineTime(self, LastOfflineTime):
        self._LastOfflineTime = LastOfflineTime

    @property
    def CreateTime(self):
        """设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LogLevel(self):
        """设备日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def CertState(self):
        """设备证书获取状态, 1 已获取过设备密钥，0 未获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState

    @property
    def EnableState(self):
        """设备可用状态，0禁用，1启用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def Labels(self):
        """设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def ClientIP(self):
        """MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def FirmwareUpdateTime(self):
        """ota最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirmwareUpdateTime

    @FirmwareUpdateTime.setter
    def FirmwareUpdateTime(self, FirmwareUpdateTime):
        self._FirmwareUpdateTime = FirmwareUpdateTime


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
        """标签标识
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
        :rtype: str
        """
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
        


class DeviceProperty(AbstractModel):
    """设备资源信息。

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _ProductName: 产品名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _DeviceName: 设备名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ResourceId: 设备资源ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        """
        self._ProductId = None
        self._ProductName = None
        self._DeviceName = None
        self._ResourceId = None

    @property
    def ProductId(self):
        """产品ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def DeviceName(self):
        """设备名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ResourceId(self):
        """设备资源ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._DeviceName = params.get("DeviceName")
        self._ResourceId = params.get("ResourceId")
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
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def ProductName(self):
        """产品名
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Md5(self):
        """资源文件md5
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Size(self):
        """资源文件大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def UpdateTime(self):
        """资源更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Status(self):
        """设备资源上传状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        """设备资源上传百分比
        :rtype: int
        """
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
        """属性名称
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Type(self):
        """属性值的类型，1 int，2 string
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """属性的值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        """属性描述名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LastProcessTime(self):
        """最后处理时间
        :rtype: int
        """
        return self._LastProcessTime

    @LastProcessTime.setter
    def LastProcessTime(self, LastProcessTime):
        self._LastProcessTime = LastProcessTime

    @property
    def Status(self):
        """状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        """错误消息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Retcode(self):
        """返回码
        :rtype: int
        """
        return self._Retcode

    @Retcode.setter
    def Retcode(self, Retcode):
        self._Retcode = Retcode

    @property
    def DstVersion(self):
        """目标更新版本
        :rtype: str
        """
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def Percent(self):
        """下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def OriVersion(self):
        """原版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriVersion

    @OriVersion.setter
    def OriVersion(self, OriVersion):
        self._OriVersion = OriVersion

    @property
    def TaskId(self):
        """任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
        """规则名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        """设备资源的cos链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID。
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号。
        :type FirmwareVersion: str
        :param _FirmwareName: 固件名称。
        :type FirmwareName: str
        :param _FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        :param _FwType: 固件类型：选填 mcu、moudule。默认：mcu
        :type FwType: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FirmwareName = None
        self._FirmwareDescription = None
        self._FwType = None

    @property
    def ProductID(self):
        """产品ID。
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号。
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareName(self):
        """固件名称。
        :rtype: str
        """
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        """固件描述
        :rtype: str
        """
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription

    @property
    def FwType(self):
        """固件类型：选填 mcu、moudule。默认：mcu
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        self._FwType = params.get("FwType")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """规则名称
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


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
        """任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        """任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
        


class GetCOSURLRequest(AbstractModel):
    """GetCOSURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        """固件URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsedSize = None
        self._Limit = None
        self._RequestId = None

    @property
    def UsedSize(self):
        """已使用的资源字节数
        :rtype: int
        """
        return self._UsedSize

    @UsedSize.setter
    def UsedSize(self, UsedSize):
        self._UsedSize = UsedSize

    @property
    def Limit(self):
        """可以使用资源的总大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UsedSize = params.get("UsedSize")
        self._Limit = params.get("Limit")
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
        """日志开始时间，毫秒级时间戳
        :rtype: int
        """
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        """日志结束时间，毫秒级时间戳
        :rtype: int
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        """查询关键字，可以同时支持键值查询和文本查询，例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。键值或文本可以包含多个，以空格隔开。其中可以索引的key比如：RequestID、ProductID、DeviceName等。
一个典型的查询示例：ProductID:ABCDE12345 DeviceName:test publish
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        """日志检索上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        """日志最大条数
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._RequestId = None

    @property
    def Context(self):
        """日志上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        """是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        """日志列表
        :rtype: list of PayloadLogItem
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """日志开始时间，毫秒级时间戳
        :rtype: int
        """
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        """日志结束时间，毫秒级时间戳
        :rtype: int
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        """查询关键字，可以同时支持键值查询和文本查询，例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。键值或文本可以包含多个，以空格隔开。其中可以索引的key包括：requestid、productid、devicename、scene、content。
一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW content:Device%20connect publish
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        """日志检索上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        """查询条数
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Context(self):
        """日志上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        """是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        """日志列表
        :rtype: list of CLSLogItem
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def TotalCount(self):
        """日志总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """日志开始时间
        :rtype: int
        """
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        """日志结束时间
        :rtype: int
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        """查询关键字，可以同时支持键值查询和文本查询，
例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。
键值或文本可以包含多个，以空格隔开。
其中可以索引的key包括：productid、devicename、loglevel
一个典型的查询示例：productid:7JK1G72JNE devicename:name publish loglevel:WARN一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW publish
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        """日志检索上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        """查询条数
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._RequestId = None

    @property
    def Context(self):
        """日志检索上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        """是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        """日志列表
        :rtype: list of SDKLogItem
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class MultiDevicesInfo(AbstractModel):
    """创建设备时返回的设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _DevicePsk: 对称加密密钥，base64 编码，采用对称加密时返回该参数
        :type DevicePsk: str
        :param _DeviceCert: 设备证书，采用非对称加密时返回该参数
        :type DeviceCert: str
        :param _DevicePrivateKey: 设备私钥，采用非对称加密时返回该参数，腾讯云为用户缓存起来，其生命周期与任务生命周期一致
        :type DevicePrivateKey: str
        :param _Result: 错误码
        :type Result: int
        :param _ErrMsg: 错误信息
        :type ErrMsg: str
        """
        self._DeviceName = None
        self._DevicePsk = None
        self._DeviceCert = None
        self._DevicePrivateKey = None
        self._Result = None
        self._ErrMsg = None

    @property
    def DeviceName(self):
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevicePsk(self):
        """对称加密密钥，base64 编码，采用对称加密时返回该参数
        :rtype: str
        """
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def DeviceCert(self):
        """设备证书，采用非对称加密时返回该参数
        :rtype: str
        """
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePrivateKey(self):
        """设备私钥，采用非对称加密时返回该参数，腾讯云为用户缓存起来，其生命周期与任务生命周期一致
        :rtype: str
        """
        return self._DevicePrivateKey

    @DevicePrivateKey.setter
    def DevicePrivateKey(self, DevicePrivateKey):
        self._DevicePrivateKey = DevicePrivateKey

    @property
    def Result(self):
        """错误码
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._DevicePsk = params.get("DevicePsk")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePrivateKey = params.get("DevicePrivateKey")
        self._Result = params.get("Result")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayloadLogItem(AbstractModel):
    """内容日志项

    """

    def __init__(self):
        r"""
        :param _Uin: 账号id
        :type Uin: str
        :param _ProductID: 产品id
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _SrcType: 来源类型
        :type SrcType: str
        :param _SrcName: 来源名称
        :type SrcName: str
        :param _Topic: 消息topic
        :type Topic: str
        :param _PayloadFmtType: 内容格式类型
        :type PayloadFmtType: str
        :param _Payload: 内容信息
        :type Payload: str
        :param _RequestID: 请求ID
        :type RequestID: str
        :param _DateTime: 日期时间
        :type DateTime: str
        """
        self._Uin = None
        self._ProductID = None
        self._DeviceName = None
        self._SrcType = None
        self._SrcName = None
        self._Topic = None
        self._PayloadFmtType = None
        self._Payload = None
        self._RequestID = None
        self._DateTime = None

    @property
    def Uin(self):
        """账号id
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProductID(self):
        """产品id
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def SrcType(self):
        """来源类型
        :rtype: str
        """
        return self._SrcType

    @SrcType.setter
    def SrcType(self, SrcType):
        self._SrcType = SrcType

    @property
    def SrcName(self):
        """来源名称
        :rtype: str
        """
        return self._SrcName

    @SrcName.setter
    def SrcName(self, SrcName):
        self._SrcName = SrcName

    @property
    def Topic(self):
        """消息topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def PayloadFmtType(self):
        """内容格式类型
        :rtype: str
        """
        return self._PayloadFmtType

    @PayloadFmtType.setter
    def PayloadFmtType(self, PayloadFmtType):
        self._PayloadFmtType = PayloadFmtType

    @property
    def Payload(self):
        """内容信息
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def RequestID(self):
        """请求ID
        :rtype: str
        """
        return self._RequestID

    @RequestID.setter
    def RequestID(self, RequestID):
        self._RequestID = RequestID

    @property
    def DateTime(self):
        """日期时间
        :rtype: str
        """
        return self._DateTime

    @DateTime.setter
    def DateTime(self, DateTime):
        self._DateTime = DateTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._SrcType = params.get("SrcType")
        self._SrcName = params.get("SrcName")
        self._Topic = params.get("Topic")
        self._PayloadFmtType = params.get("PayloadFmtType")
        self._Payload = params.get("Payload")
        self._RequestID = params.get("RequestID")
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
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20180614.models.ProductMetadata`
        :param _ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductMetadata = None
        self._ProductProperties = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductMetadata(self):
        """产品元数据
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductMetadata`
        """
        return self._ProductMetadata

    @ProductMetadata.setter
    def ProductMetadata(self, ProductMetadata):
        self._ProductMetadata = ProductMetadata

    @property
    def ProductProperties(self):
        """产品属性
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
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
        """
        self._CreationDate = None

    @property
    def CreationDate(self):
        """产品创建时间
        :rtype: int
        """
        return self._CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self._CreationDate = CreationDate


    def _deserialize(self, params):
        self._CreationDate = params.get("CreationDate")
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
        :param _ProductSecret: 动态注册产品秘钥
        :type ProductSecret: str
        :param _RegisterLimit: RegisterType为2时，设备动态创建的限制数量
        :type RegisterLimit: int
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

    @property
    def ProductDescription(self):
        """产品描述
        :rtype: str
        """
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def EncryptionType(self):
        """加密类型，1表示证书认证，2表示签名认证。如不填写，默认值是1
        :rtype: str
        """
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def Region(self):
        """产品所属区域，目前只支持广州（gz）
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductType(self):
        """产品类型，各个类型值代表的节点-类型如下：
0 普通产品，2 NB-IoT产品，4 LoRa产品，3 LoRa网关产品，5 普通网关产品   默认值是0
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Format(self):
        """数据格式，取值为json或者custom，默认值是json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Platform(self):
        """产品所属平台，默认值是0
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Appeui(self):
        """LoRa产品运营侧APPEUI，只有LoRa产品需要填写
        :rtype: str
        """
        return self._Appeui

    @Appeui.setter
    def Appeui(self, Appeui):
        self._Appeui = Appeui

    @property
    def ModelId(self):
        """产品绑定的物模型ID，-1表示不绑定
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        """产品绑定的物模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ProductKey(self):
        """产品密钥，suite产品才会有
        :rtype: str
        """
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def RegisterType(self):
        """动态注册类型 0-关闭, 1-预定义设备名 2-动态定义设备名
        :rtype: int
        """
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        """动态注册产品秘钥
        :rtype: str
        """
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        """RegisterType为2时，设备动态创建的限制数量
        :rtype: int
        """
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit


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
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def ProductName(self):
        """产品名
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Md5(self):
        """资源文件md5
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Size(self):
        """资源文件大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Description(self):
        """资源文件描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """资源创建时间
        :rtype: str
        """
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
        """任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """任务类型 0-批量创建设备类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def State(self):
        """任务状态 0-创建中 1-待执行 2-执行中 3-执行失败 4-子任务部分失败 5-执行成功
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ParametersType(self):
        """任务参数类型 cosfile-文件输入 random-随机生成
        :rtype: str
        """
        return self._ParametersType

    @ParametersType.setter
    def ParametersType(self, ParametersType):
        self._ParametersType = ParametersType

    @property
    def Parameters(self):
        """任务参数
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def ResultType(self):
        """任务执行结果类型 cosfile-文件输出 errmsg-错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Result(self):
        """任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def BatchCount(self):
        """子任务总个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BatchCount

    @BatchCount.setter
    def BatchCount(self, BatchCount):
        self._BatchCount = BatchCount

    @property
    def BatchOffset(self):
        """子任务已执行个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BatchOffset

    @BatchOffset.setter
    def BatchOffset(self, BatchOffset):
        self._BatchOffset = BatchOffset

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """任务更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CompleteTime(self):
        """任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
        


class PublishAsDeviceRequest(AbstractModel):
    """PublishAsDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Port: LoRa 设备端口
        :type Port: int
        :param _Payload: 消息内容
        :type Payload: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Port = None
        self._Payload = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Port(self):
        """LoRa 设备端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Payload(self):
        """消息内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Port = params.get("Port")
        self._Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishAsDeviceResponse(AbstractModel):
    """PublishAsDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Payload(self):
        """消息内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Qos(self):
        """消息质量等级
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        """Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """广播消息任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """消息发往的主题。命名规则：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        """消息内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Qos(self):
        """服务质量等级，取值为0或1
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        """Payload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Payload(self):
        """消息内容，utf8编码
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._PayloadBase64 = None
        self._RequestId = None

    @property
    def MessageId(self):
        """RRPC消息ID
        :rtype: int
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def PayloadBase64(self):
        """设备回复的消息内容，采用base64编码
        :rtype: str
        """
        return self._PayloadBase64

    @PayloadBase64.setter
    def PayloadBase64(self, PayloadBase64):
        self._PayloadBase64 = PayloadBase64

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._PayloadBase64 = params.get("PayloadBase64")
        self._RequestId = params.get("RequestId")


class PublishToDeviceRequest(AbstractModel):
    """PublishToDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Port: LoRa 端口
        :type Port: int
        :param _Payload: 消息内容
        :type Payload: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Port = None
        self._Payload = None

    @property
    def ProductId(self):
        """产品id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Port(self):
        """LoRa 端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Payload(self):
        """消息内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Port = params.get("Port")
        self._Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishToDeviceResponse(AbstractModel):
    """PublishToDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplaceTopicRuleRequest(AbstractModel):
    """ReplaceTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _TopicRulePayload: 替换的规则包体
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`
        :param _ModifyType: 修改类型，0：其他，1：创建行为，2：更新行为，3：删除行为
        :type ModifyType: int
        :param _ActionIndex: action增删改变更填对应topicRulePayload里面第几个action
        :type ActionIndex: int
        """
        self._RuleName = None
        self._TopicRulePayload = None
        self._ModifyType = None
        self._ActionIndex = None

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def TopicRulePayload(self):
        """替换的规则包体
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`
        """
        return self._TopicRulePayload

    @TopicRulePayload.setter
    def TopicRulePayload(self, TopicRulePayload):
        self._TopicRulePayload = TopicRulePayload

    @property
    def ModifyType(self):
        """修改类型，0：其他，1：创建行为，2：更新行为，3：删除行为
        :rtype: int
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ActionIndex(self):
        """action增删改变更填对应topicRulePayload里面第几个action
        :rtype: int
        """
        return self._ActionIndex

    @ActionIndex.setter
    def ActionIndex(self, ActionIndex):
        self._ActionIndex = ActionIndex


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self._TopicRulePayload = TopicRulePayload()
            self._TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        self._ModifyType = params.get("ModifyType")
        self._ActionIndex = params.get("ActionIndex")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Success(self):
        """是否成功
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Reason(self):
        """失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        """设备名称
        :rtype: list of str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessCount = None
        self._ResetDeviceResults = None
        self._RequestId = None

    @property
    def SuccessCount(self):
        """批量重置设备成功数
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def ResetDeviceResults(self):
        """批量重置设备结果
        :rtype: list of ResetDeviceResult
        """
        return self._ResetDeviceResults

    @ResetDeviceResults.setter
    def ResetDeviceResults(self, ResetDeviceResults):
        self._ResetDeviceResults = ResetDeviceResults

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        """固件升级任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Level: 日志等级
        :type Level: str
        :param _DateTime: 日志时间
        :type DateTime: str
        :param _Content: 日志内容
        :type Content: str
        """
        self._ProductID = None
        self._DeviceName = None
        self._Level = None
        self._DateTime = None
        self._Content = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Level(self):
        """日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def DateTime(self):
        """日志时间
        :rtype: str
        """
        return self._DateTime

    @DateTime.setter
    def DateTime(self, DateTime):
        self._DateTime = DateTime

    @property
    def Content(self):
        """日志内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        """搜索条件的Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """搜索条件的值
        :rtype: str
        """
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
        :param _ProductID: 要设置禁用状态的产品列表
        :type ProductID: list of str
        :param _Status: 0启用，1禁用
        :type Status: int
        """
        self._ProductID = None
        self._Status = None

    @property
    def ProductID(self):
        """要设置禁用状态的产品列表
        :rtype: list of str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Status(self):
        """0启用，1禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Total(self):
        """统计总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
        


class Task(AbstractModel):
    """任务描述细节

    """

    def __init__(self):
        r"""
        :param _UpdateShadowTask: 批量更新影子任务的描述细节，当 taskType 取值为 “UpdateShadow” 时，此字段必填。描述见下 BatchUpdateShadow
        :type UpdateShadowTask: :class:`tencentcloud.iotcloud.v20180614.models.BatchUpdateShadow`
        :param _PublishMessageTask: 批量下发消息任务的描述细节，当 taskType 取值为 “PublishMessage” 时，此字段必填。描述见下 BatchPublishMessage
        :type PublishMessageTask: :class:`tencentcloud.iotcloud.v20180614.models.BatchPublishMessage`
        """
        self._UpdateShadowTask = None
        self._PublishMessageTask = None

    @property
    def UpdateShadowTask(self):
        """批量更新影子任务的描述细节，当 taskType 取值为 “UpdateShadow” 时，此字段必填。描述见下 BatchUpdateShadow
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.BatchUpdateShadow`
        """
        return self._UpdateShadowTask

    @UpdateShadowTask.setter
    def UpdateShadowTask(self, UpdateShadowTask):
        self._UpdateShadowTask = UpdateShadowTask

    @property
    def PublishMessageTask(self):
        """批量下发消息任务的描述细节，当 taskType 取值为 “PublishMessage” 时，此字段必填。描述见下 BatchPublishMessage
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.BatchPublishMessage`
        """
        return self._PublishMessageTask

    @PublishMessageTask.setter
    def PublishMessageTask(self, PublishMessageTask):
        self._PublishMessageTask = PublishMessageTask


    def _deserialize(self, params):
        if params.get("UpdateShadowTask") is not None:
            self._UpdateShadowTask = BatchUpdateShadow()
            self._UpdateShadowTask._deserialize(params.get("UpdateShadowTask"))
        if params.get("PublishMessageTask") is not None:
            self._PublishMessageTask = BatchPublishMessage()
            self._PublishMessageTask._deserialize(params.get("PublishMessageTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """任务列表详细信息

    """

    def __init__(self):
        r"""
        :param _Type: 任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”
        :type Type: str
        :param _Id: 任务 ID
        :type Id: str
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _Status: 状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消
        :type Status: int
        :param _CreateTime: 任务创建时间，Unix 时间戳
        :type CreateTime: int
        :param _UpdateTime: 最后任务更新时间，Unix 时间戳
        :type UpdateTime: int
        :param _RetCode: 返回的错误码
        :type RetCode: int
        :param _ErrMsg: 返回的错误信息
        :type ErrMsg: str
        """
        self._Type = None
        self._Id = None
        self._ProductId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RetCode = None
        self._ErrMsg = None

    @property
    def Type(self):
        """任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """任务 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProductId(self):
        """产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        """状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """任务创建时间，Unix 时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后任务更新时间，Unix 时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RetCode(self):
        """返回的错误码
        :rtype: int
        """
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def ErrMsg(self):
        """返回的错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RetCode = params.get("RetCode")
        self._ErrMsg = params.get("ErrMsg")
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
        """规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Actions(self):
        """行为的JSON字符串，大部分种类举例如下：
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
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Description(self):
        """规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleDisabled(self):
        """是否禁用规则
        :rtype: bool
        """
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
        """网关设备的产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        """网关设备的设备名
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        """多个设备名
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Skey(self):
        """中兴CLAA设备的解绑需要Skey，普通设备不需要
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """设备所属产品id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EnableState(self):
        """要设置的设备状态，1为启用，0为禁用
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _Prefix: 下发delta消息的topic前缀，可选类型: "$shadow","$template"。不填写默认"$shadow"。
        :type Prefix: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._State = None
        self._ShadowVersion = None
        self._Prefix = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def State(self):
        """虚拟设备的状态，JSON字符串格式，由desired结构组成
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ShadowVersion(self):
        """当前版本号，需要和后台的version保持一致，才能更新成功
        :rtype: int
        """
        return self._ShadowVersion

    @ShadowVersion.setter
    def ShadowVersion(self, ShadowVersion):
        self._ShadowVersion = ShadowVersion

    @property
    def Prefix(self):
        """下发delta消息的topic前缀，可选类型: "$shadow","$template"。不填写默认"$shadow"。
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._State = params.get("State")
        self._ShadowVersion = params.get("ShadowVersion")
        self._Prefix = params.get("Prefix")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备影子数据，JSON字符串格式
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 设备所属产品id
        :type ProductID: str
        :param _DeviceNames: 设备名称集合
        :type DeviceNames: list of str
        :param _Status: 要设置的设备状态，1为启用，0为禁用
        :type Status: int
        """
        self._ProductID = None
        self._DeviceNames = None
        self._Status = None

    @property
    def ProductID(self):
        """设备所属产品id
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceNames(self):
        """设备名称集合
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Status(self):
        """要设置的设备状态，1为启用，0为禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RegisterType(self):
        """动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :rtype: int
        """
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def RegisterLimit(self):
        """动态注册设备上限
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._RequestId = None

    @property
    def RegisterType(self):
        """动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :rtype: int
        """
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        """动态注册产品密钥
        :rtype: str
        """
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        """动态注册设备上限
        :rtype: int
        """
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._RequestId = params.get("RequestId")


class UpdateTopicPolicyRequest(AbstractModel):
    """UpdateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _TopicName: 更新前Topic名
        :type TopicName: str
        :param _NewTopicName: 更新后Topic名
        :type NewTopicName: str
        :param _Privilege: Topic权限
        :type Privilege: int
        :param _BrokerSubscribe: 代理订阅信息
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        self._ProductID = None
        self._TopicName = None
        self._NewTopicName = None
        self._Privilege = None
        self._BrokerSubscribe = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def TopicName(self):
        """更新前Topic名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def NewTopicName(self):
        """更新后Topic名
        :rtype: str
        """
        return self._NewTopicName

    @NewTopicName.setter
    def NewTopicName(self, NewTopicName):
        self._NewTopicName = NewTopicName

    @property
    def Privilege(self):
        """Topic权限
        :rtype: int
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def BrokerSubscribe(self):
        """代理订阅信息
        :rtype: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        return self._BrokerSubscribe

    @BrokerSubscribe.setter
    def BrokerSubscribe(self, BrokerSubscribe):
        self._BrokerSubscribe = BrokerSubscribe


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _ProductID: 产品ID
        :type ProductID: str
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
        :param _FwType: 固件类型：选填 mcu、moudule。默认：mcu
        :type FwType: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Md5sum = None
        self._FileSize = None
        self._FirmwareName = None
        self._FirmwareDescription = None
        self._FwType = None

    @property
    def ProductID(self):
        """产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Md5sum(self):
        """固件的MD5值
        :rtype: str
        """
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def FileSize(self):
        """固件的大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FirmwareName(self):
        """固件名称
        :rtype: str
        """
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        """固件描述
        :rtype: str
        """
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription

    @property
    def FwType(self):
        """固件类型：选填 mcu、moudule。默认：mcu
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._Md5sum = params.get("Md5sum")
        self._FileSize = params.get("FileSize")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        self._FwType = params.get("FwType")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")