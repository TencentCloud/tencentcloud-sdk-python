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


class ActivateTWeCallLicenseRequest(AbstractModel):
    """ActivateTWeCallLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgType: TWecall类型： 0-测试激活码； 1-家庭安防场景； 2-穿戴类场景； 3-生活娱乐场景； 4-对讲及其它场景
        :type PkgType: int
        :param _MiniProgramAppId: appId
        :type MiniProgramAppId: str
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._PkgType = None
        self._MiniProgramAppId = None
        self._DeviceList = None

    @property
    def PkgType(self):
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._PkgType = params.get("PkgType")
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = TWeCallInfo()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateTWeCallLicenseResponse(AbstractModel):
    """ActivateTWeCallLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceList: 设备激活返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: list of DeviceActiveResult
        :param _FailureList: 设备激活失败返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureList: list of DeviceActiveResult
        :param _SuccessList: 设备激活成功返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessList: list of DeviceActiveResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceList = None
        self._FailureList = None
        self._SuccessList = None
        self._RequestId = None

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def FailureList(self):
        return self._FailureList

    @FailureList.setter
    def FailureList(self, FailureList):
        self._FailureList = FailureList

    @property
    def SuccessList(self):
        return self._SuccessList

    @SuccessList.setter
    def SuccessList(self, SuccessList):
        self._SuccessList = SuccessList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = DeviceActiveResult()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        if params.get("FailureList") is not None:
            self._FailureList = []
            for item in params.get("FailureList"):
                obj = DeviceActiveResult()
                obj._deserialize(item)
                self._FailureList.append(obj)
        if params.get("SuccessList") is not None:
            self._SuccessList = []
            for item in params.get("SuccessList"):
                obj = DeviceActiveResult()
                obj._deserialize(item)
                self._SuccessList.append(obj)
        self._RequestId = params.get("RequestId")


class AppDeviceInfo(AbstractModel):
    """云api直接绑定设备出参

    """

    def __init__(self):
        r"""
        :param _DeviceId: 产品ID/设备名
        :type DeviceId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _AliasName: 设备别名
        :type AliasName: str
        :param _IconUrl: icon地址
        :type IconUrl: str
        :param _FamilyId: 家庭ID
        :type FamilyId: str
        :param _RoomId: 房间ID
        :type RoomId: str
        :param _DeviceType: 设备类型
        :type DeviceType: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        """
        self._DeviceId = None
        self._ProductId = None
        self._DeviceName = None
        self._AliasName = None
        self._IconUrl = None
        self._FamilyId = None
        self._RoomId = None
        self._DeviceType = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

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
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def FamilyId(self):
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

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


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._AliasName = params.get("AliasName")
        self._IconUrl = params.get("IconUrl")
        self._FamilyId = params.get("FamilyId")
        self._RoomId = params.get("RoomId")
        self._DeviceType = params.get("DeviceType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignTWeCallLicenseRequest(AbstractModel):
    """AssignTWeCallLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgType: voip类型
        :type PkgType: int
        :param _MiniProgramAppId: appId
        :type MiniProgramAppId: str
        :param _DeductNum: License数，只支持50,500,1000,5000,10000,20000,50000
        :type DeductNum: int
        """
        self._PkgType = None
        self._MiniProgramAppId = None
        self._DeductNum = None

    @property
    def PkgType(self):
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def DeductNum(self):
        return self._DeductNum

    @DeductNum.setter
    def DeductNum(self, DeductNum):
        self._DeductNum = DeductNum


    def _deserialize(self, params):
        self._PkgType = params.get("PkgType")
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        self._DeductNum = params.get("DeductNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignTWeCallLicenseResponse(AbstractModel):
    """AssignTWeCallLicense返回参数结构体

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


class AuthMiniProgramAppInfo(AbstractModel):
    """授权小程序信息

    """

    def __init__(self):
        r"""
        :param _MiniProgramAppId: 小程序APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniProgramAppId: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _MiniProgramName: 小程序名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniProgramName: str
        :param _LicenseNum: 激活码数
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseNum: int
        :param _IotAppId: 应用ID 
注意：此字段可能返回 null，表示取不到有效值。
        :type IotAppId: str
        :param _IotAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IotAppName: str
        """
        self._MiniProgramAppId = None
        self._CreateTime = None
        self._MiniProgramName = None
        self._LicenseNum = None
        self._IotAppId = None
        self._IotAppName = None

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MiniProgramName(self):
        return self._MiniProgramName

    @MiniProgramName.setter
    def MiniProgramName(self, MiniProgramName):
        self._MiniProgramName = MiniProgramName

    @property
    def LicenseNum(self):
        return self._LicenseNum

    @LicenseNum.setter
    def LicenseNum(self, LicenseNum):
        self._LicenseNum = LicenseNum

    @property
    def IotAppId(self):
        return self._IotAppId

    @IotAppId.setter
    def IotAppId(self, IotAppId):
        self._IotAppId = IotAppId

    @property
    def IotAppName(self):
        return self._IotAppName

    @IotAppName.setter
    def IotAppName(self, IotAppName):
        self._IotAppName = IotAppName


    def _deserialize(self, params):
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        self._CreateTime = params.get("CreateTime")
        self._MiniProgramName = params.get("MiniProgramName")
        self._LicenseNum = params.get("LicenseNum")
        self._IotAppId = params.get("IotAppId")
        self._IotAppName = params.get("IotAppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchProductionInfo(AbstractModel):
    """获取返回列表的详情。

    """

    def __init__(self):
        r"""
        :param _BatchProductionId: 量产ID
        :type BatchProductionId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _BurnMethod: 烧录方式
        :type BurnMethod: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _ProductName: 产品名称
        :type ProductName: str
        """
        self._BatchProductionId = None
        self._ProductId = None
        self._BurnMethod = None
        self._CreateTime = None
        self._ProductName = None

    @property
    def BatchProductionId(self):
        return self._BatchProductionId

    @BatchProductionId.setter
    def BatchProductionId(self, BatchProductionId):
        self._BatchProductionId = BatchProductionId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BurnMethod(self):
        return self._BurnMethod

    @BurnMethod.setter
    def BurnMethod(self, BurnMethod):
        self._BurnMethod = BurnMethod

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


    def _deserialize(self, params):
        self._BatchProductionId = params.get("BatchProductionId")
        self._ProductId = params.get("ProductId")
        self._BurnMethod = params.get("BurnMethod")
        self._CreateTime = params.get("CreateTime")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudStorageUserRequest(AbstractModel):
    """BindCloudStorageUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudStorageUserResponse(AbstractModel):
    """BindCloudStorageUser返回参数结构体

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


class BindDeviceInfo(AbstractModel):
    """BindDeviceInfo

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _DeviceName: 设备名称。
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
        


class BindDevicesRequest(AbstractModel):
    """BindDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关设备的产品ID。
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备的设备名。
        :type GatewayDeviceName: str
        :param _ProductId: 被绑定设备的产品ID。
        :type ProductId: str
        :param _DeviceNames: 被绑定的多个设备名。
        :type DeviceNames: list of str
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._ProductId = None
        self._DeviceNames = None

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


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
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
    """绑定、未绑定产品详细信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _ProductName: 产品名称。
        :type ProductName: str
        :param _ProjectId: 产品所属项目ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _DataProtocol: 物模型类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataProtocol: int
        :param _CategoryId: 产品分组模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryId: int
        :param _ProductType: 产品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductType: int
        :param _NetType: 连接类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        :param _DevStatus: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DevStatus: str
        :param _ProductOwnerName: 产品拥有者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductOwnerName: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProjectId = None
        self._DataProtocol = None
        self._CategoryId = None
        self._ProductType = None
        self._NetType = None
        self._DevStatus = None
        self._ProductOwnerName = None

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DataProtocol(self):
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def DevStatus(self):
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

    @property
    def ProductOwnerName(self):
        return self._ProductOwnerName

    @ProductOwnerName.setter
    def ProductOwnerName(self, ProductOwnerName):
        self._ProductOwnerName = ProductOwnerName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProjectId = params.get("ProjectId")
        self._DataProtocol = params.get("DataProtocol")
        self._CategoryId = params.get("CategoryId")
        self._ProductType = params.get("ProductType")
        self._NetType = params.get("NetType")
        self._DevStatus = params.get("DevStatus")
        self._ProductOwnerName = params.get("ProductOwnerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindProductsRequest(AbstractModel):
    """BindProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID。
        :type GatewayProductId: str
        :param _ProductIds: 待绑定的子产品ID数组。
        :type ProductIds: list of str
        """
        self._GatewayProductId = None
        self._ProductIds = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def ProductIds(self):
        return self._ProductIds

    @ProductIds.setter
    def ProductIds(self, ProductIds):
        self._ProductIds = ProductIds


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindProductsResponse(AbstractModel):
    """BindProducts返回参数结构体

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


class CallDeviceActionAsyncRequest(AbstractModel):
    """CallDeviceActionAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :type ActionId: str
        :param _InputParams: 输入参数
        :type InputParams: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ActionId = None
        self._InputParams = None

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
    def ActionId(self):
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def InputParams(self):
        return self._InputParams

    @InputParams.setter
    def InputParams(self, InputParams):
        self._InputParams = InputParams


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ActionId = params.get("ActionId")
        self._InputParams = params.get("InputParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDeviceActionAsyncResponse(AbstractModel):
    """CallDeviceActionAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientToken: 调用Id
        :type ClientToken: str
        :param _Status: 异步调用状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientToken = None
        self._Status = None
        self._RequestId = None

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClientToken = params.get("ClientToken")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CallDeviceActionSyncRequest(AbstractModel):
    """CallDeviceActionSync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ActionId: 产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :type ActionId: str
        :param _InputParams: 输入参数
        :type InputParams: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ActionId = None
        self._InputParams = None

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
    def ActionId(self):
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def InputParams(self):
        return self._InputParams

    @InputParams.setter
    def InputParams(self, InputParams):
        self._InputParams = InputParams


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ActionId = params.get("ActionId")
        self._InputParams = params.get("InputParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDeviceActionSyncResponse(AbstractModel):
    """CallDeviceActionSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientToken: 调用Id
        :type ClientToken: str
        :param _OutputParams: 输出参数，取值设备端上报$thing/up/action method为action_reply 的 response字段，物模型协议参考https://cloud.tencent.com/document/product/1081/34916#.E8.AE.BE.E5.A4.87.E8.A1.8C.E4.B8.BA.E8.B0.83.E7.94.A8
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param _Status: 返回状态，取值设备端上报$thing/up/action	method为action_reply 的 status字段，如果不包含status字段，则取默认值，空字符串，物模型协议参考https://cloud.tencent.com/document/product/1081/34916#.E8.AE.BE.E5.A4.87.E8.A1.8C.E4.B8.BA.E8.B0.83.E7.94.A8
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientToken = None
        self._OutputParams = None
        self._Status = None
        self._RequestId = None

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def OutputParams(self):
        return self._OutputParams

    @OutputParams.setter
    def OutputParams(self, OutputParams):
        self._OutputParams = OutputParams

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClientToken = params.get("ClientToken")
        self._OutputParams = params.get("OutputParams")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CamTag(AbstractModel):
    """标签数据结构

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAssignTWeCallLicenseRequest(AbstractModel):
    """CancelAssignTWeCallLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgId: 订单号
        :type PkgId: str
        """
        self._PkgId = None

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAssignTWeCallLicenseResponse(AbstractModel):
    """CancelAssignTWeCallLicense返回参数结构体

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


class CheckFirmwareUpdateRequest(AbstractModel):
    """CheckFirmwareUpdate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _DeviceName: 设备名称。
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
        


class CheckFirmwareUpdateResponse(AbstractModel):
    """CheckFirmwareUpdate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CurrentVersion: 设备当前固件版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentVersion: str
        :param _DstVersion: 固件可升级版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type DstVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CurrentVersion = None
        self._DstVersion = None
        self._RequestId = None

    @property
    def CurrentVersion(self):
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion

    @property
    def DstVersion(self):
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CurrentVersion = params.get("CurrentVersion")
        self._DstVersion = params.get("DstVersion")
        self._RequestId = params.get("RequestId")


class CloudStorageAIServiceTask(AbstractModel):
    """云存 AI 服务任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 云存 AI 服务任务 ID
        :type TaskId: str
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ChannelId: 通道 ID
        :type ChannelId: int
        :param _ServiceType: 云存 AI 服务类型。可能取值：

- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
        :type ServiceType: str
        :param _StartTime: 对应云存视频的起始时间
        :type StartTime: int
        :param _EndTime: 对应云存视频的结束时间
        :type EndTime: int
        :param _Status: 任务状态（1：失败；2：成功但结果为空；3：成功且结果非空；4：执行中）
        :type Status: int
        :param _Result: 任务结果
        :type Result: str
        :param _Files: 任务输出文件列表
        :type Files: list of str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 最后更新时间
        :type UpdateTime: int
        :param _CustomId: 自定义任务 ID
        :type CustomId: str
        """
        self._TaskId = None
        self._ProductId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ServiceType = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Result = None
        self._Files = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CustomId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

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

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Files(self):
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

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
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ServiceType = params.get("ServiceType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._Files = params.get("Files")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CustomId = params.get("CustomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageEvent(AbstractModel):
    """云存事件

    """

    def __init__(self):
        r"""
        :param _StartTime: 事件起始时间（Unix 时间戳，秒级
        :type StartTime: int
        :param _EndTime: 事件结束时间（Unix 时间戳，秒级
        :type EndTime: int
        :param _Thumbnail: 事件缩略图
        :type Thumbnail: str
        :param _EventId: 事件ID
        :type EventId: str
        :param _UploadStatus: 事件录像上传状态，Finished: 全部上传成功 Partial: 部分上传成功 Failed: 上传失败	
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadStatus: str
        :param _Data: 事件自定义数据	
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Thumbnail = None
        self._EventId = None
        self._UploadStatus = None
        self._Data = None

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

    @property
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UploadStatus(self):
        return self._UploadStatus

    @UploadStatus.setter
    def UploadStatus(self, UploadStatus):
        self._UploadStatus = UploadStatus

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Thumbnail = params.get("Thumbnail")
        self._EventId = params.get("EventId")
        self._UploadStatus = params.get("UploadStatus")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeData(AbstractModel):
    """云存时间轴接口返回数据

    """

    def __init__(self):
        r"""
        :param _TimeList: 云存时间轴信息列表
        :type TimeList: list of CloudStorageTimeInfo
        :param _VideoURL: 播放地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoURL: str
        """
        self._TimeList = None
        self._VideoURL = None

    @property
    def TimeList(self):
        return self._TimeList

    @TimeList.setter
    def TimeList(self, TimeList):
        self._TimeList = TimeList

    @property
    def VideoURL(self):
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL


    def _deserialize(self, params):
        if params.get("TimeList") is not None:
            self._TimeList = []
            for item in params.get("TimeList"):
                obj = CloudStorageTimeInfo()
                obj._deserialize(item)
                self._TimeList.append(obj)
        self._VideoURL = params.get("VideoURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeInfo(AbstractModel):
    """云存时间轴信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

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
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageUserInfo(AbstractModel):
    """云存用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Data: 属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义
        :type Data: str
        :param _Method: 请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性
        :type Method: str
        :param _DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName , 通常情况不需要填写
        :type DeviceId: str
        :param _DataTimestamp: 上报数据UNIX时间戳(毫秒), 仅对Method:reported有效
        :type DataTimestamp: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Data = None
        self._Method = None
        self._DeviceId = None
        self._DataTimestamp = None

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DataTimestamp(self):
        return self._DataTimestamp

    @DataTimestamp.setter
    def DataTimestamp(self, DataTimestamp):
        self._DataTimestamp = DataTimestamp


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Data = params.get("Data")
        self._Method = params.get("Method")
        self._DeviceId = params.get("DeviceId")
        self._DataTimestamp = params.get("DataTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回信息
        :type Data: str
        :param _Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic.
pushResult 是表示发送结果，其中 0 表示成功， 23101 表示设备未在线或没有订阅相关的 MQTT Topic。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Result = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateBatchProductionRequest(AbstractModel):
    """CreateBatchProduction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _BurnMethod: 烧录方式，0为直接烧录，1为动态注册。
        :type BurnMethod: int
        :param _GenerationMethod: 生成方式，0为系统生成，1为文件上传。
        :type GenerationMethod: int
        :param _UploadUrl: 文件上传URL，用于文件上传时填写。
        :type UploadUrl: str
        :param _BatchCnt: 量产数量，用于系统生成时填写。
        :type BatchCnt: int
        :param _GenerationQRCode: 是否生成二维码,0为不生成，1为生成。
        :type GenerationQRCode: int
        """
        self._ProjectId = None
        self._ProductId = None
        self._BurnMethod = None
        self._GenerationMethod = None
        self._UploadUrl = None
        self._BatchCnt = None
        self._GenerationQRCode = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BurnMethod(self):
        return self._BurnMethod

    @BurnMethod.setter
    def BurnMethod(self, BurnMethod):
        self._BurnMethod = BurnMethod

    @property
    def GenerationMethod(self):
        return self._GenerationMethod

    @GenerationMethod.setter
    def GenerationMethod(self, GenerationMethod):
        self._GenerationMethod = GenerationMethod

    @property
    def UploadUrl(self):
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def BatchCnt(self):
        return self._BatchCnt

    @BatchCnt.setter
    def BatchCnt(self, BatchCnt):
        self._BatchCnt = BatchCnt

    @property
    def GenerationQRCode(self):
        return self._GenerationQRCode

    @GenerationQRCode.setter
    def GenerationQRCode(self, GenerationQRCode):
        self._GenerationQRCode = GenerationQRCode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProductId = params.get("ProductId")
        self._BurnMethod = params.get("BurnMethod")
        self._GenerationMethod = params.get("GenerationMethod")
        self._UploadUrl = params.get("UploadUrl")
        self._BatchCnt = params.get("BatchCnt")
        self._GenerationQRCode = params.get("GenerationQRCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchProductionResponse(AbstractModel):
    """CreateBatchProduction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _BatchProductionId: 量产id
        :type BatchProductionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._ProductId = None
        self._BatchProductionId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchProductionId(self):
        return self._BatchProductionId

    @BatchProductionId.setter
    def BatchProductionId(self, BatchProductionId):
        self._BatchProductionId = BatchProductionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProductId = params.get("ProductId")
        self._BatchProductionId = params.get("BatchProductionId")
        self._RequestId = params.get("RequestId")


class CreateCloudStorageAIServiceRequest(AbstractModel):
    """CreateCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _PackageId: 云存 AI 套餐 ID。可选值：

- `1m_low_od`：低功耗目标检测月套餐
- `1y_low_od`：低功耗目标检测年套餐
- `1m_ev_od`：事件目标检测月套餐
- `1y_ev_od`：事件目标检测年套餐
- `1m_ft_od`：全时目标检测月套餐
- `1y_ft_od`：全时目标检测年套餐
- `1m_low_hl`：低功耗视频浓缩月套餐
- `1y_low_hl`：低功耗视频浓缩年套餐
- `1m_ev_hl`：事件视频浓缩月套餐
- `1y_ev_hl`：事件视频浓缩年套餐
- `1m_ft_hl`：全时视频浓缩月套餐
- `1y_ft_hl`：全时视频浓缩年套餐
        :type PackageId: str
        :param _ChannelId: 通道 ID
        :type ChannelId: int
        :param _OrderId: 订单 ID
        :type OrderId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._PackageId = None
        self._ChannelId = None
        self._OrderId = None

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
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._PackageId = params.get("PackageId")
        self._ChannelId = params.get("ChannelId")
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudStorageAIServiceResponse(AbstractModel):
    """CreateCloudStorageAIService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单 ID
        :type OrderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._RequestId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param _DevAddr: LoRaWAN 设备地址
        :type DevAddr: str
        :param _AppKey: LoRaWAN 应用密钥
        :type AppKey: str
        :param _DevEUI: LoRaWAN 设备唯一标识
        :type DevEUI: str
        :param _AppSKey: LoRaWAN 应用会话密钥
        :type AppSKey: str
        :param _NwkSKey: LoRaWAN 网络会话密钥
        :type NwkSKey: str
        :param _DefinedPsk: 手动指定设备的PSK密钥
        :type DefinedPsk: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._DevAddr = None
        self._AppKey = None
        self._DevEUI = None
        self._AppSKey = None
        self._NwkSKey = None
        self._DefinedPsk = None

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
    def DevAddr(self):
        return self._DevAddr

    @DevAddr.setter
    def DevAddr(self, DevAddr):
        self._DevAddr = DevAddr

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def DevEUI(self):
        return self._DevEUI

    @DevEUI.setter
    def DevEUI(self, DevEUI):
        self._DevEUI = DevEUI

    @property
    def AppSKey(self):
        return self._AppSKey

    @AppSKey.setter
    def AppSKey(self, AppSKey):
        self._AppSKey = AppSKey

    @property
    def NwkSKey(self):
        return self._NwkSKey

    @NwkSKey.setter
    def NwkSKey(self, NwkSKey):
        self._NwkSKey = NwkSKey

    @property
    def DefinedPsk(self):
        return self._DefinedPsk

    @DefinedPsk.setter
    def DefinedPsk(self, DefinedPsk):
        self._DefinedPsk = DefinedPsk


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DevAddr = params.get("DevAddr")
        self._AppKey = params.get("AppKey")
        self._DevEUI = params.get("DevEUI")
        self._AppSKey = params.get("AppSKey")
        self._NwkSKey = params.get("NwkSKey")
        self._DefinedPsk = params.get("DefinedPsk")
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
        :param _Data: 设备参数描述。
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceData`
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
        if params.get("Data") is not None:
            self._Data = DeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateFenceBindRequest(AbstractModel):
    """CreateFenceBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _Items: 围栏绑定的产品列表
        :type Items: list of FenceBindProductItem
        """
        self._FenceId = None
        self._Items = None

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._FenceId = params.get("FenceId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFenceBindResponse(AbstractModel):
    """CreateFenceBind返回参数结构体

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


class CreateIotVideoCloudStorageRequest(AbstractModel):
    """CreateIotVideoCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _PackageId: 云存套餐ID：
yc1m3d ： 全时3天存储月套餐。
yc1m7d ： 全时7天存储月套餐。
yc1m30d ：全时30天存储月套餐。
yc1y3d ：全时3天存储年套餐。
yc1y7d ：全时7天存储年套餐。
yc1y30d ：全时30天存储年套餐。
ye1m3d ：事件3天存储月套餐。
ye1m7d ：事件7天存储月套餐。
ye1m30d ：事件30天存储月套餐 。
ye1y3d ：事件3天存储年套餐。
ye1y7d ：事件7天存储年套餐。
ye1y30d ：事件30天存储年套餐。
yc1w7d : 全时7天存储周套餐。
ye1w7d : 事件7天存储周套餐。
lye1m3d：低功耗事件3天月套餐。
lye1m7d：低功耗事件7天月套餐。
lye1m30d：低功耗事件30天月套餐。
lye1y3d：低功耗事件3天年套餐。
lye1y7d：低功耗事件7天年套餐。
lye1y30d：低功耗事件30天年套餐。
        :type PackageId: str
        :param _Override: 如果当前设备已开启云存套餐，Override=1会使用新套餐覆盖原有套餐。不传此参数则默认为0。
        :type Override: int
        :param _PackageQueue: 套餐列表顺序：PackageQueue=front会立即使用新购买的套餐，新购套餐结束后，列表中下一个未过期的套餐继续生效；PackageQueue=end会等设备当前所有已购买套餐过期后才会生效新购套餐。与Override参数不能同时使用。
        :type PackageQueue: str
        :param _OrderId: 订单id
        :type OrderId: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        :param _StorageRegion: 云存视频存储区域，国内默认为ap-guangzhou。海外默认为东南亚ap-singapore，可选美东na-ashburn、欧洲eu-frankfurt。
        :type StorageRegion: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._PackageId = None
        self._Override = None
        self._PackageQueue = None
        self._OrderId = None
        self._ChannelId = None
        self._StorageRegion = None

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
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def PackageQueue(self):
        return self._PackageQueue

    @PackageQueue.setter
    def PackageQueue(self, PackageQueue):
        self._PackageQueue = PackageQueue

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StorageRegion(self):
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._PackageId = params.get("PackageId")
        self._Override = params.get("Override")
        self._PackageQueue = params.get("PackageQueue")
        self._OrderId = params.get("OrderId")
        self._ChannelId = params.get("ChannelId")
        self._StorageRegion = params.get("StorageRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIotVideoCloudStorageResponse(AbstractModel):
    """CreateIotVideoCloudStorage返回参数结构体

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


class CreateLoRaFrequencyRequest(AbstractModel):
    """CreateLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FreqName: 频点配置名称
        :type FreqName: str
        :param _ChannelsDataUp: 数据上行信道
        :type ChannelsDataUp: list of int non-negative
        :param _ChannelsDataRX1: 数据下行RX1信道
        :type ChannelsDataRX1: list of int non-negative
        :param _ChannelsDataRX2: 数据下行RX2信道
        :type ChannelsDataRX2: list of int non-negative
        :param _ChannelsJoinUp: 入网上行信道
        :type ChannelsJoinUp: list of int non-negative
        :param _ChannelsJoinRX1: 入网下行RX1信道
        :type ChannelsJoinRX1: list of int non-negative
        :param _ChannelsJoinRX2: 入网下行RX2信道
        :type ChannelsJoinRX2: list of int non-negative
        :param _Description: 频点配置描述
        :type Description: str
        """
        self._FreqName = None
        self._ChannelsDataUp = None
        self._ChannelsDataRX1 = None
        self._ChannelsDataRX2 = None
        self._ChannelsJoinUp = None
        self._ChannelsJoinRX1 = None
        self._ChannelsJoinRX2 = None
        self._Description = None

    @property
    def FreqName(self):
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def ChannelsDataUp(self):
        return self._ChannelsDataUp

    @ChannelsDataUp.setter
    def ChannelsDataUp(self, ChannelsDataUp):
        self._ChannelsDataUp = ChannelsDataUp

    @property
    def ChannelsDataRX1(self):
        return self._ChannelsDataRX1

    @ChannelsDataRX1.setter
    def ChannelsDataRX1(self, ChannelsDataRX1):
        self._ChannelsDataRX1 = ChannelsDataRX1

    @property
    def ChannelsDataRX2(self):
        return self._ChannelsDataRX2

    @ChannelsDataRX2.setter
    def ChannelsDataRX2(self, ChannelsDataRX2):
        self._ChannelsDataRX2 = ChannelsDataRX2

    @property
    def ChannelsJoinUp(self):
        return self._ChannelsJoinUp

    @ChannelsJoinUp.setter
    def ChannelsJoinUp(self, ChannelsJoinUp):
        self._ChannelsJoinUp = ChannelsJoinUp

    @property
    def ChannelsJoinRX1(self):
        return self._ChannelsJoinRX1

    @ChannelsJoinRX1.setter
    def ChannelsJoinRX1(self, ChannelsJoinRX1):
        self._ChannelsJoinRX1 = ChannelsJoinRX1

    @property
    def ChannelsJoinRX2(self):
        return self._ChannelsJoinRX2

    @ChannelsJoinRX2.setter
    def ChannelsJoinRX2(self, ChannelsJoinRX2):
        self._ChannelsJoinRX2 = ChannelsJoinRX2

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FreqName = params.get("FreqName")
        self._ChannelsDataUp = params.get("ChannelsDataUp")
        self._ChannelsDataRX1 = params.get("ChannelsDataRX1")
        self._ChannelsDataRX2 = params.get("ChannelsDataRX2")
        self._ChannelsJoinUp = params.get("ChannelsJoinUp")
        self._ChannelsJoinRX1 = params.get("ChannelsJoinRX1")
        self._ChannelsJoinRX2 = params.get("ChannelsJoinRX2")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoRaFrequencyResponse(AbstractModel):
    """CreateLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: LoRa频点信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
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
        if params.get("Data") is not None:
            self._Data = LoRaFrequencyEntry()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateLoRaGatewayRequest(AbstractModel):
    """CreateLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: LoRa 网关Id
        :type GatewayId: str
        :param _Name: 网关名称
        :type Name: str
        :param _Description: 详情描述
        :type Description: str
        :param _Location: 位置坐标
        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        :param _Position: 位置信息
        :type Position: str
        :param _PositionDetails: 位置详情
        :type PositionDetails: str
        :param _IsPublic: 是否公开
        :type IsPublic: bool
        :param _FrequencyId: 频点ID
        :type FrequencyId: str
        """
        self._GatewayId = None
        self._Name = None
        self._Description = None
        self._Location = None
        self._Position = None
        self._PositionDetails = None
        self._IsPublic = None
        self._FrequencyId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

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
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def PositionDetails(self):
        return self._PositionDetails

    @PositionDetails.setter
    def PositionDetails(self, PositionDetails):
        self._PositionDetails = PositionDetails

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def FrequencyId(self):
        return self._FrequencyId

    @FrequencyId.setter
    def FrequencyId(self, FrequencyId):
        self._FrequencyId = FrequencyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Location") is not None:
            self._Location = LoRaGatewayLocation()
            self._Location._deserialize(params.get("Location"))
        self._Position = params.get("Position")
        self._PositionDetails = params.get("PositionDetails")
        self._IsPublic = params.get("IsPublic")
        self._FrequencyId = params.get("FrequencyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoRaGatewayResponse(AbstractModel):
    """CreateLoRaGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Gateway: LoRa 网关信息
        :type Gateway: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Gateway = None
        self._RequestId = None

    @property
    def Gateway(self):
        return self._Gateway

    @Gateway.setter
    def Gateway(self, Gateway):
        self._Gateway = Gateway

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Gateway") is not None:
            self._Gateway = LoRaGatewayItem()
            self._Gateway._deserialize(params.get("Gateway"))
        self._RequestId = params.get("RequestId")


class CreatePositionFenceRequest(AbstractModel):
    """CreatePositionFence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _FenceName: 围栏名称
        :type FenceName: str
        :param _FenceArea: 围栏区域信息，采用 GeoJSON 格式
        :type FenceArea: str
        :param _FenceDesc: 围栏描述
        :type FenceDesc: str
        """
        self._SpaceId = None
        self._FenceName = None
        self._FenceArea = None
        self._FenceDesc = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FenceName(self):
        return self._FenceName

    @FenceName.setter
    def FenceName(self, FenceName):
        self._FenceName = FenceName

    @property
    def FenceArea(self):
        return self._FenceArea

    @FenceArea.setter
    def FenceArea(self, FenceArea):
        self._FenceArea = FenceArea

    @property
    def FenceDesc(self):
        return self._FenceDesc

    @FenceDesc.setter
    def FenceDesc(self, FenceDesc):
        self._FenceDesc = FenceDesc


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._FenceName = params.get("FenceName")
        self._FenceArea = params.get("FenceArea")
        self._FenceDesc = params.get("FenceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePositionFenceResponse(AbstractModel):
    """CreatePositionFence返回参数结构体

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


class CreatePositionSpaceRequest(AbstractModel):
    """CreatePositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _SpaceName: 空间名称
        :type SpaceName: str
        :param _AuthorizeType: 授权类型，0：只读 1：读写
        :type AuthorizeType: int
        :param _ProductIdList: 产品列表
        :type ProductIdList: list of str
        :param _Description: 描述
        :type Description: str
        :param _Icon: 缩略图
        :type Icon: str
        """
        self._ProjectId = None
        self._SpaceName = None
        self._AuthorizeType = None
        self._ProductIdList = None
        self._Description = None
        self._Icon = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SpaceName(self):
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def AuthorizeType(self):
        return self._AuthorizeType

    @AuthorizeType.setter
    def AuthorizeType(self, AuthorizeType):
        self._AuthorizeType = AuthorizeType

    @property
    def ProductIdList(self):
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SpaceName = params.get("SpaceName")
        self._AuthorizeType = params.get("AuthorizeType")
        self._ProductIdList = params.get("ProductIdList")
        self._Description = params.get("Description")
        self._Icon = params.get("Icon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePositionSpaceResponse(AbstractModel):
    """CreatePositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceId = None
        self._RequestId = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param _InstanceId: 实例ID，不带实例ID，默认为公共实例
        :type InstanceId: str
        """
        self._ProjectName = None
        self._ProjectDesc = None
        self._InstanceId = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectDesc = params.get("ProjectDesc")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Project: 返回信息
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Project = None
        self._RequestId = None

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self._Project = ProjectEntry()
            self._Project._deserialize(params.get("Project"))
        self._RequestId = params.get("RequestId")


class CreateStudioProductRequest(AbstractModel):
    """CreateStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param _CategoryId: 产品分组模板ID , ( 自定义模板填写1 , 控制台调用会使用预置的其他ID)
        :type CategoryId: int
        :param _ProductType: 产品类型 填写 ( 0 普通产品 ， 5 网关产品)
        :type ProductType: int
        :param _EncryptionType: 加密类型 ，1表示证书认证，2表示秘钥认证，21表示TID认证-SE方式，22表示TID认证-软加固方式
        :type EncryptionType: str
        :param _NetType: 连接类型 可以填写 wifi、wifi-ble、cellular、5g、lorawan、ble、ethernet、wifi-ethernet、else、sub_zigbee、sub_ble、sub_433mhz、sub_else、sub_blemesh
        :type NetType: str
        :param _DataProtocol: 数据协议 (1 使用物模型 2 为自定义)
        :type DataProtocol: int
        :param _ProductDesc: 产品描述
        :type ProductDesc: str
        :param _ProjectId: 产品的项目ID
        :type ProjectId: str
        :param _Rate: 平均传输速率
        :type Rate: str
        :param _Period: 期限
        :type Period: str
        """
        self._ProductName = None
        self._CategoryId = None
        self._ProductType = None
        self._EncryptionType = None
        self._NetType = None
        self._DataProtocol = None
        self._ProductDesc = None
        self._ProjectId = None
        self._Rate = None
        self._Period = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def EncryptionType(self):
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def DataProtocol(self):
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def ProductDesc(self):
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._CategoryId = params.get("CategoryId")
        self._ProductType = params.get("ProductType")
        self._EncryptionType = params.get("EncryptionType")
        self._NetType = params.get("NetType")
        self._DataProtocol = params.get("DataProtocol")
        self._ProductDesc = params.get("ProductDesc")
        self._ProjectId = params.get("ProjectId")
        self._Rate = params.get("Rate")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStudioProductResponse(AbstractModel):
    """CreateStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品描述
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = ProductEntry()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class CreateTRTCSignaturesWithRoomIdRequest(AbstractModel):
    """CreateTRTCSignaturesWithRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TRTCUserIds: TRTC进房间的用户名称数组，数组元素不可重复，最长不超过 10 个。
        :type TRTCUserIds: list of str
        :param _RoomId: 房间id
        :type RoomId: str
        """
        self._TRTCUserIds = None
        self._RoomId = None

    @property
    def TRTCUserIds(self):
        return self._TRTCUserIds

    @TRTCUserIds.setter
    def TRTCUserIds(self, TRTCUserIds):
        self._TRTCUserIds = TRTCUserIds

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._TRTCUserIds = params.get("TRTCUserIds")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTRTCSignaturesWithRoomIdResponse(AbstractModel):
    """CreateTRTCSignaturesWithRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TRTCParamList: 返回参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TRTCParamList: list of TRTCParams
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TRTCParamList = None
        self._RequestId = None

    @property
    def TRTCParamList(self):
        return self._TRTCParamList

    @TRTCParamList.setter
    def TRTCParamList(self, TRTCParamList):
        self._TRTCParamList = TRTCParamList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TRTCParamList") is not None:
            self._TRTCParamList = []
            for item in params.get("TRTCParamList"):
                obj = TRTCParams()
                obj._deserialize(item)
                self._TRTCParamList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _Privilege: Topic权限，1发布，2订阅，3订阅和发布
        :type Privilege: int
        """
        self._ProductId = None
        self._TopicName = None
        self._Privilege = None

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


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        self._Privilege = params.get("Privilege")
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
        :type TopicRulePayload: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`
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


class DeleteCloudStorageEventRequest(AbstractModel):
    """DeleteCloudStorageEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _EventId: 事件id
        :type EventId: str
        :param _StartTime: 开始时间，unix时间
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间
        :type EndTime: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._EventId = None
        self._StartTime = None
        self._EndTime = None
        self._UserId = None
        self._ChannelId = None

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
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

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

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._EventId = params.get("EventId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudStorageEventResponse(AbstractModel):
    """DeleteCloudStorageEvent返回参数结构体

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
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _DeviceName: 设备名称。
        :type DeviceName: str
        :param _ForceDelete: 是否删除绑定设备
        :type ForceDelete: bool
        """
        self._ProductId = None
        self._DeviceName = None
        self._ForceDelete = None

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
    def ForceDelete(self):
        return self._ForceDelete

    @ForceDelete.setter
    def ForceDelete(self, ForceDelete):
        self._ForceDelete = ForceDelete


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ForceDelete = params.get("ForceDelete")
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
        :param _ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param _ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ResultMessage = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMessage(self):
        return self._ResultMessage

    @ResultMessage.setter
    def ResultMessage(self, ResultMessage):
        self._ResultMessage = ResultMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._ResultMessage = params.get("ResultMessage")
        self._RequestId = params.get("RequestId")


class DeleteDevicesRequest(AbstractModel):
    """DeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DevicesItems: 多个设备标识
        :type DevicesItems: list of DevicesItem
        """
        self._DevicesItems = None

    @property
    def DevicesItems(self):
        return self._DevicesItems

    @DevicesItems.setter
    def DevicesItems(self, DevicesItems):
        self._DevicesItems = DevicesItems


    def _deserialize(self, params):
        if params.get("DevicesItems") is not None:
            self._DevicesItems = []
            for item in params.get("DevicesItems"):
                obj = DevicesItem()
                obj._deserialize(item)
                self._DevicesItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDevicesResponse(AbstractModel):
    """DeleteDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param _ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ResultMessage = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMessage(self):
        return self._ResultMessage

    @ResultMessage.setter
    def ResultMessage(self, ResultMessage):
        self._ResultMessage = ResultMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._ResultMessage = params.get("ResultMessage")
        self._RequestId = params.get("RequestId")


class DeleteFenceBindRequest(AbstractModel):
    """DeleteFenceBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _Items: 围栏绑定的产品信息
        :type Items: list of FenceBindProductItem
        """
        self._FenceId = None
        self._Items = None

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._FenceId = params.get("FenceId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFenceBindResponse(AbstractModel):
    """DeleteFenceBind返回参数结构体

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


class DeleteLoRaFrequencyRequest(AbstractModel):
    """DeleteLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FreqId: 频点唯一ID
        :type FreqId: str
        """
        self._FreqId = None

    @property
    def FreqId(self):
        return self._FreqId

    @FreqId.setter
    def FreqId(self, FreqId):
        self._FreqId = FreqId


    def _deserialize(self, params):
        self._FreqId = params.get("FreqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoRaFrequencyResponse(AbstractModel):
    """DeleteLoRaFrequency返回参数结构体

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


class DeleteLoRaGatewayRequest(AbstractModel):
    """DeleteLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: LoRa 网关 Id
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoRaGatewayResponse(AbstractModel):
    """DeleteLoRaGateway返回参数结构体

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


class DeletePositionFenceRequest(AbstractModel):
    """DeletePositionFence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _FenceId: 围栏Id
        :type FenceId: int
        """
        self._SpaceId = None
        self._FenceId = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._FenceId = params.get("FenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePositionFenceResponse(AbstractModel):
    """DeletePositionFence返回参数结构体

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


class DeletePositionSpaceRequest(AbstractModel):
    """DeletePositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePositionSpaceResponse(AbstractModel):
    """DeletePositionSpace返回参数结构体

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


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

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


class DeleteStudioProductRequest(AbstractModel):
    """DeleteStudioProduct请求参数结构体

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
        


class DeleteStudioProductResponse(AbstractModel):
    """DeleteStudioProduct返回参数结构体

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


class DeleteTopicPolicyRequest(AbstractModel):
    """DeleteTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TopicName: Topic名称
        :type TopicName: str
        """
        self._ProductId = None
        self._TopicName = None

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


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicPolicyResponse(AbstractModel):
    """DeleteTopicPolicy返回参数结构体

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


class DescribeBatchProductionRequest(AbstractModel):
    """DescribeBatchProduction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _BatchProductionId: 量产ID
        :type BatchProductionId: str
        """
        self._ProductId = None
        self._BatchProductionId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchProductionId(self):
        return self._BatchProductionId

    @BatchProductionId.setter
    def BatchProductionId(self, BatchProductionId):
        self._BatchProductionId = BatchProductionId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._BatchProductionId = params.get("BatchProductionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchProductionResponse(AbstractModel):
    """DescribeBatchProduction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchCnt: 量产数量。
        :type BatchCnt: int
        :param _BurnMethod: 烧录方式。
        :type BurnMethod: int
        :param _CreateTime: 创建时间。
        :type CreateTime: int
        :param _DownloadUrl: 下载URL。
        :type DownloadUrl: str
        :param _GenerationMethod: 生成方式。
        :type GenerationMethod: int
        :param _UploadUrl: 上传URL。
        :type UploadUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchCnt = None
        self._BurnMethod = None
        self._CreateTime = None
        self._DownloadUrl = None
        self._GenerationMethod = None
        self._UploadUrl = None
        self._RequestId = None

    @property
    def BatchCnt(self):
        return self._BatchCnt

    @BatchCnt.setter
    def BatchCnt(self, BatchCnt):
        self._BatchCnt = BatchCnt

    @property
    def BurnMethod(self):
        return self._BurnMethod

    @BurnMethod.setter
    def BurnMethod(self, BurnMethod):
        self._BurnMethod = BurnMethod

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def GenerationMethod(self):
        return self._GenerationMethod

    @GenerationMethod.setter
    def GenerationMethod(self, GenerationMethod):
        self._GenerationMethod = GenerationMethod

    @property
    def UploadUrl(self):
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchCnt = params.get("BatchCnt")
        self._BurnMethod = params.get("BurnMethod")
        self._CreateTime = params.get("CreateTime")
        self._DownloadUrl = params.get("DownloadUrl")
        self._GenerationMethod = params.get("GenerationMethod")
        self._UploadUrl = params.get("UploadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBindedProductsRequest(AbstractModel):
    """DescribeBindedProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _ProductSource: 是否跨账号绑定产品
        :type ProductSource: int
        """
        self._GatewayProductId = None
        self._Offset = None
        self._Limit = None
        self._ProductSource = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

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
    def ProductSource(self):
        return self._ProductSource

    @ProductSource.setter
    def ProductSource(self, ProductSource):
        self._ProductSource = ProductSource


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductSource = params.get("ProductSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindedProductsResponse(AbstractModel):
    """DescribeBindedProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 当前分页的子产品数组
        :type Products: list of BindProductInfo
        :param _Total: 绑定的子产品总数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._Total = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceCallbackRequest(AbstractModel):
    """DescribeCloudStorageAIServiceCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
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
        


class DescribeCloudStorageAIServiceCallbackResponse(AbstractModel):
    """DescribeCloudStorageAIServiceCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 推送类型。http：HTTP 回调
        :type Type: str
        :param _CallbackUrl: HTTP 回调 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        :param _CallbackToken: HTTP 回调鉴权 Token
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Type = None
        self._CallbackUrl = None
        self._CallbackToken = None
        self._RequestId = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def CallbackToken(self):
        return self._CallbackToken

    @CallbackToken.setter
    def CallbackToken(self, CallbackToken):
        self._CallbackToken = CallbackToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._CallbackUrl = params.get("CallbackUrl")
        self._CallbackToken = params.get("CallbackToken")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceRequest(AbstractModel):
    """DescribeCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
        :type ServiceType: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None

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
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageAIServiceResponse(AbstractModel):
    """DescribeCloudStorageAIService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 云存 AI 套餐类型。可能取值：

- `1`：全时套餐
- `2`：事件套餐
- `3`：低功耗套餐
        :type Type: int
        :param _Status: 云存 AI 套餐生效状态。可能取值：

- `0`：未开通或已过期
- `1`：生效中
        :type Status: int
        :param _ExpireTime: 云存 AI 套餐过期时间 UNIX 时间戳
        :type ExpireTime: int
        :param _UserId: 用户 ID
        :type UserId: str
        :param _Enabled: 视频分析启用状态
        :type Enabled: bool
        :param _Config: 视频分析配置参数
        :type Config: str
        :param _ROI: 视频分析识别区域
        :type ROI: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Type = None
        self._Status = None
        self._ExpireTime = None
        self._UserId = None
        self._Enabled = None
        self._Config = None
        self._ROI = None
        self._RequestId = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ROI(self):
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._UserId = params.get("UserId")
        self._Enabled = params.get("Enabled")
        self._Config = params.get("Config")
        self._ROI = params.get("ROI")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceTaskRequest(AbstractModel):
    """DescribeCloudStorageAIServiceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageAIServiceTaskResponse(AbstractModel):
    """DescribeCloudStorageAIServiceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfo: 任务信息
        :type TaskInfo: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTask`
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
            self._TaskInfo = CloudStorageAIServiceTask()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceTasksRequest(AbstractModel):
    """DescribeCloudStorageAIServiceTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
        :type ServiceType: str
        :param _Limit: 分页拉取数量
        :type Limit: int
        :param _Offset: 分页拉取偏移
        :type Offset: int
        :param _Status: 任务状态。可选值：
- （不传）：查询全部状态的任务
- `1`：失败
- `2`：成功但结果为空
- `3`：成功且结果非空
- `4`：执行中
        :type Status: int
        :param _UserId: 用户 ID
        :type UserId: str
        :param _ChannelId: 通道 ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._UserId = None
        self._ChannelId = None

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
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageAIServiceTasksResponse(AbstractModel):
    """DescribeCloudStorageAIServiceTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务列表
        :type Tasks: list of CloudStorageAIServiceTask
        :param _Total: 任务数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._Total = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = CloudStorageAIServiceTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageDateRequest(AbstractModel):
    """DescribeCloudStorageDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None
        self._ChannelId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageDateResponse(AbstractModel):
    """DescribeCloudStorageDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云存日期数组，["2021-01-05","2021-01-06"]
        :type Data: list of str
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


class DescribeCloudStorageEventsRequest(AbstractModel):
    """DescribeCloudStorageEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param _EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param _Context: 请求上下文, 用作查询游标
        :type Context: str
        :param _Size: 查询数据项目的最大数量, 默认为10。假设传Size=10，返回的实际事件数量为N，则 5 <= N <= 10。
        :type Size: int
        :param _EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _ChannelId: 通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._Size = None
        self._EventId = None
        self._UserId = None
        self._ChannelId = None

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

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._Size = params.get("Size")
        self._EventId = params.get("EventId")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageEventsResponse(AbstractModel):
    """DescribeCloudStorageEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 云存事件列表
        :type Events: list of CloudStorageEvent
        :param _Context: 请求上下文, 用作查询游标
        :type Context: str
        :param _Listover: 拉取结果是否已经结束
        :type Listover: bool
        :param _Total: 内部结果数量，并不等同于事件总数。
        :type Total: int
        :param _VideoURL: 视频播放URL
        :type VideoURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._Context = None
        self._Listover = None
        self._Total = None
        self._VideoURL = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

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
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def VideoURL(self):
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = CloudStorageEvent()
                obj._deserialize(item)
                self._Events.append(obj)
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        self._Total = params.get("Total")
        self._VideoURL = params.get("VideoURL")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageMultiThumbnailRequest(AbstractModel):
    """DescribeCloudStorageMultiThumbnail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _MultiThumbnail: 多个缩略图文件名根据 | 分割
        :type MultiThumbnail: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._MultiThumbnail = None

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
    def MultiThumbnail(self):
        return self._MultiThumbnail

    @MultiThumbnail.setter
    def MultiThumbnail(self, MultiThumbnail):
        self._MultiThumbnail = MultiThumbnail


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._MultiThumbnail = params.get("MultiThumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageMultiThumbnailResponse(AbstractModel):
    """DescribeCloudStorageMultiThumbnail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ThumbnailURLInfoList: 缩略图访问地址
        :type ThumbnailURLInfoList: list of ThumbnailURLInfoList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ThumbnailURLInfoList = None
        self._RequestId = None

    @property
    def ThumbnailURLInfoList(self):
        return self._ThumbnailURLInfoList

    @ThumbnailURLInfoList.setter
    def ThumbnailURLInfoList(self, ThumbnailURLInfoList):
        self._ThumbnailURLInfoList = ThumbnailURLInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ThumbnailURLInfoList") is not None:
            self._ThumbnailURLInfoList = []
            for item in params.get("ThumbnailURLInfoList"):
                obj = ThumbnailURLInfoList()
                obj._deserialize(item)
                self._ThumbnailURLInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageOrderRequest(AbstractModel):
    """DescribeCloudStorageOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单id
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageOrderResponse(AbstractModel):
    """DescribeCloudStorageOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 云存套餐开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _ExpireTime: 云存套餐过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _PackageId: 套餐id
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _Status: 套餐状态
0：等待生效
1: 已过期
2:生效
        :type Status: int
        :param _ChannelId: 通道id
        :type ChannelId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._ExpireTime = None
        self._PackageId = None
        self._Status = None
        self._ChannelId = None
        self._RequestId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._PackageId = params.get("PackageId")
        self._Status = params.get("Status")
        self._ChannelId = params.get("ChannelId")
        self._RequestId = params.get("RequestId")


class DescribeCloudStoragePackageConsumeDetailsRequest(AbstractModel):
    """DescribeCloudStoragePackageConsumeDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始日期
        :type StartDate: str
        :param _EndDate: 结束日期
        :type EndDate: str
        """
        self._StartDate = None
        self._EndDate = None

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStoragePackageConsumeDetailsResponse(AbstractModel):
    """DescribeCloudStoragePackageConsumeDetails返回参数结构体

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


class DescribeCloudStoragePackageConsumeStatsRequest(AbstractModel):
    """DescribeCloudStoragePackageConsumeStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始日期
        :type StartDate: str
        :param _EndDate: 结束日期，开始与结束日期间隔不可超过一年
        :type EndDate: str
        """
        self._StartDate = None
        self._EndDate = None

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStoragePackageConsumeStatsResponse(AbstractModel):
    """DescribeCloudStoragePackageConsumeStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Stats: 统计列表详情
        :type Stats: list of PackageConsumeStat
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Stats = None
        self._RequestId = None

    @property
    def Stats(self):
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Stats") is not None:
            self._Stats = []
            for item in params.get("Stats"):
                obj = PackageConsumeStat()
                obj._deserialize(item)
                self._Stats.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageRequest(AbstractModel):
    """DescribeCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 云存用户ID
        :type UserId: str
        :param _ChannelId: 通道ID 非NVR设备不填 NVR设备必填 默认为无	
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None
        self._ChannelId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageResponse(AbstractModel):
    """DescribeCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 云存开启状态，1为开启，0为未开启或已过期
        :type Status: int
        :param _Type: 云存类型，1为全时云存，2为事件云存
        :type Type: int
        :param _ExpireTime: 云存套餐过期时间
        :type ExpireTime: int
        :param _ShiftDuration: 云存回看时长
        :type ShiftDuration: int
        :param _UserId: 云存用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Type = None
        self._ExpireTime = None
        self._ShiftDuration = None
        self._UserId = None
        self._RequestId = None

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
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ShiftDuration(self):
        return self._ShiftDuration

    @ShiftDuration.setter
    def ShiftDuration(self, ShiftDuration):
        self._ShiftDuration = ShiftDuration

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._ShiftDuration = params.get("ShiftDuration")
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageStreamDataRequest(AbstractModel):
    """DescribeCloudStorageStreamData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _StartTime: 图片流事件开始时间
        :type StartTime: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._StartTime = None

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
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageStreamDataResponse(AbstractModel):
    """DescribeCloudStorageStreamData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoStream: 图片流视频地址
        :type VideoStream: str
        :param _AudioStream: 图片流音频地址
        :type AudioStream: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VideoStream = None
        self._AudioStream = None
        self._RequestId = None

    @property
    def VideoStream(self):
        return self._VideoStream

    @VideoStream.setter
    def VideoStream(self, VideoStream):
        self._VideoStream = VideoStream

    @property
    def AudioStream(self):
        return self._AudioStream

    @AudioStream.setter
    def AudioStream(self, AudioStream):
        self._AudioStream = AudioStream

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VideoStream = params.get("VideoStream")
        self._AudioStream = params.get("AudioStream")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageThumbnailListRequest(AbstractModel):
    """DescribeCloudStorageThumbnailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ThumbnailList: 缩略图文件名列表
        :type ThumbnailList: list of str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ThumbnailList = None

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
    def ThumbnailList(self):
        return self._ThumbnailList

    @ThumbnailList.setter
    def ThumbnailList(self, ThumbnailList):
        self._ThumbnailList = ThumbnailList


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ThumbnailList = params.get("ThumbnailList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageThumbnailListResponse(AbstractModel):
    """DescribeCloudStorageThumbnailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ThumbnailURLInfoList: 缩略图访问地址
        :type ThumbnailURLInfoList: list of ThumbnailURLInfoList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ThumbnailURLInfoList = None
        self._RequestId = None

    @property
    def ThumbnailURLInfoList(self):
        return self._ThumbnailURLInfoList

    @ThumbnailURLInfoList.setter
    def ThumbnailURLInfoList(self, ThumbnailURLInfoList):
        self._ThumbnailURLInfoList = ThumbnailURLInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ThumbnailURLInfoList") is not None:
            self._ThumbnailURLInfoList = []
            for item in params.get("ThumbnailURLInfoList"):
                obj = ThumbnailURLInfoList()
                obj._deserialize(item)
                self._ThumbnailURLInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageThumbnailRequest(AbstractModel):
    """DescribeCloudStorageThumbnail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Thumbnail: 缩略图文件名
        :type Thumbnail: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Thumbnail = None

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
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageThumbnailResponse(AbstractModel):
    """DescribeCloudStorageThumbnail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ThumbnailURL: 缩略图访问地址
        :type ThumbnailURL: str
        :param _ExpireTime: 缩略图访问地址的过期时间
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ThumbnailURL = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def ThumbnailURL(self):
        return self._ThumbnailURL

    @ThumbnailURL.setter
    def ThumbnailURL(self, ThumbnailURL):
        self._ThumbnailURL = ThumbnailURL

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ThumbnailURL = params.get("ThumbnailURL")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageTimeRequest(AbstractModel):
    """DescribeCloudStorageTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Date: 云存日期，例如"2020-01-05"
        :type Date: str
        :param _StartTime: 开始时间，unix时间
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间
        :type EndTime: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Date = None
        self._StartTime = None
        self._EndTime = None
        self._UserId = None
        self._ChannelId = None

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
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

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

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Date = params.get("Date")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageTimeResponse(AbstractModel):
    """DescribeCloudStorageTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回数据
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageTimeData`
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
        if params.get("Data") is not None:
            self._Data = CloudStorageTimeData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageUsersRequest(AbstractModel):
    """DescribeCloudStorageUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Limit: 分页拉取数量
        :type Limit: int
        :param _Offset: 分页拉取偏移
        :type Offset: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Limit = None
        self._Offset = None

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageUsersResponse(AbstractModel):
    """DescribeCloudStorageUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 用户总数
        :type TotalCount: int
        :param _Users: 用户信息
        :type Users: list of CloudStorageUserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Users = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = CloudStorageUserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceBindGatewayRequest(AbstractModel):
    """DescribeDeviceBindGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
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
        


class DescribeDeviceBindGatewayResponse(AbstractModel):
    """DescribeDeviceBindGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备名
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayDeviceName: str
        :param _GatewayName: 网关产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayName: str
        :param _GatewayProductOwnerName: 设备对应产品所属的主账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayProductOwnerName: str
        :param _GatewayProductOwnerUin: 设备对应产品所属的主账号 UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayProductOwnerUin: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._GatewayName = None
        self._GatewayProductOwnerName = None
        self._GatewayProductOwnerUin = None
        self._RequestId = None

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
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def GatewayProductOwnerName(self):
        return self._GatewayProductOwnerName

    @GatewayProductOwnerName.setter
    def GatewayProductOwnerName(self, GatewayProductOwnerName):
        self._GatewayProductOwnerName = GatewayProductOwnerName

    @property
    def GatewayProductOwnerUin(self):
        return self._GatewayProductOwnerUin

    @GatewayProductOwnerUin.setter
    def GatewayProductOwnerUin(self, GatewayProductOwnerUin):
        self._GatewayProductOwnerUin = GatewayProductOwnerUin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._GatewayName = params.get("GatewayName")
        self._GatewayProductOwnerName = params.get("GatewayProductOwnerName")
        self._GatewayProductOwnerUin = params.get("GatewayProductOwnerUin")
        self._RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 区间开始时间（Unix 时间戳，毫秒级）
        :type MinTime: int
        :param _MaxTime: 区间结束时间（Unix 时间戳，毫秒级）
        :type MaxTime: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FieldName: 属性字段名称，对应数据模板中功能属性的标识符
        :type FieldName: str
        :param _Limit: 返回条数
        :type Limit: int
        :param _Context: 检索上下文
        :type Context: str
        """
        self._MinTime = None
        self._MaxTime = None
        self._ProductId = None
        self._DeviceName = None
        self._FieldName = None
        self._Limit = None
        self._Context = None

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
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._FieldName = params.get("FieldName")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param _Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param _Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FieldName = None
        self._Listover = None
        self._Context = None
        self._Results = None
        self._RequestId = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

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
        self._FieldName = params.get("FieldName")
        self._Listover = params.get("Listover")
        self._Context = params.get("Context")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._DeviceId = None

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
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备数据
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


class DescribeDeviceFirmWareRequest(AbstractModel):
    """DescribeDeviceFirmWare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _DeviceName: 设备名称。
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
        


class DescribeDeviceFirmWareResponse(AbstractModel):
    """DescribeDeviceFirmWare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 固件信息
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


class DescribeDeviceFirmwaresRequest(AbstractModel):
    """DescribeDeviceFirmwares请求参数结构体

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
        


class DescribeDeviceFirmwaresResponse(AbstractModel):
    """DescribeDeviceFirmwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Firmwares: 固件信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Firmwares: list of DeviceFirmwareInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Firmwares = None
        self._RequestId = None

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
        if params.get("Firmwares") is not None:
            self._Firmwares = []
            for item in params.get("Firmwares"):
                obj = DeviceFirmwareInfo()
                obj._deserialize(item)
                self._Firmwares.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceLocationSolveRequest(AbstractModel):
    """DescribeDeviceLocationSolve请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _LocationType: 定位解析类型，wifi或GNSSNavigation
        :type LocationType: str
        :param _GNSSNavigation: LoRaEdge卫星导航电文
        :type GNSSNavigation: str
        :param _WiFiInfo: wifi信息
        :type WiFiInfo: list of WifiInfo
        """
        self._ProductId = None
        self._DeviceName = None
        self._LocationType = None
        self._GNSSNavigation = None
        self._WiFiInfo = None

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
    def LocationType(self):
        return self._LocationType

    @LocationType.setter
    def LocationType(self, LocationType):
        self._LocationType = LocationType

    @property
    def GNSSNavigation(self):
        return self._GNSSNavigation

    @GNSSNavigation.setter
    def GNSSNavigation(self, GNSSNavigation):
        self._GNSSNavigation = GNSSNavigation

    @property
    def WiFiInfo(self):
        return self._WiFiInfo

    @WiFiInfo.setter
    def WiFiInfo(self, WiFiInfo):
        self._WiFiInfo = WiFiInfo


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._LocationType = params.get("LocationType")
        self._GNSSNavigation = params.get("GNSSNavigation")
        if params.get("WiFiInfo") is not None:
            self._WiFiInfo = []
            for item in params.get("WiFiInfo"):
                obj = WifiInfo()
                obj._deserialize(item)
                self._WiFiInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceLocationSolveResponse(AbstractModel):
    """DescribeDeviceLocationSolve返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Longitude: 经度
        :type Longitude: float
        :param _Latitude: 纬度
        :type Latitude: float
        :param _LocationType: 类型
        :type LocationType: str
        :param _Accuracy: 误差精度预估，单位为米
注意：此字段可能返回 null，表示取不到有效值。
        :type Accuracy: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Longitude = None
        self._Latitude = None
        self._LocationType = None
        self._Accuracy = None
        self._RequestId = None

    @property
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def LocationType(self):
        return self._LocationType

    @LocationType.setter
    def LocationType(self, LocationType):
        self._LocationType = LocationType

    @property
    def Accuracy(self):
        return self._Accuracy

    @Accuracy.setter
    def Accuracy(self, Accuracy):
        self._Accuracy = Accuracy

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._LocationType = params.get("LocationType")
        self._Accuracy = params.get("Accuracy")
        self._RequestId = params.get("RequestId")


class DescribeDevicePackagesRequest(AbstractModel):
    """DescribeDevicePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Limit: 分页拉取数量
        :type Limit: int
        :param _Offset: 分页拉取偏移
        :type Offset: int
        :param _CSUserId: 用户id
        :type CSUserId: str
        :param _ChannelId: 通道id
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Limit = None
        self._Offset = None
        self._CSUserId = None
        self._ChannelId = None

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CSUserId(self):
        return self._CSUserId

    @CSUserId.setter
    def CSUserId(self, CSUserId):
        self._CSUserId = CSUserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CSUserId = params.get("CSUserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePackagesResponse(AbstractModel):
    """DescribeDevicePackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 有效云存套餐数量
        :type TotalCount: int
        :param _Packages: 有效云存套餐列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Packages: list of PackageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Packages = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Packages(self):
        return self._Packages

    @Packages.setter
    def Packages(self, Packages):
        self._Packages = Packages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Packages") is not None:
            self._Packages = []
            for item in params.get("Packages"):
                obj = PackageInfo()
                obj._deserialize(item)
                self._Packages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicePositionListRequest(AbstractModel):
    """DescribeDevicePositionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductIdList: 产品标识列表
        :type ProductIdList: list of str
        :param _CoordinateType: 坐标类型
        :type CoordinateType: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页的大小
        :type Limit: int
        """
        self._ProductIdList = None
        self._CoordinateType = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductIdList(self):
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def CoordinateType(self):
        return self._CoordinateType

    @CoordinateType.setter
    def CoordinateType(self, CoordinateType):
        self._CoordinateType = CoordinateType

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
        self._ProductIdList = params.get("ProductIdList")
        self._CoordinateType = params.get("CoordinateType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePositionListResponse(AbstractModel):
    """DescribeDevicePositionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Positions: 产品设备位置信息列表
        :type Positions: list of ProductDevicesPositionItem
        :param _Total: 产品设备位置信息的数目
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Positions = None
        self._Total = None
        self._RequestId = None

    @property
    def Positions(self):
        return self._Positions

    @Positions.setter
    def Positions(self, Positions):
        self._Positions = Positions

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
        if params.get("Positions") is not None:
            self._Positions = []
            for item in params.get("Positions"):
                obj = ProductDevicesPositionItem()
                obj._deserialize(item)
                self._Positions.append(obj)
        self._Total = params.get("Total")
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
        :param _DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._DeviceId = None

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
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Device: 设备信息
        :type Device: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Device = None
        self._RequestId = None

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self._Device = DeviceInfo()
            self._Device._deserialize(params.get("Device"))
        self._RequestId = params.get("RequestId")


class DescribeFenceBindListRequest(AbstractModel):
    """DescribeFenceBindList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _Offset: 翻页偏移量，0起始
        :type Offset: int
        :param _Limit: 最大返回结果数
        :type Limit: int
        """
        self._FenceId = None
        self._Offset = None
        self._Limit = None

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

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
        self._FenceId = params.get("FenceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFenceBindListResponse(AbstractModel):
    """DescribeFenceBindList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 围栏绑定的产品设备列表
        :type List: list of FenceBindProductItem
        :param _Total: 围栏绑定的设备总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFenceEventListRequest(AbstractModel):
    """DescribeFenceEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 围栏告警信息的查询起始时间，Unix时间，单位为毫秒
        :type StartTime: int
        :param _EndTime: 围栏告警信息的查询结束时间，Unix时间，单位为毫秒
        :type EndTime: int
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _Offset: 翻页偏移量，0起始
        :type Offset: int
        :param _Limit: 最大返回结果数
        :type Limit: int
        :param _ProductId: 告警对应的产品Id
        :type ProductId: str
        :param _DeviceName: 告警对应的设备名称
        :type DeviceName: str
        """
        self._StartTime = None
        self._EndTime = None
        self._FenceId = None
        self._Offset = None
        self._Limit = None
        self._ProductId = None
        self._DeviceName = None

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

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

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

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._FenceId = params.get("FenceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFenceEventListResponse(AbstractModel):
    """DescribeFenceEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 围栏告警事件列表
        :type List: list of FenceEventItem
        :param _Total: 围栏告警事件总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FenceEventItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
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
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
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
        :param _FwType: 固件升级模块
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

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
        :param _CreateTime: 固件任务创建时间，单位：秒
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
        :param _OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalVersion: str
        :param _CreateUserId: 创建账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _CreatorNickName: 创建账号ID昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
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
        self._CreateUserId = None
        self._CreatorNickName = None
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
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

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
        self._CreateUserId = params.get("CreateUserId")
        self._CreatorNickName = params.get("CreatorNickName")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareUpdateStatusRequest(AbstractModel):
    """DescribeFirmwareUpdateStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID。
        :type ProductId: str
        :param _DeviceName: 设备名。
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
        


class DescribeFirmwareUpdateStatusResponse(AbstractModel):
    """DescribeFirmwareUpdateStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriVersion: 升级任务源版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriVersion: str
        :param _DstVersion: 升级任务目标版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type DstVersion: str
        :param _Status: 升级状态：- 0：设备离线。- 1：待处理。- 2：消息下发成功。- 3：下载中。- 4：烧录中。- 5：失败。- 6：升级完成。- 7：正在处理中。- 8：等待用户确认。- 10：升级超时。- 20：下载完成。
        :type Status: int
        :param _Percent: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriVersion = None
        self._DstVersion = None
        self._Status = None
        self._Percent = None
        self._RequestId = None

    @property
    def OriVersion(self):
        return self._OriVersion

    @OriVersion.setter
    def OriVersion(self, OriVersion):
        self._OriVersion = OriVersion

    @property
    def DstVersion(self):
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

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

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriVersion = params.get("OriVersion")
        self._DstVersion = params.get("DstVersion")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
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
        :param _ProductId: 子产品的ID
        :type ProductId: str
        :param _Offset: 分页的偏移
        :type Offset: int
        :param _Limit: 分页的页大小
        :type Limit: int
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._ProductId = None
        self._Offset = None
        self._Limit = None

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
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
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
        


class DescribeGatewayBindDevicesResponse(AbstractModel):
    """DescribeGatewayBindDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 子设备信息。
        :type Devices: list of BindDeviceInfo
        :param _Total: 子设备总数。
        :type Total: int
        :param _ProductName: 子设备所属的产品名。
        :type ProductName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._Total = None
        self._ProductName = None
        self._RequestId = None

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = BindDeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._Total = params.get("Total")
        self._ProductName = params.get("ProductName")
        self._RequestId = params.get("RequestId")


class DescribeGatewaySubDeviceListRequest(AbstractModel):
    """DescribeGatewaySubDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备名称
        :type GatewayDeviceName: str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页的大小
        :type Limit: int
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewaySubDeviceListResponse(AbstractModel):
    """DescribeGatewaySubDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 设备的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _DeviceList: 设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: list of FamilySubDevice
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = FamilySubDevice()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewaySubProductsRequest(AbstractModel):
    """DescribeGatewaySubProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param _Offset: 分页的偏移量
        :type Offset: int
        :param _Limit: 分页的大小
        :type Limit: int
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _ProductSource: 是否跨账号产品
        :type ProductSource: int
        """
        self._GatewayProductId = None
        self._Offset = None
        self._Limit = None
        self._ProjectId = None
        self._ProductSource = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductSource(self):
        return self._ProductSource

    @ProductSource.setter
    def ProductSource(self, ProductSource):
        self._ProductSource = ProductSource


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        self._ProductSource = params.get("ProductSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewaySubProductsResponse(AbstractModel):
    """DescribeGatewaySubProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 当前分页的可绑定或解绑的产品信息。
        :type Products: list of BindProductInfo
        :param _Total: 可绑定或解绑的产品总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._Total = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Include: 附加查询返回包含字段值，不传返回0，有效值 ProductNum、ProjectNum、UsedDeviceNum、TotalDevice、ActivateDevice
        :type Include: list of str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProductId: 产品ID，-1 代表全部产品
        :type ProductId: str
        """
        self._InstanceId = None
        self._Include = None
        self._ProjectId = None
        self._ProductId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Include(self):
        return self._Include

    @Include.setter
    def Include(self, Include):
        self._Include = Include

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Include = params.get("Include")
        self._ProjectId = params.get("ProjectId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.InstanceDetail`
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
        if params.get("Data") is not None:
            self._Data = InstanceDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeLoRaFrequencyRequest(AbstractModel):
    """DescribeLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FreqId: 频点唯一ID
        :type FreqId: str
        """
        self._FreqId = None

    @property
    def FreqId(self):
        return self._FreqId

    @FreqId.setter
    def FreqId(self, FreqId):
        self._FreqId = FreqId


    def _deserialize(self, params):
        self._FreqId = params.get("FreqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoRaFrequencyResponse(AbstractModel):
    """DescribeLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回详情项
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
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
        if params.get("Data") is not None:
            self._Data = LoRaFrequencyEntry()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

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
        


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 产品数据模板
        :type Model: :class:`tencentcloud.iotexplorer.v20190423.models.ProductModelDefinition`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Model = None
        self._RequestId = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ProductModelDefinition()
            self._Model._deserialize(params.get("Model"))
        self._RequestId = params.get("RequestId")


class DescribePackageConsumeTaskRequest(AbstractModel):
    """DescribePackageConsumeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackageConsumeTaskResponse(AbstractModel):
    """DescribePackageConsumeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _URL: 文件下载的url，文件详情是套餐包消耗详情
        :type URL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._URL = None
        self._RequestId = None

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._RequestId = params.get("RequestId")


class DescribePackageConsumeTasksRequest(AbstractModel):
    """DescribePackageConsumeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页单页量
        :type Limit: int
        :param _Offset: 分页的偏移量，第一页为0
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackageConsumeTasksResponse(AbstractModel):
    """DescribePackageConsumeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _List: 任务列表
        :type List: list of PackageConsumeTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PackageConsumeTask()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePositionFenceListRequest(AbstractModel):
    """DescribePositionFenceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _Offset: 翻页偏移量，0起始
        :type Offset: int
        :param _Limit: 最大返回结果数
        :type Limit: int
        """
        self._SpaceId = None
        self._Offset = None
        self._Limit = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

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
        self._SpaceId = params.get("SpaceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePositionFenceListResponse(AbstractModel):
    """DescribePositionFenceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 围栏列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PositionFenceInfo
        :param _Total: 围栏数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PositionFenceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProductCloudStorageAIServiceRequest(AbstractModel):
    """DescribeProductCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
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
        


class DescribeProductCloudStorageAIServiceResponse(AbstractModel):
    """DescribeProductCloudStorageAIService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Enabled: 开通状态
        :type Enabled: bool
        :param _Available: 当前账号是否可开通
        :type Available: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Enabled = None
        self._Available = None
        self._RequestId = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Available = params.get("Available")
        self._RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Project: 返回信息
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntryEx`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Project = None
        self._RequestId = None

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self._Project = ProjectEntryEx()
            self._Project._deserialize(params.get("Project"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceFenceEventListRequest(AbstractModel):
    """DescribeSpaceFenceEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _StartTime: 围栏告警信息的查询起始时间，Unix时间，单位为毫秒
        :type StartTime: int
        :param _EndTime: 围栏告警信息的查询结束时间，Unix时间，单位为毫秒
        :type EndTime: int
        :param _Offset: 翻页偏移量，0起始
        :type Offset: int
        :param _Limit: 最大返回结果数
        :type Limit: int
        """
        self._SpaceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

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
        self._SpaceId = params.get("SpaceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceFenceEventListResponse(AbstractModel):
    """DescribeSpaceFenceEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 围栏告警事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of FenceEventItem
        :param _Total: 围栏告警事件总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FenceEventItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeStudioProductRequest(AbstractModel):
    """DescribeStudioProduct请求参数结构体

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
        


class DescribeStudioProductResponse(AbstractModel):
    """DescribeStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品详情
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = ProductEntry()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class DescribeTopicPolicyRequest(AbstractModel):
    """DescribeTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TopicName: Topic名字
        :type TopicName: str
        """
        self._ProductId = None
        self._TopicName = None

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


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicPolicyResponse(AbstractModel):
    """DescribeTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _Privilege: Topic权限
        :type Privilege: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductId = None
        self._TopicName = None
        self._Privilege = None
        self._RequestId = None

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        self._Privilege = params.get("Privilege")
        self._RequestId = params.get("RequestId")


class DescribeTopicRuleRequest(AbstractModel):
    """DescribeTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称。
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
        


class DescribeTopicRuleResponse(AbstractModel):
    """DescribeTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRule`
        :param _CamTag: 规则绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type CamTag: list of CamTag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._CamTag = None
        self._RequestId = None

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def CamTag(self):
        return self._CamTag

    @CamTag.setter
    def CamTag(self, CamTag):
        self._CamTag = CamTag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = TopicRule()
            self._Rule._deserialize(params.get("Rule"))
        if params.get("CamTag") is not None:
            self._CamTag = []
            for item in params.get("CamTag"):
                obj = CamTag()
                obj._deserialize(item)
                self._CamTag.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceActiveResult(AbstractModel):
    """设备激活结果数据

    """

    def __init__(self):
        r"""
        :param _ModelId: 模版ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _Sn: SN信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Sn: str
        :param _ErrCode: 设备激活状态，0：激活成功；9800020：设备数超出限制；9800040：资源包类型和设备类型不匹配；9800039：资源包余额不足；9800037：激活码序号已使用；9800038：设备有效期超出限制；
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        """
        self._ModelId = None
        self._Sn = None
        self._ErrCode = None
        self._ExpireTime = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Sn(self):
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Sn = params.get("Sn")
        self._ErrCode = params.get("ErrCode")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceData(AbstractModel):
    """DeviceData

    """

    def __init__(self):
        r"""
        :param _DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param _DeviceName: 设备名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevicePrivateKey: str
        :param _DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevicePsk: str
        """
        self._DeviceCert = None
        self._DeviceName = None
        self._DevicePrivateKey = None
        self._DevicePsk = None

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevicePrivateKey(self):
        return self._DevicePrivateKey

    @DevicePrivateKey.setter
    def DevicePrivateKey(self, DevicePrivateKey):
        self._DevicePrivateKey = DevicePrivateKey

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk


    def _deserialize(self, params):
        self._DeviceCert = params.get("DeviceCert")
        self._DeviceName = params.get("DeviceName")
        self._DevicePrivateKey = params.get("DevicePrivateKey")
        self._DevicePsk = params.get("DevicePsk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        r"""
        :param _Time: 时间点，毫秒时间戳
        :type Time: str
        :param _Value: 字段取值
        :type Value: str
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceFirmwareInfo(AbstractModel):
    """设备固件信息

    """

    def __init__(self):
        r"""
        :param _FwType: 固件类型
        :type FwType: str
        :param _Version: 固件版本
        :type Version: str
        :param _UpdateTime: 最后更新时间
        :type UpdateTime: int
        """
        self._FwType = None
        self._Version = None
        self._UpdateTime = None

    @property
    def FwType(self):
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._FwType = params.get("FwType")
        self._Version = params.get("Version")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Status: 0: 离线, 1: 在线, 2: 获取失败, 3 未激活
        :type Status: int
        :param _DevicePsk: 设备密钥，密钥加密的设备返回
        :type DevicePsk: str
        :param _FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param _LoginTime: 最后一次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginTime: int
        :param _CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Version: 设备固件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _DeviceCert: 设备证书
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param _LogLevel: 日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param _DevAddr: LoRaWAN 设备地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DevAddr: str
        :param _AppKey: LoRaWAN 应用密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param _DevEUI: LoRaWAN 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DevEUI: str
        :param _AppSKey: LoRaWAN 应用会话密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AppSKey: str
        :param _NwkSKey: LoRaWAN 网络会话密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type NwkSKey: str
        :param _CreateUserId: 创建人Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _CreatorNickName: 创建人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
        :param _EnableState: 启用/禁用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _DeviceType: 设备类型（设备、子设备、网关）
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param _IsLora: 是否是 lora 设备
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLora: bool
        """
        self._DeviceName = None
        self._Status = None
        self._DevicePsk = None
        self._FirstOnlineTime = None
        self._LoginTime = None
        self._CreateTime = None
        self._Version = None
        self._DeviceCert = None
        self._LogLevel = None
        self._DevAddr = None
        self._AppKey = None
        self._DevEUI = None
        self._AppSKey = None
        self._NwkSKey = None
        self._CreateUserId = None
        self._CreatorNickName = None
        self._EnableState = None
        self._ProductId = None
        self._ProductName = None
        self._DeviceType = None
        self._IsLora = None

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
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def FirstOnlineTime(self):
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def DevAddr(self):
        return self._DevAddr

    @DevAddr.setter
    def DevAddr(self, DevAddr):
        self._DevAddr = DevAddr

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def DevEUI(self):
        return self._DevEUI

    @DevEUI.setter
    def DevEUI(self, DevEUI):
        self._DevEUI = DevEUI

    @property
    def AppSKey(self):
        return self._AppSKey

    @AppSKey.setter
    def AppSKey(self, AppSKey):
        self._AppSKey = AppSKey

    @property
    def NwkSKey(self):
        return self._NwkSKey

    @NwkSKey.setter
    def NwkSKey(self, NwkSKey):
        self._NwkSKey = NwkSKey

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

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
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def IsLora(self):
        return self._IsLora

    @IsLora.setter
    def IsLora(self, IsLora):
        self._IsLora = IsLora


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Status = params.get("Status")
        self._DevicePsk = params.get("DevicePsk")
        self._FirstOnlineTime = params.get("FirstOnlineTime")
        self._LoginTime = params.get("LoginTime")
        self._CreateTime = params.get("CreateTime")
        self._Version = params.get("Version")
        self._DeviceCert = params.get("DeviceCert")
        self._LogLevel = params.get("LogLevel")
        self._DevAddr = params.get("DevAddr")
        self._AppKey = params.get("AppKey")
        self._DevEUI = params.get("DevEUI")
        self._AppSKey = params.get("AppSKey")
        self._NwkSKey = params.get("NwkSKey")
        self._CreateUserId = params.get("CreateUserId")
        self._CreatorNickName = params.get("CreatorNickName")
        self._EnableState = params.get("EnableState")
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._DeviceType = params.get("DeviceType")
        self._IsLora = params.get("IsLora")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePositionItem(AbstractModel):
    """设备位置详情

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _CreateTime: 位置信息时间
        :type CreateTime: int
        :param _Longitude: 设备经度信息
        :type Longitude: float
        :param _Latitude: 设备纬度信息
        :type Latitude: float
        """
        self._DeviceName = None
        self._CreateTime = None
        self._Longitude = None
        self._Latitude = None

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
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._CreateTime = params.get("CreateTime")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSignatureInfo(AbstractModel):
    """设备签名

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self._DeviceName = None
        self._DeviceSignature = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceSignature(self):
        return self._DeviceSignature

    @DeviceSignature.setter
    def DeviceSignature(self, DeviceSignature):
        self._DeviceSignature = DeviceSignature


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUser(AbstractModel):
    """设备的用户

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _Role: 用户角色 1所有者，0：其他分享者
        :type Role: int
        :param _FamilyId: 家庭ID，所有者带该参数
注意：此字段可能返回 null，表示取不到有效值。
        :type FamilyId: str
        :param _FamilyName: 家庭名称，所有者带该参数
注意：此字段可能返回 null，表示取不到有效值。
        :type FamilyName: str
        """
        self._UserId = None
        self._Role = None
        self._FamilyId = None
        self._FamilyName = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def FamilyId(self):
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def FamilyName(self):
        return self._FamilyName

    @FamilyName.setter
    def FamilyName(self, FamilyName):
        self._FamilyName = FamilyName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Role = params.get("Role")
        self._FamilyId = params.get("FamilyId")
        self._FamilyName = params.get("FamilyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesItem(AbstractModel):
    """ProductId -> DeviceName

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
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
        


class DirectBindDeviceInFamilyRequest(AbstractModel):
    """DirectBindDeviceInFamily请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IotAppID: 小程序appid
        :type IotAppID: str
        :param _UserID: 用户ID
        :type UserID: str
        :param _FamilyId: 家庭ID
        :type FamilyId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _RoomId: 房间ID
        :type RoomId: str
        """
        self._IotAppID = None
        self._UserID = None
        self._FamilyId = None
        self._ProductId = None
        self._DeviceName = None
        self._RoomId = None

    @property
    def IotAppID(self):
        return self._IotAppID

    @IotAppID.setter
    def IotAppID(self, IotAppID):
        self._IotAppID = IotAppID

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def FamilyId(self):
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

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
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._IotAppID = params.get("IotAppID")
        self._UserID = params.get("UserID")
        self._FamilyId = params.get("FamilyId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectBindDeviceInFamilyResponse(AbstractModel):
    """DirectBindDeviceInFamily返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppDeviceInfo: 返回设备信息
        :type AppDeviceInfo: :class:`tencentcloud.iotexplorer.v20190423.models.AppDeviceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppDeviceInfo = None
        self._RequestId = None

    @property
    def AppDeviceInfo(self):
        return self._AppDeviceInfo

    @AppDeviceInfo.setter
    def AppDeviceInfo(self, AppDeviceInfo):
        self._AppDeviceInfo = AppDeviceInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppDeviceInfo") is not None:
            self._AppDeviceInfo = AppDeviceInfo()
            self._AppDeviceInfo._deserialize(params.get("AppDeviceInfo"))
        self._RequestId = params.get("RequestId")


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


class DismissRoomByStrRoomIdFromTRTCRequest(AbstractModel):
    """DismissRoomByStrRoomIdFromTRTC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间id
        :type RoomId: str
        """
        self._RoomId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdFromTRTCResponse(AbstractModel):
    """DismissRoomByStrRoomIdFromTRTC返回参数结构体

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


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        r"""
        :param _TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param _ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param _Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self._TimeStamp = None
        self._ProductId = None
        self._DeviceName = None
        self._EventId = None
        self._Type = None
        self._Data = None

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

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
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._TimeStamp = params.get("TimeStamp")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._EventId = params.get("EventId")
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilySubDevice(AbstractModel):
    """子设备详情

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _AliasName: 设备别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param _FamilyId: 设备绑定的家庭ID
        :type FamilyId: str
        :param _RoomId: 设备所在的房间ID，默认"0"
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: str
        :param _IconUrl: 图标
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param _IconUrlGrid: grid图标
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrlGrid: str
        :param _CreateTime: 设备绑定时间戳
        :type CreateTime: int
        :param _UpdateTime: 设备更新时间戳
        :type UpdateTime: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._DeviceId = None
        self._AliasName = None
        self._FamilyId = None
        self._RoomId = None
        self._IconUrl = None
        self._IconUrlGrid = None
        self._CreateTime = None
        self._UpdateTime = None

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
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def FamilyId(self):
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def IconUrlGrid(self):
        return self._IconUrlGrid

    @IconUrlGrid.setter
    def IconUrlGrid(self, IconUrlGrid):
        self._IconUrlGrid = IconUrlGrid

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


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceId = params.get("DeviceId")
        self._AliasName = params.get("AliasName")
        self._FamilyId = params.get("FamilyId")
        self._RoomId = params.get("RoomId")
        self._IconUrl = params.get("IconUrl")
        self._IconUrlGrid = params.get("IconUrlGrid")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceAlarmPoint(AbstractModel):
    """围栏告警位置点

    """

    def __init__(self):
        r"""
        :param _AlarmTime: 围栏告警时间
        :type AlarmTime: int
        :param _Longitude: 围栏告警位置的经度
        :type Longitude: float
        :param _Latitude: 围栏告警位置的纬度
        :type Latitude: float
        """
        self._AlarmTime = None
        self._Longitude = None
        self._Latitude = None

    @property
    def AlarmTime(self):
        return self._AlarmTime

    @AlarmTime.setter
    def AlarmTime(self, AlarmTime):
        self._AlarmTime = AlarmTime

    @property
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude


    def _deserialize(self, params):
        self._AlarmTime = params.get("AlarmTime")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceBindDeviceItem(AbstractModel):
    """围栏绑定的设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _AlertCondition: 告警条件(In，进围栏报警；Out，出围栏报警；InOrOut，进围栏或者出围栏均报警)
        :type AlertCondition: str
        :param _FenceEnable: 是否使能围栏(true，使能；false，禁用)
        :type FenceEnable: bool
        :param _Method: 告警处理方法
        :type Method: str
        """
        self._DeviceName = None
        self._AlertCondition = None
        self._FenceEnable = None
        self._Method = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AlertCondition(self):
        return self._AlertCondition

    @AlertCondition.setter
    def AlertCondition(self, AlertCondition):
        self._AlertCondition = AlertCondition

    @property
    def FenceEnable(self):
        return self._FenceEnable

    @FenceEnable.setter
    def FenceEnable(self, FenceEnable):
        self._FenceEnable = FenceEnable

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._AlertCondition = params.get("AlertCondition")
        self._FenceEnable = params.get("FenceEnable")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceBindProductItem(AbstractModel):
    """围栏绑定的产品信息

    """

    def __init__(self):
        r"""
        :param _Devices: 围栏绑定的设备信息
        :type Devices: list of FenceBindDeviceItem
        :param _ProductId: 围栏绑定的产品Id
        :type ProductId: str
        """
        self._Devices = None
        self._ProductId = None

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = FenceBindDeviceItem()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FenceEventItem(AbstractModel):
    """围栏事件详情

    """

    def __init__(self):
        r"""
        :param _ProductId: 围栏事件的产品Id
        :type ProductId: str
        :param _DeviceName: 围栏事件的设备名称
        :type DeviceName: str
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _AlertType: 围栏事件的告警类型（In，进围栏报警；Out，出围栏报警；InOrOut，进围栏或者出围栏均报警）
        :type AlertType: str
        :param _Data: 围栏事件的设备位置信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.FenceAlarmPoint`
        """
        self._ProductId = None
        self._DeviceName = None
        self._FenceId = None
        self._AlertType = None
        self._Data = None

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
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def AlertType(self):
        return self._AlertType

    @AlertType.setter
    def AlertType(self, AlertType):
        self._AlertType = AlertType

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._FenceId = params.get("FenceId")
        self._AlertType = params.get("AlertType")
        if params.get("Data") is not None:
            self._Data = FenceAlarmPoint()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    - 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。

    - 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段
        :type Name: str
        :param _Values: 字段的过滤的一个或多个值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _FwType: 固件升级模块
注意：此字段可能返回 null，表示取不到有效值。
        :type FwType: str
        :param _CreateUserId: 创建者子 uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _CreatorNickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
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
        self._CreatorNickName = None
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
    def CreatorNickName(self):
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

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
        self._CreatorNickName = params.get("CreatorNickName")
        self._UserDefined = params.get("UserDefined")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicRequest(AbstractModel):
    """GenSingleDeviceSignatureOfPublic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 设备所属的产品ID
        :type ProductId: str
        :param _DeviceName: 需要绑定的设备
        :type DeviceName: str
        :param _Expire: 设备绑定签名的有效时间,以秒为单位。取值范围：0 < Expire <= 86400，Expire == -1（十年）
        :type Expire: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Expire = None

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
    def Expire(self):
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicResponse(AbstractModel):
    """GenSingleDeviceSignatureOfPublic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceSignature: 设备签名
        :type DeviceSignature: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceSignatureInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceSignature = None
        self._RequestId = None

    @property
    def DeviceSignature(self):
        return self._DeviceSignature

    @DeviceSignature.setter
    def DeviceSignature(self, DeviceSignature):
        self._DeviceSignature = DeviceSignature

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceSignature") is not None:
            self._DeviceSignature = DeviceSignatureInfo()
            self._DeviceSignature._deserialize(params.get("DeviceSignature"))
        self._RequestId = params.get("RequestId")


class GenerateCloudStorageAIServiceTaskFileURLRequest(AbstractModel):
    """GenerateCloudStorageAIServiceTaskFileURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 产品 ID
        :type TaskId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _ExpireTime: 过期时间 UNIX 时间戳（默认值为当前时间 1 小时后，最大不超过文件所属任务的过期时间）
        :type ExpireTime: int
        """
        self._TaskId = None
        self._FileName = None
        self._ExpireTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FileName = params.get("FileName")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCloudStorageAIServiceTaskFileURLResponse(AbstractModel):
    """GenerateCloudStorageAIServiceTaskFileURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileURL: 文件下载 URL
        :type FileURL: str
        :param _ExpireTime: 过期时间 UNIX 时间戳（最大不超过文件所属任务的过期时间）
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileURL = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def FileURL(self):
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileURL = params.get("FileURL")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class GenerateSignedVideoURLRequest(AbstractModel):
    """GenerateSignedVideoURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoURL: 视频播放原始URL地址
        :type VideoURL: str
        :param _ExpireTime: 播放链接过期时间
        :type ExpireTime: int
        :param _ChannelId: 通道ID 非NVR设备不填 NVR设备必填 默认为无	
        :type ChannelId: int
        """
        self._VideoURL = None
        self._ExpireTime = None
        self._ChannelId = None

    @property
    def VideoURL(self):
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._VideoURL = params.get("VideoURL")
        self._ExpireTime = params.get("ExpireTime")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateSignedVideoURLResponse(AbstractModel):
    """GenerateSignedVideoURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignedVideoURL: 视频防盗链播放URL
        :type SignedVideoURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignedVideoURL = None
        self._RequestId = None

    @property
    def SignedVideoURL(self):
        return self._SignedVideoURL

    @SignedVideoURL.setter
    def SignedVideoURL(self, SignedVideoURL):
        self._SignedVideoURL = SignedVideoURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignedVideoURL = params.get("SignedVideoURL")
        self._RequestId = params.get("RequestId")


class GetAuthMiniProgramAppListRequest(AbstractModel):
    """GetAuthMiniProgramAppList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniProgramAppId: appId
        :type MiniProgramAppId: str
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        """
        self._MiniProgramAppId = None
        self._Offset = None
        self._Limit = None

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

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
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthMiniProgramAppListResponse(AbstractModel):
    """GetAuthMiniProgramAppList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniProgramList: 小程序列表
        :type MiniProgramList: list of AuthMiniProgramAppInfo
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MiniProgramList = None
        self._Total = None
        self._RequestId = None

    @property
    def MiniProgramList(self):
        return self._MiniProgramList

    @MiniProgramList.setter
    def MiniProgramList(self, MiniProgramList):
        self._MiniProgramList = MiniProgramList

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
        if params.get("MiniProgramList") is not None:
            self._MiniProgramList = []
            for item in params.get("MiniProgramList"):
                obj = AuthMiniProgramAppInfo()
                obj._deserialize(item)
                self._MiniProgramList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetBatchProductionsListRequest(AbstractModel):
    """GetBatchProductionsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量限制
        :type Limit: int
        """
        self._ProjectId = None
        self._Offset = None
        self._Limit = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
        self._ProjectId = params.get("ProjectId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBatchProductionsListResponse(AbstractModel):
    """GetBatchProductionsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchProductions: 返回详情信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchProductions: list of BatchProductionInfo
        :param _TotalCnt: 返回数量。
        :type TotalCnt: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchProductions = None
        self._TotalCnt = None
        self._RequestId = None

    @property
    def BatchProductions(self):
        return self._BatchProductions

    @BatchProductions.setter
    def BatchProductions(self, BatchProductions):
        self._BatchProductions = BatchProductions

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BatchProductions") is not None:
            self._BatchProductions = []
            for item in params.get("BatchProductions"):
                obj = BatchProductionInfo()
                obj._deserialize(item)
                self._BatchProductions.append(obj)
        self._TotalCnt = params.get("TotalCnt")
        self._RequestId = params.get("RequestId")


class GetCOSURLRequest(AbstractModel):
    """GetCOSURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param _FileSize: 文件大小
        :type FileSize: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FileSize = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

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
        self._ProductID = params.get("ProductID")
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


class GetDeviceListRequest(AbstractModel):
    """GetDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 需要查看设备列表的产品ID, -1代表ProjectId来筛选
        :type ProductId: str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页的大小，数值范围 10-100
        :type Limit: int
        :param _FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :type FirmwareVersion: str
        :param _DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        :param _ProjectId: 项目ID。产品 ID 为 -1 时，该参数必填
        :type ProjectId: str
        :param _Filters: 每次请求的Filters的上限为10，Filter.Values的上限为1。
        :type Filters: list of Filter
        """
        self._ProductId = None
        self._Offset = None
        self._Limit = None
        self._FirmwareVersion = None
        self._DeviceName = None
        self._ProjectId = None
        self._Filters = None

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._DeviceName = params.get("DeviceName")
        self._ProjectId = params.get("ProjectId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceListResponse(AbstractModel):
    """GetDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 返回的设备列表, 注意列表设备的 DevicePsk 为空, 要获取设备的 DevicePsk 请使用 DescribeDevice
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceInfo
        :param _Total: 产品下的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._Total = None
        self._RequestId = None

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

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
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetDeviceLocationHistoryRequest(AbstractModel):
    """GetDeviceLocationHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _StartTime: 查询起始时间，Unix时间，单位为毫秒
        :type StartTime: int
        :param _EndTime: 查询结束时间，Unix时间，单位为毫秒
        :type EndTime: int
        :param _CoordinateType: 坐标类型
        :type CoordinateType: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._StartTime = None
        self._EndTime = None
        self._CoordinateType = None

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

    @property
    def CoordinateType(self):
        return self._CoordinateType

    @CoordinateType.setter
    def CoordinateType(self, CoordinateType):
        self._CoordinateType = CoordinateType


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CoordinateType = params.get("CoordinateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLocationHistoryResponse(AbstractModel):
    """GetDeviceLocationHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Positions: 历史位置列表
        :type Positions: list of PositionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Positions = None
        self._RequestId = None

    @property
    def Positions(self):
        return self._Positions

    @Positions.setter
    def Positions(self, Positions):
        self._Positions = Positions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Positions") is not None:
            self._Positions = []
            for item in params.get("Positions"):
                obj = PositionItem()
                obj._deserialize(item)
                self._Positions.append(obj)
        self._RequestId = params.get("RequestId")


class GetDeviceSumStatisticsRequest(AbstractModel):
    """GetDeviceSumStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _ProductIds: 产品id列表，长度为0则拉取项目内全部产品
        :type ProductIds: list of str
        """
        self._ProjectId = None
        self._ProductIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductIds(self):
        return self._ProductIds

    @ProductIds.setter
    def ProductIds(self, ProductIds):
        self._ProductIds = ProductIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceSumStatisticsResponse(AbstractModel):
    """GetDeviceSumStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivationCount: 激活设备总数
        :type ActivationCount: int
        :param _OnlineCount: 在线设备总数
        :type OnlineCount: int
        :param _ActivationBeforeDay: 前一天激活设备数
        :type ActivationBeforeDay: int
        :param _ActiveBeforeDay: 前一天活跃设备数
        :type ActiveBeforeDay: int
        :param _ActivationWeekDayCount: 前一周激活设备数
        :type ActivationWeekDayCount: int
        :param _ActiveWeekDayCount: 前一周活跃设备数
        :type ActiveWeekDayCount: int
        :param _ActivationBeforeWeekDayCount: 上一周激活设备数
        :type ActivationBeforeWeekDayCount: int
        :param _ActiveBeforeWeekDayCount: 上一周活跃设备数
        :type ActiveBeforeWeekDayCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivationCount = None
        self._OnlineCount = None
        self._ActivationBeforeDay = None
        self._ActiveBeforeDay = None
        self._ActivationWeekDayCount = None
        self._ActiveWeekDayCount = None
        self._ActivationBeforeWeekDayCount = None
        self._ActiveBeforeWeekDayCount = None
        self._RequestId = None

    @property
    def ActivationCount(self):
        return self._ActivationCount

    @ActivationCount.setter
    def ActivationCount(self, ActivationCount):
        self._ActivationCount = ActivationCount

    @property
    def OnlineCount(self):
        return self._OnlineCount

    @OnlineCount.setter
    def OnlineCount(self, OnlineCount):
        self._OnlineCount = OnlineCount

    @property
    def ActivationBeforeDay(self):
        return self._ActivationBeforeDay

    @ActivationBeforeDay.setter
    def ActivationBeforeDay(self, ActivationBeforeDay):
        self._ActivationBeforeDay = ActivationBeforeDay

    @property
    def ActiveBeforeDay(self):
        return self._ActiveBeforeDay

    @ActiveBeforeDay.setter
    def ActiveBeforeDay(self, ActiveBeforeDay):
        self._ActiveBeforeDay = ActiveBeforeDay

    @property
    def ActivationWeekDayCount(self):
        return self._ActivationWeekDayCount

    @ActivationWeekDayCount.setter
    def ActivationWeekDayCount(self, ActivationWeekDayCount):
        self._ActivationWeekDayCount = ActivationWeekDayCount

    @property
    def ActiveWeekDayCount(self):
        return self._ActiveWeekDayCount

    @ActiveWeekDayCount.setter
    def ActiveWeekDayCount(self, ActiveWeekDayCount):
        self._ActiveWeekDayCount = ActiveWeekDayCount

    @property
    def ActivationBeforeWeekDayCount(self):
        return self._ActivationBeforeWeekDayCount

    @ActivationBeforeWeekDayCount.setter
    def ActivationBeforeWeekDayCount(self, ActivationBeforeWeekDayCount):
        self._ActivationBeforeWeekDayCount = ActivationBeforeWeekDayCount

    @property
    def ActiveBeforeWeekDayCount(self):
        return self._ActiveBeforeWeekDayCount

    @ActiveBeforeWeekDayCount.setter
    def ActiveBeforeWeekDayCount(self, ActiveBeforeWeekDayCount):
        self._ActiveBeforeWeekDayCount = ActiveBeforeWeekDayCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivationCount = params.get("ActivationCount")
        self._OnlineCount = params.get("OnlineCount")
        self._ActivationBeforeDay = params.get("ActivationBeforeDay")
        self._ActiveBeforeDay = params.get("ActiveBeforeDay")
        self._ActivationWeekDayCount = params.get("ActivationWeekDayCount")
        self._ActiveWeekDayCount = params.get("ActiveWeekDayCount")
        self._ActivationBeforeWeekDayCount = params.get("ActivationBeforeWeekDayCount")
        self._ActiveBeforeWeekDayCount = params.get("ActiveBeforeWeekDayCount")
        self._RequestId = params.get("RequestId")


class GetFamilyDeviceUserListRequest(AbstractModel):
    """GetFamilyDeviceUserList请求参数结构体

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
        


class GetFamilyDeviceUserListResponse(AbstractModel):
    """GetFamilyDeviceUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserList: 设备的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of DeviceUser
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserList = None
        self._RequestId = None

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = DeviceUser()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class GetGatewaySubDeviceListRequest(AbstractModel):
    """GetGatewaySubDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备名称
        :type GatewayDeviceName: str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页的大小
        :type Limit: int
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGatewaySubDeviceListResponse(AbstractModel):
    """GetGatewaySubDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 设备的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _DeviceList: 设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: :class:`tencentcloud.iotexplorer.v20190423.models.FamilySubDevice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DeviceList") is not None:
            self._DeviceList = FamilySubDevice()
            self._DeviceList._deserialize(params.get("DeviceList"))
        self._RequestId = params.get("RequestId")


class GetLoRaGatewayListRequest(AbstractModel):
    """GetLoRaGatewayList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsCommunity: 是否是社区网关
        :type IsCommunity: bool
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制个数
        :type Limit: int
        """
        self._IsCommunity = None
        self._Offset = None
        self._Limit = None

    @property
    def IsCommunity(self):
        return self._IsCommunity

    @IsCommunity.setter
    def IsCommunity(self, IsCommunity):
        self._IsCommunity = IsCommunity

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
        self._IsCommunity = params.get("IsCommunity")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLoRaGatewayListResponse(AbstractModel):
    """GetLoRaGatewayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回总数
        :type Total: int
        :param _Gateways: 返回详情项
注意：此字段可能返回 null，表示取不到有效值。
        :type Gateways: list of LoRaGatewayItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Gateways = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Gateways(self):
        return self._Gateways

    @Gateways.setter
    def Gateways(self, Gateways):
        self._Gateways = Gateways

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Gateways") is not None:
            self._Gateways = []
            for item in params.get("Gateways"):
                obj = LoRaGatewayItem()
                obj._deserialize(item)
                self._Gateways.append(obj)
        self._RequestId = params.get("RequestId")


class GetPositionSpaceListRequest(AbstractModel):
    """GetPositionSpaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _Offset: 翻页偏移量，0起始
        :type Offset: int
        :param _Limit: 最大返回结果数
        :type Limit: int
        """
        self._ProjectId = None
        self._Offset = None
        self._Limit = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
        self._ProjectId = params.get("ProjectId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPositionSpaceListResponse(AbstractModel):
    """GetPositionSpaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 位置空间列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PositionSpaceInfo
        :param _Total: 位置空间数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PositionSpaceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetProjectListRequest(AbstractModel):
    """GetProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 个数限制
        :type Limit: int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProjectId: 按项目ID搜索
        :type ProjectId: str
        :param _ProductId: 按产品ID搜索
        :type ProductId: str
        :param _Includes: 加载 ProductCount、DeviceCount、ApplicationCount，可选值：ProductCount、DeviceCount、ApplicationCount，可多选
        :type Includes: list of str
        :param _ProjectName: 按项目名称搜索
        :type ProjectName: str
        """
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._ProjectId = None
        self._ProductId = None
        self._Includes = None
        self._ProjectName = None

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Includes(self):
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._ProjectId = params.get("ProjectId")
        self._ProductId = params.get("ProductId")
        self._Includes = params.get("Includes")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProjectListResponse(AbstractModel):
    """GetProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Projects: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Projects: list of ProjectEntryEx
        :param _Total: 列表项个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Projects = None
        self._Total = None
        self._RequestId = None

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

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
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = ProjectEntryEx()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetStudioProductListRequest(AbstractModel):
    """GetStudioProductList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _DevStatus: 产品DevStatus
        :type DevStatus: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        """
        self._ProjectId = None
        self._DevStatus = None
        self._Offset = None
        self._Limit = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DevStatus(self):
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

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
        self._ProjectId = params.get("ProjectId")
        self._DevStatus = params.get("DevStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStudioProductListResponse(AbstractModel):
    """GetStudioProductList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 产品列表
        :type Products: list of ProductEntry
        :param _Total: 产品数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._Total = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetTWeCallActiveStatusRequest(AbstractModel):
    """GetTWeCallActiveStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniProgramAppId: appId
        :type MiniProgramAppId: str
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._MiniProgramAppId = None
        self._DeviceList = None

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def DeviceList(self):
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = TWeCallInfo()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTWeCallActiveStatusResponse(AbstractModel):
    """GetTWeCallActiveStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TWeCallActiveInfos: 激活状态
        :type TWeCallActiveInfos: list of TWeCallActiveInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TWeCallActiveInfos = None
        self._RequestId = None

    @property
    def TWeCallActiveInfos(self):
        return self._TWeCallActiveInfos

    @TWeCallActiveInfos.setter
    def TWeCallActiveInfos(self, TWeCallActiveInfos):
        self._TWeCallActiveInfos = TWeCallActiveInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TWeCallActiveInfos") is not None:
            self._TWeCallActiveInfos = []
            for item in params.get("TWeCallActiveInfos"):
                obj = TWeCallActiveInfo()
                obj._deserialize(item)
                self._TWeCallActiveInfos.append(obj)
        self._RequestId = params.get("RequestId")


class GetTWeCallPkgListRequest(AbstractModel):
    """GetTWeCallPkgList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniProgramAppId: appId
        :type MiniProgramAppId: str
        :param _PkgType: 类型
        :type PkgType: list of int
        :param _Status: 状态
        :type Status: list of int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 每页数据大小
        :type Limit: int
        """
        self._MiniProgramAppId = None
        self._PkgType = None
        self._Status = None
        self._Offset = None
        self._Limit = None

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def PkgType(self):
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        self._PkgType = params.get("PkgType")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTWeCallPkgListResponse(AbstractModel):
    """GetTWeCallPkgList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TWeCallPkgList: 激活状态
        :type TWeCallPkgList: list of TWeCallPkgInfo
        :param _Total: 总数
        :type Total: int
        :param _TWeCallCategoryPkgList: 分类统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TWeCallCategoryPkgList: list of TWeCallCategoryPkgInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TWeCallPkgList = None
        self._Total = None
        self._TWeCallCategoryPkgList = None
        self._RequestId = None

    @property
    def TWeCallPkgList(self):
        return self._TWeCallPkgList

    @TWeCallPkgList.setter
    def TWeCallPkgList(self, TWeCallPkgList):
        self._TWeCallPkgList = TWeCallPkgList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TWeCallCategoryPkgList(self):
        return self._TWeCallCategoryPkgList

    @TWeCallCategoryPkgList.setter
    def TWeCallCategoryPkgList(self, TWeCallCategoryPkgList):
        self._TWeCallCategoryPkgList = TWeCallCategoryPkgList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TWeCallPkgList") is not None:
            self._TWeCallPkgList = []
            for item in params.get("TWeCallPkgList"):
                obj = TWeCallPkgInfo()
                obj._deserialize(item)
                self._TWeCallPkgList.append(obj)
        self._Total = params.get("Total")
        if params.get("TWeCallCategoryPkgList") is not None:
            self._TWeCallCategoryPkgList = []
            for item in params.get("TWeCallCategoryPkgList"):
                obj = TWeCallCategoryPkgInfo()
                obj._deserialize(item)
                self._TWeCallCategoryPkgList.append(obj)
        self._RequestId = params.get("RequestId")


class GetTopicRuleListRequest(AbstractModel):
    """GetTopicRuleList请求参数结构体

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
        


class GetTopicRuleListResponse(AbstractModel):
    """GetTopicRuleList返回参数结构体

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


class GetWechatDeviceTicketRequest(AbstractModel):
    """GetWechatDeviceTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 产品名称
        :type DeviceName: str
        :param _IsThirdApp: 是否第三方小程序
        :type IsThirdApp: int
        :param _ModelId: 模板ID
        :type ModelId: str
        :param _MiniProgramAppId: 小程序APPID
        :type MiniProgramAppId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._IsThirdApp = None
        self._ModelId = None
        self._MiniProgramAppId = None

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
    def IsThirdApp(self):
        return self._IsThirdApp

    @IsThirdApp.setter
    def IsThirdApp(self, IsThirdApp):
        self._IsThirdApp = IsThirdApp

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def MiniProgramAppId(self):
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._IsThirdApp = params.get("IsThirdApp")
        self._ModelId = params.get("ModelId")
        self._MiniProgramAppId = params.get("MiniProgramAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWechatDeviceTicketResponse(AbstractModel):
    """GetWechatDeviceTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WXDeviceInfo: 微信设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WXDeviceInfo: :class:`tencentcloud.iotexplorer.v20190423.models.WXDeviceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WXDeviceInfo = None
        self._RequestId = None

    @property
    def WXDeviceInfo(self):
        return self._WXDeviceInfo

    @WXDeviceInfo.setter
    def WXDeviceInfo(self, WXDeviceInfo):
        self._WXDeviceInfo = WXDeviceInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WXDeviceInfo") is not None:
            self._WXDeviceInfo = WXDeviceInfo()
            self._WXDeviceInfo._deserialize(params.get("WXDeviceInfo"))
        self._RequestId = params.get("RequestId")


class InheritCloudStorageUserRequest(AbstractModel):
    """InheritCloudStorageUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 原始用户ID
        :type UserId: str
        :param _ToUserId: 目标用户ID
        :type ToUserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None
        self._ToUserId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ToUserId(self):
        return self._ToUserId

    @ToUserId.setter
    def ToUserId(self, ToUserId):
        self._ToUserId = ToUserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        self._ToUserId = params.get("ToUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InheritCloudStorageUserResponse(AbstractModel):
    """InheritCloudStorageUser返回参数结构体

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


class InstanceDetail(AbstractModel):
    """实例信息
    公共实例过期时间 0001-01-01T00:00:00Z，公共实例是永久有效

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceType: 实例类型（0 公共实例 1 标准企业实例 2新企业实例3新公共实例）
        :type InstanceType: int
        :param _Region: 地域字母缩写
        :type Region: str
        :param _ZoneId: 区域全拼
        :type ZoneId: str
        :param _TotalDeviceNum: 支持设备总数
        :type TotalDeviceNum: int
        :param _UsedDeviceNum: 已注册设备数
        :type UsedDeviceNum: int
        :param _ProjectNum: 项目数
        :type ProjectNum: int
        :param _ProductNum: 产品数
        :type ProductNum: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _ExpireTime: 过期时间，公共实例过期时间 0001-01-01T00:00:00Z，公共实例是永久有效
        :type ExpireTime: str
        :param _TotalDevice: 总设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalDevice: int
        :param _ActivateDevice: 激活设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivateDevice: int
        :param _Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _UpDownTPS: 消息上下行配置TPS
注意：此字段可能返回 null，表示取不到有效值。
        :type UpDownTPS: int
        :param _UpDownCurrentTPS: 当前消息上下行TPS
注意：此字段可能返回 null，表示取不到有效值。
        :type UpDownCurrentTPS: int
        :param _ForwardTPS: 消息转发配置TPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardTPS: int
        :param _ForwardCurrentTPS: 消息转发当前TPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardCurrentTPS: int
        :param _CellNum: 实例单元数
注意：此字段可能返回 null，表示取不到有效值。
        :type CellNum: int
        :param _BillingTag: 实例Tag
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingTag: str
        :param _EverydayFreeMessageCount: 每日消息数
注意：此字段可能返回 null，表示取不到有效值。
        :type EverydayFreeMessageCount: int
        :param _MaxDeviceOnlineCount: 最大在线设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDeviceOnlineCount: int
        """
        self._InstanceId = None
        self._InstanceType = None
        self._Region = None
        self._ZoneId = None
        self._TotalDeviceNum = None
        self._UsedDeviceNum = None
        self._ProjectNum = None
        self._ProductNum = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ExpireTime = None
        self._TotalDevice = None
        self._ActivateDevice = None
        self._Description = None
        self._Status = None
        self._UpDownTPS = None
        self._UpDownCurrentTPS = None
        self._ForwardTPS = None
        self._ForwardCurrentTPS = None
        self._CellNum = None
        self._BillingTag = None
        self._EverydayFreeMessageCount = None
        self._MaxDeviceOnlineCount = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TotalDeviceNum(self):
        return self._TotalDeviceNum

    @TotalDeviceNum.setter
    def TotalDeviceNum(self, TotalDeviceNum):
        self._TotalDeviceNum = TotalDeviceNum

    @property
    def UsedDeviceNum(self):
        return self._UsedDeviceNum

    @UsedDeviceNum.setter
    def UsedDeviceNum(self, UsedDeviceNum):
        self._UsedDeviceNum = UsedDeviceNum

    @property
    def ProjectNum(self):
        return self._ProjectNum

    @ProjectNum.setter
    def ProjectNum(self, ProjectNum):
        self._ProjectNum = ProjectNum

    @property
    def ProductNum(self):
        return self._ProductNum

    @ProductNum.setter
    def ProductNum(self, ProductNum):
        self._ProductNum = ProductNum

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
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TotalDevice(self):
        return self._TotalDevice

    @TotalDevice.setter
    def TotalDevice(self, TotalDevice):
        self._TotalDevice = TotalDevice

    @property
    def ActivateDevice(self):
        return self._ActivateDevice

    @ActivateDevice.setter
    def ActivateDevice(self, ActivateDevice):
        self._ActivateDevice = ActivateDevice

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpDownTPS(self):
        return self._UpDownTPS

    @UpDownTPS.setter
    def UpDownTPS(self, UpDownTPS):
        self._UpDownTPS = UpDownTPS

    @property
    def UpDownCurrentTPS(self):
        return self._UpDownCurrentTPS

    @UpDownCurrentTPS.setter
    def UpDownCurrentTPS(self, UpDownCurrentTPS):
        self._UpDownCurrentTPS = UpDownCurrentTPS

    @property
    def ForwardTPS(self):
        return self._ForwardTPS

    @ForwardTPS.setter
    def ForwardTPS(self, ForwardTPS):
        self._ForwardTPS = ForwardTPS

    @property
    def ForwardCurrentTPS(self):
        return self._ForwardCurrentTPS

    @ForwardCurrentTPS.setter
    def ForwardCurrentTPS(self, ForwardCurrentTPS):
        self._ForwardCurrentTPS = ForwardCurrentTPS

    @property
    def CellNum(self):
        return self._CellNum

    @CellNum.setter
    def CellNum(self, CellNum):
        self._CellNum = CellNum

    @property
    def BillingTag(self):
        return self._BillingTag

    @BillingTag.setter
    def BillingTag(self, BillingTag):
        self._BillingTag = BillingTag

    @property
    def EverydayFreeMessageCount(self):
        return self._EverydayFreeMessageCount

    @EverydayFreeMessageCount.setter
    def EverydayFreeMessageCount(self, EverydayFreeMessageCount):
        self._EverydayFreeMessageCount = EverydayFreeMessageCount

    @property
    def MaxDeviceOnlineCount(self):
        return self._MaxDeviceOnlineCount

    @MaxDeviceOnlineCount.setter
    def MaxDeviceOnlineCount(self, MaxDeviceOnlineCount):
        self._MaxDeviceOnlineCount = MaxDeviceOnlineCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceType = params.get("InstanceType")
        self._Region = params.get("Region")
        self._ZoneId = params.get("ZoneId")
        self._TotalDeviceNum = params.get("TotalDeviceNum")
        self._UsedDeviceNum = params.get("UsedDeviceNum")
        self._ProjectNum = params.get("ProjectNum")
        self._ProductNum = params.get("ProductNum")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._TotalDevice = params.get("TotalDevice")
        self._ActivateDevice = params.get("ActivateDevice")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._UpDownTPS = params.get("UpDownTPS")
        self._UpDownCurrentTPS = params.get("UpDownCurrentTPS")
        self._ForwardTPS = params.get("ForwardTPS")
        self._ForwardCurrentTPS = params.get("ForwardCurrentTPS")
        self._CellNum = params.get("CellNum")
        self._BillingTag = params.get("BillingTag")
        self._EverydayFreeMessageCount = params.get("EverydayFreeMessageCount")
        self._MaxDeviceOnlineCount = params.get("MaxDeviceOnlineCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventHistoryRequest(AbstractModel):
    """ListEventHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件
        :type Type: str
        :param _StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param _EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param _Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param _Size: 单次获取的历史数据项目的最大数量, 缺省10
        :type Size: int
        :param _EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._Size = None
        self._EventId = None

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._Size = params.get("Size")
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventHistoryResponse(AbstractModel):
    """ListEventHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param _EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Total = None
        self._Listover = None
        self._EventHistory = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def EventHistory(self):
        return self._EventHistory

    @EventHistory.setter
    def EventHistory(self, EventHistory):
        self._EventHistory = EventHistory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Total = params.get("Total")
        self._Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self._EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self._EventHistory.append(obj)
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
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._PageNum = None
        self._PageSize = None
        self._ProductID = None
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
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProductID = params.get("ProductID")
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


class ListTopicPolicyRequest(AbstractModel):
    """ListTopicPolicy请求参数结构体

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
        


class ListTopicPolicyResponse(AbstractModel):
    """ListTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: Topic列表
        :type Topics: list of TopicItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topics = None
        self._RequestId = None

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicItem()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._RequestId = params.get("RequestId")


class LoRaFrequencyEntry(AbstractModel):
    """LoRa自定义频点信息

    """

    def __init__(self):
        r"""
        :param _FreqId: 频点唯一ID
        :type FreqId: str
        :param _FreqName: 频点名称
        :type FreqName: str
        :param _Description: 频点描述
        :type Description: str
        :param _ChannelsDataUp: 数据上行信道
        :type ChannelsDataUp: list of int non-negative
        :param _ChannelsDataRX1: 数据下行信道RX1
        :type ChannelsDataRX1: list of int non-negative
        :param _ChannelsDataRX2: 数据下行信道RX2
        :type ChannelsDataRX2: list of int non-negative
        :param _ChannelsJoinUp: 入网上行信道
        :type ChannelsJoinUp: list of int non-negative
        :param _ChannelsJoinRX1: 入网下行RX1信道
        :type ChannelsJoinRX1: list of int non-negative
        :param _ChannelsJoinRX2: 入网下行RX2信道
        :type ChannelsJoinRX2: list of int non-negative
        :param _CreateTime: 创建时间
        :type CreateTime: int
        """
        self._FreqId = None
        self._FreqName = None
        self._Description = None
        self._ChannelsDataUp = None
        self._ChannelsDataRX1 = None
        self._ChannelsDataRX2 = None
        self._ChannelsJoinUp = None
        self._ChannelsJoinRX1 = None
        self._ChannelsJoinRX2 = None
        self._CreateTime = None

    @property
    def FreqId(self):
        return self._FreqId

    @FreqId.setter
    def FreqId(self, FreqId):
        self._FreqId = FreqId

    @property
    def FreqName(self):
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ChannelsDataUp(self):
        return self._ChannelsDataUp

    @ChannelsDataUp.setter
    def ChannelsDataUp(self, ChannelsDataUp):
        self._ChannelsDataUp = ChannelsDataUp

    @property
    def ChannelsDataRX1(self):
        return self._ChannelsDataRX1

    @ChannelsDataRX1.setter
    def ChannelsDataRX1(self, ChannelsDataRX1):
        self._ChannelsDataRX1 = ChannelsDataRX1

    @property
    def ChannelsDataRX2(self):
        return self._ChannelsDataRX2

    @ChannelsDataRX2.setter
    def ChannelsDataRX2(self, ChannelsDataRX2):
        self._ChannelsDataRX2 = ChannelsDataRX2

    @property
    def ChannelsJoinUp(self):
        return self._ChannelsJoinUp

    @ChannelsJoinUp.setter
    def ChannelsJoinUp(self, ChannelsJoinUp):
        self._ChannelsJoinUp = ChannelsJoinUp

    @property
    def ChannelsJoinRX1(self):
        return self._ChannelsJoinRX1

    @ChannelsJoinRX1.setter
    def ChannelsJoinRX1(self, ChannelsJoinRX1):
        self._ChannelsJoinRX1 = ChannelsJoinRX1

    @property
    def ChannelsJoinRX2(self):
        return self._ChannelsJoinRX2

    @ChannelsJoinRX2.setter
    def ChannelsJoinRX2(self, ChannelsJoinRX2):
        self._ChannelsJoinRX2 = ChannelsJoinRX2

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._FreqId = params.get("FreqId")
        self._FreqName = params.get("FreqName")
        self._Description = params.get("Description")
        self._ChannelsDataUp = params.get("ChannelsDataUp")
        self._ChannelsDataRX1 = params.get("ChannelsDataRX1")
        self._ChannelsDataRX2 = params.get("ChannelsDataRX2")
        self._ChannelsJoinUp = params.get("ChannelsJoinUp")
        self._ChannelsJoinRX1 = params.get("ChannelsJoinRX1")
        self._ChannelsJoinRX2 = params.get("ChannelsJoinRX2")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoRaGatewayItem(AbstractModel):
    """LoRa 网关信息

    """

    def __init__(self):
        r"""
        :param _GatewayId: LoRa 网关Id
        :type GatewayId: str
        :param _IsPublic: 是否是公开网关
        :type IsPublic: bool
        :param _Description: 网关描述
        :type Description: str
        :param _Name: 网关名称
        :type Name: str
        :param _Position: 网关位置信息
        :type Position: str
        :param _PositionDetails: 网关位置详情
        :type PositionDetails: str
        :param _Location: LoRa 网关位置坐标
        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        :param _UpdatedAt: 最后更新时间
        :type UpdatedAt: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _LastSeenAt: 最后上报时间
        :type LastSeenAt: str
        :param _FrequencyId: 频点ID
        :type FrequencyId: str
        """
        self._GatewayId = None
        self._IsPublic = None
        self._Description = None
        self._Name = None
        self._Position = None
        self._PositionDetails = None
        self._Location = None
        self._UpdatedAt = None
        self._CreatedAt = None
        self._LastSeenAt = None
        self._FrequencyId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def PositionDetails(self):
        return self._PositionDetails

    @PositionDetails.setter
    def PositionDetails(self, PositionDetails):
        self._PositionDetails = PositionDetails

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def LastSeenAt(self):
        return self._LastSeenAt

    @LastSeenAt.setter
    def LastSeenAt(self, LastSeenAt):
        self._LastSeenAt = LastSeenAt

    @property
    def FrequencyId(self):
        return self._FrequencyId

    @FrequencyId.setter
    def FrequencyId(self, FrequencyId):
        self._FrequencyId = FrequencyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._IsPublic = params.get("IsPublic")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Position = params.get("Position")
        self._PositionDetails = params.get("PositionDetails")
        if params.get("Location") is not None:
            self._Location = LoRaGatewayLocation()
            self._Location._deserialize(params.get("Location"))
        self._UpdatedAt = params.get("UpdatedAt")
        self._CreatedAt = params.get("CreatedAt")
        self._LastSeenAt = params.get("LastSeenAt")
        self._FrequencyId = params.get("FrequencyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoRaGatewayLocation(AbstractModel):
    """网关坐标

    """

    def __init__(self):
        r"""
        :param _Latitude: 纬度
        :type Latitude: float
        :param _Longitude: 精度
        :type Longitude: float
        :param _Accuracy: 准确度
        :type Accuracy: float
        :param _Altitude: 海拔
        :type Altitude: float
        """
        self._Latitude = None
        self._Longitude = None
        self._Accuracy = None
        self._Altitude = None

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Accuracy(self):
        return self._Accuracy

    @Accuracy.setter
    def Accuracy(self, Accuracy):
        self._Accuracy = Accuracy

    @property
    def Altitude(self):
        return self._Altitude

    @Altitude.setter
    def Altitude(self, Altitude):
        self._Altitude = Altitude


    def _deserialize(self, params):
        self._Latitude = params.get("Latitude")
        self._Longitude = params.get("Longitude")
        self._Accuracy = params.get("Accuracy")
        self._Altitude = params.get("Altitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudStorageAIServiceCallbackRequest(AbstractModel):
    """ModifyCloudStorageAIServiceCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _Type: 推送类型。可选值：
- `http`：HTTP 回调
        :type Type: str
        :param _CallbackUrl: HTTP 回调 URL
        :type CallbackUrl: str
        :param _CallbackToken: HTTP 回调鉴权 Token
        :type CallbackToken: str
        """
        self._ProductId = None
        self._Type = None
        self._CallbackUrl = None
        self._CallbackToken = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def CallbackToken(self):
        return self._CallbackToken

    @CallbackToken.setter
    def CallbackToken(self, CallbackToken):
        self._CallbackToken = CallbackToken


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Type = params.get("Type")
        self._CallbackUrl = params.get("CallbackUrl")
        self._CallbackToken = params.get("CallbackToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudStorageAIServiceCallbackResponse(AbstractModel):
    """ModifyCloudStorageAIServiceCallback返回参数结构体

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


class ModifyCloudStorageAIServiceRequest(AbstractModel):
    """ModifyCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
        :type ServiceType: str
        :param _Enabled: 视频分析启用状态
        :type Enabled: bool
        :param _ROI: 视频分析识别区域
        :type ROI: str
        :param _Config: 视频分析配置参数
        :type Config: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._Enabled = None
        self._ROI = None
        self._Config = None

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
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ROI(self):
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._Enabled = params.get("Enabled")
        self._ROI = params.get("ROI")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudStorageAIServiceResponse(AbstractModel):
    """ModifyCloudStorageAIService返回参数结构体

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


class ModifyFenceBindRequest(AbstractModel):
    """ModifyFenceBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _Items: 围栏绑定的产品列表
        :type Items: list of FenceBindProductItem
        """
        self._FenceId = None
        self._Items = None

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._FenceId = params.get("FenceId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFenceBindResponse(AbstractModel):
    """ModifyFenceBind返回参数结构体

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


class ModifyLoRaFrequencyRequest(AbstractModel):
    """ModifyLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FreqId: 频点唯一ID
        :type FreqId: str
        :param _FreqName: 频点名称
        :type FreqName: str
        :param _Description: 频点描述
        :type Description: str
        :param _ChannelsDataUp: 数据上行信道
        :type ChannelsDataUp: list of int non-negative
        :param _ChannelsDataRX1: 数据下行信道RX1
        :type ChannelsDataRX1: list of int non-negative
        :param _ChannelsDataRX2: 数据下行信道RX2
        :type ChannelsDataRX2: list of int non-negative
        :param _ChannelsJoinUp: 入网上行信道
        :type ChannelsJoinUp: list of int non-negative
        :param _ChannelsJoinRX1: 入网下行信道RX1
        :type ChannelsJoinRX1: list of int non-negative
        :param _ChannelsJoinRX2: 入网下行信道RX2
        :type ChannelsJoinRX2: list of int non-negative
        """
        self._FreqId = None
        self._FreqName = None
        self._Description = None
        self._ChannelsDataUp = None
        self._ChannelsDataRX1 = None
        self._ChannelsDataRX2 = None
        self._ChannelsJoinUp = None
        self._ChannelsJoinRX1 = None
        self._ChannelsJoinRX2 = None

    @property
    def FreqId(self):
        return self._FreqId

    @FreqId.setter
    def FreqId(self, FreqId):
        self._FreqId = FreqId

    @property
    def FreqName(self):
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ChannelsDataUp(self):
        return self._ChannelsDataUp

    @ChannelsDataUp.setter
    def ChannelsDataUp(self, ChannelsDataUp):
        self._ChannelsDataUp = ChannelsDataUp

    @property
    def ChannelsDataRX1(self):
        return self._ChannelsDataRX1

    @ChannelsDataRX1.setter
    def ChannelsDataRX1(self, ChannelsDataRX1):
        self._ChannelsDataRX1 = ChannelsDataRX1

    @property
    def ChannelsDataRX2(self):
        return self._ChannelsDataRX2

    @ChannelsDataRX2.setter
    def ChannelsDataRX2(self, ChannelsDataRX2):
        self._ChannelsDataRX2 = ChannelsDataRX2

    @property
    def ChannelsJoinUp(self):
        return self._ChannelsJoinUp

    @ChannelsJoinUp.setter
    def ChannelsJoinUp(self, ChannelsJoinUp):
        self._ChannelsJoinUp = ChannelsJoinUp

    @property
    def ChannelsJoinRX1(self):
        return self._ChannelsJoinRX1

    @ChannelsJoinRX1.setter
    def ChannelsJoinRX1(self, ChannelsJoinRX1):
        self._ChannelsJoinRX1 = ChannelsJoinRX1

    @property
    def ChannelsJoinRX2(self):
        return self._ChannelsJoinRX2

    @ChannelsJoinRX2.setter
    def ChannelsJoinRX2(self, ChannelsJoinRX2):
        self._ChannelsJoinRX2 = ChannelsJoinRX2


    def _deserialize(self, params):
        self._FreqId = params.get("FreqId")
        self._FreqName = params.get("FreqName")
        self._Description = params.get("Description")
        self._ChannelsDataUp = params.get("ChannelsDataUp")
        self._ChannelsDataRX1 = params.get("ChannelsDataRX1")
        self._ChannelsDataRX2 = params.get("ChannelsDataRX2")
        self._ChannelsJoinUp = params.get("ChannelsJoinUp")
        self._ChannelsJoinRX1 = params.get("ChannelsJoinRX1")
        self._ChannelsJoinRX2 = params.get("ChannelsJoinRX2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoRaFrequencyResponse(AbstractModel):
    """ModifyLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 频点信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
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
        if params.get("Data") is not None:
            self._Data = LoRaFrequencyEntry()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyLoRaGatewayRequest(AbstractModel):
    """ModifyLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Description: 描述信息
        :type Description: str
        :param _GatewayId: LoRa网关Id
        :type GatewayId: str
        :param _Location: LoRa网关位置坐标
        :type Location: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        :param _Name: LoRa网关名称
        :type Name: str
        :param _IsPublic: 是否公开可见
        :type IsPublic: bool
        :param _Position: 位置信息
        :type Position: str
        :param _PositionDetails: 位置详情
        :type PositionDetails: str
        :param _FrequencyId: 频点ID
        :type FrequencyId: str
        """
        self._Description = None
        self._GatewayId = None
        self._Location = None
        self._Name = None
        self._IsPublic = None
        self._Position = None
        self._PositionDetails = None
        self._FrequencyId = None

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def PositionDetails(self):
        return self._PositionDetails

    @PositionDetails.setter
    def PositionDetails(self, PositionDetails):
        self._PositionDetails = PositionDetails

    @property
    def FrequencyId(self):
        return self._FrequencyId

    @FrequencyId.setter
    def FrequencyId(self, FrequencyId):
        self._FrequencyId = FrequencyId


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._GatewayId = params.get("GatewayId")
        if params.get("Location") is not None:
            self._Location = LoRaGatewayLocation()
            self._Location._deserialize(params.get("Location"))
        self._Name = params.get("Name")
        self._IsPublic = params.get("IsPublic")
        self._Position = params.get("Position")
        self._PositionDetails = params.get("PositionDetails")
        self._FrequencyId = params.get("FrequencyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoRaGatewayResponse(AbstractModel):
    """ModifyLoRaGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Gateway: 返回网关数据
        :type Gateway: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Gateway = None
        self._RequestId = None

    @property
    def Gateway(self):
        return self._Gateway

    @Gateway.setter
    def Gateway(self, Gateway):
        self._Gateway = Gateway

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Gateway") is not None:
            self._Gateway = LoRaGatewayItem()
            self._Gateway._deserialize(params.get("Gateway"))
        self._RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self._ProductId = None
        self._ModelSchema = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelSchema(self):
        return self._ModelSchema

    @ModelSchema.setter
    def ModelSchema(self, ModelSchema):
        self._ModelSchema = ModelSchema


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ModelSchema = params.get("ModelSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

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


class ModifyPositionFenceRequest(AbstractModel):
    """ModifyPositionFence请求参数结构体

    """


class ModifyPositionFenceResponse(AbstractModel):
    """ModifyPositionFence返回参数结构体

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


class ModifyPositionSpaceRequest(AbstractModel):
    """ModifyPositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _SpaceName: 位置空间名称
        :type SpaceName: str
        :param _AuthorizeType: 授权类型
        :type AuthorizeType: int
        :param _ProductIdList: 产品列表
        :type ProductIdList: list of str
        :param _Description: 位置空间描述
        :type Description: str
        :param _Icon: 缩略图
        :type Icon: str
        """
        self._SpaceId = None
        self._SpaceName = None
        self._AuthorizeType = None
        self._ProductIdList = None
        self._Description = None
        self._Icon = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def AuthorizeType(self):
        return self._AuthorizeType

    @AuthorizeType.setter
    def AuthorizeType(self, AuthorizeType):
        self._AuthorizeType = AuthorizeType

    @property
    def ProductIdList(self):
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._SpaceName = params.get("SpaceName")
        self._AuthorizeType = params.get("AuthorizeType")
        self._ProductIdList = params.get("ProductIdList")
        self._Description = params.get("Description")
        self._Icon = params.get("Icon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPositionSpaceResponse(AbstractModel):
    """ModifyPositionSpace返回参数结构体

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


class ModifyProductCloudStorageAIServiceRequest(AbstractModel):
    """ModifyProductCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _Enabled: 开通状态
        :type Enabled: bool
        """
        self._ProductId = None
        self._Enabled = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductCloudStorageAIServiceResponse(AbstractModel):
    """ModifyProductCloudStorageAIService返回参数结构体

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


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDesc: 项目描述
        :type ProjectDesc: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDesc = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDesc = params.get("ProjectDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Project: 项目详情
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Project = None
        self._RequestId = None

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self._Project = ProjectEntry()
            self._Project._deserialize(params.get("Project"))
        self._RequestId = params.get("RequestId")


class ModifySpacePropertyRequest(AbstractModel):
    """ModifySpaceProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _Data: 产品属性
        :type Data: str
        """
        self._SpaceId = None
        self._ProductId = None
        self._Data = None

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._ProductId = params.get("ProductId")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySpacePropertyResponse(AbstractModel):
    """ModifySpaceProperty返回参数结构体

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


class ModifyStudioProductRequest(AbstractModel):
    """ModifyStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductDesc: 产品描述
        :type ProductDesc: str
        :param _ModuleId: 模型ID
        :type ModuleId: int
        :param _EnableProductScript: 是否打开二进制转Json功能, 取值为字符串 true/false
        :type EnableProductScript: str
        :param _BindStrategy: 传1或者2；1代表强踢，2代表非强踢。传其它值不做任何处理
        :type BindStrategy: int
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductDesc = None
        self._ModuleId = None
        self._EnableProductScript = None
        self._BindStrategy = None

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
    def ProductDesc(self):
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def ModuleId(self):
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def EnableProductScript(self):
        return self._EnableProductScript

    @EnableProductScript.setter
    def EnableProductScript(self, EnableProductScript):
        self._EnableProductScript = EnableProductScript

    @property
    def BindStrategy(self):
        return self._BindStrategy

    @BindStrategy.setter
    def BindStrategy(self, BindStrategy):
        self._BindStrategy = BindStrategy


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProductDesc = params.get("ProductDesc")
        self._ModuleId = params.get("ModuleId")
        self._EnableProductScript = params.get("EnableProductScript")
        self._BindStrategy = params.get("BindStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStudioProductResponse(AbstractModel):
    """ModifyStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品描述
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = ProductEntry()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class ModifyTopicPolicyRequest(AbstractModel):
    """ModifyTopicPolicy请求参数结构体

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
        """
        self._ProductId = None
        self._TopicName = None
        self._NewTopicName = None
        self._Privilege = None

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


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        self._NewTopicName = params.get("NewTopicName")
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicPolicyResponse(AbstractModel):
    """ModifyTopicPolicy返回参数结构体

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


class ModifyTopicRuleRequest(AbstractModel):
    """ModifyTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _TopicRulePayload: 替换的规则包体
        :type TopicRulePayload: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`
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
        


class ModifyTopicRuleResponse(AbstractModel):
    """ModifyTopicRule返回参数结构体

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


class PackageConsumeStat(AbstractModel):
    """云存套餐包消耗统计

    """

    def __init__(self):
        r"""
        :param _PackageId: 云存套餐包id
        :type PackageId: str
        :param _PackageName: 云存套餐包名称
        :type PackageName: str
        :param _Cnt: 消耗个数
        :type Cnt: int
        :param _Price: 套餐包单价，单位分
        :type Price: int
        :param _Source: 消耗来源，1预付费
        :type Source: int
        """
        self._PackageId = None
        self._PackageName = None
        self._Cnt = None
        self._Price = None
        self._Source = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Cnt(self):
        return self._Cnt

    @Cnt.setter
    def Cnt(self, Cnt):
        self._Cnt = Cnt

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        self._Cnt = params.get("Cnt")
        self._Price = params.get("Price")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageConsumeTask(AbstractModel):
    """套餐包消耗任务列表

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        :param _CreateTime: 任务创始时间
        :type CreateTime: str
        :param _State: 任务状态，1待处理，2处理中，3已完成
        :type State: int
        """
        self._TaskId = None
        self._CreateTime = None
        self._State = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageInfo(AbstractModel):
    """结构体（PackageInfo）记录了设备拥有的有效套餐信息，包括云存开启状态、云存类型、云存回看时长、云存套餐过期时间

    """

    def __init__(self):
        r"""
        :param _Status: 云存开启状态，0为未开启，2为正在生效，1为已过期
注：这里只返回状态为0的数据
        :type Status: int
        :param _CSType: 云存类型，1为全时云存，2为事件云存
        :type CSType: int
        :param _CSShiftDuration: 云存回看时长
        :type CSShiftDuration: int
        :param _CSExpiredTime: 云存套餐过期时间
        :type CSExpiredTime: int
        :param _CreatedAt: 云存套餐创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: int
        :param _UpdatedAt: 云存套餐更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: int
        :param _PackageId: 套餐id
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _OrderId: 订单id
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _ChannelId: 通道id
        :type ChannelId: int
        :param _CSUserId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type CSUserId: str
        """
        self._Status = None
        self._CSType = None
        self._CSShiftDuration = None
        self._CSExpiredTime = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._PackageId = None
        self._OrderId = None
        self._ChannelId = None
        self._CSUserId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CSType(self):
        return self._CSType

    @CSType.setter
    def CSType(self, CSType):
        self._CSType = CSType

    @property
    def CSShiftDuration(self):
        return self._CSShiftDuration

    @CSShiftDuration.setter
    def CSShiftDuration(self, CSShiftDuration):
        self._CSShiftDuration = CSShiftDuration

    @property
    def CSExpiredTime(self):
        return self._CSExpiredTime

    @CSExpiredTime.setter
    def CSExpiredTime(self, CSExpiredTime):
        self._CSExpiredTime = CSExpiredTime

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def CSUserId(self):
        return self._CSUserId

    @CSUserId.setter
    def CSUserId(self, CSUserId):
        self._CSUserId = CSUserId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CSType = params.get("CSType")
        self._CSShiftDuration = params.get("CSShiftDuration")
        self._CSExpiredTime = params.get("CSExpiredTime")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._PackageId = params.get("PackageId")
        self._OrderId = params.get("OrderId")
        self._ChannelId = params.get("ChannelId")
        self._CSUserId = params.get("CSUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionFenceInfo(AbstractModel):
    """围栏详细信息(包含创建时间及更新时间)

    """

    def __init__(self):
        r"""
        :param _GeoFence: 围栏信息
        :type GeoFence: :class:`tencentcloud.iotexplorer.v20190423.models.PositionFenceItem`
        :param _CreateTime: 围栏创建时间
        :type CreateTime: int
        :param _UpdateTime: 围栏更新时间
        :type UpdateTime: int
        """
        self._GeoFence = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def GeoFence(self):
        return self._GeoFence

    @GeoFence.setter
    def GeoFence(self, GeoFence):
        self._GeoFence = GeoFence

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


    def _deserialize(self, params):
        if params.get("GeoFence") is not None:
            self._GeoFence = PositionFenceItem()
            self._GeoFence._deserialize(params.get("GeoFence"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionFenceItem(AbstractModel):
    """围栏信息

    """

    def __init__(self):
        r"""
        :param _FenceId: 围栏Id
        :type FenceId: int
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _FenceName: 围栏名称
        :type FenceName: str
        :param _FenceDesc: 围栏描述
        :type FenceDesc: str
        :param _FenceArea: 围栏区域信息，采用 GeoJSON 格式
        :type FenceArea: str
        """
        self._FenceId = None
        self._SpaceId = None
        self._FenceName = None
        self._FenceDesc = None
        self._FenceArea = None

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FenceName(self):
        return self._FenceName

    @FenceName.setter
    def FenceName(self, FenceName):
        self._FenceName = FenceName

    @property
    def FenceDesc(self):
        return self._FenceDesc

    @FenceDesc.setter
    def FenceDesc(self, FenceDesc):
        self._FenceDesc = FenceDesc

    @property
    def FenceArea(self):
        return self._FenceArea

    @FenceArea.setter
    def FenceArea(self, FenceArea):
        self._FenceArea = FenceArea


    def _deserialize(self, params):
        self._FenceId = params.get("FenceId")
        self._SpaceId = params.get("SpaceId")
        self._FenceName = params.get("FenceName")
        self._FenceDesc = params.get("FenceDesc")
        self._FenceArea = params.get("FenceArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionItem(AbstractModel):
    """位置点

    """

    def __init__(self):
        r"""
        :param _CreateTime: 位置点的时间
        :type CreateTime: int
        :param _Longitude: 位置点的经度
        :type Longitude: float
        :param _Latitude: 位置点的纬度
        :type Latitude: float
        :param _LocationType: 位置点的定位类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationType: str
        :param _Accuracy: 位置点的精度预估，单位为米
注意：此字段可能返回 null，表示取不到有效值。
        :type Accuracy: float
        """
        self._CreateTime = None
        self._Longitude = None
        self._Latitude = None
        self._LocationType = None
        self._Accuracy = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def LocationType(self):
        return self._LocationType

    @LocationType.setter
    def LocationType(self, LocationType):
        self._LocationType = LocationType

    @property
    def Accuracy(self):
        return self._Accuracy

    @Accuracy.setter
    def Accuracy(self, Accuracy):
        self._Accuracy = Accuracy


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._LocationType = params.get("LocationType")
        self._Accuracy = params.get("Accuracy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionSpaceInfo(AbstractModel):
    """位置空间详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        :param _SpaceName: 位置空间名称
        :type SpaceName: str
        :param _AuthorizeType: 授权类型
        :type AuthorizeType: int
        :param _Description: 描述备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ProductIdList: 产品列表
        :type ProductIdList: list of str
        :param _Icon: 缩略图
        :type Icon: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _Zoom: 用户自定义地图缩放
        :type Zoom: int
        """
        self._ProjectId = None
        self._SpaceId = None
        self._SpaceName = None
        self._AuthorizeType = None
        self._Description = None
        self._ProductIdList = None
        self._Icon = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Zoom = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SpaceId(self):
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def AuthorizeType(self):
        return self._AuthorizeType

    @AuthorizeType.setter
    def AuthorizeType(self, AuthorizeType):
        self._AuthorizeType = AuthorizeType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductIdList(self):
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

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
    def Zoom(self):
        return self._Zoom

    @Zoom.setter
    def Zoom(self, Zoom):
        self._Zoom = Zoom


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SpaceId = params.get("SpaceId")
        self._SpaceName = params.get("SpaceName")
        self._AuthorizeType = params.get("AuthorizeType")
        self._Description = params.get("Description")
        self._ProductIdList = params.get("ProductIdList")
        self._Icon = params.get("Icon")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Zoom = params.get("Zoom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductDevicesPositionItem(AbstractModel):
    """产品设备位置信息

    """

    def __init__(self):
        r"""
        :param _Items: 设备位置列表
        :type Items: list of DevicePositionItem
        :param _ProductId: 产品标识
        :type ProductId: str
        :param _Total: 设备位置数量
        :type Total: int
        """
        self._Items = None
        self._ProductId = None
        self._Total = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DevicePositionItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._ProductId = params.get("ProductId")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductEntry(AbstractModel):
    """产品详情

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _CategoryId: 产品分组模板ID
        :type CategoryId: int
        :param _EncryptionType: 加密类型。1表示证书认证，2表示秘钥认证，21表示TID认证-SE方式，22表示TID认证-软加固方式
        :type EncryptionType: str
        :param _NetType: 连接类型。如：
wifi、wifi-ble、cellular、5g、lorawan、ble、ethernet、wifi-ethernet、else、sub_zigbee、sub_ble、sub_433mhz、sub_else、sub_blemesh
        :type NetType: str
        :param _DataProtocol: 数据协议 (1 使用物模型 2 为自定义类型)
        :type DataProtocol: int
        :param _ProductDesc: 产品描述
        :type ProductDesc: str
        :param _DevStatus: 状态 如：all 全部, dev 开发中, audit 审核中 released 已发布
        :type DevStatus: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _Region: 区域
        :type Region: str
        :param _ProductType: 产品类型。如： 0 普通产品 ， 5 网关产品
        :type ProductType: int
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ModuleId: 产品ModuleId
        :type ModuleId: int
        :param _EnableProductScript: 是否使用脚本进行二进制转json功能 可以取值 true / false
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableProductScript: str
        :param _CreateUserId: 创建人 UinId
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _CreatorNickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
        :param _BindStrategy: 绑定策略（1：强踢；2：非强踢；0：表示无意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type BindStrategy: int
        :param _DeviceCount: 设备数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCount: int
        :param _Rate: 平均传输速率
注意：此字段可能返回 null，表示取不到有效值。
        :type Rate: str
        :param _Period: 有效期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: str
        """
        self._ProductId = None
        self._ProductName = None
        self._CategoryId = None
        self._EncryptionType = None
        self._NetType = None
        self._DataProtocol = None
        self._ProductDesc = None
        self._DevStatus = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Region = None
        self._ProductType = None
        self._ProjectId = None
        self._ModuleId = None
        self._EnableProductScript = None
        self._CreateUserId = None
        self._CreatorNickName = None
        self._BindStrategy = None
        self._DeviceCount = None
        self._Rate = None
        self._Period = None

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
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def EncryptionType(self):
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def DataProtocol(self):
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def ProductDesc(self):
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def DevStatus(self):
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModuleId(self):
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def EnableProductScript(self):
        return self._EnableProductScript

    @EnableProductScript.setter
    def EnableProductScript(self, EnableProductScript):
        self._EnableProductScript = EnableProductScript

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def BindStrategy(self):
        return self._BindStrategy

    @BindStrategy.setter
    def BindStrategy(self, BindStrategy):
        self._BindStrategy = BindStrategy

    @property
    def DeviceCount(self):
        return self._DeviceCount

    @DeviceCount.setter
    def DeviceCount(self, DeviceCount):
        self._DeviceCount = DeviceCount

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._CategoryId = params.get("CategoryId")
        self._EncryptionType = params.get("EncryptionType")
        self._NetType = params.get("NetType")
        self._DataProtocol = params.get("DataProtocol")
        self._ProductDesc = params.get("ProductDesc")
        self._DevStatus = params.get("DevStatus")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Region = params.get("Region")
        self._ProductType = params.get("ProductType")
        self._ProjectId = params.get("ProjectId")
        self._ModuleId = params.get("ModuleId")
        self._EnableProductScript = params.get("EnableProductScript")
        self._CreateUserId = params.get("CreateUserId")
        self._CreatorNickName = params.get("CreatorNickName")
        self._BindStrategy = params.get("BindStrategy")
        self._DeviceCount = params.get("DeviceCount")
        self._Rate = params.get("Rate")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ModelDefine: 模型定义
        :type ModelDefine: str
        :param _UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        :param _CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param _CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        :param _NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypeModel: str
        """
        self._ProductId = None
        self._ModelDefine = None
        self._UpdateTime = None
        self._CreateTime = None
        self._CategoryModel = None
        self._NetTypeModel = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelDefine(self):
        return self._ModelDefine

    @ModelDefine.setter
    def ModelDefine(self, ModelDefine):
        self._ModelDefine = ModelDefine

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CategoryModel(self):
        return self._CategoryModel

    @CategoryModel.setter
    def CategoryModel(self, CategoryModel):
        self._CategoryModel = CategoryModel

    @property
    def NetTypeModel(self):
        return self._NetTypeModel

    @NetTypeModel.setter
    def NetTypeModel(self, NetTypeModel):
        self._NetTypeModel = NetTypeModel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ModelDefine = params.get("ModelDefine")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._CategoryModel = params.get("CategoryModel")
        self._NetTypeModel = params.get("NetTypeModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectEntry(AbstractModel):
    """项目详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param _CreateTime: 创建时间，unix时间戳
        :type CreateTime: int
        :param _UpdateTime: 更新时间，unix时间戳
        :type UpdateTime: int
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDesc = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc

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


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDesc = params.get("ProjectDesc")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectEntryEx(AbstractModel):
    """项目详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param _CreateTime: 项目创建时间，unix时间戳
        :type CreateTime: int
        :param _UpdateTime: 项目更新时间，unix时间戳
        :type UpdateTime: int
        :param _ProductCount: 产品数量
        :type ProductCount: int
        :param _NativeAppCount: NativeApp数量
        :type NativeAppCount: int
        :param _WebAppCount: WebApp数量
        :type WebAppCount: int
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ApplicationCount: 应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationCount: int
        :param _DeviceCount: 设备注册总数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCount: int
        :param _EnableOpenState: 是否开通物联使能
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableOpenState: int
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDesc = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ProductCount = None
        self._NativeAppCount = None
        self._WebAppCount = None
        self._InstanceId = None
        self._ApplicationCount = None
        self._DeviceCount = None
        self._EnableOpenState = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc

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
    def ProductCount(self):
        return self._ProductCount

    @ProductCount.setter
    def ProductCount(self, ProductCount):
        self._ProductCount = ProductCount

    @property
    def NativeAppCount(self):
        return self._NativeAppCount

    @NativeAppCount.setter
    def NativeAppCount(self, NativeAppCount):
        self._NativeAppCount = NativeAppCount

    @property
    def WebAppCount(self):
        return self._WebAppCount

    @WebAppCount.setter
    def WebAppCount(self, WebAppCount):
        self._WebAppCount = WebAppCount

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApplicationCount(self):
        return self._ApplicationCount

    @ApplicationCount.setter
    def ApplicationCount(self, ApplicationCount):
        self._ApplicationCount = ApplicationCount

    @property
    def DeviceCount(self):
        return self._DeviceCount

    @DeviceCount.setter
    def DeviceCount(self, DeviceCount):
        self._DeviceCount = DeviceCount

    @property
    def EnableOpenState(self):
        return self._EnableOpenState

    @EnableOpenState.setter
    def EnableOpenState(self, EnableOpenState):
        self._EnableOpenState = EnableOpenState


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDesc = params.get("ProjectDesc")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ProductCount = params.get("ProductCount")
        self._NativeAppCount = params.get("NativeAppCount")
        self._WebAppCount = params.get("WebAppCount")
        self._InstanceId = params.get("InstanceId")
        self._ApplicationCount = params.get("ApplicationCount")
        self._DeviceCount = params.get("DeviceCount")
        self._EnableOpenState = params.get("EnableOpenState")
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
        :param _PayloadEncoding: ayload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
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
        :param _TaskId: 广播消息任务Id
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


class PublishFirmwareUpdateMessageRequest(AbstractModel):
    """PublishFirmwareUpdateMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品 ID。
        :type ProductID: str
        :param _DeviceName: 设备名称。
        :type DeviceName: str
        """
        self._ProductID = None
        self._DeviceName = None

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
        


class PublishFirmwareUpdateMessageResponse(AbstractModel):
    """PublishFirmwareUpdateMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 请求状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Topic: 消息发往的主题
        :type Topic: str
        :param _Payload: 云端下发到设备的控制报文
        :type Payload: str
        :param _Qos: 消息服务质量等级，取值为0或1
        :type Qos: int
        :param _PayloadEncoding: Payload的内容编码格式，取值为base64或空。base64表示云端将接收到的base64编码后的报文再转换成二进制报文下发至设备，为空表示不作转换，透传下发至设备
        :type PayloadEncoding: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Topic = None
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
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

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
        self._DeviceName = params.get("DeviceName")
        self._Topic = params.get("Topic")
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
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: int
        :param _PayloadBase64: 设备回复的消息内容，采用base64编码
注意：此字段可能返回 null，表示取不到有效值。
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


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DevStatus: 产品DevStatus
        :type DevStatus: str
        """
        self._ProductId = None
        self._DevStatus = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DevStatus(self):
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DevStatus = params.get("DevStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseStudioProductResponse(AbstractModel):
    """ReleaseStudioProduct返回参数结构体

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


class RemoveUserByRoomIdFromTRTCRequest(AbstractModel):
    """RemoveUserByRoomIdFromTRTC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间id
        :type RoomId: str
        :param _TRTCUserIds: 用户名称数组，数组元素不可重复，最长不超过 10 个。
        :type TRTCUserIds: list of str
        """
        self._RoomId = None
        self._TRTCUserIds = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TRTCUserIds(self):
        return self._TRTCUserIds

    @TRTCUserIds.setter
    def TRTCUserIds(self, TRTCUserIds):
        self._TRTCUserIds = TRTCUserIds


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._TRTCUserIds = params.get("TRTCUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByRoomIdFromTRTCResponse(AbstractModel):
    """RemoveUserByRoomIdFromTRTC返回参数结构体

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


class ResetCloudStorageAIServiceRequest(AbstractModel):
    """ResetCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
        :type ServiceType: str
        :param _ChannelId: 通道 ID
        :type ChannelId: int
        :param _UserId: 用户 ID
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._ChannelId = None
        self._UserId = None

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
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._ChannelId = params.get("ChannelId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetCloudStorageAIServiceResponse(AbstractModel):
    """ResetCloudStorageAIService返回参数结构体

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


class ResetCloudStorageEventRequest(AbstractModel):
    """ResetCloudStorageEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None
        self._ChannelId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetCloudStorageEventResponse(AbstractModel):
    """ResetCloudStorageEvent返回参数结构体

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


class ResetCloudStorageRequest(AbstractModel):
    """ResetCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ChannelId: 通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :type ChannelId: int
        :param _UserId: 云存用户Id，为空则为默认云存空间。
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ChannelId = None
        self._UserId = None

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
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetCloudStorageResponse(AbstractModel):
    """ResetCloudStorage返回参数结构体

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
        


class SearchPositionSpaceRequest(AbstractModel):
    """SearchPositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _SpaceName: 位置空间名字
        :type SpaceName: str
        :param _Offset: 偏移量，从0开始
        :type Offset: int
        :param _Limit: 最大获取数量
        :type Limit: int
        """
        self._ProjectId = None
        self._SpaceName = None
        self._Offset = None
        self._Limit = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SpaceName(self):
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

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
        self._ProjectId = params.get("ProjectId")
        self._SpaceName = params.get("SpaceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPositionSpaceResponse(AbstractModel):
    """SearchPositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 位置空间列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PositionSpaceInfo
        :param _Total: 符合条件的位置空间个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PositionSpaceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _Limit: 列表Limit
        :type Limit: int
        :param _Offset: 列表Offset
        :type Offset: int
        :param _DevStatus: 产品Status
        :type DevStatus: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Filters: 每次请求的Filters的上限为10，Filter.Values的上限为1。
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._ProductName = None
        self._Limit = None
        self._Offset = None
        self._DevStatus = None
        self._ProductId = None
        self._Filters = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DevStatus(self):
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

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
        self._ProjectId = params.get("ProjectId")
        self._ProductName = params.get("ProductName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DevStatus = params.get("DevStatus")
        self._ProductId = params.get("ProductId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchStudioProductResponse(AbstractModel):
    """SearchStudioProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 产品列表
        :type Products: list of ProductEntry
        :param _Total: 产品数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._Total = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class SearchTopicRuleRequest(AbstractModel):
    """SearchTopicRule请求参数结构体

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
        


class SearchTopicRuleResponse(AbstractModel):
    """SearchTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 搜索到的规则总数
        :type TotalCnt: int
        :param _Rules: 规则信息列表
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


class TRTCParams(AbstractModel):
    """TRTC 的参数 可以用来加入房间

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC入参: TRTC的实例ID
        :type SdkAppId: int
        :param _UserId: TRTC入参: 用户加入房间的ID
        :type UserId: str
        :param _UserSig: TRTC入参: 用户的签名用来鉴权
        :type UserSig: str
        :param _StrRoomId: TRTC入参: 加入的TRTC房间名称
        :type StrRoomId: str
        :param _PrivateKey: TRTC入参: 校验TRTC的KEY
        :type PrivateKey: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._UserSig = None
        self._StrRoomId = None
        self._PrivateKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def StrRoomId(self):
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._StrRoomId = params.get("StrRoomId")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TWeCallActiveInfo(AbstractModel):
    """TWeCall设备激活信息

    """

    def __init__(self):
        r"""
        :param _ModelId: 小程序ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _Sn: Sn信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Sn: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        """
        self._ModelId = None
        self._Sn = None
        self._ExpireTime = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Sn(self):
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Sn = params.get("Sn")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TWeCallCategoryPkgInfo(AbstractModel):
    """TWeCall分类统计数据

    """

    def __init__(self):
        r"""
        :param _PkgType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgType: int
        :param _All: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type All: int
        :param _Used: 已使用数
注意：此字段可能返回 null，表示取不到有效值。
        :type Used: int
        """
        self._PkgType = None
        self._All = None
        self._Used = None

    @property
    def PkgType(self):
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType

    @property
    def All(self):
        return self._All

    @All.setter
    def All(self, All):
        self._All = All

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used


    def _deserialize(self, params):
        self._PkgType = params.get("PkgType")
        self._All = params.get("All")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TWeCallInfo(AbstractModel):
    """TWeCall信息

    """

    def __init__(self):
        r"""
        :param _ModelId: 小程序ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _Sn: Sn信息，SN格式：产品ID_设备名
注意：此字段可能返回 null，表示取不到有效值。
        :type Sn: str
        :param _ActiveNum: 激活数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveNum: int
        """
        self._ModelId = None
        self._Sn = None
        self._ActiveNum = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Sn(self):
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ActiveNum(self):
        return self._ActiveNum

    @ActiveNum.setter
    def ActiveNum(self, ActiveNum):
        self._ActiveNum = ActiveNum


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Sn = params.get("Sn")
        self._ActiveNum = params.get("ActiveNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TWeCallPkgInfo(AbstractModel):
    """TWeCall设备信息

    """

    def __init__(self):
        r"""
        :param _PkgId: 包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param _PkgType: 包类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgType: int
        :param _CreateTime: 生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _LicenseUsedNum: 已使用
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseUsedNum: int
        :param _LicenseTotalNum: 总量
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseTotalNum: int
        """
        self._PkgId = None
        self._PkgType = None
        self._CreateTime = None
        self._ExpireTime = None
        self._Status = None
        self._LicenseUsedNum = None
        self._LicenseTotalNum = None

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgType(self):
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LicenseUsedNum(self):
        return self._LicenseUsedNum

    @LicenseUsedNum.setter
    def LicenseUsedNum(self, LicenseUsedNum):
        self._LicenseUsedNum = LicenseUsedNum

    @property
    def LicenseTotalNum(self):
        return self._LicenseTotalNum

    @LicenseTotalNum.setter
    def LicenseTotalNum(self, LicenseTotalNum):
        self._LicenseTotalNum = LicenseTotalNum


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._PkgType = params.get("PkgType")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        self._LicenseUsedNum = params.get("LicenseUsedNum")
        self._LicenseTotalNum = params.get("LicenseTotalNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThumbnailURLInfoList(AbstractModel):
    """缩略图信息

    """

    def __init__(self):
        r"""
        :param _ThumbnailURL: 缩略图访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ThumbnailURL: str
        :param _ExpireTime: 缩略图访问地址的过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        """
        self._ThumbnailURL = None
        self._ExpireTime = None

    @property
    def ThumbnailURL(self):
        return self._ThumbnailURL

    @ThumbnailURL.setter
    def ThumbnailURL(self, ThumbnailURL):
        self._ThumbnailURL = ThumbnailURL

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._ThumbnailURL = params.get("ThumbnailURL")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicItem(AbstractModel):
    """Topic信息, 包括Topic名字和权限

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _Privilege: Topic权限 , 1上报  2下发
        :type Privilege: int
        """
        self._TopicName = None
        self._Privilege = None

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


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRule(AbstractModel):
    """TopicRule结构

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称。
        :type RuleName: str
        :param _Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param _Description: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Actions: 行为的JSON字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: str
        :param _RuleDisabled: 是否禁用规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDisabled: bool
        """
        self._RuleName = None
        self._Sql = None
        self._Description = None
        self._Actions = None
        self._RuleDisabled = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def RuleDisabled(self):
        return self._RuleDisabled

    @RuleDisabled.setter
    def RuleDisabled(self, RuleDisabled):
        self._RuleDisabled = RuleDisabled


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Sql = params.get("Sql")
        self._Description = params.get("Description")
        self._Actions = params.get("Actions")
        self._RuleDisabled = params.get("RuleDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Description: 规则描述
        :type Description: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: int
        :param _RuleDisabled: 规则是否禁用
        :type RuleDisabled: bool
        """
        self._RuleName = None
        self._Description = None
        self._CreatedAt = None
        self._RuleDisabled = None

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


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        self._CreatedAt = params.get("CreatedAt")
        self._RuleDisabled = params.get("RuleDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRulePayload(AbstractModel):
    """TopicRulePayload结构

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
        


class TransferCloudStorageRequest(AbstractModel):
    """TransferCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 已开通云存的设备名称
        :type DeviceName: str
        :param _ToDeviceName: 未开通云存的设备名称
        :type ToDeviceName: str
        :param _ToProductId: 未开通云存的设备产品ID
        :type ToProductId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ToDeviceName = None
        self._ToProductId = None

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
    def ToDeviceName(self):
        return self._ToDeviceName

    @ToDeviceName.setter
    def ToDeviceName(self, ToDeviceName):
        self._ToDeviceName = ToDeviceName

    @property
    def ToProductId(self):
        return self._ToProductId

    @ToProductId.setter
    def ToProductId(self, ToProductId):
        self._ToProductId = ToProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ToDeviceName = params.get("ToDeviceName")
        self._ToProductId = params.get("ToProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferCloudStorageResponse(AbstractModel):
    """TransferCloudStorage返回参数结构体

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
        :param _DeviceNames: 设备名列表
        :type DeviceNames: list of str
        """
        self._GatewayProductId = None
        self._GatewayDeviceName = None
        self._ProductId = None
        self._DeviceNames = None

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


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
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


class UnbindProductsRequest(AbstractModel):
    """UnbindProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param _ProductIds: 待解绑的子产品ID数组
        :type ProductIds: list of str
        """
        self._GatewayProductId = None
        self._ProductIds = None

    @property
    def GatewayProductId(self):
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def ProductIds(self):
        return self._ProductIds

    @ProductIds.setter
    def ProductIds(self, ProductIds):
        self._ProductIds = ProductIds


    def _deserialize(self, params):
        self._GatewayProductId = params.get("GatewayProductId")
        self._ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindProductsResponse(AbstractModel):
    """UnbindProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayDeviceNames: 绑定了待解绑的LoRa产品下的设备的网关设备列表
        :type GatewayDeviceNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GatewayDeviceNames = None
        self._RequestId = None

    @property
    def GatewayDeviceNames(self):
        return self._GatewayDeviceNames

    @GatewayDeviceNames.setter
    def GatewayDeviceNames(self, GatewayDeviceNames):
        self._GatewayDeviceNames = GatewayDeviceNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GatewayDeviceNames = params.get("GatewayDeviceNames")
        self._RequestId = params.get("RequestId")


class UpdateDeviceTWeCallAuthorizeStatusRequest(AbstractModel):
    """UpdateDeviceTWeCallAuthorizeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: TweCall授权状态：0未授权，1已授权
        :type Status: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _WechatOpenId: 微信用户的openId
        :type WechatOpenId: str
        """
        self._Status = None
        self._ProductId = None
        self._DeviceName = None
        self._WechatOpenId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def WechatOpenId(self):
        return self._WechatOpenId

    @WechatOpenId.setter
    def WechatOpenId(self, WechatOpenId):
        self._WechatOpenId = WechatOpenId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._WechatOpenId = params.get("WechatOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceTWeCallAuthorizeStatusResponse(AbstractModel):
    """UpdateDeviceTWeCallAuthorizeStatus返回参数结构体

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


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DevicesItems: 多个设备标识
        :type DevicesItems: list of DevicesItem
        :param _Status: 1：启用；0：禁用
        :type Status: int
        """
        self._DevicesItems = None
        self._Status = None

    @property
    def DevicesItems(self):
        return self._DevicesItems

    @DevicesItems.setter
    def DevicesItems(self, DevicesItems):
        self._DevicesItems = DevicesItems

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("DevicesItems") is not None:
            self._DevicesItems = []
            for item in params.get("DevicesItems"):
                obj = DevicesItem()
                obj._deserialize(item)
                self._DevicesItems.append(obj)
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
        :param _ResultCode: 删除的结果代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param _ResultMessage: 删除的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ResultMessage = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMessage(self):
        return self._ResultMessage

    @ResultMessage.setter
    def ResultMessage(self, ResultMessage):
        self._ResultMessage = ResultMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._ResultMessage = params.get("ResultMessage")
        self._RequestId = params.get("RequestId")


class UpdateFirmwareRequest(AbstractModel):
    """UpdateFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _FirmwareVersion: 固件新的版本号
        :type FirmwareVersion: str
        :param _FirmwareOriVersion: 固件原版本号
        :type FirmwareOriVersion: str
        :param _UpgradeMethod: 固件升级方式；0 静默升级 1 用户确认升级   不填默认静默升级
        :type UpgradeMethod: int
        """
        self._ProductID = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._FirmwareOriVersion = None
        self._UpgradeMethod = None

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


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareOriVersion = params.get("FirmwareOriVersion")
        self._UpgradeMethod = params.get("UpgradeMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFirmwareResponse(AbstractModel):
    """UpdateFirmware返回参数结构体

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
        :param _FwType: 固件升级模块；可选值 mcu|moudule
        :type FwType: str
        :param _FirmwareUserDefined: 固件用户自定义配置信息
        :type FirmwareUserDefined: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Md5sum = None
        self._FileSize = None
        self._FirmwareName = None
        self._FirmwareDescription = None
        self._FwType = None
        self._FirmwareUserDefined = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

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
    def FwType(self):
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def FirmwareUserDefined(self):
        return self._FirmwareUserDefined

    @FirmwareUserDefined.setter
    def FirmwareUserDefined(self, FirmwareUserDefined):
        self._FirmwareUserDefined = FirmwareUserDefined


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._Md5sum = params.get("Md5sum")
        self._FileSize = params.get("FileSize")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        self._FwType = params.get("FwType")
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


class WXDeviceInfo(AbstractModel):
    """微信硬件设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _WXIoTDeviceInfo: 设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WXIoTDeviceInfo: :class:`tencentcloud.iotexplorer.v20190423.models.WXIoTDeviceInfo`
        """
        self._DeviceId = None
        self._WXIoTDeviceInfo = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def WXIoTDeviceInfo(self):
        return self._WXIoTDeviceInfo

    @WXIoTDeviceInfo.setter
    def WXIoTDeviceInfo(self, WXIoTDeviceInfo):
        self._WXIoTDeviceInfo = WXIoTDeviceInfo


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        if params.get("WXIoTDeviceInfo") is not None:
            self._WXIoTDeviceInfo = WXIoTDeviceInfo()
            self._WXIoTDeviceInfo._deserialize(params.get("WXIoTDeviceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WXIoTDeviceInfo(AbstractModel):
    """微信物联网硬件信息

    """

    def __init__(self):
        r"""
        :param _SN: sn信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SN: str
        :param _SNTicket: 票据
注意：此字段可能返回 null，表示取不到有效值。
        :type SNTicket: str
        :param _ModelId: 模版ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        """
        self._SN = None
        self._SNTicket = None
        self._ModelId = None

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def SNTicket(self):
        return self._SNTicket

    @SNTicket.setter
    def SNTicket(self, SNTicket):
        self._SNTicket = SNTicket

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._SN = params.get("SN")
        self._SNTicket = params.get("SNTicket")
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WifiInfo(AbstractModel):
    """wifi定位信息

    """

    def __init__(self):
        r"""
        :param _MAC: mac地址
        :type MAC: str
        :param _RSSI: 信号强度
        :type RSSI: int
        """
        self._MAC = None
        self._RSSI = None

    @property
    def MAC(self):
        return self._MAC

    @MAC.setter
    def MAC(self, MAC):
        self._MAC = MAC

    @property
    def RSSI(self):
        return self._RSSI

    @RSSI.setter
    def RSSI(self, RSSI):
        self._RSSI = RSSI


    def _deserialize(self, params):
        self._MAC = params.get("MAC")
        self._RSSI = params.get("RSSI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        