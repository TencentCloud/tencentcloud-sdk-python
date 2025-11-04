# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""激活设备

    """

    def __init__(self):
        r"""
        :param _Vendor: 厂商名称
        :type Vendor: str
        :param _SN: 设备SN序列号
        :type SN: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Description: 备注
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

        :type LicensePayMode: int
        :param _GroupId: 设备分组ID
        :type GroupId: str
        :param _GroupName: 设备分组名称，预留参数，需要分组时传入GroupId
        :type GroupName: str
        :param _FlowTrunc: 设备无流量包处理方式，0: 按量付费，1: 截断加速
        :type FlowTrunc: int
        :param _DeviceId: 激活后的设备ID
        :type DeviceId: str
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
        self._FlowTrunc = None
        self._DeviceId = None

    @property
    def Vendor(self):
        r"""厂商名称
        :rtype: str
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def SN(self):
        r"""设备SN序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Description(self):
        r"""备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DataKey(self):
        r"""设备密钥
        :rtype: str
        """
        return self._DataKey

    @DataKey.setter
    def DataKey(self, DataKey):
        self._DataKey = DataKey

    @property
    def AccessScope(self):
        r"""接入环境。0：公有云网关；1：自有网关；2：公有云网关和自有网关。不填默认公有云网关。 具体含义： 公有云网关：即该设备只能接入公有云网关（就近接入） 自有网关：即该设备只能接入已经注册上线的自有网关（就近接入或固定ip接入） 公有云网关和自有网关：即该设备同时可以接入公有云网关和已经注册上线的自有网关（就近接入或固定ip接入）
        :rtype: int
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def LicensePayMode(self):
        r"""当付费方为租户时，可选择租户license付费方式：
0，月度授权
1，永久授权
若不传则默认为月度授权。
当付费方为厂商时，此参数无效

        :rtype: int
        """
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def GroupId(self):
        r"""设备分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""设备分组名称，预留参数，需要分组时传入GroupId
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def FlowTrunc(self):
        r"""设备无流量包处理方式，0: 按量付费，1: 截断加速
        :rtype: int
        """
        return self._FlowTrunc

    @FlowTrunc.setter
    def FlowTrunc(self, FlowTrunc):
        self._FlowTrunc = FlowTrunc

    @property
    def DeviceId(self):
        r"""激活后的设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


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
        self._FlowTrunc = params.get("FlowTrunc")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateHardwareRequest(AbstractModel):
    r"""ActivateHardware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Hardware: 待激活的设备列表
        :type Hardware: list of ActivateHardware
        """
        self._Hardware = None

    @property
    def Hardware(self):
        r"""待激活的设备列表
        :rtype: list of ActivateHardware
        """
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
    r"""ActivateHardware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HardwareInfo: 完成激活的设备信息
        :type HardwareInfo: list of ActivateHardware
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HardwareInfo = None
        self._RequestId = None

    @property
    def HardwareInfo(self):
        r"""完成激活的设备信息
        :rtype: list of ActivateHardware
        """
        return self._HardwareInfo

    @HardwareInfo.setter
    def HardwareInfo(self, HardwareInfo):
        self._HardwareInfo = HardwareInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class ActiveDeviceList(AbstractModel):
    r"""激活设备数统计

    """

    def __init__(self):
        r"""
        :param _Count: 数量
        :type Count: int
        :param _Time: 时间
        :type Time: str
        """
        self._Count = None
        self._Time = None

    @property
    def Count(self):
        r"""数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Time(self):
        r"""时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceRequest(AbstractModel):
    r"""AddDevice请求参数结构体

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
若不传则默认为月度授权，永久授权设备需要调用OrderPerLicense接口支付授权费，否则设备无法使用
        :type LicensePayMode: int
        :param _GroupName: 设备分组名称，非必选，预留参数，需要分组时传入GroupId
        :type GroupName: str
        :param _GroupId: 设备分组ID，非必选，如果不填写则默认设备无分组
        :type GroupId: str
        :param _FlowTrunc: 设备无流量包处理方式，0: 按量付费，1: 截断加速
        :type FlowTrunc: int
        """
        self._DeviceName = None
        self._Remark = None
        self._DataKey = None
        self._Encrypted = None
        self._AccessScope = None
        self._LicensePayMode = None
        self._GroupName = None
        self._GroupId = None
        self._FlowTrunc = None

    @property
    def DeviceName(self):
        r"""新建设备的名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Remark(self):
        r"""新建设备的备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DataKey(self):
        r"""新建设备的base64密钥字符串，非必选，如果不填写则由系统自动生成
        :rtype: str
        """
        return self._DataKey

    @DataKey.setter
    def DataKey(self, DataKey):
        self._DataKey = DataKey

    @property
    def Encrypted(self):
        r"""是否设置预置密钥
        :rtype: bool
        """
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

    @property
    def AccessScope(self):
        r"""接入环境。0：公有云网关；1：自有网关；2：公有云网关和自有网关。不填默认公有云网关。
具体含义：
公有云网关：即该设备只能接入公有云网关（就近接入）
自有网关：即该设备只能接入已经注册上线的自有网关（就近接入或固定ip接入）
公有云网关和自有网关：即该设备同时可以接入公有云网关和已经注册上线的自有网关（就近接入或固定ip接入）
        :rtype: int
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def LicensePayMode(self):
        r"""license付费方式： 
0，月度授权 
1，永久授权 
若不传则默认为月度授权，永久授权设备需要调用OrderPerLicense接口支付授权费，否则设备无法使用
        :rtype: int
        """
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def GroupName(self):
        r"""设备分组名称，非必选，预留参数，需要分组时传入GroupId
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        r"""设备分组ID，非必选，如果不填写则默认设备无分组
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def FlowTrunc(self):
        r"""设备无流量包处理方式，0: 按量付费，1: 截断加速
        :rtype: int
        """
        return self._FlowTrunc

    @FlowTrunc.setter
    def FlowTrunc(self, FlowTrunc):
        self._FlowTrunc = FlowTrunc


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Remark = params.get("Remark")
        self._DataKey = params.get("DataKey")
        self._Encrypted = params.get("Encrypted")
        self._AccessScope = params.get("AccessScope")
        self._LicensePayMode = params.get("LicensePayMode")
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._FlowTrunc = params.get("FlowTrunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceResponse(AbstractModel):
    r"""AddDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataKey: 经过加密算法加密后的base64格式密钥
        :type DataKey: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _Signature: 签名字符串
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
        r"""经过加密算法加密后的base64格式密钥
        :rtype: str
        """
        return self._DataKey

    @DataKey.setter
    def DataKey(self, DataKey):
        self._DataKey = DataKey

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Signature(self):
        r"""签名字符串
        :rtype: str
        """
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataKey = params.get("DataKey")
        self._DeviceId = params.get("DeviceId")
        self._Signature = params.get("Signature")
        self._RequestId = params.get("RequestId")


class AddGroupRequest(AbstractModel):
    r"""AddGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 分组的名称
        :type GroupName: str
        :param _Description: 分组的描述
        :type Description: str
        """
        self._GroupName = None
        self._Description = None

    @property
    def GroupName(self):
        r"""分组的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        r"""分组的描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddGroupResponse(AbstractModel):
    r"""AddGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组的唯一ID，仅做分组唯一区分
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""分组的唯一ID，仅做分组唯一区分
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class AddHardwareRequest(AbstractModel):
    r"""AddHardware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Hardware: 硬件列表
        :type Hardware: list of Hardware
        """
        self._Hardware = None

    @property
    def Hardware(self):
        r"""硬件列表
        :rtype: list of Hardware
        """
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
    r"""AddHardware返回参数结构体

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
        r"""硬件设备
        :rtype: list of Hardware
        """
        return self._Hardware

    @Hardware.setter
    def Hardware(self, Hardware):
        self._Hardware = Hardware

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class AddL3ConnRequest(AbstractModel):
    r"""AddL3Conn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cidr1: 设置互通网段CIDR1，支持： 10.0.0.0 - 10.255.255.255，172.16.0.0 - 172.31.255.255，192.168.0.0 - 192.168.255.255
        :type Cidr1: str
        :param _Cidr2: 设置互通网段CIDR2，支持： 10.0.0.0 - 10.255.255.255，172.16.0.0 - 172.31.255.255，192.168.0.0 - 192.168.255.255
        :type Cidr2: str
        :param _DeviceId1: CIDR1对应的设备ID
        :type DeviceId1: str
        :param _DeviceId2: CIDR2对应的设备ID
        :type DeviceId2: str
        :param _Description: 规则描述
        :type Description: str
        """
        self._Cidr1 = None
        self._Cidr2 = None
        self._DeviceId1 = None
        self._DeviceId2 = None
        self._Description = None

    @property
    def Cidr1(self):
        r"""设置互通网段CIDR1，支持： 10.0.0.0 - 10.255.255.255，172.16.0.0 - 172.31.255.255，192.168.0.0 - 192.168.255.255
        :rtype: str
        """
        return self._Cidr1

    @Cidr1.setter
    def Cidr1(self, Cidr1):
        self._Cidr1 = Cidr1

    @property
    def Cidr2(self):
        r"""设置互通网段CIDR2，支持： 10.0.0.0 - 10.255.255.255，172.16.0.0 - 172.31.255.255，192.168.0.0 - 192.168.255.255
        :rtype: str
        """
        return self._Cidr2

    @Cidr2.setter
    def Cidr2(self, Cidr2):
        self._Cidr2 = Cidr2

    @property
    def DeviceId1(self):
        r"""CIDR1对应的设备ID
        :rtype: str
        """
        return self._DeviceId1

    @DeviceId1.setter
    def DeviceId1(self, DeviceId1):
        self._DeviceId1 = DeviceId1

    @property
    def DeviceId2(self):
        r"""CIDR2对应的设备ID
        :rtype: str
        """
        return self._DeviceId2

    @DeviceId2.setter
    def DeviceId2(self, DeviceId2):
        self._DeviceId2 = DeviceId2

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Cidr1 = params.get("Cidr1")
        self._Cidr2 = params.get("Cidr2")
        self._DeviceId1 = params.get("DeviceId1")
        self._DeviceId2 = params.get("DeviceId2")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddL3ConnResponse(AbstractModel):
    r"""AddL3Conn返回参数结构体

    """

    def __init__(self):
        r"""
        :param _L3ConnId: 互通规则ID
        :type L3ConnId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._L3ConnId = None
        self._RequestId = None

    @property
    def L3ConnId(self):
        r"""互通规则ID
        :rtype: str
        """
        return self._L3ConnId

    @L3ConnId.setter
    def L3ConnId(self, L3ConnId):
        self._L3ConnId = L3ConnId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._L3ConnId = params.get("L3ConnId")
        self._RequestId = params.get("RequestId")


class CreateEncryptedKeyRequest(AbstractModel):
    r"""CreateEncryptedKey请求参数结构体

    """


class CreateEncryptedKeyResponse(AbstractModel):
    r"""CreateEncryptedKey返回参数结构体

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
        r"""预置密钥
        :rtype: str
        """
        return self._EncryptedKey

    @EncryptedKey.setter
    def EncryptedKey(self, EncryptedKey):
        self._EncryptedKey = EncryptedKey

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptedKey = params.get("EncryptedKey")
        self._RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    r"""DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 删除设备的唯一ID
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        r"""删除设备的唯一ID
        :rtype: str
        """
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
    r"""DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    r"""DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 删除指定分组
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        r"""删除指定分组
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    r"""DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteL3ConnRequest(AbstractModel):
    r"""DeleteL3Conn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _L3ConnIdList: 互通规则ID列表
        :type L3ConnIdList: list of str
        """
        self._L3ConnIdList = None

    @property
    def L3ConnIdList(self):
        r"""互通规则ID列表
        :rtype: list of str
        """
        return self._L3ConnIdList

    @L3ConnIdList.setter
    def L3ConnIdList(self, L3ConnIdList):
        self._L3ConnIdList = L3ConnIdList


    def _deserialize(self, params):
        self._L3ConnIdList = params.get("L3ConnIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL3ConnResponse(AbstractModel):
    r"""DeleteL3Conn返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeviceBaseInfo(AbstractModel):
    r"""设备的基本信息

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
        :type LicensePayMode: int
        :param _Payer: 付费方 0：厂商付费 1：客户付费
        :type Payer: int
        :param _GroupId: 设备分组ID
        :type GroupId: str
        :param _GroupName: 设备分组名称
        :type GroupName: str
        :param _FlowTrunc: 设备无流量包处理方式，0: 按量付费，1: 截断加速
        :type FlowTrunc: int
        :param _Sn: 设备sn
        :type Sn: str
        :param _Vendor: 厂商
        :type Vendor: str
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
        self._FlowTrunc = None
        self._Sn = None
        self._Vendor = None

    @property
    def DeviceId(self):
        r"""设备唯一ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def CreateTime(self):
        r"""设备创建的时间，单位：ms
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastTime(self):
        r"""设备最后在线时间，单位：ms
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def Remark(self):
        r"""设备的备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AccessScope(self):
        r"""接入环境。0：公有云网关；1：自有网关；2：公有云网关和自有网关。默认公有云网关。 具体含义： 公有云网关：即该设备只能接入公有云网关（就近接入） 自有网关：即该设备只能接入已经注册上线的自有网关（就近接入或固定ip接入） 公有云网关和自有网关：即该设备同时可以接入公有云网关和已经注册上线的自有网关（就近接入或固定ip接入）
        :rtype: int
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def LicensePayMode(self):
        r"""license授权有效期 0：月度授权 1：永久授权
        :rtype: int
        """
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def Payer(self):
        r"""付费方 0：厂商付费 1：客户付费
        :rtype: int
        """
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def GroupId(self):
        r"""设备分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""设备分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def FlowTrunc(self):
        r"""设备无流量包处理方式，0: 按量付费，1: 截断加速
        :rtype: int
        """
        return self._FlowTrunc

    @FlowTrunc.setter
    def FlowTrunc(self, FlowTrunc):
        self._FlowTrunc = FlowTrunc

    @property
    def Sn(self):
        r"""设备sn
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def Vendor(self):
        r"""厂商
        :rtype: str
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor


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
        self._FlowTrunc = params.get("FlowTrunc")
        self._Sn = params.get("Sn")
        self._Vendor = params.get("Vendor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDetails(AbstractModel):
    r"""设备详细信息

    """

    def __init__(self):
        r"""
        :param _DeviceBaseInfo: 设备基本信息
        :type DeviceBaseInfo: :class:`tencentcloud.mna.v20210119.models.DeviceBaseInfo`
        :param _DeviceNetInfo: 设备网络信息
        :type DeviceNetInfo: list of DeviceNetInfo
        :param _GatewaySite: 聚合服务器地址
        :type GatewaySite: str
        :param _BusinessDownRate: 业务下行速率
        :type BusinessDownRate: float
        :param _BusinessUpRate: 业务上行速率
        :type BusinessUpRate: float
        """
        self._DeviceBaseInfo = None
        self._DeviceNetInfo = None
        self._GatewaySite = None
        self._BusinessDownRate = None
        self._BusinessUpRate = None

    @property
    def DeviceBaseInfo(self):
        r"""设备基本信息
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeviceBaseInfo`
        """
        return self._DeviceBaseInfo

    @DeviceBaseInfo.setter
    def DeviceBaseInfo(self, DeviceBaseInfo):
        self._DeviceBaseInfo = DeviceBaseInfo

    @property
    def DeviceNetInfo(self):
        r"""设备网络信息
        :rtype: list of DeviceNetInfo
        """
        return self._DeviceNetInfo

    @DeviceNetInfo.setter
    def DeviceNetInfo(self, DeviceNetInfo):
        self._DeviceNetInfo = DeviceNetInfo

    @property
    def GatewaySite(self):
        r"""聚合服务器地址
        :rtype: str
        """
        return self._GatewaySite

    @GatewaySite.setter
    def GatewaySite(self, GatewaySite):
        self._GatewaySite = GatewaySite

    @property
    def BusinessDownRate(self):
        r"""业务下行速率
        :rtype: float
        """
        return self._BusinessDownRate

    @BusinessDownRate.setter
    def BusinessDownRate(self, BusinessDownRate):
        self._BusinessDownRate = BusinessDownRate

    @property
    def BusinessUpRate(self):
        r"""业务上行速率
        :rtype: float
        """
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
        


class DeviceNetInfo(AbstractModel):
    r"""设备网络状态信息

    """

    def __init__(self):
        r"""
        :param _Type: 网络类型：
0:数据
1:Wi-Fi
2:有线
        :type Type: int
        :param _DataEnable: 启用/禁用
        :type DataEnable: bool
        :param _UploadLimit: 上行限速
        :type UploadLimit: str
        :param _DownloadLimit: 下行限速
        :type DownloadLimit: str
        :param _DataRx: 接收实时速率
        :type DataRx: int
        :param _DataTx: 发送实时速率
        :type DataTx: int
        :param _Vendor: 运营商类型：
1: 中国移动；
2: 中国电信; 
3: 中国联通
        :type Vendor: int
        :param _State: 连接状态：
0:无连接
1:连接中
2:已连接
        :type State: int
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _SignalStrength: 信号强度/单位：dbm
        :type SignalStrength: int
        :param _Rat: 数据网络类型：
-1 ：无效值   
2：2G 
3：3G 
4：4G 
5：5G
        :type Rat: int
        :param _NetInfoName: 网卡名
        :type NetInfoName: str
        :param _DownRate: 下行实时速率（浮点数类型代替上一版本DataRx的整型）
        :type DownRate: float
        :param _UpRate: 上行实时速率（浮点数类型代替上一版本TxRate的整型）
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
        r"""网络类型：
0:数据
1:Wi-Fi
2:有线
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DataEnable(self):
        r"""启用/禁用
        :rtype: bool
        """
        return self._DataEnable

    @DataEnable.setter
    def DataEnable(self, DataEnable):
        self._DataEnable = DataEnable

    @property
    def UploadLimit(self):
        r"""上行限速
        :rtype: str
        """
        return self._UploadLimit

    @UploadLimit.setter
    def UploadLimit(self, UploadLimit):
        self._UploadLimit = UploadLimit

    @property
    def DownloadLimit(self):
        r"""下行限速
        :rtype: str
        """
        return self._DownloadLimit

    @DownloadLimit.setter
    def DownloadLimit(self, DownloadLimit):
        self._DownloadLimit = DownloadLimit

    @property
    def DataRx(self):
        r"""接收实时速率
        :rtype: int
        """
        return self._DataRx

    @DataRx.setter
    def DataRx(self, DataRx):
        self._DataRx = DataRx

    @property
    def DataTx(self):
        r"""发送实时速率
        :rtype: int
        """
        return self._DataTx

    @DataTx.setter
    def DataTx(self, DataTx):
        self._DataTx = DataTx

    @property
    def Vendor(self):
        r"""运营商类型：
1: 中国移动；
2: 中国电信; 
3: 中国联通
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def State(self):
        r"""连接状态：
0:无连接
1:连接中
2:已连接
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PublicIp(self):
        r"""公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def SignalStrength(self):
        r"""信号强度/单位：dbm
        :rtype: int
        """
        return self._SignalStrength

    @SignalStrength.setter
    def SignalStrength(self, SignalStrength):
        self._SignalStrength = SignalStrength

    @property
    def Rat(self):
        r"""数据网络类型：
-1 ：无效值   
2：2G 
3：3G 
4：4G 
5：5G
        :rtype: int
        """
        return self._Rat

    @Rat.setter
    def Rat(self, Rat):
        self._Rat = Rat

    @property
    def NetInfoName(self):
        r"""网卡名
        :rtype: str
        """
        return self._NetInfoName

    @NetInfoName.setter
    def NetInfoName(self, NetInfoName):
        self._NetInfoName = NetInfoName

    @property
    def DownRate(self):
        r"""下行实时速率（浮点数类型代替上一版本DataRx的整型）
        :rtype: float
        """
        return self._DownRate

    @DownRate.setter
    def DownRate(self, DownRate):
        self._DownRate = DownRate

    @property
    def UpRate(self):
        r"""上行实时速率（浮点数类型代替上一版本TxRate的整型）
        :rtype: float
        """
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
    r"""设备付费模式信息

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
        :type ResourceId: str
        """
        self._DeviceId = None
        self._PayMode = None
        self._PayModeDesc = None
        self._ResourceId = None

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def PayMode(self):
        r"""付费模式。
1：预付费流量包
0：按流量后付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeDesc(self):
        r"""付费模式描述
        :rtype: str
        """
        return self._PayModeDesc

    @PayModeDesc.setter
    def PayModeDesc(self, PayModeDesc):
        self._PayModeDesc = PayModeDesc

    @property
    def ResourceId(self):
        r"""流量包ID，仅当付费模式为流量包类型时才有。
        :rtype: str
        """
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
        


class DownloadActiveDeviceCountRequest(AbstractModel):
    r"""DownloadActiveDeviceCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 查询粒度。0:day, 1:week, 2:month, 不传默认为day
        :type Period: int
        :param _StartTime: 开始时间。单位秒
        :type StartTime: int
        :param _EndTime: 结束时间。单位秒
        :type EndTime: int
        :param _DevGroup: 设备组, 不传查询全部
        :type DevGroup: str
        :param _LicenseType: license类型, 不传查询全部, 1: 租户月付，2：厂商月付，3：永久授权
        :type LicenseType: int
        """
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._DevGroup = None
        self._LicenseType = None

    @property
    def Period(self):
        r"""查询粒度。0:day, 1:week, 2:month, 不传默认为day
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""开始时间。单位秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。单位秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DevGroup(self):
        r"""设备组, 不传查询全部
        :rtype: str
        """
        return self._DevGroup

    @DevGroup.setter
    def DevGroup(self, DevGroup):
        self._DevGroup = DevGroup

    @property
    def LicenseType(self):
        r"""license类型, 不传查询全部, 1: 租户月付，2：厂商月付，3：永久授权
        :rtype: int
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DevGroup = params.get("DevGroup")
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadActiveDeviceCountResponse(AbstractModel):
    r"""DownloadActiveDeviceCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FilePath: URL地址
        :type FilePath: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FilePath = None
        self._RequestId = None

    @property
    def FilePath(self):
        r"""URL地址
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FilePath = params.get("FilePath")
        self._RequestId = params.get("RequestId")


class FlowDetails(AbstractModel):
    r"""设备流量信息

    """

    def __init__(self):
        r"""
        :param _NetDetails: 流量数据点
        :type NetDetails: list of NetDetails
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _MaxValue: 流量最大值（单位：bytes）
        :type MaxValue: float
        :param _AvgValue: 流量平均值（单位：bytes）
        :type AvgValue: float
        :param _TotalValue: 流量总值（单位：bytes）
        :type TotalValue: float
        """
        self._NetDetails = None
        self._DeviceId = None
        self._MaxValue = None
        self._AvgValue = None
        self._TotalValue = None

    @property
    def NetDetails(self):
        r"""流量数据点
        :rtype: list of NetDetails
        """
        return self._NetDetails

    @NetDetails.setter
    def NetDetails(self, NetDetails):
        self._NetDetails = NetDetails

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def MaxValue(self):
        r"""流量最大值（单位：bytes）
        :rtype: float
        """
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def AvgValue(self):
        r"""流量平均值（单位：bytes）
        :rtype: float
        """
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def TotalValue(self):
        r"""流量总值（单位：bytes）
        :rtype: float
        """
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
    r"""流量包信息

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
        r"""流量包的唯一资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        r"""流量包所属的用户AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageType(self):
        r"""流量包规格类型。可取值如下：
DEVICE_1_FLOW_20G、DEVICE_2_FLOW_50G、
DEVICE_3_FLOW_100G、
DEVICE_5_FLOW_500G，分别代表20G、50G、100G、500G档位的流量包。
档位也影响流量包可绑定的设备数量上限：
20G：最多绑定1个设备
50G：最多绑定2个设备
100G：最多绑定3个设备
500G：最多绑定5个设备
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Status(self):
        r"""流量包状态，0：未生效，1：有效期内，2：已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""购买时间，Unix时间戳格式，单位：秒
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ActiveTime(self):
        r"""生效时间，Unix时间戳格式，单位：秒
        :rtype: int
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def ExpireTime(self):
        r"""过期时间，Unix时间戳格式，单位：秒
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeviceList(self):
        r"""流量包绑定的设备ID列表
        :rtype: list of str
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def CapacitySize(self):
        r"""流量包总容量，单位：MB
        :rtype: int
        """
        return self._CapacitySize

    @CapacitySize.setter
    def CapacitySize(self, CapacitySize):
        self._CapacitySize = CapacitySize

    @property
    def CapacityRemain(self):
        r"""流量包余量，单位：MB
        :rtype: int
        """
        return self._CapacityRemain

    @CapacityRemain.setter
    def CapacityRemain(self, CapacityRemain):
        self._CapacityRemain = CapacityRemain

    @property
    def RenewFlag(self):
        r"""自动续费标识。true代表自动续费，false代表不自动续费
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ModifyStatus(self):
        r"""资源包变更状态，0：未发生变配；1：变配中；2：已变配或已续费
        :rtype: int
        """
        return self._ModifyStatus

    @ModifyStatus.setter
    def ModifyStatus(self, ModifyStatus):
        self._ModifyStatus = ModifyStatus

    @property
    def TruncFlag(self):
        r"""流量截断标识。true代表开启流量截断，false代表不开启流量截断
        :rtype: bool
        """
        return self._TruncFlag

    @TruncFlag.setter
    def TruncFlag(self, TruncFlag):
        self._TruncFlag = TruncFlag

    @property
    def CapacityRemainPrecise(self):
        r"""流量包精确余量，单位：MB
        :rtype: int
        """
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
        


class GetActiveDeviceCountRequest(AbstractModel):
    r"""GetActiveDeviceCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 查询粒度。0:day, 1:week, 2:month, 不传默认为day
        :type Period: int
        :param _StartTime: 开始时间。单位秒
        :type StartTime: int
        :param _EndTime: 结束时间。单位秒
        :type EndTime: int
        :param _DevGroup: 设备组, 不传查询全部
        :type DevGroup: str
        :param _LicenseType: license类型, 不传查询全部, 1: 租户月付，2：厂商月付，3：永久授权
        :type LicenseType: int
        """
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._DevGroup = None
        self._LicenseType = None

    @property
    def Period(self):
        r"""查询粒度。0:day, 1:week, 2:month, 不传默认为day
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""开始时间。单位秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。单位秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DevGroup(self):
        r"""设备组, 不传查询全部
        :rtype: str
        """
        return self._DevGroup

    @DevGroup.setter
    def DevGroup(self, DevGroup):
        self._DevGroup = DevGroup

    @property
    def LicenseType(self):
        r"""license类型, 不传查询全部, 1: 租户月付，2：厂商月付，3：永久授权
        :rtype: int
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DevGroup = params.get("DevGroup")
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetActiveDeviceCountResponse(AbstractModel):
    r"""GetActiveDeviceCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActiveDeviceList: 激活设备统计
        :type ActiveDeviceList: list of ActiveDeviceList
        :param _Period: 查询粒度，0:day, 1:week, 2:month, 不传默认为day
        :type Period: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _DevGroup: 设备组
        :type DevGroup: str
        :param _LicenseType: license类型, 不传查询全部, 1: 租户月付，2：厂商月付，3：永久授权
        :type LicenseType: str
        :param _AppId: 租户ID
        :type AppId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActiveDeviceList = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._DevGroup = None
        self._LicenseType = None
        self._AppId = None
        self._RequestId = None

    @property
    def ActiveDeviceList(self):
        r"""激活设备统计
        :rtype: list of ActiveDeviceList
        """
        return self._ActiveDeviceList

    @ActiveDeviceList.setter
    def ActiveDeviceList(self, ActiveDeviceList):
        self._ActiveDeviceList = ActiveDeviceList

    @property
    def Period(self):
        r"""查询粒度，0:day, 1:week, 2:month, 不传默认为day
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DevGroup(self):
        r"""设备组
        :rtype: str
        """
        return self._DevGroup

    @DevGroup.setter
    def DevGroup(self, DevGroup):
        self._DevGroup = DevGroup

    @property
    def LicenseType(self):
        r"""license类型, 不传查询全部, 1: 租户月付，2：厂商月付，3：永久授权
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def AppId(self):
        r"""租户ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActiveDeviceList") is not None:
            self._ActiveDeviceList = []
            for item in params.get("ActiveDeviceList"):
                obj = ActiveDeviceList()
                obj._deserialize(item)
                self._ActiveDeviceList.append(obj)
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DevGroup = params.get("DevGroup")
        self._LicenseType = params.get("LicenseType")
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class GetDevicePayModeRequest(AbstractModel):
    r"""GetDevicePayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIdList: 设备ID列表
        :type DeviceIdList: list of str
        """
        self._DeviceIdList = None

    @property
    def DeviceIdList(self):
        r"""设备ID列表
        :rtype: list of str
        """
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
    r"""GetDevicePayMode返回参数结构体

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
        r"""结果信息
        :rtype: list of DevicePayModeInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 搜索指定设备的id
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        r"""搜索指定设备的id
        :rtype: str
        """
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
    r"""GetDevice返回参数结构体

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
        r"""设备详细信息
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeviceDetails`
        """
        return self._DeviceDetails

    @DeviceDetails.setter
    def DeviceDetails(self, DeviceDetails):
        self._DeviceDetails = DeviceDetails

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetDevices请求参数结构体

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
        r"""每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前查看页码，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        r"""搜索设备的关键字（ID或者设备名），为空时匹配所有设备
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DeviceType(self):
        r"""DeviceType
不传：返回所有设备；
1:自有设备；
2:三方设备
        :rtype: int
        """
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
    r"""GetDevices返回参数结构体

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
        r"""设备信息列表
        :rtype: list of DeviceBaseInfo
        """
        return self._DeviceInfos

    @DeviceInfos.setter
    def DeviceInfos(self, DeviceInfos):
        self._DeviceInfos = DeviceInfos

    @property
    def Length(self):
        r"""设备总记录条数
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetFlowAlarmInfo请求参数结构体

    """


class GetFlowAlarmInfoResponse(AbstractModel):
    r"""GetFlowAlarmInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmValue: 流量包的告警阈值
        :type AlarmValue: int
        :param _NotifyUrl: 告警通知回调url
        :type NotifyUrl: str
        :param _CallbackKey: 告警通知回调key
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
        r"""流量包的告警阈值
        :rtype: int
        """
        return self._AlarmValue

    @AlarmValue.setter
    def AlarmValue(self, AlarmValue):
        self._AlarmValue = AlarmValue

    @property
    def NotifyUrl(self):
        r"""告警通知回调url
        :rtype: str
        """
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def CallbackKey(self):
        r"""告警通知回调key
        :rtype: str
        """
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetFlowPackages请求参数结构体

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
        r"""页码，从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ResourceId(self):
        r"""流量包的唯一资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DeviceId(self):
        r"""流量包绑定的设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        r"""流量包状态，0：未生效，1：有效期内，2：已过期

        :rtype: int
        """
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
    r"""GetFlowPackages返回参数结构体

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
        r"""流量包列表
        :rtype: list of FlowPackageInfo
        """
        return self._PackageList

    @PackageList.setter
    def PackageList(self, PackageList):
        self._PackageList = PackageList

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetFlowStatisticByGroup请求参数结构体

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
        :param _MpApplicationId: 应用ID, 查询分组流量时无需使用。 查询应用流量时该字段为应用ID，GroupId 填写 "-1"
        :type MpApplicationId: str
        """
        self._GroupId = None
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None
        self._AccessRegion = None
        self._GatewayType = None
        self._MpApplicationId = None

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def BeginTime(self):
        r"""开始查找时间
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""截止时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""流量种类（1：上行流量，2：下行流量， 3: 上下行总和）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeGranularity(self):
        r"""时间粒度（1：按小时统计，2：按天统计）
        :rtype: int
        """
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity

    @property
    def AccessRegion(self):
        r"""接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        r"""网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :rtype: int
        """
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def MpApplicationId(self):
        r"""应用ID, 查询分组流量时无需使用。 查询应用流量时该字段为应用ID，GroupId 填写 "-1"
        :rtype: str
        """
        return self._MpApplicationId

    @MpApplicationId.setter
    def MpApplicationId(self, MpApplicationId):
        self._MpApplicationId = MpApplicationId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        self._AccessRegion = params.get("AccessRegion")
        self._GatewayType = params.get("GatewayType")
        self._MpApplicationId = params.get("MpApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFlowStatisticByGroupResponse(AbstractModel):
    r"""GetFlowStatisticByGroup返回参数结构体

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
        r"""流量详细信息
        :rtype: list of NetDetails
        """
        return self._NetDetails

    @NetDetails.setter
    def NetDetails(self, NetDetails):
        self._NetDetails = NetDetails

    @property
    def MaxValue(self):
        r"""查找时间段流量使用最大值（单位：byte）
        :rtype: float
        """
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def AvgValue(self):
        r"""查找时间段流量使用平均值（单位：byte）
        :rtype: float
        """
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def TotalValue(self):
        r"""查找时间段流量使用总量（单位：byte）
        :rtype: float
        """
        return self._TotalValue

    @TotalValue.setter
    def TotalValue(self, TotalValue):
        self._TotalValue = TotalValue

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class GetFlowStatisticByRegionRequest(AbstractModel):
    r"""GetFlowStatisticByRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 开始查找时间
        :type BeginTime: int
        :param _EndTime: 截止时间
        :type EndTime: int
        :param _Type: 流量种类（1：上行流量，2：下行流量， 3: 上下行总和）
        :type Type: int
        :param _TimeGranularity: 时间粒度（1：按小时统计，2：按天统计）
        :type TimeGranularity: int
        :param _GatewayType: 网关类型。0：公有云网关；1：自有网关。 
        :type GatewayType: int
        :param _AccessRegion: 接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :type AccessRegion: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._Type = None
        self._TimeGranularity = None
        self._GatewayType = None
        self._AccessRegion = None

    @property
    def BeginTime(self):
        r"""开始查找时间
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""截止时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""流量种类（1：上行流量，2：下行流量， 3: 上下行总和）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeGranularity(self):
        r"""时间粒度（1：按小时统计，2：按天统计）
        :rtype: int
        """
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity

    @property
    def GatewayType(self):
        r"""网关类型。0：公有云网关；1：自有网关。 
        :rtype: int
        """
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def AccessRegion(self):
        r"""接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimeGranularity = params.get("TimeGranularity")
        self._GatewayType = params.get("GatewayType")
        self._AccessRegion = params.get("AccessRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFlowStatisticByRegionResponse(AbstractModel):
    r"""GetFlowStatisticByRegion返回参数结构体

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
        r"""流量详细信息
        :rtype: list of NetDetails
        """
        return self._NetDetails

    @NetDetails.setter
    def NetDetails(self, NetDetails):
        self._NetDetails = NetDetails

    @property
    def MaxValue(self):
        r"""查找时间段流量使用最大值（单位：byte）
        :rtype: float
        """
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def AvgValue(self):
        r"""查找时间段流量使用平均值（单位：byte）
        :rtype: float
        """
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def TotalValue(self):
        r"""查找时间段流量使用总量（单位：byte）
        :rtype: float
        """
        return self._TotalValue

    @TotalValue.setter
    def TotalValue(self, TotalValue):
        self._TotalValue = TotalValue

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetFlowStatistic请求参数结构体

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
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BeginTime(self):
        r"""开始查找时间
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""截止时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""流量种类（1：上行流量，2：下行流量，3：上下行总和）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeGranularity(self):
        r"""时间粒度（1：按小时统计，2：按天统计）
        :rtype: int
        """
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity

    @property
    def AccessRegion(self):
        r"""接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        r"""网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :rtype: int
        """
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def DeviceList(self):
        r"""设备ID列表，用于查询多设备流量，该字段启用时DeviceId可传"-1"
        :rtype: list of str
        """
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
    r"""GetFlowStatistic返回参数结构体

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
        r"""流量详细信息
        :rtype: list of NetDetails
        """
        return self._NetDetails

    @NetDetails.setter
    def NetDetails(self, NetDetails):
        self._NetDetails = NetDetails

    @property
    def MaxValue(self):
        r"""查找时间段流量使用最大值（单位：byte）
        :rtype: float
        """
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def AvgValue(self):
        r"""查找时间段流量使用平均值（单位：byte）
        :rtype: float
        """
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def TotalValue(self):
        r"""查找时间段流量使用总量（单位：byte）
        :rtype: float
        """
        return self._TotalValue

    @TotalValue.setter
    def TotalValue(self, TotalValue):
        self._TotalValue = TotalValue

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class GetGroupDetailRequest(AbstractModel):
    r"""GetGroupDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _PageSize: 每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备	
        :type PageSize: int
        :param _PageNumber: 每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备	
        :type PageNumber: int
        :param _KeyWord: 搜索关键字
        :type KeyWord: str
        """
        self._GroupId = None
        self._PageSize = None
        self._PageNumber = None
        self._KeyWord = None

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PageSize(self):
        r"""每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备	
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备	
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def KeyWord(self):
        r"""搜索关键字
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupDetailResponse(AbstractModel):
    r"""GetGroupDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfo: 分组基本信息
        :type GroupInfo: :class:`tencentcloud.mna.v20210119.models.GroupInfo`
        :param _DeviceInfos: 分组中设备列表
        :type DeviceInfos: list of DeviceBaseInfo
        :param _Length: 设备总记录条数
        :type Length: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfo = None
        self._DeviceInfos = None
        self._Length = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def GroupInfo(self):
        r"""分组基本信息
        :rtype: :class:`tencentcloud.mna.v20210119.models.GroupInfo`
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

    @property
    def DeviceInfos(self):
        r"""分组中设备列表
        :rtype: list of DeviceBaseInfo
        """
        return self._DeviceInfos

    @DeviceInfos.setter
    def DeviceInfos(self, DeviceInfos):
        self._DeviceInfos = DeviceInfos

    @property
    def Length(self):
        r"""设备总记录条数
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupInfo") is not None:
            self._GroupInfo = GroupInfo()
            self._GroupInfo._deserialize(params.get("GroupInfo"))
        if params.get("DeviceInfos") is not None:
            self._DeviceInfos = []
            for item in params.get("DeviceInfos"):
                obj = DeviceBaseInfo()
                obj._deserialize(item)
                self._DeviceInfos.append(obj)
        self._Length = params.get("Length")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    r"""GetGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :type PageSize: int
        :param _PageNumber: 当前查看页码，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :type PageNumber: int
        :param _Keyword: 搜索分组的关键字，为空时匹配所有分组
        :type Keyword: str
        """
        self._PageSize = None
        self._PageNumber = None
        self._Keyword = None

    @property
    def PageSize(self):
        r"""每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前查看页码，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        r"""搜索分组的关键字，为空时匹配所有分组
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    r"""GetGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfos: 设备信息列表
        :type GroupInfos: list of GroupInfo
        :param _Length: 设备总记录条数
        :type Length: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfos = None
        self._Length = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def GroupInfos(self):
        r"""设备信息列表
        :rtype: list of GroupInfo
        """
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def Length(self):
        r"""设备总记录条数
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        self._Length = params.get("Length")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class GetHardwareListRequest(AbstractModel):
    r"""GetHardwareList请求参数结构体

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
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""页面设备数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""关键字
        :rtype: str
        """
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
    r"""GetHardwareList返回参数结构体

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
        r"""硬件信息列表
        :rtype: list of HardwareInfo
        """
        return self._HardwareInfos

    @HardwareInfos.setter
    def HardwareInfos(self, HardwareInfos):
        self._HardwareInfos = HardwareInfos

    @property
    def Length(self):
        r"""硬件总数
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class GetL3ConnListRequest(AbstractModel):
    r"""GetL3ConnList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :type PageSize: int
        :param _PageNumber: 当前查看页码，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :type PageNumber: int
        :param _DeviceId: 搜索分组的DeviceId，为空时匹配所有分组
        :type DeviceId: str
        """
        self._PageSize = None
        self._PageNumber = None
        self._DeviceId = None

    @property
    def PageSize(self):
        r"""每页显示记录数，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前查看页码，PageSize、PageNumber值均为-1 时，按照1页无限制条数匹配所有设备
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def DeviceId(self):
        r"""搜索分组的DeviceId，为空时匹配所有分组
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetL3ConnListResponse(AbstractModel):
    r"""GetL3ConnList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _L3ConnList: 互通规则列表
        :type L3ConnList: list of L3ConnInfo
        :param _Length: 设备总记录条数
        :type Length: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._L3ConnList = None
        self._Length = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def L3ConnList(self):
        r"""互通规则列表
        :rtype: list of L3ConnInfo
        """
        return self._L3ConnList

    @L3ConnList.setter
    def L3ConnList(self, L3ConnList):
        self._L3ConnList = L3ConnList

    @property
    def Length(self):
        r"""设备总记录条数
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("L3ConnList") is not None:
            self._L3ConnList = []
            for item in params.get("L3ConnList"):
                obj = L3ConnInfo()
                obj._deserialize(item)
                self._L3ConnList.append(obj)
        self._Length = params.get("Length")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class GetMultiFlowStatisticRequest(AbstractModel):
    r"""GetMultiFlowStatistic请求参数结构体

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
        r"""设备id列表，单次最多请求10个设备
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def BeginTime(self):
        r"""1659514436
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""1659515000
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""统计流量类型（1：上行流量，2：下行流量， 3: 上下行总和）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeGranularity(self):
        r"""统计时间粒度（1：按小时统计，2：按天统计）
        :rtype: int
        """
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity

    @property
    def AccessRegion(self):
        r"""接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        r"""网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :rtype: int
        """
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
    r"""GetMultiFlowStatistic返回参数结构体

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
        r"""批量设备流量信息
        :rtype: list of FlowDetails
        """
        return self._FlowDetails

    @FlowDetails.setter
    def FlowDetails(self, FlowDetails):
        self._FlowDetails = FlowDetails

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetNetMonitor请求参数结构体

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
        r"""设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BeginTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metrics(self):
        r"""统计指标（上行速率："TxRate":bit/s，下行速率："RxRate":bit/s，丢包："Loss":%，时延："RTT":ms）
        :rtype: str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def GatewayType(self):
        r"""网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :rtype: int
        """
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
    r"""GetNetMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorData: 监控数据
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
        r"""监控数据
        :rtype: list of MonitorData
        """
        return self._MonitorData

    @MonitorData.setter
    def MonitorData(self, MonitorData):
        self._MonitorData = MonitorData

    @property
    def AccessRegion(self):
        r"""接入区域。取值范围：['MC','AP','EU','AM']
MC=中国大陆
AP=亚太
EU=欧洲
AM=美洲
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""GetPublicKey请求参数结构体

    """


class GetPublicKeyResponse(AbstractModel):
    r"""GetPublicKey返回参数结构体

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
        r"""非对称公钥
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PublicKey = params.get("PublicKey")
        self._RequestId = params.get("RequestId")


class GetStatisticDataRequest(AbstractModel):
    r"""GetStatisticData请求参数结构体

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
        r"""设备ID。若不指定设备，可传"-1"
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BeginTime(self):
        r"""统计开始时间，单位：s
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""统计结束时间，单位：s
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TimeGranularity(self):
        r"""聚合粒度：
1:按小时统计
2:按天统计
        :rtype: int
        """
        return self._TimeGranularity

    @TimeGranularity.setter
    def TimeGranularity(self, TimeGranularity):
        self._TimeGranularity = TimeGranularity

    @property
    def AccessRegion(self):
        r"""接入区域。取值范围：['MC','AP','EU','AM'] MC=中国大陆 AP=亚太 EU=欧洲 AM=美洲。不填代表全量区域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def GatewayType(self):
        r"""网关类型。0：公有云网关；1：自有网关。不传默认为0。
        :rtype: int
        """
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def DeviceList(self):
        r"""设备ID列表，最多10个设备，下载多个设备流量和时使用，此时DeviceId可传"-1"
        :rtype: list of str
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def GroupId(self):
        r"""设备分组ID，若不指定分组则不传，按分组下载数据时使用
        :rtype: str
        """
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
    r"""GetStatisticData返回参数结构体

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
        r"""文件地址url
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FilePath = params.get("FilePath")
        self._RequestId = params.get("RequestId")


class GetVendorHardwareRequest(AbstractModel):
    r"""GetVendorHardware请求参数结构体

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
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""页面数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Status(self):
        r"""激活状态，
空：全部；
1:待激活；
2:已激活；
        :rtype: int
        """
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
    r"""GetVendorHardware返回参数结构体

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
        r"""硬件信息列表
        :rtype: list of VendorHardware
        """
        return self._VendorHardware

    @VendorHardware.setter
    def VendorHardware(self, VendorHardware):
        self._VendorHardware = VendorHardware

    @property
    def Length(self):
        r"""设备总数
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def TotalPage(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class GroupAddDeviceRequest(AbstractModel):
    r"""GroupAddDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _DeviceList: 待添加的设备列表
        :type DeviceList: list of str
        """
        self._GroupId = None
        self._DeviceList = None

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DeviceList(self):
        r"""待添加的设备列表
        :rtype: list of str
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DeviceList = params.get("DeviceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupAddDeviceResponse(AbstractModel):
    r"""GroupAddDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceNum: 分组中的设备数量
        :type DeviceNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceNum = None
        self._RequestId = None

    @property
    def DeviceNum(self):
        r"""分组中的设备数量
        :rtype: int
        """
        return self._DeviceNum

    @DeviceNum.setter
    def DeviceNum(self, DeviceNum):
        self._DeviceNum = DeviceNum

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceNum = params.get("DeviceNum")
        self._RequestId = params.get("RequestId")


class GroupDeleteDeviceRequest(AbstractModel):
    r"""GroupDeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _DeviceList: 待删除的设备列表
        :type DeviceList: list of str
        """
        self._GroupId = None
        self._DeviceList = None

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DeviceList(self):
        r"""待删除的设备列表
        :rtype: list of str
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DeviceList = params.get("DeviceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupDeleteDeviceResponse(AbstractModel):
    r"""GroupDeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceNum: 分组中的设备数量
        :type DeviceNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceNum = None
        self._RequestId = None

    @property
    def DeviceNum(self):
        r"""分组中的设备数量
        :rtype: int
        """
        return self._DeviceNum

    @DeviceNum.setter
    def DeviceNum(self, DeviceNum):
        self._DeviceNum = DeviceNum

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceNum = params.get("DeviceNum")
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    r"""分组的基本信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _GroupName: 分组名
        :type GroupName: str
        :param _CreateTime: 分组创建的时间，单位：ms	
        :type CreateTime: str
        :param _UpdateTime: 分组更新的时间，单位：ms	
        :type UpdateTime: str
        :param _Description: 分组描述
        :type Description: str
        :param _DeviceNum: 分组中的设备数量
        :type DeviceNum: int
        """
        self._GroupId = None
        self._GroupName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Description = None
        self._DeviceNum = None

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""分组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def CreateTime(self):
        r"""分组创建的时间，单位：ms	
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""分组更新的时间，单位：ms	
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Description(self):
        r"""分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DeviceNum(self):
        r"""分组中的设备数量
        :rtype: int
        """
        return self._DeviceNum

    @DeviceNum.setter
    def DeviceNum(self, DeviceNum):
        self._DeviceNum = DeviceNum


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Description = params.get("Description")
        self._DeviceNum = params.get("DeviceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hardware(AbstractModel):
    r"""新建Hardware入参

    """

    def __init__(self):
        r"""
        :param _SN: 硬件序列号
        :type SN: str
        :param _LicenseChargingMode: license计费模式：
1，租户付费
2，厂商月付费
3，厂商永久授权
        :type LicenseChargingMode: int
        :param _Description: 设备描述
        :type Description: str
        :param _HardwareId: 硬件ID，入参无需传递
        :type HardwareId: str
        """
        self._SN = None
        self._LicenseChargingMode = None
        self._Description = None
        self._HardwareId = None

    @property
    def SN(self):
        r"""硬件序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def LicenseChargingMode(self):
        r"""license计费模式：
1，租户付费
2，厂商月付费
3，厂商永久授权
        :rtype: int
        """
        return self._LicenseChargingMode

    @LicenseChargingMode.setter
    def LicenseChargingMode(self, LicenseChargingMode):
        self._LicenseChargingMode = LicenseChargingMode

    @property
    def Description(self):
        r"""设备描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def HardwareId(self):
        r"""硬件ID，入参无需传递
        :rtype: str
        """
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
    r"""硬件信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ActiveTime: 激活时间
        :type ActiveTime: str
        :param _LastOnlineTime: 最后在线时间
        :type LastOnlineTime: str
        :param _Description: 备注
        :type Description: str
        :param _VendorDescription: 厂商备注
        :type VendorDescription: str
        :param _LicenseChargingMode: license计费模式： 1，租户月付费 2，厂商月付费 3，license永久授权
注：后续将废弃此参数，新接入请使用LicensePayMode和Payer
        :type LicenseChargingMode: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _SN: 硬件序列号
        :type SN: str
        :param _LicensePayMode: license授权有效期 
0：月度授权 
1：永久授权
        :type LicensePayMode: int
        :param _Payer: 付费方 
0：客户付费 
1：厂商付费
        :type Payer: int
        :param _GroupId: 设备分组ID
        :type GroupId: str
        :param _GroupName: 设备分组名称
        :type GroupName: str
        :param _FlowTrunc: 设备无流量包处理方式，0: 按量付费，1: 截断加速	
        :type FlowTrunc: int
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
        self._FlowTrunc = None

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ActiveTime(self):
        r"""激活时间
        :rtype: str
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def LastOnlineTime(self):
        r"""最后在线时间
        :rtype: str
        """
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def Description(self):
        r"""备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VendorDescription(self):
        r"""厂商备注
        :rtype: str
        """
        return self._VendorDescription

    @VendorDescription.setter
    def VendorDescription(self, VendorDescription):
        self._VendorDescription = VendorDescription

    @property
    def LicenseChargingMode(self):
        r"""license计费模式： 1，租户月付费 2，厂商月付费 3，license永久授权
注：后续将废弃此参数，新接入请使用LicensePayMode和Payer
        :rtype: int
        """
        return self._LicenseChargingMode

    @LicenseChargingMode.setter
    def LicenseChargingMode(self, LicenseChargingMode):
        self._LicenseChargingMode = LicenseChargingMode

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SN(self):
        r"""硬件序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def LicensePayMode(self):
        r"""license授权有效期 
0：月度授权 
1：永久授权
        :rtype: int
        """
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def Payer(self):
        r"""付费方 
0：客户付费 
1：厂商付费
        :rtype: int
        """
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def GroupId(self):
        r"""设备分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""设备分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def FlowTrunc(self):
        r"""设备无流量包处理方式，0: 按量付费，1: 截断加速	
        :rtype: int
        """
        return self._FlowTrunc

    @FlowTrunc.setter
    def FlowTrunc(self, FlowTrunc):
        self._FlowTrunc = FlowTrunc


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
        self._FlowTrunc = params.get("FlowTrunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L3ConnInfo(AbstractModel):
    r"""三层互通规则信息

    """

    def __init__(self):
        r"""
        :param _L3ConnId: 互通规则ID
        :type L3ConnId: str
        :param _DeviceId1: 互通设备ID
        :type DeviceId1: str
        :param _Cidr1: 互通规则CIDR
        :type Cidr1: str
        :param _DeviceId2: 互通设备ID
        :type DeviceId2: str
        :param _Cidr2: 互通规则CIDR
        :type Cidr2: str
        :param _Enable: 互通规则启用状态
        :type Enable: bool
        :param _Description: 互通规则描述
        :type Description: str
        """
        self._L3ConnId = None
        self._DeviceId1 = None
        self._Cidr1 = None
        self._DeviceId2 = None
        self._Cidr2 = None
        self._Enable = None
        self._Description = None

    @property
    def L3ConnId(self):
        r"""互通规则ID
        :rtype: str
        """
        return self._L3ConnId

    @L3ConnId.setter
    def L3ConnId(self, L3ConnId):
        self._L3ConnId = L3ConnId

    @property
    def DeviceId1(self):
        r"""互通设备ID
        :rtype: str
        """
        return self._DeviceId1

    @DeviceId1.setter
    def DeviceId1(self, DeviceId1):
        self._DeviceId1 = DeviceId1

    @property
    def Cidr1(self):
        r"""互通规则CIDR
        :rtype: str
        """
        return self._Cidr1

    @Cidr1.setter
    def Cidr1(self, Cidr1):
        self._Cidr1 = Cidr1

    @property
    def DeviceId2(self):
        r"""互通设备ID
        :rtype: str
        """
        return self._DeviceId2

    @DeviceId2.setter
    def DeviceId2(self, DeviceId2):
        self._DeviceId2 = DeviceId2

    @property
    def Cidr2(self):
        r"""互通规则CIDR
        :rtype: str
        """
        return self._Cidr2

    @Cidr2.setter
    def Cidr2(self, Cidr2):
        self._Cidr2 = Cidr2

    @property
    def Enable(self):
        r"""互通规则启用状态
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        r"""互通规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._L3ConnId = params.get("L3ConnId")
        self._DeviceId1 = params.get("DeviceId1")
        self._Cidr1 = params.get("Cidr1")
        self._DeviceId2 = params.get("DeviceId2")
        self._Cidr2 = params.get("Cidr2")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPackageRenewFlagRequest(AbstractModel):
    r"""ModifyPackageRenewFlag请求参数结构体

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
        r"""流量包的唯一资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RenewFlag(self):
        r"""自动续费标识。true代表自动续费，false代表不自动续费
        :rtype: bool
        """
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
    r"""ModifyPackageRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorData(AbstractModel):
    r"""流量监控指标

    """

    def __init__(self):
        r"""
        :param _Time: 时间点：s
        :type Time: str
        :param _BusinessMetrics: 业务指标（bps/ms/%）
        :type BusinessMetrics: float
        :param _SlotNetInfo: 网卡状态信息
        :type SlotNetInfo: list of SlotNetInfo
        """
        self._Time = None
        self._BusinessMetrics = None
        self._SlotNetInfo = None

    @property
    def Time(self):
        r"""时间点：s
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def BusinessMetrics(self):
        r"""业务指标（bps/ms/%）
        :rtype: float
        """
        return self._BusinessMetrics

    @BusinessMetrics.setter
    def BusinessMetrics(self, BusinessMetrics):
        self._BusinessMetrics = BusinessMetrics

    @property
    def SlotNetInfo(self):
        r"""网卡状态信息
        :rtype: list of SlotNetInfo
        """
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
    r"""网络详细信息

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
        r"""流量值（byte）
        :rtype: float
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def Time(self):
        r"""时间点，单位：s
        :rtype: str
        """
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
        


class OrderFlowPackageRequest(AbstractModel):
    r"""OrderFlowPackage请求参数结构体

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
        :param _PackageRegion: 区域标识，0：中国境内，1：中国境外
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
        r"""流量包规格类型。可取值如下：
DEVICE_1_FLOW_20G、DEVICE_2_FLOW_50G、
DEVICE_3_FLOW_100G、
DEVICE_5_FLOW_500G，分别代表20G、50G、100G、500G档位的流量包。
档位也影响流量包可绑定的设备数量上限：
20G：最多绑定1个设备
50G：最多绑定2个设备
100G：最多绑定3个设备
500G：最多绑定5个设备
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def DeviceList(self):
        r"""流量包绑定的设备ID列表。捆绑设备个数上限取决于包的规格档位：
20G：最多绑定1个设备
50G：最多绑定2个设备
100G：最多绑定3个设备
500G：最多绑定5个设备
        :rtype: list of str
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def AutoRenewFlag(self):
        r"""是否自动续费，该选项和流量截断冲突，只能开启一个
        :rtype: bool
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PackageRegion(self):
        r"""区域标识，0：中国境内，1：中国境外
        :rtype: int
        """
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def FlowTruncFlag(self):
        r"""是否开启流量截断功能，该选项和自动续费冲突
        :rtype: bool
        """
        return self._FlowTruncFlag

    @FlowTruncFlag.setter
    def FlowTruncFlag(self, FlowTruncFlag):
        self._FlowTruncFlag = FlowTruncFlag

    @property
    def AutoVoucher(self):
        r"""是否自动选择代金券，默认false。
有多张券时的选择策略：按照可支付订单全部金额的券，先到期的券，可抵扣金额最大的券，余额最小的券，现金券 这个优先级进行扣券，且最多只抵扣一张券。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""指定代金券ID。自动选择代金券时此参数无效。目前只允许传入一张代金券。
注：若指定的代金券不符合订单抵扣条件，则正常支付，不扣券
        :rtype: list of str
        """
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
    r"""OrderFlowPackage返回参数结构体

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
        r"""流量包的唯一资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._RequestId = params.get("RequestId")


class OrderInfo(AbstractModel):
    r"""返回上报的订单信息

    """

    def __init__(self):
        r"""
        :param _Uin: 父账号uin
        :type Uin: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _PackageType: 用量类型
        :type PackageType: str
        :param _OrderId: 订单编号唯一标识符
        :type OrderId: str
        :param _ReportMonth: 上报月份，默认当前月
        :type ReportMonth: str
        :param _Updated: 数据更新时间
        :type Updated: str
        """
        self._Uin = None
        self._ProjectId = None
        self._PackageType = None
        self._OrderId = None
        self._ReportMonth = None
        self._Updated = None

    @property
    def Uin(self):
        r"""父账号uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PackageType(self):
        r"""用量类型
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def OrderId(self):
        r"""订单编号唯一标识符
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ReportMonth(self):
        r"""上报月份，默认当前月
        :rtype: str
        """
        return self._ReportMonth

    @ReportMonth.setter
    def ReportMonth(self, ReportMonth):
        self._ReportMonth = ReportMonth

    @property
    def Updated(self):
        r"""数据更新时间
        :rtype: str
        """
        return self._Updated

    @Updated.setter
    def Updated(self, Updated):
        self._Updated = Updated


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ProjectId = params.get("ProjectId")
        self._PackageType = params.get("PackageType")
        self._OrderId = params.get("OrderId")
        self._ReportMonth = params.get("ReportMonth")
        self._Updated = params.get("Updated")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderPerLicenseRequest(AbstractModel):
    r"""OrderPerLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 购买永久授权License的设备ID，如果是厂商未激活设备采用HardwareId
        :type DeviceId: str
        :param _Type: 设备类型，0: SDK，1: CPE，作为用户创建或激活设备时传0，作为厂商创建待激活设备时传1
        :type Type: int
        :param _RollBack: 购买失败后是否回滚（删除）设备，默认false，如果设备绑定了生效中的流量包则不能回滚。
        :type RollBack: bool
        :param _AutoVoucher: 是否自动选择代金券，默认false。
有多张券时的选择策略：按照可支付订单全部金额的券，先到期的券，可抵扣金额最大的券，余额最小的券，现金券 这个优先级进行扣券，且最多只抵扣一张券。
        :type AutoVoucher: bool
        :param _VoucherIds: 指定代金券ID。自动选择代金券时此参数无效。目前只允许传入一张代金券。
注：若指定的代金券不符合订单抵扣条件，则正常支付，不扣券
        :type VoucherIds: list of str
        """
        self._DeviceId = None
        self._Type = None
        self._RollBack = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def DeviceId(self):
        r"""购买永久授权License的设备ID，如果是厂商未激活设备采用HardwareId
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Type(self):
        r"""设备类型，0: SDK，1: CPE，作为用户创建或激活设备时传0，作为厂商创建待激活设备时传1
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RollBack(self):
        r"""购买失败后是否回滚（删除）设备，默认false，如果设备绑定了生效中的流量包则不能回滚。
        :rtype: bool
        """
        return self._RollBack

    @RollBack.setter
    def RollBack(self, RollBack):
        self._RollBack = RollBack

    @property
    def AutoVoucher(self):
        r"""是否自动选择代金券，默认false。
有多张券时的选择策略：按照可支付订单全部金额的券，先到期的券，可抵扣金额最大的券，余额最小的券，现金券 这个优先级进行扣券，且最多只抵扣一张券。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""指定代金券ID。自动选择代金券时此参数无效。目前只允许传入一张代金券。
注：若指定的代金券不符合订单抵扣条件，则正常支付，不扣券
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Type = params.get("Type")
        self._RollBack = params.get("RollBack")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderPerLicenseResponse(AbstractModel):
    r"""OrderPerLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 一次性授权License的资源ID
        :type ResourceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._RequestId = None

    @property
    def ResourceId(self):
        r"""一次性授权License的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._RequestId = params.get("RequestId")


class ReportOrderRequest(AbstractModel):
    r"""ReportOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单编号唯一标识符
        :type OrderId: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _PackageType: 用量类型
        :type PackageType: str
        :param _ReportMonth: 上报月份，默认当前月
        :type ReportMonth: str
        """
        self._OrderId = None
        self._ProjectId = None
        self._PackageType = None
        self._ReportMonth = None

    @property
    def OrderId(self):
        r"""订单编号唯一标识符
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PackageType(self):
        r"""用量类型
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ReportMonth(self):
        r"""上报月份，默认当前月
        :rtype: str
        """
        return self._ReportMonth

    @ReportMonth.setter
    def ReportMonth(self, ReportMonth):
        self._ReportMonth = ReportMonth


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._ProjectId = params.get("ProjectId")
        self._PackageType = params.get("PackageType")
        self._ReportMonth = params.get("ReportMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportOrderResponse(AbstractModel):
    r"""ReportOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderInfo: 订单信息
        :type OrderInfo: :class:`tencentcloud.mna.v20210119.models.OrderInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderInfo = None
        self._RequestId = None

    @property
    def OrderInfo(self):
        r"""订单信息
        :rtype: :class:`tencentcloud.mna.v20210119.models.OrderInfo`
        """
        return self._OrderInfo

    @OrderInfo.setter
    def OrderInfo(self, OrderInfo):
        self._OrderInfo = OrderInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OrderInfo") is not None:
            self._OrderInfo = OrderInfo()
            self._OrderInfo._deserialize(params.get("OrderInfo"))
        self._RequestId = params.get("RequestId")


class SetNotifyUrlRequest(AbstractModel):
    r"""SetNotifyUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotifyUrl: 告警通知回调url
        :type NotifyUrl: str
        :param _CallbackKey: 告警通知回调key
        :type CallbackKey: str
        :param _AlarmValue: 流量包的告警阈值
        :type AlarmValue: int
        """
        self._NotifyUrl = None
        self._CallbackKey = None
        self._AlarmValue = None

    @property
    def NotifyUrl(self):
        r"""告警通知回调url
        :rtype: str
        """
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def CallbackKey(self):
        r"""告警通知回调key
        :rtype: str
        """
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def AlarmValue(self):
        r"""流量包的告警阈值
        :rtype: int
        """
        return self._AlarmValue

    @AlarmValue.setter
    def AlarmValue(self, AlarmValue):
        self._AlarmValue = AlarmValue


    def _deserialize(self, params):
        self._NotifyUrl = params.get("NotifyUrl")
        self._CallbackKey = params.get("CallbackKey")
        self._AlarmValue = params.get("AlarmValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNotifyUrlResponse(AbstractModel):
    r"""SetNotifyUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SlotNetInfo(AbstractModel):
    r"""网卡流量指标数据

    """

    def __init__(self):
        r"""
        :param _NetInfoName: 网卡名
        :type NetInfoName: str
        :param _PublicIP: 公网IP
        :type PublicIP: str
        :param _Current: 指标数据（bps/ms/%）
        :type Current: float
        """
        self._NetInfoName = None
        self._PublicIP = None
        self._Current = None

    @property
    def NetInfoName(self):
        r"""网卡名
        :rtype: str
        """
        return self._NetInfoName

    @NetInfoName.setter
    def NetInfoName(self, NetInfoName):
        self._NetInfoName = NetInfoName

    @property
    def PublicIP(self):
        r"""公网IP
        :rtype: str
        """
        return self._PublicIP

    @PublicIP.setter
    def PublicIP(self, PublicIP):
        self._PublicIP = PublicIP

    @property
    def Current(self):
        r"""指标数据（bps/ms/%）
        :rtype: float
        """
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
        


class UpdateDeviceRequest(AbstractModel):
    r"""UpdateDevice请求参数结构体

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
        :param _FlowTrunc: 设备无流量包处理方式，0: 按量付费，1: 截断加速
        :type FlowTrunc: int
        """
        self._DeviceId = None
        self._DeviceName = None
        self._Remark = None
        self._UpdateNetInfo = None
        self._FlowTrunc = None

    @property
    def DeviceId(self):
        r"""设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Remark(self):
        r"""设备备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdateNetInfo(self):
        r"""更新设备网络信息
        :rtype: list of UpdateNetInfo
        """
        return self._UpdateNetInfo

    @UpdateNetInfo.setter
    def UpdateNetInfo(self, UpdateNetInfo):
        self._UpdateNetInfo = UpdateNetInfo

    @property
    def FlowTrunc(self):
        r"""设备无流量包处理方式，0: 按量付费，1: 截断加速
        :rtype: int
        """
        return self._FlowTrunc

    @FlowTrunc.setter
    def FlowTrunc(self, FlowTrunc):
        self._FlowTrunc = FlowTrunc


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
        self._FlowTrunc = params.get("FlowTrunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceResponse(AbstractModel):
    r"""UpdateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateGroupRequest(AbstractModel):
    r"""UpdateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _Description: 分组备注
        :type Description: str
        """
        self._GroupId = None
        self._Description = None

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Description(self):
        r"""分组备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    r"""UpdateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateHardwareRequest(AbstractModel):
    r"""UpdateHardware请求参数结构体

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
        r"""硬件ID
        :rtype: str
        """
        return self._HardwareId

    @HardwareId.setter
    def HardwareId(self, HardwareId):
        self._HardwareId = HardwareId

    @property
    def SN(self):
        r"""硬件序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def Description(self):
        r"""设备备注
        :rtype: str
        """
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
    r"""UpdateHardware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateL3CidrRequest(AbstractModel):
    r"""UpdateL3Cidr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _L3ConnId: 互通规则ID
        :type L3ConnId: str
        :param _Cidr1: 互通规则CIDR
        :type Cidr1: str
        :param _DeviceId1: 互通设备ID
        :type DeviceId1: str
        :param _DeviceId2: 互通设备ID
        :type DeviceId2: str
        :param _Cidr2: 互通规则CIDR
        :type Cidr2: str
        """
        self._L3ConnId = None
        self._Cidr1 = None
        self._DeviceId1 = None
        self._DeviceId2 = None
        self._Cidr2 = None

    @property
    def L3ConnId(self):
        r"""互通规则ID
        :rtype: str
        """
        return self._L3ConnId

    @L3ConnId.setter
    def L3ConnId(self, L3ConnId):
        self._L3ConnId = L3ConnId

    @property
    def Cidr1(self):
        r"""互通规则CIDR
        :rtype: str
        """
        return self._Cidr1

    @Cidr1.setter
    def Cidr1(self, Cidr1):
        self._Cidr1 = Cidr1

    @property
    def DeviceId1(self):
        r"""互通设备ID
        :rtype: str
        """
        return self._DeviceId1

    @DeviceId1.setter
    def DeviceId1(self, DeviceId1):
        self._DeviceId1 = DeviceId1

    @property
    def DeviceId2(self):
        r"""互通设备ID
        :rtype: str
        """
        return self._DeviceId2

    @DeviceId2.setter
    def DeviceId2(self, DeviceId2):
        self._DeviceId2 = DeviceId2

    @property
    def Cidr2(self):
        r"""互通规则CIDR
        :rtype: str
        """
        return self._Cidr2

    @Cidr2.setter
    def Cidr2(self, Cidr2):
        self._Cidr2 = Cidr2


    def _deserialize(self, params):
        self._L3ConnId = params.get("L3ConnId")
        self._Cidr1 = params.get("Cidr1")
        self._DeviceId1 = params.get("DeviceId1")
        self._DeviceId2 = params.get("DeviceId2")
        self._Cidr2 = params.get("Cidr2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateL3CidrResponse(AbstractModel):
    r"""UpdateL3Cidr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateL3ConnRequest(AbstractModel):
    r"""UpdateL3Conn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _L3ConnId: 互通规则ID
        :type L3ConnId: str
        :param _Description: 互通规则备注
        :type Description: str
        """
        self._L3ConnId = None
        self._Description = None

    @property
    def L3ConnId(self):
        r"""互通规则ID
        :rtype: str
        """
        return self._L3ConnId

    @L3ConnId.setter
    def L3ConnId(self, L3ConnId):
        self._L3ConnId = L3ConnId

    @property
    def Description(self):
        r"""互通规则备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._L3ConnId = params.get("L3ConnId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateL3ConnResponse(AbstractModel):
    r"""UpdateL3Conn返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateL3SwitchRequest(AbstractModel):
    r"""UpdateL3Switch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _L3ConnId: 互通规则ID
        :type L3ConnId: str
        :param _Enable: 互通规则开关
        :type Enable: bool
        """
        self._L3ConnId = None
        self._Enable = None

    @property
    def L3ConnId(self):
        r"""互通规则ID
        :rtype: str
        """
        return self._L3ConnId

    @L3ConnId.setter
    def L3ConnId(self, L3ConnId):
        self._L3ConnId = L3ConnId

    @property
    def Enable(self):
        r"""互通规则开关
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._L3ConnId = params.get("L3ConnId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateL3SwitchResponse(AbstractModel):
    r"""UpdateL3Switch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateNetInfo(AbstractModel):
    r"""更新设备网络状态信息

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
        r"""网络类型：
0:数据
1:Wi-Fi
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DataEnable(self):
        r"""启用/禁用
        :rtype: bool
        """
        return self._DataEnable

    @DataEnable.setter
    def DataEnable(self, DataEnable):
        self._DataEnable = DataEnable

    @property
    def UploadLimit(self):
        r"""上行限速：bit
        :rtype: int
        """
        return self._UploadLimit

    @UploadLimit.setter
    def UploadLimit(self, UploadLimit):
        self._UploadLimit = UploadLimit

    @property
    def DownloadLimit(self):
        r"""下行限速：bit
        :rtype: int
        """
        return self._DownloadLimit

    @DownloadLimit.setter
    def DownloadLimit(self, DownloadLimit):
        self._DownloadLimit = DownloadLimit

    @property
    def NetInfoName(self):
        r"""网卡名
        :rtype: str
        """
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
    r"""厂商硬件详细信息

    """

    def __init__(self):
        r"""
        :param _HardwareId: 硬件id
        :type HardwareId: str
        :param _SN: 硬件序列号
        :type SN: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Status: 激活状态， 空：全部； 1:待激活； 2:已激活
        :type Status: int
        :param _ActiveTime: 激活时间
        :type ActiveTime: str
        :param _Description: 厂商备注
        :type Description: str
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _LicenseChargingMode: license计费模式： 1，租户月付费 2，厂商月付费 3，license永久授权
注：设备为租户付费且未激活（未选择月付还是永久付费）时，此参数返回1，仅代表租户付费。后续将废弃此参数，新接入请使用LicensePayMode和Payer
        :type LicenseChargingMode: int
        :param _LastOnlineTime: 最后在线时间
        :type LastOnlineTime: str
        :param _LicensePayMode: license授权有效期
0：月度授权
1：永久授权
-1：未知
        :type LicensePayMode: int
        :param _Payer: 付费方
0：客户付费
1：厂商付费
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
        r"""硬件id
        :rtype: str
        """
        return self._HardwareId

    @HardwareId.setter
    def HardwareId(self, HardwareId):
        self._HardwareId = HardwareId

    @property
    def SN(self):
        r"""硬件序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        r"""激活状态， 空：全部； 1:待激活； 2:已激活
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActiveTime(self):
        r"""激活时间
        :rtype: str
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def Description(self):
        r"""厂商备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DeviceId(self):
        r"""设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def LicenseChargingMode(self):
        r"""license计费模式： 1，租户月付费 2，厂商月付费 3，license永久授权
注：设备为租户付费且未激活（未选择月付还是永久付费）时，此参数返回1，仅代表租户付费。后续将废弃此参数，新接入请使用LicensePayMode和Payer
        :rtype: int
        """
        return self._LicenseChargingMode

    @LicenseChargingMode.setter
    def LicenseChargingMode(self, LicenseChargingMode):
        self._LicenseChargingMode = LicenseChargingMode

    @property
    def LastOnlineTime(self):
        r"""最后在线时间
        :rtype: str
        """
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def LicensePayMode(self):
        r"""license授权有效期
0：月度授权
1：永久授权
-1：未知
        :rtype: int
        """
        return self._LicensePayMode

    @LicensePayMode.setter
    def LicensePayMode(self, LicensePayMode):
        self._LicensePayMode = LicensePayMode

    @property
    def Payer(self):
        r"""付费方
0：客户付费
1：厂商付费
        :rtype: int
        """
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
        