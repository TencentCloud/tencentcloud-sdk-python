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


class ActivateHardware(AbstractModel):
    """激活设备

    """

    def __init__(self):
        r"""
        :param _Vendor: 厂商名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Vendor: str
        :param _SN: 设备SN序列号
        :type SN: str
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _DataKey: 设备密钥
        :type DataKey: str
        :param _AccessScope: 接入环境。0：公有云网关；1：自有网关；2：公有云网关和自有网关。不填默认公有云网关。 具体含义： 公有云网关：即该设备只能接入公有云网关（就近接入） 自有网关：即该设备只能接入已经注册上线的自有网关（就近接入或固定ip接入） 公有云网关和自有网关：即该设备同时可以接入公有云网关和已经注册上线的自有网关（就近接入或固定ip接入）
        :type AccessScope: int
        :param _LicensePayMode: 当付费方为租户时，可选择租户license付费方式：
0，月度授权
1，永久授权
若不传则默认为月度授权。
当付费方为厂商时，此参数无效

注意：此字段可能返回 null，表示取不到有效值。
        :type LicensePayMode: int
        :param _GroupId: 设备分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 设备分组名称，预留参数，需要分组时传入GroupId
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self._Vendor = None
        self._SN = None
        self._DeviceName = None
        self._Description = None
        self._DataKey = None
        self._AccessScope = None
        self._LicensePayMode = None
        self._GroupId = None
        self._GroupName = None

    @property
    def Vendor(self):
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DataKey(self):
        return self._DataKey

    @DataKey.setter
    def DataKey(self, DataKey):
        self._DataKey = DataKey

    @property
    def AccessScope(self):
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def LicensePayMode(self):
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._SN = params.get("SN")
        self._DeviceName = params.get("DeviceName")
        self._Description = params.get("Description")
        self._DataKey = params.get("DataKey")
        self._AccessScope = params.get("AccessScope")
        self._LicensePayMode = params.get("LicensePayMode")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateHardwareRequest(AbstractModel):
    """ActivateHardware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Hardware: 待激活的设备列表
        :type Hardware: list of ActivateHardware
        """
        self._Hardware = None

    @property
    def Hardware(self):
        return self._Hardware

    @Hardware.setter
    def Hardware(self, Hardware):
        self._Hardware = Hardware


    def _deserialize(self, params):
        if params.get("Hardware") is not None:
            self._Hardware = []
            for item in params.get("Hardware"):
                obj = ActivateHardware()
                obj._deserialize(item)
                self._Hardware.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateHardwareResponse(AbstractModel):
    """ActivateHardware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HardwareInfo: 完成激活的设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareInfo: list of ActivateHardware
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HardwareInfo = None
        self._RequestId = None

    @property
    def HardwareInfo(self):
        return self._HardwareInfo

    @HardwareInfo.setter
    def HardwareInfo(self, HardwareInfo):
        self._HardwareInfo = HardwareInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HardwareInfo") is not None:
            self._HardwareInfo = []
            for item in params.get("HardwareInfo"):
                obj = ActivateHardware()
                obj._deserialize(item)
                self._HardwareInfo.append(obj)
        self._RequestId = params.get("RequestId")


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
        :param _AccessScope: 接入环境。0：公有云网关；1：自有网关；2：公有云网关和自有网关。不填默认公有云网关。
具体含义：
公有云网关：即该设备只能接入公有云网关（就近接入）
自有网关：即该设备只能接入已经注册上线的自有网关（就近接入或固定ip接入）
公有云网关和自有网关：即该设备同时可以接入公有云网关和已经注册上线的自有网关（就近接入或固定ip接入）
        :type AccessScope: int
        :param _LicensePayMode: license付费方式： 
0，月度授权 
1，永久授权 
若不传则默认为月度授权
        :type LicensePayMode: int
        :param _GroupName: 设备分组名称，非必选，预留参数，需要分组时传入GroupId
        :type GroupName: str
        :param _GroupId: 设备分组ID，非必选，如果不填写则默认设备无分组
        :type GroupId: str
        """
        self._DeviceName = None
        self._Remark = None
        self._DataKey = None
        self._Encrypted = None
        self._AccessScope = None
        self._LicensePayMode = None
        self._GroupName = None
        self._GroupId = None

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

    @property
    def AccessScope(self):
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def LicensePayMode(self):
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Remark = params.get("Remark")
        self._DataKey = params.get("DataKey")
        self._Encrypted = params.get("Encrypted")
        self._AccessScope = params.get("AccessScope")
        self._LicensePayMode = params.get("LicensePayMode")
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class AddHardwareRequest(AbstractModel):
    """AddHardware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Hardware: 硬件列表
        :type Hardware: list of Hardware
        """
        self._Hardware = None

    @property
    def Hardware(self):
        return self._Hardware

    @Hardware.setter
    def Hardware(self, Hardware):
        self._Hardware = Hardware


    def _deserialize(self, params):
        if params.get("Hardware") is not None:
            self._Hardware = []
            for item in params.get("Hardware"):
                obj = Hardware()
                obj._deserialize(item)
                self._Hardware.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddHardwareResponse(AbstractModel):
    """AddHardware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Hardware: 硬件设备
        :type Hardware: list of Hardware
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Hardware = None
        self._RequestId = None

    @property
    def Hardware(self):
        return self._Hardware

    @Hardware.setter
    def Hardware(self, Hardware):
        self._Hardware = Hardware

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Hardware") is not None:
            self._Hardware = []
            for item in params.get("Hardware"):
                obj = Hardware()
                obj._deserialize(item)
                self._Hardware.append(obj)
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _AccessScope: 接入环境。0：公有云网关；1：自有网关；2：公有云网关和自有网关。默认公有云网关。 具体含义： 公有云网关：即该设备只能接入公有云网关（就近接入） 自有网关：即该设备只能接入已经注册上线的自有网关（就近接入或固定ip接入） 公有云网关和自有网关：即该设备同时可以接入公有云网关和已经注册上线的自有网关（就近接入或固定ip接入）
        :type AccessScope: int
        :param _LicensePayMode: license授权有效期 0：月度授权 1：永久授权
注意：此字段可能返回 null，表示取不到有效值。
        :type LicensePayMode: int
        :param _Payer: 付费方 0：厂商付费 1：客户付费
注意：此字段可能返回 null，表示取不到有效值。
        :type Payer: int
        :param _GroupId: 设备分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 设备分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._CreateTime = None
        self._LastTime = None
        self._Remark = None
        self._AccessScope = None
        self._LicensePayMode = None
        self._Payer = None
        self._GroupId = None
        self._GroupName = None

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

    @property
    def AccessScope(self):
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def LicensePayMode(self):
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def Payer(self):
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._CreateTime = params.get("CreateTime")
        self._LastTime = params.get("LastTime")
        self._Remark = params.get("Remark")
        self._AccessScope = params.get("AccessScope")
        self._LicensePayMode = params.get("LicensePayMode")
        self._Payer = params.get("Payer")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
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
        


class DevicePayModeInfo(AbstractModel):
    """设备付费模式信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _PayMode: 付费模式。
1：预付费流量包
0：按流量后付费
        :type PayMode: int
        :param _PayModeDesc: 付费模式描述
        :type PayModeDesc: str
        :param _ResourceId: 流量包ID，仅当付费模式为流量包类型时才有。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        """
        self._DeviceId = None
        self._PayMode = None
        self._PayModeDesc = None
        self._ResourceId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeDesc(self):
        return self._PayModeDesc

    @PayModeDesc.setter
    def PayModeDesc(self, PayModeDesc):
        self._PayModeDesc = PayModeDesc

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._PayMode = params.get("PayMode")
        self._PayModeDesc = params.get("PayModeDesc")
        self._ResourceId = params.get("ResourceId")
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
        


class FlowPackageInfo(AbstractModel):
    """流量包信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 流量包的唯一资源ID
        :type ResourceId: str
        :param _AppId: 流量包所属的用户AppId
        :type AppId: int
        :param _PackageType: 流量包规格类型。可取值如下：
DEVICE_1_FLOW_20G、DEVICE_2_FLOW_50G、
DEVICE_3_FLOW_100G、
DEVICE_5_FLOW_500G，分别代表20G、50G、100G、500G档位的流量包。
档位也影响流量包可绑定的设备数量上限：
20G：最多绑定1个设备
50G：最多绑定2个设备
100G：最多绑定3个设备
500G：最多绑定5个设备
        :type PackageType: str
        :param _Status: 流量包状态，0：未生效，1：有效期内，2：已过期
        :type Status: int
        :param _CreateTime: 购买时间，Unix时间戳格式，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _ActiveTime: 生效时间，Unix时间戳格式，单位：秒
        :type ActiveTime: int
        :param _ExpireTime: 过期时间，Unix时间戳格式，单位：秒
        :type ExpireTime: int
        :param _DeviceList: 流量包绑定的设备ID列表
        :type DeviceList: list of str
        :param _CapacitySize: 流量包总容量，单位：MB
        :type CapacitySize: int
        :param _CapacityRemain: 流量包余量，单位：MB
        :type CapacityRemain: int
        :param _RenewFlag: 自动续费标识。true代表自动续费，false代表不自动续费
        :type RenewFlag: bool
        :param _ModifyStatus: 资源包变更状态，0：未发生变配；1：变配中；2：已变配或已续费
        :type ModifyStatus: int
        :param _TruncFlag: 流量截断标识。true代表开启流量截断，false代表不开启流量截断
        :type TruncFlag: bool
        :param _CapacityRemainPrecise: 流量包精确余量，单位：MB
        :type CapacityRemainPrecise: int
        """
        self._ResourceId = None
        self._AppId = None
        self._PackageType = None
        self._Status = None
        self._CreateTime = None
        self._ActiveTime = None
        self._ExpireTime = None
        self._DeviceList = None
        self._CapacitySize = None
        self._CapacityRemain = None
        self._RenewFlag = None
        self._ModifyStatus = None
        self._TruncFlag = None
        self._CapacityRemainPrecise = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

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
    def ActiveTime(self):
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def CapacitySize(self):
        return self._CapacitySize

    @CapacitySize.setter
    def CapacitySize(self, CapacitySize):
        self._CapacitySize = CapacitySize

    @property
    def CapacityRemain(self):
        return self._CapacityRemain

    @CapacityRemain.setter
    def CapacityRemain(self, CapacityRemain):
        self._CapacityRemain = CapacityRemain

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ModifyStatus(self):
        return self._ModifyStatus

    @ModifyStatus.setter
    def ModifyStatus(self, ModifyStatus):
        self._ModifyStatus = ModifyStatus

    @property
    def TruncFlag(self):
        return self._TruncFlag

    @TruncFlag.setter
    def TruncFlag(self, TruncFlag):
        self._TruncFlag = TruncFlag

    @property
    def CapacityRemainPrecise(self):
        return self._CapacityRemainPrecise

    @CapacityRemainPrecise.setter
    def CapacityRemainPrecise(self, CapacityRemainPrecise):
        self._CapacityRemainPrecise = CapacityRemainPrecise


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._PackageType = params.get("PackageType")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ActiveTime = params.get("ActiveTime")
        self._ExpireTime = params.get("ExpireTime")
        self._DeviceList = params.get("DeviceList")
        self._CapacitySize = params.get("CapacitySize")
        self._CapacityRemain = params.get("CapacityRemain")
        self._RenewFlag = params.get("RenewFlag")
        self._ModifyStatus = params.get("ModifyStatus")
        self._TruncFlag = params.get("TruncFlag")
        self._CapacityRemainPrecise = params.get("CapacityRemainPrecise")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicePayModeRequest(AbstractModel):
    """GetDevicePayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIdList: 设备ID列表
        :type DeviceIdList: list of str
        """
        self._DeviceIdList = None

    @property
    def DeviceIdList(self):
        return self._DeviceIdList

    @DeviceIdList.setter
    def DeviceIdList(self, DeviceIdList):
        self._DeviceIdList = DeviceIdList


    def _deserialize(self, params):
        self._DeviceIdList = params.get("DeviceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicePayModeResponse(AbstractModel):
    """GetDevicePayMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果信息
        :type Result: list of DevicePayModeInfo
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
            self._Result = []
            for item in params.get("Result"):
                obj = DevicePayModeInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class GetFlowAlarmInfoRequest(AbstractModel):
    """GetFlowAlarmInfo请求参数结构体

    """


class GetFlowAlarmInfoResponse(AbstractModel):
    """GetFlowAlarmInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmValue: 流量包的告警阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmValue: int
        :param _NotifyUrl: 告警通知回调url
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyUrl: str
        :param _CallbackKey: 告警通知回调key
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmValue = None
        self._NotifyUrl = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def AlarmValue(self):
        return self._AlarmValue

    @AlarmValue.setter
    def AlarmValue(self, AlarmValue):
        self._AlarmValue = AlarmValue

    @property
    def NotifyUrl(self):
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmValue = params.get("AlarmValue")
        self._NotifyUrl = params.get("NotifyUrl")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class GetFlowPackagesRequest(AbstractModel):
    """GetFlowPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码，从1开始
        :type PageNumber: int
        :param _PageSize: 每页个数
        :type PageSize: int
        :param _ResourceId: 流量包的唯一资源ID
        :type ResourceId: str
        :param _DeviceId: 流量包绑定的设备ID
        :type DeviceId: str
        :param _Status: 流量包状态，0：未生效，1：有效期内，2：已过期

        :type Status: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._ResourceId = None
        self._DeviceId = None
        self._Status = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ResourceId = params.get("ResourceId")
        self._DeviceId = params.get("DeviceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFlowPackagesResponse(AbstractModel):
    """GetFlowPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageList: 流量包列表
        :type PackageList: list of FlowPackageInfo
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackageList = None
        self._Total = None
        self._RequestId = None

    @property
    def PackageList(self):
        return self._PackageList

    @PackageList.setter
    def PackageList(self, PackageList):
        self._PackageList = PackageList

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
        if params.get("PackageList") is not None:
            self._PackageList = []
            for item in params.get("PackageList"):
                obj = FlowPackageInfo()
                obj._deserialize(item)
                self._PackageList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetFlowStatisticByGroupRequest(AbstractModel):
    """GetFlowStatisticByGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _BeginTime: 开始查找时间
        :type BeginTime: int
        :param _EndTime: 截止时间
        :type EndTime: int
        :param _Type: 流量种类（1：上行流量，2：下行流量， 3: 上下行总和）
        :type Type: int
        :param _TimeGranularity: 时间粒度（1：按小时统计，2：按天统计）
        :type TimeGranularity: int
        :param _AccessRegion: 接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :type AccessRegion: str
        :param _GatewayType: 网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :type GatewayType: int
        """
        self._GroupId = None
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None
        self._AccessRegion = None
        self._GatewayType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        self._AccessRegion = params.get("AccessRegion")
        self._GatewayType = params.get("GatewayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFlowStatisticByGroupResponse(AbstractModel):
    """GetFlowStatisticByGroup返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Type: 流量种类（1：上行流量，2：下行流量，3：上下行总和）
        :type Type: int
        :param _TimeGranularity: 时间粒度（1：按小时统计，2：按天统计）
        :type TimeGranularity: int
        :param _AccessRegion: 接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :type AccessRegion: str
        :param _GatewayType: 网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :type GatewayType: int
        :param _DeviceList: 设备ID列表，用于查询多设备流量，该字段启用时DeviceId可传"-1"
        :type DeviceList: list of str
        """
        self._DeviceId = None
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None
        self._AccessRegion = None
        self._GatewayType = None
        self._DeviceList = None

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

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        self._AccessRegion = params.get("AccessRegion")
        self._GatewayType = params.get("GatewayType")
        self._DeviceList = params.get("DeviceList")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class GetHardwareListRequest(AbstractModel):
    """GetHardwareList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页面设备数量
        :type PageSize: int
        :param _Keyword: 关键字
        :type Keyword: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetHardwareListResponse(AbstractModel):
    """GetHardwareList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HardwareInfos: 硬件信息列表
        :type HardwareInfos: list of HardwareInfo
        :param _Length: 硬件总数
        :type Length: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HardwareInfos = None
        self._Length = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def HardwareInfos(self):
        return self._HardwareInfos

    @HardwareInfos.setter
    def HardwareInfos(self, HardwareInfos):
        self._HardwareInfos = HardwareInfos

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
        if params.get("HardwareInfos") is not None:
            self._HardwareInfos = []
            for item in params.get("HardwareInfos"):
                obj = HardwareInfo()
                obj._deserialize(item)
                self._HardwareInfos.append(obj)
        self._Length = params.get("Length")
        self._TotalPage = params.get("TotalPage")
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
        :param _Type: 统计流量类型（1：上行流量，2：下行流量， 3: 上下行总和）
        :type Type: int
        :param _TimeGranularity: 统计时间粒度（1：按小时统计，2：按天统计）
        :type TimeGranularity: int
        :param _AccessRegion: 接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :type AccessRegion: str
        :param _GatewayType: 网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :type GatewayType: int
        """
        self._DeviceIds = None
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None
        self._AccessRegion = None
        self._GatewayType = None

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

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        self._AccessRegion = params.get("AccessRegion")
        self._GatewayType = params.get("GatewayType")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _GatewayType: 网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :type GatewayType: int
        """
        self._DeviceId = None
        self._BeginTime = None
        self._EndTime = None
        self._Metrics = None
        self._GatewayType = None

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

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Metrics = params.get("Metrics")
        self._GatewayType = params.get("GatewayType")
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
        :param _AccessRegion: 接入区域。取值范围：['MC','AP','EU','AM']
MC=中国大陆
AP=亚太
EU=欧洲
AM=美洲
        :type AccessRegion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorData = None
        self._AccessRegion = None
        self._RequestId = None

    @property
    def MonitorData(self):
        return self._MonitorData

    @MonitorData.setter
    def MonitorData(self, MonitorData):
        self._MonitorData = MonitorData

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

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
        self._AccessRegion = params.get("AccessRegion")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _DeviceId: 设备ID。若不指定设备，可传"-1"
        :type DeviceId: str
        :param _BeginTime: 统计开始时间，单位：s
        :type BeginTime: int
        :param _EndTime: 统计结束时间，单位：s
        :type EndTime: int
        :param _TimeGranularity: 聚合粒度：
1:按小时统计
2:按天统计
        :type TimeGranularity: int
        :param _AccessRegion: 接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :type AccessRegion: str
        :param _GatewayType: 网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :type GatewayType: int
        :param _DeviceList: 设备ID列表，最多10个设备，下载多个设备流量和时使用，此时DeviceId可传"-1"
        :type DeviceList: list of str
        :param _GroupId: 设备分组ID，若不指定分组则不传，按分组下载数据时使用
        :type GroupId: str
        """
        self._DeviceId = None
        self._BeginTime = None
        self._EndTime = None
        self._TimeGranularity = None
        self._AccessRegion = None
        self._GatewayType = None
        self._DeviceList = None
        self._GroupId = None

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

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TimeGranularity = params.get("TimeGranularity")
        self._AccessRegion = params.get("AccessRegion")
        self._GatewayType = params.get("GatewayType")
        self._DeviceList = params.get("DeviceList")
        self._GroupId = params.get("GroupId")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class GetVendorHardwareRequest(AbstractModel):
    """GetVendorHardware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页面数量
        :type PageSize: int
        :param _Keyword: 关键字
        :type Keyword: str
        :param _Status: 激活状态，
空：全部；
1:待激活；
2:已激活；
        :type Status: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._Status = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetVendorHardwareResponse(AbstractModel):
    """GetVendorHardware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VendorHardware: 硬件信息列表
        :type VendorHardware: list of VendorHardware
        :param _Length: 设备总数
        :type Length: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VendorHardware = None
        self._Length = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def VendorHardware(self):
        return self._VendorHardware

    @VendorHardware.setter
    def VendorHardware(self, VendorHardware):
        self._VendorHardware = VendorHardware

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
        if params.get("VendorHardware") is not None:
            self._VendorHardware = []
            for item in params.get("VendorHardware"):
                obj = VendorHardware()
                obj._deserialize(item)
                self._VendorHardware.append(obj)
        self._Length = params.get("Length")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class Hardware(AbstractModel):
    """新建Hardware入参

    """

    def __init__(self):
        r"""
        :param _SN: 硬件序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SN: str
        :param _LicenseChargingMode: license计费模式：
1，租户付费
2，厂商月付费
3，厂商永久授权
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseChargingMode: int
        :param _Description: 设备描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _HardwareId: 硬件ID，入参无需传递
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareId: str
        """
        self._SN = None
        self._LicenseChargingMode = None
        self._Description = None
        self._HardwareId = None

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def LicenseChargingMode(self):
        return self._LicenseChargingMode

    @LicenseChargingMode.setter
    def LicenseChargingMode(self, LicenseChargingMode):
        self._LicenseChargingMode = LicenseChargingMode

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def HardwareId(self):
        return self._HardwareId

    @HardwareId.setter
    def HardwareId(self, HardwareId):
        self._HardwareId = HardwareId


    def _deserialize(self, params):
        self._SN = params.get("SN")
        self._LicenseChargingMode = params.get("LicenseChargingMode")
        self._Description = params.get("Description")
        self._HardwareId = params.get("HardwareId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HardwareInfo(AbstractModel):
    """硬件信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param _LastOnlineTime: 最后在线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnlineTime: str
        :param _Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _VendorDescription: 厂商备注
注意：此字段可能返回 null，表示取不到有效值。
        :type VendorDescription: str
        :param _LicenseChargingMode: license计费模式： 1，租户月付费 2，厂商月付费 3，license永久授权
注：后续将废弃此参数，新接入请使用LicensePayMode和Payer
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseChargingMode: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _SN: 硬件序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SN: str
        :param _LicensePayMode: license授权有效期 
0：月度授权 
1：永久授权
注意：此字段可能返回 null，表示取不到有效值。
        :type LicensePayMode: int
        :param _Payer: 付费方 
0：客户付费 
1：厂商付费
注意：此字段可能返回 null，表示取不到有效值。
        :type Payer: int
        :param _GroupId: 设备分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 设备分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ActiveTime = None
        self._LastOnlineTime = None
        self._Description = None
        self._VendorDescription = None
        self._LicenseChargingMode = None
        self._CreateTime = None
        self._SN = None
        self._LicensePayMode = None
        self._Payer = None
        self._GroupId = None
        self._GroupName = None

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
    def ActiveTime(self):
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def LastOnlineTime(self):
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VendorDescription(self):
        return self._VendorDescription

    @VendorDescription.setter
    def VendorDescription(self, VendorDescription):
        self._VendorDescription = VendorDescription

    @property
    def LicenseChargingMode(self):
        return self._LicenseChargingMode

    @LicenseChargingMode.setter
    def LicenseChargingMode(self, LicenseChargingMode):
        self._LicenseChargingMode = LicenseChargingMode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def LicensePayMode(self):
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def Payer(self):
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ActiveTime = params.get("ActiveTime")
        self._LastOnlineTime = params.get("LastOnlineTime")
        self._Description = params.get("Description")
        self._VendorDescription = params.get("VendorDescription")
        self._LicenseChargingMode = params.get("LicenseChargingMode")
        self._CreateTime = params.get("CreateTime")
        self._SN = params.get("SN")
        self._LicensePayMode = params.get("LicensePayMode")
        self._Payer = params.get("Payer")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPackageRenewFlagRequest(AbstractModel):
    """ModifyPackageRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 流量包的唯一资源ID
        :type ResourceId: str
        :param _RenewFlag: 自动续费标识。true代表自动续费，false代表不自动续费
        :type RenewFlag: bool
        """
        self._ResourceId = None
        self._RenewFlag = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPackageRenewFlagResponse(AbstractModel):
    """ModifyPackageRenewFlag返回参数结构体

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
        :param _Current: 流量值（byte）
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
        


class OrderFlowPackageRequest(AbstractModel):
    """OrderFlowPackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageType: 流量包规格类型。可取值如下：
DEVICE_1_FLOW_20G、DEVICE_2_FLOW_50G、
DEVICE_3_FLOW_100G、
DEVICE_5_FLOW_500G，分别代表20G、50G、100G、500G档位的流量包。
档位也影响流量包可绑定的设备数量上限：
20G：最多绑定1个设备
50G：最多绑定2个设备
100G：最多绑定3个设备
500G：最多绑定5个设备
        :type PackageType: str
        :param _DeviceList: 流量包绑定的设备ID列表。捆绑设备个数上限取决于包的规格档位：
20G：最多绑定1个设备
50G：最多绑定2个设备
100G：最多绑定3个设备
500G：最多绑定5个设备
        :type DeviceList: list of str
        :param _AutoRenewFlag: 是否自动续费，该选项和流量截断冲突，只能开启一个
        :type AutoRenewFlag: bool
        :param _PackageRegion: 区域标识，0：国内，1：国外
        :type PackageRegion: int
        :param _FlowTruncFlag: 是否开启流量截断功能，该选项和自动续费冲突
        :type FlowTruncFlag: bool
        :param _AutoVoucher: 是否自动选择代金券，默认false。
有多张券时的选择策略：按照可支付订单全部金额的券，先到期的券，可抵扣金额最大的券，余额最小的券，现金券 这个优先级进行扣券，且最多只抵扣一张券。
        :type AutoVoucher: bool
        :param _VoucherIds: 指定代金券ID。自动选择代金券时此参数无效。目前只允许传入一张代金券。
注：若指定的代金券不符合订单抵扣条件，则正常支付，不扣券
        :type VoucherIds: list of str
        """
        self._PackageType = None
        self._DeviceList = None
        self._AutoRenewFlag = None
        self._PackageRegion = None
        self._FlowTruncFlag = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def FlowTruncFlag(self):
        return self._FlowTruncFlag

    @FlowTruncFlag.setter
    def FlowTruncFlag(self, FlowTruncFlag):
        self._FlowTruncFlag = FlowTruncFlag

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._PackageType = params.get("PackageType")
        self._DeviceList = params.get("DeviceList")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PackageRegion = params.get("PackageRegion")
        self._FlowTruncFlag = params.get("FlowTruncFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderFlowPackageResponse(AbstractModel):
    """OrderFlowPackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 流量包的唯一资源ID
        :type ResourceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._RequestId = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._RequestId = params.get("RequestId")


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


class UpdateHardwareRequest(AbstractModel):
    """UpdateHardware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HardwareId: 硬件ID
        :type HardwareId: str
        :param _SN: 硬件序列号
        :type SN: str
        :param _Description: 设备备注
        :type Description: str
        """
        self._HardwareId = None
        self._SN = None
        self._Description = None

    @property
    def HardwareId(self):
        return self._HardwareId

    @HardwareId.setter
    def HardwareId(self, HardwareId):
        self._HardwareId = HardwareId

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._HardwareId = params.get("HardwareId")
        self._SN = params.get("SN")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateHardwareResponse(AbstractModel):
    """UpdateHardware返回参数结构体

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
        


class VendorHardware(AbstractModel):
    """厂商硬件详细信息

    """

    def __init__(self):
        r"""
        :param _HardwareId: 硬件id
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareId: str
        :param _SN: 硬件序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SN: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Status: 激活状态， 空：全部； 1:待激活； 2:已激活
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ActiveTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: str
        :param _Description: 厂商备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _DeviceId: 设备id
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _LicenseChargingMode: license计费模式： 1，租户月付费 2，厂商月付费 3，license永久授权
注：设备为租户付费且未激活（未选择月付还是永久付费）时，此参数返回1，仅代表租户付费。后续将废弃此参数，新接入请使用LicensePayMode和Payer
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseChargingMode: int
        :param _LastOnlineTime: 最后在线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnlineTime: str
        :param _LicensePayMode: license授权有效期
0：月度授权
1：永久授权
-1：未知
注意：此字段可能返回 null，表示取不到有效值。
        :type LicensePayMode: int
        :param _Payer: 付费方
0：客户付费
1：厂商付费
注意：此字段可能返回 null，表示取不到有效值。
        :type Payer: int
        """
        self._HardwareId = None
        self._SN = None
        self._CreateTime = None
        self._Status = None
        self._ActiveTime = None
        self._Description = None
        self._DeviceId = None
        self._LicenseChargingMode = None
        self._LastOnlineTime = None
        self._LicensePayMode = None
        self._Payer = None

    @property
    def HardwareId(self):
        return self._HardwareId

    @HardwareId.setter
    def HardwareId(self, HardwareId):
        self._HardwareId = HardwareId

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActiveTime(self):
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def LicenseChargingMode(self):
        return self._LicenseChargingMode

    @LicenseChargingMode.setter
    def LicenseChargingMode(self, LicenseChargingMode):
        self._LicenseChargingMode = LicenseChargingMode

    @property
    def LastOnlineTime(self):
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def LicensePayMode(self):
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def Payer(self):
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer


    def _deserialize(self, params):
        self._HardwareId = params.get("HardwareId")
        self._SN = params.get("SN")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._ActiveTime = params.get("ActiveTime")
        self._Description = params.get("Description")
        self._DeviceId = params.get("DeviceId")
        self._LicenseChargingMode = params.get("LicenseChargingMode")
        self._LastOnlineTime = params.get("LastOnlineTime")
        self._LicensePayMode = params.get("LicensePayMode")
        self._Payer = params.get("Payer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        