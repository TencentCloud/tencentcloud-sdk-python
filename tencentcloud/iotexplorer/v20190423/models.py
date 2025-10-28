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


class AISearchInfo(AbstractModel):
    r"""AI视频搜索结果结构体。

    """

    def __init__(self):
        r"""
        :param _Summary: 基于搜索结果的总结
        :type Summary: str
        :param _Targets: 视频结果集
        :type Targets: list of TargetInfo
        :param _VideoURL: 视频回放URL
        :type VideoURL: str
        """
        self._Summary = None
        self._Targets = None
        self._VideoURL = None

    @property
    def Summary(self):
        r"""基于搜索结果的总结
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Targets(self):
        r"""视频结果集
        :rtype: list of TargetInfo
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def VideoURL(self):
        r"""视频回放URL
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL


    def _deserialize(self, params):
        self._Summary = params.get("Summary")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetInfo()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._VideoURL = params.get("VideoURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateDeviceInfo(AbstractModel):
    r"""设备激活详情信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceType: 实例类型
        :type InstanceType: int
        :param _DeviceActivationDetails: 设备激活信息
        :type DeviceActivationDetails: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceActivationDetail`
        :param _RegisteredDeviceType: 已注册设备类型信息
        :type RegisteredDeviceType: :class:`tencentcloud.iotexplorer.v20190423.models.RegisteredDeviceTypeInfo`
        :param _RegisteredDeviceNetType: 已注册设备通信类型信息
        :type RegisteredDeviceNetType: :class:`tencentcloud.iotexplorer.v20190423.models.RegisteredDeviceNetTypeInfo`
        """
        self._InstanceId = None
        self._InstanceType = None
        self._DeviceActivationDetails = None
        self._RegisteredDeviceType = None
        self._RegisteredDeviceNetType = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        r"""实例类型
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DeviceActivationDetails(self):
        r"""设备激活信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceActivationDetail`
        """
        return self._DeviceActivationDetails

    @DeviceActivationDetails.setter
    def DeviceActivationDetails(self, DeviceActivationDetails):
        self._DeviceActivationDetails = DeviceActivationDetails

    @property
    def RegisteredDeviceType(self):
        r"""已注册设备类型信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.RegisteredDeviceTypeInfo`
        """
        return self._RegisteredDeviceType

    @RegisteredDeviceType.setter
    def RegisteredDeviceType(self, RegisteredDeviceType):
        self._RegisteredDeviceType = RegisteredDeviceType

    @property
    def RegisteredDeviceNetType(self):
        r"""已注册设备通信类型信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.RegisteredDeviceNetTypeInfo`
        """
        return self._RegisteredDeviceNetType

    @RegisteredDeviceNetType.setter
    def RegisteredDeviceNetType(self, RegisteredDeviceNetType):
        self._RegisteredDeviceNetType = RegisteredDeviceNetType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceType = params.get("InstanceType")
        if params.get("DeviceActivationDetails") is not None:
            self._DeviceActivationDetails = DeviceActivationDetail()
            self._DeviceActivationDetails._deserialize(params.get("DeviceActivationDetails"))
        if params.get("RegisteredDeviceType") is not None:
            self._RegisteredDeviceType = RegisteredDeviceTypeInfo()
            self._RegisteredDeviceType._deserialize(params.get("RegisteredDeviceType"))
        if params.get("RegisteredDeviceNetType") is not None:
            self._RegisteredDeviceNetType = RegisteredDeviceNetTypeInfo()
            self._RegisteredDeviceNetType._deserialize(params.get("RegisteredDeviceNetType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateTWeCallLicenseRequest(AbstractModel):
    r"""ActivateTWeCallLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgType: TWecall类型：0-体验套餐；1-基础版；3-高级版；
        :type PkgType: int
        :param _MiniProgramAppId: 参数已弃用，不用传参
        :type MiniProgramAppId: str
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._PkgType = None
        self._MiniProgramAppId = None
        self._DeviceList = None

    @property
    def PkgType(self):
        r"""TWecall类型：0-体验套餐；1-基础版；3-高级版；
        :rtype: int
        """
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType

    @property
    def MiniProgramAppId(self):
        warnings.warn("parameter `MiniProgramAppId` is deprecated", DeprecationWarning) 

        r"""参数已弃用，不用传参
        :rtype: str
        """
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        warnings.warn("parameter `MiniProgramAppId` is deprecated", DeprecationWarning) 

        self._MiniProgramAppId = MiniProgramAppId

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: list of TWeCallInfo
        """
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
    r"""ActivateTWeCallLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceList: 设备激活返回数据
        :type DeviceList: list of DeviceActiveResult
        :param _FailureList: 设备激活失败返回数据
        :type FailureList: list of DeviceActiveResult
        :param _SuccessList: 设备激活成功返回数据
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
        warnings.warn("parameter `DeviceList` is deprecated", DeprecationWarning) 

        r"""设备激活返回数据
        :rtype: list of DeviceActiveResult
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        warnings.warn("parameter `DeviceList` is deprecated", DeprecationWarning) 

        self._DeviceList = DeviceList

    @property
    def FailureList(self):
        r"""设备激活失败返回数据
        :rtype: list of DeviceActiveResult
        """
        return self._FailureList

    @FailureList.setter
    def FailureList(self, FailureList):
        self._FailureList = FailureList

    @property
    def SuccessList(self):
        r"""设备激活成功返回数据
        :rtype: list of DeviceActiveResult
        """
        return self._SuccessList

    @SuccessList.setter
    def SuccessList(self, SuccessList):
        self._SuccessList = SuccessList

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
    r"""云api直接绑定设备出参

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
        r"""产品ID/设备名
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AliasName(self):
        r"""设备别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def IconUrl(self):
        r"""icon地址
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def FamilyId(self):
        r"""家庭ID
        :rtype: str
        """
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DeviceType(self):
        r"""设备类型
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: int
        """
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
        


class AuthMiniProgramAppInfo(AbstractModel):
    r"""授权小程序信息

    """

    def __init__(self):
        r"""
        :param _MiniProgramAppId: 小程序APPID
        :type MiniProgramAppId: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _MiniProgramName: 小程序名称
        :type MiniProgramName: str
        :param _LicenseNum: 激活码数
        :type LicenseNum: int
        :param _IotAppId: 应用ID 
        :type IotAppId: str
        :param _IotAppName: 应用名称
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
        r"""小程序APPID
        :rtype: str
        """
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MiniProgramName(self):
        r"""小程序名称
        :rtype: str
        """
        return self._MiniProgramName

    @MiniProgramName.setter
    def MiniProgramName(self, MiniProgramName):
        self._MiniProgramName = MiniProgramName

    @property
    def LicenseNum(self):
        r"""激活码数
        :rtype: int
        """
        return self._LicenseNum

    @LicenseNum.setter
    def LicenseNum(self, LicenseNum):
        self._LicenseNum = LicenseNum

    @property
    def IotAppId(self):
        r"""应用ID 
        :rtype: str
        """
        return self._IotAppId

    @IotAppId.setter
    def IotAppId(self, IotAppId):
        self._IotAppId = IotAppId

    @property
    def IotAppName(self):
        r"""应用名称
        :rtype: str
        """
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
    r"""获取返回列表的详情。

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
        r"""量产ID
        :rtype: str
        """
        return self._BatchProductionId

    @BatchProductionId.setter
    def BatchProductionId(self, BatchProductionId):
        self._BatchProductionId = BatchProductionId

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BurnMethod(self):
        r"""烧录方式
        :rtype: int
        """
        return self._BurnMethod

    @BurnMethod.setter
    def BurnMethod(self, BurnMethod):
        self._BurnMethod = BurnMethod

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
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
        


class BatchUpdateFirmwareRequest(AbstractModel):
    r"""BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件新版本号
        :type FirmwareVersion: str
        :param _FirmwareOriVersion: 固件原版本号
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
        :param _TimeoutInterval: 固件升级任务，默认超时时间。 最小取值120秒，最大为900秒
        :type TimeoutInterval: int
        :param _Type: 固件升级任务类型，默认静态升级值为空或1，动态升级值为7
        :type Type: int
        :param _DelayTime: 任务延迟时间
        :type DelayTime: int
        :param _OverrideMode: 是否覆盖，0不覆盖，1覆盖
        :type OverrideMode: int
        :param _MaxRetryNum: 失败重试次数
        :type MaxRetryNum: int
        :param _RetryInterval: 重试间隔min
        :type RetryInterval: int
        :param _FwType: 固件模块
        :type FwType: str
        :param _TaskUserDefine: 用户自定义信息
        :type TaskUserDefine: str
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
        self._Type = None
        self._DelayTime = None
        self._OverrideMode = None
        self._MaxRetryNum = None
        self._RetryInterval = None
        self._FwType = None
        self._TaskUserDefine = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件新版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareOriVersion(self):
        r"""固件原版本号
        :rtype: str
        """
        return self._FirmwareOriVersion

    @FirmwareOriVersion.setter
    def FirmwareOriVersion(self, FirmwareOriVersion):
        self._FirmwareOriVersion = FirmwareOriVersion

    @property
    def UpgradeMethod(self):
        r"""升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式
        :rtype: int
        """
        return self._UpgradeMethod

    @UpgradeMethod.setter
    def UpgradeMethod(self, UpgradeMethod):
        self._UpgradeMethod = UpgradeMethod

    @property
    def FileName(self):
        r"""设备列表文件名称，根据文件列表升级固件需要填写此参数
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        r"""设备列表的文件md5值
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileSize(self):
        r"""设备列表的文件大小值
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DeviceNames(self):
        r"""需要升级的设备名称列表
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def TimeoutInterval(self):
        r"""固件升级任务，默认超时时间。 最小取值120秒，最大为900秒
        :rtype: int
        """
        return self._TimeoutInterval

    @TimeoutInterval.setter
    def TimeoutInterval(self, TimeoutInterval):
        self._TimeoutInterval = TimeoutInterval

    @property
    def Type(self):
        r"""固件升级任务类型，默认静态升级值为空或1，动态升级值为7
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DelayTime(self):
        r"""任务延迟时间
        :rtype: int
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def OverrideMode(self):
        r"""是否覆盖，0不覆盖，1覆盖
        :rtype: int
        """
        return self._OverrideMode

    @OverrideMode.setter
    def OverrideMode(self, OverrideMode):
        self._OverrideMode = OverrideMode

    @property
    def MaxRetryNum(self):
        r"""失败重试次数
        :rtype: int
        """
        return self._MaxRetryNum

    @MaxRetryNum.setter
    def MaxRetryNum(self, MaxRetryNum):
        self._MaxRetryNum = MaxRetryNum

    @property
    def RetryInterval(self):
        r"""重试间隔min
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def FwType(self):
        r"""固件模块
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def TaskUserDefine(self):
        r"""用户自定义信息
        :rtype: str
        """
        return self._TaskUserDefine

    @TaskUserDefine.setter
    def TaskUserDefine(self, TaskUserDefine):
        self._TaskUserDefine = TaskUserDefine


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
        self._Type = params.get("Type")
        self._DelayTime = params.get("DelayTime")
        self._OverrideMode = params.get("OverrideMode")
        self._MaxRetryNum = params.get("MaxRetryNum")
        self._RetryInterval = params.get("RetryInterval")
        self._FwType = params.get("FwType")
        self._TaskUserDefine = params.get("TaskUserDefine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareResponse(AbstractModel):
    r"""BatchUpdateFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindCloudStorageUserRequest(AbstractModel):
    r"""BindCloudStorageUser请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
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
    r"""BindCloudStorageUser返回参数结构体

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


class BindDeviceInfo(AbstractModel):
    r"""BindDeviceInfo

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
        r"""产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称。
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
        


class BindDevicesRequest(AbstractModel):
    r"""BindDevices请求参数结构体

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
        r"""网关设备的产品ID。
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        r"""网关设备的设备名。
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        r"""被绑定设备的产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""被绑定的多个设备名。
        :rtype: list of str
        """
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
    r"""BindDevices返回参数结构体

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


class BindProductInfo(AbstractModel):
    r"""绑定、未绑定产品详细信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _ProductName: 产品名称。
        :type ProductName: str
        :param _ProjectId: 产品所属项目ID。
        :type ProjectId: str
        :param _DataProtocol: 物模型类型。
        :type DataProtocol: int
        :param _CategoryId: 产品分组模板ID
        :type CategoryId: int
        :param _ProductType: 产品类型
        :type ProductType: int
        :param _NetType: 连接类型
        :type NetType: str
        :param _DevStatus: 状态
        :type DevStatus: str
        :param _ProductOwnerName: 产品拥有者名称
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
        r"""产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        r"""产品名称。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProjectId(self):
        r"""产品所属项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DataProtocol(self):
        r"""物模型类型。
        :rtype: int
        """
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def CategoryId(self):
        r"""产品分组模板ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ProductType(self):
        r"""产品类型
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def NetType(self):
        r"""连接类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def DevStatus(self):
        r"""状态
        :rtype: str
        """
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

    @property
    def ProductOwnerName(self):
        r"""产品拥有者名称
        :rtype: str
        """
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
    r"""BindProducts请求参数结构体

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
        r"""网关产品ID。
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def ProductIds(self):
        r"""待绑定的子产品ID数组。
        :rtype: list of str
        """
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
    r"""BindProducts返回参数结构体

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


class CallDeviceActionAsyncRequest(AbstractModel):
    r"""CallDeviceActionAsync请求参数结构体

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
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ActionId(self):
        r"""产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :rtype: str
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def InputParams(self):
        r"""输入参数
        :rtype: str
        """
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
    r"""CallDeviceActionAsync返回参数结构体

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
        r"""调用Id
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Status(self):
        r"""异步调用状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._ClientToken = params.get("ClientToken")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CallDeviceActionSyncRequest(AbstractModel):
    r"""CallDeviceActionSync请求参数结构体

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
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ActionId(self):
        r"""产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义
        :rtype: str
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def InputParams(self):
        r"""输入参数
        :rtype: str
        """
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
    r"""CallDeviceActionSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientToken: 调用Id
        :type ClientToken: str
        :param _OutputParams: 输出参数，取值设备端上报$thing/up/action method为action_reply 的 response字段，物模型协议参考https://cloud.tencent.com/document/product/1081/34916#.E8.AE.BE.E5.A4.87.E8.A1.8C.E4.B8.BA.E8.B0.83.E7.94.A8
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
        r"""调用Id
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def OutputParams(self):
        r"""输出参数，取值设备端上报$thing/up/action method为action_reply 的 response字段，物模型协议参考https://cloud.tencent.com/document/product/1081/34916#.E8.AE.BE.E5.A4.87.E8.A1.8C.E4.B8.BA.E8.B0.83.E7.94.A8
        :rtype: str
        """
        return self._OutputParams

    @OutputParams.setter
    def OutputParams(self, OutputParams):
        self._OutputParams = OutputParams

    @property
    def Status(self):
        r"""返回状态，取值设备端上报$thing/up/action	method为action_reply 的 status字段，如果不包含status字段，则取默认值，空字符串，物模型协议参考https://cloud.tencent.com/document/product/1081/34916#.E8.AE.BE.E5.A4.87.E8.A1.8C.E4.B8.BA.E8.B0.83.E7.94.A8
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._ClientToken = params.get("ClientToken")
        self._OutputParams = params.get("OutputParams")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CamTag(AbstractModel):
    r"""标签数据结构

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: str
        """
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
    r"""CancelAssignTWeCallLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgId: 订单号
        :type PkgId: str
        """
        self._PkgId = None

    @property
    def PkgId(self):
        r"""订单号
        :rtype: str
        """
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
    r"""CancelAssignTWeCallLicense返回参数结构体

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


class ChangeP2PRouteRequest(AbstractModel):
    r"""ChangeP2PRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _RouteId: P2P线路
        :type RouteId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._RouteId = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def RouteId(self):
        r"""P2P线路
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeP2PRouteResponse(AbstractModel):
    r"""ChangeP2PRoute返回参数结构体

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


class CheckFirmwareUpdateRequest(AbstractModel):
    r"""CheckFirmwareUpdate请求参数结构体

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
        r"""产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称。
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
        


class CheckFirmwareUpdateResponse(AbstractModel):
    r"""CheckFirmwareUpdate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CurrentVersion: 设备当前固件版本。
        :type CurrentVersion: str
        :param _DstVersion: 固件可升级版本。
        :type DstVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CurrentVersion = None
        self._DstVersion = None
        self._RequestId = None

    @property
    def CurrentVersion(self):
        r"""设备当前固件版本。
        :rtype: str
        """
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion

    @property
    def DstVersion(self):
        r"""固件可升级版本。
        :rtype: str
        """
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

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
        self._CurrentVersion = params.get("CurrentVersion")
        self._DstVersion = params.get("DstVersion")
        self._RequestId = params.get("RequestId")


class CloudStorageAIServiceTask(AbstractModel):
    r"""云存 AI 服务任务信息

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
- `VideoToText`：视频语义理解
        :type ServiceType: str
        :param _StartTime: 对应云存视频的起始时间（秒级 UNIX 时间戳）
        :type StartTime: int
        :param _StartTimeMs: 对应云存视频的起始时间（毫秒级 UNIX 时间戳）
        :type StartTimeMs: int
        :param _EndTime: 对应云存视频的结束时间（秒级 UNIX 时间戳）
        :type EndTime: int
        :param _EndTimeMs: 对应云存视频的结束时间（毫秒级 UNIX 时间戳）
        :type EndTimeMs: int
        :param _Status: 任务状态（1：失败；2：成功但结果为空；3：成功且结果非空；4：执行中）
        :type Status: int
        :param _Result: 任务结果
        :type Result: str
        :param _Files: 任务输出文件列表
        :type Files: list of str
        :param _FilesInfo: 任务输出文件信息列表
        :type FilesInfo: list of CloudStorageAIServiceTaskFileInfo
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
        self._StartTimeMs = None
        self._EndTime = None
        self._EndTimeMs = None
        self._Status = None
        self._Result = None
        self._Files = None
        self._FilesInfo = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CustomId = None

    @property
    def TaskId(self):
        r"""云存 AI 服务任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ServiceType(self):
        r"""云存 AI 服务类型。可能取值：

- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StartTime(self):
        r"""对应云存视频的起始时间（秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StartTimeMs(self):
        r"""对应云存视频的起始时间（毫秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTime(self):
        r"""对应云存视频的结束时间（秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EndTimeMs(self):
        r"""对应云存视频的结束时间（毫秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def Status(self):
        r"""任务状态（1：失败；2：成功但结果为空；3：成功且结果非空；4：执行中）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        r"""任务结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Files(self):
        r"""任务输出文件列表
        :rtype: list of str
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def FilesInfo(self):
        r"""任务输出文件信息列表
        :rtype: list of CloudStorageAIServiceTaskFileInfo
        """
        return self._FilesInfo

    @FilesInfo.setter
    def FilesInfo(self, FilesInfo):
        self._FilesInfo = FilesInfo

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最后更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CustomId(self):
        r"""自定义任务 ID
        :rtype: str
        """
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
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTime = params.get("EndTime")
        self._EndTimeMs = params.get("EndTimeMs")
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._Files = params.get("Files")
        if params.get("FilesInfo") is not None:
            self._FilesInfo = []
            for item in params.get("FilesInfo"):
                obj = CloudStorageAIServiceTaskFileInfo()
                obj._deserialize(item)
                self._FilesInfo.append(obj)
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
        


class CloudStorageAIServiceTaskFileInfo(AbstractModel):
    r"""云存 AI 任务输出文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称（含扩展名）
        :type FileName: str
        :param _FileSize: 文件大小（单位：bytes）
        :type FileSize: int
        :param _DownloadURL: 文件下载 URL
        :type DownloadURL: str
        :param _MimeType: 文件的 MIME Type
        :type MimeType: str
        :param _VideoMetaInfo: 视频文件元数据（仅当文件为视频类型时包含该字段）
        :type VideoMetaInfo: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTaskVideoMetaInfo`
        :param _Labels: 文件标签
        :type Labels: list of CloudStorageAIServiceTaskFileLabel
        """
        self._FileName = None
        self._FileSize = None
        self._DownloadURL = None
        self._MimeType = None
        self._VideoMetaInfo = None
        self._Labels = None

    @property
    def FileName(self):
        r"""文件名称（含扩展名）
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""文件大小（单位：bytes）
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadURL(self):
        r"""文件下载 URL
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def MimeType(self):
        r"""文件的 MIME Type
        :rtype: str
        """
        return self._MimeType

    @MimeType.setter
    def MimeType(self, MimeType):
        self._MimeType = MimeType

    @property
    def VideoMetaInfo(self):
        r"""视频文件元数据（仅当文件为视频类型时包含该字段）
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTaskVideoMetaInfo`
        """
        return self._VideoMetaInfo

    @VideoMetaInfo.setter
    def VideoMetaInfo(self, VideoMetaInfo):
        self._VideoMetaInfo = VideoMetaInfo

    @property
    def Labels(self):
        r"""文件标签
        :rtype: list of CloudStorageAIServiceTaskFileLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._DownloadURL = params.get("DownloadURL")
        self._MimeType = params.get("MimeType")
        if params.get("VideoMetaInfo") is not None:
            self._VideoMetaInfo = CloudStorageAIServiceTaskVideoMetaInfo()
            self._VideoMetaInfo._deserialize(params.get("VideoMetaInfo"))
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = CloudStorageAIServiceTaskFileLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageAIServiceTaskFileLabel(AbstractModel):
    r"""云存 AI 任务输出文件标签

    """

    def __init__(self):
        r"""
        :param _Key: key1
        :type Key: str
        :param _Value: value1
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""key1
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""value1
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
        


class CloudStorageAIServiceTaskVideoMetaInfo(AbstractModel):
    r"""云存 AI 任务输出视频文件元数据

    """

    def __init__(self):
        r"""
        :param _ThumbnailFileName: 视频对应的缩略图的文件名称（含扩展名）
        :type ThumbnailFileName: str
        :param _DurationMilliSeconds: 视频时长（单位：毫秒）
        :type DurationMilliSeconds: int
        """
        self._ThumbnailFileName = None
        self._DurationMilliSeconds = None

    @property
    def ThumbnailFileName(self):
        r"""视频对应的缩略图的文件名称（含扩展名）
        :rtype: str
        """
        return self._ThumbnailFileName

    @ThumbnailFileName.setter
    def ThumbnailFileName(self, ThumbnailFileName):
        self._ThumbnailFileName = ThumbnailFileName

    @property
    def DurationMilliSeconds(self):
        r"""视频时长（单位：毫秒）
        :rtype: int
        """
        return self._DurationMilliSeconds

    @DurationMilliSeconds.setter
    def DurationMilliSeconds(self, DurationMilliSeconds):
        self._DurationMilliSeconds = DurationMilliSeconds


    def _deserialize(self, params):
        self._ThumbnailFileName = params.get("ThumbnailFileName")
        self._DurationMilliSeconds = params.get("DurationMilliSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageEvent(AbstractModel):
    r"""云存事件

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
        :type UploadStatus: str
        :param _Data: 事件自定义数据	
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
        r"""事件起始时间（Unix 时间戳，秒级
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""事件结束时间（Unix 时间戳，秒级
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Thumbnail(self):
        r"""事件缩略图
        :rtype: str
        """
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail

    @property
    def EventId(self):
        r"""事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UploadStatus(self):
        r"""事件录像上传状态，Finished: 全部上传成功 Partial: 部分上传成功 Failed: 上传失败	
        :rtype: str
        """
        return self._UploadStatus

    @UploadStatus.setter
    def UploadStatus(self, UploadStatus):
        self._UploadStatus = UploadStatus

    @property
    def Data(self):
        r"""事件自定义数据	
        :rtype: str
        """
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
        


class CloudStorageEventWithAITasks(AbstractModel):
    r"""云存事件及其关联的云存 AI 任务

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
        :type UploadStatus: str
        :param _Data: 事件自定义数据	
        :type Data: str
        :param _AITasks: 事件关联的云存 AI 任务列表
        :type AITasks: list of CloudStorageAIServiceTask
        """
        self._StartTime = None
        self._EndTime = None
        self._Thumbnail = None
        self._EventId = None
        self._UploadStatus = None
        self._Data = None
        self._AITasks = None

    @property
    def StartTime(self):
        r"""事件起始时间（Unix 时间戳，秒级
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""事件结束时间（Unix 时间戳，秒级
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Thumbnail(self):
        r"""事件缩略图
        :rtype: str
        """
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail

    @property
    def EventId(self):
        r"""事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UploadStatus(self):
        r"""事件录像上传状态，Finished: 全部上传成功 Partial: 部分上传成功 Failed: 上传失败	
        :rtype: str
        """
        return self._UploadStatus

    @UploadStatus.setter
    def UploadStatus(self, UploadStatus):
        self._UploadStatus = UploadStatus

    @property
    def Data(self):
        r"""事件自定义数据	
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AITasks(self):
        r"""事件关联的云存 AI 任务列表
        :rtype: list of CloudStorageAIServiceTask
        """
        return self._AITasks

    @AITasks.setter
    def AITasks(self, AITasks):
        self._AITasks = AITasks


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Thumbnail = params.get("Thumbnail")
        self._EventId = params.get("EventId")
        self._UploadStatus = params.get("UploadStatus")
        self._Data = params.get("Data")
        if params.get("AITasks") is not None:
            self._AITasks = []
            for item in params.get("AITasks"):
                obj = CloudStorageAIServiceTask()
                obj._deserialize(item)
                self._AITasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStoragePackageInfo(AbstractModel):
    r"""云存套餐包信息

    """

    def __init__(self):
        r"""
        :param _PackageId: 套餐包id
        :type PackageId: str
        :param _PackageName: 套餐包名字
        :type PackageName: str
        :param _Num: 套餐包数量
        :type Num: int
        :param _UsedNum: 已使用数量
        :type UsedNum: int
        """
        self._PackageId = None
        self._PackageName = None
        self._Num = None
        self._UsedNum = None

    @property
    def PackageId(self):
        r"""套餐包id
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        r"""套餐包名字
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Num(self):
        r"""套餐包数量
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def UsedNum(self):
        r"""已使用数量
        :rtype: int
        """
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        self._Num = params.get("Num")
        self._UsedNum = params.get("UsedNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeData(AbstractModel):
    r"""云存时间轴接口返回数据

    """

    def __init__(self):
        r"""
        :param _TimeList: 云存时间轴信息列表
        :type TimeList: list of CloudStorageTimeInfo
        :param _VideoURL: 播放地址
        :type VideoURL: str
        """
        self._TimeList = None
        self._VideoURL = None

    @property
    def TimeList(self):
        r"""云存时间轴信息列表
        :rtype: list of CloudStorageTimeInfo
        """
        return self._TimeList

    @TimeList.setter
    def TimeList(self, TimeList):
        self._TimeList = TimeList

    @property
    def VideoURL(self):
        r"""播放地址
        :rtype: str
        """
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
    r"""云存时间轴信息

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
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
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
    r"""云存用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
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
    r"""ControlDeviceData请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Data(self):
        r"""属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Method(self):
        r"""请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DeviceId(self):
        r"""设备ID，该字段有值将代替 ProductId/DeviceName , 通常情况不需要填写
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DataTimestamp(self):
        r"""上报数据UNIX时间戳(毫秒), 仅对Method:reported有效
        :rtype: int
        """
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
    r"""ControlDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回信息
        :type Data: str
        :param _Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic.
pushResult 是表示发送结果，其中 0 表示成功， 23101 表示设备未在线或没有订阅相关的 MQTT Topic。
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Result = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回信息
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Result(self):
        r"""JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic.
pushResult 是表示发送结果，其中 0 表示成功， 23101 表示设备未在线或没有订阅相关的 MQTT Topic。
        :rtype: str
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
        self._Data = params.get("Data")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CountDataInfo(AbstractModel):
    r"""云存上报统计信息

    """

    def __init__(self):
        r"""
        :param _VideoExceptionNum: 视频上报异常次数
        :type VideoExceptionNum: int
        :param _VideoSuccessNum: 视频上报成功次数
        :type VideoSuccessNum: int
        :param _VideoSuccessRate: 视频上报成功率

        :type VideoSuccessRate: str
        :param _EventExceptionNum: 事件上报异常次数
        :type EventExceptionNum: int
        :param _EventSuccessNum: 事件上报成功次数
        :type EventSuccessNum: int
        :param _EventSuccessRate: 事件上报成功率
        :type EventSuccessRate: str
        """
        self._VideoExceptionNum = None
        self._VideoSuccessNum = None
        self._VideoSuccessRate = None
        self._EventExceptionNum = None
        self._EventSuccessNum = None
        self._EventSuccessRate = None

    @property
    def VideoExceptionNum(self):
        r"""视频上报异常次数
        :rtype: int
        """
        return self._VideoExceptionNum

    @VideoExceptionNum.setter
    def VideoExceptionNum(self, VideoExceptionNum):
        self._VideoExceptionNum = VideoExceptionNum

    @property
    def VideoSuccessNum(self):
        r"""视频上报成功次数
        :rtype: int
        """
        return self._VideoSuccessNum

    @VideoSuccessNum.setter
    def VideoSuccessNum(self, VideoSuccessNum):
        self._VideoSuccessNum = VideoSuccessNum

    @property
    def VideoSuccessRate(self):
        r"""视频上报成功率

        :rtype: str
        """
        return self._VideoSuccessRate

    @VideoSuccessRate.setter
    def VideoSuccessRate(self, VideoSuccessRate):
        self._VideoSuccessRate = VideoSuccessRate

    @property
    def EventExceptionNum(self):
        r"""事件上报异常次数
        :rtype: int
        """
        return self._EventExceptionNum

    @EventExceptionNum.setter
    def EventExceptionNum(self, EventExceptionNum):
        self._EventExceptionNum = EventExceptionNum

    @property
    def EventSuccessNum(self):
        r"""事件上报成功次数
        :rtype: int
        """
        return self._EventSuccessNum

    @EventSuccessNum.setter
    def EventSuccessNum(self, EventSuccessNum):
        self._EventSuccessNum = EventSuccessNum

    @property
    def EventSuccessRate(self):
        r"""事件上报成功率
        :rtype: str
        """
        return self._EventSuccessRate

    @EventSuccessRate.setter
    def EventSuccessRate(self, EventSuccessRate):
        self._EventSuccessRate = EventSuccessRate


    def _deserialize(self, params):
        self._VideoExceptionNum = params.get("VideoExceptionNum")
        self._VideoSuccessNum = params.get("VideoSuccessNum")
        self._VideoSuccessRate = params.get("VideoSuccessRate")
        self._EventExceptionNum = params.get("EventExceptionNum")
        self._EventSuccessNum = params.get("EventSuccessNum")
        self._EventSuccessRate = params.get("EventSuccessRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAISearchTaskAsyncRequest(AbstractModel):
    r"""CreateAISearchTaskAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Query: 自然语言查询
        :type Query: str
        :param _SummaryLang: 搜索结果总结的语言类型，支持的类型有：en-US、zh-CN、id-ID、th-TH
        :type SummaryLang: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Query = None
        self._SummaryLang = None
        self._ChannelId = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Query(self):
        r"""自然语言查询
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def SummaryLang(self):
        r"""搜索结果总结的语言类型，支持的类型有：en-US、zh-CN、id-ID、th-TH
        :rtype: str
        """
        return self._SummaryLang

    @SummaryLang.setter
    def SummaryLang(self, SummaryLang):
        self._SummaryLang = SummaryLang

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Query = params.get("Query")
        self._SummaryLang = params.get("SummaryLang")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAISearchTaskAsyncResponse(AbstractModel):
    r"""CreateAISearchTaskAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateBatchProductionRequest(AbstractModel):
    r"""CreateBatchProduction请求参数结构体

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BurnMethod(self):
        r"""烧录方式，0为直接烧录，1为动态注册。
        :rtype: int
        """
        return self._BurnMethod

    @BurnMethod.setter
    def BurnMethod(self, BurnMethod):
        self._BurnMethod = BurnMethod

    @property
    def GenerationMethod(self):
        r"""生成方式，0为系统生成，1为文件上传。
        :rtype: int
        """
        return self._GenerationMethod

    @GenerationMethod.setter
    def GenerationMethod(self, GenerationMethod):
        self._GenerationMethod = GenerationMethod

    @property
    def UploadUrl(self):
        r"""文件上传URL，用于文件上传时填写。
        :rtype: str
        """
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def BatchCnt(self):
        r"""量产数量，用于系统生成时填写。
        :rtype: int
        """
        return self._BatchCnt

    @BatchCnt.setter
    def BatchCnt(self, BatchCnt):
        self._BatchCnt = BatchCnt

    @property
    def GenerationQRCode(self):
        r"""是否生成二维码,0为不生成，1为生成。
        :rtype: int
        """
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
    r"""CreateBatchProduction返回参数结构体

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
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchProductionId(self):
        r"""量产id
        :rtype: str
        """
        return self._BatchProductionId

    @BatchProductionId.setter
    def BatchProductionId(self, BatchProductionId):
        self._BatchProductionId = BatchProductionId

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
        self._ProjectId = params.get("ProjectId")
        self._ProductId = params.get("ProductId")
        self._BatchProductionId = params.get("BatchProductionId")
        self._RequestId = params.get("RequestId")


class CreateCloudStorageAIServiceRequest(AbstractModel):
    r"""CreateCloudStorageAIService请求参数结构体

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
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def PackageId(self):
        r"""云存 AI 套餐 ID。可选值：

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
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def OrderId(self):
        r"""订单 ID
        :rtype: str
        """
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
    r"""CreateCloudStorageAIService返回参数结构体

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
        r"""订单 ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

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
        self._OrderId = params.get("OrderId")
        self._RequestId = params.get("RequestId")


class CreateCloudStorageAIServiceTaskRequest(AbstractModel):
    r"""CreateCloudStorageAIServiceTask请求参数结构体

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
- `VideoToText`：视频语义理解
        :type ServiceType: str
        :param _StartTime: 待分析云存的起始时间
        :type StartTime: int
        :param _EndTime: 待分析云存的结束时间
        :type EndTime: int
        :param _ChannelId: 通道 ID
        :type ChannelId: int
        :param _Config: 视频分析配置参数
        :type Config: str
        :param _ROI: 视频分析识别区域
        :type ROI: str
        :param _VideoURLs: 分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :type VideoURLs: list of str
        :param _CustomId: 自定义任务 ID
        :type CustomId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._StartTime = None
        self._EndTime = None
        self._ChannelId = None
        self._Config = None
        self._ROI = None
        self._VideoURLs = None
        self._CustomId = None

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StartTime(self):
        r"""待分析云存的起始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""待分析云存的结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Config(self):
        r"""视频分析配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ROI(self):
        r"""视频分析识别区域
        :rtype: str
        """
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI

    @property
    def VideoURLs(self):
        r"""分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :rtype: list of str
        """
        return self._VideoURLs

    @VideoURLs.setter
    def VideoURLs(self, VideoURLs):
        self._VideoURLs = VideoURLs

    @property
    def CustomId(self):
        r"""自定义任务 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ChannelId = params.get("ChannelId")
        self._Config = params.get("Config")
        self._ROI = params.get("ROI")
        self._VideoURLs = params.get("VideoURLs")
        self._CustomId = params.get("CustomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudStorageAIServiceTaskResponse(AbstractModel):
    r"""CreateCloudStorageAIServiceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDeviceChannelRequest(AbstractModel):
    r"""CreateDeviceChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._ChannelId = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceChannelResponse(AbstractModel):
    r"""CreateDeviceChannel返回参数结构体

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


class CreateDeviceRequest(AbstractModel):
    r"""CreateDevice请求参数结构体

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
        r"""产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevAddr(self):
        r"""LoRaWAN 设备地址
        :rtype: str
        """
        return self._DevAddr

    @DevAddr.setter
    def DevAddr(self, DevAddr):
        self._DevAddr = DevAddr

    @property
    def AppKey(self):
        r"""LoRaWAN 应用密钥
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def DevEUI(self):
        r"""LoRaWAN 设备唯一标识
        :rtype: str
        """
        return self._DevEUI

    @DevEUI.setter
    def DevEUI(self, DevEUI):
        self._DevEUI = DevEUI

    @property
    def AppSKey(self):
        r"""LoRaWAN 应用会话密钥
        :rtype: str
        """
        return self._AppSKey

    @AppSKey.setter
    def AppSKey(self, AppSKey):
        self._AppSKey = AppSKey

    @property
    def NwkSKey(self):
        r"""LoRaWAN 网络会话密钥
        :rtype: str
        """
        return self._NwkSKey

    @NwkSKey.setter
    def NwkSKey(self, NwkSKey):
        self._NwkSKey = NwkSKey

    @property
    def DefinedPsk(self):
        r"""手动指定设备的PSK密钥
        :rtype: str
        """
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
    r"""CreateDevice返回参数结构体

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
        r"""设备参数描述。
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateExternalSourceAIServiceTaskRequest(AbstractModel):
    r"""CreateExternalSourceAIServiceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :type ServiceType: str
        :param _VideoURLs: 分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :type VideoURLs: list of str
        :param _CustomId: 自定义任务 ID
        :type CustomId: str
        :param _Config: 视频分析配置参数
        :type Config: str
        :param _ROI: 视频分析识别区域
        :type ROI: str
        """
        self._ProductId = None
        self._ServiceType = None
        self._VideoURLs = None
        self._CustomId = None
        self._Config = None
        self._ROI = None

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def VideoURLs(self):
        r"""分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :rtype: list of str
        """
        return self._VideoURLs

    @VideoURLs.setter
    def VideoURLs(self, VideoURLs):
        self._VideoURLs = VideoURLs

    @property
    def CustomId(self):
        r"""自定义任务 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def Config(self):
        r"""视频分析配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ROI(self):
        r"""视频分析识别区域
        :rtype: str
        """
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ServiceType = params.get("ServiceType")
        self._VideoURLs = params.get("VideoURLs")
        self._CustomId = params.get("CustomId")
        self._Config = params.get("Config")
        self._ROI = params.get("ROI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExternalSourceAIServiceTaskResponse(AbstractModel):
    r"""CreateExternalSourceAIServiceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateFenceBindRequest(AbstractModel):
    r"""CreateFenceBind请求参数结构体

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
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Items(self):
        r"""围栏绑定的产品列表
        :rtype: list of FenceBindProductItem
        """
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
    r"""CreateFenceBind返回参数结构体

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


class CreateFreeCloudStorageRequest(AbstractModel):
    r"""CreateFreeCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _PackageId: 云存套餐ID：
lye1w3d：低功耗事件3天周套餐。
ye1w3d：事件3天周套餐
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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def PackageId(self):
        r"""云存套餐ID：
lye1w3d：低功耗事件3天周套餐。
ye1w3d：事件3天周套餐
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Override(self):
        r"""如果当前设备已开启云存套餐，Override=1会使用新套餐覆盖原有套餐。不传此参数则默认为0。
        :rtype: int
        """
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def PackageQueue(self):
        r"""套餐列表顺序：PackageQueue=front会立即使用新购买的套餐，新购套餐结束后，列表中下一个未过期的套餐继续生效；PackageQueue=end会等设备当前所有已购买套餐过期后才会生效新购套餐。与Override参数不能同时使用。
        :rtype: str
        """
        return self._PackageQueue

    @PackageQueue.setter
    def PackageQueue(self, PackageQueue):
        self._PackageQueue = PackageQueue

    @property
    def OrderId(self):
        r"""订单id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StorageRegion(self):
        r"""云存视频存储区域，国内默认为ap-guangzhou。海外默认为东南亚ap-singapore，可选美东na-ashburn、欧洲eu-frankfurt。
        :rtype: str
        """
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
        


class CreateFreeCloudStorageResponse(AbstractModel):
    r"""CreateFreeCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 订单金额，单位为分
        :type Price: int
        :param _Amount: 支付金额，单位为分
        :type Amount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._Amount = None
        self._RequestId = None

    @property
    def Price(self):
        r"""订单金额，单位为分
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Amount(self):
        r"""支付金额，单位为分
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

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
        self._Price = params.get("Price")
        self._Amount = params.get("Amount")
        self._RequestId = params.get("RequestId")


class CreateIotVideoCloudStorageRequest(AbstractModel):
    r"""CreateIotVideoCloudStorage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def PackageId(self):
        r"""云存套餐ID：
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
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Override(self):
        r"""如果当前设备已开启云存套餐，Override=1会使用新套餐覆盖原有套餐。不传此参数则默认为0。
        :rtype: int
        """
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def PackageQueue(self):
        r"""套餐列表顺序：PackageQueue=front会立即使用新购买的套餐，新购套餐结束后，列表中下一个未过期的套餐继续生效；PackageQueue=end会等设备当前所有已购买套餐过期后才会生效新购套餐。与Override参数不能同时使用。
        :rtype: str
        """
        return self._PackageQueue

    @PackageQueue.setter
    def PackageQueue(self, PackageQueue):
        self._PackageQueue = PackageQueue

    @property
    def OrderId(self):
        r"""订单id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StorageRegion(self):
        r"""云存视频存储区域，国内默认为ap-guangzhou。海外默认为东南亚ap-singapore，可选美东na-ashburn、欧洲eu-frankfurt。
        :rtype: str
        """
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
    r"""CreateIotVideoCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 订单金额，单位为分
        :type Price: int
        :param _Amount: 支付金额，单位为分
        :type Amount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._Amount = None
        self._RequestId = None

    @property
    def Price(self):
        r"""订单金额，单位为分
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Amount(self):
        r"""支付金额，单位为分
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

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
        self._Price = params.get("Price")
        self._Amount = params.get("Amount")
        self._RequestId = params.get("RequestId")


class CreateLoRaFrequencyRequest(AbstractModel):
    r"""CreateLoRaFrequency请求参数结构体

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
        r"""频点配置名称
        :rtype: str
        """
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def ChannelsDataUp(self):
        r"""数据上行信道
        :rtype: list of int non-negative
        """
        return self._ChannelsDataUp

    @ChannelsDataUp.setter
    def ChannelsDataUp(self, ChannelsDataUp):
        self._ChannelsDataUp = ChannelsDataUp

    @property
    def ChannelsDataRX1(self):
        r"""数据下行RX1信道
        :rtype: list of int non-negative
        """
        return self._ChannelsDataRX1

    @ChannelsDataRX1.setter
    def ChannelsDataRX1(self, ChannelsDataRX1):
        self._ChannelsDataRX1 = ChannelsDataRX1

    @property
    def ChannelsDataRX2(self):
        r"""数据下行RX2信道
        :rtype: list of int non-negative
        """
        return self._ChannelsDataRX2

    @ChannelsDataRX2.setter
    def ChannelsDataRX2(self, ChannelsDataRX2):
        self._ChannelsDataRX2 = ChannelsDataRX2

    @property
    def ChannelsJoinUp(self):
        r"""入网上行信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinUp

    @ChannelsJoinUp.setter
    def ChannelsJoinUp(self, ChannelsJoinUp):
        self._ChannelsJoinUp = ChannelsJoinUp

    @property
    def ChannelsJoinRX1(self):
        r"""入网下行RX1信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinRX1

    @ChannelsJoinRX1.setter
    def ChannelsJoinRX1(self, ChannelsJoinRX1):
        self._ChannelsJoinRX1 = ChannelsJoinRX1

    @property
    def ChannelsJoinRX2(self):
        r"""入网下行RX2信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinRX2

    @ChannelsJoinRX2.setter
    def ChannelsJoinRX2(self, ChannelsJoinRX2):
        self._ChannelsJoinRX2 = ChannelsJoinRX2

    @property
    def Description(self):
        r"""频点配置描述
        :rtype: str
        """
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
    r"""CreateLoRaFrequency返回参数结构体

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
        r"""LoRa频点信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = LoRaFrequencyEntry()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateLoRaGatewayRequest(AbstractModel):
    r"""CreateLoRaGateway请求参数结构体

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
        r"""LoRa 网关Id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""网关名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""详情描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Location(self):
        r"""位置坐标
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Position(self):
        r"""位置信息
        :rtype: str
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def PositionDetails(self):
        r"""位置详情
        :rtype: str
        """
        return self._PositionDetails

    @PositionDetails.setter
    def PositionDetails(self, PositionDetails):
        self._PositionDetails = PositionDetails

    @property
    def IsPublic(self):
        r"""是否公开
        :rtype: bool
        """
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def FrequencyId(self):
        r"""频点ID
        :rtype: str
        """
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
    r"""CreateLoRaGateway返回参数结构体

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
        r"""LoRa 网关信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`
        """
        return self._Gateway

    @Gateway.setter
    def Gateway(self, Gateway):
        self._Gateway = Gateway

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
        if params.get("Gateway") is not None:
            self._Gateway = LoRaGatewayItem()
            self._Gateway._deserialize(params.get("Gateway"))
        self._RequestId = params.get("RequestId")


class CreateOtaModuleRequest(AbstractModel):
    r"""CreateOtaModule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FwType: 模块类型
        :type FwType: str
        :param _Name: 模块类型名称
        :type Name: str
        :param _Remark: 类型描述
        :type Remark: str
        """
        self._ProductID = None
        self._FwType = None
        self._Name = None
        self._Remark = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FwType(self):
        r"""模块类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Name(self):
        r"""模块类型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""类型描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FwType = params.get("FwType")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOtaModuleResponse(AbstractModel):
    r"""CreateOtaModule返回参数结构体

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


class CreatePositionFenceRequest(AbstractModel):
    r"""CreatePositionFence请求参数结构体

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
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FenceName(self):
        r"""围栏名称
        :rtype: str
        """
        return self._FenceName

    @FenceName.setter
    def FenceName(self, FenceName):
        self._FenceName = FenceName

    @property
    def FenceArea(self):
        r"""围栏区域信息，采用 GeoJSON 格式
        :rtype: str
        """
        return self._FenceArea

    @FenceArea.setter
    def FenceArea(self, FenceArea):
        self._FenceArea = FenceArea

    @property
    def FenceDesc(self):
        r"""围栏描述
        :rtype: str
        """
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
    r"""CreatePositionFence返回参数结构体

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


class CreatePositionSpaceRequest(AbstractModel):
    r"""CreatePositionSpace请求参数结构体

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SpaceName(self):
        r"""空间名称
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def AuthorizeType(self):
        r"""授权类型，0：只读 1：读写
        :rtype: int
        """
        return self._AuthorizeType

    @AuthorizeType.setter
    def AuthorizeType(self, AuthorizeType):
        self._AuthorizeType = AuthorizeType

    @property
    def ProductIdList(self):
        r"""产品列表
        :rtype: list of str
        """
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Icon(self):
        r"""缩略图
        :rtype: str
        """
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
    r"""CreatePositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间Id
        :type SpaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceId = None
        self._RequestId = None

    @property
    def SpaceId(self):
        r"""空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

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
        self._SpaceId = params.get("SpaceId")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    r"""CreateProject请求参数结构体

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
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        r"""项目描述
        :rtype: str
        """
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc

    @property
    def InstanceId(self):
        r"""实例ID，不带实例ID，默认为公共实例
        :rtype: str
        """
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
    r"""CreateProject返回参数结构体

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
        r"""返回信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

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
        if params.get("Project") is not None:
            self._Project = ProjectEntry()
            self._Project._deserialize(params.get("Project"))
        self._RequestId = params.get("RequestId")


class CreateStudioProductRequest(AbstractModel):
    r"""CreateStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param _CategoryId: 产品分组模板ID , ( 自定义模板填写1 , 控制台调用会使用预置的其他ID)
        :type CategoryId: int
        :param _ProductType: 产品类型 填写 ( 0 普通产品 ， 5 网关产品)
        :type ProductType: int
        :param _EncryptionType: 加密类型 ，1表示证书认证，2表示密钥认证，21表示TID认证-SE方式，22表示TID认证-软加固方式
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
        r"""产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def CategoryId(self):
        r"""产品分组模板ID , ( 自定义模板填写1 , 控制台调用会使用预置的其他ID)
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ProductType(self):
        r"""产品类型 填写 ( 0 普通产品 ， 5 网关产品)
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def EncryptionType(self):
        r"""加密类型 ，1表示证书认证，2表示密钥认证，21表示TID认证-SE方式，22表示TID认证-软加固方式
        :rtype: str
        """
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def NetType(self):
        r"""连接类型 可以填写 wifi、wifi-ble、cellular、5g、lorawan、ble、ethernet、wifi-ethernet、else、sub_zigbee、sub_ble、sub_433mhz、sub_else、sub_blemesh
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def DataProtocol(self):
        r"""数据协议 (1 使用物模型 2 为自定义)
        :rtype: int
        """
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def ProductDesc(self):
        r"""产品描述
        :rtype: str
        """
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def ProjectId(self):
        r"""产品的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Rate(self):
        r"""平均传输速率
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Period(self):
        r"""期限
        :rtype: str
        """
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
    r"""CreateStudioProduct返回参数结构体

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
        r"""产品描述
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

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
        if params.get("Product") is not None:
            self._Product = ProductEntry()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class CreateTRTCSignaturesWithRoomIdRequest(AbstractModel):
    r"""CreateTRTCSignaturesWithRoomId请求参数结构体

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
        r"""TRTC进房间的用户名称数组，数组元素不可重复，最长不超过 10 个。
        :rtype: list of str
        """
        return self._TRTCUserIds

    @TRTCUserIds.setter
    def TRTCUserIds(self, TRTCUserIds):
        self._TRTCUserIds = TRTCUserIds

    @property
    def RoomId(self):
        r"""房间id
        :rtype: str
        """
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
    r"""CreateTRTCSignaturesWithRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TRTCParamList: 返回参数数组
        :type TRTCParamList: list of TRTCParams
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TRTCParamList = None
        self._RequestId = None

    @property
    def TRTCParamList(self):
        r"""返回参数数组
        :rtype: list of TRTCParams
        """
        return self._TRTCParamList

    @TRTCParamList.setter
    def TRTCParamList(self, TRTCParamList):
        self._TRTCParamList = TRTCParamList

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
        if params.get("TRTCParamList") is not None:
            self._TRTCParamList = []
            for item in params.get("TRTCParamList"):
                obj = TRTCParams()
                obj._deserialize(item)
                self._TRTCParamList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTWeSeeRecognitionTaskRequest(AbstractModel):
    r"""CreateTWeSeeRecognitionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _InputURL: 输入视频 / 图片的 URL
        :type InputURL: str
        :param _CustomId: 自定义事件 ID
        :type CustomId: str
        :param _EnableSearch: 是否保存该事件使其可被搜索
        :type EnableSearch: bool
        :param _StartTimeMs: 事件起始时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :type StartTimeMs: int
        :param _EndTimeMs: 事件结束时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :type EndTimeMs: int
        :param _Config: 算法配置
        :type Config: str
        :param _IsCustomDevice: 是否自定义设备，为 true 时不检查设备存在性，默认为 false
        :type IsCustomDevice: bool
        :param _InputType: 输入类型。可选值：

- `video`：视频（默认值）
- `image`：图片
        :type InputType: str
        :param _SummaryQOS: 摘要服务质量。可选值：

- `minutely`：分钟级（默认值）
- `immediate`：立即
        :type SummaryQOS: str
        :param _SummaryConfig: 摘要输出配置
        :type SummaryConfig: :class:`tencentcloud.iotexplorer.v20190423.models.VisionSummaryConfig`
        :param _ServiceType: 算法类型，可能取值：
- `Summary`：视频/图片摘要
- `ObjectDetect`：目标检测
        :type ServiceType: str
        :param _ObjectDetectConfig: 目标检测配置
        :type ObjectDetectConfig: :class:`tencentcloud.iotexplorer.v20190423.models.VisionObjectDetectConfig`
        """
        self._ProductId = None
        self._DeviceName = None
        self._InputURL = None
        self._CustomId = None
        self._EnableSearch = None
        self._StartTimeMs = None
        self._EndTimeMs = None
        self._Config = None
        self._IsCustomDevice = None
        self._InputType = None
        self._SummaryQOS = None
        self._SummaryConfig = None
        self._ServiceType = None
        self._ObjectDetectConfig = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def InputURL(self):
        r"""输入视频 / 图片的 URL
        :rtype: str
        """
        return self._InputURL

    @InputURL.setter
    def InputURL(self, InputURL):
        self._InputURL = InputURL

    @property
    def CustomId(self):
        r"""自定义事件 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def EnableSearch(self):
        r"""是否保存该事件使其可被搜索
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch

    @property
    def StartTimeMs(self):
        r"""事件起始时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTimeMs(self):
        r"""事件结束时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def Config(self):
        r"""算法配置
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def IsCustomDevice(self):
        r"""是否自定义设备，为 true 时不检查设备存在性，默认为 false
        :rtype: bool
        """
        return self._IsCustomDevice

    @IsCustomDevice.setter
    def IsCustomDevice(self, IsCustomDevice):
        self._IsCustomDevice = IsCustomDevice

    @property
    def InputType(self):
        r"""输入类型。可选值：

- `video`：视频（默认值）
- `image`：图片
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def SummaryQOS(self):
        r"""摘要服务质量。可选值：

- `minutely`：分钟级（默认值）
- `immediate`：立即
        :rtype: str
        """
        return self._SummaryQOS

    @SummaryQOS.setter
    def SummaryQOS(self, SummaryQOS):
        self._SummaryQOS = SummaryQOS

    @property
    def SummaryConfig(self):
        r"""摘要输出配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionSummaryConfig`
        """
        return self._SummaryConfig

    @SummaryConfig.setter
    def SummaryConfig(self, SummaryConfig):
        self._SummaryConfig = SummaryConfig

    @property
    def ServiceType(self):
        r"""算法类型，可能取值：
- `Summary`：视频/图片摘要
- `ObjectDetect`：目标检测
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ObjectDetectConfig(self):
        r"""目标检测配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionObjectDetectConfig`
        """
        return self._ObjectDetectConfig

    @ObjectDetectConfig.setter
    def ObjectDetectConfig(self, ObjectDetectConfig):
        self._ObjectDetectConfig = ObjectDetectConfig


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._InputURL = params.get("InputURL")
        self._CustomId = params.get("CustomId")
        self._EnableSearch = params.get("EnableSearch")
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTimeMs = params.get("EndTimeMs")
        self._Config = params.get("Config")
        self._IsCustomDevice = params.get("IsCustomDevice")
        self._InputType = params.get("InputType")
        self._SummaryQOS = params.get("SummaryQOS")
        if params.get("SummaryConfig") is not None:
            self._SummaryConfig = VisionSummaryConfig()
            self._SummaryConfig._deserialize(params.get("SummaryConfig"))
        self._ServiceType = params.get("ServiceType")
        if params.get("ObjectDetectConfig") is not None:
            self._ObjectDetectConfig = VisionObjectDetectConfig()
            self._ObjectDetectConfig._deserialize(params.get("ObjectDetectConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTWeSeeRecognitionTaskResponse(AbstractModel):
    r"""CreateTWeSeeRecognitionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateTWeSeeServiceRequest(AbstractModel):
    r"""CreateTWeSeeService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 服务类型
1.VideoSummary
2.ImageSummary
        :type Service: str
        """
        self._Service = None

    @property
    def Service(self):
        r"""服务类型
1.VideoSummary
2.ImageSummary
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTWeSeeServiceResponse(AbstractModel):
    r"""CreateTWeSeeService返回参数结构体

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


class CreateTWeTalkProductConfigRequest(AbstractModel):
    r"""CreateTWeTalkProductConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _SystemPrompt: 系统提示词
        :type SystemPrompt: str
        :param _GreetingMessage: 欢迎语
        :type GreetingMessage: str
        :param _VoiceType: 音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :type VoiceType: int
        :param _FastVoiceType: 复刻音色
        :type FastVoiceType: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        """
        self._ProductId = None
        self._SystemPrompt = None
        self._GreetingMessage = None
        self._VoiceType = None
        self._FastVoiceType = None
        self._TargetLanguage = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def SystemPrompt(self):
        r"""系统提示词
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt

    @property
    def GreetingMessage(self):
        r"""欢迎语
        :rtype: str
        """
        return self._GreetingMessage

    @GreetingMessage.setter
    def GreetingMessage(self, GreetingMessage):
        self._GreetingMessage = GreetingMessage

    @property
    def VoiceType(self):
        r"""音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def FastVoiceType(self):
        r"""复刻音色
        :rtype: str
        """
        return self._FastVoiceType

    @FastVoiceType.setter
    def FastVoiceType(self, FastVoiceType):
        self._FastVoiceType = FastVoiceType

    @property
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._SystemPrompt = params.get("SystemPrompt")
        self._GreetingMessage = params.get("GreetingMessage")
        self._VoiceType = params.get("VoiceType")
        self._FastVoiceType = params.get("FastVoiceType")
        self._TargetLanguage = params.get("TargetLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTWeTalkProductConfigResponse(AbstractModel):
    r"""CreateTWeTalkProductConfig返回参数结构体

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


class CreateTWeTalkProductConfigV2Request(AbstractModel):
    r"""CreateTWeTalkProductConfigV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        :param _ConfigName: 名称
        :type ConfigName: str
        :param _BasicConfig: 系统基础配置，当需要使用系统三段式配置时配置。
        :type BasicConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkBasicConfigInfo`
        :param _STTConfig: 自定义语音识别配置
        :type STTConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkSTTConfigInfo`
        :param _LLMConfig: 自定义大模型配置
        :type LLMConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkLLMConfigInfo`
        :param _TTSConfig: 语音合成配置
        :type TTSConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkTTSConfigInfo`
        :param _ConversationConfig: 会话配置
        :type ConversationConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkConversationConfigInfo`
        """
        self._ProductId = None
        self._DeviceName = None
        self._TargetLanguage = None
        self._ConfigName = None
        self._BasicConfig = None
        self._STTConfig = None
        self._LLMConfig = None
        self._TTSConfig = None
        self._ConversationConfig = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def ConfigName(self):
        r"""名称
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def BasicConfig(self):
        r"""系统基础配置，当需要使用系统三段式配置时配置。
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkBasicConfigInfo`
        """
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def STTConfig(self):
        r"""自定义语音识别配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkSTTConfigInfo`
        """
        return self._STTConfig

    @STTConfig.setter
    def STTConfig(self, STTConfig):
        self._STTConfig = STTConfig

    @property
    def LLMConfig(self):
        r"""自定义大模型配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkLLMConfigInfo`
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""语音合成配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkTTSConfigInfo`
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def ConversationConfig(self):
        r"""会话配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkConversationConfigInfo`
        """
        return self._ConversationConfig

    @ConversationConfig.setter
    def ConversationConfig(self, ConversationConfig):
        self._ConversationConfig = ConversationConfig


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._TargetLanguage = params.get("TargetLanguage")
        self._ConfigName = params.get("ConfigName")
        if params.get("BasicConfig") is not None:
            self._BasicConfig = TalkBasicConfigInfo()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("STTConfig") is not None:
            self._STTConfig = TalkSTTConfigInfo()
            self._STTConfig._deserialize(params.get("STTConfig"))
        if params.get("LLMConfig") is not None:
            self._LLMConfig = TalkLLMConfigInfo()
            self._LLMConfig._deserialize(params.get("LLMConfig"))
        if params.get("TTSConfig") is not None:
            self._TTSConfig = TalkTTSConfigInfo()
            self._TTSConfig._deserialize(params.get("TTSConfig"))
        if params.get("ConversationConfig") is not None:
            self._ConversationConfig = TalkConversationConfigInfo()
            self._ConversationConfig._deserialize(params.get("ConversationConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTWeTalkProductConfigV2Response(AbstractModel):
    r"""CreateTWeTalkProductConfigV2返回参数结构体

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


class CreateTopicPolicyRequest(AbstractModel):
    r"""CreateTopicPolicy请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        r"""Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Privilege(self):
        r"""Topic权限，1发布，2订阅，3订阅和发布
        :rtype: int
        """
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
    r"""CreateTopicPolicy返回参数结构体

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


class CreateTopicRuleRequest(AbstractModel):
    r"""CreateTopicRule请求参数结构体

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
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def TopicRulePayload(self):
        r"""规则内容
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`
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
    r"""CreateTopicRule返回参数结构体

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


class DeleteCloudStorageEventRequest(AbstractModel):
    r"""DeleteCloudStorageEvent请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def EventId(self):
        r"""事件id
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def StartTime(self):
        r"""开始时间，unix时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，unix时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
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
    r"""DeleteCloudStorageEvent返回参数结构体

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


class DeleteDeviceRequest(AbstractModel):
    r"""DeleteDevice请求参数结构体

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
        r"""产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ForceDelete(self):
        r"""是否删除绑定设备
        :rtype: bool
        """
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
    r"""DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 删除的结果代码
        :type ResultCode: str
        :param _ResultMessage: 删除的结果信息
        :type ResultMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ResultMessage = None
        self._RequestId = None

    @property
    def ResultCode(self):
        r"""删除的结果代码
        :rtype: str
        """
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMessage(self):
        r"""删除的结果信息
        :rtype: str
        """
        return self._ResultMessage

    @ResultMessage.setter
    def ResultMessage(self, ResultMessage):
        self._ResultMessage = ResultMessage

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
        self._ResultCode = params.get("ResultCode")
        self._ResultMessage = params.get("ResultMessage")
        self._RequestId = params.get("RequestId")


class DeleteDevicesRequest(AbstractModel):
    r"""DeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DevicesItems: 多个设备标识
        :type DevicesItems: list of DevicesItem
        """
        self._DevicesItems = None

    @property
    def DevicesItems(self):
        r"""多个设备标识
        :rtype: list of DevicesItem
        """
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
    r"""DeleteDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 删除的结果代码
        :type ResultCode: str
        :param _ResultMessage: 删除的结果信息
        :type ResultMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ResultMessage = None
        self._RequestId = None

    @property
    def ResultCode(self):
        r"""删除的结果代码
        :rtype: str
        """
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMessage(self):
        r"""删除的结果信息
        :rtype: str
        """
        return self._ResultMessage

    @ResultMessage.setter
    def ResultMessage(self, ResultMessage):
        self._ResultMessage = ResultMessage

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
        self._ResultCode = params.get("ResultCode")
        self._ResultMessage = params.get("ResultMessage")
        self._RequestId = params.get("RequestId")


class DeleteFenceBindRequest(AbstractModel):
    r"""DeleteFenceBind请求参数结构体

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
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Items(self):
        r"""围栏绑定的产品信息
        :rtype: list of FenceBindProductItem
        """
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
    r"""DeleteFenceBind返回参数结构体

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


class DeleteLoRaFrequencyRequest(AbstractModel):
    r"""DeleteLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FreqId: 频点唯一ID
        :type FreqId: str
        """
        self._FreqId = None

    @property
    def FreqId(self):
        r"""频点唯一ID
        :rtype: str
        """
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
    r"""DeleteLoRaFrequency返回参数结构体

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


class DeleteLoRaGatewayRequest(AbstractModel):
    r"""DeleteLoRaGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: LoRa 网关 Id
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        r"""LoRa 网关 Id
        :rtype: str
        """
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
    r"""DeleteLoRaGateway返回参数结构体

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


class DeleteOtaModuleRequest(AbstractModel):
    r"""DeleteOtaModule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FwType: 模块类型
        :type FwType: str
        """
        self._ProductID = None
        self._FwType = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FwType(self):
        r"""模块类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOtaModuleResponse(AbstractModel):
    r"""DeleteOtaModule返回参数结构体

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


class DeletePositionFenceRequest(AbstractModel):
    r"""DeletePositionFence请求参数结构体

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
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FenceId(self):
        r"""围栏Id
        :rtype: int
        """
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
    r"""DeletePositionFence返回参数结构体

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


class DeletePositionSpaceRequest(AbstractModel):
    r"""DeletePositionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 位置空间Id
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        r"""位置空间Id
        :rtype: str
        """
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
    r"""DeletePositionSpace返回参数结构体

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


class DeleteProjectRequest(AbstractModel):
    r"""DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
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
    r"""DeleteProject返回参数结构体

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


class DeleteStudioProductRequest(AbstractModel):
    r"""DeleteStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品ID
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
        


class DeleteStudioProductResponse(AbstractModel):
    r"""DeleteStudioProduct返回参数结构体

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


class DeleteTopicPolicyRequest(AbstractModel):
    r"""DeleteTopicPolicy请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        r"""Topic名称
        :rtype: str
        """
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
    r"""DeleteTopicPolicy返回参数结构体

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


class DeleteTopicRuleRequest(AbstractModel):
    r"""DeleteTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        r"""规则名
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
    r"""DeleteTopicRule返回参数结构体

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


class DescribeAISearchTaskAsyncRequest(AbstractModel):
    r"""DescribeAISearchTaskAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
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
        


class DescribeAISearchTaskAsyncResponse(AbstractModel):
    r"""DescribeAISearchTaskAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态。0-初始状态；1-正在处理；2-处理失败；3-成功
        :type Status: int
        :param _Data: 任务处理结果数据
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.AISearchInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Data = None
        self._RequestId = None

    @property
    def Status(self):
        r"""状态。0-初始状态；1-正在处理；2-处理失败；3-成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Data(self):
        r"""任务处理结果数据
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.AISearchInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Status = params.get("Status")
        if params.get("Data") is not None:
            self._Data = AISearchInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeActivateDeviceRequest(AbstractModel):
    r"""DescribeActivateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActivateDeviceResponse(AbstractModel):
    r"""DescribeActivateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备激活详情信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.ActivateDeviceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""设备激活详情信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ActivateDeviceInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ActivateDeviceInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeActivateLicenseServiceRequest(AbstractModel):
    r"""DescribeActivateLicenseService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _LicenseType: 激活码类型
        :type LicenseType: str
        """
        self._InstanceId = None
        self._LicenseType = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LicenseType(self):
        r"""激活码类型
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActivateLicenseServiceResponse(AbstractModel):
    r"""DescribeActivateLicenseService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 增值服务激活码信息
        :type Data: list of LicenseServiceNumInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""增值服务激活码信息
        :rtype: list of LicenseServiceNumInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LicenseServiceNumInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBatchProductionRequest(AbstractModel):
    r"""DescribeBatchProduction请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchProductionId(self):
        r"""量产ID
        :rtype: str
        """
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
    r"""DescribeBatchProduction返回参数结构体

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
        :param _SuccessCount: 成功数
        :type SuccessCount: int
        :param _LastFailedReason: 量产最后失败原因
        :type LastFailedReason: str
        :param _Status: 量产状态  0：任务创建，未量产；1：处理中；2：量产结束上传结果中；3：任务完成
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchCnt = None
        self._BurnMethod = None
        self._CreateTime = None
        self._DownloadUrl = None
        self._GenerationMethod = None
        self._UploadUrl = None
        self._SuccessCount = None
        self._LastFailedReason = None
        self._Status = None
        self._RequestId = None

    @property
    def BatchCnt(self):
        r"""量产数量。
        :rtype: int
        """
        return self._BatchCnt

    @BatchCnt.setter
    def BatchCnt(self, BatchCnt):
        self._BatchCnt = BatchCnt

    @property
    def BurnMethod(self):
        r"""烧录方式。
        :rtype: int
        """
        return self._BurnMethod

    @BurnMethod.setter
    def BurnMethod(self, BurnMethod):
        self._BurnMethod = BurnMethod

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DownloadUrl(self):
        r"""下载URL。
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def GenerationMethod(self):
        r"""生成方式。
        :rtype: int
        """
        return self._GenerationMethod

    @GenerationMethod.setter
    def GenerationMethod(self, GenerationMethod):
        self._GenerationMethod = GenerationMethod

    @property
    def UploadUrl(self):
        r"""上传URL。
        :rtype: str
        """
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def SuccessCount(self):
        r"""成功数
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def LastFailedReason(self):
        r"""量产最后失败原因
        :rtype: str
        """
        return self._LastFailedReason

    @LastFailedReason.setter
    def LastFailedReason(self, LastFailedReason):
        self._LastFailedReason = LastFailedReason

    @property
    def Status(self):
        r"""量产状态  0：任务创建，未量产；1：处理中；2：量产结束上传结果中；3：任务完成
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._BatchCnt = params.get("BatchCnt")
        self._BurnMethod = params.get("BurnMethod")
        self._CreateTime = params.get("CreateTime")
        self._DownloadUrl = params.get("DownloadUrl")
        self._GenerationMethod = params.get("GenerationMethod")
        self._UploadUrl = params.get("UploadUrl")
        self._SuccessCount = params.get("SuccessCount")
        self._LastFailedReason = params.get("LastFailedReason")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeBindedProductsRequest(AbstractModel):
    r"""DescribeBindedProducts请求参数结构体

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
        r"""网关产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductSource(self):
        r"""是否跨账号绑定产品
        :rtype: int
        """
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
    r"""DescribeBindedProducts返回参数结构体

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
        r"""当前分页的子产品数组
        :rtype: list of BindProductInfo
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def Total(self):
        r"""绑定的子产品总数量
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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceCallbackRequest(AbstractModel):
    r"""DescribeCloudStorageAIServiceCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品 ID
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
        


class DescribeCloudStorageAIServiceCallbackResponse(AbstractModel):
    r"""DescribeCloudStorageAIServiceCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 推送类型。http：HTTP 回调
        :type Type: str
        :param _CallbackUrl: HTTP 回调 URL
        :type CallbackUrl: str
        :param _CallbackToken: HTTP 回调鉴权 Token
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
        r"""推送类型。http：HTTP 回调
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallbackUrl(self):
        r"""HTTP 回调 URL
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def CallbackToken(self):
        r"""HTTP 回调鉴权 Token
        :rtype: str
        """
        return self._CallbackToken

    @CallbackToken.setter
    def CallbackToken(self, CallbackToken):
        self._CallbackToken = CallbackToken

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
        self._Type = params.get("Type")
        self._CallbackUrl = params.get("CallbackUrl")
        self._CallbackToken = params.get("CallbackToken")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceRequest(AbstractModel):
    r"""DescribeCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
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
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `Highlight`：视频浓缩
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def UserId(self):
        r"""用户 ID
        :rtype: str
        """
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
        


class DescribeCloudStorageAIServiceResponse(AbstractModel):
    r"""DescribeCloudStorageAIService返回参数结构体

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
        :param _PackageId: 云存 AI 套餐 ID
        :type PackageId: str
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
        self._PackageId = None
        self._RequestId = None

    @property
    def Type(self):
        r"""云存 AI 套餐类型。可能取值：

- `1`：全时套餐
- `2`：事件套餐
- `3`：低功耗套餐
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""云存 AI 套餐生效状态。可能取值：

- `0`：未开通或已过期
- `1`：生效中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        r"""云存 AI 套餐过期时间 UNIX 时间戳
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UserId(self):
        r"""用户 ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Enabled(self):
        r"""视频分析启用状态
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Config(self):
        r"""视频分析配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ROI(self):
        r"""视频分析识别区域
        :rtype: str
        """
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI

    @property
    def PackageId(self):
        r"""云存 AI 套餐 ID
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

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
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._UserId = params.get("UserId")
        self._Enabled = params.get("Enabled")
        self._Config = params.get("Config")
        self._ROI = params.get("ROI")
        self._PackageId = params.get("PackageId")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceTaskRequest(AbstractModel):
    r"""DescribeCloudStorageAIServiceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _FileURLExpireTime: 下载 URL 的过期时间。

若传入该参数，则响应中将包含所有文件的下载 URL
        :type FileURLExpireTime: int
        """
        self._TaskId = None
        self._FileURLExpireTime = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileURLExpireTime(self):
        r"""下载 URL 的过期时间。

若传入该参数，则响应中将包含所有文件的下载 URL
        :rtype: int
        """
        return self._FileURLExpireTime

    @FileURLExpireTime.setter
    def FileURLExpireTime(self, FileURLExpireTime):
        self._FileURLExpireTime = FileURLExpireTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FileURLExpireTime = params.get("FileURLExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageAIServiceTaskResponse(AbstractModel):
    r"""DescribeCloudStorageAIServiceTask返回参数结构体

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
        r"""任务信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTask`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

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
        if params.get("TaskInfo") is not None:
            self._TaskInfo = CloudStorageAIServiceTask()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageAIServiceTasksRequest(AbstractModel):
    r"""DescribeCloudStorageAIServiceTasks请求参数结构体

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
- `VideoToText`：视频语义理解
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
        :param _DeviceNames: 设备名称列表。

当需要同时查询多台设备的任务列表时传入，优先级高于参数 `DeviceName`
        :type DeviceNames: list of str
        :param _StartTime: 查询任务时间范围的起始时间（秒级 UNIX 时间戳）
        :type StartTime: int
        :param _EndTime: 查询任务时间范围的结束时间（秒级 UNIX 时间戳）
        :type EndTime: int
        :param _FileURLExpireTime: 下载 URL 的过期时间。

若传入该参数，则响应中将包含所有文件的下载 URL
        :type FileURLExpireTime: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._UserId = None
        self._ChannelId = None
        self._DeviceNames = None
        self._StartTime = None
        self._EndTime = None
        self._FileURLExpireTime = None

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Limit(self):
        r"""分页拉取数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页拉取偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        r"""任务状态。可选值：
- （不传）：查询全部状态的任务
- `1`：失败
- `2`：成功但结果为空
- `3`：成功且结果非空
- `4`：执行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserId(self):
        r"""用户 ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def DeviceNames(self):
        r"""设备名称列表。

当需要同时查询多台设备的任务列表时传入，优先级高于参数 `DeviceName`
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def StartTime(self):
        r"""查询任务时间范围的起始时间（秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询任务时间范围的结束时间（秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileURLExpireTime(self):
        r"""下载 URL 的过期时间。

若传入该参数，则响应中将包含所有文件的下载 URL
        :rtype: int
        """
        return self._FileURLExpireTime

    @FileURLExpireTime.setter
    def FileURLExpireTime(self, FileURLExpireTime):
        self._FileURLExpireTime = FileURLExpireTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        self._DeviceNames = params.get("DeviceNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._FileURLExpireTime = params.get("FileURLExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageAIServiceTasksResponse(AbstractModel):
    r"""DescribeCloudStorageAIServiceTasks返回参数结构体

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
        r"""任务列表
        :rtype: list of CloudStorageAIServiceTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Total(self):
        r"""任务数量
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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = CloudStorageAIServiceTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageDateRequest(AbstractModel):
    r"""DescribeCloudStorageDate请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
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
    r"""DescribeCloudStorageDate返回参数结构体

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
        r"""云存日期数组，["2021-01-05","2021-01-06"]
        :rtype: list of str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageEventsRequest(AbstractModel):
    r"""DescribeCloudStorageEvents请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def StartTime(self):
        r"""起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        r"""请求上下文, 用作查询游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        r"""查询数据项目的最大数量, 默认为10。假设传Size=10，返回的实际事件数量为N，则 5 <= N <= 10。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        r"""事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :rtype: int
        """
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
    r"""DescribeCloudStorageEvents返回参数结构体

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
        r"""云存事件列表
        :rtype: list of CloudStorageEvent
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Context(self):
        r"""请求上下文, 用作查询游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        r"""拉取结果是否已经结束
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Total(self):
        r"""内部结果数量，并不等同于事件总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def VideoURL(self):
        r"""视频播放URL
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

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


class DescribeCloudStorageEventsWithAITasksRequest(AbstractModel):
    r"""DescribeCloudStorageEventsWithAITasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ServiceTypes: 事件关联的视频 AI 分析服务类型（支持多选）。可选值：

- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :type ServiceTypes: list of str
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
        self._ServiceTypes = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._Size = None
        self._EventId = None
        self._UserId = None
        self._ChannelId = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceTypes(self):
        r"""事件关联的视频 AI 分析服务类型（支持多选）。可选值：

- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: list of str
        """
        return self._ServiceTypes

    @ServiceTypes.setter
    def ServiceTypes(self, ServiceTypes):
        self._ServiceTypes = ServiceTypes

    @property
    def StartTime(self):
        r"""起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        r"""请求上下文, 用作查询游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        r"""查询数据项目的最大数量, 默认为10。假设传Size=10，返回的实际事件数量为N，则 5 <= N <= 10。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        r"""事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceTypes = params.get("ServiceTypes")
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
        


class DescribeCloudStorageEventsWithAITasksResponse(AbstractModel):
    r"""DescribeCloudStorageEventsWithAITasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 云存事件列表
        :type Events: list of CloudStorageEventWithAITasks
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
        r"""云存事件列表
        :rtype: list of CloudStorageEventWithAITasks
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Context(self):
        r"""请求上下文, 用作查询游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        r"""拉取结果是否已经结束
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Total(self):
        r"""内部结果数量，并不等同于事件总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def VideoURL(self):
        r"""视频播放URL
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = CloudStorageEventWithAITasks()
                obj._deserialize(item)
                self._Events.append(obj)
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        self._Total = params.get("Total")
        self._VideoURL = params.get("VideoURL")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageMultiThumbnailRequest(AbstractModel):
    r"""DescribeCloudStorageMultiThumbnail请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def MultiThumbnail(self):
        r"""多个缩略图文件名根据 | 分割
        :rtype: str
        """
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
    r"""DescribeCloudStorageMultiThumbnail返回参数结构体

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
        r"""缩略图访问地址
        :rtype: list of ThumbnailURLInfoList
        """
        return self._ThumbnailURLInfoList

    @ThumbnailURLInfoList.setter
    def ThumbnailURLInfoList(self, ThumbnailURLInfoList):
        self._ThumbnailURLInfoList = ThumbnailURLInfoList

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
        if params.get("ThumbnailURLInfoList") is not None:
            self._ThumbnailURLInfoList = []
            for item in params.get("ThumbnailURLInfoList"):
                obj = ThumbnailURLInfoList()
                obj._deserialize(item)
                self._ThumbnailURLInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageOrderRequest(AbstractModel):
    r"""DescribeCloudStorageOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单id
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        r"""订单id
        :rtype: str
        """
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
    r"""DescribeCloudStorageOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 云存套餐开始时间
        :type StartTime: int
        :param _ExpireTime: 云存套餐过期时间
        :type ExpireTime: int
        :param _PackageId: 套餐id
        :type PackageId: str
        :param _Status: 套餐状态
0：等待生效
1: 已过期
2:生效
        :type Status: int
        :param _ChannelId: 通道id
        :type ChannelId: int
        :param _Price: 订单金额，单位为分
        :type Price: int
        :param _Amount: 支付金额，单位为分
        :type Amount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._ExpireTime = None
        self._PackageId = None
        self._Status = None
        self._ChannelId = None
        self._Price = None
        self._Amount = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""云存套餐开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""云存套餐过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PackageId(self):
        r"""套餐id
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Status(self):
        r"""套餐状态
0：等待生效
1: 已过期
2:生效
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelId(self):
        r"""通道id
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Price(self):
        r"""订单金额，单位为分
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Amount(self):
        r"""支付金额，单位为分
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

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
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._PackageId = params.get("PackageId")
        self._Status = params.get("Status")
        self._ChannelId = params.get("ChannelId")
        self._Price = params.get("Price")
        self._Amount = params.get("Amount")
        self._RequestId = params.get("RequestId")


class DescribeCloudStoragePackageConsumeDetailsRequest(AbstractModel):
    r"""DescribeCloudStoragePackageConsumeDetails请求参数结构体

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
        r"""开始日期
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""结束日期
        :rtype: str
        """
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
    r"""DescribeCloudStoragePackageConsumeDetails返回参数结构体

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


class DescribeCloudStoragePackageConsumeStatsRequest(AbstractModel):
    r"""DescribeCloudStoragePackageConsumeStats请求参数结构体

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
        r"""开始日期
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""结束日期，开始与结束日期间隔不可超过一年
        :rtype: str
        """
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
    r"""DescribeCloudStoragePackageConsumeStats返回参数结构体

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
        r"""统计列表详情
        :rtype: list of PackageConsumeStat
        """
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

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
        if params.get("Stats") is not None:
            self._Stats = []
            for item in params.get("Stats"):
                obj = PackageConsumeStat()
                obj._deserialize(item)
                self._Stats.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageRequest(AbstractModel):
    r"""DescribeCloudStorage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""云存用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID 非NVR设备不填 NVR设备必填 默认为无	
        :rtype: int
        """
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
    r"""DescribeCloudStorage返回参数结构体

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
        r"""云存开启状态，1为开启，0为未开启或已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""云存类型，1为全时云存，2为事件云存
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        r"""云存套餐过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ShiftDuration(self):
        r"""云存回看时长
        :rtype: int
        """
        return self._ShiftDuration

    @ShiftDuration.setter
    def ShiftDuration(self, ShiftDuration):
        self._ShiftDuration = ShiftDuration

    @property
    def UserId(self):
        r"""云存用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._ShiftDuration = params.get("ShiftDuration")
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageStreamDataRequest(AbstractModel):
    r"""DescribeCloudStorageStreamData请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def StartTime(self):
        r"""图片流事件开始时间
        :rtype: int
        """
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
    r"""DescribeCloudStorageStreamData返回参数结构体

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
        r"""图片流视频地址
        :rtype: str
        """
        return self._VideoStream

    @VideoStream.setter
    def VideoStream(self, VideoStream):
        self._VideoStream = VideoStream

    @property
    def AudioStream(self):
        r"""图片流音频地址
        :rtype: str
        """
        return self._AudioStream

    @AudioStream.setter
    def AudioStream(self, AudioStream):
        self._AudioStream = AudioStream

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
        self._VideoStream = params.get("VideoStream")
        self._AudioStream = params.get("AudioStream")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageThumbnailListRequest(AbstractModel):
    r"""DescribeCloudStorageThumbnailList请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ThumbnailList(self):
        r"""缩略图文件名列表
        :rtype: list of str
        """
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
    r"""DescribeCloudStorageThumbnailList返回参数结构体

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
        r"""缩略图访问地址
        :rtype: list of ThumbnailURLInfoList
        """
        return self._ThumbnailURLInfoList

    @ThumbnailURLInfoList.setter
    def ThumbnailURLInfoList(self, ThumbnailURLInfoList):
        self._ThumbnailURLInfoList = ThumbnailURLInfoList

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
        if params.get("ThumbnailURLInfoList") is not None:
            self._ThumbnailURLInfoList = []
            for item in params.get("ThumbnailURLInfoList"):
                obj = ThumbnailURLInfoList()
                obj._deserialize(item)
                self._ThumbnailURLInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageThumbnailRequest(AbstractModel):
    r"""DescribeCloudStorageThumbnail请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Thumbnail(self):
        r"""缩略图文件名
        :rtype: str
        """
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
    r"""DescribeCloudStorageThumbnail返回参数结构体

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
        r"""缩略图访问地址
        :rtype: str
        """
        return self._ThumbnailURL

    @ThumbnailURL.setter
    def ThumbnailURL(self, ThumbnailURL):
        self._ThumbnailURL = ThumbnailURL

    @property
    def ExpireTime(self):
        r"""缩略图访问地址的过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
        self._ThumbnailURL = params.get("ThumbnailURL")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageTimeRequest(AbstractModel):
    r"""DescribeCloudStorageTime请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Date(self):
        r"""云存日期，例如"2020-01-05"
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def StartTime(self):
        r"""开始时间，unix时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，unix时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
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
    r"""DescribeCloudStorageTime返回参数结构体

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
        r"""接口返回数据
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageTimeData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CloudStorageTimeData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageUsersRequest(AbstractModel):
    r"""DescribeCloudStorageUsers请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Limit(self):
        r"""分页拉取数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页拉取偏移
        :rtype: int
        """
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
    r"""DescribeCloudStorageUsers返回参数结构体

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
        r"""用户总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Users(self):
        r"""用户信息
        :rtype: list of CloudStorageUserInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = CloudStorageUserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCsReportCountDataInfoRequest(AbstractModel):
    r"""DescribeCsReportCountDataInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _StartTime: 统计开始时间戳
        :type StartTime: int
        :param _EndTime: 统计结束时间戳
        :type EndTime: int
        :param _ChannelId: 设备通道
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._StartTime = None
        self._EndTime = None
        self._ChannelId = None

    @property
    def ProductId(self):
        r"""产品id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def StartTime(self):
        r"""统计开始时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""统计结束时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ChannelId(self):
        r"""设备通道
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCsReportCountDataInfoResponse(AbstractModel):
    r"""DescribeCsReportCountDataInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云存上报统计信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.CountDataInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""云存上报统计信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CountDataInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CountDataInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceBindGatewayRequest(AbstractModel):
    r"""DescribeDeviceBindGateway请求参数结构体

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
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
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
        


class DescribeDeviceBindGatewayResponse(AbstractModel):
    r"""DescribeDeviceBindGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayProductId: 网关产品ID
        :type GatewayProductId: str
        :param _GatewayDeviceName: 网关设备名
        :type GatewayDeviceName: str
        :param _GatewayName: 网关产品名称
        :type GatewayName: str
        :param _GatewayProductOwnerName: 设备对应产品所属的主账号名称
        :type GatewayProductOwnerName: str
        :param _GatewayProductOwnerUin: 设备对应产品所属的主账号 UIN
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
        r"""网关产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        r"""网关设备名
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def GatewayName(self):
        r"""网关产品名称
        :rtype: str
        """
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def GatewayProductOwnerName(self):
        r"""设备对应产品所属的主账号名称
        :rtype: str
        """
        return self._GatewayProductOwnerName

    @GatewayProductOwnerName.setter
    def GatewayProductOwnerName(self, GatewayProductOwnerName):
        self._GatewayProductOwnerName = GatewayProductOwnerName

    @property
    def GatewayProductOwnerUin(self):
        r"""设备对应产品所属的主账号 UIN
        :rtype: str
        """
        return self._GatewayProductOwnerUin

    @GatewayProductOwnerUin.setter
    def GatewayProductOwnerUin(self, GatewayProductOwnerUin):
        self._GatewayProductOwnerUin = GatewayProductOwnerUin

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
        self._GatewayProductId = params.get("GatewayProductId")
        self._GatewayDeviceName = params.get("GatewayDeviceName")
        self._GatewayName = params.get("GatewayName")
        self._GatewayProductOwnerName = params.get("GatewayProductOwnerName")
        self._GatewayProductOwnerUin = params.get("GatewayProductOwnerUin")
        self._RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    r"""DescribeDeviceDataHistory请求参数结构体

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
        r"""区间开始时间（Unix 时间戳，毫秒级）
        :rtype: int
        """
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        r"""区间结束时间（Unix 时间戳，毫秒级）
        :rtype: int
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def FieldName(self):
        r"""属性字段名称，对应数据模板中功能属性的标识符
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Limit(self):
        r"""返回条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        r"""检索上下文
        :rtype: str
        """
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
    r"""DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FieldName: 属性字段名称，对应数据模板中功能属性的标识符
        :type FieldName: str
        :param _Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
        :type Listover: bool
        :param _Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
        :type Context: str
        :param _Results: 历史数据结果数组，返回对应时间点及取值。
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
        r"""属性字段名称，对应数据模板中功能属性的标识符
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Listover(self):
        r"""数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Context(self):
        r"""检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Results(self):
        r"""历史数据结果数组，返回对应时间点及取值。
        :rtype: list of DeviceDataHistoryItem
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
    r"""DescribeDeviceData请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def DeviceId(self):
        r"""设备ID，该字段有值将代替 ProductId/DeviceName
        :rtype: str
        """
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
    r"""DescribeDeviceData返回参数结构体

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
        r"""设备数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDeviceFirmWareRequest(AbstractModel):
    r"""DescribeDeviceFirmWare请求参数结构体

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
        r"""产品ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称。
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
        


class DescribeDeviceFirmWareResponse(AbstractModel):
    r"""DescribeDeviceFirmWare返回参数结构体

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
        r"""固件信息
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDeviceFirmwaresRequest(AbstractModel):
    r"""DescribeDeviceFirmwares请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
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
        


class DescribeDeviceFirmwaresResponse(AbstractModel):
    r"""DescribeDeviceFirmwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Firmwares: 固件信息列表
        :type Firmwares: list of DeviceFirmwareInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Firmwares = None
        self._RequestId = None

    @property
    def Firmwares(self):
        r"""固件信息列表
        :rtype: list of DeviceFirmwareInfo
        """
        return self._Firmwares

    @Firmwares.setter
    def Firmwares(self, Firmwares):
        self._Firmwares = Firmwares

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
        if params.get("Firmwares") is not None:
            self._Firmwares = []
            for item in params.get("Firmwares"):
                obj = DeviceFirmwareInfo()
                obj._deserialize(item)
                self._Firmwares.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceLocationSolveRequest(AbstractModel):
    r"""DescribeDeviceLocationSolve请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def LocationType(self):
        r"""定位解析类型，wifi或GNSSNavigation
        :rtype: str
        """
        return self._LocationType

    @LocationType.setter
    def LocationType(self, LocationType):
        self._LocationType = LocationType

    @property
    def GNSSNavigation(self):
        r"""LoRaEdge卫星导航电文
        :rtype: str
        """
        return self._GNSSNavigation

    @GNSSNavigation.setter
    def GNSSNavigation(self, GNSSNavigation):
        self._GNSSNavigation = GNSSNavigation

    @property
    def WiFiInfo(self):
        r"""wifi信息
        :rtype: list of WifiInfo
        """
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
    r"""DescribeDeviceLocationSolve返回参数结构体

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
        r"""经度
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""纬度
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def LocationType(self):
        r"""类型
        :rtype: str
        """
        return self._LocationType

    @LocationType.setter
    def LocationType(self, LocationType):
        self._LocationType = LocationType

    @property
    def Accuracy(self):
        r"""误差精度预估，单位为米
        :rtype: float
        """
        return self._Accuracy

    @Accuracy.setter
    def Accuracy(self, Accuracy):
        self._Accuracy = Accuracy

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
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._LocationType = params.get("LocationType")
        self._Accuracy = params.get("Accuracy")
        self._RequestId = params.get("RequestId")


class DescribeDevicePackagesRequest(AbstractModel):
    r"""DescribeDevicePackages请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Limit(self):
        r"""分页拉取数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页拉取偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CSUserId(self):
        r"""用户id
        :rtype: str
        """
        return self._CSUserId

    @CSUserId.setter
    def CSUserId(self, CSUserId):
        self._CSUserId = CSUserId

    @property
    def ChannelId(self):
        r"""通道id
        :rtype: int
        """
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
    r"""DescribeDevicePackages返回参数结构体

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
        r"""有效云存套餐数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Packages(self):
        r"""有效云存套餐列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PackageInfo
        """
        return self._Packages

    @Packages.setter
    def Packages(self, Packages):
        self._Packages = Packages

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Packages") is not None:
            self._Packages = []
            for item in params.get("Packages"):
                obj = PackageInfo()
                obj._deserialize(item)
                self._Packages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicePositionListRequest(AbstractModel):
    r"""DescribeDevicePositionList请求参数结构体

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
        r"""产品标识列表
        :rtype: list of str
        """
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def CoordinateType(self):
        r"""坐标类型
        :rtype: int
        """
        return self._CoordinateType

    @CoordinateType.setter
    def CoordinateType(self, CoordinateType):
        self._CoordinateType = CoordinateType

    @property
    def Offset(self):
        r"""分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的大小
        :rtype: int
        """
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
    r"""DescribeDevicePositionList返回参数结构体

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
        r"""产品设备位置信息列表
        :rtype: list of ProductDevicesPositionItem
        """
        return self._Positions

    @Positions.setter
    def Positions(self, Positions):
        self._Positions = Positions

    @property
    def Total(self):
        r"""产品设备位置信息的数目
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
        if params.get("Positions") is not None:
            self._Positions = []
            for item in params.get("Positions"):
                obj = ProductDevicesPositionItem()
                obj._deserialize(item)
                self._Positions.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    r"""DescribeDevice请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceId(self):
        r"""设备ID，该字段有值将代替 ProductId/DeviceName
        :rtype: str
        """
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
    r"""DescribeDevice返回参数结构体

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
        r"""设备信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceInfo`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

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
        if params.get("Device") is not None:
            self._Device = DeviceInfo()
            self._Device._deserialize(params.get("Device"))
        self._RequestId = params.get("RequestId")


class DescribeFenceBindListRequest(AbstractModel):
    r"""DescribeFenceBindList请求参数结构体

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
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Offset(self):
        r"""翻页偏移量，0起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大返回结果数
        :rtype: int
        """
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
    r"""DescribeFenceBindList返回参数结构体

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
        r"""围栏绑定的产品设备列表
        :rtype: list of FenceBindProductItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""围栏绑定的设备总数
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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FenceBindProductItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFenceEventListRequest(AbstractModel):
    r"""DescribeFenceEventList请求参数结构体

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
        r"""围栏告警信息的查询起始时间，Unix时间，单位为毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""围栏告警信息的查询结束时间，Unix时间，单位为毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FenceId(self):
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Offset(self):
        r"""翻页偏移量，0起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大返回结果数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductId(self):
        r"""告警对应的产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""告警对应的设备名称
        :rtype: str
        """
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
    r"""DescribeFenceEventList返回参数结构体

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
        r"""围栏告警事件列表
        :rtype: list of FenceEventItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""围栏告警事件总数
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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FenceEventItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareRequest(AbstractModel):
    r"""DescribeFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _FwType: 固件模块
        :type FwType: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FwType = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FwType(self):
        r"""固件模块
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareResponse(AbstractModel):
    r"""DescribeFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 固件版本号
        :type Version: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Name: 固件名称
        :type Name: str
        :param _Description: 固件描述
        :type Description: str
        :param _Md5sum: 固件Md5值
        :type Md5sum: str
        :param _Createtime: 固件上传的秒级时间戳
        :type Createtime: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _FwType: 固件升级模块
        :type FwType: str
        :param _UserDefined: 固件用户自定义配置信息
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
        r"""固件版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Name(self):
        r"""固件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""固件描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Md5sum(self):
        r"""固件Md5值
        :rtype: str
        """
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def Createtime(self):
        r"""固件上传的秒级时间戳
        :rtype: int
        """
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def FwType(self):
        r"""固件升级模块
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def UserDefined(self):
        r"""固件用户自定义配置信息
        :rtype: str
        """
        return self._UserDefined

    @UserDefined.setter
    def UserDefined(self, UserDefined):
        self._UserDefined = UserDefined

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
    r"""DescribeFirmwareTaskDevices请求参数结构体

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
        :param _FwType: 固件类型
        :type FwType: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._FwType = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件版本
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Filters(self):
        r"""筛选条件
        :rtype: list of SearchKeyword
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询的数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


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
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDevicesResponse(AbstractModel):
    r"""DescribeFirmwareTaskDevices返回参数结构体

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
        r"""固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Devices(self):
        r"""固件升级任务的设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceUpdateStatus
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

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
        self._Total = params.get("Total")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceUpdateStatus()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskRequest(AbstractModel):
    r"""DescribeFirmwareTask请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        r"""固件任务ID
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
    r"""DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 固件任务ID
        :type TaskId: int
        :param _Status: 固件任务状态
        :type Status: int
        :param _CreateTime: 固件任务创建时间，单位：秒
        :type CreateTime: int
        :param _Type: 固件任务升级类型
        :type Type: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
        :type UpgradeMode: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
        :type OriginalVersion: str
        :param _CreateUserId: 创建账号ID
        :type CreateUserId: int
        :param _CreatorNickName: 创建账号ID昵称
        :type CreatorNickName: str
        :param _DelayTime: 延迟时间
        :type DelayTime: int
        :param _TimeoutInterval: 超时时间
        :type TimeoutInterval: int
        :param _UpgradeMethod: 静默升级or用户确认升级
        :type UpgradeMethod: int
        :param _MaxRetryNum: 最大重试次数
        :type MaxRetryNum: int
        :param _FwType: 固件类型
        :type FwType: str
        :param _RetryInterval: 重试间隔时间单位min
        :type RetryInterval: int
        :param _OverrideMode: 是否覆盖任务
        :type OverrideMode: int
        :param _TaskUserDefine: 用户自定义消息
        :type TaskUserDefine: str
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
        self._DelayTime = None
        self._TimeoutInterval = None
        self._UpgradeMethod = None
        self._MaxRetryNum = None
        self._FwType = None
        self._RetryInterval = None
        self._OverrideMode = None
        self._TaskUserDefine = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""固件任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""固件任务状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""固件任务创建时间，单位：秒
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Type(self):
        r"""固件任务升级类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def UpgradeMode(self):
        r"""固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
        :rtype: str
        """
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OriginalVersion(self):
        r"""原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
        :rtype: str
        """
        return self._OriginalVersion

    @OriginalVersion.setter
    def OriginalVersion(self, OriginalVersion):
        self._OriginalVersion = OriginalVersion

    @property
    def CreateUserId(self):
        r"""创建账号ID
        :rtype: int
        """
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        r"""创建账号ID昵称
        :rtype: str
        """
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def DelayTime(self):
        r"""延迟时间
        :rtype: int
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def TimeoutInterval(self):
        r"""超时时间
        :rtype: int
        """
        return self._TimeoutInterval

    @TimeoutInterval.setter
    def TimeoutInterval(self, TimeoutInterval):
        self._TimeoutInterval = TimeoutInterval

    @property
    def UpgradeMethod(self):
        r"""静默升级or用户确认升级
        :rtype: int
        """
        return self._UpgradeMethod

    @UpgradeMethod.setter
    def UpgradeMethod(self, UpgradeMethod):
        self._UpgradeMethod = UpgradeMethod

    @property
    def MaxRetryNum(self):
        r"""最大重试次数
        :rtype: int
        """
        return self._MaxRetryNum

    @MaxRetryNum.setter
    def MaxRetryNum(self, MaxRetryNum):
        self._MaxRetryNum = MaxRetryNum

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def RetryInterval(self):
        r"""重试间隔时间单位min
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def OverrideMode(self):
        r"""是否覆盖任务
        :rtype: int
        """
        return self._OverrideMode

    @OverrideMode.setter
    def OverrideMode(self, OverrideMode):
        self._OverrideMode = OverrideMode

    @property
    def TaskUserDefine(self):
        r"""用户自定义消息
        :rtype: str
        """
        return self._TaskUserDefine

    @TaskUserDefine.setter
    def TaskUserDefine(self, TaskUserDefine):
        self._TaskUserDefine = TaskUserDefine

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
        self._DelayTime = params.get("DelayTime")
        self._TimeoutInterval = params.get("TimeoutInterval")
        self._UpgradeMethod = params.get("UpgradeMethod")
        self._MaxRetryNum = params.get("MaxRetryNum")
        self._FwType = params.get("FwType")
        self._RetryInterval = params.get("RetryInterval")
        self._OverrideMode = params.get("OverrideMode")
        self._TaskUserDefine = params.get("TaskUserDefine")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTasksRequest(AbstractModel):
    r"""DescribeFirmwareTasks请求参数结构体

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
        :param _FwType: 固件类型
        :type FwType: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._FwType = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Offset(self):
        r"""查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回查询结果条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""搜索过滤条件
        :rtype: list of SearchKeyword
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


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
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTasksResponse(AbstractModel):
    r"""DescribeFirmwareTasks返回参数结构体

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
        r"""固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FirmwareTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def Total(self):
        r"""固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。
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
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareUpdateStatusRequest(AbstractModel):
    r"""DescribeFirmwareUpdateStatus请求参数结构体

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
        r"""产品 ID。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名。
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
        


class DescribeFirmwareUpdateStatusResponse(AbstractModel):
    r"""DescribeFirmwareUpdateStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriVersion: 升级任务源版本。
        :type OriVersion: str
        :param _DstVersion: 升级任务目标版本。
        :type DstVersion: str
        :param _Status: 升级状态：- 0：设备离线。- 1：待处理。- 2：消息下发成功。- 3：下载中。- 4：烧录中。- 5：失败。- 6：升级完成。- 7：正在处理中。- 8：等待用户确认。- 10：升级超时。- 20：下载完成。
        :type Status: int
        :param _Percent: 进度
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
        r"""升级任务源版本。
        :rtype: str
        """
        return self._OriVersion

    @OriVersion.setter
    def OriVersion(self, OriVersion):
        self._OriVersion = OriVersion

    @property
    def DstVersion(self):
        r"""升级任务目标版本。
        :rtype: str
        """
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def Status(self):
        r"""升级状态：- 0：设备离线。- 1：待处理。- 2：消息下发成功。- 3：下载中。- 4：烧录中。- 5：失败。- 6：升级完成。- 7：正在处理中。- 8：等待用户确认。- 10：升级超时。- 20：下载完成。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        r"""进度
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

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
        self._OriVersion = params.get("OriVersion")
        self._DstVersion = params.get("DstVersion")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._RequestId = params.get("RequestId")


class DescribeFreeCloudStorageNumRequest(AbstractModel):
    r"""DescribeFreeCloudStorageNum请求参数结构体

    """


class DescribeFreeCloudStorageNumResponse(AbstractModel):
    r"""DescribeFreeCloudStorageNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageInfos: 套餐包信息
        :type PackageInfos: list of CloudStoragePackageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackageInfos = None
        self._RequestId = None

    @property
    def PackageInfos(self):
        r"""套餐包信息
        :rtype: list of CloudStoragePackageInfo
        """
        return self._PackageInfos

    @PackageInfos.setter
    def PackageInfos(self, PackageInfos):
        self._PackageInfos = PackageInfos

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
        if params.get("PackageInfos") is not None:
            self._PackageInfos = []
            for item in params.get("PackageInfos"):
                obj = CloudStoragePackageInfo()
                obj._deserialize(item)
                self._PackageInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayBindDevicesRequest(AbstractModel):
    r"""DescribeGatewayBindDevices请求参数结构体

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
        r"""网关设备的产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        r"""网关设备的设备名
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        r"""子产品的ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        r"""分页的偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的页大小
        :rtype: int
        """
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
    r"""DescribeGatewayBindDevices返回参数结构体

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
        r"""子设备信息。
        :rtype: list of BindDeviceInfo
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Total(self):
        r"""子设备总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ProductName(self):
        r"""子设备所属的产品名。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

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
    r"""DescribeGatewaySubDeviceList请求参数结构体

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
        r"""网关产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        r"""网关设备名称
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def Offset(self):
        r"""分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的大小
        :rtype: int
        """
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
    r"""DescribeGatewaySubDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 设备的总数
        :type Total: int
        :param _DeviceList: 设备列表
        :type DeviceList: list of FamilySubDevice
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""设备的总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: list of FamilySubDevice
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

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
        self._Total = params.get("Total")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = FamilySubDevice()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewaySubProductsRequest(AbstractModel):
    r"""DescribeGatewaySubProducts请求参数结构体

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
        r"""网关产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def Offset(self):
        r"""分页的偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductSource(self):
        r"""是否跨账号产品
        :rtype: int
        """
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
    r"""DescribeGatewaySubProducts返回参数结构体

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
        r"""当前分页的可绑定或解绑的产品信息。
        :rtype: list of BindProductInfo
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def Total(self):
        r"""可绑定或解绑的产品总数
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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    r"""DescribeInstance请求参数结构体

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
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Include(self):
        r"""附加查询返回包含字段值，不传返回0，有效值 ProductNum、ProjectNum、UsedDeviceNum、TotalDevice、ActivateDevice
        :rtype: list of str
        """
        return self._Include

    @Include.setter
    def Include(self, Include):
        self._Include = Include

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        r"""产品ID，-1 代表全部产品
        :rtype: str
        """
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
    r"""DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 实例信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.InstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""实例信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.InstanceDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = InstanceDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeLoRaFrequencyRequest(AbstractModel):
    r"""DescribeLoRaFrequency请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FreqId: 频点唯一ID
        :type FreqId: str
        """
        self._FreqId = None

    @property
    def FreqId(self):
        r"""频点唯一ID
        :rtype: str
        """
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
    r"""DescribeLoRaFrequency返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回详情项
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回详情项
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = LoRaFrequencyEntry()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    r"""DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品ID
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
        


class DescribeModelDefinitionResponse(AbstractModel):
    r"""DescribeModelDefinition返回参数结构体

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
        r"""产品数据模板
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProductModelDefinition`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

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
        if params.get("Model") is not None:
            self._Model = ProductModelDefinition()
            self._Model._deserialize(params.get("Model"))
        self._RequestId = params.get("RequestId")


class DescribeP2PRouteRequest(AbstractModel):
    r"""DescribeP2PRoute请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
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
        


class DescribeP2PRouteResponse(AbstractModel):
    r"""DescribeP2PRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteId: 当前p2p线路
        :type RouteId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RouteId = None
        self._RequestId = None

    @property
    def RouteId(self):
        r"""当前p2p线路
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

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
        self._RouteId = params.get("RouteId")
        self._RequestId = params.get("RequestId")


class DescribePackageConsumeTaskRequest(AbstractModel):
    r"""DescribePackageConsumeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务id
        :rtype: int
        """
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
    r"""DescribePackageConsumeTask返回参数结构体

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
        r"""文件下载的url，文件详情是套餐包消耗详情
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

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
        self._URL = params.get("URL")
        self._RequestId = params.get("RequestId")


class DescribePackageConsumeTasksRequest(AbstractModel):
    r"""DescribePackageConsumeTasks请求参数结构体

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
        r"""分页单页量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页的偏移量，第一页为0
        :rtype: int
        """
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
    r"""DescribePackageConsumeTasks返回参数结构体

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
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""任务列表
        :rtype: list of PackageConsumeTask
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PackageConsumeTask()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePositionFenceListRequest(AbstractModel):
    r"""DescribePositionFenceList请求参数结构体

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
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Offset(self):
        r"""翻页偏移量，0起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大返回结果数
        :rtype: int
        """
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
    r"""DescribePositionFenceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 围栏列表
        :type List: list of PositionFenceInfo
        :param _Total: 围栏数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        r"""围栏列表
        :rtype: list of PositionFenceInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""围栏数量
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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PositionFenceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProductCloudStorageAIServiceRequest(AbstractModel):
    r"""DescribeProductCloudStorageAIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品 ID
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
        


class DescribeProductCloudStorageAIServiceResponse(AbstractModel):
    r"""DescribeProductCloudStorageAIService返回参数结构体

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
        r"""开通状态
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Available(self):
        r"""当前账号是否可开通
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

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
        self._Enabled = params.get("Enabled")
        self._Available = params.get("Available")
        self._RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    r"""DescribeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
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
    r"""DescribeProject返回参数结构体

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
        r"""返回信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntryEx`
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

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
        if params.get("Project") is not None:
            self._Project = ProjectEntryEx()
            self._Project._deserialize(params.get("Project"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceFenceEventListRequest(AbstractModel):
    r"""DescribeSpaceFenceEventList请求参数结构体

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
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def StartTime(self):
        r"""围栏告警信息的查询起始时间，Unix时间，单位为毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""围栏告警信息的查询结束时间，Unix时间，单位为毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""翻页偏移量，0起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大返回结果数
        :rtype: int
        """
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
    r"""DescribeSpaceFenceEventList返回参数结构体

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
        r"""围栏告警事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FenceEventItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""围栏告警事件总数
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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FenceEventItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeStudioProductRequest(AbstractModel):
    r"""DescribeStudioProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品ID
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
        


class DescribeStudioProductResponse(AbstractModel):
    r"""DescribeStudioProduct返回参数结构体

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
        r"""产品详情
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

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
        if params.get("Product") is not None:
            self._Product = ProductEntry()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class DescribeSubscribedTopicPolicyRequest(AbstractModel):
    r"""DescribeSubscribedTopicPolicy请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
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
        


class DescribeSubscribedTopicPolicyResponse(AbstractModel):
    r"""DescribeSubscribedTopicPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: 已订阅Topic信息
        :type Topics: list of SubscribedTopicItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topics = None
        self._RequestId = None

    @property
    def Topics(self):
        r"""已订阅Topic信息
        :rtype: list of SubscribedTopicItem
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = SubscribedTopicItem()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTWeSeeConfigRequest(AbstractModel):
    r"""DescribeTWeSeeConfig请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
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
        


class DescribeTWeSeeConfigResponse(AbstractModel):
    r"""DescribeTWeSeeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnableSummary: 是否开启视频摘要
        :type EnableSummary: bool
        :param _EnableSearch: 是否开启视频搜索
        :type EnableSearch: bool
        :param _Config: 配置参数
        :type Config: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnableSummary = None
        self._EnableSearch = None
        self._Config = None
        self._RequestId = None

    @property
    def EnableSummary(self):
        r"""是否开启视频摘要
        :rtype: bool
        """
        return self._EnableSummary

    @EnableSummary.setter
    def EnableSummary(self, EnableSummary):
        self._EnableSummary = EnableSummary

    @property
    def EnableSearch(self):
        r"""是否开启视频搜索
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch

    @property
    def Config(self):
        r"""配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

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
        self._EnableSummary = params.get("EnableSummary")
        self._EnableSearch = params.get("EnableSearch")
        self._Config = params.get("Config")
        self._RequestId = params.get("RequestId")


class DescribeTWeSeeRecognitionTaskRequest(AbstractModel):
    r"""DescribeTWeSeeRecognitionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _FileURLExpireTime: 下载 URL 的过期时间。

若传入该参数，则响应中将包含所有文件的下载 URL
        :type FileURLExpireTime: int
        """
        self._TaskId = None
        self._FileURLExpireTime = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileURLExpireTime(self):
        r"""下载 URL 的过期时间。

若传入该参数，则响应中将包含所有文件的下载 URL
        :rtype: int
        """
        return self._FileURLExpireTime

    @FileURLExpireTime.setter
    def FileURLExpireTime(self, FileURLExpireTime):
        self._FileURLExpireTime = FileURLExpireTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FileURLExpireTime = params.get("FileURLExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTWeSeeRecognitionTaskResponse(AbstractModel):
    r"""DescribeTWeSeeRecognitionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfo: 任务信息
        :type TaskInfo: :class:`tencentcloud.iotexplorer.v20190423.models.VisionRecognitionTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfo = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        r"""任务信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionRecognitionTask`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

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
        if params.get("TaskInfo") is not None:
            self._TaskInfo = VisionRecognitionTask()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTWeTalkProductConfigRequest(AbstractModel):
    r"""DescribeTWeTalkProductConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        """
        self._ProductId = None
        self._TargetLanguage = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TargetLanguage = params.get("TargetLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTWeTalkProductConfigResponse(AbstractModel):
    r"""DescribeTWeTalkProductConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.TalkProductConfigInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""配置信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkProductConfigInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TalkProductConfigInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTWeTalkProductConfigV2Request(AbstractModel):
    r"""DescribeTWeTalkProductConfigV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        :param _IncludeCredentials: 是否脱敏
        :type IncludeCredentials: bool
        """
        self._ProductId = None
        self._DeviceName = None
        self._TargetLanguage = None
        self._IncludeCredentials = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def IncludeCredentials(self):
        r"""是否脱敏
        :rtype: bool
        """
        return self._IncludeCredentials

    @IncludeCredentials.setter
    def IncludeCredentials(self, IncludeCredentials):
        self._IncludeCredentials = IncludeCredentials


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._TargetLanguage = params.get("TargetLanguage")
        self._IncludeCredentials = params.get("IncludeCredentials")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTWeTalkProductConfigV2Response(AbstractModel):
    r"""DescribeTWeTalkProductConfigV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置信息
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.TalkProductConfigV2Info`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""配置信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkProductConfigV2Info`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TalkProductConfigV2Info()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTopicPolicyRequest(AbstractModel):
    r"""DescribeTopicPolicy请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        r"""Topic名字
        :rtype: str
        """
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
    r"""DescribeTopicPolicy返回参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        r"""Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Privilege(self):
        r"""Topic权限
        :rtype: int
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

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
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        self._Privilege = params.get("Privilege")
        self._RequestId = params.get("RequestId")


class DescribeTopicRuleRequest(AbstractModel):
    r"""DescribeTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称。
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        r"""规则名称。
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
        


class DescribeTopicRuleResponse(AbstractModel):
    r"""DescribeTopicRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则描述。
        :type Rule: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRule`
        :param _CamTag: 规则绑定的标签
        :type CamTag: list of CamTag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._CamTag = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则描述。
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def CamTag(self):
        r"""规则绑定的标签
        :rtype: list of CamTag
        """
        return self._CamTag

    @CamTag.setter
    def CamTag(self, CamTag):
        self._CamTag = CamTag

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


class DescribeUnbindedDevicesRequest(AbstractModel):
    r"""DescribeUnbindedDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页的页大小
        :type Limit: int
        """
        self._ProductId = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的页大小
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
        


class DescribeUnbindedDevicesResponse(AbstractModel):
    r"""DescribeUnbindedDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UnbindedDevices: 未绑定的设备列表
        :type UnbindedDevices: list of BindDeviceInfo
        :param _Total: 设备的总数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UnbindedDevices = None
        self._Total = None
        self._RequestId = None

    @property
    def UnbindedDevices(self):
        r"""未绑定的设备列表
        :rtype: list of BindDeviceInfo
        """
        return self._UnbindedDevices

    @UnbindedDevices.setter
    def UnbindedDevices(self, UnbindedDevices):
        self._UnbindedDevices = UnbindedDevices

    @property
    def Total(self):
        r"""设备的总数量
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
        if params.get("UnbindedDevices") is not None:
            self._UnbindedDevices = []
            for item in params.get("UnbindedDevices"):
                obj = BindDeviceInfo()
                obj._deserialize(item)
                self._UnbindedDevices.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeVideoLicenseRequest(AbstractModel):
    r"""DescribeVideoLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoLicenseResponse(AbstractModel):
    r"""DescribeVideoLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 视频激活码分类概览
        :type License: list of VideoLicenseEntity
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._License = None
        self._RequestId = None

    @property
    def License(self):
        r"""视频激活码分类概览
        :rtype: list of VideoLicenseEntity
        """
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

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
        if params.get("License") is not None:
            self._License = []
            for item in params.get("License"):
                obj = VideoLicenseEntity()
                obj._deserialize(item)
                self._License.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceActivationDetail(AbstractModel):
    r"""设备激活详情信息

    """

    def __init__(self):
        r"""
        :param _TotalDeviceNum: 可注册设备数
        :type TotalDeviceNum: int
        :param _UsedDeviceNum: 已注册设备数
        :type UsedDeviceNum: int
        :param _TotalNormalLicense: 设备授权数
        :type TotalNormalLicense: int
        :param _UsedNormalLicense: 已使用设备授权数
        :type UsedNormalLicense: int
        :param _TotalBluetoothLicense: 蓝牙授权数
        :type TotalBluetoothLicense: int
        :param _UsedBluetoothLicense: 已使用蓝牙授权数
        :type UsedBluetoothLicense: int
        :param _TotalFreeLicense: 可免费注册设备数
        :type TotalFreeLicense: int
        :param _UsedFreeLicense: 已使用注册设备数
        :type UsedFreeLicense: int
        """
        self._TotalDeviceNum = None
        self._UsedDeviceNum = None
        self._TotalNormalLicense = None
        self._UsedNormalLicense = None
        self._TotalBluetoothLicense = None
        self._UsedBluetoothLicense = None
        self._TotalFreeLicense = None
        self._UsedFreeLicense = None

    @property
    def TotalDeviceNum(self):
        r"""可注册设备数
        :rtype: int
        """
        return self._TotalDeviceNum

    @TotalDeviceNum.setter
    def TotalDeviceNum(self, TotalDeviceNum):
        self._TotalDeviceNum = TotalDeviceNum

    @property
    def UsedDeviceNum(self):
        r"""已注册设备数
        :rtype: int
        """
        return self._UsedDeviceNum

    @UsedDeviceNum.setter
    def UsedDeviceNum(self, UsedDeviceNum):
        self._UsedDeviceNum = UsedDeviceNum

    @property
    def TotalNormalLicense(self):
        r"""设备授权数
        :rtype: int
        """
        return self._TotalNormalLicense

    @TotalNormalLicense.setter
    def TotalNormalLicense(self, TotalNormalLicense):
        self._TotalNormalLicense = TotalNormalLicense

    @property
    def UsedNormalLicense(self):
        r"""已使用设备授权数
        :rtype: int
        """
        return self._UsedNormalLicense

    @UsedNormalLicense.setter
    def UsedNormalLicense(self, UsedNormalLicense):
        self._UsedNormalLicense = UsedNormalLicense

    @property
    def TotalBluetoothLicense(self):
        r"""蓝牙授权数
        :rtype: int
        """
        return self._TotalBluetoothLicense

    @TotalBluetoothLicense.setter
    def TotalBluetoothLicense(self, TotalBluetoothLicense):
        self._TotalBluetoothLicense = TotalBluetoothLicense

    @property
    def UsedBluetoothLicense(self):
        r"""已使用蓝牙授权数
        :rtype: int
        """
        return self._UsedBluetoothLicense

    @UsedBluetoothLicense.setter
    def UsedBluetoothLicense(self, UsedBluetoothLicense):
        self._UsedBluetoothLicense = UsedBluetoothLicense

    @property
    def TotalFreeLicense(self):
        r"""可免费注册设备数
        :rtype: int
        """
        return self._TotalFreeLicense

    @TotalFreeLicense.setter
    def TotalFreeLicense(self, TotalFreeLicense):
        self._TotalFreeLicense = TotalFreeLicense

    @property
    def UsedFreeLicense(self):
        r"""已使用注册设备数
        :rtype: int
        """
        return self._UsedFreeLicense

    @UsedFreeLicense.setter
    def UsedFreeLicense(self, UsedFreeLicense):
        self._UsedFreeLicense = UsedFreeLicense


    def _deserialize(self, params):
        self._TotalDeviceNum = params.get("TotalDeviceNum")
        self._UsedDeviceNum = params.get("UsedDeviceNum")
        self._TotalNormalLicense = params.get("TotalNormalLicense")
        self._UsedNormalLicense = params.get("UsedNormalLicense")
        self._TotalBluetoothLicense = params.get("TotalBluetoothLicense")
        self._UsedBluetoothLicense = params.get("UsedBluetoothLicense")
        self._TotalFreeLicense = params.get("TotalFreeLicense")
        self._UsedFreeLicense = params.get("UsedFreeLicense")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceActiveResult(AbstractModel):
    r"""设备激活结果数据

    """

    def __init__(self):
        r"""
        :param _ModelId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _Sn: SN信息
        :type Sn: str
        :param _ErrCode: 设备激活状态，0：激活成功；50011：系统错误；50012：产品不存在；50013：设备不存在；50014：产品无权限；50015：不是音视频产品；50016：SN格式错误；50017：激活码类型错误；50018：激活次数限频；50019：激活码不足；50020：SN已暂停；
        :type ErrCode: int
        :param _ExpireTime: 过期时间
        :type ExpireTime: int
        """
        self._ModelId = None
        self._Sn = None
        self._ErrCode = None
        self._ExpireTime = None

    @property
    def ModelId(self):
        warnings.warn("parameter `ModelId` is deprecated", DeprecationWarning) 

        r"""模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        warnings.warn("parameter `ModelId` is deprecated", DeprecationWarning) 

        self._ModelId = ModelId

    @property
    def Sn(self):
        r"""SN信息
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ErrCode(self):
        r"""设备激活状态，0：激活成功；50011：系统错误；50012：产品不存在；50013：设备不存在；50014：产品无权限；50015：不是音视频产品；50016：SN格式错误；50017：激活码类型错误；50018：激活次数限频；50019：激活码不足；50020：SN已暂停；
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ExpireTime(self):
        r"""过期时间
        :rtype: int
        """
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
    r"""DeviceData

    """

    def __init__(self):
        r"""
        :param _DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数。
        :type DeviceCert: str
        :param _DeviceName: 设备名称。
        :type DeviceName: str
        :param _DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数。
        :type DevicePrivateKey: str
        :param _DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数。
        :type DevicePsk: str
        """
        self._DeviceCert = None
        self._DeviceName = None
        self._DevicePrivateKey = None
        self._DevicePsk = None

    @property
    def DeviceCert(self):
        r"""设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数。
        :rtype: str
        """
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DeviceName(self):
        r"""设备名称。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevicePrivateKey(self):
        r"""设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数。
        :rtype: str
        """
        return self._DevicePrivateKey

    @DevicePrivateKey.setter
    def DevicePrivateKey(self, DevicePrivateKey):
        self._DevicePrivateKey = DevicePrivateKey

    @property
    def DevicePsk(self):
        r"""对称加密密钥，base64编码。采用对称加密时返回该参数。
        :rtype: str
        """
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
    r"""设备历史数据结构

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
        r"""时间点，毫秒时间戳
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        r"""字段取值
        :rtype: str
        """
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
    r"""设备固件信息

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
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Version(self):
        r"""固件版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UpdateTime(self):
        r"""最后更新时间
        :rtype: int
        """
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
    r"""设备详细信息

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
        :type FirstOnlineTime: int
        :param _LoginTime: 最后一次上线时间
        :type LoginTime: int
        :param _CreateTime: 设备创建时间
        :type CreateTime: int
        :param _Version: 设备固件版本
        :type Version: str
        :param _DeviceCert: 设备证书
        :type DeviceCert: str
        :param _LogLevel: 日志级别
        :type LogLevel: int
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
        :param _CreateUserId: 创建人Id
        :type CreateUserId: int
        :param _CreatorNickName: 创建人昵称
        :type CreatorNickName: str
        :param _EnableState: 启用/禁用状态
        :type EnableState: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _DeviceType: 设备类型（设备、子设备、网关）
        :type DeviceType: str
        :param _IsLora: 是否是 lora 设备
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
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Status(self):
        r"""0: 离线, 1: 在线, 2: 获取失败, 3 未激活
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DevicePsk(self):
        r"""设备密钥，密钥加密的设备返回
        :rtype: str
        """
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def FirstOnlineTime(self):
        r"""首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LoginTime(self):
        r"""最后一次上线时间
        :rtype: int
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def CreateTime(self):
        r"""设备创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Version(self):
        r"""设备固件版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def DeviceCert(self):
        r"""设备证书
        :rtype: str
        """
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def LogLevel(self):
        r"""日志级别
        :rtype: int
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def DevAddr(self):
        r"""LoRaWAN 设备地址
        :rtype: str
        """
        return self._DevAddr

    @DevAddr.setter
    def DevAddr(self, DevAddr):
        self._DevAddr = DevAddr

    @property
    def AppKey(self):
        r"""LoRaWAN 应用密钥
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def DevEUI(self):
        r"""LoRaWAN 设备唯一标识
        :rtype: str
        """
        return self._DevEUI

    @DevEUI.setter
    def DevEUI(self, DevEUI):
        self._DevEUI = DevEUI

    @property
    def AppSKey(self):
        r"""LoRaWAN 应用会话密钥
        :rtype: str
        """
        return self._AppSKey

    @AppSKey.setter
    def AppSKey(self, AppSKey):
        self._AppSKey = AppSKey

    @property
    def NwkSKey(self):
        r"""LoRaWAN 网络会话密钥
        :rtype: str
        """
        return self._NwkSKey

    @NwkSKey.setter
    def NwkSKey(self, NwkSKey):
        self._NwkSKey = NwkSKey

    @property
    def CreateUserId(self):
        r"""创建人Id
        :rtype: int
        """
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        r"""创建人昵称
        :rtype: str
        """
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def EnableState(self):
        r"""启用/禁用状态
        :rtype: int
        """
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def DeviceType(self):
        r"""设备类型（设备、子设备、网关）
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def IsLora(self):
        r"""是否是 lora 设备
        :rtype: bool
        """
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
    r"""设备位置详情

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
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def CreateTime(self):
        r"""位置信息时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Longitude(self):
        r"""设备经度信息
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""设备纬度信息
        :rtype: float
        """
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
    r"""设备签名

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
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceSignature(self):
        r"""设备签名
        :rtype: str
        """
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
        


class DeviceUpdateStatus(AbstractModel):
    r"""设备固件更新状态

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
        :param _FwType: 固件类型
        :type FwType: str
        :param _RetryNum: 重试次数
        :type RetryNum: int
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
        self._FwType = None
        self._RetryNum = None

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LastProcessTime(self):
        r"""最后处理时间
        :rtype: int
        """
        return self._LastProcessTime

    @LastProcessTime.setter
    def LastProcessTime(self, LastProcessTime):
        self._LastProcessTime = LastProcessTime

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        r"""错误消息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Retcode(self):
        r"""返回码
        :rtype: int
        """
        return self._Retcode

    @Retcode.setter
    def Retcode(self, Retcode):
        self._Retcode = Retcode

    @property
    def DstVersion(self):
        r"""目标更新版本
        :rtype: str
        """
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def Percent(self):
        r"""下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def OriVersion(self):
        r"""原版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriVersion

    @OriVersion.setter
    def OriVersion(self, OriVersion):
        self._OriVersion = OriVersion

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def RetryNum(self):
        r"""重试次数
        :rtype: int
        """
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


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
        self._FwType = params.get("FwType")
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUser(AbstractModel):
    r"""设备的用户

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _Role: 用户角色 1所有者，0：其他分享者
        :type Role: int
        :param _FamilyId: 家庭ID，所有者带该参数
        :type FamilyId: str
        :param _FamilyName: 家庭名称，所有者带该参数
        :type FamilyName: str
        """
        self._UserId = None
        self._Role = None
        self._FamilyId = None
        self._FamilyName = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        r"""用户角色 1所有者，0：其他分享者
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def FamilyId(self):
        r"""家庭ID，所有者带该参数
        :rtype: str
        """
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def FamilyName(self):
        r"""家庭名称，所有者带该参数
        :rtype: str
        """
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
    r"""ProductId -> DeviceName

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
        r"""产品id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
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
        


class DiarySHLConfig(AbstractModel):
    r"""Diary Simple Highlight 配置

    """

    def __init__(self):
        r"""
        :param _StartOffset: 每个视频偏移时长，单位秒
        :type StartOffset: int
        :param _PlaySpeed: 视频浓缩倍数，支持1,2,4之间
        :type PlaySpeed: int
        :param _MiniExtract: 单个视频最小提取时长，单位秒
        :type MiniExtract: int
        :param _OutDuration: 每天最终输出视频时长，单位秒
注：免费版固定10s
        :type OutDuration: int
        """
        self._StartOffset = None
        self._PlaySpeed = None
        self._MiniExtract = None
        self._OutDuration = None

    @property
    def StartOffset(self):
        r"""每个视频偏移时长，单位秒
        :rtype: int
        """
        return self._StartOffset

    @StartOffset.setter
    def StartOffset(self, StartOffset):
        self._StartOffset = StartOffset

    @property
    def PlaySpeed(self):
        r"""视频浓缩倍数，支持1,2,4之间
        :rtype: int
        """
        return self._PlaySpeed

    @PlaySpeed.setter
    def PlaySpeed(self, PlaySpeed):
        self._PlaySpeed = PlaySpeed

    @property
    def MiniExtract(self):
        r"""单个视频最小提取时长，单位秒
        :rtype: int
        """
        return self._MiniExtract

    @MiniExtract.setter
    def MiniExtract(self, MiniExtract):
        self._MiniExtract = MiniExtract

    @property
    def OutDuration(self):
        r"""每天最终输出视频时长，单位秒
注：免费版固定10s
        :rtype: int
        """
        return self._OutDuration

    @OutDuration.setter
    def OutDuration(self, OutDuration):
        self._OutDuration = OutDuration


    def _deserialize(self, params):
        self._StartOffset = params.get("StartOffset")
        self._PlaySpeed = params.get("PlaySpeed")
        self._MiniExtract = params.get("MiniExtract")
        self._OutDuration = params.get("OutDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectBindDeviceInFamilyRequest(AbstractModel):
    r"""DirectBindDeviceInFamily请求参数结构体

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
        r"""小程序appid
        :rtype: str
        """
        return self._IotAppID

    @IotAppID.setter
    def IotAppID(self, IotAppID):
        self._IotAppID = IotAppID

    @property
    def UserID(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def FamilyId(self):
        r"""家庭ID
        :rtype: str
        """
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: str
        """
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
    r"""DirectBindDeviceInFamily返回参数结构体

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
        r"""返回设备信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.AppDeviceInfo`
        """
        return self._AppDeviceInfo

    @AppDeviceInfo.setter
    def AppDeviceInfo(self, AppDeviceInfo):
        self._AppDeviceInfo = AppDeviceInfo

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
        if params.get("AppDeviceInfo") is not None:
            self._AppDeviceInfo = AppDeviceInfo()
            self._AppDeviceInfo._deserialize(params.get("AppDeviceInfo"))
        self._RequestId = params.get("RequestId")


class DisableTopicRuleRequest(AbstractModel):
    r"""DisableTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        r"""规则名称
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
    r"""DisableTopicRule返回参数结构体

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


class DismissRoomByStrRoomIdFromTRTCRequest(AbstractModel):
    r"""DismissRoomByStrRoomIdFromTRTC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间id
        :type RoomId: str
        """
        self._RoomId = None

    @property
    def RoomId(self):
        r"""房间id
        :rtype: str
        """
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
    r"""DismissRoomByStrRoomIdFromTRTC返回参数结构体

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


class EnableTopicRuleRequest(AbstractModel):
    r"""EnableTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        r"""规则名称
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
    r"""EnableTopicRule返回参数结构体

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


class EventHistoryItem(AbstractModel):
    r"""设备事件的搜索结果项

    """

    def __init__(self):
        r"""
        :param _TimeStamp: 事件的时间戳
        :type TimeStamp: int
        :param _ProductId: 事件的产品ID
        :type ProductId: str
        :param _DeviceName: 事件的设备名称
        :type DeviceName: str
        :param _EventId: 事件的标识符ID
        :type EventId: str
        :param _Type: 事件的类型
        :type Type: str
        :param _Data: 事件的数据
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
        r"""事件的时间戳
        :rtype: int
        """
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

    @property
    def ProductId(self):
        r"""事件的产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""事件的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EventId(self):
        r"""事件的标识符ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Type(self):
        r"""事件的类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        r"""事件的数据
        :rtype: str
        """
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
    r"""子设备详情

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
        :type AliasName: str
        :param _FamilyId: 设备绑定的家庭ID
        :type FamilyId: str
        :param _RoomId: 设备所在的房间ID，默认"0"
        :type RoomId: str
        :param _IconUrl: 图标
        :type IconUrl: str
        :param _IconUrlGrid: grid图标
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
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def AliasName(self):
        r"""设备别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def FamilyId(self):
        r"""设备绑定的家庭ID
        :rtype: str
        """
        return self._FamilyId

    @FamilyId.setter
    def FamilyId(self, FamilyId):
        self._FamilyId = FamilyId

    @property
    def RoomId(self):
        r"""设备所在的房间ID，默认"0"
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def IconUrl(self):
        r"""图标
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def IconUrlGrid(self):
        r"""grid图标
        :rtype: str
        """
        return self._IconUrlGrid

    @IconUrlGrid.setter
    def IconUrlGrid(self, IconUrlGrid):
        self._IconUrlGrid = IconUrlGrid

    @property
    def CreateTime(self):
        r"""设备绑定时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""设备更新时间戳
        :rtype: int
        """
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
    r"""围栏告警位置点

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
        r"""围栏告警时间
        :rtype: int
        """
        return self._AlarmTime

    @AlarmTime.setter
    def AlarmTime(self, AlarmTime):
        self._AlarmTime = AlarmTime

    @property
    def Longitude(self):
        r"""围栏告警位置的经度
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""围栏告警位置的纬度
        :rtype: float
        """
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
    r"""围栏绑定的设备信息

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
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AlertCondition(self):
        r"""告警条件(In，进围栏报警；Out，出围栏报警；InOrOut，进围栏或者出围栏均报警)
        :rtype: str
        """
        return self._AlertCondition

    @AlertCondition.setter
    def AlertCondition(self, AlertCondition):
        self._AlertCondition = AlertCondition

    @property
    def FenceEnable(self):
        r"""是否使能围栏(true，使能；false，禁用)
        :rtype: bool
        """
        return self._FenceEnable

    @FenceEnable.setter
    def FenceEnable(self, FenceEnable):
        self._FenceEnable = FenceEnable

    @property
    def Method(self):
        r"""告警处理方法
        :rtype: str
        """
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
    r"""围栏绑定的产品信息

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
        r"""围栏绑定的设备信息
        :rtype: list of FenceBindDeviceItem
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def ProductId(self):
        r"""围栏绑定的产品Id
        :rtype: str
        """
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
    r"""围栏事件详情

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
        r"""围栏事件的产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""围栏事件的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FenceId(self):
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def AlertType(self):
        r"""围栏事件的告警类型（In，进围栏报警；Out，出围栏报警；InOrOut，进围栏或者出围栏均报警）
        :rtype: str
        """
        return self._AlertType

    @AlertType.setter
    def AlertType(self, AlertType):
        self._AlertType = AlertType

    @property
    def Data(self):
        r"""围栏事件的设备位置信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.FenceAlarmPoint`
        """
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
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

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
        r"""需要过滤的字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""字段的过滤的一个或多个值
        :rtype: list of str
        """
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
    r"""设备固件详细信息

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
        :type ProductName: str
        :param _Name: 固件名称
        :type Name: str
        :param _Description: 固件描述
        :type Description: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FwType: 固件升级模块
        :type FwType: str
        :param _CreateUserId: 创建者子 uin
        :type CreateUserId: int
        :param _CreatorNickName: 创建者昵称
        :type CreatorNickName: str
        :param _UserDefined: 固件用户自定义配置信息
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
        r"""固件版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Md5sum(self):
        r"""固件MD5值
        :rtype: str
        """
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def CreateTime(self):
        r"""固件创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        r"""固件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""固件描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FwType(self):
        r"""固件升级模块
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def CreateUserId(self):
        r"""创建者子 uin
        :rtype: int
        """
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        r"""创建者昵称
        :rtype: str
        """
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def UserDefined(self):
        r"""固件用户自定义配置信息
        :rtype: str
        """
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
        


class FirmwareTaskInfo(AbstractModel):
    r"""固件升级任务信息

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
        :param _CreatorNickName: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorNickName: str
        :param _CreateUserId: 创建者ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserId: int
        :param _CronTime: 任务启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CronTime: int
        :param _FwType: 固件类型
        :type FwType: str
        """
        self._TaskId = None
        self._Status = None
        self._Type = None
        self._CreateTime = None
        self._CreatorNickName = None
        self._CreateUserId = None
        self._CronTime = None
        self._FwType = None

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        r"""任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreatorNickName(self):
        r"""创建者
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def CreateUserId(self):
        r"""创建者ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CronTime(self):
        r"""任务启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CronTime

    @CronTime.setter
    def CronTime(self, CronTime):
        self._CronTime = CronTime

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._CreatorNickName = params.get("CreatorNickName")
        self._CreateUserId = params.get("CreateUserId")
        self._CronTime = params.get("CronTime")
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenSingleDeviceSignatureOfPublicRequest(AbstractModel):
    r"""GenSingleDeviceSignatureOfPublic请求参数结构体

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
        r"""设备所属的产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""需要绑定的设备
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Expire(self):
        r"""设备绑定签名的有效时间,以秒为单位。取值范围：0 < Expire <= 86400，Expire == -1（十年）
        :rtype: int
        """
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
    r"""GenSingleDeviceSignatureOfPublic返回参数结构体

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
        r"""设备签名
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceSignatureInfo`
        """
        return self._DeviceSignature

    @DeviceSignature.setter
    def DeviceSignature(self, DeviceSignature):
        self._DeviceSignature = DeviceSignature

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
        if params.get("DeviceSignature") is not None:
            self._DeviceSignature = DeviceSignatureInfo()
            self._DeviceSignature._deserialize(params.get("DeviceSignature"))
        self._RequestId = params.get("RequestId")


class GenerateCloudStorageAIServiceTaskFileURLRequest(AbstractModel):
    r"""GenerateCloudStorageAIServiceTaskFileURL请求参数结构体

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
        r"""产品 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileName(self):
        r"""文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ExpireTime(self):
        r"""过期时间 UNIX 时间戳（默认值为当前时间 1 小时后，最大不超过文件所属任务的过期时间）
        :rtype: int
        """
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
    r"""GenerateCloudStorageAIServiceTaskFileURL返回参数结构体

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
        r"""文件下载 URL
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def ExpireTime(self):
        r"""过期时间 UNIX 时间戳（最大不超过文件所属任务的过期时间）
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
        self._FileURL = params.get("FileURL")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class GenerateSignedVideoURLRequest(AbstractModel):
    r"""GenerateSignedVideoURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoURL: 视频播放原始URL地址
        :type VideoURL: str
        :param _ExpireTime: 播放链接过期时间（时间戳，单位秒）
        :type ExpireTime: int
        :param _ChannelId: 通道ID 非NVR设备不填 NVR设备必填 默认为无	
        :type ChannelId: int
        """
        self._VideoURL = None
        self._ExpireTime = None
        self._ChannelId = None

    @property
    def VideoURL(self):
        r"""视频播放原始URL地址
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

    @property
    def ExpireTime(self):
        r"""播放链接过期时间（时间戳，单位秒）
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChannelId(self):
        r"""通道ID 非NVR设备不填 NVR设备必填 默认为无	
        :rtype: int
        """
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
    r"""GenerateSignedVideoURL返回参数结构体

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
        r"""视频防盗链播放URL
        :rtype: str
        """
        return self._SignedVideoURL

    @SignedVideoURL.setter
    def SignedVideoURL(self, SignedVideoURL):
        self._SignedVideoURL = SignedVideoURL

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
        self._SignedVideoURL = params.get("SignedVideoURL")
        self._RequestId = params.get("RequestId")


class GetAuthMiniProgramAppListRequest(AbstractModel):
    r"""GetAuthMiniProgramAppList请求参数结构体

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
        r"""appId
        :rtype: str
        """
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        self._MiniProgramAppId = MiniProgramAppId

    @property
    def Offset(self):
        r"""页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页大小
        :rtype: int
        """
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
    r"""GetAuthMiniProgramAppList返回参数结构体

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
        r"""小程序列表
        :rtype: list of AuthMiniProgramAppInfo
        """
        return self._MiniProgramList

    @MiniProgramList.setter
    def MiniProgramList(self, MiniProgramList):
        self._MiniProgramList = MiniProgramList

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
        if params.get("MiniProgramList") is not None:
            self._MiniProgramList = []
            for item in params.get("MiniProgramList"):
                obj = AuthMiniProgramAppInfo()
                obj._deserialize(item)
                self._MiniProgramList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetBatchProductionsListRequest(AbstractModel):
    r"""GetBatchProductionsList请求参数结构体

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量限制
        :rtype: int
        """
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
    r"""GetBatchProductionsList返回参数结构体

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
        r"""返回详情信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BatchProductionInfo
        """
        return self._BatchProductions

    @BatchProductions.setter
    def BatchProductions(self, BatchProductions):
        self._BatchProductions = BatchProductions

    @property
    def TotalCnt(self):
        r"""返回数量。
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

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
        if params.get("BatchProductions") is not None:
            self._BatchProductions = []
            for item in params.get("BatchProductions"):
                obj = BatchProductionInfo()
                obj._deserialize(item)
                self._BatchProductions.append(obj)
        self._TotalCnt = params.get("TotalCnt")
        self._RequestId = params.get("RequestId")


class GetCOSURLRequest(AbstractModel):
    r"""GetCOSURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param _FileSize: 文件大小
        :type FileSize: int
        :param _FwType: 模块类型or固件类型
        :type FwType: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FileSize = None
        self._FwType = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件版本
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FileSize(self):
        r"""文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FwType(self):
        r"""模块类型or固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FileSize = params.get("FileSize")
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCOSURLResponse(AbstractModel):
    r"""GetCOSURL返回参数结构体

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
        r"""固件URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class GetDeviceListRequest(AbstractModel):
    r"""GetDeviceList请求参数结构体

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
        :param _FwType: 固件类型
        :type FwType: str
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
        self._FwType = None
        self._DeviceName = None
        self._ProjectId = None
        self._Filters = None

    @property
    def ProductId(self):
        r"""需要查看设备列表的产品ID, -1代表ProjectId来筛选
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        r"""分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的大小，数值范围 10-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FirmwareVersion(self):
        r"""设备固件版本号，若不带此参数会返回所有固件版本的设备。传"None-FirmwareVersion"查询无版本号的设备
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def DeviceName(self):
        r"""需要过滤的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ProjectId(self):
        r"""项目ID。产品 ID 为 -1 时，该参数必填
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Filters(self):
        r"""每次请求的Filters的上限为10，Filter.Values的上限为1。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FwType = params.get("FwType")
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
    r"""GetDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 返回的设备列表, 注意列表设备的 DevicePsk 为空, 要获取设备的 DevicePsk 请使用 DescribeDevice
        :type Devices: list of DeviceInfo
        :param _Total: 产品下的设备总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._Total = None
        self._RequestId = None

    @property
    def Devices(self):
        r"""返回的设备列表, 注意列表设备的 DevicePsk 为空, 要获取设备的 DevicePsk 请使用 DescribeDevice
        :rtype: list of DeviceInfo
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Total(self):
        r"""产品下的设备总数
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
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetDeviceLocationHistoryRequest(AbstractModel):
    r"""GetDeviceLocationHistory请求参数结构体

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
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def StartTime(self):
        r"""查询起始时间，Unix时间，单位为毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，Unix时间，单位为毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CoordinateType(self):
        r"""坐标类型
        :rtype: int
        """
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
    r"""GetDeviceLocationHistory返回参数结构体

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
        r"""历史位置列表
        :rtype: list of PositionItem
        """
        return self._Positions

    @Positions.setter
    def Positions(self, Positions):
        self._Positions = Positions

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
        if params.get("Positions") is not None:
            self._Positions = []
            for item in params.get("Positions"):
                obj = PositionItem()
                obj._deserialize(item)
                self._Positions.append(obj)
        self._RequestId = params.get("RequestId")


class GetDeviceSumStatisticsRequest(AbstractModel):
    r"""GetDeviceSumStatistics请求参数结构体

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
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductIds(self):
        r"""产品id列表，长度为0则拉取项目内全部产品
        :rtype: list of str
        """
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
    r"""GetDeviceSumStatistics返回参数结构体

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
        r"""激活设备总数
        :rtype: int
        """
        return self._ActivationCount

    @ActivationCount.setter
    def ActivationCount(self, ActivationCount):
        self._ActivationCount = ActivationCount

    @property
    def OnlineCount(self):
        r"""在线设备总数
        :rtype: int
        """
        return self._OnlineCount

    @OnlineCount.setter
    def OnlineCount(self, OnlineCount):
        self._OnlineCount = OnlineCount

    @property
    def ActivationBeforeDay(self):
        r"""前一天激活设备数
        :rtype: int
        """
        return self._ActivationBeforeDay

    @ActivationBeforeDay.setter
    def ActivationBeforeDay(self, ActivationBeforeDay):
        self._ActivationBeforeDay = ActivationBeforeDay

    @property
    def ActiveBeforeDay(self):
        r"""前一天活跃设备数
        :rtype: int
        """
        return self._ActiveBeforeDay

    @ActiveBeforeDay.setter
    def ActiveBeforeDay(self, ActiveBeforeDay):
        self._ActiveBeforeDay = ActiveBeforeDay

    @property
    def ActivationWeekDayCount(self):
        r"""前一周激活设备数
        :rtype: int
        """
        return self._ActivationWeekDayCount

    @ActivationWeekDayCount.setter
    def ActivationWeekDayCount(self, ActivationWeekDayCount):
        self._ActivationWeekDayCount = ActivationWeekDayCount

    @property
    def ActiveWeekDayCount(self):
        r"""前一周活跃设备数
        :rtype: int
        """
        return self._ActiveWeekDayCount

    @ActiveWeekDayCount.setter
    def ActiveWeekDayCount(self, ActiveWeekDayCount):
        self._ActiveWeekDayCount = ActiveWeekDayCount

    @property
    def ActivationBeforeWeekDayCount(self):
        r"""上一周激活设备数
        :rtype: int
        """
        return self._ActivationBeforeWeekDayCount

    @ActivationBeforeWeekDayCount.setter
    def ActivationBeforeWeekDayCount(self, ActivationBeforeWeekDayCount):
        self._ActivationBeforeWeekDayCount = ActivationBeforeWeekDayCount

    @property
    def ActiveBeforeWeekDayCount(self):
        r"""上一周活跃设备数
        :rtype: int
        """
        return self._ActiveBeforeWeekDayCount

    @ActiveBeforeWeekDayCount.setter
    def ActiveBeforeWeekDayCount(self, ActiveBeforeWeekDayCount):
        self._ActiveBeforeWeekDayCount = ActiveBeforeWeekDayCount

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
    r"""GetFamilyDeviceUserList请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
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
        


class GetFamilyDeviceUserListResponse(AbstractModel):
    r"""GetFamilyDeviceUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserList: 设备的用户列表
        :type UserList: list of DeviceUser
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserList = None
        self._RequestId = None

    @property
    def UserList(self):
        r"""设备的用户列表
        :rtype: list of DeviceUser
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

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
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = DeviceUser()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class GetGatewaySubDeviceListRequest(AbstractModel):
    r"""GetGatewaySubDeviceList请求参数结构体

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
        r"""网关产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        r"""网关设备名称
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def Offset(self):
        r"""分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的大小
        :rtype: int
        """
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
    r"""GetGatewaySubDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 设备的总数
        :type Total: int
        :param _DeviceList: 设备列表
        :type DeviceList: :class:`tencentcloud.iotexplorer.v20190423.models.FamilySubDevice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""设备的总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.FamilySubDevice`
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

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
        self._Total = params.get("Total")
        if params.get("DeviceList") is not None:
            self._DeviceList = FamilySubDevice()
            self._DeviceList._deserialize(params.get("DeviceList"))
        self._RequestId = params.get("RequestId")


class GetLoRaGatewayListRequest(AbstractModel):
    r"""GetLoRaGatewayList请求参数结构体

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
        r"""是否是社区网关
        :rtype: bool
        """
        return self._IsCommunity

    @IsCommunity.setter
    def IsCommunity(self, IsCommunity):
        self._IsCommunity = IsCommunity

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制个数
        :rtype: int
        """
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
    r"""GetLoRaGatewayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回总数
        :type Total: int
        :param _Gateways: 返回详情项
        :type Gateways: list of LoRaGatewayItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Gateways = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Gateways(self):
        r"""返回详情项
        :rtype: list of LoRaGatewayItem
        """
        return self._Gateways

    @Gateways.setter
    def Gateways(self, Gateways):
        self._Gateways = Gateways

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
        self._Total = params.get("Total")
        if params.get("Gateways") is not None:
            self._Gateways = []
            for item in params.get("Gateways"):
                obj = LoRaGatewayItem()
                obj._deserialize(item)
                self._Gateways.append(obj)
        self._RequestId = params.get("RequestId")


class GetPositionSpaceListRequest(AbstractModel):
    r"""GetPositionSpaceList请求参数结构体

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
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Offset(self):
        r"""翻页偏移量，0起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大返回结果数
        :rtype: int
        """
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
    r"""GetPositionSpaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 位置空间列表
        :type List: list of PositionSpaceInfo
        :param _Total: 位置空间数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        r"""位置空间列表
        :rtype: list of PositionSpaceInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""位置空间数量
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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PositionSpaceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetProjectListRequest(AbstractModel):
    r"""GetProjectList请求参数结构体

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""个数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProjectId(self):
        r"""按项目ID搜索
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductId(self):
        r"""按产品ID搜索
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Includes(self):
        r"""加载 ProductCount、DeviceCount、ApplicationCount，可选值：ProductCount、DeviceCount、ApplicationCount，可多选
        :rtype: list of str
        """
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def ProjectName(self):
        r"""按项目名称搜索
        :rtype: str
        """
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
    r"""GetProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Projects: 项目列表
        :type Projects: list of ProjectEntryEx
        :param _Total: 列表项个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Projects = None
        self._Total = None
        self._RequestId = None

    @property
    def Projects(self):
        r"""项目列表
        :rtype: list of ProjectEntryEx
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def Total(self):
        r"""列表项个数
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
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = ProjectEntryEx()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetStudioProductListRequest(AbstractModel):
    r"""GetStudioProductList请求参数结构体

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DevStatus(self):
        r"""产品DevStatus
        :rtype: str
        """
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""数量限制
        :rtype: int
        """
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
    r"""GetStudioProductList返回参数结构体

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
        r"""产品列表
        :rtype: list of ProductEntry
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def Total(self):
        r"""产品数量
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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetTWeCallActiveStatusRequest(AbstractModel):
    r"""GetTWeCallActiveStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniProgramAppId: 参数已弃用，不用传参
        :type MiniProgramAppId: str
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._MiniProgramAppId = None
        self._DeviceList = None

    @property
    def MiniProgramAppId(self):
        warnings.warn("parameter `MiniProgramAppId` is deprecated", DeprecationWarning) 

        r"""参数已弃用，不用传参
        :rtype: str
        """
        return self._MiniProgramAppId

    @MiniProgramAppId.setter
    def MiniProgramAppId(self, MiniProgramAppId):
        warnings.warn("parameter `MiniProgramAppId` is deprecated", DeprecationWarning) 

        self._MiniProgramAppId = MiniProgramAppId

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: list of TWeCallInfo
        """
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
    r"""GetTWeCallActiveStatus返回参数结构体

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
        r"""激活状态
        :rtype: list of TWeCallActiveInfo
        """
        return self._TWeCallActiveInfos

    @TWeCallActiveInfos.setter
    def TWeCallActiveInfos(self, TWeCallActiveInfos):
        self._TWeCallActiveInfos = TWeCallActiveInfos

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
        if params.get("TWeCallActiveInfos") is not None:
            self._TWeCallActiveInfos = []
            for item in params.get("TWeCallActiveInfos"):
                obj = TWeCallActiveInfo()
                obj._deserialize(item)
                self._TWeCallActiveInfos.append(obj)
        self._RequestId = params.get("RequestId")


class GetTWeTalkProductConfigListRequest(AbstractModel):
    r"""GetTWeTalkProductConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TargetLanguage: 	支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 偏移量，10-100
        :type Limit: int
        """
        self._ProductId = None
        self._TargetLanguage = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TargetLanguage(self):
        r"""	支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def Offset(self):
        r"""页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""偏移量，10-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TargetLanguage = params.get("TargetLanguage")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTWeTalkProductConfigListResponse(AbstractModel):
    r"""GetTWeTalkProductConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置信息列表
        :type Data: list of TalkProductConfigInfo
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""配置信息列表
        :rtype: list of TalkProductConfigInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TalkProductConfigInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetTWeTalkProductConfigListV2Request(AbstractModel):
    r"""GetTWeTalkProductConfigListV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        :param _IncludeCredentials: 是否脱敏
        :type IncludeCredentials: bool
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 每页数据大小， 10-100
        :type Limit: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._TargetLanguage = None
        self._IncludeCredentials = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def IncludeCredentials(self):
        r"""是否脱敏
        :rtype: bool
        """
        return self._IncludeCredentials

    @IncludeCredentials.setter
    def IncludeCredentials(self, IncludeCredentials):
        self._IncludeCredentials = IncludeCredentials

    @property
    def Offset(self):
        r"""页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数据大小， 10-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._TargetLanguage = params.get("TargetLanguage")
        self._IncludeCredentials = params.get("IncludeCredentials")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTWeTalkProductConfigListV2Response(AbstractModel):
    r"""GetTWeTalkProductConfigListV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置信息
        :type Data: list of TalkProductConfigV2Info
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""配置信息
        :rtype: list of TalkProductConfigV2Info
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TalkProductConfigV2Info()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetTopicRuleListRequest(AbstractModel):
    r"""GetTopicRuleList请求参数结构体

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
        r"""请求的页数
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""分页的大小
        :rtype: int
        """
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
    r"""GetTopicRuleList返回参数结构体

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
        r"""规则总数量
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of TopicRuleInfo
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

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
        self._TotalCnt = params.get("TotalCnt")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = TopicRuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class GetWechatDeviceTicketRequest(AbstractModel):
    r"""GetWechatDeviceTicket请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""产品名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def IsThirdApp(self):
        r"""是否第三方小程序
        :rtype: int
        """
        return self._IsThirdApp

    @IsThirdApp.setter
    def IsThirdApp(self, IsThirdApp):
        self._IsThirdApp = IsThirdApp

    @property
    def ModelId(self):
        r"""模板ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def MiniProgramAppId(self):
        r"""小程序APPID
        :rtype: str
        """
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
    r"""GetWechatDeviceTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WXDeviceInfo: 微信设备信息
        :type WXDeviceInfo: :class:`tencentcloud.iotexplorer.v20190423.models.WXDeviceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WXDeviceInfo = None
        self._RequestId = None

    @property
    def WXDeviceInfo(self):
        r"""微信设备信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.WXDeviceInfo`
        """
        return self._WXDeviceInfo

    @WXDeviceInfo.setter
    def WXDeviceInfo(self, WXDeviceInfo):
        self._WXDeviceInfo = WXDeviceInfo

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
        if params.get("WXDeviceInfo") is not None:
            self._WXDeviceInfo = WXDeviceInfo()
            self._WXDeviceInfo._deserialize(params.get("WXDeviceInfo"))
        self._RequestId = params.get("RequestId")


class IdleResponseInfo(AbstractModel):
    r"""空闲检测配置信息。

    """

    def __init__(self):
        r"""
        :param _RetryCount: 重试次数（1-3）
        :type RetryCount: int
        :param _Message: 响应信息
        :type Message: str
        """
        self._RetryCount = None
        self._Message = None

    @property
    def RetryCount(self):
        r"""重试次数（1-3）
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def Message(self):
        r"""响应信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._RetryCount = params.get("RetryCount")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InheritCloudStorageUserRequest(AbstractModel):
    r"""InheritCloudStorageUser请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""原始用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ToUserId(self):
        r"""目标用户ID
        :rtype: str
        """
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
    r"""InheritCloudStorageUser返回参数结构体

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


class InstanceDetail(AbstractModel):
    r"""实例信息
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
        :type TotalDevice: int
        :param _ActivateDevice: 激活设备数
        :type ActivateDevice: int
        :param _Description: 备注
        :type Description: str
        :param _Status: 实例状态
        :type Status: int
        :param _UpDownTPS: 消息上下行配置TPS
        :type UpDownTPS: int
        :param _UpDownCurrentTPS: 当前消息上下行TPS
        :type UpDownCurrentTPS: int
        :param _ForwardTPS: 消息转发配置TPS
        :type ForwardTPS: int
        :param _ForwardCurrentTPS: 消息转发当前TPS
        :type ForwardCurrentTPS: int
        :param _CellNum: 实例单元数
        :type CellNum: int
        :param _BillingTag: 实例Tag，企业实例必传
        :type BillingTag: str
        :param _EverydayFreeMessageCount: 每日消息数
        :type EverydayFreeMessageCount: int
        :param _MaxDeviceOnlineCount: 最大在线设备数
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
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        r"""实例类型（0 公共实例 1 标准企业实例 2新企业实例3新公共实例）
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Region(self):
        r"""地域字母缩写
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ZoneId(self):
        r"""区域全拼
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TotalDeviceNum(self):
        r"""支持设备总数
        :rtype: int
        """
        return self._TotalDeviceNum

    @TotalDeviceNum.setter
    def TotalDeviceNum(self, TotalDeviceNum):
        self._TotalDeviceNum = TotalDeviceNum

    @property
    def UsedDeviceNum(self):
        r"""已注册设备数
        :rtype: int
        """
        return self._UsedDeviceNum

    @UsedDeviceNum.setter
    def UsedDeviceNum(self, UsedDeviceNum):
        self._UsedDeviceNum = UsedDeviceNum

    @property
    def ProjectNum(self):
        r"""项目数
        :rtype: int
        """
        return self._ProjectNum

    @ProjectNum.setter
    def ProjectNum(self, ProjectNum):
        self._ProjectNum = ProjectNum

    @property
    def ProductNum(self):
        r"""产品数
        :rtype: int
        """
        return self._ProductNum

    @ProductNum.setter
    def ProductNum(self, ProductNum):
        self._ProductNum = ProductNum

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
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExpireTime(self):
        r"""过期时间，公共实例过期时间 0001-01-01T00:00:00Z，公共实例是永久有效
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TotalDevice(self):
        r"""总设备数
        :rtype: int
        """
        return self._TotalDevice

    @TotalDevice.setter
    def TotalDevice(self, TotalDevice):
        self._TotalDevice = TotalDevice

    @property
    def ActivateDevice(self):
        r"""激活设备数
        :rtype: int
        """
        return self._ActivateDevice

    @ActivateDevice.setter
    def ActivateDevice(self, ActivateDevice):
        self._ActivateDevice = ActivateDevice

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
    def Status(self):
        r"""实例状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpDownTPS(self):
        r"""消息上下行配置TPS
        :rtype: int
        """
        return self._UpDownTPS

    @UpDownTPS.setter
    def UpDownTPS(self, UpDownTPS):
        self._UpDownTPS = UpDownTPS

    @property
    def UpDownCurrentTPS(self):
        r"""当前消息上下行TPS
        :rtype: int
        """
        return self._UpDownCurrentTPS

    @UpDownCurrentTPS.setter
    def UpDownCurrentTPS(self, UpDownCurrentTPS):
        self._UpDownCurrentTPS = UpDownCurrentTPS

    @property
    def ForwardTPS(self):
        r"""消息转发配置TPS
        :rtype: int
        """
        return self._ForwardTPS

    @ForwardTPS.setter
    def ForwardTPS(self, ForwardTPS):
        self._ForwardTPS = ForwardTPS

    @property
    def ForwardCurrentTPS(self):
        r"""消息转发当前TPS
        :rtype: int
        """
        return self._ForwardCurrentTPS

    @ForwardCurrentTPS.setter
    def ForwardCurrentTPS(self, ForwardCurrentTPS):
        self._ForwardCurrentTPS = ForwardCurrentTPS

    @property
    def CellNum(self):
        r"""实例单元数
        :rtype: int
        """
        return self._CellNum

    @CellNum.setter
    def CellNum(self, CellNum):
        self._CellNum = CellNum

    @property
    def BillingTag(self):
        r"""实例Tag，企业实例必传
        :rtype: str
        """
        return self._BillingTag

    @BillingTag.setter
    def BillingTag(self, BillingTag):
        self._BillingTag = BillingTag

    @property
    def EverydayFreeMessageCount(self):
        r"""每日消息数
        :rtype: int
        """
        return self._EverydayFreeMessageCount

    @EverydayFreeMessageCount.setter
    def EverydayFreeMessageCount(self, EverydayFreeMessageCount):
        self._EverydayFreeMessageCount = EverydayFreeMessageCount

    @property
    def MaxDeviceOnlineCount(self):
        r"""最大在线设备数
        :rtype: int
        """
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
        


class InvokeAISearchServiceRequest(AbstractModel):
    r"""InvokeAISearchService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Query: 自然语言查询
        :type Query: str
        :param _SummaryLang: 搜索结果总结的语言类型，支持的类型有：en-US、zh-CN、id-ID、th-TH
        :type SummaryLang: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        :param _EnableSummary: 是否需要返回总结，默认为True；  开启后会加大接口响应时长
        :type EnableSummary: bool
        :param _StartTimeMs: 开始时间。

注：
1. 单位为毫秒（ms）
2. 如果同时指定了StartTimeMs与EndTimeMs，时间区间不能大于7天；如果只指定其中一个（例如只指定StartTimeMs，则查询自StartTimeMs后1天内的数据， 反之EndTimeMs也一样）
3. 只要指定了其中一个参数，接口则会忽略Query参数中关于时间的描述；（例如Query为"过去三天关于猫咪的视频"， 则会将"过去三天忽略"）
        :type StartTimeMs: int
        :param _EndTimeMs: 结束时间。

注：
1. 单位为毫秒（ms）
2. 如果同时指定了StartTimeMs与EndTimeMs，时间区间不能大于7天；如果只指定其中一个（例如只指定StartTimeMs，则查询自StartTimeMs后1天内的数据， 反之EndTimeMs也一样）
3. 只要指定了其中一个参数，接口则会忽略Query参数中关于时间的描述；（例如Query为"过去三天关于猫咪的视频"， 则会将"过去三天忽略"）
        :type EndTimeMs: int
        :param _TimeZone: 时区。默认值：Asia/Shanghai

注：
符合iana标准 https://www.iana.org/time-zones，例如Asia/Shanghai、Asia/Bangkok

        :type TimeZone: str
        :param _SearchMode: 取值为1表示高级搜索，取值为2表示简单搜索，默认为1
        :type SearchMode: int
        :param _Limit: 最终输出的条数；仅当SearchMode为2时支持自定义设置，默认为50
        :type Limit: int
        :param _VectorSearchRadius: 向量搜索的相似度搜索半径，取值范围[-1, 1]；仅当SearchMode为2时支持自定义设置，默认为0.5
        :type VectorSearchRadius: float
        :param _VectorSearchTopK: 指定向量搜索最相似的 Top K；仅当SearchMode为2时支持自定义设置，默认为100
        :type VectorSearchTopK: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Query = None
        self._SummaryLang = None
        self._ChannelId = None
        self._EnableSummary = None
        self._StartTimeMs = None
        self._EndTimeMs = None
        self._TimeZone = None
        self._SearchMode = None
        self._Limit = None
        self._VectorSearchRadius = None
        self._VectorSearchTopK = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Query(self):
        r"""自然语言查询
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def SummaryLang(self):
        r"""搜索结果总结的语言类型，支持的类型有：en-US、zh-CN、id-ID、th-TH
        :rtype: str
        """
        return self._SummaryLang

    @SummaryLang.setter
    def SummaryLang(self, SummaryLang):
        self._SummaryLang = SummaryLang

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def EnableSummary(self):
        r"""是否需要返回总结，默认为True；  开启后会加大接口响应时长
        :rtype: bool
        """
        return self._EnableSummary

    @EnableSummary.setter
    def EnableSummary(self, EnableSummary):
        self._EnableSummary = EnableSummary

    @property
    def StartTimeMs(self):
        r"""开始时间。

注：
1. 单位为毫秒（ms）
2. 如果同时指定了StartTimeMs与EndTimeMs，时间区间不能大于7天；如果只指定其中一个（例如只指定StartTimeMs，则查询自StartTimeMs后1天内的数据， 反之EndTimeMs也一样）
3. 只要指定了其中一个参数，接口则会忽略Query参数中关于时间的描述；（例如Query为"过去三天关于猫咪的视频"， 则会将"过去三天忽略"）
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTimeMs(self):
        r"""结束时间。

注：
1. 单位为毫秒（ms）
2. 如果同时指定了StartTimeMs与EndTimeMs，时间区间不能大于7天；如果只指定其中一个（例如只指定StartTimeMs，则查询自StartTimeMs后1天内的数据， 反之EndTimeMs也一样）
3. 只要指定了其中一个参数，接口则会忽略Query参数中关于时间的描述；（例如Query为"过去三天关于猫咪的视频"， 则会将"过去三天忽略"）
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def TimeZone(self):
        r"""时区。默认值：Asia/Shanghai

注：
符合iana标准 https://www.iana.org/time-zones，例如Asia/Shanghai、Asia/Bangkok

        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def SearchMode(self):
        r"""取值为1表示高级搜索，取值为2表示简单搜索，默认为1
        :rtype: int
        """
        return self._SearchMode

    @SearchMode.setter
    def SearchMode(self, SearchMode):
        self._SearchMode = SearchMode

    @property
    def Limit(self):
        r"""最终输出的条数；仅当SearchMode为2时支持自定义设置，默认为50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def VectorSearchRadius(self):
        r"""向量搜索的相似度搜索半径，取值范围[-1, 1]；仅当SearchMode为2时支持自定义设置，默认为0.5
        :rtype: float
        """
        return self._VectorSearchRadius

    @VectorSearchRadius.setter
    def VectorSearchRadius(self, VectorSearchRadius):
        self._VectorSearchRadius = VectorSearchRadius

    @property
    def VectorSearchTopK(self):
        r"""指定向量搜索最相似的 Top K；仅当SearchMode为2时支持自定义设置，默认为100
        :rtype: int
        """
        return self._VectorSearchTopK

    @VectorSearchTopK.setter
    def VectorSearchTopK(self, VectorSearchTopK):
        self._VectorSearchTopK = VectorSearchTopK


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Query = params.get("Query")
        self._SummaryLang = params.get("SummaryLang")
        self._ChannelId = params.get("ChannelId")
        self._EnableSummary = params.get("EnableSummary")
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTimeMs = params.get("EndTimeMs")
        self._TimeZone = params.get("TimeZone")
        self._SearchMode = params.get("SearchMode")
        self._Limit = params.get("Limit")
        self._VectorSearchRadius = params.get("VectorSearchRadius")
        self._VectorSearchTopK = params.get("VectorSearchTopK")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeAISearchServiceResponse(AbstractModel):
    r"""InvokeAISearchService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Summary: 基于搜索结果的总结
        :type Summary: str
        :param _Targets: 视频结果集
        :type Targets: list of TargetInfo
        :param _VideoURL: 视频回放URL
        :type VideoURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Summary = None
        self._Targets = None
        self._VideoURL = None
        self._RequestId = None

    @property
    def Summary(self):
        r"""基于搜索结果的总结
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Targets(self):
        r"""视频结果集
        :rtype: list of TargetInfo
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def VideoURL(self):
        r"""视频回放URL
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

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
        self._Summary = params.get("Summary")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetInfo()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._VideoURL = params.get("VideoURL")
        self._RequestId = params.get("RequestId")


class InvokeCloudStorageAIServiceTaskRequest(AbstractModel):
    r"""InvokeCloudStorageAIServiceTask请求参数结构体

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
- `VideoToText`：视频语义理解
        :type ServiceType: str
        :param _StartTime: 待分析云存的起始时间
        :type StartTime: int
        :param _EndTime: 待分析云存的结束时间
        :type EndTime: int
        :param _ChannelId: 通道 ID
        :type ChannelId: int
        :param _Config: 视频分析配置参数
        :type Config: str
        :param _ROI: 视频分析识别区域
        :type ROI: str
        :param _VideoURLs: 分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :type VideoURLs: list of str
        :param _CustomId: 自定义任务 ID
        :type CustomId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._StartTime = None
        self._EndTime = None
        self._ChannelId = None
        self._Config = None
        self._ROI = None
        self._VideoURLs = None
        self._CustomId = None

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StartTime(self):
        r"""待分析云存的起始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""待分析云存的结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Config(self):
        r"""视频分析配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ROI(self):
        r"""视频分析识别区域
        :rtype: str
        """
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI

    @property
    def VideoURLs(self):
        r"""分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :rtype: list of str
        """
        return self._VideoURLs

    @VideoURLs.setter
    def VideoURLs(self, VideoURLs):
        self._VideoURLs = VideoURLs

    @property
    def CustomId(self):
        r"""自定义任务 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ChannelId = params.get("ChannelId")
        self._Config = params.get("Config")
        self._ROI = params.get("ROI")
        self._VideoURLs = params.get("VideoURLs")
        self._CustomId = params.get("CustomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCloudStorageAIServiceTaskResponse(AbstractModel):
    r"""InvokeCloudStorageAIServiceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Completed: 任务是否执行完成
        :type Completed: bool
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _TaskInfo: 任务信息
        :type TaskInfo: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Completed = None
        self._TaskId = None
        self._TaskInfo = None
        self._RequestId = None

    @property
    def Completed(self):
        r"""任务是否执行完成
        :rtype: bool
        """
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskInfo(self):
        r"""任务信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTask`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

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
        self._Completed = params.get("Completed")
        self._TaskId = params.get("TaskId")
        if params.get("TaskInfo") is not None:
            self._TaskInfo = CloudStorageAIServiceTask()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class InvokeExternalSourceAIServiceTaskRequest(AbstractModel):
    r"""InvokeExternalSourceAIServiceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品 ID
        :type ProductId: str
        :param _ServiceType: 云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :type ServiceType: str
        :param _VideoURLs: 分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :type VideoURLs: list of str
        :param _CustomId: 自定义任务 ID
        :type CustomId: str
        :param _Config: 视频分析配置参数
        :type Config: str
        :param _ROI: 视频分析识别区域
        :type ROI: str
        """
        self._ProductId = None
        self._ServiceType = None
        self._VideoURLs = None
        self._CustomId = None
        self._Config = None
        self._ROI = None

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `VideoToText`：视频语义理解
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def VideoURLs(self):
        r"""分析外部传入的视频 URL 列表，支持 HLS 点播（m3u8）及常见视频格式（mp4 等）
        :rtype: list of str
        """
        return self._VideoURLs

    @VideoURLs.setter
    def VideoURLs(self, VideoURLs):
        self._VideoURLs = VideoURLs

    @property
    def CustomId(self):
        r"""自定义任务 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def Config(self):
        r"""视频分析配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ROI(self):
        r"""视频分析识别区域
        :rtype: str
        """
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ServiceType = params.get("ServiceType")
        self._VideoURLs = params.get("VideoURLs")
        self._CustomId = params.get("CustomId")
        self._Config = params.get("Config")
        self._ROI = params.get("ROI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeExternalSourceAIServiceTaskResponse(AbstractModel):
    r"""InvokeExternalSourceAIServiceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Completed: 任务是否执行完成
        :type Completed: bool
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _TaskInfo: 任务信息
        :type TaskInfo: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Completed = None
        self._TaskId = None
        self._TaskInfo = None
        self._RequestId = None

    @property
    def Completed(self):
        r"""任务是否执行完成
        :rtype: bool
        """
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskInfo(self):
        r"""任务信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CloudStorageAIServiceTask`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

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
        self._Completed = params.get("Completed")
        self._TaskId = params.get("TaskId")
        if params.get("TaskInfo") is not None:
            self._TaskInfo = CloudStorageAIServiceTask()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class InvokeTWeSeeRecognitionTaskRequest(AbstractModel):
    r"""InvokeTWeSeeRecognitionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _InputURL: 输入视频 / 图片的 URL
        :type InputURL: str
        :param _CustomId: 自定义事件 ID
        :type CustomId: str
        :param _EnableSearch: 是否保存该事件使其可被搜索
        :type EnableSearch: bool
        :param _StartTimeMs: 事件起始时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :type StartTimeMs: int
        :param _EndTimeMs: 事件结束时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :type EndTimeMs: int
        :param _Config: 算法配置
        :type Config: str
        :param _IsCustomDevice: 是否自定义设备，为 true 时不检查设备存在性，默认为 false
        :type IsCustomDevice: bool
        :param _InputType: 输入类型。可选值：

- `video`：视频（默认值）
- `image`：图片
        :type InputType: str
        :param _SummaryQOS: 摘要服务质量。可选值：

- `minutely`：分钟级（默认值）
- `immediate`：立即
        :type SummaryQOS: str
        :param _SummaryConfig: 摘要输出配置
        :type SummaryConfig: :class:`tencentcloud.iotexplorer.v20190423.models.VisionSummaryConfig`
        :param _ServiceType: 算法类型，可能取值：
- `Summary`：视频/图片摘要
- `ObjectDetect`：目标检测
        :type ServiceType: str
        :param _ObjectDetectConfig: 目标检测配置
        :type ObjectDetectConfig: :class:`tencentcloud.iotexplorer.v20190423.models.VisionObjectDetectConfig`
        """
        self._ProductId = None
        self._DeviceName = None
        self._InputURL = None
        self._CustomId = None
        self._EnableSearch = None
        self._StartTimeMs = None
        self._EndTimeMs = None
        self._Config = None
        self._IsCustomDevice = None
        self._InputType = None
        self._SummaryQOS = None
        self._SummaryConfig = None
        self._ServiceType = None
        self._ObjectDetectConfig = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def InputURL(self):
        r"""输入视频 / 图片的 URL
        :rtype: str
        """
        return self._InputURL

    @InputURL.setter
    def InputURL(self, InputURL):
        self._InputURL = InputURL

    @property
    def CustomId(self):
        r"""自定义事件 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def EnableSearch(self):
        r"""是否保存该事件使其可被搜索
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch

    @property
    def StartTimeMs(self):
        r"""事件起始时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTimeMs(self):
        r"""事件结束时间事件起始时间（毫秒级 UNIX 时间戳，若不传则默认为接口调用时间）
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def Config(self):
        r"""算法配置
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def IsCustomDevice(self):
        r"""是否自定义设备，为 true 时不检查设备存在性，默认为 false
        :rtype: bool
        """
        return self._IsCustomDevice

    @IsCustomDevice.setter
    def IsCustomDevice(self, IsCustomDevice):
        self._IsCustomDevice = IsCustomDevice

    @property
    def InputType(self):
        r"""输入类型。可选值：

- `video`：视频（默认值）
- `image`：图片
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def SummaryQOS(self):
        r"""摘要服务质量。可选值：

- `minutely`：分钟级（默认值）
- `immediate`：立即
        :rtype: str
        """
        return self._SummaryQOS

    @SummaryQOS.setter
    def SummaryQOS(self, SummaryQOS):
        self._SummaryQOS = SummaryQOS

    @property
    def SummaryConfig(self):
        r"""摘要输出配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionSummaryConfig`
        """
        return self._SummaryConfig

    @SummaryConfig.setter
    def SummaryConfig(self, SummaryConfig):
        self._SummaryConfig = SummaryConfig

    @property
    def ServiceType(self):
        r"""算法类型，可能取值：
- `Summary`：视频/图片摘要
- `ObjectDetect`：目标检测
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ObjectDetectConfig(self):
        r"""目标检测配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionObjectDetectConfig`
        """
        return self._ObjectDetectConfig

    @ObjectDetectConfig.setter
    def ObjectDetectConfig(self, ObjectDetectConfig):
        self._ObjectDetectConfig = ObjectDetectConfig


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._InputURL = params.get("InputURL")
        self._CustomId = params.get("CustomId")
        self._EnableSearch = params.get("EnableSearch")
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTimeMs = params.get("EndTimeMs")
        self._Config = params.get("Config")
        self._IsCustomDevice = params.get("IsCustomDevice")
        self._InputType = params.get("InputType")
        self._SummaryQOS = params.get("SummaryQOS")
        if params.get("SummaryConfig") is not None:
            self._SummaryConfig = VisionSummaryConfig()
            self._SummaryConfig._deserialize(params.get("SummaryConfig"))
        self._ServiceType = params.get("ServiceType")
        if params.get("ObjectDetectConfig") is not None:
            self._ObjectDetectConfig = VisionObjectDetectConfig()
            self._ObjectDetectConfig._deserialize(params.get("ObjectDetectConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeTWeSeeRecognitionTaskResponse(AbstractModel):
    r"""InvokeTWeSeeRecognitionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _Completed: 任务是否执行完成
        :type Completed: bool
        :param _Result: 语义理解任务结果（仅当 Completed 为 true 时包含该出参）
        :type Result: :class:`tencentcloud.iotexplorer.v20190423.models.VisionRecognitionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Completed = None
        self._Result = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Completed(self):
        r"""任务是否执行完成
        :rtype: bool
        """
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def Result(self):
        r"""语义理解任务结果（仅当 Completed 为 true 时包含该出参）
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionRecognitionResult`
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
        self._TaskId = params.get("TaskId")
        self._Completed = params.get("Completed")
        if params.get("Result") is not None:
            self._Result = VisionRecognitionResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InvokeVideosKeywordsAnalyzerRequest(AbstractModel):
    r"""InvokeVideosKeywordsAnalyzer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _StartTimeMs: 开始时间。

注：
1. 单位为毫秒（ms）
2. 时间区间必须控制在某一个自然天内，不支持跨天
        :type StartTimeMs: int
        :param _EndTimeMs: 结束时间。

注：
1. 单位为毫秒（ms）
2. 时间区间必须控制在某一个自然天内，不支持跨天
        :type EndTimeMs: int
        :param _KeywordsMaxNum: 返回的关键字最大数量，默认为5；最大不能超过10
        :type KeywordsMaxNum: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._StartTimeMs = None
        self._EndTimeMs = None
        self._KeywordsMaxNum = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def StartTimeMs(self):
        r"""开始时间。

注：
1. 单位为毫秒（ms）
2. 时间区间必须控制在某一个自然天内，不支持跨天
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTimeMs(self):
        r"""结束时间。

注：
1. 单位为毫秒（ms）
2. 时间区间必须控制在某一个自然天内，不支持跨天
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def KeywordsMaxNum(self):
        r"""返回的关键字最大数量，默认为5；最大不能超过10
        :rtype: int
        """
        return self._KeywordsMaxNum

    @KeywordsMaxNum.setter
    def KeywordsMaxNum(self, KeywordsMaxNum):
        self._KeywordsMaxNum = KeywordsMaxNum


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTimeMs = params.get("EndTimeMs")
        self._KeywordsMaxNum = params.get("KeywordsMaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeVideosKeywordsAnalyzerResponse(AbstractModel):
    r"""InvokeVideosKeywordsAnalyzer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Keywords: 基于搜索结果的总结
        :type Keywords: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Keywords = None
        self._RequestId = None

    @property
    def Keywords(self):
        r"""基于搜索结果的总结
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

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
        self._Keywords = params.get("Keywords")
        self._RequestId = params.get("RequestId")


class IotApplication(AbstractModel):
    r"""应用信息

    """

    def __init__(self):
        r"""
        :param _IotAppID: 应用 ID
        :type IotAppID: str
        :param _AppName: 应用名称
        :type AppName: str
        :param _Description: 应用说明
        :type Description: str
        :param _DevMode: 开发模式
        :type DevMode: int
        :param _IOSAppKey: iOS 平台 AppKey
        :type IOSAppKey: str
        :param _IOSAppSecret: iOS 平台 AppSecret
        :type IOSAppSecret: str
        :param _AndroidAppKey: Android 平台 AppKey
        :type AndroidAppKey: str
        :param _AndroidAppSecret: Android 平台 AppSecret
        :type AndroidAppSecret: str
        :param _Products: 绑定的产品列表，数据为：ProdcutID 数组 JSON 序列化后的字符串
        :type Products: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PushSecretID: 信鸽推送APP ID
        :type PushSecretID: str
        :param _PushSecretKey: 信鸽推送SECRET KEY
        :type PushSecretKey: str
        :param _PushEnvironment: iOS平台推送环境
        :type PushEnvironment: str
        :param _MiniProgramAppKey: 小程序平台 AppKey
        :type MiniProgramAppKey: str
        :param _MiniProgramAppSecret: 小程序平台 AppSecret
        :type MiniProgramAppSecret: str
        :param _TPNSiOSAccessID: TPNS服务iOS应用AccessID，TPNS全称为腾讯移动推送（Tencent Push Notification Service），详见：https://cloud.tencent.com/document/product/548
        :type TPNSiOSAccessID: str
        :param _TPNSiOSSecretKey: TPNS服务iOS应用SecretKey
        :type TPNSiOSSecretKey: str
        :param _TPNSiOSPushEnvironment: TPNS服务iOS应用推送环境
        :type TPNSiOSPushEnvironment: str
        :param _TPNSAndroidAccessID: TPNS服务Android应用AccessID
        :type TPNSAndroidAccessID: str
        :param _TPNSAndroidSecretKey: TPNS服务Android应用SecretKey
        :type TPNSAndroidSecretKey: str
        :param _TPNSiOSRegion: TPNS服务iOS应用所属地域，详细说明参见 ModifyApplication 同名入参。
        :type TPNSiOSRegion: str
        :param _TPNSAndroidRegion: TPNS服务Android应用所属地域，详细说明参见 ModifyApplication 同名入参。
        :type TPNSAndroidRegion: str
        :param _SelfSmsAppId: 自主短信配置APPID
        :type SelfSmsAppId: str
        :param _SelfSmsAppKey: 自主短信配置APPKey
        :type SelfSmsAppKey: str
        :param _SelfSmsSign: 自主短信配置签名
        :type SelfSmsSign: str
        :param _SelfSmsTemplateId: 自主短信配置模板ID
        :type SelfSmsTemplateId: int
        :param _WechatNotifyStatus: 第三方小程序强提醒开关 0：关闭；1：开启
        :type WechatNotifyStatus: int
        :param _InterconnectionProducts: 互联互通产品ID列表
        :type InterconnectionProducts: str
        """
        self._IotAppID = None
        self._AppName = None
        self._Description = None
        self._DevMode = None
        self._IOSAppKey = None
        self._IOSAppSecret = None
        self._AndroidAppKey = None
        self._AndroidAppSecret = None
        self._Products = None
        self._CreateTime = None
        self._ProjectId = None
        self._PushSecretID = None
        self._PushSecretKey = None
        self._PushEnvironment = None
        self._MiniProgramAppKey = None
        self._MiniProgramAppSecret = None
        self._TPNSiOSAccessID = None
        self._TPNSiOSSecretKey = None
        self._TPNSiOSPushEnvironment = None
        self._TPNSAndroidAccessID = None
        self._TPNSAndroidSecretKey = None
        self._TPNSiOSRegion = None
        self._TPNSAndroidRegion = None
        self._SelfSmsAppId = None
        self._SelfSmsAppKey = None
        self._SelfSmsSign = None
        self._SelfSmsTemplateId = None
        self._WechatNotifyStatus = None
        self._InterconnectionProducts = None

    @property
    def IotAppID(self):
        r"""应用 ID
        :rtype: str
        """
        return self._IotAppID

    @IotAppID.setter
    def IotAppID(self, IotAppID):
        self._IotAppID = IotAppID

    @property
    def AppName(self):
        r"""应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Description(self):
        r"""应用说明
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DevMode(self):
        r"""开发模式
        :rtype: int
        """
        return self._DevMode

    @DevMode.setter
    def DevMode(self, DevMode):
        self._DevMode = DevMode

    @property
    def IOSAppKey(self):
        r"""iOS 平台 AppKey
        :rtype: str
        """
        return self._IOSAppKey

    @IOSAppKey.setter
    def IOSAppKey(self, IOSAppKey):
        self._IOSAppKey = IOSAppKey

    @property
    def IOSAppSecret(self):
        r"""iOS 平台 AppSecret
        :rtype: str
        """
        return self._IOSAppSecret

    @IOSAppSecret.setter
    def IOSAppSecret(self, IOSAppSecret):
        self._IOSAppSecret = IOSAppSecret

    @property
    def AndroidAppKey(self):
        r"""Android 平台 AppKey
        :rtype: str
        """
        return self._AndroidAppKey

    @AndroidAppKey.setter
    def AndroidAppKey(self, AndroidAppKey):
        self._AndroidAppKey = AndroidAppKey

    @property
    def AndroidAppSecret(self):
        r"""Android 平台 AppSecret
        :rtype: str
        """
        return self._AndroidAppSecret

    @AndroidAppSecret.setter
    def AndroidAppSecret(self, AndroidAppSecret):
        self._AndroidAppSecret = AndroidAppSecret

    @property
    def Products(self):
        r"""绑定的产品列表，数据为：ProdcutID 数组 JSON 序列化后的字符串
        :rtype: str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

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
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PushSecretID(self):
        r"""信鸽推送APP ID
        :rtype: str
        """
        return self._PushSecretID

    @PushSecretID.setter
    def PushSecretID(self, PushSecretID):
        self._PushSecretID = PushSecretID

    @property
    def PushSecretKey(self):
        r"""信鸽推送SECRET KEY
        :rtype: str
        """
        return self._PushSecretKey

    @PushSecretKey.setter
    def PushSecretKey(self, PushSecretKey):
        self._PushSecretKey = PushSecretKey

    @property
    def PushEnvironment(self):
        r"""iOS平台推送环境
        :rtype: str
        """
        return self._PushEnvironment

    @PushEnvironment.setter
    def PushEnvironment(self, PushEnvironment):
        self._PushEnvironment = PushEnvironment

    @property
    def MiniProgramAppKey(self):
        r"""小程序平台 AppKey
        :rtype: str
        """
        return self._MiniProgramAppKey

    @MiniProgramAppKey.setter
    def MiniProgramAppKey(self, MiniProgramAppKey):
        self._MiniProgramAppKey = MiniProgramAppKey

    @property
    def MiniProgramAppSecret(self):
        r"""小程序平台 AppSecret
        :rtype: str
        """
        return self._MiniProgramAppSecret

    @MiniProgramAppSecret.setter
    def MiniProgramAppSecret(self, MiniProgramAppSecret):
        self._MiniProgramAppSecret = MiniProgramAppSecret

    @property
    def TPNSiOSAccessID(self):
        r"""TPNS服务iOS应用AccessID，TPNS全称为腾讯移动推送（Tencent Push Notification Service），详见：https://cloud.tencent.com/document/product/548
        :rtype: str
        """
        return self._TPNSiOSAccessID

    @TPNSiOSAccessID.setter
    def TPNSiOSAccessID(self, TPNSiOSAccessID):
        self._TPNSiOSAccessID = TPNSiOSAccessID

    @property
    def TPNSiOSSecretKey(self):
        r"""TPNS服务iOS应用SecretKey
        :rtype: str
        """
        return self._TPNSiOSSecretKey

    @TPNSiOSSecretKey.setter
    def TPNSiOSSecretKey(self, TPNSiOSSecretKey):
        self._TPNSiOSSecretKey = TPNSiOSSecretKey

    @property
    def TPNSiOSPushEnvironment(self):
        r"""TPNS服务iOS应用推送环境
        :rtype: str
        """
        return self._TPNSiOSPushEnvironment

    @TPNSiOSPushEnvironment.setter
    def TPNSiOSPushEnvironment(self, TPNSiOSPushEnvironment):
        self._TPNSiOSPushEnvironment = TPNSiOSPushEnvironment

    @property
    def TPNSAndroidAccessID(self):
        r"""TPNS服务Android应用AccessID
        :rtype: str
        """
        return self._TPNSAndroidAccessID

    @TPNSAndroidAccessID.setter
    def TPNSAndroidAccessID(self, TPNSAndroidAccessID):
        self._TPNSAndroidAccessID = TPNSAndroidAccessID

    @property
    def TPNSAndroidSecretKey(self):
        r"""TPNS服务Android应用SecretKey
        :rtype: str
        """
        return self._TPNSAndroidSecretKey

    @TPNSAndroidSecretKey.setter
    def TPNSAndroidSecretKey(self, TPNSAndroidSecretKey):
        self._TPNSAndroidSecretKey = TPNSAndroidSecretKey

    @property
    def TPNSiOSRegion(self):
        r"""TPNS服务iOS应用所属地域，详细说明参见 ModifyApplication 同名入参。
        :rtype: str
        """
        return self._TPNSiOSRegion

    @TPNSiOSRegion.setter
    def TPNSiOSRegion(self, TPNSiOSRegion):
        self._TPNSiOSRegion = TPNSiOSRegion

    @property
    def TPNSAndroidRegion(self):
        r"""TPNS服务Android应用所属地域，详细说明参见 ModifyApplication 同名入参。
        :rtype: str
        """
        return self._TPNSAndroidRegion

    @TPNSAndroidRegion.setter
    def TPNSAndroidRegion(self, TPNSAndroidRegion):
        self._TPNSAndroidRegion = TPNSAndroidRegion

    @property
    def SelfSmsAppId(self):
        r"""自主短信配置APPID
        :rtype: str
        """
        return self._SelfSmsAppId

    @SelfSmsAppId.setter
    def SelfSmsAppId(self, SelfSmsAppId):
        self._SelfSmsAppId = SelfSmsAppId

    @property
    def SelfSmsAppKey(self):
        r"""自主短信配置APPKey
        :rtype: str
        """
        return self._SelfSmsAppKey

    @SelfSmsAppKey.setter
    def SelfSmsAppKey(self, SelfSmsAppKey):
        self._SelfSmsAppKey = SelfSmsAppKey

    @property
    def SelfSmsSign(self):
        r"""自主短信配置签名
        :rtype: str
        """
        return self._SelfSmsSign

    @SelfSmsSign.setter
    def SelfSmsSign(self, SelfSmsSign):
        self._SelfSmsSign = SelfSmsSign

    @property
    def SelfSmsTemplateId(self):
        r"""自主短信配置模板ID
        :rtype: int
        """
        return self._SelfSmsTemplateId

    @SelfSmsTemplateId.setter
    def SelfSmsTemplateId(self, SelfSmsTemplateId):
        self._SelfSmsTemplateId = SelfSmsTemplateId

    @property
    def WechatNotifyStatus(self):
        r"""第三方小程序强提醒开关 0：关闭；1：开启
        :rtype: int
        """
        return self._WechatNotifyStatus

    @WechatNotifyStatus.setter
    def WechatNotifyStatus(self, WechatNotifyStatus):
        self._WechatNotifyStatus = WechatNotifyStatus

    @property
    def InterconnectionProducts(self):
        r"""互联互通产品ID列表
        :rtype: str
        """
        return self._InterconnectionProducts

    @InterconnectionProducts.setter
    def InterconnectionProducts(self, InterconnectionProducts):
        self._InterconnectionProducts = InterconnectionProducts


    def _deserialize(self, params):
        self._IotAppID = params.get("IotAppID")
        self._AppName = params.get("AppName")
        self._Description = params.get("Description")
        self._DevMode = params.get("DevMode")
        self._IOSAppKey = params.get("IOSAppKey")
        self._IOSAppSecret = params.get("IOSAppSecret")
        self._AndroidAppKey = params.get("AndroidAppKey")
        self._AndroidAppSecret = params.get("AndroidAppSecret")
        self._Products = params.get("Products")
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._PushSecretID = params.get("PushSecretID")
        self._PushSecretKey = params.get("PushSecretKey")
        self._PushEnvironment = params.get("PushEnvironment")
        self._MiniProgramAppKey = params.get("MiniProgramAppKey")
        self._MiniProgramAppSecret = params.get("MiniProgramAppSecret")
        self._TPNSiOSAccessID = params.get("TPNSiOSAccessID")
        self._TPNSiOSSecretKey = params.get("TPNSiOSSecretKey")
        self._TPNSiOSPushEnvironment = params.get("TPNSiOSPushEnvironment")
        self._TPNSAndroidAccessID = params.get("TPNSAndroidAccessID")
        self._TPNSAndroidSecretKey = params.get("TPNSAndroidSecretKey")
        self._TPNSiOSRegion = params.get("TPNSiOSRegion")
        self._TPNSAndroidRegion = params.get("TPNSAndroidRegion")
        self._SelfSmsAppId = params.get("SelfSmsAppId")
        self._SelfSmsAppKey = params.get("SelfSmsAppKey")
        self._SelfSmsSign = params.get("SelfSmsSign")
        self._SelfSmsTemplateId = params.get("SelfSmsTemplateId")
        self._WechatNotifyStatus = params.get("WechatNotifyStatus")
        self._InterconnectionProducts = params.get("InterconnectionProducts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseServiceNumInfo(AbstractModel):
    r"""增值服务数量统计

    """

    def __init__(self):
        r"""
        :param _LicenseType: 服务类型
        :type LicenseType: str
        :param _TotalNum: 授权总数
        :type TotalNum: int
        :param _UsedNum: 已使用授权数
        :type UsedNum: int
        :param _TWeCallLicense: TWeCall激活码
        :type TWeCallLicense: list of TWeCallLicenseInfo
        """
        self._LicenseType = None
        self._TotalNum = None
        self._UsedNum = None
        self._TWeCallLicense = None

    @property
    def LicenseType(self):
        r"""服务类型
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def TotalNum(self):
        r"""授权总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def UsedNum(self):
        r"""已使用授权数
        :rtype: int
        """
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum

    @property
    def TWeCallLicense(self):
        r"""TWeCall激活码
        :rtype: list of TWeCallLicenseInfo
        """
        return self._TWeCallLicense

    @TWeCallLicense.setter
    def TWeCallLicense(self, TWeCallLicense):
        self._TWeCallLicense = TWeCallLicense


    def _deserialize(self, params):
        self._LicenseType = params.get("LicenseType")
        self._TotalNum = params.get("TotalNum")
        self._UsedNum = params.get("UsedNum")
        if params.get("TWeCallLicense") is not None:
            self._TWeCallLicense = []
            for item in params.get("TWeCallLicense"):
                obj = TWeCallLicenseInfo()
                obj._deserialize(item)
                self._TWeCallLicense.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventHistoryRequest(AbstractModel):
    r"""ListEventHistory请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Type(self):
        r"""搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        r"""起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        r"""搜索上下文, 用作查询游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        r"""单次获取的历史数据项目的最大数量, 缺省10
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        r"""事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :rtype: str
        """
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
    r"""ListEventHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param _Total: 搜索结果数量
        :type Total: int
        :param _Listover: 搜索结果是否已经结束
        :type Listover: bool
        :param _EventHistory: 搜集结果集
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
        r"""搜索上下文, 用作查询游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Total(self):
        r"""搜索结果数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Listover(self):
        r"""搜索结果是否已经结束
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def EventHistory(self):
        r"""搜集结果集
        :rtype: list of EventHistoryItem
        """
        return self._EventHistory

    @EventHistory.setter
    def EventHistory(self, EventHistory):
        self._EventHistory = EventHistory

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
    r"""ListFirmwares请求参数结构体

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
        r"""获取的页数
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""分页的大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Filters(self):
        r"""搜索过滤条件
        :rtype: list of SearchKeyword
        """
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
    r"""ListFirmwares返回参数结构体

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
        r"""固件总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Firmwares(self):
        r"""固件列表
        :rtype: list of FirmwareInfo
        """
        return self._Firmwares

    @Firmwares.setter
    def Firmwares(self, Firmwares):
        self._Firmwares = Firmwares

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Firmwares") is not None:
            self._Firmwares = []
            for item in params.get("Firmwares"):
                obj = FirmwareInfo()
                obj._deserialize(item)
                self._Firmwares.append(obj)
        self._RequestId = params.get("RequestId")


class ListOtaModulesRequest(AbstractModel):
    r"""ListOtaModules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 获取的页数
        :type PageNum: int
        :param _PageSize: 分页的大小
        :type PageSize: int
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._PageNum = None
        self._PageSize = None
        self._Filters = None

    @property
    def PageNum(self):
        r"""获取的页数
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""分页的大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""搜索过滤条件
        :rtype: list of SearchKeyword
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
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
        


class ListOtaModulesResponse(AbstractModel):
    r"""ListOtaModules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 固件总数
        :type TotalCount: int
        :param _Modules: 固件列表
        :type Modules: list of OtaModuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Modules = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""固件总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Modules(self):
        r"""固件列表
        :rtype: list of OtaModuleInfo
        """
        return self._Modules

    @Modules.setter
    def Modules(self, Modules):
        self._Modules = Modules

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Modules") is not None:
            self._Modules = []
            for item in params.get("Modules"):
                obj = OtaModuleInfo()
                obj._deserialize(item)
                self._Modules.append(obj)
        self._RequestId = params.get("RequestId")


class ListProductOtaModulesRequest(AbstractModel):
    r"""ListProductOtaModules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        """
        self._ProductID = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListProductOtaModulesResponse(AbstractModel):
    r"""ListProductOtaModules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Modules: 固件列表
        :type Modules: list of OtaModuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Modules = None
        self._RequestId = None

    @property
    def Modules(self):
        r"""固件列表
        :rtype: list of OtaModuleInfo
        """
        return self._Modules

    @Modules.setter
    def Modules(self, Modules):
        self._Modules = Modules

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
        if params.get("Modules") is not None:
            self._Modules = []
            for item in params.get("Modules"):
                obj = OtaModuleInfo()
                obj._deserialize(item)
                self._Modules.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopicPolicyRequest(AbstractModel):
    r"""ListTopicPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品ID
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
        


class ListTopicPolicyResponse(AbstractModel):
    r"""ListTopicPolicy返回参数结构体

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
        r"""Topic列表
        :rtype: list of TopicItem
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicItem()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._RequestId = params.get("RequestId")


class LoRaFrequencyEntry(AbstractModel):
    r"""LoRa自定义频点信息

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
        r"""频点唯一ID
        :rtype: str
        """
        return self._FreqId

    @FreqId.setter
    def FreqId(self, FreqId):
        self._FreqId = FreqId

    @property
    def FreqName(self):
        r"""频点名称
        :rtype: str
        """
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def Description(self):
        r"""频点描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ChannelsDataUp(self):
        r"""数据上行信道
        :rtype: list of int non-negative
        """
        return self._ChannelsDataUp

    @ChannelsDataUp.setter
    def ChannelsDataUp(self, ChannelsDataUp):
        self._ChannelsDataUp = ChannelsDataUp

    @property
    def ChannelsDataRX1(self):
        r"""数据下行信道RX1
        :rtype: list of int non-negative
        """
        return self._ChannelsDataRX1

    @ChannelsDataRX1.setter
    def ChannelsDataRX1(self, ChannelsDataRX1):
        self._ChannelsDataRX1 = ChannelsDataRX1

    @property
    def ChannelsDataRX2(self):
        r"""数据下行信道RX2
        :rtype: list of int non-negative
        """
        return self._ChannelsDataRX2

    @ChannelsDataRX2.setter
    def ChannelsDataRX2(self, ChannelsDataRX2):
        self._ChannelsDataRX2 = ChannelsDataRX2

    @property
    def ChannelsJoinUp(self):
        r"""入网上行信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinUp

    @ChannelsJoinUp.setter
    def ChannelsJoinUp(self, ChannelsJoinUp):
        self._ChannelsJoinUp = ChannelsJoinUp

    @property
    def ChannelsJoinRX1(self):
        r"""入网下行RX1信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinRX1

    @ChannelsJoinRX1.setter
    def ChannelsJoinRX1(self, ChannelsJoinRX1):
        self._ChannelsJoinRX1 = ChannelsJoinRX1

    @property
    def ChannelsJoinRX2(self):
        r"""入网下行RX2信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinRX2

    @ChannelsJoinRX2.setter
    def ChannelsJoinRX2(self, ChannelsJoinRX2):
        self._ChannelsJoinRX2 = ChannelsJoinRX2

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
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
    r"""LoRa 网关信息

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
        r"""LoRa 网关Id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def IsPublic(self):
        r"""是否是公开网关
        :rtype: bool
        """
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def Description(self):
        r"""网关描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""网关名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        r"""网关位置信息
        :rtype: str
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def PositionDetails(self):
        r"""网关位置详情
        :rtype: str
        """
        return self._PositionDetails

    @PositionDetails.setter
    def PositionDetails(self, PositionDetails):
        self._PositionDetails = PositionDetails

    @property
    def Location(self):
        r"""LoRa 网关位置坐标
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def UpdatedAt(self):
        r"""最后更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def LastSeenAt(self):
        r"""最后上报时间
        :rtype: str
        """
        return self._LastSeenAt

    @LastSeenAt.setter
    def LastSeenAt(self, LastSeenAt):
        self._LastSeenAt = LastSeenAt

    @property
    def FrequencyId(self):
        r"""频点ID
        :rtype: str
        """
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
    r"""网关坐标

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
        r"""纬度
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Longitude(self):
        r"""精度
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Accuracy(self):
        r"""准确度
        :rtype: float
        """
        return self._Accuracy

    @Accuracy.setter
    def Accuracy(self, Accuracy):
        self._Accuracy = Accuracy

    @property
    def Altitude(self):
        r"""海拔
        :rtype: float
        """
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
        


class ModifyApplicationRequest(AbstractModel):
    r"""ModifyApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IotAppID: 应用ID
        :type IotAppID: str
        :param _AppName: 应用名称
        :type AppName: str
        :param _Description: 应用说明
        :type Description: str
        :param _Products: 关联的产品
        :type Products: str
        :param _PushSecretID: 信鸽推送APP ID
        :type PushSecretID: str
        :param _PushSecretKey: 信鸽推送SECRET KEY
        :type PushSecretKey: str
        :param _PushEnvironment: iOS平台推送环境
        :type PushEnvironment: str
        :param _TPNSiOSAccessID: TPNS服务iOS应用AccessID，TPNS全称为腾讯移动推送（Tencent Push Notification Service），详见：https://cloud.tencent.com/document/product/548
        :type TPNSiOSAccessID: str
        :param _TPNSiOSSecretKey: TPNS服务iOS应用SecretKey
        :type TPNSiOSSecretKey: str
        :param _TPNSiOSPushEnvironment: TPNS服务iOS应用推送环境
        :type TPNSiOSPushEnvironment: str
        :param _TPNSAndroidAccessID: TPNS服务Android应用AccessID
        :type TPNSAndroidAccessID: str
        :param _TPNSAndroidSecretKey: TPNS服务Android应用SecretKey
        :type TPNSAndroidSecretKey: str
        :param _TPNSiOSRegion: TPNS服务iOS应用所属地域，广州：ap-guangzhou，上海：ap-shanghai，中国香港：ap-hongkong，新加坡：ap-singapore。
        :type TPNSiOSRegion: str
        :param _TPNSAndroidRegion: TPNS服务Android应用所属地域，广州：ap-guangzhou，上海：ap-shanghai，中国香港：ap-hongkong，新加坡：ap-singapore。
        :type TPNSAndroidRegion: str
        :param _TurnKeySwitch: TurnKey小程序托管
        :type TurnKeySwitch: int
        """
        self._IotAppID = None
        self._AppName = None
        self._Description = None
        self._Products = None
        self._PushSecretID = None
        self._PushSecretKey = None
        self._PushEnvironment = None
        self._TPNSiOSAccessID = None
        self._TPNSiOSSecretKey = None
        self._TPNSiOSPushEnvironment = None
        self._TPNSAndroidAccessID = None
        self._TPNSAndroidSecretKey = None
        self._TPNSiOSRegion = None
        self._TPNSAndroidRegion = None
        self._TurnKeySwitch = None

    @property
    def IotAppID(self):
        r"""应用ID
        :rtype: str
        """
        return self._IotAppID

    @IotAppID.setter
    def IotAppID(self, IotAppID):
        self._IotAppID = IotAppID

    @property
    def AppName(self):
        r"""应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Description(self):
        r"""应用说明
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Products(self):
        r"""关联的产品
        :rtype: str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def PushSecretID(self):
        r"""信鸽推送APP ID
        :rtype: str
        """
        return self._PushSecretID

    @PushSecretID.setter
    def PushSecretID(self, PushSecretID):
        self._PushSecretID = PushSecretID

    @property
    def PushSecretKey(self):
        r"""信鸽推送SECRET KEY
        :rtype: str
        """
        return self._PushSecretKey

    @PushSecretKey.setter
    def PushSecretKey(self, PushSecretKey):
        self._PushSecretKey = PushSecretKey

    @property
    def PushEnvironment(self):
        r"""iOS平台推送环境
        :rtype: str
        """
        return self._PushEnvironment

    @PushEnvironment.setter
    def PushEnvironment(self, PushEnvironment):
        self._PushEnvironment = PushEnvironment

    @property
    def TPNSiOSAccessID(self):
        r"""TPNS服务iOS应用AccessID，TPNS全称为腾讯移动推送（Tencent Push Notification Service），详见：https://cloud.tencent.com/document/product/548
        :rtype: str
        """
        return self._TPNSiOSAccessID

    @TPNSiOSAccessID.setter
    def TPNSiOSAccessID(self, TPNSiOSAccessID):
        self._TPNSiOSAccessID = TPNSiOSAccessID

    @property
    def TPNSiOSSecretKey(self):
        r"""TPNS服务iOS应用SecretKey
        :rtype: str
        """
        return self._TPNSiOSSecretKey

    @TPNSiOSSecretKey.setter
    def TPNSiOSSecretKey(self, TPNSiOSSecretKey):
        self._TPNSiOSSecretKey = TPNSiOSSecretKey

    @property
    def TPNSiOSPushEnvironment(self):
        r"""TPNS服务iOS应用推送环境
        :rtype: str
        """
        return self._TPNSiOSPushEnvironment

    @TPNSiOSPushEnvironment.setter
    def TPNSiOSPushEnvironment(self, TPNSiOSPushEnvironment):
        self._TPNSiOSPushEnvironment = TPNSiOSPushEnvironment

    @property
    def TPNSAndroidAccessID(self):
        r"""TPNS服务Android应用AccessID
        :rtype: str
        """
        return self._TPNSAndroidAccessID

    @TPNSAndroidAccessID.setter
    def TPNSAndroidAccessID(self, TPNSAndroidAccessID):
        self._TPNSAndroidAccessID = TPNSAndroidAccessID

    @property
    def TPNSAndroidSecretKey(self):
        r"""TPNS服务Android应用SecretKey
        :rtype: str
        """
        return self._TPNSAndroidSecretKey

    @TPNSAndroidSecretKey.setter
    def TPNSAndroidSecretKey(self, TPNSAndroidSecretKey):
        self._TPNSAndroidSecretKey = TPNSAndroidSecretKey

    @property
    def TPNSiOSRegion(self):
        r"""TPNS服务iOS应用所属地域，广州：ap-guangzhou，上海：ap-shanghai，中国香港：ap-hongkong，新加坡：ap-singapore。
        :rtype: str
        """
        return self._TPNSiOSRegion

    @TPNSiOSRegion.setter
    def TPNSiOSRegion(self, TPNSiOSRegion):
        self._TPNSiOSRegion = TPNSiOSRegion

    @property
    def TPNSAndroidRegion(self):
        r"""TPNS服务Android应用所属地域，广州：ap-guangzhou，上海：ap-shanghai，中国香港：ap-hongkong，新加坡：ap-singapore。
        :rtype: str
        """
        return self._TPNSAndroidRegion

    @TPNSAndroidRegion.setter
    def TPNSAndroidRegion(self, TPNSAndroidRegion):
        self._TPNSAndroidRegion = TPNSAndroidRegion

    @property
    def TurnKeySwitch(self):
        r"""TurnKey小程序托管
        :rtype: int
        """
        return self._TurnKeySwitch

    @TurnKeySwitch.setter
    def TurnKeySwitch(self, TurnKeySwitch):
        self._TurnKeySwitch = TurnKeySwitch


    def _deserialize(self, params):
        self._IotAppID = params.get("IotAppID")
        self._AppName = params.get("AppName")
        self._Description = params.get("Description")
        self._Products = params.get("Products")
        self._PushSecretID = params.get("PushSecretID")
        self._PushSecretKey = params.get("PushSecretKey")
        self._PushEnvironment = params.get("PushEnvironment")
        self._TPNSiOSAccessID = params.get("TPNSiOSAccessID")
        self._TPNSiOSSecretKey = params.get("TPNSiOSSecretKey")
        self._TPNSiOSPushEnvironment = params.get("TPNSiOSPushEnvironment")
        self._TPNSAndroidAccessID = params.get("TPNSAndroidAccessID")
        self._TPNSAndroidSecretKey = params.get("TPNSAndroidSecretKey")
        self._TPNSiOSRegion = params.get("TPNSiOSRegion")
        self._TPNSAndroidRegion = params.get("TPNSAndroidRegion")
        self._TurnKeySwitch = params.get("TurnKeySwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    r"""ModifyApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Application: 应用信息
        :type Application: :class:`tencentcloud.iotexplorer.v20190423.models.IotApplication`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Application = None
        self._RequestId = None

    @property
    def Application(self):
        r"""应用信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.IotApplication`
        """
        return self._Application

    @Application.setter
    def Application(self, Application):
        self._Application = Application

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
        if params.get("Application") is not None:
            self._Application = IotApplication()
            self._Application._deserialize(params.get("Application"))
        self._RequestId = params.get("RequestId")


class ModifyCloudStorageAIServiceCallbackRequest(AbstractModel):
    r"""ModifyCloudStorageAIServiceCallback请求参数结构体

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
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        r"""推送类型。可选值：
- `http`：HTTP 回调
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallbackUrl(self):
        r"""HTTP 回调 URL
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def CallbackToken(self):
        r"""HTTP 回调鉴权 Token
        :rtype: str
        """
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
    r"""ModifyCloudStorageAIServiceCallback返回参数结构体

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


class ModifyCloudStorageAIServiceRequest(AbstractModel):
    r"""ModifyCloudStorageAIService请求参数结构体

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
- `SimpleHighlight`：TrueX SimpleHighlight
        :type ServiceType: str
        :param _Enabled: 视频分析启用状态
        :type Enabled: bool
        :param _ROI: 视频分析识别区域
        :type ROI: str
        :param _Config: 视频分析配置参数
        :type Config: str
        :param _SHLConfig: SimpleHighlight 算法配置参数
        :type SHLConfig: :class:`tencentcloud.iotexplorer.v20190423.models.DiarySHLConfig`
        """
        self._ProductId = None
        self._DeviceName = None
        self._ServiceType = None
        self._Enabled = None
        self._ROI = None
        self._Config = None
        self._SHLConfig = None

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
- `SimpleHighlight`：TrueX SimpleHighlight
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Enabled(self):
        r"""视频分析启用状态
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ROI(self):
        r"""视频分析识别区域
        :rtype: str
        """
        return self._ROI

    @ROI.setter
    def ROI(self, ROI):
        self._ROI = ROI

    @property
    def Config(self):
        r"""视频分析配置参数
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def SHLConfig(self):
        r"""SimpleHighlight 算法配置参数
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DiarySHLConfig`
        """
        return self._SHLConfig

    @SHLConfig.setter
    def SHLConfig(self, SHLConfig):
        self._SHLConfig = SHLConfig


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ServiceType = params.get("ServiceType")
        self._Enabled = params.get("Enabled")
        self._ROI = params.get("ROI")
        self._Config = params.get("Config")
        if params.get("SHLConfig") is not None:
            self._SHLConfig = DiarySHLConfig()
            self._SHLConfig._deserialize(params.get("SHLConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudStorageAIServiceResponse(AbstractModel):
    r"""ModifyCloudStorageAIService返回参数结构体

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


class ModifyFenceBindRequest(AbstractModel):
    r"""ModifyFenceBind请求参数结构体

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
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Items(self):
        r"""围栏绑定的产品列表
        :rtype: list of FenceBindProductItem
        """
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
    r"""ModifyFenceBind返回参数结构体

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


class ModifyLoRaFrequencyRequest(AbstractModel):
    r"""ModifyLoRaFrequency请求参数结构体

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
        r"""频点唯一ID
        :rtype: str
        """
        return self._FreqId

    @FreqId.setter
    def FreqId(self, FreqId):
        self._FreqId = FreqId

    @property
    def FreqName(self):
        r"""频点名称
        :rtype: str
        """
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def Description(self):
        r"""频点描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ChannelsDataUp(self):
        r"""数据上行信道
        :rtype: list of int non-negative
        """
        return self._ChannelsDataUp

    @ChannelsDataUp.setter
    def ChannelsDataUp(self, ChannelsDataUp):
        self._ChannelsDataUp = ChannelsDataUp

    @property
    def ChannelsDataRX1(self):
        r"""数据下行信道RX1
        :rtype: list of int non-negative
        """
        return self._ChannelsDataRX1

    @ChannelsDataRX1.setter
    def ChannelsDataRX1(self, ChannelsDataRX1):
        self._ChannelsDataRX1 = ChannelsDataRX1

    @property
    def ChannelsDataRX2(self):
        r"""数据下行信道RX2
        :rtype: list of int non-negative
        """
        return self._ChannelsDataRX2

    @ChannelsDataRX2.setter
    def ChannelsDataRX2(self, ChannelsDataRX2):
        self._ChannelsDataRX2 = ChannelsDataRX2

    @property
    def ChannelsJoinUp(self):
        r"""入网上行信道
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinUp

    @ChannelsJoinUp.setter
    def ChannelsJoinUp(self, ChannelsJoinUp):
        self._ChannelsJoinUp = ChannelsJoinUp

    @property
    def ChannelsJoinRX1(self):
        r"""入网下行信道RX1
        :rtype: list of int non-negative
        """
        return self._ChannelsJoinRX1

    @ChannelsJoinRX1.setter
    def ChannelsJoinRX1(self, ChannelsJoinRX1):
        self._ChannelsJoinRX1 = ChannelsJoinRX1

    @property
    def ChannelsJoinRX2(self):
        r"""入网下行信道RX2
        :rtype: list of int non-negative
        """
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
    r"""ModifyLoRaFrequency返回参数结构体

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
        r"""频点信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaFrequencyEntry`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = LoRaFrequencyEntry()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyLoRaGatewayRequest(AbstractModel):
    r"""ModifyLoRaGateway请求参数结构体

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
        r"""描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GatewayId(self):
        r"""LoRa网关Id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Location(self):
        r"""LoRa网关位置坐标
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Name(self):
        r"""LoRa网关名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsPublic(self):
        r"""是否公开可见
        :rtype: bool
        """
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def Position(self):
        r"""位置信息
        :rtype: str
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def PositionDetails(self):
        r"""位置详情
        :rtype: str
        """
        return self._PositionDetails

    @PositionDetails.setter
    def PositionDetails(self, PositionDetails):
        self._PositionDetails = PositionDetails

    @property
    def FrequencyId(self):
        r"""频点ID
        :rtype: str
        """
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
    r"""ModifyLoRaGateway返回参数结构体

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
        r"""返回网关数据
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.LoRaGatewayItem`
        """
        return self._Gateway

    @Gateway.setter
    def Gateway(self, Gateway):
        self._Gateway = Gateway

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
        if params.get("Gateway") is not None:
            self._Gateway = LoRaGatewayItem()
            self._Gateway._deserialize(params.get("Gateway"))
        self._RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    r"""ModifyModelDefinition请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelSchema(self):
        r"""数据模板定义
        :rtype: str
        """
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
    r"""ModifyModelDefinition返回参数结构体

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


class ModifyPositionFenceRequest(AbstractModel):
    r"""ModifyPositionFence请求参数结构体

    """


class ModifyPositionFenceResponse(AbstractModel):
    r"""ModifyPositionFence返回参数结构体

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


class ModifyPositionSpaceRequest(AbstractModel):
    r"""ModifyPositionSpace请求参数结构体

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
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        r"""位置空间名称
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def AuthorizeType(self):
        r"""授权类型
        :rtype: int
        """
        return self._AuthorizeType

    @AuthorizeType.setter
    def AuthorizeType(self, AuthorizeType):
        self._AuthorizeType = AuthorizeType

    @property
    def ProductIdList(self):
        r"""产品列表
        :rtype: list of str
        """
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def Description(self):
        r"""位置空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Icon(self):
        r"""缩略图
        :rtype: str
        """
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
    r"""ModifyPositionSpace返回参数结构体

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


class ModifyProductCloudStorageAIServiceRequest(AbstractModel):
    r"""ModifyProductCloudStorageAIService请求参数结构体

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
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Enabled(self):
        r"""开通状态
        :rtype: bool
        """
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
    r"""ModifyProductCloudStorageAIService返回参数结构体

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


class ModifyProjectRequest(AbstractModel):
    r"""ModifyProject请求参数结构体

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        r"""项目描述
        :rtype: str
        """
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
    r"""ModifyProject返回参数结构体

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
        r"""项目详情
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

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
        if params.get("Project") is not None:
            self._Project = ProjectEntry()
            self._Project._deserialize(params.get("Project"))
        self._RequestId = params.get("RequestId")


class ModifySpacePropertyRequest(AbstractModel):
    r"""ModifySpaceProperty请求参数结构体

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
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Data(self):
        r"""产品属性
        :rtype: str
        """
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
    r"""ModifySpaceProperty返回参数结构体

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


class ModifyStudioProductRequest(AbstractModel):
    r"""ModifyStudioProduct请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductDesc(self):
        r"""产品描述
        :rtype: str
        """
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def ModuleId(self):
        r"""模型ID
        :rtype: int
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def EnableProductScript(self):
        r"""是否打开二进制转Json功能, 取值为字符串 true/false
        :rtype: str
        """
        return self._EnableProductScript

    @EnableProductScript.setter
    def EnableProductScript(self, EnableProductScript):
        self._EnableProductScript = EnableProductScript

    @property
    def BindStrategy(self):
        r"""传1或者2；1代表强踢，2代表非强踢。传其它值不做任何处理
        :rtype: int
        """
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
    r"""ModifyStudioProduct返回参数结构体

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
        r"""产品描述
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

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
        if params.get("Product") is not None:
            self._Product = ProductEntry()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class ModifyTWeSeeConfigRequest(AbstractModel):
    r"""ModifyTWeSeeConfig请求参数结构体

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
        :param _EnableSummary: 是否开启视频摘要，不传则不修改
        :type EnableSummary: bool
        :param _EnableSearch: 是否开启视频搜索，不传则不修改
        :type EnableSearch: bool
        :param _Config: 配置参数，不传则不修改
        :type Config: str
        :param _SummaryConfig: 视频摘要配置参数，不传则不修改
        :type SummaryConfig: :class:`tencentcloud.iotexplorer.v20190423.models.VisionSummaryConfig`
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None
        self._ChannelId = None
        self._EnableSummary = None
        self._EnableSearch = None
        self._Config = None
        self._SummaryConfig = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def EnableSummary(self):
        r"""是否开启视频摘要，不传则不修改
        :rtype: bool
        """
        return self._EnableSummary

    @EnableSummary.setter
    def EnableSummary(self, EnableSummary):
        self._EnableSummary = EnableSummary

    @property
    def EnableSearch(self):
        r"""是否开启视频搜索，不传则不修改
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch

    @property
    def Config(self):
        r"""配置参数，不传则不修改
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def SummaryConfig(self):
        r"""视频摘要配置参数，不传则不修改
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionSummaryConfig`
        """
        return self._SummaryConfig

    @SummaryConfig.setter
    def SummaryConfig(self, SummaryConfig):
        self._SummaryConfig = SummaryConfig


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        self._EnableSummary = params.get("EnableSummary")
        self._EnableSearch = params.get("EnableSearch")
        self._Config = params.get("Config")
        if params.get("SummaryConfig") is not None:
            self._SummaryConfig = VisionSummaryConfig()
            self._SummaryConfig._deserialize(params.get("SummaryConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTWeSeeConfigResponse(AbstractModel):
    r"""ModifyTWeSeeConfig返回参数结构体

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


class ModifyTWeTalkProductConfigRequest(AbstractModel):
    r"""ModifyTWeTalkProductConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _SystemPrompt: 系统提示词
        :type SystemPrompt: str
        :param _GreetingMessage: 欢迎语
        :type GreetingMessage: str
        :param _VoiceType: 音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :type VoiceType: int
        :param _FastVoiceType: 复刻音色
        :type FastVoiceType: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        """
        self._ProductId = None
        self._SystemPrompt = None
        self._GreetingMessage = None
        self._VoiceType = None
        self._FastVoiceType = None
        self._TargetLanguage = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def SystemPrompt(self):
        r"""系统提示词
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt

    @property
    def GreetingMessage(self):
        r"""欢迎语
        :rtype: str
        """
        return self._GreetingMessage

    @GreetingMessage.setter
    def GreetingMessage(self, GreetingMessage):
        self._GreetingMessage = GreetingMessage

    @property
    def VoiceType(self):
        r"""音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def FastVoiceType(self):
        r"""复刻音色
        :rtype: str
        """
        return self._FastVoiceType

    @FastVoiceType.setter
    def FastVoiceType(self, FastVoiceType):
        self._FastVoiceType = FastVoiceType

    @property
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._SystemPrompt = params.get("SystemPrompt")
        self._GreetingMessage = params.get("GreetingMessage")
        self._VoiceType = params.get("VoiceType")
        self._FastVoiceType = params.get("FastVoiceType")
        self._TargetLanguage = params.get("TargetLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTWeTalkProductConfigResponse(AbstractModel):
    r"""ModifyTWeTalkProductConfig返回参数结构体

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


class ModifyTWeTalkProductConfigV2Request(AbstractModel):
    r"""ModifyTWeTalkProductConfigV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        :param _ConfigName: 名称
        :type ConfigName: str
        :param _BasicConfig: 系统基础配置，当需要使用系统三段式配置时配置。
        :type BasicConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkBasicConfigInfo`
        :param _STTConfig: 自定义语音识别配置
        :type STTConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkSTTConfigInfo`
        :param _LLMConfig: 自定义大模型配置
        :type LLMConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkLLMConfigInfo`
        :param _TTSConfig: 语音合成配置
        :type TTSConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkTTSConfigInfo`
        :param _ConversationConfig: 会话配置
        :type ConversationConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkConversationConfigInfo`
        """
        self._ProductId = None
        self._DeviceName = None
        self._TargetLanguage = None
        self._ConfigName = None
        self._BasicConfig = None
        self._STTConfig = None
        self._LLMConfig = None
        self._TTSConfig = None
        self._ConversationConfig = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def ConfigName(self):
        r"""名称
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def BasicConfig(self):
        r"""系统基础配置，当需要使用系统三段式配置时配置。
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkBasicConfigInfo`
        """
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def STTConfig(self):
        r"""自定义语音识别配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkSTTConfigInfo`
        """
        return self._STTConfig

    @STTConfig.setter
    def STTConfig(self, STTConfig):
        self._STTConfig = STTConfig

    @property
    def LLMConfig(self):
        r"""自定义大模型配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkLLMConfigInfo`
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""语音合成配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkTTSConfigInfo`
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def ConversationConfig(self):
        r"""会话配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkConversationConfigInfo`
        """
        return self._ConversationConfig

    @ConversationConfig.setter
    def ConversationConfig(self, ConversationConfig):
        self._ConversationConfig = ConversationConfig


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._TargetLanguage = params.get("TargetLanguage")
        self._ConfigName = params.get("ConfigName")
        if params.get("BasicConfig") is not None:
            self._BasicConfig = TalkBasicConfigInfo()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("STTConfig") is not None:
            self._STTConfig = TalkSTTConfigInfo()
            self._STTConfig._deserialize(params.get("STTConfig"))
        if params.get("LLMConfig") is not None:
            self._LLMConfig = TalkLLMConfigInfo()
            self._LLMConfig._deserialize(params.get("LLMConfig"))
        if params.get("TTSConfig") is not None:
            self._TTSConfig = TalkTTSConfigInfo()
            self._TTSConfig._deserialize(params.get("TTSConfig"))
        if params.get("ConversationConfig") is not None:
            self._ConversationConfig = TalkConversationConfigInfo()
            self._ConversationConfig._deserialize(params.get("ConversationConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTWeTalkProductConfigV2Response(AbstractModel):
    r"""ModifyTWeTalkProductConfigV2返回参数结构体

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


class ModifyTopicPolicyRequest(AbstractModel):
    r"""ModifyTopicPolicy请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        r"""更新前Topic名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def NewTopicName(self):
        r"""更新后Topic名
        :rtype: str
        """
        return self._NewTopicName

    @NewTopicName.setter
    def NewTopicName(self, NewTopicName):
        self._NewTopicName = NewTopicName

    @property
    def Privilege(self):
        r"""Topic权限
        :rtype: int
        """
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
    r"""ModifyTopicPolicy返回参数结构体

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


class ModifyTopicRuleRequest(AbstractModel):
    r"""ModifyTopicRule请求参数结构体

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
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def TopicRulePayload(self):
        r"""替换的规则包体
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TopicRulePayload`
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
        


class ModifyTopicRuleResponse(AbstractModel):
    r"""ModifyTopicRule返回参数结构体

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


class OtaModuleInfo(AbstractModel):
    r"""升级包类型详细信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 模块创建时间
        :type CreateTime: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _Name: 模块名称
        :type Name: str
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FwType: 模块类型
        :type FwType: str
        :param _IsBuildIn: 是否系统内置升级包类型
        :type IsBuildIn: bool
        :param _Remark: 模块描述
        :type Remark: str
        """
        self._CreateTime = None
        self._ProductName = None
        self._Name = None
        self._ProductID = None
        self._FwType = None
        self._IsBuildIn = None
        self._Remark = None

    @property
    def CreateTime(self):
        r"""模块创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        r"""模块名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FwType(self):
        r"""模块类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def IsBuildIn(self):
        r"""是否系统内置升级包类型
        :rtype: bool
        """
        return self._IsBuildIn

    @IsBuildIn.setter
    def IsBuildIn(self, IsBuildIn):
        self._IsBuildIn = IsBuildIn

    @property
    def Remark(self):
        r"""模块描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProductName = params.get("ProductName")
        self._Name = params.get("Name")
        self._ProductID = params.get("ProductID")
        self._FwType = params.get("FwType")
        self._IsBuildIn = params.get("IsBuildIn")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageConsumeStat(AbstractModel):
    r"""云存套餐包消耗统计

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
        r"""云存套餐包id
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        r"""云存套餐包名称
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Cnt(self):
        r"""消耗个数
        :rtype: int
        """
        return self._Cnt

    @Cnt.setter
    def Cnt(self, Cnt):
        self._Cnt = Cnt

    @property
    def Price(self):
        r"""套餐包单价，单位分
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Source(self):
        r"""消耗来源，1预付费
        :rtype: int
        """
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
    r"""套餐包消耗任务列表

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
        r"""任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CreateTime(self):
        r"""任务创始时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        r"""任务状态，1待处理，2处理中，3已完成
        :rtype: int
        """
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
    r"""结构体（PackageInfo）记录了设备拥有的有效套餐信息，包括云存开启状态、云存类型、云存回看时长、云存套餐过期时间

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
        :type CreatedAt: int
        :param _UpdatedAt: 云存套餐更新时间
        :type UpdatedAt: int
        :param _PackageId: 套餐id
        :type PackageId: str
        :param _OrderId: 订单id
        :type OrderId: str
        :param _ChannelId: 通道id
        :type ChannelId: int
        :param _CSUserId: 用户id
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
        r"""云存开启状态，0为未开启，2为正在生效，1为已过期
注：这里只返回状态为0的数据
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CSType(self):
        r"""云存类型，1为全时云存，2为事件云存
        :rtype: int
        """
        return self._CSType

    @CSType.setter
    def CSType(self, CSType):
        self._CSType = CSType

    @property
    def CSShiftDuration(self):
        r"""云存回看时长
        :rtype: int
        """
        return self._CSShiftDuration

    @CSShiftDuration.setter
    def CSShiftDuration(self, CSShiftDuration):
        self._CSShiftDuration = CSShiftDuration

    @property
    def CSExpiredTime(self):
        r"""云存套餐过期时间
        :rtype: int
        """
        return self._CSExpiredTime

    @CSExpiredTime.setter
    def CSExpiredTime(self, CSExpiredTime):
        self._CSExpiredTime = CSExpiredTime

    @property
    def CreatedAt(self):
        r"""云存套餐创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""云存套餐更新时间
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PackageId(self):
        r"""套餐id
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def OrderId(self):
        r"""订单id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChannelId(self):
        r"""通道id
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def CSUserId(self):
        r"""用户id
        :rtype: str
        """
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
        


class PauseTWeCallDeviceRequest(AbstractModel):
    r"""PauseTWeCallDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._DeviceList = None

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: list of TWeCallInfo
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
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
        


class PauseTWeCallDeviceResponse(AbstractModel):
    r"""PauseTWeCallDevice返回参数结构体

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


class PositionFenceInfo(AbstractModel):
    r"""围栏详细信息(包含创建时间及更新时间)

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
        r"""围栏信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.PositionFenceItem`
        """
        return self._GeoFence

    @GeoFence.setter
    def GeoFence(self, GeoFence):
        self._GeoFence = GeoFence

    @property
    def CreateTime(self):
        r"""围栏创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""围栏更新时间
        :rtype: int
        """
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
    r"""围栏信息

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
        r"""围栏Id
        :rtype: int
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def SpaceId(self):
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FenceName(self):
        r"""围栏名称
        :rtype: str
        """
        return self._FenceName

    @FenceName.setter
    def FenceName(self, FenceName):
        self._FenceName = FenceName

    @property
    def FenceDesc(self):
        r"""围栏描述
        :rtype: str
        """
        return self._FenceDesc

    @FenceDesc.setter
    def FenceDesc(self, FenceDesc):
        self._FenceDesc = FenceDesc

    @property
    def FenceArea(self):
        r"""围栏区域信息，采用 GeoJSON 格式
        :rtype: str
        """
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
    r"""位置点

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
        :type LocationType: str
        :param _Accuracy: 位置点的精度预估，单位为米
        :type Accuracy: float
        """
        self._CreateTime = None
        self._Longitude = None
        self._Latitude = None
        self._LocationType = None
        self._Accuracy = None

    @property
    def CreateTime(self):
        r"""位置点的时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Longitude(self):
        r"""位置点的经度
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""位置点的纬度
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def LocationType(self):
        r"""位置点的定位类型
        :rtype: str
        """
        return self._LocationType

    @LocationType.setter
    def LocationType(self, LocationType):
        self._LocationType = LocationType

    @property
    def Accuracy(self):
        r"""位置点的精度预估，单位为米
        :rtype: float
        """
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
    r"""位置空间详情

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
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SpaceId(self):
        r"""位置空间Id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        r"""位置空间名称
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def AuthorizeType(self):
        r"""授权类型
        :rtype: int
        """
        return self._AuthorizeType

    @AuthorizeType.setter
    def AuthorizeType(self, AuthorizeType):
        self._AuthorizeType = AuthorizeType

    @property
    def Description(self):
        r"""描述备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductIdList(self):
        r"""产品列表
        :rtype: list of str
        """
        return self._ProductIdList

    @ProductIdList.setter
    def ProductIdList(self, ProductIdList):
        self._ProductIdList = ProductIdList

    @property
    def Icon(self):
        r"""缩略图
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Zoom(self):
        r"""用户自定义地图缩放
        :rtype: int
        """
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
    r"""产品设备位置信息

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
        r"""设备位置列表
        :rtype: list of DevicePositionItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def ProductId(self):
        r"""产品标识
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Total(self):
        r"""设备位置数量
        :rtype: int
        """
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
    r"""产品详情

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _CategoryId: 产品分组模板ID
        :type CategoryId: int
        :param _EncryptionType: 加密类型。1表示证书认证，2表示密钥认证，21表示TID认证-SE方式，22表示TID认证-软加固方式
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
        :type EnableProductScript: str
        :param _CreateUserId: 创建人 UinId
        :type CreateUserId: int
        :param _CreatorNickName: 创建者昵称
        :type CreatorNickName: str
        :param _BindStrategy: 绑定策略（1：强踢；2：非强踢；0：表示无意义）
        :type BindStrategy: int
        :param _DeviceCount: 设备数量
        :type DeviceCount: int
        :param _Rate: 平均传输速率
        :type Rate: str
        :param _Period: 有效期
        :type Period: str
        :param _IsInterconnection: 互联互通标识
        :type IsInterconnection: int
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
        self._IsInterconnection = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def CategoryId(self):
        r"""产品分组模板ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def EncryptionType(self):
        r"""加密类型。1表示证书认证，2表示密钥认证，21表示TID认证-SE方式，22表示TID认证-软加固方式
        :rtype: str
        """
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def NetType(self):
        r"""连接类型。如：
wifi、wifi-ble、cellular、5g、lorawan、ble、ethernet、wifi-ethernet、else、sub_zigbee、sub_ble、sub_433mhz、sub_else、sub_blemesh
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def DataProtocol(self):
        r"""数据协议 (1 使用物模型 2 为自定义类型)
        :rtype: int
        """
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def ProductDesc(self):
        r"""产品描述
        :rtype: str
        """
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def DevStatus(self):
        r"""状态 如：all 全部, dev 开发中, audit 审核中 released 已发布
        :rtype: str
        """
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductType(self):
        r"""产品类型。如： 0 普通产品 ， 5 网关产品
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModuleId(self):
        r"""产品ModuleId
        :rtype: int
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def EnableProductScript(self):
        r"""是否使用脚本进行二进制转json功能 可以取值 true / false
        :rtype: str
        """
        return self._EnableProductScript

    @EnableProductScript.setter
    def EnableProductScript(self, EnableProductScript):
        self._EnableProductScript = EnableProductScript

    @property
    def CreateUserId(self):
        r"""创建人 UinId
        :rtype: int
        """
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def CreatorNickName(self):
        r"""创建者昵称
        :rtype: str
        """
        return self._CreatorNickName

    @CreatorNickName.setter
    def CreatorNickName(self, CreatorNickName):
        self._CreatorNickName = CreatorNickName

    @property
    def BindStrategy(self):
        r"""绑定策略（1：强踢；2：非强踢；0：表示无意义）
        :rtype: int
        """
        return self._BindStrategy

    @BindStrategy.setter
    def BindStrategy(self, BindStrategy):
        self._BindStrategy = BindStrategy

    @property
    def DeviceCount(self):
        r"""设备数量
        :rtype: int
        """
        return self._DeviceCount

    @DeviceCount.setter
    def DeviceCount(self, DeviceCount):
        self._DeviceCount = DeviceCount

    @property
    def Rate(self):
        r"""平均传输速率
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Period(self):
        r"""有效期
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def IsInterconnection(self):
        r"""互联互通标识
        :rtype: int
        """
        return self._IsInterconnection

    @IsInterconnection.setter
    def IsInterconnection(self, IsInterconnection):
        self._IsInterconnection = IsInterconnection


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
        self._IsInterconnection = params.get("IsInterconnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductModelDefinition(AbstractModel):
    r"""产品模型定义

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
        :type CategoryModel: str
        :param _NetTypeModel: 产品的连接类型的模型
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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelDefine(self):
        r"""模型定义
        :rtype: str
        """
        return self._ModelDefine

    @ModelDefine.setter
    def ModelDefine(self, ModelDefine):
        self._ModelDefine = ModelDefine

    @property
    def UpdateTime(self):
        r"""更新时间，秒级时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        r"""创建时间，秒级时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CategoryModel(self):
        r"""产品所属分类的模型快照（产品创建时刻的）
        :rtype: str
        """
        return self._CategoryModel

    @CategoryModel.setter
    def CategoryModel(self, CategoryModel):
        self._CategoryModel = CategoryModel

    @property
    def NetTypeModel(self):
        r"""产品的连接类型的模型
        :rtype: str
        """
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
    r"""项目详情

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        r"""项目描述
        :rtype: str
        """
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc

    @property
    def CreateTime(self):
        r"""创建时间，unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间，unix时间戳
        :rtype: int
        """
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
    r"""项目详情

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
        :type InstanceId: str
        :param _ApplicationCount: 应用数量
        :type ApplicationCount: int
        :param _DeviceCount: 设备注册总数
        :type DeviceCount: int
        :param _EnableOpenState: 是否开通物联使能
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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDesc(self):
        r"""项目描述
        :rtype: str
        """
        return self._ProjectDesc

    @ProjectDesc.setter
    def ProjectDesc(self, ProjectDesc):
        self._ProjectDesc = ProjectDesc

    @property
    def CreateTime(self):
        r"""项目创建时间，unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""项目更新时间，unix时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ProductCount(self):
        r"""产品数量
        :rtype: int
        """
        return self._ProductCount

    @ProductCount.setter
    def ProductCount(self, ProductCount):
        self._ProductCount = ProductCount

    @property
    def NativeAppCount(self):
        r"""NativeApp数量
        :rtype: int
        """
        return self._NativeAppCount

    @NativeAppCount.setter
    def NativeAppCount(self, NativeAppCount):
        self._NativeAppCount = NativeAppCount

    @property
    def WebAppCount(self):
        r"""WebApp数量
        :rtype: int
        """
        return self._WebAppCount

    @WebAppCount.setter
    def WebAppCount(self, WebAppCount):
        self._WebAppCount = WebAppCount

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApplicationCount(self):
        r"""应用数量
        :rtype: int
        """
        return self._ApplicationCount

    @ApplicationCount.setter
    def ApplicationCount(self, ApplicationCount):
        self._ApplicationCount = ApplicationCount

    @property
    def DeviceCount(self):
        r"""设备注册总数
        :rtype: int
        """
        return self._DeviceCount

    @DeviceCount.setter
    def DeviceCount(self, DeviceCount):
        self._DeviceCount = DeviceCount

    @property
    def EnableOpenState(self):
        r"""是否开通物联使能
        :rtype: int
        """
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
    r"""PublishBroadcastMessage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Payload(self):
        r"""消息内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Qos(self):
        r"""消息质量等级
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        r"""ayload内容的编码格式，取值为base64或空。base64表示云端将收到的请求数据进行base64解码后下发到设备，空则直接将原始内容下发到设备
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
    r"""PublishBroadcastMessage返回参数结构体

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
        r"""广播消息任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PublishFirmwareUpdateMessageRequest(AbstractModel):
    r"""PublishFirmwareUpdateMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品 ID。
        :type ProductID: str
        :param _DeviceName: 设备名称。
        :type DeviceName: str
        :param _FwType: 固件类型
        :type FwType: str
        """
        self._ProductID = None
        self._DeviceName = None
        self._FwType = None

    @property
    def ProductID(self):
        r"""产品 ID。
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        r"""设备名称。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FwType(self):
        r"""固件类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishFirmwareUpdateMessageResponse(AbstractModel):
    r"""PublishFirmwareUpdateMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 请求状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""请求状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class PublishMessageRequest(AbstractModel):
    r"""PublishMessage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Topic(self):
        r"""消息发往的主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        r"""云端下发到设备的控制报文
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Qos(self):
        r"""消息服务质量等级，取值为0或1
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        r"""Payload的内容编码格式，取值为base64或空。base64表示云端将接收到的base64编码后的报文再转换成二进制报文下发至设备，为空表示不作转换，透传下发至设备
        :rtype: str
        """
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
    r"""PublishMessage返回参数结构体

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


class PublishRRPCMessageRequest(AbstractModel):
    r"""PublishRRPCMessage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Payload(self):
        r"""消息内容，utf8编码
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
    r"""PublishRRPCMessage返回参数结构体

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
        r"""RRPC消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def PayloadBase64(self):
        r"""设备回复的消息内容，采用base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayloadBase64

    @PayloadBase64.setter
    def PayloadBase64(self, PayloadBase64):
        self._PayloadBase64 = PayloadBase64

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
        self._MessageId = params.get("MessageId")
        self._PayloadBase64 = params.get("PayloadBase64")
        self._RequestId = params.get("RequestId")


class RegisteredDeviceNetTypeInfo(AbstractModel):
    r"""已注册通信类型信息

    """

    def __init__(self):
        r"""
        :param _NormalDeviceNum: 普通设备数
        :type NormalDeviceNum: int
        :param _BluetoothDeviceNum: 蓝牙设备数
        :type BluetoothDeviceNum: int
        """
        self._NormalDeviceNum = None
        self._BluetoothDeviceNum = None

    @property
    def NormalDeviceNum(self):
        r"""普通设备数
        :rtype: int
        """
        return self._NormalDeviceNum

    @NormalDeviceNum.setter
    def NormalDeviceNum(self, NormalDeviceNum):
        self._NormalDeviceNum = NormalDeviceNum

    @property
    def BluetoothDeviceNum(self):
        r"""蓝牙设备数
        :rtype: int
        """
        return self._BluetoothDeviceNum

    @BluetoothDeviceNum.setter
    def BluetoothDeviceNum(self, BluetoothDeviceNum):
        self._BluetoothDeviceNum = BluetoothDeviceNum


    def _deserialize(self, params):
        self._NormalDeviceNum = params.get("NormalDeviceNum")
        self._BluetoothDeviceNum = params.get("BluetoothDeviceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisteredDeviceTypeInfo(AbstractModel):
    r"""已注册设备类型信息

    """

    def __init__(self):
        r"""
        :param _NormalDeviceNum: 已注册设备数
        :type NormalDeviceNum: int
        :param _GatewayDeviceNum: 已注册网关数
        :type GatewayDeviceNum: int
        :param _SubDeviceNum: 已注册子设备数
        :type SubDeviceNum: int
        :param _VideoDeviceNum: 已注册视频设备数
        :type VideoDeviceNum: int
        """
        self._NormalDeviceNum = None
        self._GatewayDeviceNum = None
        self._SubDeviceNum = None
        self._VideoDeviceNum = None

    @property
    def NormalDeviceNum(self):
        r"""已注册设备数
        :rtype: int
        """
        return self._NormalDeviceNum

    @NormalDeviceNum.setter
    def NormalDeviceNum(self, NormalDeviceNum):
        self._NormalDeviceNum = NormalDeviceNum

    @property
    def GatewayDeviceNum(self):
        r"""已注册网关数
        :rtype: int
        """
        return self._GatewayDeviceNum

    @GatewayDeviceNum.setter
    def GatewayDeviceNum(self, GatewayDeviceNum):
        self._GatewayDeviceNum = GatewayDeviceNum

    @property
    def SubDeviceNum(self):
        r"""已注册子设备数
        :rtype: int
        """
        return self._SubDeviceNum

    @SubDeviceNum.setter
    def SubDeviceNum(self, SubDeviceNum):
        self._SubDeviceNum = SubDeviceNum

    @property
    def VideoDeviceNum(self):
        r"""已注册视频设备数
        :rtype: int
        """
        return self._VideoDeviceNum

    @VideoDeviceNum.setter
    def VideoDeviceNum(self, VideoDeviceNum):
        self._VideoDeviceNum = VideoDeviceNum


    def _deserialize(self, params):
        self._NormalDeviceNum = params.get("NormalDeviceNum")
        self._GatewayDeviceNum = params.get("GatewayDeviceNum")
        self._SubDeviceNum = params.get("SubDeviceNum")
        self._VideoDeviceNum = params.get("VideoDeviceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseStudioProductRequest(AbstractModel):
    r"""ReleaseStudioProduct请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DevStatus(self):
        r"""产品DevStatus
        :rtype: str
        """
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
    r"""ReleaseStudioProduct返回参数结构体

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


class RemoveUserByRoomIdFromTRTCRequest(AbstractModel):
    r"""RemoveUserByRoomIdFromTRTC请求参数结构体

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
        r"""房间id
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TRTCUserIds(self):
        r"""用户名称数组，数组元素不可重复，最长不超过 10 个。
        :rtype: list of str
        """
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
    r"""RemoveUserByRoomIdFromTRTC返回参数结构体

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


class ResetCloudStorageAIServiceRequest(AbstractModel):
    r"""ResetCloudStorageAIService请求参数结构体

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
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ServiceType(self):
        r"""云存 AI 服务类型。可选值：
- `RealtimeObjectDetect`：目标检测
- `Highlight`：视频浓缩
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def UserId(self):
        r"""用户 ID
        :rtype: str
        """
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
    r"""ResetCloudStorageAIService返回参数结构体

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


class ResetCloudStorageEventRequest(AbstractModel):
    r"""ResetCloudStorageEvent请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
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
    r"""ResetCloudStorageEvent返回参数结构体

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


class ResetCloudStorageRequest(AbstractModel):
    r"""ResetCloudStorage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ChannelId(self):
        r"""通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def UserId(self):
        r"""云存用户Id，为空则为默认云存空间。
        :rtype: str
        """
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
    r"""ResetCloudStorage返回参数结构体

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


class ResetTWeCallDeviceRequest(AbstractModel):
    r"""ResetTWeCallDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._DeviceList = None

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: list of TWeCallInfo
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
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
        


class ResetTWeCallDeviceResponse(AbstractModel):
    r"""ResetTWeCallDevice返回参数结构体

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


class ResumeWeCallDeviceRequest(AbstractModel):
    r"""ResumeWeCallDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceList: 设备列表
        :type DeviceList: list of TWeCallInfo
        """
        self._DeviceList = None

    @property
    def DeviceList(self):
        r"""设备列表
        :rtype: list of TWeCallInfo
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
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
        


class ResumeWeCallDeviceResponse(AbstractModel):
    r"""ResumeWeCallDevice返回参数结构体

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


class SearchKeyword(AbstractModel):
    r"""搜索关键词

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
        r"""搜索条件的Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""搜索条件的值
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
        


class SearchPositionSpaceRequest(AbstractModel):
    r"""SearchPositionSpace请求参数结构体

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
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SpaceName(self):
        r"""位置空间名字
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def Offset(self):
        r"""偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大获取数量
        :rtype: int
        """
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
    r"""SearchPositionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 位置空间列表
        :type List: list of PositionSpaceInfo
        :param _Total: 符合条件的位置空间个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def List(self):
        r"""位置空间列表
        :rtype: list of PositionSpaceInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""符合条件的位置空间个数
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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PositionSpaceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class SearchStudioProductRequest(AbstractModel):
    r"""SearchStudioProduct请求参数结构体

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
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Limit(self):
        r"""列表Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""列表Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DevStatus(self):
        r"""产品Status
        :rtype: str
        """
        return self._DevStatus

    @DevStatus.setter
    def DevStatus(self, DevStatus):
        self._DevStatus = DevStatus

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Filters(self):
        r"""每次请求的Filters的上限为10，Filter.Values的上限为1。
        :rtype: list of Filter
        """
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
    r"""SearchStudioProduct返回参数结构体

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
        r"""产品列表
        :rtype: list of ProductEntry
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def Total(self):
        r"""产品数量
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
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class SearchTopicRuleRequest(AbstractModel):
    r"""SearchTopicRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名
        :type RuleName: str
        """
        self._RuleName = None

    @property
    def RuleName(self):
        r"""规则名
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
        


class SearchTopicRuleResponse(AbstractModel):
    r"""SearchTopicRule返回参数结构体

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
        r"""搜索到的规则总数
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def Rules(self):
        r"""规则信息列表
        :rtype: list of TopicRuleInfo
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

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
        self._TotalCnt = params.get("TotalCnt")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = TopicRuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class SubscribedTopicItem(AbstractModel):
    r"""已订阅Topic信息

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic名称
        :type TopicName: str
        """
        self._TopicName = None

    @property
    def TopicName(self):
        r"""Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCParams(AbstractModel):
    r"""TRTC 的参数 可以用来加入房间

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
        r"""TRTC入参: TRTC的实例ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        r"""TRTC入参: 用户加入房间的ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""TRTC入参: 用户的签名用来鉴权
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def StrRoomId(self):
        r"""TRTC入参: 加入的TRTC房间名称
        :rtype: str
        """
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def PrivateKey(self):
        r"""TRTC入参: 校验TRTC的KEY
        :rtype: str
        """
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
    r"""TWeCall设备激活信息

    """

    def __init__(self):
        r"""
        :param _ModelId: 小程序ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _Sn: Sn信息
        :type Sn: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: int
        :param _PkgType: 类型
        :type PkgType: int
        """
        self._ModelId = None
        self._Sn = None
        self._ExpireTime = None
        self._PkgType = None

    @property
    def ModelId(self):
        warnings.warn("parameter `ModelId` is deprecated", DeprecationWarning) 

        r"""小程序ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        warnings.warn("parameter `ModelId` is deprecated", DeprecationWarning) 

        self._ModelId = ModelId

    @property
    def Sn(self):
        r"""Sn信息
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ExpireTime(self):
        r"""过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PkgType(self):
        r"""类型
        :rtype: int
        """
        return self._PkgType

    @PkgType.setter
    def PkgType(self, PkgType):
        self._PkgType = PkgType


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Sn = params.get("Sn")
        self._ExpireTime = params.get("ExpireTime")
        self._PkgType = params.get("PkgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TWeCallInfo(AbstractModel):
    r"""TWeCall信息

    """

    def __init__(self):
        r"""
        :param _Sn: Sn信息，SN格式：产品ID_设备名
        :type Sn: str
        :param _ModelId: 小程序ID，参数已弃用，不用传参
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _ActiveNum: 激活数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveNum: int
        """
        self._Sn = None
        self._ModelId = None
        self._ActiveNum = None

    @property
    def Sn(self):
        r"""Sn信息，SN格式：产品ID_设备名
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ModelId(self):
        warnings.warn("parameter `ModelId` is deprecated", DeprecationWarning) 

        r"""小程序ID，参数已弃用，不用传参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        warnings.warn("parameter `ModelId` is deprecated", DeprecationWarning) 

        self._ModelId = ModelId

    @property
    def ActiveNum(self):
        warnings.warn("parameter `ActiveNum` is deprecated", DeprecationWarning) 

        r"""激活数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActiveNum

    @ActiveNum.setter
    def ActiveNum(self, ActiveNum):
        warnings.warn("parameter `ActiveNum` is deprecated", DeprecationWarning) 

        self._ActiveNum = ActiveNum


    def _deserialize(self, params):
        self._Sn = params.get("Sn")
        self._ModelId = params.get("ModelId")
        self._ActiveNum = params.get("ActiveNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TWeCallLicenseInfo(AbstractModel):
    r"""TWeCall信息

    """

    def __init__(self):
        r"""
        :param _TWeCallType: voip类型
        :type TWeCallType: str
        :param _TotalNum: 总数
        :type TotalNum: int
        :param _UsedNum: 已使用
        :type UsedNum: int
        """
        self._TWeCallType = None
        self._TotalNum = None
        self._UsedNum = None

    @property
    def TWeCallType(self):
        r"""voip类型
        :rtype: str
        """
        return self._TWeCallType

    @TWeCallType.setter
    def TWeCallType(self, TWeCallType):
        self._TWeCallType = TWeCallType

    @property
    def TotalNum(self):
        r"""总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def UsedNum(self):
        r"""已使用
        :rtype: int
        """
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum


    def _deserialize(self, params):
        self._TWeCallType = params.get("TWeCallType")
        self._TotalNum = params.get("TotalNum")
        self._UsedNum = params.get("UsedNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkBasicConfigInfo(AbstractModel):
    r"""基础配置信息。

    """

    def __init__(self):
        r"""
        :param _SystemPrompt: 系统提示词
        :type SystemPrompt: str
        :param _GreetingMessage: 欢迎语，支持多个欢迎语随机切换，格式：字符串数组，JSON字符串。
        :type GreetingMessage: str
        :param _DefaultVoiceType: 音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :type DefaultVoiceType: int
        """
        self._SystemPrompt = None
        self._GreetingMessage = None
        self._DefaultVoiceType = None

    @property
    def SystemPrompt(self):
        r"""系统提示词
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt

    @property
    def GreetingMessage(self):
        r"""欢迎语，支持多个欢迎语随机切换，格式：字符串数组，JSON字符串。
        :rtype: str
        """
        return self._GreetingMessage

    @GreetingMessage.setter
    def GreetingMessage(self, GreetingMessage):
        self._GreetingMessage = GreetingMessage

    @property
    def DefaultVoiceType(self):
        r"""音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :rtype: int
        """
        return self._DefaultVoiceType

    @DefaultVoiceType.setter
    def DefaultVoiceType(self, DefaultVoiceType):
        self._DefaultVoiceType = DefaultVoiceType


    def _deserialize(self, params):
        self._SystemPrompt = params.get("SystemPrompt")
        self._GreetingMessage = params.get("GreetingMessage")
        self._DefaultVoiceType = params.get("DefaultVoiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkConversationConfigInfo(AbstractModel):
    r"""会话配置信息。

    """

    def __init__(self):
        r"""
        :param _SessionTimeout: 会话超时（秒）
        :type SessionTimeout: int
        :param _InterruptionEnabled: 允许打断
        :type InterruptionEnabled: bool
        :param _MaxContextTokens: 最大上下文
        :type MaxContextTokens: int
        :param _IdleDetection: 空闲检测配置
        :type IdleDetection: :class:`tencentcloud.iotexplorer.v20190423.models.TalkIdleDetectionConfigInfo`
        :param _EmotionEnabled: 是否启用情绪识别
        :type EmotionEnabled: bool
        :param _SemanticVADEnabled: 是否启用语义vad
        :type SemanticVADEnabled: bool
        :param _NoiseFilterEnabled: 是否启用噪声过滤
        :type NoiseFilterEnabled: bool
        """
        self._SessionTimeout = None
        self._InterruptionEnabled = None
        self._MaxContextTokens = None
        self._IdleDetection = None
        self._EmotionEnabled = None
        self._SemanticVADEnabled = None
        self._NoiseFilterEnabled = None

    @property
    def SessionTimeout(self):
        r"""会话超时（秒）
        :rtype: int
        """
        return self._SessionTimeout

    @SessionTimeout.setter
    def SessionTimeout(self, SessionTimeout):
        self._SessionTimeout = SessionTimeout

    @property
    def InterruptionEnabled(self):
        r"""允许打断
        :rtype: bool
        """
        return self._InterruptionEnabled

    @InterruptionEnabled.setter
    def InterruptionEnabled(self, InterruptionEnabled):
        self._InterruptionEnabled = InterruptionEnabled

    @property
    def MaxContextTokens(self):
        r"""最大上下文
        :rtype: int
        """
        return self._MaxContextTokens

    @MaxContextTokens.setter
    def MaxContextTokens(self, MaxContextTokens):
        self._MaxContextTokens = MaxContextTokens

    @property
    def IdleDetection(self):
        r"""空闲检测配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkIdleDetectionConfigInfo`
        """
        return self._IdleDetection

    @IdleDetection.setter
    def IdleDetection(self, IdleDetection):
        self._IdleDetection = IdleDetection

    @property
    def EmotionEnabled(self):
        r"""是否启用情绪识别
        :rtype: bool
        """
        return self._EmotionEnabled

    @EmotionEnabled.setter
    def EmotionEnabled(self, EmotionEnabled):
        self._EmotionEnabled = EmotionEnabled

    @property
    def SemanticVADEnabled(self):
        r"""是否启用语义vad
        :rtype: bool
        """
        return self._SemanticVADEnabled

    @SemanticVADEnabled.setter
    def SemanticVADEnabled(self, SemanticVADEnabled):
        self._SemanticVADEnabled = SemanticVADEnabled

    @property
    def NoiseFilterEnabled(self):
        r"""是否启用噪声过滤
        :rtype: bool
        """
        return self._NoiseFilterEnabled

    @NoiseFilterEnabled.setter
    def NoiseFilterEnabled(self, NoiseFilterEnabled):
        self._NoiseFilterEnabled = NoiseFilterEnabled


    def _deserialize(self, params):
        self._SessionTimeout = params.get("SessionTimeout")
        self._InterruptionEnabled = params.get("InterruptionEnabled")
        self._MaxContextTokens = params.get("MaxContextTokens")
        if params.get("IdleDetection") is not None:
            self._IdleDetection = TalkIdleDetectionConfigInfo()
            self._IdleDetection._deserialize(params.get("IdleDetection"))
        self._EmotionEnabled = params.get("EmotionEnabled")
        self._SemanticVADEnabled = params.get("SemanticVADEnabled")
        self._NoiseFilterEnabled = params.get("NoiseFilterEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkIdleDetectionConfigInfo(AbstractModel):
    r"""空闲检测信息。

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否启用
        :type Enabled: bool
        :param _TimeoutSeconds: 用户沉默多少秒后触发空闲回调
        :type TimeoutSeconds: float
        :param _MaxRetries: 最大重试次数（1-3）
        :type MaxRetries: int
        :param _IdleResponses: 空闲响应
        :type IdleResponses: list of IdleResponseInfo
        """
        self._Enabled = None
        self._TimeoutSeconds = None
        self._MaxRetries = None
        self._IdleResponses = None

    @property
    def Enabled(self):
        r"""是否启用
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def TimeoutSeconds(self):
        r"""用户沉默多少秒后触发空闲回调
        :rtype: float
        """
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def MaxRetries(self):
        r"""最大重试次数（1-3）
        :rtype: int
        """
        return self._MaxRetries

    @MaxRetries.setter
    def MaxRetries(self, MaxRetries):
        self._MaxRetries = MaxRetries

    @property
    def IdleResponses(self):
        r"""空闲响应
        :rtype: list of IdleResponseInfo
        """
        return self._IdleResponses

    @IdleResponses.setter
    def IdleResponses(self, IdleResponses):
        self._IdleResponses = IdleResponses


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._MaxRetries = params.get("MaxRetries")
        if params.get("IdleResponses") is not None:
            self._IdleResponses = []
            for item in params.get("IdleResponses"):
                obj = IdleResponseInfo()
                obj._deserialize(item)
                self._IdleResponses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkLLMConfigInfo(AbstractModel):
    r"""LLM配置信息。

    """

    def __init__(self):
        r"""
        :param _LLMType: 支持的LLM类型，tencent-腾讯；openai-OPENAI格式；anthropic-ANTHROPIC；gemini-GEMINI;gemini-GEMINI;coze-扣子;dify-DIFY；tencent_lke-腾讯智能体平台；系统默认-openai。
        :type LLMType: str
        :param _Enabled: 是否开启
        :type Enabled: bool
        :param _Model: 模型
        :type Model: str
        :param _Streaming: 是否开启
        :type Streaming: bool
        :param _Config: 配置信息JSON字符串，根据`LLMType`进行不同的值匹配。例如`LLMType`是`openai`，`Config`值是`{\"ApiKey\":\"sk-09***\",\"ApiUrl\":\"base_url\",\"SystemPrompt\":\"你是一个语音助手\",\"Timeout\":30,\"History\":0,\"MetaInfo\":{\"productID\":\"test\"}}`

## openai
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "SystemPrompt": "一个小小助手",
  "Timeout":20,
  "History":10,
  "MetaInfo":{}
}
```

## anthropic
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "SystemPrompt": "一个小小助手"
}
```
## gemini
```
{
  "AppId": 123456,
  "AccessToken": "*****",
  "ResourceId": "SecretKey****",
  "ModelName": "16k_zh",
  "Language":""
}
```
## coze
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "BotId": "v1",
   "UserId": "xxx",
  "ApiUrl": "https://api.coze.cn/v3/chat"
}
```
## dify
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "User": "xxx",
  "Inputs":{},
  "ConversationId":"c1"
}
```
## tencent_lke
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "SystemRole": "一个小小助手",
  "SessionId":"123456"
}
```

        :type Config: str
        :param _Temperature: 温度
        :type Temperature: float
        :param _MaxTokens: 最大token数
        :type MaxTokens: int
        :param _TopP: topP
        :type TopP: float
        """
        self._LLMType = None
        self._Enabled = None
        self._Model = None
        self._Streaming = None
        self._Config = None
        self._Temperature = None
        self._MaxTokens = None
        self._TopP = None

    @property
    def LLMType(self):
        r"""支持的LLM类型，tencent-腾讯；openai-OPENAI格式；anthropic-ANTHROPIC；gemini-GEMINI;gemini-GEMINI;coze-扣子;dify-DIFY；tencent_lke-腾讯智能体平台；系统默认-openai。
        :rtype: str
        """
        return self._LLMType

    @LLMType.setter
    def LLMType(self, LLMType):
        self._LLMType = LLMType

    @property
    def Enabled(self):
        r"""是否开启
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Model(self):
        r"""模型
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Streaming(self):
        r"""是否开启
        :rtype: bool
        """
        return self._Streaming

    @Streaming.setter
    def Streaming(self, Streaming):
        self._Streaming = Streaming

    @property
    def Config(self):
        r"""配置信息JSON字符串，根据`LLMType`进行不同的值匹配。例如`LLMType`是`openai`，`Config`值是`{\"ApiKey\":\"sk-09***\",\"ApiUrl\":\"base_url\",\"SystemPrompt\":\"你是一个语音助手\",\"Timeout\":30,\"History\":0,\"MetaInfo\":{\"productID\":\"test\"}}`

## openai
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "SystemPrompt": "一个小小助手",
  "Timeout":20,
  "History":10,
  "MetaInfo":{}
}
```

## anthropic
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "SystemPrompt": "一个小小助手"
}
```
## gemini
```
{
  "AppId": 123456,
  "AccessToken": "*****",
  "ResourceId": "SecretKey****",
  "ModelName": "16k_zh",
  "Language":""
}
```
## coze
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "BotId": "v1",
   "UserId": "xxx",
  "ApiUrl": "https://api.coze.cn/v3/chat"
}
```
## dify
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "User": "xxx",
  "Inputs":{},
  "ConversationId":"c1"
}
```
## tencent_lke
```
{
   "ApiKey": "sk-XXXXXXXXXXXX",
   "ApiUrl": "https://api.openai.com/v1",
   "SystemRole": "一个小小助手",
  "SessionId":"123456"
}
```

        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Temperature(self):
        r"""温度
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def MaxTokens(self):
        r"""最大token数
        :rtype: int
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def TopP(self):
        r"""topP
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP


    def _deserialize(self, params):
        self._LLMType = params.get("LLMType")
        self._Enabled = params.get("Enabled")
        self._Model = params.get("Model")
        self._Streaming = params.get("Streaming")
        self._Config = params.get("Config")
        self._Temperature = params.get("Temperature")
        self._MaxTokens = params.get("MaxTokens")
        self._TopP = params.get("TopP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkProductConfigInfo(AbstractModel):
    r"""Talk配置信息描述。

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _TargetLanguage: 支持的语言，zh-中文；en-英文；默认zh
        :type TargetLanguage: str
        :param _SystemPrompt:  系统提示词
        :type SystemPrompt: str
        :param _GreetingMessage: 欢迎语
        :type GreetingMessage: str
        :param _VoiceType: 音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :type VoiceType: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        """
        self._ProductId = None
        self._TargetLanguage = None
        self._SystemPrompt = None
        self._GreetingMessage = None
        self._VoiceType = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TargetLanguage(self):
        r"""支持的语言，zh-中文；en-英文；默认zh
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def SystemPrompt(self):
        r""" 系统提示词
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt

    @property
    def GreetingMessage(self):
        r"""欢迎语
        :rtype: str
        """
        return self._GreetingMessage

    @GreetingMessage.setter
    def GreetingMessage(self, GreetingMessage):
        self._GreetingMessage = GreetingMessage

    @property
    def VoiceType(self):
        r"""音色，支持的音色列表：100510000-阅读男声智逍遥；101001-情感女声智瑜；101002-通用女声智聆；101003-客服女声智美；101004-通用男声智云；101005-通用女声智莉；101006-助手女声智言；101008-客服女声智琪；101009-知性女声智芸；101010-通用男声智华；101011-新闻女声智燕；101012-新闻女声智丹；101013-新闻男声智辉；101014 -新闻男声智宁；101015-男童声智萌；101016-女童声智甜；101017-情感女声智蓉；101018-情感男声智靖；101019-粤语女声智彤。
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TargetLanguage = params.get("TargetLanguage")
        self._SystemPrompt = params.get("SystemPrompt")
        self._GreetingMessage = params.get("GreetingMessage")
        self._VoiceType = params.get("VoiceType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkProductConfigV2Info(AbstractModel):
    r"""twetalk连接配置信息。

    """

    def __init__(self):
        r"""
        :param _Uin: UIN
        :type Uin: int
        :param _AppId: APPID
        :type AppId: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ConfigName: 配置名称
        :type ConfigName: str
        :param _TargetLanguage: 语言，默认zh；zh-中文；en-英文
        :type TargetLanguage: str
        :param _BasicConfig: 基础配置
        :type BasicConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkBasicConfigInfo`
        :param _STTConfig: 语音识别配置
        :type STTConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkSTTConfigInfo`
        :param _LLMConfig: 大模型配置
        :type LLMConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkLLMConfigInfo`
        :param _TTSConfig: 语音合成配置
        :type TTSConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkTTSConfigInfo`
        :param _ConversationConfig: 会话配置
        :type ConversationConfig: :class:`tencentcloud.iotexplorer.v20190423.models.TalkConversationConfigInfo`
        :param _Version: 版本号
        :type Version: int
        :param _CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param _UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        """
        self._Uin = None
        self._AppId = None
        self._ProductId = None
        self._DeviceName = None
        self._ConfigName = None
        self._TargetLanguage = None
        self._BasicConfig = None
        self._STTConfig = None
        self._LLMConfig = None
        self._TTSConfig = None
        self._ConversationConfig = None
        self._Version = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Uin(self):
        r"""UIN
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        r"""APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ConfigName(self):
        r"""配置名称
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def TargetLanguage(self):
        r"""语言，默认zh；zh-中文；en-英文
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def BasicConfig(self):
        r"""基础配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkBasicConfigInfo`
        """
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def STTConfig(self):
        r"""语音识别配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkSTTConfigInfo`
        """
        return self._STTConfig

    @STTConfig.setter
    def STTConfig(self, STTConfig):
        self._STTConfig = STTConfig

    @property
    def LLMConfig(self):
        r"""大模型配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkLLMConfigInfo`
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""语音合成配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkTTSConfigInfo`
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def ConversationConfig(self):
        r"""会话配置
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.TalkConversationConfigInfo`
        """
        return self._ConversationConfig

    @ConversationConfig.setter
    def ConversationConfig(self, ConversationConfig):
        self._ConversationConfig = ConversationConfig

    @property
    def Version(self):
        r"""版本号
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CreateTime(self):
        r"""创建时间，秒级时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间，秒级时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ConfigName = params.get("ConfigName")
        self._TargetLanguage = params.get("TargetLanguage")
        if params.get("BasicConfig") is not None:
            self._BasicConfig = TalkBasicConfigInfo()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("STTConfig") is not None:
            self._STTConfig = TalkSTTConfigInfo()
            self._STTConfig._deserialize(params.get("STTConfig"))
        if params.get("LLMConfig") is not None:
            self._LLMConfig = TalkLLMConfigInfo()
            self._LLMConfig._deserialize(params.get("LLMConfig"))
        if params.get("TTSConfig") is not None:
            self._TTSConfig = TalkTTSConfigInfo()
            self._TTSConfig._deserialize(params.get("TTSConfig"))
        if params.get("ConversationConfig") is not None:
            self._ConversationConfig = TalkConversationConfigInfo()
            self._ConversationConfig._deserialize(params.get("ConversationConfig"))
        self._Version = params.get("Version")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkSTTConfigInfo(AbstractModel):
    r"""STT配置信息。

    """

    def __init__(self):
        r"""
        :param _STTType: 支持的STT类型，tencent-腾讯；azure-亚马逊；volcengine-火山引擎；deepgram-Deepgram;系统默认-tencent。
        :type STTType: str
        :param _Enabled: 是否开启
        :type Enabled: bool
        :param _Config: 配置信息JSON字符串，根据STTType进行不同的值匹配。例如`STTType`是`tencent`，`Config`值是`{\"AppId\":123456,\"SecretId\":\"secretId*****\",\"SecretKey\":\"SecretKey****\",\"EngineType\":\"16k_zh\"}`

## tencent
```
{
  "AppId": 123456,
  "SecretId": "secretId*****",
  "SecretKey": "SecretKey****",
  "EngineType": "16k_zh"
}
```

## azure
```
{
  "Region": "",
  "EndpointId": "id",
  "Language": "zh-CN",
  "SubscriptionKey": "*****"
}
```
## volcengine
```
{
  "AppId": 123456,
  "AccessToken": "*****",
  "ResourceId": "SecretKey****",
  "ModelName": "16k_zh",
  "Language":""
}
```
## deepgram
```
{
  "Model": "nova-2",
  "Language": "zh",
   "BaseUrl":"http://www.deepgram.com",
  "ApiKey": "SecretKey****"
}
```

        :type Config: str
        """
        self._STTType = None
        self._Enabled = None
        self._Config = None

    @property
    def STTType(self):
        r"""支持的STT类型，tencent-腾讯；azure-亚马逊；volcengine-火山引擎；deepgram-Deepgram;系统默认-tencent。
        :rtype: str
        """
        return self._STTType

    @STTType.setter
    def STTType(self, STTType):
        self._STTType = STTType

    @property
    def Enabled(self):
        r"""是否开启
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Config(self):
        r"""配置信息JSON字符串，根据STTType进行不同的值匹配。例如`STTType`是`tencent`，`Config`值是`{\"AppId\":123456,\"SecretId\":\"secretId*****\",\"SecretKey\":\"SecretKey****\",\"EngineType\":\"16k_zh\"}`

## tencent
```
{
  "AppId": 123456,
  "SecretId": "secretId*****",
  "SecretKey": "SecretKey****",
  "EngineType": "16k_zh"
}
```

## azure
```
{
  "Region": "",
  "EndpointId": "id",
  "Language": "zh-CN",
  "SubscriptionKey": "*****"
}
```
## volcengine
```
{
  "AppId": 123456,
  "AccessToken": "*****",
  "ResourceId": "SecretKey****",
  "ModelName": "16k_zh",
  "Language":""
}
```
## deepgram
```
{
  "Model": "nova-2",
  "Language": "zh",
   "BaseUrl":"http://www.deepgram.com",
  "ApiKey": "SecretKey****"
}
```

        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._STTType = params.get("STTType")
        self._Enabled = params.get("Enabled")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TalkTTSConfigInfo(AbstractModel):
    r"""TTS配置信息。

    """

    def __init__(self):
        r"""
        :param _TTSType: 支持的LLM类型，支持tencent-腾讯；azure-亚马逊；volcengine-火山引擎；elevenlabs-ELEVENLABS；minimax-MINIMAX；cartesia-CARTESIA；aliyun-阿里；系统默认-tencent。
        :type TTSType: str
        :param _Enabled: 是否开启
        :type Enabled: bool
        :param _Config: 配置信息JSON字符串，根据`TTSType`进行不同的值匹配。例如`TTSType`是`tencent`，`Config`值是`{\"AppId\":123456,\"SecretId\":\"secretId*****\",\"SecretKey\":\"SecretKey****\",\"VoiceType\":10001}`

## tencent
```
{
   "AppId": 100203,
   "SecretId": "XXXX",
   "SecretKey": "XXXXX",
  "VoiceType":123456
}
```

## azure
```
{
   "SubscriptionKey": 100203,
   "Region": "ch-zn",
   "VoiceName": "XXXXX",
  "Language":"zh"
}
```
## elevenlabs
```
{
   "ModelId": 100203,
   "VoiceId": "ch-zn",
   "ApiKey": "XXXXX"
}
```
## minimax
```
{  
  "Model":"xxxx",
   "ApiUrl": "346w34",
   "ApiKey": "xxx",
   "GroupId": "ion",
  "VoiceType":"xioawei"
}
```
## cartesia
```
{  
  "Model":"xxxx",
   "ApiKey": "xxx",
  "VoiceId":"xioawei"
}
```
## aliyun
```
{
   "VoiceType": 100203,
   "RegionId": "XXXX",
   "ApiKey": "XXXXX"
}
```
## volcengine
```
{
   "AppId": "346w34",
   "AccessToken": "xxx",
   "ResourceId": "volc.bigasr.sauc.duration",
  "VoiceType":"xioawei"
}
```

        :type Config: str
        :param _Speed: 温度
        :type Speed: float
        :param _Volume: 最大token数
        :type Volume: float
        :param _Pitch: PITCH
        :type Pitch: float
        """
        self._TTSType = None
        self._Enabled = None
        self._Config = None
        self._Speed = None
        self._Volume = None
        self._Pitch = None

    @property
    def TTSType(self):
        r"""支持的LLM类型，支持tencent-腾讯；azure-亚马逊；volcengine-火山引擎；elevenlabs-ELEVENLABS；minimax-MINIMAX；cartesia-CARTESIA；aliyun-阿里；系统默认-tencent。
        :rtype: str
        """
        return self._TTSType

    @TTSType.setter
    def TTSType(self, TTSType):
        self._TTSType = TTSType

    @property
    def Enabled(self):
        r"""是否开启
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Config(self):
        r"""配置信息JSON字符串，根据`TTSType`进行不同的值匹配。例如`TTSType`是`tencent`，`Config`值是`{\"AppId\":123456,\"SecretId\":\"secretId*****\",\"SecretKey\":\"SecretKey****\",\"VoiceType\":10001}`

## tencent
```
{
   "AppId": 100203,
   "SecretId": "XXXX",
   "SecretKey": "XXXXX",
  "VoiceType":123456
}
```

## azure
```
{
   "SubscriptionKey": 100203,
   "Region": "ch-zn",
   "VoiceName": "XXXXX",
  "Language":"zh"
}
```
## elevenlabs
```
{
   "ModelId": 100203,
   "VoiceId": "ch-zn",
   "ApiKey": "XXXXX"
}
```
## minimax
```
{  
  "Model":"xxxx",
   "ApiUrl": "346w34",
   "ApiKey": "xxx",
   "GroupId": "ion",
  "VoiceType":"xioawei"
}
```
## cartesia
```
{  
  "Model":"xxxx",
   "ApiKey": "xxx",
  "VoiceId":"xioawei"
}
```
## aliyun
```
{
   "VoiceType": 100203,
   "RegionId": "XXXX",
   "ApiKey": "XXXXX"
}
```
## volcengine
```
{
   "AppId": "346w34",
   "AccessToken": "xxx",
   "ResourceId": "volc.bigasr.sauc.duration",
  "VoiceType":"xioawei"
}
```

        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Speed(self):
        r"""温度
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def Volume(self):
        r"""最大token数
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Pitch(self):
        r"""PITCH
        :rtype: float
        """
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch


    def _deserialize(self, params):
        self._TTSType = params.get("TTSType")
        self._Enabled = params.get("Enabled")
        self._Config = params.get("Config")
        self._Speed = params.get("Speed")
        self._Volume = params.get("Volume")
        self._Pitch = params.get("Pitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetInfo(AbstractModel):
    r"""视频语义搜索结果

    """

    def __init__(self):
        r"""
        :param _Id: 视频唯一ID
        :type Id: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _StartTimeMs: 视频起始时间（毫秒级Unix时间戳）
        :type StartTimeMs: int
        :param _EndTimeMs: 视频结束时间（毫秒级Unix时间戳）
        :type EndTimeMs: int
        :param _EventId: 用户自定义事件ID，后续扩展使用
        :type EventId: str
        :param _Summary: 视频内容摘要
        :type Summary: str
        :param _ChannelId: 通道ID
        :type ChannelId: int
        :param _Thumbnail: 缩略图路径
        :type Thumbnail: str
        """
        self._Id = None
        self._ProductId = None
        self._DeviceName = None
        self._StartTimeMs = None
        self._EndTimeMs = None
        self._EventId = None
        self._Summary = None
        self._ChannelId = None
        self._Thumbnail = None

    @property
    def Id(self):
        r"""视频唯一ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def StartTimeMs(self):
        r"""视频起始时间（毫秒级Unix时间戳）
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTimeMs(self):
        r"""视频结束时间（毫秒级Unix时间戳）
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def EventId(self):
        r"""用户自定义事件ID，后续扩展使用
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Summary(self):
        r"""视频内容摘要
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def ChannelId(self):
        r"""通道ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Thumbnail(self):
        r"""缩略图路径
        :rtype: str
        """
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTimeMs = params.get("EndTimeMs")
        self._EventId = params.get("EventId")
        self._Summary = params.get("Summary")
        self._ChannelId = params.get("ChannelId")
        self._Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThumbnailURLInfoList(AbstractModel):
    r"""缩略图信息

    """

    def __init__(self):
        r"""
        :param _ThumbnailURL: 缩略图访问地址
        :type ThumbnailURL: str
        :param _ExpireTime: 缩略图访问地址的过期时间
        :type ExpireTime: int
        """
        self._ThumbnailURL = None
        self._ExpireTime = None

    @property
    def ThumbnailURL(self):
        r"""缩略图访问地址
        :rtype: str
        """
        return self._ThumbnailURL

    @ThumbnailURL.setter
    def ThumbnailURL(self, ThumbnailURL):
        self._ThumbnailURL = ThumbnailURL

    @property
    def ExpireTime(self):
        r"""缩略图访问地址的过期时间
        :rtype: int
        """
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
    r"""Topic信息, 包括Topic名字和权限

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
        r"""Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Privilege(self):
        r"""Topic权限 , 1上报  2下发
        :rtype: int
        """
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
    r"""TopicRule结构

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称。
        :type RuleName: str
        :param _Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param _Description: 规则描述。
        :type Description: str
        :param _Actions: 行为的JSON字符串。
        :type Actions: str
        :param _RuleDisabled: 是否禁用规则
        :type RuleDisabled: bool
        """
        self._RuleName = None
        self._Sql = None
        self._Description = None
        self._Actions = None
        self._RuleDisabled = None

    @property
    def RuleName(self):
        r"""规则名称。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Sql(self):
        r"""规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Description(self):
        r"""规则描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Actions(self):
        r"""行为的JSON字符串。
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def RuleDisabled(self):
        r"""是否禁用规则
        :rtype: bool
        """
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
    r"""规则信息

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
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RuleDisabled(self):
        r"""规则是否禁用
        :rtype: bool
        """
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
    r"""TopicRulePayload结构

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
        r"""规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Actions(self):
        r"""行为的JSON字符串，大部分种类举例如下：
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
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleDisabled(self):
        r"""是否禁用规则
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
        


class TransferCloudStorageRequest(AbstractModel):
    r"""TransferCloudStorage请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""已开通云存的设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ToDeviceName(self):
        r"""未开通云存的设备名称
        :rtype: str
        """
        return self._ToDeviceName

    @ToDeviceName.setter
    def ToDeviceName(self, ToDeviceName):
        self._ToDeviceName = ToDeviceName

    @property
    def ToProductId(self):
        r"""未开通云存的设备产品ID
        :rtype: str
        """
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
    r"""TransferCloudStorage返回参数结构体

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


class TransferTWeCallDeviceRequest(AbstractModel):
    r"""TransferTWeCallDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TransferInDevice: sn信息，product_deviceName
        :type TransferInDevice: str
        :param _TransferOutDevice: sn信息，product_deviceName
        :type TransferOutDevice: str
        """
        self._TransferInDevice = None
        self._TransferOutDevice = None

    @property
    def TransferInDevice(self):
        r"""sn信息，product_deviceName
        :rtype: str
        """
        return self._TransferInDevice

    @TransferInDevice.setter
    def TransferInDevice(self, TransferInDevice):
        self._TransferInDevice = TransferInDevice

    @property
    def TransferOutDevice(self):
        r"""sn信息，product_deviceName
        :rtype: str
        """
        return self._TransferOutDevice

    @TransferOutDevice.setter
    def TransferOutDevice(self, TransferOutDevice):
        self._TransferOutDevice = TransferOutDevice


    def _deserialize(self, params):
        self._TransferInDevice = params.get("TransferInDevice")
        self._TransferOutDevice = params.get("TransferOutDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferTWeCallDeviceResponse(AbstractModel):
    r"""TransferTWeCallDevice返回参数结构体

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


class UnbindDevicesRequest(AbstractModel):
    r"""UnbindDevices请求参数结构体

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
        r"""网关设备的产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def GatewayDeviceName(self):
        r"""网关设备的设备名
        :rtype: str
        """
        return self._GatewayDeviceName

    @GatewayDeviceName.setter
    def GatewayDeviceName(self, GatewayDeviceName):
        self._GatewayDeviceName = GatewayDeviceName

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""设备名列表
        :rtype: list of str
        """
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
    r"""UnbindDevices返回参数结构体

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


class UnbindProductsRequest(AbstractModel):
    r"""UnbindProducts请求参数结构体

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
        r"""网关产品ID
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId

    @property
    def ProductIds(self):
        r"""待解绑的子产品ID数组
        :rtype: list of str
        """
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
    r"""UnbindProducts返回参数结构体

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
        r"""绑定了待解绑的LoRa产品下的设备的网关设备列表
        :rtype: list of str
        """
        return self._GatewayDeviceNames

    @GatewayDeviceNames.setter
    def GatewayDeviceNames(self, GatewayDeviceNames):
        self._GatewayDeviceNames = GatewayDeviceNames

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
        self._GatewayDeviceNames = params.get("GatewayDeviceNames")
        self._RequestId = params.get("RequestId")


class UpdateDeviceTWeCallAuthorizeStatusRequest(AbstractModel):
    r"""UpdateDeviceTWeCallAuthorizeStatus请求参数结构体

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
        r"""TweCall授权状态：0未授权，1已授权
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def WechatOpenId(self):
        r"""微信用户的openId
        :rtype: str
        """
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
    r"""UpdateDeviceTWeCallAuthorizeStatus返回参数结构体

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


class UpdateDevicesEnableStateRequest(AbstractModel):
    r"""UpdateDevicesEnableState请求参数结构体

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
        r"""多个设备标识
        :rtype: list of DevicesItem
        """
        return self._DevicesItems

    @DevicesItems.setter
    def DevicesItems(self, DevicesItems):
        self._DevicesItems = DevicesItems

    @property
    def Status(self):
        r"""1：启用；0：禁用
        :rtype: int
        """
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
    r"""UpdateDevicesEnableState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 删除的结果代码
        :type ResultCode: str
        :param _ResultMessage: 删除的结果信息
        :type ResultMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ResultMessage = None
        self._RequestId = None

    @property
    def ResultCode(self):
        r"""删除的结果代码
        :rtype: str
        """
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMessage(self):
        r"""删除的结果信息
        :rtype: str
        """
        return self._ResultMessage

    @ResultMessage.setter
    def ResultMessage(self, ResultMessage):
        self._ResultMessage = ResultMessage

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
        self._ResultCode = params.get("ResultCode")
        self._ResultMessage = params.get("ResultMessage")
        self._RequestId = params.get("RequestId")


class UpdateFirmwareRequest(AbstractModel):
    r"""UpdateFirmware请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        r"""固件新的版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareOriVersion(self):
        r"""固件原版本号
        :rtype: str
        """
        return self._FirmwareOriVersion

    @FirmwareOriVersion.setter
    def FirmwareOriVersion(self, FirmwareOriVersion):
        self._FirmwareOriVersion = FirmwareOriVersion

    @property
    def UpgradeMethod(self):
        r"""固件升级方式；0 静默升级 1 用户确认升级   不填默认静默升级
        :rtype: int
        """
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
    r"""UpdateFirmware返回参数结构体

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


class UpdateOtaModuleRequest(AbstractModel):
    r"""UpdateOtaModule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FwType: 模块类型
        :type FwType: str
        :param _Name: 模块类型名称
        :type Name: str
        :param _Remark: 模块类型描述
        :type Remark: str
        """
        self._ProductID = None
        self._FwType = None
        self._Name = None
        self._Remark = None

    @property
    def ProductID(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FwType(self):
        r"""模块类型
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Name(self):
        r"""模块类型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""模块类型描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FwType = params.get("FwType")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOtaModuleResponse(AbstractModel):
    r"""UpdateOtaModule返回参数结构体

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


class UpdateOtaTaskStatusRequest(AbstractModel):
    r"""UpdateOtaTaskStatus请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TaskId(self):
        r"""固件升级任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""固件任务取消状态
        :rtype: int
        """
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
    r"""UpdateOtaTaskStatus返回参数结构体

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


class UploadFirmwareRequest(AbstractModel):
    r"""UploadFirmware请求参数结构体

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
        r"""产品ID
        :rtype: str
        """
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        r"""固件版本号
        :rtype: str
        """
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Md5sum(self):
        r"""固件的MD5值
        :rtype: str
        """
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def FileSize(self):
        r"""固件的大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FirmwareName(self):
        r"""固件名称
        :rtype: str
        """
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        r"""固件描述
        :rtype: str
        """
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription

    @property
    def FwType(self):
        r"""固件升级模块；可选值 mcu|moudule
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def FirmwareUserDefined(self):
        r"""固件用户自定义配置信息
        :rtype: str
        """
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
    r"""UploadFirmware返回参数结构体

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


class VideoLicenseEntity(AbstractModel):
    r"""视频设备激活码统计

    """

    def __init__(self):
        r"""
        :param _Type: 激活码类型，取值范围如下：0_5_mbps、1_mbps、1_5_mbps、2_mbps
        :type Type: str
        :param _TotalCount: 有效激活码总数
        :type TotalCount: int
        :param _UsedCount: 待使用的激活码数量
        :type UsedCount: int
        :param _ExpiresSoonCount: 即将过期的激活码数量
        :type ExpiresSoonCount: int
        """
        self._Type = None
        self._TotalCount = None
        self._UsedCount = None
        self._ExpiresSoonCount = None

    @property
    def Type(self):
        r"""激活码类型，取值范围如下：0_5_mbps、1_mbps、1_5_mbps、2_mbps
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TotalCount(self):
        r"""有效激活码总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UsedCount(self):
        r"""待使用的激活码数量
        :rtype: int
        """
        return self._UsedCount

    @UsedCount.setter
    def UsedCount(self, UsedCount):
        self._UsedCount = UsedCount

    @property
    def ExpiresSoonCount(self):
        r"""即将过期的激活码数量
        :rtype: int
        """
        return self._ExpiresSoonCount

    @ExpiresSoonCount.setter
    def ExpiresSoonCount(self, ExpiresSoonCount):
        self._ExpiresSoonCount = ExpiresSoonCount


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TotalCount = params.get("TotalCount")
        self._UsedCount = params.get("UsedCount")
        self._ExpiresSoonCount = params.get("ExpiresSoonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VisionObjectDetectConfig(AbstractModel):
    r"""目标检测配置

    """

    def __init__(self):
        r"""
        :param _DetectTypes: 检测类别，可选值：
- `adult`：成年人
- `child`：儿童
        :type DetectTypes: list of str
        """
        self._DetectTypes = None

    @property
    def DetectTypes(self):
        r"""检测类别，可选值：
- `adult`：成年人
- `child`：儿童
        :rtype: list of str
        """
        return self._DetectTypes

    @DetectTypes.setter
    def DetectTypes(self, DetectTypes):
        self._DetectTypes = DetectTypes


    def _deserialize(self, params):
        self._DetectTypes = params.get("DetectTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VisionRecognitionResult(AbstractModel):
    r"""TWeSee 语义理解结果

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态（1：分析失败；2：下载/读取视频/图片失败；3：成功；4：执行中）
        :type Status: int
        :param _DetectedClassifications: 识别到的目标类型。可能取值：

- `person`：人
- `vehicle`：车辆
- `dog`：狗
- `cat`：猫
- `fire`：火焰
- `smoke`：烟雾
- `package`：快递包裹
- `license_plate`：车牌
        :type DetectedClassifications: list of str
        :param _Summary: 摘要文本
        :type Summary: str
        :param _AlternativeSummary: 摘要文本（次选语言）
        :type AlternativeSummary: str
        :param _ErrorCode: 错误码，可能取值：

- `DownloadFailed`：下载视频/图片文件失败
- `ReadFailed`：读取视频/图片文件失败
        :type ErrorCode: str
        """
        self._Status = None
        self._DetectedClassifications = None
        self._Summary = None
        self._AlternativeSummary = None
        self._ErrorCode = None

    @property
    def Status(self):
        r"""任务状态（1：分析失败；2：下载/读取视频/图片失败；3：成功；4：执行中）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DetectedClassifications(self):
        r"""识别到的目标类型。可能取值：

- `person`：人
- `vehicle`：车辆
- `dog`：狗
- `cat`：猫
- `fire`：火焰
- `smoke`：烟雾
- `package`：快递包裹
- `license_plate`：车牌
        :rtype: list of str
        """
        return self._DetectedClassifications

    @DetectedClassifications.setter
    def DetectedClassifications(self, DetectedClassifications):
        self._DetectedClassifications = DetectedClassifications

    @property
    def Summary(self):
        r"""摘要文本
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def AlternativeSummary(self):
        r"""摘要文本（次选语言）
        :rtype: str
        """
        return self._AlternativeSummary

    @AlternativeSummary.setter
    def AlternativeSummary(self, AlternativeSummary):
        self._AlternativeSummary = AlternativeSummary

    @property
    def ErrorCode(self):
        r"""错误码，可能取值：

- `DownloadFailed`：下载视频/图片文件失败
- `ReadFailed`：读取视频/图片文件失败
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DetectedClassifications = params.get("DetectedClassifications")
        self._Summary = params.get("Summary")
        self._AlternativeSummary = params.get("AlternativeSummary")
        self._ErrorCode = params.get("ErrorCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VisionRecognitionTask(AbstractModel):
    r"""TWeSee 语义理解任务信息

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
        :param _StartTime: 对应云存视频的起始时间（秒级 UNIX 时间戳）
        :type StartTime: int
        :param _StartTimeMs: 对应云存视频的起始时间（毫秒级 UNIX 时间戳）
        :type StartTimeMs: int
        :param _EndTime: 对应云存视频的结束时间（秒级 UNIX 时间戳）
        :type EndTime: int
        :param _EndTimeMs: 对应云存视频的结束时间（毫秒级 UNIX 时间戳）
        :type EndTimeMs: int
        :param _Status: 任务状态（1：分析失败；2：下载/读取视频/图片失败；3：成功；4：执行中）
        :type Status: int
        :param _Result: 任务结果
        :type Result: :class:`tencentcloud.iotexplorer.v20190423.models.VisionRecognitionResult`
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 最后更新时间
        :type UpdateTime: int
        :param _CustomId: 自定义任务 ID
        :type CustomId: str
        :param _Files: 任务输出文件列表
        :type Files: list of str
        :param _FilesInfo: 任务输出文件信息列表
        :type FilesInfo: list of CloudStorageAIServiceTaskFileInfo
        """
        self._TaskId = None
        self._ProductId = None
        self._DeviceName = None
        self._ChannelId = None
        self._StartTime = None
        self._StartTimeMs = None
        self._EndTime = None
        self._EndTimeMs = None
        self._Status = None
        self._Result = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CustomId = None
        self._Files = None
        self._FilesInfo = None

    @property
    def TaskId(self):
        r"""云存 AI 服务任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProductId(self):
        r"""产品 ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def ChannelId(self):
        r"""通道 ID
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        r"""对应云存视频的起始时间（秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StartTimeMs(self):
        r"""对应云存视频的起始时间（毫秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._StartTimeMs

    @StartTimeMs.setter
    def StartTimeMs(self, StartTimeMs):
        self._StartTimeMs = StartTimeMs

    @property
    def EndTime(self):
        r"""对应云存视频的结束时间（秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EndTimeMs(self):
        r"""对应云存视频的结束时间（毫秒级 UNIX 时间戳）
        :rtype: int
        """
        return self._EndTimeMs

    @EndTimeMs.setter
    def EndTimeMs(self, EndTimeMs):
        self._EndTimeMs = EndTimeMs

    @property
    def Status(self):
        r"""任务状态（1：分析失败；2：下载/读取视频/图片失败；3：成功；4：执行中）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        r"""任务结果
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.VisionRecognitionResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最后更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CustomId(self):
        r"""自定义任务 ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def Files(self):
        r"""任务输出文件列表
        :rtype: list of str
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def FilesInfo(self):
        r"""任务输出文件信息列表
        :rtype: list of CloudStorageAIServiceTaskFileInfo
        """
        return self._FilesInfo

    @FilesInfo.setter
    def FilesInfo(self, FilesInfo):
        self._FilesInfo = FilesInfo


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._StartTimeMs = params.get("StartTimeMs")
        self._EndTime = params.get("EndTime")
        self._EndTimeMs = params.get("EndTimeMs")
        self._Status = params.get("Status")
        if params.get("Result") is not None:
            self._Result = VisionRecognitionResult()
            self._Result._deserialize(params.get("Result"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CustomId = params.get("CustomId")
        self._Files = params.get("Files")
        if params.get("FilesInfo") is not None:
            self._FilesInfo = []
            for item in params.get("FilesInfo"):
                obj = CloudStorageAIServiceTaskFileInfo()
                obj._deserialize(item)
                self._FilesInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VisionSummaryConfig(AbstractModel):
    r"""视频摘要配置

    """

    def __init__(self):
        r"""
        :param _OutputLang: 主输出语言

支持列表如下：
zh 中文
en 英语
ja 日语
ko 韩文
pt-BR 葡萄牙语（巴西）
th 泰语

        :type OutputLang: str
        :param _AlternativeOutputLang: 可选输出语言

支持列表如下：
zh 中文
en 英语
ja 日语
ko 韩文
pt-BR 葡萄牙语（巴西）
th 泰语

        :type AlternativeOutputLang: str
        :param _MultiCameraLayout: 多摄像头布局定义。可能取值：

- 单摄（默认值）：`Single`

- 双摄（纵向排列）- 全部画面：`Vertical,Num=2,Index=0;1`
- 双摄（纵向排列）- 画面1：`Vertical,Num=2,Index=0`
- 双摄（纵向排列）- 画面2：`Vertical,Num=2,Index=1`

- 三摄（纵向排列）- 全部画面：`Vertical,Num=3,Index=0;1;2`
- 三摄（纵向排列）- 画面1：`Vertical,Num=3,Index=0`
- 三摄（纵向排列）- 画面2：`Vertical,Num=3,Index=1`
- 三摄（纵向排列）- 画面3：`Vertical,Num=3,Index=2`
- 三摄（纵向排列）- 画面1+2：`Vertical,Num=3,Index=0;1`
- 三摄（纵向排列）- 画面1+3：`Vertical,Num=3,Index=0;2`
- 三摄（纵向排列）- 画面2+3：`Vertical,Num=3,Index=1;2`
        :type MultiCameraLayout: str
        """
        self._OutputLang = None
        self._AlternativeOutputLang = None
        self._MultiCameraLayout = None

    @property
    def OutputLang(self):
        r"""主输出语言

支持列表如下：
zh 中文
en 英语
ja 日语
ko 韩文
pt-BR 葡萄牙语（巴西）
th 泰语

        :rtype: str
        """
        return self._OutputLang

    @OutputLang.setter
    def OutputLang(self, OutputLang):
        self._OutputLang = OutputLang

    @property
    def AlternativeOutputLang(self):
        r"""可选输出语言

支持列表如下：
zh 中文
en 英语
ja 日语
ko 韩文
pt-BR 葡萄牙语（巴西）
th 泰语

        :rtype: str
        """
        return self._AlternativeOutputLang

    @AlternativeOutputLang.setter
    def AlternativeOutputLang(self, AlternativeOutputLang):
        self._AlternativeOutputLang = AlternativeOutputLang

    @property
    def MultiCameraLayout(self):
        r"""多摄像头布局定义。可能取值：

- 单摄（默认值）：`Single`

- 双摄（纵向排列）- 全部画面：`Vertical,Num=2,Index=0;1`
- 双摄（纵向排列）- 画面1：`Vertical,Num=2,Index=0`
- 双摄（纵向排列）- 画面2：`Vertical,Num=2,Index=1`

- 三摄（纵向排列）- 全部画面：`Vertical,Num=3,Index=0;1;2`
- 三摄（纵向排列）- 画面1：`Vertical,Num=3,Index=0`
- 三摄（纵向排列）- 画面2：`Vertical,Num=3,Index=1`
- 三摄（纵向排列）- 画面3：`Vertical,Num=3,Index=2`
- 三摄（纵向排列）- 画面1+2：`Vertical,Num=3,Index=0;1`
- 三摄（纵向排列）- 画面1+3：`Vertical,Num=3,Index=0;2`
- 三摄（纵向排列）- 画面2+3：`Vertical,Num=3,Index=1;2`
        :rtype: str
        """
        return self._MultiCameraLayout

    @MultiCameraLayout.setter
    def MultiCameraLayout(self, MultiCameraLayout):
        self._MultiCameraLayout = MultiCameraLayout


    def _deserialize(self, params):
        self._OutputLang = params.get("OutputLang")
        self._AlternativeOutputLang = params.get("AlternativeOutputLang")
        self._MultiCameraLayout = params.get("MultiCameraLayout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WXDeviceInfo(AbstractModel):
    r"""微信硬件设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _WXIoTDeviceInfo: 设备信息
        :type WXIoTDeviceInfo: :class:`tencentcloud.iotexplorer.v20190423.models.WXIoTDeviceInfo`
        """
        self._DeviceId = None
        self._WXIoTDeviceInfo = None

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
    def WXIoTDeviceInfo(self):
        r"""设备信息
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.WXIoTDeviceInfo`
        """
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
    r"""微信物联网硬件信息

    """

    def __init__(self):
        r"""
        :param _SN: sn信息
        :type SN: str
        :param _SNTicket: 票据
        :type SNTicket: str
        :param _ModelId: 模板ID
        :type ModelId: str
        """
        self._SN = None
        self._SNTicket = None
        self._ModelId = None

    @property
    def SN(self):
        r"""sn信息
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def SNTicket(self):
        r"""票据
        :rtype: str
        """
        return self._SNTicket

    @SNTicket.setter
    def SNTicket(self, SNTicket):
        self._SNTicket = SNTicket

    @property
    def ModelId(self):
        r"""模板ID
        :rtype: str
        """
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
    r"""wifi定位信息

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
        r"""mac地址
        :rtype: str
        """
        return self._MAC

    @MAC.setter
    def MAC(self, MAC):
        self._MAC = MAC

    @property
    def RSSI(self):
        r"""信号强度
        :rtype: int
        """
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
        