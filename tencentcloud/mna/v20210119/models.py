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


class AddDeviceRequest(AbstractModel):
    """AddDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 新建设备的名称
        :type DeviceName: str
        :param _Remark: 新建设备的备注
        :type Remark: str
        :param _DataKey: 新建设备的base64密钥字符串，非必选，如果不填写则由系统自动生成
        :type DataKey: str
        :param _Encrypted: 是否设置预置密钥
        :type Encrypted: bool
        """
        self._DeviceName = None
        self._Remark = None
        self._DataKey = None
        self._Encrypted = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DataKey(self):
        return self._DataKey

    @DataKey.setter
    def DataKey(self, DataKey):
        self._DataKey = DataKey

    @property
    def Encrypted(self):
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Remark = params.get("Remark")
        self._DataKey = params.get("DataKey")
        self._Encrypted = params.get("Encrypted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceResponse(AbstractModel):
    """AddDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataKey: 经过加密算法加密后的base64格式密钥
        :type DataKey: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _Signature: 签名字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Signature: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataKey = None
        self._DeviceId = None
        self._Signature = None
        self._RequestId = None

    @property
    def DataKey(self):
        return self._DataKey

    @DataKey.setter
    def DataKey(self, DataKey):
        self._DataKey = DataKey

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataKey = params.get("DataKey")
        self._DeviceId = params.get("DeviceId")
        self._Signature = params.get("Signature")
        self._RequestId = params.get("RequestId")


class Capacity(AbstractModel):
    """接口能力扩展，用于填充电信的加速Token，并为未来参数提供兼容空间

    """

    def __init__(self):
        r"""
        :param _CTCCToken: 电信鉴权的Token。要加速的电信手机终端访问 http://qos.189.cn/qos-api/getToken?appid=TencentCloud 页面，获取返回结果中result的值
        :type CTCCToken: str
        :param _Province: 终端所处在的省份，建议不填写由服务端自动获取，若需填写请填写带有省、市、自治区、特别行政区等后缀的省份中文全称
        :type Province: str
        """
        self._CTCCToken = None
        self._Province = None

    @property
    def CTCCToken(self):
        return self._CTCCToken

    @CTCCToken.setter
    def CTCCToken(self, CTCCToken):
        self._CTCCToken = CTCCToken

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province


    def _deserialize(self, params):
        self._CTCCToken = params.get("CTCCToken")
        self._Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Context(AbstractModel):
    """加速策略关键数据

    """

    def __init__(self):
        r"""
        :param _NetworkData: 测速数据
        :type NetworkData: :class:`tencentcloud.mna.v20210119.models.NetworkData`
        :param _ExpectedLowThreshold: 用户期望最低门限
        :type ExpectedLowThreshold: :class:`tencentcloud.mna.v20210119.models.ExpectedThreshold`
        :param _ExpectedHighThreshold: 用户期望最高门限
        :type ExpectedHighThreshold: :class:`tencentcloud.mna.v20210119.models.ExpectedThreshold`
        """
        self._NetworkData = None
        self._ExpectedLowThreshold = None
        self._ExpectedHighThreshold = None

    @property
    def NetworkData(self):
        return self._NetworkData

    @NetworkData.setter
    def NetworkData(self, NetworkData):
        self._NetworkData = NetworkData

    @property
    def ExpectedLowThreshold(self):
        return self._ExpectedLowThreshold

    @ExpectedLowThreshold.setter
    def ExpectedLowThreshold(self, ExpectedLowThreshold):
        self._ExpectedLowThreshold = ExpectedLowThreshold

    @property
    def ExpectedHighThreshold(self):
        return self._ExpectedHighThreshold

    @ExpectedHighThreshold.setter
    def ExpectedHighThreshold(self, ExpectedHighThreshold):
        self._ExpectedHighThreshold = ExpectedHighThreshold


    def _deserialize(self, params):
        if params.get("NetworkData") is not None:
            self._NetworkData = NetworkData()
            self._NetworkData._deserialize(params.get("NetworkData"))
        if params.get("ExpectedLowThreshold") is not None:
            self._ExpectedLowThreshold = ExpectedThreshold()
            self._ExpectedLowThreshold._deserialize(params.get("ExpectedLowThreshold"))
        if params.get("ExpectedHighThreshold") is not None:
            self._ExpectedHighThreshold = ExpectedThreshold()
            self._ExpectedHighThreshold._deserialize(params.get("ExpectedHighThreshold"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEncryptedKeyRequest(AbstractModel):
    """CreateEncryptedKey请求参数结构体

    """


class CreateEncryptedKeyResponse(AbstractModel):
    """CreateEncryptedKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EncryptedKey: 预置密钥
        :type EncryptedKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EncryptedKey = None
        self._RequestId = None

    @property
    def EncryptedKey(self):
        return self._EncryptedKey

    @EncryptedKey.setter
    def EncryptedKey(self, EncryptedKey):
        self._EncryptedKey = EncryptedKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptedKey = params.get("EncryptedKey")
        self._RequestId = params.get("RequestId")


class CreateQosRequest(AbstractModel):
    """CreateQos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcAddressInfo: 加速业务源地址信息，SrcIpv6和（SrcIpv4+SrcPublicIpv4）二选一，目前Ipv6不可用，全部填写以Ipv4参数为准。
        :type SrcAddressInfo: :class:`tencentcloud.mna.v20210119.models.SrcAddressInfo`
        :param _DestAddressInfo: 加速业务目标地址信息
        :type DestAddressInfo: :class:`tencentcloud.mna.v20210119.models.DestAddressInfo`
        :param _QosMenu: 加速套餐
T100K：时延性保障 + 带宽保障上下行保障 100kbps
T200K：时延性保障 + 带宽保障上下行保障 200kbps
T400K：时延性保障 + 带宽保障上下行保障  400kbps
BD1M：带宽型保障 + 下行带宽保障1Mbps
BD2M：带宽型保障 + 下行带宽保障2Mbps
BD4M：带宽型保障 + 下行带宽保障4Mbps
BU1M：带宽型保障 + 上行带宽保障1Mbps
BU2M：带宽型保障 + 上行带宽保障2Mbps
BU4M：带宽型保障 + 上行带宽保障4Mbps
        :type QosMenu: str
        :param _DeviceInfo: 申请加速的设备信息，包括运营商，操作系统，设备唯一标识等。
        :type DeviceInfo: :class:`tencentcloud.mna.v20210119.models.DeviceInfo`
        :param _Duration: 期望加速时长（单位分钟），默认值30分钟
        :type Duration: int
        :param _Capacity: 接口能力扩展，如果是电信用户，必须填充CTCC Token字段
        :type Capacity: :class:`tencentcloud.mna.v20210119.models.Capacity`
        :param _TemplateId: 应用模板ID
        :type TemplateId: str
        :param _Protocol: 针对特殊协议进行加速
1. IP （默认值）
2. UDP
3. TCP
        :type Protocol: int
        :param _Context: 加速策略关键数据
        :type Context: :class:`tencentcloud.mna.v20210119.models.Context`
        :param _Extern: 签名
        :type Extern: str
        """
        self._SrcAddressInfo = None
        self._DestAddressInfo = None
        self._QosMenu = None
        self._DeviceInfo = None
        self._Duration = None
        self._Capacity = None
        self._TemplateId = None
        self._Protocol = None
        self._Context = None
        self._Extern = None

    @property
    def SrcAddressInfo(self):
        return self._SrcAddressInfo

    @SrcAddressInfo.setter
    def SrcAddressInfo(self, SrcAddressInfo):
        self._SrcAddressInfo = SrcAddressInfo

    @property
    def DestAddressInfo(self):
        return self._DestAddressInfo

    @DestAddressInfo.setter
    def DestAddressInfo(self, DestAddressInfo):
        self._DestAddressInfo = DestAddressInfo

    @property
    def QosMenu(self):
        return self._QosMenu

    @QosMenu.setter
    def QosMenu(self, QosMenu):
        self._QosMenu = QosMenu

    @property
    def DeviceInfo(self):
        return self._DeviceInfo

    @DeviceInfo.setter
    def DeviceInfo(self, DeviceInfo):
        self._DeviceInfo = DeviceInfo

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Extern(self):
        return self._Extern

    @Extern.setter
    def Extern(self, Extern):
        self._Extern = Extern


    def _deserialize(self, params):
        if params.get("SrcAddressInfo") is not None:
            self._SrcAddressInfo = SrcAddressInfo()
            self._SrcAddressInfo._deserialize(params.get("SrcAddressInfo"))
        if params.get("DestAddressInfo") is not None:
            self._DestAddressInfo = DestAddressInfo()
            self._DestAddressInfo._deserialize(params.get("DestAddressInfo"))
        self._QosMenu = params.get("QosMenu")
        if params.get("DeviceInfo") is not None:
            self._DeviceInfo = DeviceInfo()
            self._DeviceInfo._deserialize(params.get("DeviceInfo"))
        self._Duration = params.get("Duration")
        if params.get("Capacity") is not None:
            self._Capacity = Capacity()
            self._Capacity._deserialize(params.get("Capacity"))
        self._TemplateId = params.get("TemplateId")
        self._Protocol = params.get("Protocol")
        if params.get("Context") is not None:
            self._Context = Context()
            self._Context._deserialize(params.get("Context"))
        self._Extern = params.get("Extern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQosResponse(AbstractModel):
    """CreateQos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 单次加速唯一 Id
        :type SessionId: str
        :param _Duration: 当前加速剩余时长（单位秒）
        :type Duration: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._Duration = None
        self._RequestId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Duration = params.get("Duration")
        self._RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 删除设备的唯一ID
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteQosRequest(AbstractModel):
    """DeleteQos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 单次加速唯一 Id
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQosResponse(AbstractModel):
    """DeleteQos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 单次加速唯一 Id
        :type SessionId: str
        :param _Duration: 本次加速会话持续时间（单位秒）
        :type Duration: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._Duration = None
        self._RequestId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Duration = params.get("Duration")
        self._RequestId = params.get("RequestId")


class DescribeQosRequest(AbstractModel):
    """DescribeQos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 单次加速唯一 Id
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQosResponse(AbstractModel):
    """DescribeQos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0：无匹配的加速中会话
1：存在匹配的加速中会话
        :type Status: int
        :param _SrcPublicIpv4: 手机公网出口IP，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcPublicIpv4: str
        :param _DestIpv4: 业务访问目的IP，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DestIpv4: list of str
        :param _Duration: 当前加速剩余时长（单位秒）有，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _QosMenu: 加速套餐类型，仅匹配时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type QosMenu: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._SrcPublicIpv4 = None
        self._DestIpv4 = None
        self._Duration = None
        self._QosMenu = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcPublicIpv4(self):
        return self._SrcPublicIpv4

    @SrcPublicIpv4.setter
    def SrcPublicIpv4(self, SrcPublicIpv4):
        self._SrcPublicIpv4 = SrcPublicIpv4

    @property
    def DestIpv4(self):
        return self._DestIpv4

    @DestIpv4.setter
    def DestIpv4(self, DestIpv4):
        self._DestIpv4 = DestIpv4

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def QosMenu(self):
        return self._QosMenu

    @QosMenu.setter
    def QosMenu(self, QosMenu):
        self._QosMenu = QosMenu

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._SrcPublicIpv4 = params.get("SrcPublicIpv4")
        self._DestIpv4 = params.get("DestIpv4")
        self._Duration = params.get("Duration")
        self._QosMenu = params.get("QosMenu")
        self._RequestId = params.get("RequestId")


class DestAddressInfo(AbstractModel):
    """多网聚合加速目标地址结构体

    """

    def __init__(self):
        r"""
        :param _DestIp: 加速业务目标 ip 地址数组
        :type DestIp: list of str
        """
        self._DestIp = None

    @property
    def DestIp(self):
        return self._DestIp

    @DestIp.setter
    def DestIp(self, DestIp):
        self._DestIp = DestIp


    def _deserialize(self, params):
        self._DestIp = params.get("DestIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceBaseInfo(AbstractModel):
    """设备的基本信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一ID
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _CreateTime: 设备创建的时间，单位：ms
        :type CreateTime: str
        :param _LastTime: 设备最后在线时间，单位：ms
        :type LastTime: str
        :param _Remark: 设备的备注
        :type Remark: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._CreateTime = None
        self._LastTime = None
        self._Remark = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastTime(self):
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._CreateTime = params.get("CreateTime")
        self._LastTime = params.get("LastTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDetails(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        r"""
        :param _DeviceBaseInfo: 设备基本信息
        :type DeviceBaseInfo: :class:`tencentcloud.mna.v20210119.models.DeviceBaseInfo`
        :param _DeviceNetInfo: 设备网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceNetInfo: list of DeviceNetInfo
        :param _GatewaySite: 聚合服务器地址
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewaySite: str
        :param _BusinessDownRate: 业务下行速率
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessDownRate: float
        :param _BusinessUpRate: 业务上行速率
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessUpRate: float
        """
        self._DeviceBaseInfo = None
        self._DeviceNetInfo = None
        self._GatewaySite = None
        self._BusinessDownRate = None
        self._BusinessUpRate = None

    @property
    def DeviceBaseInfo(self):
        return self._DeviceBaseInfo

    @DeviceBaseInfo.setter
    def DeviceBaseInfo(self, DeviceBaseInfo):
        self._DeviceBaseInfo = DeviceBaseInfo

    @property
    def DeviceNetInfo(self):
        return self._DeviceNetInfo

    @DeviceNetInfo.setter
    def DeviceNetInfo(self, DeviceNetInfo):
        self._DeviceNetInfo = DeviceNetInfo

    @property
    def GatewaySite(self):
        return self._GatewaySite

    @GatewaySite.setter
    def GatewaySite(self, GatewaySite):
        self._GatewaySite = GatewaySite

    @property
    def BusinessDownRate(self):
        return self._BusinessDownRate

    @BusinessDownRate.setter
    def BusinessDownRate(self, BusinessDownRate):
        self._BusinessDownRate = BusinessDownRate

    @property
    def BusinessUpRate(self):
        return self._BusinessUpRate

    @BusinessUpRate.setter
    def BusinessUpRate(self, BusinessUpRate):
        self._BusinessUpRate = BusinessUpRate


    def _deserialize(self, params):
        if params.get("DeviceBaseInfo") is not None:
            self._DeviceBaseInfo = DeviceBaseInfo()
            self._DeviceBaseInfo._deserialize(params.get("DeviceBaseInfo"))
        if params.get("DeviceNetInfo") is not None:
            self._DeviceNetInfo = []
            for item in params.get("DeviceNetInfo"):
                obj = DeviceNetInfo()
                obj._deserialize(item)
                self._DeviceNetInfo.append(obj)
        self._GatewaySite = params.get("GatewaySite")
        self._BusinessDownRate = params.get("BusinessDownRate")
        self._BusinessUpRate = params.get("BusinessUpRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备信息结构体

    """

    def __init__(self):
        r"""
        :param _Vendor: 运营商
1：移动 
2：电信
3：联通
4：广电
99：其他
        :type Vendor: int
        :param _OS: 设备操作系统：
1：Android
2： IOS
99：其他
        :type OS: int
        :param _DeviceId: 设备唯一标识
IOS 填写 IDFV
Android 填写 IMEI
        :type DeviceId: str
        :param _PhoneNum: 用户手机号码
        :type PhoneNum: str
        :param _Wireless: 无线信息
1：4G
2：5G
3：WIFI
99：其他
        :type Wireless: int
        """
        self._Vendor = None
        self._OS = None
        self._DeviceId = None
        self._PhoneNum = None
        self._Wireless = None

    @property
    def Vendor(self):
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def OS(self):
        return self._OS

    @OS.setter
    def OS(self, OS):
        self._OS = OS

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Wireless(self):
        return self._Wireless

    @Wireless.setter
    def Wireless(self, Wireless):
        self._Wireless = Wireless


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._OS = params.get("OS")
        self._DeviceId = params.get("DeviceId")
        self._PhoneNum = params.get("PhoneNum")
        self._Wireless = params.get("Wireless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceNetInfo(AbstractModel):
    """设备网络状态信息

    """

    def __init__(self):
        r"""
        :param _Type: 网络类型：
0:数据
1:Wi-Fi
2:有线
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _DataEnable: 启用/禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEnable: bool
        :param _UploadLimit: 上行限速
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadLimit: str
        :param _DownloadLimit: 下行限速
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadLimit: str
        :param _DataRx: 接收实时速率
注意：此字段可能返回 null，表示取不到有效值。
        :type DataRx: int
        :param _DataTx: 发送实时速率
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTx: int
        :param _Vendor: 运营商类型：
1: 中国移动；
2: 中国电信; 
3: 中国联通
注意：此字段可能返回 null，表示取不到有效值。
        :type Vendor: int
        :param _State: 连接状态：
0:无连接
1:连接中
2:已连接
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _PublicIp: 公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _SignalStrength: 信号强度/单位：dbm
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalStrength: int
        :param _Rat: 数据网络类型：
-1 ：无效值   
2：2G 
3：3G 
4：4G 
5：5G
注意：此字段可能返回 null，表示取不到有效值。
        :type Rat: int
        :param _NetInfoName: 网卡名
注意：此字段可能返回 null，表示取不到有效值。
        :type NetInfoName: str
        :param _DownRate: 下行实时速率（浮点数类型代替上一版本DataRx的整型）
注意：此字段可能返回 null，表示取不到有效值。
        :type DownRate: float
        :param _UpRate: 上行实时速率（浮点数类型代替上一版本TxRate的整型）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpRate: float
        """
        self._Type = None
        self._DataEnable = None
        self._UploadLimit = None
        self._DownloadLimit = None
        self._DataRx = None
        self._DataTx = None
        self._Vendor = None
        self._State = None
        self._PublicIp = None
        self._SignalStrength = None
        self._Rat = None
        self._NetInfoName = None
        self._DownRate = None
        self._UpRate = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DataEnable(self):
        return self._DataEnable

    @DataEnable.setter
    def DataEnable(self, DataEnable):
        self._DataEnable = DataEnable

    @property
    def UploadLimit(self):
        return self._UploadLimit

    @UploadLimit.setter
    def UploadLimit(self, UploadLimit):
        self._UploadLimit = UploadLimit

    @property
    def DownloadLimit(self):
        return self._DownloadLimit

    @DownloadLimit.setter
    def DownloadLimit(self, DownloadLimit):
        self._DownloadLimit = DownloadLimit

    @property
    def DataRx(self):
        return self._DataRx

    @DataRx.setter
    def DataRx(self, DataRx):
        self._DataRx = DataRx

    @property
    def DataTx(self):
        return self._DataTx

    @DataTx.setter
    def DataTx(self, DataTx):
        self._DataTx = DataTx

    @property
    def Vendor(self):
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def SignalStrength(self):
        return self._SignalStrength

    @SignalStrength.setter
    def SignalStrength(self, SignalStrength):
        self._SignalStrength = SignalStrength

    @property
    def Rat(self):
        return self._Rat

    @Rat.setter
    def Rat(self, Rat):
        self._Rat = Rat

    @property
    def NetInfoName(self):
        return self._NetInfoName

    @NetInfoName.setter
    def NetInfoName(self, NetInfoName):
        self._NetInfoName = NetInfoName

    @property
    def DownRate(self):
        return self._DownRate

    @DownRate.setter
    def DownRate(self, DownRate):
        self._DownRate = DownRate

    @property
    def UpRate(self):
        return self._UpRate

    @UpRate.setter
    def UpRate(self, UpRate):
        self._UpRate = UpRate


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._DataEnable = params.get("DataEnable")
        self._UploadLimit = params.get("UploadLimit")
        self._DownloadLimit = params.get("DownloadLimit")
        self._DataRx = params.get("DataRx")
        self._DataTx = params.get("DataTx")
        self._Vendor = params.get("Vendor")
        self._State = params.get("State")
        self._PublicIp = params.get("PublicIp")
        self._SignalStrength = params.get("SignalStrength")
        self._Rat = params.get("Rat")
        self._NetInfoName = params.get("NetInfoName")
        self._DownRate = params.get("DownRate")
        self._UpRate = params.get("UpRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpectedThreshold(AbstractModel):
    """用户期望门限

    """

    def __init__(self):
        r"""
        :param _RTT: 期望发起加速的时延阈值
        :type RTT: float
        :param _Loss: 期望发起加速的丢包率阈值
        :type Loss: float
        :param _Jitter: 期望发起加速的抖动阈值
        :type Jitter: float
        """
        self._RTT = None
        self._Loss = None
        self._Jitter = None

    @property
    def RTT(self):
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def Loss(self):
        return self._Loss

    @Loss.setter
    def Loss(self, Loss):
        self._Loss = Loss

    @property
    def Jitter(self):
        return self._Jitter

    @Jitter.setter
    def Jitter(self, Jitter):
        self._Jitter = Jitter


    def _deserialize(self, params):
        self._RTT = params.get("RTT")
        self._Loss = params.get("Loss")
        self._Jitter = params.get("Jitter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowDetails(AbstractModel):
    """设备流量信息

    """

    def __init__(self):
        r"""
        :param _NetDetails: 流量数据点
注意：此字段可能返回 null，表示取不到有效值。
        :type NetDetails: list of NetDetails
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _MaxValue: 流量最大值（单位：bytes）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxValue: float
        :param _AvgValue: 流量平均值（单位：bytes）
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgValue: float
        :param _TotalValue: 流量总值（单位：bytes）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalValue: float
        """
        self._NetDetails = None
        self._DeviceId = None
        self._MaxValue = None
        self._AvgValue = None
        self._TotalValue = None

    @property
    def NetDetails(self):
        return self._NetDetails

    @NetDetails.setter
    def NetDetails(self, NetDetails):
        self._NetDetails = NetDetails

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def MaxValue(self):
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def AvgValue(self):
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def TotalValue(self):
        return self._TotalValue

    @TotalValue.setter
    def TotalValue(self, TotalValue):
        self._TotalValue = TotalValue


    def _deserialize(self, params):
        if params.get("NetDetails") is not None:
            self._NetDetails = []
            for item in params.get("NetDetails"):
                obj = NetDetails()
                obj._deserialize(item)
                self._NetDetails.append(obj)
        self._DeviceId = params.get("DeviceId")
        self._MaxValue = params.get("MaxValue")
        self._AvgValue = params.get("AvgValue")
        self._TotalValue = params.get("TotalValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceRequest(AbstractModel):
    """GetDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 搜索指定设备的id
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceResponse(AbstractModel):
    """GetDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceDetails: 设备详细信息
        :type DeviceDetails: :class:`tencentcloud.mna.v20210119.models.DeviceDetails`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceDetails = None
        self._RequestId = None

    @property
    def DeviceDetails(self):
        return self._DeviceDetails

    @DeviceDetails.setter
    def DeviceDetails(self, DeviceDetails):
        self._DeviceDetails = DeviceDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceDetails") is not None:
            self._DeviceDetails = DeviceDetails()
            self._DeviceDetails._deserialize(params.get("DeviceDetails"))
        self._RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    """GetDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :type PageSize: int
        :param _PageNumber: 当前查看页码，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :type PageNumber: int
        :param _Keyword: 搜索设备的关键字（ID或者设备名），为空时匹配所有设备
        :type Keyword: str
        :param _DeviceType: DeviceType
不传：返回所有设备；
1:自有设备；
2:三方设备
        :type DeviceType: int
        """
        self._PageSize = None
        self._PageNumber = None
        self._Keyword = None
        self._DeviceType = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Keyword = params.get("Keyword")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicesResponse(AbstractModel):
    """GetDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceInfos: 设备信息列表
        :type DeviceInfos: list of DeviceBaseInfo
        :param _Length: 设备总记录条数
        :type Length: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceInfos = None
        self._Length = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def DeviceInfos(self):
        return self._DeviceInfos

    @DeviceInfos.setter
    def DeviceInfos(self, DeviceInfos):
        self._DeviceInfos = DeviceInfos

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceInfos") is not None:
            self._DeviceInfos = []
            for item in params.get("DeviceInfos"):
                obj = DeviceBaseInfo()
                obj._deserialize(item)
                self._DeviceInfos.append(obj)
        self._Length = params.get("Length")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class GetFlowStatisticRequest(AbstractModel):
    """GetFlowStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _BeginTime: 开始查找时间
        :type BeginTime: int
        :param _EndTime: 截止时间
        :type EndTime: int
        :param _Type: 流量种类（1：上行流量，2：下行流量）
        :type Type: int
        :param _TimeGranularity: 时间粒度（1：按小时统计，2：按天统计）
        :type TimeGranularity: int
        """
        self._DeviceId = None
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeGranularity(self):
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFlowStatisticResponse(AbstractModel):
    """GetFlowStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetDetails: 流量详细信息
        :type NetDetails: list of NetDetails
        :param _MaxValue: 查找时间段流量使用最大值（单位：byte）
        :type MaxValue: float
        :param _AvgValue: 查找时间段流量使用平均值（单位：byte）
        :type AvgValue: float
        :param _TotalValue: 查找时间段流量使用总量（单位：byte）
        :type TotalValue: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetDetails = None
        self._MaxValue = None
        self._AvgValue = None
        self._TotalValue = None
        self._RequestId = None

    @property
    def NetDetails(self):
        return self._NetDetails

    @NetDetails.setter
    def NetDetails(self, NetDetails):
        self._NetDetails = NetDetails

    @property
    def MaxValue(self):
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def AvgValue(self):
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def TotalValue(self):
        return self._TotalValue

    @TotalValue.setter
    def TotalValue(self, TotalValue):
        self._TotalValue = TotalValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NetDetails") is not None:
            self._NetDetails = []
            for item in params.get("NetDetails"):
                obj = NetDetails()
                obj._deserialize(item)
                self._NetDetails.append(obj)
        self._MaxValue = params.get("MaxValue")
        self._AvgValue = params.get("AvgValue")
        self._TotalValue = params.get("TotalValue")
        self._RequestId = params.get("RequestId")


class GetMultiFlowStatisticRequest(AbstractModel):
    """GetMultiFlowStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIds: 设备id列表，单次最多请求10个设备
        :type DeviceIds: list of str
        :param _BeginTime: 1659514436
        :type BeginTime: int
        :param _EndTime: 1659515000
        :type EndTime: int
        :param _Type: 统计流量类型（1：上行流量，2：下行流量）
        :type Type: int
        :param _TimeGranularity: 统计时间粒度（1：按小时统计，2：按天统计）
        :type TimeGranularity: int
        """
        self._DeviceIds = None
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None

    @property
    def DeviceIds(self):
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeGranularity(self):
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMultiFlowStatisticResponse(AbstractModel):
    """GetMultiFlowStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowDetails: 批量设备流量信息
        :type FlowDetails: list of FlowDetails
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowDetails = None
        self._RequestId = None

    @property
    def FlowDetails(self):
        return self._FlowDetails

    @FlowDetails.setter
    def FlowDetails(self, FlowDetails):
        self._FlowDetails = FlowDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FlowDetails") is not None:
            self._FlowDetails = []
            for item in params.get("FlowDetails"):
                obj = FlowDetails()
                obj._deserialize(item)
                self._FlowDetails.append(obj)
        self._RequestId = params.get("RequestId")


class GetNetMonitorRequest(AbstractModel):
    """GetNetMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _BeginTime: 开始时间
        :type BeginTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Metrics: 统计指标（上行速率："TxRate":bit/s，下行速率："RxRate":bit/s，丢包："Loss":%，时延："RTT":ms）
        :type Metrics: str
        """
        self._DeviceId = None
        self._BeginTime = None
        self._EndTime = None
        self._Metrics = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Metrics = params.get("Metrics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetNetMonitorResponse(AbstractModel):
    """GetNetMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorData: 监控数据
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorData: list of MonitorData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorData = None
        self._RequestId = None

    @property
    def MonitorData(self):
        return self._MonitorData

    @MonitorData.setter
    def MonitorData(self, MonitorData):
        self._MonitorData = MonitorData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MonitorData") is not None:
            self._MonitorData = []
            for item in params.get("MonitorData"):
                obj = MonitorData()
                obj._deserialize(item)
                self._MonitorData.append(obj)
        self._RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey请求参数结构体

    """


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PublicKey: 非对称公钥
        :type PublicKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PublicKey = None
        self._RequestId = None

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PublicKey = params.get("PublicKey")
        self._RequestId = params.get("RequestId")


class GetStatisticDataRequest(AbstractModel):
    """GetStatisticData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _BeginTime: 统计开始时间，单位：s
        :type BeginTime: int
        :param _EndTime: 统计结束时间，单位：s
        :type EndTime: int
        :param _TimeGranularity: 聚合粒度：
1:按小时统计
2:按天统计
        :type TimeGranularity: int
        """
        self._DeviceId = None
        self._BeginTime = None
        self._EndTime = None
        self._TimeGranularity = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TimeGranularity(self):
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TimeGranularity = params.get("TimeGranularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStatisticDataResponse(AbstractModel):
    """GetStatisticData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FilePath: 文件地址url
        :type FilePath: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FilePath = None
        self._RequestId = None

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FilePath = params.get("FilePath")
        self._RequestId = params.get("RequestId")


class MonitorData(AbstractModel):
    """流量监控指标

    """

    def __init__(self):
        r"""
        :param _Time: 时间点：s
        :type Time: str
        :param _BusinessMetrics: 业务指标（bps/ms/%）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessMetrics: float
        :param _SlotNetInfo: 网卡状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotNetInfo: list of SlotNetInfo
        """
        self._Time = None
        self._BusinessMetrics = None
        self._SlotNetInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def BusinessMetrics(self):
        return self._BusinessMetrics

    @BusinessMetrics.setter
    def BusinessMetrics(self, BusinessMetrics):
        self._BusinessMetrics = BusinessMetrics

    @property
    def SlotNetInfo(self):
        return self._SlotNetInfo

    @SlotNetInfo.setter
    def SlotNetInfo(self, SlotNetInfo):
        self._SlotNetInfo = SlotNetInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._BusinessMetrics = params.get("BusinessMetrics")
        if params.get("SlotNetInfo") is not None:
            self._SlotNetInfo = []
            for item in params.get("SlotNetInfo"):
                obj = SlotNetInfo()
                obj._deserialize(item)
                self._SlotNetInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetails(AbstractModel):
    """网络详细信息

    """

    def __init__(self):
        r"""
        :param _Current: 流量值（bit）
        :type Current: float
        :param _Time: 时间点，单位：s
        :type Time: str
        """
        self._Current = None
        self._Time = None

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Current = params.get("Current")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkData(AbstractModel):
    """测速数据

    """

    def __init__(self):
        r"""
        :param _RTT: 时延数组，最大长度30
        :type RTT: list of float
        :param _Loss: 丢包率
        :type Loss: float
        :param _Jitter: 抖动
        :type Jitter: float
        :param _Timestamp: 10位秒级时间戳
        :type Timestamp: int
        """
        self._RTT = None
        self._Loss = None
        self._Jitter = None
        self._Timestamp = None

    @property
    def RTT(self):
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def Loss(self):
        return self._Loss

    @Loss.setter
    def Loss(self, Loss):
        self._Loss = Loss

    @property
    def Jitter(self):
        return self._Jitter

    @Jitter.setter
    def Jitter(self, Jitter):
        self._Jitter = Jitter

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._RTT = params.get("RTT")
        self._Loss = params.get("Loss")
        self._Jitter = params.get("Jitter")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlotNetInfo(AbstractModel):
    """网卡流量指标数据

    """

    def __init__(self):
        r"""
        :param _NetInfoName: 网卡名
注意：此字段可能返回 null，表示取不到有效值。
        :type NetInfoName: str
        :param _PublicIP: 公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIP: str
        :param _Current: 指标数据（bps/ms/%）
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: float
        """
        self._NetInfoName = None
        self._PublicIP = None
        self._Current = None

    @property
    def NetInfoName(self):
        return self._NetInfoName

    @NetInfoName.setter
    def NetInfoName(self, NetInfoName):
        self._NetInfoName = NetInfoName

    @property
    def PublicIP(self):
        return self._PublicIP

    @PublicIP.setter
    def PublicIP(self, PublicIP):
        self._PublicIP = PublicIP

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current


    def _deserialize(self, params):
        self._NetInfoName = params.get("NetInfoName")
        self._PublicIP = params.get("PublicIP")
        self._Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrcAddressInfo(AbstractModel):
    """移动网络加速源地址结构体

    """

    def __init__(self):
        r"""
        :param _SrcIpv4: 用户私网 ipv4 地址
        :type SrcIpv4: str
        :param _SrcPublicIpv4: 用户公网 ipv4 地址
        :type SrcPublicIpv4: str
        :param _SrcIpv6: 用户 ipv6 地址
        :type SrcIpv6: str
        """
        self._SrcIpv4 = None
        self._SrcPublicIpv4 = None
        self._SrcIpv6 = None

    @property
    def SrcIpv4(self):
        return self._SrcIpv4

    @SrcIpv4.setter
    def SrcIpv4(self, SrcIpv4):
        self._SrcIpv4 = SrcIpv4

    @property
    def SrcPublicIpv4(self):
        return self._SrcPublicIpv4

    @SrcPublicIpv4.setter
    def SrcPublicIpv4(self, SrcPublicIpv4):
        self._SrcPublicIpv4 = SrcPublicIpv4

    @property
    def SrcIpv6(self):
        return self._SrcIpv6

    @SrcIpv6.setter
    def SrcIpv6(self, SrcIpv6):
        self._SrcIpv6 = SrcIpv6


    def _deserialize(self, params):
        self._SrcIpv4 = params.get("SrcIpv4")
        self._SrcPublicIpv4 = params.get("SrcPublicIpv4")
        self._SrcIpv6 = params.get("SrcIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceRequest(AbstractModel):
    """UpdateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Remark: 设备备注
        :type Remark: str
        :param _UpdateNetInfo: 更新设备网络信息
        :type UpdateNetInfo: list of UpdateNetInfo
        """
        self._DeviceId = None
        self._DeviceName = None
        self._Remark = None
        self._UpdateNetInfo = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdateNetInfo(self):
        return self._UpdateNetInfo

    @UpdateNetInfo.setter
    def UpdateNetInfo(self, UpdateNetInfo):
        self._UpdateNetInfo = UpdateNetInfo


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._Remark = params.get("Remark")
        if params.get("UpdateNetInfo") is not None:
            self._UpdateNetInfo = []
            for item in params.get("UpdateNetInfo"):
                obj = UpdateNetInfo()
                obj._deserialize(item)
                self._UpdateNetInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceResponse(AbstractModel):
    """UpdateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class UpdateNetInfo(AbstractModel):
    """更新设备网络状态信息

    """

    def __init__(self):
        r"""
        :param _Type: 网络类型：
0:数据
1:Wi-Fi
        :type Type: int
        :param _DataEnable: 启用/禁用
        :type DataEnable: bool
        :param _UploadLimit: 上行限速：bit
        :type UploadLimit: int
        :param _DownloadLimit: 下行限速：bit
        :type DownloadLimit: int
        :param _NetInfoName: 网卡名
        :type NetInfoName: str
        """
        self._Type = None
        self._DataEnable = None
        self._UploadLimit = None
        self._DownloadLimit = None
        self._NetInfoName = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DataEnable(self):
        return self._DataEnable

    @DataEnable.setter
    def DataEnable(self, DataEnable):
        self._DataEnable = DataEnable

    @property
    def UploadLimit(self):
        return self._UploadLimit

    @UploadLimit.setter
    def UploadLimit(self, UploadLimit):
        self._UploadLimit = UploadLimit

    @property
    def DownloadLimit(self):
        return self._DownloadLimit

    @DownloadLimit.setter
    def DownloadLimit(self, DownloadLimit):
        self._DownloadLimit = DownloadLimit

    @property
    def NetInfoName(self):
        return self._NetInfoName

    @NetInfoName.setter
    def NetInfoName(self, NetInfoName):
        self._NetInfoName = NetInfoName


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._DataEnable = params.get("DataEnable")
        self._UploadLimit = params.get("UploadLimit")
        self._DownloadLimit = params.get("DownloadLimit")
        self._NetInfoName = params.get("NetInfoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        