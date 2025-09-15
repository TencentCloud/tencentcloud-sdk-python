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


class AppInfo(AbstractModel):
    r"""应用包名信息

    """

    def __init__(self):
        r"""
        :param _Id: 应用Id
        :type Id: int
        :param _AppId: 用户appid
        :type AppId: str
        :param _AppName: 应用名称
        :type AppName: str
        :param _BundleId: Ios 包名
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _PackageName: Andorid 包名
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _AppType: 应用详情
        :type AppType: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _MacBundleId: Mac 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type MacBundleId: str
        :param _WinProcessName: windows 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type WinProcessName: str
        :param _DomainList: 允许的web域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        """
        self._Id = None
        self._AppId = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._AppType = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._MacBundleId = None
        self._WinProcessName = None
        self._DomainList = None

    @property
    def Id(self):
        r"""应用Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def BundleId(self):
        r"""Ios 包名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""Andorid 包名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def AppType(self):
        r"""应用详情
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def MacBundleId(self):
        r"""Mac 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""windows 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName

    @property
    def DomainList(self):
        r"""允许的web域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._AppType = params.get("AppType")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        self._DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInfo(AbstractModel):
    r"""视立方license用户 应用结构

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称
        :type AppName: str
        :param _BundleId: Ios应用的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _AppType: 应用类型，formal： 正式应用，test：测试应用
        :type AppType: str
        :param _Licenses: license数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Licenses: list of License
        :param _LicenseKey: license 秘钥
        :type LicenseKey: str
        :param _PackageName: 安卓应用的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _ApplicationId: 用户应用Id
        :type ApplicationId: int
        :param _LicenseUrl: 视立方下载license的url
        :type LicenseUrl: str
        :param _XMagics: 优图美视信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type XMagics: list of XMagicInfo
        :param _MacBundleId: Mac  进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type MacBundleId: str
        :param _WinProcessName: windows 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type WinProcessName: str
        :param _DomainList: web端Domain列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        :param _AppId: 账号AppId
        :type AppId: str
        :param _NameLimit: 扩展包名数量上限
        :type NameLimit: int
        """
        self._AppName = None
        self._BundleId = None
        self._AppType = None
        self._Licenses = None
        self._LicenseKey = None
        self._PackageName = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._ApplicationId = None
        self._LicenseUrl = None
        self._XMagics = None
        self._MacBundleId = None
        self._WinProcessName = None
        self._DomainList = None
        self._AppId = None
        self._NameLimit = None

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
    def BundleId(self):
        r"""Ios应用的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def AppType(self):
        r"""应用类型，formal： 正式应用，test：测试应用
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def Licenses(self):
        r"""license数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of License
        """
        return self._Licenses

    @Licenses.setter
    def Licenses(self, Licenses):
        self._Licenses = Licenses

    @property
    def LicenseKey(self):
        r"""license 秘钥
        :rtype: str
        """
        return self._LicenseKey

    @LicenseKey.setter
    def LicenseKey(self, LicenseKey):
        self._LicenseKey = LicenseKey

    @property
    def PackageName(self):
        r"""安卓应用的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ApplicationId(self):
        r"""用户应用Id
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def LicenseUrl(self):
        r"""视立方下载license的url
        :rtype: str
        """
        return self._LicenseUrl

    @LicenseUrl.setter
    def LicenseUrl(self, LicenseUrl):
        self._LicenseUrl = LicenseUrl

    @property
    def XMagics(self):
        r"""优图美视信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of XMagicInfo
        """
        return self._XMagics

    @XMagics.setter
    def XMagics(self, XMagics):
        self._XMagics = XMagics

    @property
    def MacBundleId(self):
        r"""Mac  进程名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""windows 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName

    @property
    def DomainList(self):
        r"""web端Domain列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def AppId(self):
        r"""账号AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def NameLimit(self):
        r"""扩展包名数量上限
        :rtype: int
        """
        return self._NameLimit

    @NameLimit.setter
    def NameLimit(self, NameLimit):
        self._NameLimit = NameLimit


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._AppType = params.get("AppType")
        if params.get("Licenses") is not None:
            self._Licenses = []
            for item in params.get("Licenses"):
                obj = License()
                obj._deserialize(item)
                self._Licenses.append(obj)
        self._LicenseKey = params.get("LicenseKey")
        self._PackageName = params.get("PackageName")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._ApplicationId = params.get("ApplicationId")
        self._LicenseUrl = params.get("LicenseUrl")
        if params.get("XMagics") is not None:
            self._XMagics = []
            for item in params.get("XMagics"):
                obj = XMagicInfo()
                obj._deserialize(item)
                self._XMagics.append(obj)
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        self._DomainList = params.get("DomainList")
        self._AppId = params.get("AppId")
        self._NameLimit = params.get("NameLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateActivityLicenseRequest(AbstractModel):
    r"""CreateActivityLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Activity: 活动Id
        :type Activity: str
        """
        self._Activity = None

    @property
    def Activity(self):
        r"""活动Id
        :rtype: str
        """
        return self._Activity

    @Activity.setter
    def Activity(self, Activity):
        self._Activity = Activity


    def _deserialize(self, params):
        self._Activity = params.get("Activity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateActivityLicenseResponse(AbstractModel):
    r"""CreateActivityLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 用户appid
        :type AppId: str
        :param _AppName: app名称
        :type AppName: str
        :param _BundleId: ios包名
        :type BundleId: str
        :param _PackageName: 安卓包名
        :type PackageName: str
        :param _Duration: 有效时长
        :type Duration: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _LicenseKey: license秘钥
        :type LicenseKey: str
        :param _LicenseUrl: license 授权文件下载链接
        :type LicenseUrl: str
        :param _ResidueDay: license剩余天数，最后一天以及过期显示0
        :type ResidueDay: int
        :param _Residue: license剩余秒数
        :type Residue: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._Duration = None
        self._StartTime = None
        self._EndTime = None
        self._LicenseKey = None
        self._LicenseUrl = None
        self._ResidueDay = None
        self._Residue = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppName(self):
        r"""app名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""ios包名
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""安卓包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Duration(self):
        r"""有效时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def LicenseKey(self):
        r"""license秘钥
        :rtype: str
        """
        return self._LicenseKey

    @LicenseKey.setter
    def LicenseKey(self, LicenseKey):
        self._LicenseKey = LicenseKey

    @property
    def LicenseUrl(self):
        r"""license 授权文件下载链接
        :rtype: str
        """
        return self._LicenseUrl

    @LicenseUrl.setter
    def LicenseUrl(self, LicenseUrl):
        self._LicenseUrl = LicenseUrl

    @property
    def ResidueDay(self):
        r"""license剩余天数，最后一天以及过期显示0
        :rtype: int
        """
        return self._ResidueDay

    @ResidueDay.setter
    def ResidueDay(self, ResidueDay):
        self._ResidueDay = ResidueDay

    @property
    def Residue(self):
        r"""license剩余秒数
        :rtype: int
        """
        return self._Residue

    @Residue.setter
    def Residue(self, Residue):
        self._Residue = Residue

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
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._Duration = params.get("Duration")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._LicenseKey = params.get("LicenseKey")
        self._LicenseUrl = params.get("LicenseUrl")
        self._ResidueDay = params.get("ResidueDay")
        self._Residue = params.get("Residue")
        self._RequestId = params.get("RequestId")


class CreateApplicationAndBindLicenseRequest(AbstractModel):
    r"""CreateApplicationAndBindLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名
        :type AppName: str
        :param _BundleId: 应用ID
        :type BundleId: str
        :param _PackageName: 包名
        :type PackageName: str
        :param _ResourceIds: 资源包ID
        :type ResourceIds: list of str
        :param _CompanyPermit: 营业执照
        :type CompanyPermit: str
        :param _CompanyType: 公司类型
        :type CompanyType: str
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _XMagicResourceIds: 优图资源id列表
        :type XMagicResourceIds: list of str
        :param _MacBundleId: Mac 进程名
        :type MacBundleId: str
        :param _WinProcessName: Windows 进程名
        :type WinProcessName: str
        :param _DomainList: 要开通的域名列表
        :type DomainList: list of str
        :param _Platform: 要开通的端，web/mobile/pc
        :type Platform: str
        """
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._ResourceIds = None
        self._CompanyPermit = None
        self._CompanyType = None
        self._CompanyName = None
        self._XMagicResourceIds = None
        self._MacBundleId = None
        self._WinProcessName = None
        self._DomainList = None
        self._Platform = None

    @property
    def AppName(self):
        r"""应用名
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def ResourceIds(self):
        r"""资源包ID
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def CompanyPermit(self):
        r"""营业执照
        :rtype: str
        """
        return self._CompanyPermit

    @CompanyPermit.setter
    def CompanyPermit(self, CompanyPermit):
        self._CompanyPermit = CompanyPermit

    @property
    def CompanyType(self):
        r"""公司类型
        :rtype: str
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def CompanyName(self):
        r"""公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def XMagicResourceIds(self):
        r"""优图资源id列表
        :rtype: list of str
        """
        return self._XMagicResourceIds

    @XMagicResourceIds.setter
    def XMagicResourceIds(self, XMagicResourceIds):
        self._XMagicResourceIds = XMagicResourceIds

    @property
    def MacBundleId(self):
        r"""Mac 进程名
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""Windows 进程名
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName

    @property
    def DomainList(self):
        r"""要开通的域名列表
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def Platform(self):
        r"""要开通的端，web/mobile/pc
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._ResourceIds = params.get("ResourceIds")
        self._CompanyPermit = params.get("CompanyPermit")
        self._CompanyType = params.get("CompanyType")
        self._CompanyName = params.get("CompanyName")
        self._XMagicResourceIds = params.get("XMagicResourceIds")
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        self._DomainList = params.get("DomainList")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAndBindLicenseResponse(AbstractModel):
    r"""CreateApplicationAndBindLicense返回参数结构体

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


class CreateApplicationAndVideoRequest(AbstractModel):
    r"""CreateApplicationAndVideo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称
        :type AppName: str
        :param _BundleId: Ios 包名
        :type BundleId: str
        :param _PackageName: Android 包名
        :type PackageName: str
        """
        self._AppName = None
        self._BundleId = None
        self._PackageName = None

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
    def BundleId(self):
        r"""Ios 包名
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""Android 包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAndVideoResponse(AbstractModel):
    r"""CreateApplicationAndVideo返回参数结构体

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


class CreateApplicationAndWebPlayerLicenseRequest(AbstractModel):
    r"""CreateApplicationAndWebPlayerLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称
        :type AppName: str
        :param _DomainList: 域名列表
        :type DomainList: list of str
        """
        self._AppName = None
        self._DomainList = None

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
    def DomainList(self):
        r"""域名列表
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAndWebPlayerLicenseResponse(AbstractModel):
    r"""CreateApplicationAndWebPlayerLicense返回参数结构体

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


class CreateLicenseRequest(AbstractModel):
    r"""CreateLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _ResourceIds: 资源包ID
        :type ResourceIds: list of str
        :param _Group: url地址分组
        :type Group: int
        """
        self._ApplicationId = None
        self._ResourceIds = None
        self._Group = None

    @property
    def ApplicationId(self):
        r"""应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ResourceIds(self):
        r"""资源包ID
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Group(self):
        r"""url地址分组
        :rtype: int
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ResourceIds = params.get("ResourceIds")
        self._Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLicenseResponse(AbstractModel):
    r"""CreateLicense返回参数结构体

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


class CreateTestXMagicRequest(AbstractModel):
    r"""CreateTestXMagic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 将腾讯特效创建到哪个应用下
        :type ApplicationId: int
        :param _CompanyPermit: 营业执照
        :type CompanyPermit: str
        :param _CompanyType: 公司类型
        :type CompanyType: str
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _PlanList: 测试套餐名称
        :type PlanList: list of str
        """
        self._ApplicationId = None
        self._CompanyPermit = None
        self._CompanyType = None
        self._CompanyName = None
        self._PlanList = None

    @property
    def ApplicationId(self):
        r"""将腾讯特效创建到哪个应用下
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def CompanyPermit(self):
        r"""营业执照
        :rtype: str
        """
        return self._CompanyPermit

    @CompanyPermit.setter
    def CompanyPermit(self, CompanyPermit):
        self._CompanyPermit = CompanyPermit

    @property
    def CompanyType(self):
        r"""公司类型
        :rtype: str
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def CompanyName(self):
        r"""公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def PlanList(self):
        r"""测试套餐名称
        :rtype: list of str
        """
        return self._PlanList

    @PlanList.setter
    def PlanList(self, PlanList):
        self._PlanList = PlanList


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._CompanyPermit = params.get("CompanyPermit")
        self._CompanyType = params.get("CompanyType")
        self._CompanyName = params.get("CompanyName")
        self._PlanList = params.get("PlanList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTestXMagicResponse(AbstractModel):
    r"""CreateTestXMagic返回参数结构体

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


class CreateTrialApplicationAndLicenseRequest(AbstractModel):
    r"""CreateTrialApplicationAndLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名
        :type AppName: str
        :param _BundleId: 应用ID
        :type BundleId: str
        :param _PackageName: 包名
        :type PackageName: str
        :param _FeatureIds: 功能 id 数组
        :type FeatureIds: list of int
        :param _XMagic: 是否要开通优图功能
        :type XMagic: bool
        :param _CompanyPermit: 营业执照
        :type CompanyPermit: str
        :param _CompanyType: 公司类型
        :type CompanyType: str
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _PlanList: 要开通的测试功能名称，基础套餐只能有一个
        :type PlanList: list of str
        :param _MacBundleId: Mac 进程名
        :type MacBundleId: str
        :param _WinProcessName: Windows 进程名
        :type WinProcessName: str
        :param _Platform: 要创建到哪个平台，web、mobile、pc，默认mobile
        :type Platform: str
        :param _DomainList: 授权域名列表
        :type DomainList: list of str
        """
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._FeatureIds = None
        self._XMagic = None
        self._CompanyPermit = None
        self._CompanyType = None
        self._CompanyName = None
        self._PlanList = None
        self._MacBundleId = None
        self._WinProcessName = None
        self._Platform = None
        self._DomainList = None

    @property
    def AppName(self):
        r"""应用名
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def FeatureIds(self):
        r"""功能 id 数组
        :rtype: list of int
        """
        return self._FeatureIds

    @FeatureIds.setter
    def FeatureIds(self, FeatureIds):
        self._FeatureIds = FeatureIds

    @property
    def XMagic(self):
        r"""是否要开通优图功能
        :rtype: bool
        """
        return self._XMagic

    @XMagic.setter
    def XMagic(self, XMagic):
        self._XMagic = XMagic

    @property
    def CompanyPermit(self):
        r"""营业执照
        :rtype: str
        """
        return self._CompanyPermit

    @CompanyPermit.setter
    def CompanyPermit(self, CompanyPermit):
        self._CompanyPermit = CompanyPermit

    @property
    def CompanyType(self):
        r"""公司类型
        :rtype: str
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def CompanyName(self):
        r"""公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def PlanList(self):
        r"""要开通的测试功能名称，基础套餐只能有一个
        :rtype: list of str
        """
        return self._PlanList

    @PlanList.setter
    def PlanList(self, PlanList):
        self._PlanList = PlanList

    @property
    def MacBundleId(self):
        r"""Mac 进程名
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""Windows 进程名
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName

    @property
    def Platform(self):
        r"""要创建到哪个平台，web、mobile、pc，默认mobile
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def DomainList(self):
        r"""授权域名列表
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._FeatureIds = params.get("FeatureIds")
        self._XMagic = params.get("XMagic")
        self._CompanyPermit = params.get("CompanyPermit")
        self._CompanyType = params.get("CompanyType")
        self._CompanyName = params.get("CompanyName")
        self._PlanList = params.get("PlanList")
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        self._Platform = params.get("Platform")
        self._DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrialApplicationAndLicenseResponse(AbstractModel):
    r"""CreateTrialApplicationAndLicense返回参数结构体

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


class CreateTrialLicenseRequest(AbstractModel):
    r"""CreateTrialLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _FeatureIds: 功能 ID 数组
        :type FeatureIds: list of int non-negative
        :param _Group: Url分组
        :type Group: int
        """
        self._ApplicationId = None
        self._FeatureIds = None
        self._Group = None

    @property
    def ApplicationId(self):
        r"""应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def FeatureIds(self):
        r"""功能 ID 数组
        :rtype: list of int non-negative
        """
        return self._FeatureIds

    @FeatureIds.setter
    def FeatureIds(self, FeatureIds):
        self._FeatureIds = FeatureIds

    @property
    def Group(self):
        r"""Url分组
        :rtype: int
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._FeatureIds = params.get("FeatureIds")
        self._Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrialLicenseResponse(AbstractModel):
    r"""CreateTrialLicense返回参数结构体

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


class CreateXMagicRequest(AbstractModel):
    r"""CreateXMagic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ApplicationId
        :type ApplicationId: int
        :param _CompanyPermit: 营业执照
        :type CompanyPermit: str
        :param _CompanyType: 公司类型
        :type CompanyType: str
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _XMagicResourceIds: 优图资源id列表
        :type XMagicResourceIds: list of str
        """
        self._ApplicationId = None
        self._CompanyPermit = None
        self._CompanyType = None
        self._CompanyName = None
        self._XMagicResourceIds = None

    @property
    def ApplicationId(self):
        r"""应用ApplicationId
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def CompanyPermit(self):
        r"""营业执照
        :rtype: str
        """
        return self._CompanyPermit

    @CompanyPermit.setter
    def CompanyPermit(self, CompanyPermit):
        self._CompanyPermit = CompanyPermit

    @property
    def CompanyType(self):
        r"""公司类型
        :rtype: str
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def CompanyName(self):
        r"""公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def XMagicResourceIds(self):
        r"""优图资源id列表
        :rtype: list of str
        """
        return self._XMagicResourceIds

    @XMagicResourceIds.setter
    def XMagicResourceIds(self, XMagicResourceIds):
        self._XMagicResourceIds = XMagicResourceIds


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._CompanyPermit = params.get("CompanyPermit")
        self._CompanyType = params.get("CompanyType")
        self._CompanyName = params.get("CompanyName")
        self._XMagicResourceIds = params.get("XMagicResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateXMagicResponse(AbstractModel):
    r"""CreateXMagic返回参数结构体

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


class DescribeFeatureListRequest(AbstractModel):
    r"""DescribeFeatureList请求参数结构体

    """


class DescribeFeatureListResponse(AbstractModel):
    r"""DescribeFeatureList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FeatureList: 功能列表
        :type FeatureList: list of VideoFeature
        :param _XMagicFeatureList: 优图功能列表
        :type XMagicFeatureList: list of XMagicFeature
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FeatureList = None
        self._XMagicFeatureList = None
        self._RequestId = None

    @property
    def FeatureList(self):
        r"""功能列表
        :rtype: list of VideoFeature
        """
        return self._FeatureList

    @FeatureList.setter
    def FeatureList(self, FeatureList):
        self._FeatureList = FeatureList

    @property
    def XMagicFeatureList(self):
        r"""优图功能列表
        :rtype: list of XMagicFeature
        """
        return self._XMagicFeatureList

    @XMagicFeatureList.setter
    def XMagicFeatureList(self, XMagicFeatureList):
        self._XMagicFeatureList = XMagicFeatureList

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
        if params.get("FeatureList") is not None:
            self._FeatureList = []
            for item in params.get("FeatureList"):
                obj = VideoFeature()
                obj._deserialize(item)
                self._FeatureList.append(obj)
        if params.get("XMagicFeatureList") is not None:
            self._XMagicFeatureList = []
            for item in params.get("XMagicFeatureList"):
                obj = XMagicFeature()
                obj._deserialize(item)
                self._XMagicFeatureList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLicenseListRequest(AbstractModel):
    r"""DescribeLicenseList请求参数结构体

    """


class DescribeLicenseListResponse(AbstractModel):
    r"""DescribeLicenseList返回参数结构体

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


class DescribeNewsRequest(AbstractModel):
    r"""DescribeNews请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码，从0开始
        :type PageNumber: int
        :param _PageSize: 每页数据量
        :type PageSize: int
        """
        self._PageNumber = None
        self._PageSize = None

    @property
    def PageNumber(self):
        r"""页码，从0开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数据量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewsResponse(AbstractModel):
    r"""DescribeNews返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NewsList: 产品动态详情列表
        :type NewsList: list of NewsInfo
        :param _Count: 总数据量
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NewsList = None
        self._Count = None
        self._RequestId = None

    @property
    def NewsList(self):
        r"""产品动态详情列表
        :rtype: list of NewsInfo
        """
        return self._NewsList

    @NewsList.setter
    def NewsList(self, NewsList):
        self._NewsList = NewsList

    @property
    def Count(self):
        r"""总数据量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        if params.get("NewsList") is not None:
            self._NewsList = []
            for item in params.get("NewsList"):
                obj = NewsInfo()
                obj._deserialize(item)
                self._NewsList.append(obj)
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeSTSRequest(AbstractModel):
    r"""DescribeSTS请求参数结构体

    """


class DescribeSTSResponse(AbstractModel):
    r"""DescribeSTS返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Bucket: 桶名称
        :type Bucket: str
        :param _Region: 地区
        :type Region: str
        :param _StartTime: 开始生效时间
        :type StartTime: int
        :param _ExpiredTime: 临时token过期时间
        :type ExpiredTime: int
        :param _SessionToken: 临时token
        :type SessionToken: str
        :param _TmpSecretId: 临时SecretId
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时秘钥
        :type TmpSecretKey: str
        :param _Path: 上传的根路径，底下可以多层
        :type Path: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Bucket = None
        self._Region = None
        self._StartTime = None
        self._ExpiredTime = None
        self._SessionToken = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Path = None
        self._RequestId = None

    @property
    def Bucket(self):
        r"""桶名称
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""地区
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def StartTime(self):
        r"""开始生效时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        r"""临时token过期时间
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SessionToken(self):
        r"""临时token
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def TmpSecretId(self):
        r"""临时SecretId
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""临时秘钥
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Path(self):
        r"""上传的根路径，底下可以多层
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

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
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._SessionToken = params.get("SessionToken")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Path = params.get("Path")
        self._RequestId = params.get("RequestId")


class DescribeTrialFeatureRequest(AbstractModel):
    r"""DescribeTrialFeature请求参数结构体

    """


class DescribeTrialFeatureResponse(AbstractModel):
    r"""DescribeTrialFeature返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FeatureList: 功能列表
        :type FeatureList: list of Feature
        :param _XMagicTrial: 可以开通的优图测试功能
注意：此字段可能返回 null，表示取不到有效值。
        :type XMagicTrial: :class:`tencentcloud.vcube.v20220410.models.XMagicTrial`
        :param _XMagicTrialList: 可以开通的优图测试功能列表
        :type XMagicTrialList: list of XMagicTrial
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FeatureList = None
        self._XMagicTrial = None
        self._XMagicTrialList = None
        self._RequestId = None

    @property
    def FeatureList(self):
        r"""功能列表
        :rtype: list of Feature
        """
        return self._FeatureList

    @FeatureList.setter
    def FeatureList(self, FeatureList):
        self._FeatureList = FeatureList

    @property
    def XMagicTrial(self):
        r"""可以开通的优图测试功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.XMagicTrial`
        """
        return self._XMagicTrial

    @XMagicTrial.setter
    def XMagicTrial(self, XMagicTrial):
        self._XMagicTrial = XMagicTrial

    @property
    def XMagicTrialList(self):
        r"""可以开通的优图测试功能列表
        :rtype: list of XMagicTrial
        """
        return self._XMagicTrialList

    @XMagicTrialList.setter
    def XMagicTrialList(self, XMagicTrialList):
        self._XMagicTrialList = XMagicTrialList

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
        if params.get("FeatureList") is not None:
            self._FeatureList = []
            for item in params.get("FeatureList"):
                obj = Feature()
                obj._deserialize(item)
                self._FeatureList.append(obj)
        if params.get("XMagicTrial") is not None:
            self._XMagicTrial = XMagicTrial()
            self._XMagicTrial._deserialize(params.get("XMagicTrial"))
        if params.get("XMagicTrialList") is not None:
            self._XMagicTrialList = []
            for item in params.get("XMagicTrialList"):
                obj = XMagicTrial()
                obj._deserialize(item)
                self._XMagicTrialList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserConfigRequest(AbstractModel):
    r"""DescribeUserConfig请求参数结构体

    """


class DescribeUserConfigResponse(AbstractModel):
    r"""DescribeUserConfig返回参数结构体

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


class DescribeVcubeApplicationAndLicenseRequest(AbstractModel):
    r"""DescribeVcubeApplicationAndLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 查询对应业务方的license，直播:live 点播：vod
        :type BizType: str
        :param _AppType: 应用类型测试：test，正式：formal
        :type AppType: str
        :param _AppName: 应用名称，模糊查询
        :type AppName: str
        :param _BundleId: Ios包名，模糊查询
        :type BundleId: str
        :param _PackageName: Android 包名，模糊查询
        :type PackageName: str
        :param _Platform: 平台信息，pc 或者 mobile
        :type Platform: str
        :param _MacBundleId: Mac 进程名
        :type MacBundleId: str
        :param _WinProcessName: Windows 进程名
        :type WinProcessName: str
        """
        self._BizType = None
        self._AppType = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._Platform = None
        self._MacBundleId = None
        self._WinProcessName = None

    @property
    def BizType(self):
        r"""查询对应业务方的license，直播:live 点播：vod
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def AppType(self):
        r"""应用类型测试：test，正式：formal
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppName(self):
        r"""应用名称，模糊查询
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""Ios包名，模糊查询
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""Android 包名，模糊查询
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        r"""平台信息，pc 或者 mobile
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MacBundleId(self):
        r"""Mac 进程名
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""Windows 进程名
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._AppType = params.get("AppType")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVcubeApplicationAndLicenseResponse(AbstractModel):
    r"""DescribeVcubeApplicationAndLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationInfoList: 应用license列表
        :type ApplicationInfoList: list of ApplicationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationInfoList = None
        self._RequestId = None

    @property
    def ApplicationInfoList(self):
        r"""应用license列表
        :rtype: list of ApplicationInfo
        """
        return self._ApplicationInfoList

    @ApplicationInfoList.setter
    def ApplicationInfoList(self, ApplicationInfoList):
        self._ApplicationInfoList = ApplicationInfoList

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
        if params.get("ApplicationInfoList") is not None:
            self._ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInfo()
                obj._deserialize(item)
                self._ApplicationInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVcubeApplicationAndPlayListRequest(AbstractModel):
    r"""DescribeVcubeApplicationAndPlayList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 查询对应业务方的license，直播:live 点播：vod
        :type BizType: str
        :param _AppType: 应用类型测试：test，正式：formal
        :type AppType: str
        :param _AppName: 应用名称，模糊查询
        :type AppName: str
        :param _BundleId: Ios包名，模糊查询
        :type BundleId: str
        :param _PackageName: Android 包名，模糊查询
        :type PackageName: str
        :param _Platform: 平台信息，pc 或者 mobile
        :type Platform: str
        :param _MacBundleId: Mac 进程名
        :type MacBundleId: str
        :param _WinProcessName: Windows 进程名
        :type WinProcessName: str
        """
        self._BizType = None
        self._AppType = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._Platform = None
        self._MacBundleId = None
        self._WinProcessName = None

    @property
    def BizType(self):
        r"""查询对应业务方的license，直播:live 点播：vod
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def AppType(self):
        r"""应用类型测试：test，正式：formal
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppName(self):
        r"""应用名称，模糊查询
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""Ios包名，模糊查询
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""Android 包名，模糊查询
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        r"""平台信息，pc 或者 mobile
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MacBundleId(self):
        r"""Mac 进程名
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""Windows 进程名
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._AppType = params.get("AppType")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVcubeApplicationAndPlayListResponse(AbstractModel):
    r"""DescribeVcubeApplicationAndPlayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationInfoList: 应用license列表
        :type ApplicationInfoList: list of ApplicationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationInfoList = None
        self._RequestId = None

    @property
    def ApplicationInfoList(self):
        r"""应用license列表
        :rtype: list of ApplicationInfo
        """
        return self._ApplicationInfoList

    @ApplicationInfoList.setter
    def ApplicationInfoList(self, ApplicationInfoList):
        self._ApplicationInfoList = ApplicationInfoList

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
        if params.get("ApplicationInfoList") is not None:
            self._ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInfo()
                obj._deserialize(item)
                self._ApplicationInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVcubeApplicationAndXMagicListRequest(AbstractModel):
    r"""DescribeVcubeApplicationAndXMagicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 查询对应业务方的license，直播:live 点播：vod
        :type BizType: str
        :param _AppType: 应用类型测试：test，正式：formal
        :type AppType: str
        :param _AppName: 应用名称，模糊查询
        :type AppName: str
        :param _BundleId: Ios包名，模糊查询
        :type BundleId: str
        :param _PackageName: Android 包名，模糊查询
        :type PackageName: str
        :param _Platform: 平台信息，pc 或者 mobile
        :type Platform: str
        :param _MacBundleId: Mac 进程名
        :type MacBundleId: str
        :param _WinProcessName: Windows 进程名
        :type WinProcessName: str
        """
        self._BizType = None
        self._AppType = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._Platform = None
        self._MacBundleId = None
        self._WinProcessName = None

    @property
    def BizType(self):
        r"""查询对应业务方的license，直播:live 点播：vod
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def AppType(self):
        r"""应用类型测试：test，正式：formal
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppName(self):
        r"""应用名称，模糊查询
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""Ios包名，模糊查询
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""Android 包名，模糊查询
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        r"""平台信息，pc 或者 mobile
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MacBundleId(self):
        r"""Mac 进程名
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def WinProcessName(self):
        r"""Windows 进程名
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._AppType = params.get("AppType")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._MacBundleId = params.get("MacBundleId")
        self._WinProcessName = params.get("WinProcessName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVcubeApplicationAndXMagicListResponse(AbstractModel):
    r"""DescribeVcubeApplicationAndXMagicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationInfoList: 应用license列表
        :type ApplicationInfoList: list of ApplicationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationInfoList = None
        self._RequestId = None

    @property
    def ApplicationInfoList(self):
        r"""应用license列表
        :rtype: list of ApplicationInfo
        """
        return self._ApplicationInfoList

    @ApplicationInfoList.setter
    def ApplicationInfoList(self, ApplicationInfoList):
        self._ApplicationInfoList = ApplicationInfoList

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
        if params.get("ApplicationInfoList") is not None:
            self._ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInfo()
                obj._deserialize(item)
                self._ApplicationInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVcubeResourcesListRequest(AbstractModel):
    r"""DescribeVcubeResourcesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 查询资源页码
        :type PageNumber: int
        :param _PageSize: 每页的数据量
        :type PageSize: int
        :param _AppName: 应用名称，模块查询
        :type AppName: str
        :param _ResourceId: 资源Id，资源包id或者license资源id
        :type ResourceId: str
        :param _Word: 资源Id、应用名称、包名
        :type Word: str
        :param _Platform: 查询资源所属平台，web、mobile
        :type Platform: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._AppName = None
        self._ResourceId = None
        self._Word = None
        self._Platform = None

    @property
    def PageNumber(self):
        r"""查询资源页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页的数据量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AppName(self):
        r"""应用名称，模块查询
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ResourceId(self):
        r"""资源Id，资源包id或者license资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Word(self):
        r"""资源Id、应用名称、包名
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Platform(self):
        r"""查询资源所属平台，web、mobile
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._AppName = params.get("AppName")
        self._ResourceId = params.get("ResourceId")
        self._Word = params.get("Word")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVcubeResourcesListResponse(AbstractModel):
    r"""DescribeVcubeResourcesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceList: 资源列表
        :type ResourceList: list of LicenseResourceInfo
        :param _TotalCount: 总数据量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResourceList(self):
        r"""资源列表
        :rtype: list of LicenseResourceInfo
        """
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def TotalCount(self):
        r"""总数据量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ResourceList") is not None:
            self._ResourceList = []
            for item in params.get("ResourceList"):
                obj = LicenseResourceInfo()
                obj._deserialize(item)
                self._ResourceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeVcubeResourcesRequest(AbstractModel):
    r"""DescribeVcubeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 查找那个平台的资源
        :type Platform: str
        """
        self._Platform = None

    @property
    def Platform(self):
        r"""查找那个平台的资源
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVcubeResourcesResponse(AbstractModel):
    r"""DescribeVcubeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceList: 资源列表
        :type ResourceList: list of LicenseResourceSimpleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceList = None
        self._RequestId = None

    @property
    def ResourceList(self):
        r"""资源列表
        :rtype: list of LicenseResourceSimpleInfo
        """
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

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
        if params.get("ResourceList") is not None:
            self._ResourceList = []
            for item in params.get("ResourceList"):
                obj = LicenseResourceSimpleInfo()
                obj._deserialize(item)
                self._ResourceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeXMagicResourceListRequest(AbstractModel):
    r"""DescribeXMagicResourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页页码 第一页是0
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _AppName: 关联的应用名称
        :type AppName: str
        :param _ResourceId: 优图资源Id
        :type ResourceId: str
        :param _Word: 查询关键字，资源Id、应用名称、包名
        :type Word: str
        :param _Platform: 平台信息，pc 或者 mobile
        :type Platform: str
        :param _BizType: 所属业务，xmagic：优图， avatar：虚拟人，不传查全部
        :type BizType: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._AppName = None
        self._ResourceId = None
        self._Word = None
        self._Platform = None
        self._BizType = None

    @property
    def PageNumber(self):
        r"""分页页码 第一页是0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AppName(self):
        r"""关联的应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ResourceId(self):
        r"""优图资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Word(self):
        r"""查询关键字，资源Id、应用名称、包名
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Platform(self):
        r"""平台信息，pc 或者 mobile
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def BizType(self):
        r"""所属业务，xmagic：优图， avatar：虚拟人，不传查全部
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._AppName = params.get("AppName")
        self._ResourceId = params.get("ResourceId")
        self._Word = params.get("Word")
        self._Platform = params.get("Platform")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeXMagicResourceListResponse(AbstractModel):
    r"""DescribeXMagicResourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: 优图资源包信息
        :type Resources: list of XMagicResourceSimpleInfo
        :param _Count: 资源数量
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resources = None
        self._Count = None
        self._RequestId = None

    @property
    def Resources(self):
        r"""优图资源包信息
        :rtype: list of XMagicResourceSimpleInfo
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Count(self):
        r"""资源数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = XMagicResourceSimpleInfo()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeXMagicResourceRequest(AbstractModel):
    r"""DescribeXMagicResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页页码 第一页是0
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        """
        self._PageNumber = None
        self._PageSize = None

    @property
    def PageNumber(self):
        r"""分页页码 第一页是0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeXMagicResourceResponse(AbstractModel):
    r"""DescribeXMagicResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: 优图资源包信息
        :type Resources: list of XMagicResource
        :param _Count: 资源数量
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resources = None
        self._Count = None
        self._RequestId = None

    @property
    def Resources(self):
        r"""优图资源包信息
        :rtype: list of XMagicResource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Count(self):
        r"""资源数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = XMagicResource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class Feature(AbstractModel):
    r"""功能描述模型

    """

    def __init__(self):
        r"""
        :param _Id: 索引
        :type Id: int
        :param _FeatureId: 功能ID
        :type FeatureId: int
        :param _Name: 功能名称
        :type Name: str
        :param _Type: 功能类型
        :type Type: str
        :param _Trial: 是否可以申请试用
        :type Trial: bool
        :param _TrialCount: 可以试用的次数
        :type TrialCount: int
        :param _Duration: 可以试用的时长，单位天
        :type Duration: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        """
        self._Id = None
        self._FeatureId = None
        self._Name = None
        self._Type = None
        self._Trial = None
        self._TrialCount = None
        self._Duration = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def Id(self):
        r"""索引
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FeatureId(self):
        r"""功能ID
        :rtype: int
        """
        return self._FeatureId

    @FeatureId.setter
    def FeatureId(self, FeatureId):
        self._FeatureId = FeatureId

    @property
    def Name(self):
        r"""功能名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""功能类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Trial(self):
        r"""是否可以申请试用
        :rtype: bool
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial

    @property
    def TrialCount(self):
        r"""可以试用的次数
        :rtype: int
        """
        return self._TrialCount

    @TrialCount.setter
    def TrialCount(self, TrialCount):
        self._TrialCount = TrialCount

    @property
    def Duration(self):
        r"""可以试用的时长，单位天
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FeatureId = params.get("FeatureId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Trial = params.get("Trial")
        self._TrialCount = params.get("TrialCount")
        self._Duration = params.get("Duration")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class License(AbstractModel):
    r"""视立方应用license

    """

    def __init__(self):
        r"""
        :param _Type: license类型
        :type Type: str
        :param _Remark: 老系统迁移备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _StartTime: license生效时间
        :type StartTime: str
        :param _EndTime: license失效时间
        :type EndTime: str
        :param _FeatureId: license对应的功能Id
        :type FeatureId: int
        :param _LicenseType: license是测试：test还是正式：formal
        :type LicenseType: str
        :param _Renewal: 测试license 是否可以续期
        :type Renewal: bool
        :param _LicenseId: license索引
        :type LicenseId: int
        :param _Name: license名称
        :type Name: str
        :param _Update: 测试license 是否升级
        :type Update: bool
        :param _OldLicenseUrl: 兼容老的licenseUrl
注意：此字段可能返回 null，表示取不到有效值。
        :type OldLicenseUrl: str
        :param _Group: 视立方url分组
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: int
        :param _Expired: 过期：true ，未过期：其它
        :type Expired: bool
        :param _RestTime: 返回还有多少秒过期，过期返回0
注意：此字段可能返回 null，表示取不到有效值。
        :type RestTime: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _Resource: 计费资源相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.vcube.v20220410.models.RenewResource`
        :param _IsVest: 是否为马甲包
        :type IsVest: bool
        """
        self._Type = None
        self._Remark = None
        self._StartTime = None
        self._EndTime = None
        self._FeatureId = None
        self._LicenseType = None
        self._Renewal = None
        self._LicenseId = None
        self._Name = None
        self._Update = None
        self._OldLicenseUrl = None
        self._Group = None
        self._Expired = None
        self._RestTime = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Resource = None
        self._IsVest = None

    @property
    def Type(self):
        r"""license类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Remark(self):
        r"""老系统迁移备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StartTime(self):
        r"""license生效时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""license失效时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FeatureId(self):
        r"""license对应的功能Id
        :rtype: int
        """
        return self._FeatureId

    @FeatureId.setter
    def FeatureId(self, FeatureId):
        self._FeatureId = FeatureId

    @property
    def LicenseType(self):
        r"""license是测试：test还是正式：formal
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def Renewal(self):
        r"""测试license 是否可以续期
        :rtype: bool
        """
        return self._Renewal

    @Renewal.setter
    def Renewal(self, Renewal):
        self._Renewal = Renewal

    @property
    def LicenseId(self):
        r"""license索引
        :rtype: int
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId

    @property
    def Name(self):
        r"""license名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Update(self):
        r"""测试license 是否升级
        :rtype: bool
        """
        return self._Update

    @Update.setter
    def Update(self, Update):
        self._Update = Update

    @property
    def OldLicenseUrl(self):
        r"""兼容老的licenseUrl
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OldLicenseUrl

    @OldLicenseUrl.setter
    def OldLicenseUrl(self, OldLicenseUrl):
        self._OldLicenseUrl = OldLicenseUrl

    @property
    def Group(self):
        r"""视立方url分组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Expired(self):
        r"""过期：true ，未过期：其它
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def RestTime(self):
        r"""返回还有多少秒过期，过期返回0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RestTime

    @RestTime.setter
    def RestTime(self, RestTime):
        self._RestTime = RestTime

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Resource(self):
        r"""计费资源相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.RenewResource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def IsVest(self):
        r"""是否为马甲包
        :rtype: bool
        """
        return self._IsVest

    @IsVest.setter
    def IsVest(self, IsVest):
        self._IsVest = IsVest


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Remark = params.get("Remark")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._FeatureId = params.get("FeatureId")
        self._LicenseType = params.get("LicenseType")
        self._Renewal = params.get("Renewal")
        self._LicenseId = params.get("LicenseId")
        self._Name = params.get("Name")
        self._Update = params.get("Update")
        self._OldLicenseUrl = params.get("OldLicenseUrl")
        self._Group = params.get("Group")
        self._Expired = params.get("Expired")
        self._RestTime = params.get("RestTime")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Resource") is not None:
            self._Resource = RenewResource()
            self._Resource._deserialize(params.get("Resource"))
        self._IsVest = params.get("IsVest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseResourceInfo(AbstractModel):
    r"""license 资源信息

    """

    def __init__(self):
        r"""
        :param _Id: 授权功能Id
        :type Id: int
        :param _AppId: 用户appid
        :type AppId: str
        :param _Duration: 有效期时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _FeatureId: 功能Id
        :type FeatureId: int
        :param _StartTime: 此license资源的开始生效时间
        :type StartTime: str
        :param _EndTime: 此license资源的生效结束时间
        :type EndTime: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _IsUse: 此资源是否可用于续期和更新有效期
        :type IsUse: bool
        :param _Status: 此资源的状态
        :type Status: int
        :param _IsolatedTimestamp: 销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTimestamp: str
        :param _Name: 功能模块名称
        :type Name: str
        :param _Type: 功能模块类型
        :type Type: str
        :param _Package: 资源包信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Package: :class:`tencentcloud.vcube.v20220410.models.Package`
        :param _Application: 应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Application: :class:`tencentcloud.vcube.v20220410.models.AppInfo`
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _AutoRenewFlag: 自动续费状态
        :type AutoRenewFlag: int
        """
        self._Id = None
        self._AppId = None
        self._Duration = None
        self._FeatureId = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._IsUse = None
        self._Status = None
        self._IsolatedTimestamp = None
        self._Name = None
        self._Type = None
        self._Package = None
        self._Application = None
        self._ResourceId = None
        self._AutoRenewFlag = None

    @property
    def Id(self):
        r"""授权功能Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Duration(self):
        r"""有效期时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FeatureId(self):
        r"""功能Id
        :rtype: int
        """
        return self._FeatureId

    @FeatureId.setter
    def FeatureId(self, FeatureId):
        self._FeatureId = FeatureId

    @property
    def StartTime(self):
        r"""此license资源的开始生效时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""此license资源的生效结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def IsUse(self):
        r"""此资源是否可用于续期和更新有效期
        :rtype: bool
        """
        return self._IsUse

    @IsUse.setter
    def IsUse(self, IsUse):
        self._IsUse = IsUse

    @property
    def Status(self):
        r"""此资源的状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolatedTimestamp(self):
        r"""销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def Name(self):
        r"""功能模块名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""功能模块类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Package(self):
        r"""资源包信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.Package`
        """
        return self._Package

    @Package.setter
    def Package(self, Package):
        self._Package = Package

    @property
    def Application(self):
        r"""应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.AppInfo`
        """
        return self._Application

    @Application.setter
    def Application(self, Application):
        self._Application = Application

    @property
    def ResourceId(self):
        r"""资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AutoRenewFlag(self):
        r"""自动续费状态
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Duration = params.get("Duration")
        self._FeatureId = params.get("FeatureId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._IsUse = params.get("IsUse")
        self._Status = params.get("Status")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Package") is not None:
            self._Package = Package()
            self._Package._deserialize(params.get("Package"))
        if params.get("Application") is not None:
            self._Application = AppInfo()
            self._Application._deserialize(params.get("Application"))
        self._ResourceId = params.get("ResourceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseResourceSimpleInfo(AbstractModel):
    r"""license 资源信息

    """

    def __init__(self):
        r"""
        :param _Id: 授权功能Id
        :type Id: int
        :param _AppId: 用户appid
        :type AppId: str
        :param _Duration: 有效期时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _FeatureId: 功能Id
        :type FeatureId: int
        :param _StartTime: 此license资源的开始生效时间
        :type StartTime: str
        :param _EndTime: 此license资源的生效结束时间
        :type EndTime: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _IsUse: 此资源是否可用于续期和更新有效期
        :type IsUse: bool
        :param _Status: 此资源的状态
        :type Status: int
        :param _IsolatedTimestamp: 销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTimestamp: str
        :param _Name: 功能模块名称
        :type Name: str
        :param _Type: 功能模块类型
        :type Type: str
        :param _Package: 资源包信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Package: :class:`tencentcloud.vcube.v20220410.models.Package`
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _AutoRenewFlag: 自动续费状态
        :type AutoRenewFlag: int
        """
        self._Id = None
        self._AppId = None
        self._Duration = None
        self._FeatureId = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._IsUse = None
        self._Status = None
        self._IsolatedTimestamp = None
        self._Name = None
        self._Type = None
        self._Package = None
        self._ResourceId = None
        self._AutoRenewFlag = None

    @property
    def Id(self):
        r"""授权功能Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Duration(self):
        r"""有效期时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FeatureId(self):
        r"""功能Id
        :rtype: int
        """
        return self._FeatureId

    @FeatureId.setter
    def FeatureId(self, FeatureId):
        self._FeatureId = FeatureId

    @property
    def StartTime(self):
        r"""此license资源的开始生效时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""此license资源的生效结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def IsUse(self):
        r"""此资源是否可用于续期和更新有效期
        :rtype: bool
        """
        return self._IsUse

    @IsUse.setter
    def IsUse(self, IsUse):
        self._IsUse = IsUse

    @property
    def Status(self):
        r"""此资源的状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolatedTimestamp(self):
        r"""销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def Name(self):
        r"""功能模块名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""功能模块类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Package(self):
        r"""资源包信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.Package`
        """
        return self._Package

    @Package.setter
    def Package(self, Package):
        self._Package = Package

    @property
    def ResourceId(self):
        r"""资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AutoRenewFlag(self):
        r"""自动续费状态
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Duration = params.get("Duration")
        self._FeatureId = params.get("FeatureId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._IsUse = params.get("IsUse")
        self._Status = params.get("Status")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Package") is not None:
            self._Package = Package()
            self._Package._deserialize(params.get("Package"))
        self._ResourceId = params.get("ResourceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
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
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        :param _AppName: 应用名
        :type AppName: str
        :param _BundleId: 应用ID
        :type BundleId: str
        :param _PackageName: 包名
        :type PackageName: str
        :param _WinProcessName: Windows 进程名
        :type WinProcessName: str
        :param _MacBundleId: Mac 进程名
        :type MacBundleId: str
        :param _DomainList: 要追加的web域名列表
        :type DomainList: list of str
        """
        self._ApplicationId = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None
        self._WinProcessName = None
        self._MacBundleId = None
        self._DomainList = None

    @property
    def ApplicationId(self):
        r"""应用ID
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppName(self):
        r"""应用名
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""应用ID
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def WinProcessName(self):
        r"""Windows 进程名
        :rtype: str
        """
        return self._WinProcessName

    @WinProcessName.setter
    def WinProcessName(self, WinProcessName):
        self._WinProcessName = WinProcessName

    @property
    def MacBundleId(self):
        r"""Mac 进程名
        :rtype: str
        """
        return self._MacBundleId

    @MacBundleId.setter
    def MacBundleId(self, MacBundleId):
        self._MacBundleId = MacBundleId

    @property
    def DomainList(self):
        r"""要追加的web域名列表
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        self._WinProcessName = params.get("WinProcessName")
        self._MacBundleId = params.get("MacBundleId")
        self._DomainList = params.get("DomainList")
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


class ModifyFormalApplicationRequest(AbstractModel):
    r"""ModifyFormalApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用Id
        :type ApplicationId: int
        :param _AppName: 应用名称
        :type AppName: str
        :param _BundleId: Ios 包名称
        :type BundleId: str
        :param _PackageName: Android  包名称
        :type PackageName: str
        """
        self._ApplicationId = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None

    @property
    def ApplicationId(self):
        r"""应用Id
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

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
    def BundleId(self):
        r"""Ios 包名称
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""Android  包名称
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFormalApplicationResponse(AbstractModel):
    r"""ModifyFormalApplication返回参数结构体

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


class ModifyLicenseRequest(AbstractModel):
    r"""ModifyLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseId: License 功能模块 Id
        :type LicenseId: str
        :param _ResourceId: 资源包 Id
        :type ResourceId: str
        """
        self._LicenseId = None
        self._ResourceId = None

    @property
    def LicenseId(self):
        r"""License 功能模块 Id
        :rtype: str
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId

    @property
    def ResourceId(self):
        r"""资源包 Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._LicenseId = params.get("LicenseId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLicenseResponse(AbstractModel):
    r"""ModifyLicense返回参数结构体

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


class ModifyPresetApplicationRequest(AbstractModel):
    r"""ModifyPresetApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用Id
        :type ApplicationId: int
        :param _AppName: 您的app名称
        :type AppName: str
        :param _BundleId: ios包名
        :type BundleId: str
        :param _PackageName: 安卓包名
        :type PackageName: str
        """
        self._ApplicationId = None
        self._AppName = None
        self._BundleId = None
        self._PackageName = None

    @property
    def ApplicationId(self):
        r"""应用Id
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppName(self):
        r"""您的app名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def BundleId(self):
        r"""ios包名
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def PackageName(self):
        r"""安卓包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AppName = params.get("AppName")
        self._BundleId = params.get("BundleId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPresetApplicationResponse(AbstractModel):
    r"""ModifyPresetApplication返回参数结构体

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


class ModifyTrialLicenseRequest(AbstractModel):
    r"""ModifyTrialLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseId: 授权ID
        :type LicenseId: str
        """
        self._LicenseId = None

    @property
    def LicenseId(self):
        r"""授权ID
        :rtype: str
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId


    def _deserialize(self, params):
        self._LicenseId = params.get("LicenseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTrialLicenseResponse(AbstractModel):
    r"""ModifyTrialLicense返回参数结构体

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


class ModifyXMagicRequest(AbstractModel):
    r"""ModifyXMagic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _XMagicId: 优图licenseId
        :type XMagicId: str
        """
        self._ResourceId = None
        self._XMagicId = None

    @property
    def ResourceId(self):
        r"""资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def XMagicId(self):
        r"""优图licenseId
        :rtype: str
        """
        return self._XMagicId

    @XMagicId.setter
    def XMagicId(self, XMagicId):
        self._XMagicId = XMagicId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._XMagicId = params.get("XMagicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyXMagicResponse(AbstractModel):
    r"""ModifyXMagic返回参数结构体

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


class NewsInfo(AbstractModel):
    r"""视立方产品概览页新闻动态

    """

    def __init__(self):
        r"""
        :param _Id: 新闻Id
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""新闻Id
        :rtype: int
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
        


class Package(AbstractModel):
    r"""资源包结构

    """

    def __init__(self):
        r"""
        :param _Id: 资源包Id
        :type Id: int
        :param _BizResourceId: 资源包资源Id
        :type BizResourceId: str
        :param _Site: 站点 中国站还是国际站
        :type Site: str
        :param _StartTime: 资源包开始生效时间
        :type StartTime: str
        :param _EndTime: 资源包过期时间
        :type EndTime: str
        :param _RefundTime: 资源包退费时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundTime: str
        :param _Name: 资源包名称
        :type Name: str
        :param _Type: 资源包类型ID,对应点播：PackageId 对应直播：TypeId
        :type Type: str
        """
        self._Id = None
        self._BizResourceId = None
        self._Site = None
        self._StartTime = None
        self._EndTime = None
        self._RefundTime = None
        self._Name = None
        self._Type = None

    @property
    def Id(self):
        r"""资源包Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BizResourceId(self):
        r"""资源包资源Id
        :rtype: str
        """
        return self._BizResourceId

    @BizResourceId.setter
    def BizResourceId(self, BizResourceId):
        self._BizResourceId = BizResourceId

    @property
    def Site(self):
        r"""站点 中国站还是国际站
        :rtype: str
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def StartTime(self):
        r"""资源包开始生效时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""资源包过期时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RefundTime(self):
        r"""资源包退费时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RefundTime

    @RefundTime.setter
    def RefundTime(self, RefundTime):
        self._RefundTime = RefundTime

    @property
    def Name(self):
        r"""资源包名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""资源包类型ID,对应点播：PackageId 对应直播：TypeId
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._BizResourceId = params.get("BizResourceId")
        self._Site = params.get("Site")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RefundTime = params.get("RefundTime")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewLicenseRequest(AbstractModel):
    r"""RenewLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseId: License 功能模块 Id
        :type LicenseId: str
        :param _ResourceId: 资源包 Id
        :type ResourceId: str
        """
        self._LicenseId = None
        self._ResourceId = None

    @property
    def LicenseId(self):
        r"""License 功能模块 Id
        :rtype: str
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId

    @property
    def ResourceId(self):
        r"""资源包 Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._LicenseId = params.get("LicenseId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewLicenseResponse(AbstractModel):
    r"""RenewLicense返回参数结构体

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


class RenewResource(AbstractModel):
    r"""自动续期资源info

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _AutoRenewFlag: 自动续期标记，0：默认，1：自动续期，2：不续期
        :type AutoRenewFlag: int
        :param _IsolatedTimestamp: 资源冻结时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTimestamp: str
        :param _Refund: 资源销毁状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Refund: bool
        :param _SubProductCode: 子产品码
        :type SubProductCode: str
        :param _EndTime: 资源到期时间
        :type EndTime: str
        """
        self._ResourceId = None
        self._AutoRenewFlag = None
        self._IsolatedTimestamp = None
        self._Refund = None
        self._SubProductCode = None
        self._EndTime = None

    @property
    def ResourceId(self):
        r"""资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AutoRenewFlag(self):
        r"""自动续期标记，0：默认，1：自动续期，2：不续期
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def IsolatedTimestamp(self):
        r"""资源冻结时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def Refund(self):
        r"""资源销毁状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Refund

    @Refund.setter
    def Refund(self, Refund):
        self._Refund = Refund

    @property
    def SubProductCode(self):
        r"""子产品码
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def EndTime(self):
        r"""资源到期时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._Refund = params.get("Refund")
        self._SubProductCode = params.get("SubProductCode")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewTestXMagicRequest(AbstractModel):
    r"""RenewTestXMagic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _XMagicId: 优图美视Id
        :type XMagicId: int
        """
        self._XMagicId = None

    @property
    def XMagicId(self):
        r"""优图美视Id
        :rtype: int
        """
        return self._XMagicId

    @XMagicId.setter
    def XMagicId(self, XMagicId):
        self._XMagicId = XMagicId


    def _deserialize(self, params):
        self._XMagicId = params.get("XMagicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewTestXMagicResponse(AbstractModel):
    r"""RenewTestXMagic返回参数结构体

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


class RenewVideoRequest(AbstractModel):
    r"""RenewVideo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseId: 要续期的视频播放license Id
        :type LicenseId: int
        """
        self._LicenseId = None

    @property
    def LicenseId(self):
        r"""要续期的视频播放license Id
        :rtype: int
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId


    def _deserialize(self, params):
        self._LicenseId = params.get("LicenseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewVideoResponse(AbstractModel):
    r"""RenewVideo返回参数结构体

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


class UpdateTestXMagicRequest(AbstractModel):
    r"""UpdateTestXMagic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _XMagicId: 优图美视功能Id
        :type XMagicId: int
        :param _ResourceId: XMagic套餐包Id
        :type ResourceId: str
        """
        self._XMagicId = None
        self._ResourceId = None

    @property
    def XMagicId(self):
        r"""优图美视功能Id
        :rtype: int
        """
        return self._XMagicId

    @XMagicId.setter
    def XMagicId(self, XMagicId):
        self._XMagicId = XMagicId

    @property
    def ResourceId(self):
        r"""XMagic套餐包Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._XMagicId = params.get("XMagicId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTestXMagicResponse(AbstractModel):
    r"""UpdateTestXMagic返回参数结构体

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


class UpdateTrialLicenseRequest(AbstractModel):
    r"""UpdateTrialLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseId: 执照ID
        :type LicenseId: str
        :param _ResourceId: 资源包ID
        :type ResourceId: str
        """
        self._LicenseId = None
        self._ResourceId = None

    @property
    def LicenseId(self):
        r"""执照ID
        :rtype: str
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId

    @property
    def ResourceId(self):
        r"""资源包ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._LicenseId = params.get("LicenseId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTrialLicenseResponse(AbstractModel):
    r"""UpdateTrialLicense返回参数结构体

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


class UpdateXMagicRequest(AbstractModel):
    r"""UpdateXMagic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _XMagicId: 要修改的XMagic Id
        :type XMagicId: int
        :param _XMagicResourceId: 资源id
        :type XMagicResourceId: str
        :param _CompanyPermit: 营业执照地址
        :type CompanyPermit: str
        :param _CompanyType: 公司类型
        :type CompanyType: str
        :param _CompanyName: 公司名称
        :type CompanyName: str
        """
        self._XMagicId = None
        self._XMagicResourceId = None
        self._CompanyPermit = None
        self._CompanyType = None
        self._CompanyName = None

    @property
    def XMagicId(self):
        r"""要修改的XMagic Id
        :rtype: int
        """
        return self._XMagicId

    @XMagicId.setter
    def XMagicId(self, XMagicId):
        self._XMagicId = XMagicId

    @property
    def XMagicResourceId(self):
        r"""资源id
        :rtype: str
        """
        return self._XMagicResourceId

    @XMagicResourceId.setter
    def XMagicResourceId(self, XMagicResourceId):
        self._XMagicResourceId = XMagicResourceId

    @property
    def CompanyPermit(self):
        r"""营业执照地址
        :rtype: str
        """
        return self._CompanyPermit

    @CompanyPermit.setter
    def CompanyPermit(self, CompanyPermit):
        self._CompanyPermit = CompanyPermit

    @property
    def CompanyType(self):
        r"""公司类型
        :rtype: str
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def CompanyName(self):
        r"""公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName


    def _deserialize(self, params):
        self._XMagicId = params.get("XMagicId")
        self._XMagicResourceId = params.get("XMagicResourceId")
        self._CompanyPermit = params.get("CompanyPermit")
        self._CompanyType = params.get("CompanyType")
        self._CompanyName = params.get("CompanyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateXMagicResponse(AbstractModel):
    r"""UpdateXMagic返回参数结构体

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


class VideoFeature(AbstractModel):
    r"""视频功能描述模型

    """

    def __init__(self):
        r"""
        :param _Id: 索引
        :type Id: int
        :param _FeatureId: 功能ID
        :type FeatureId: int
        :param _Name: 功能名称
        :type Name: str
        :param _Type: 功能类型
        :type Type: str
        :param _Trial: 是否可以申请试用
        :type Trial: bool
        :param _TrialCount: 可以试用的次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TrialCount: int
        :param _Duration: 可以试用的时长，单位天
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _BizType: 功能所属业务方
        :type BizType: str
        :param _Platform: 平台类型
        :type Platform: str
        """
        self._Id = None
        self._FeatureId = None
        self._Name = None
        self._Type = None
        self._Trial = None
        self._TrialCount = None
        self._Duration = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._BizType = None
        self._Platform = None

    @property
    def Id(self):
        r"""索引
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FeatureId(self):
        r"""功能ID
        :rtype: int
        """
        return self._FeatureId

    @FeatureId.setter
    def FeatureId(self, FeatureId):
        self._FeatureId = FeatureId

    @property
    def Name(self):
        r"""功能名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""功能类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Trial(self):
        r"""是否可以申请试用
        :rtype: bool
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial

    @property
    def TrialCount(self):
        r"""可以试用的次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TrialCount

    @TrialCount.setter
    def TrialCount(self, TrialCount):
        self._TrialCount = TrialCount

    @property
    def Duration(self):
        r"""可以试用的时长，单位天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def BizType(self):
        r"""功能所属业务方
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Platform(self):
        r"""平台类型
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FeatureId = params.get("FeatureId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Trial = params.get("Trial")
        self._TrialCount = params.get("TrialCount")
        self._Duration = params.get("Duration")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._BizType = params.get("BizType")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XMagicFeature(AbstractModel):
    r"""优图的的功能，Trial 为true的可以开通测试

    """

    def __init__(self):
        r"""
        :param _Name: 功能名称
        :type Name: str
        :param _TrialCount: 可以申请的次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TrialCount: int
        :param _Duration: 每次申请的时长单位：天
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _Plan: 功能类别
        :type Plan: str
        :param _XMagicType: single: 原子能力,combined:套餐
        :type XMagicType: str
        :param _Trial: 此功能是否支持开通测试
        :type Trial: bool
        :param _BizType: 功能所属业务方
        :type BizType: str
        """
        self._Name = None
        self._TrialCount = None
        self._Duration = None
        self._Plan = None
        self._XMagicType = None
        self._Trial = None
        self._BizType = None

    @property
    def Name(self):
        r"""功能名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TrialCount(self):
        r"""可以申请的次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TrialCount

    @TrialCount.setter
    def TrialCount(self, TrialCount):
        self._TrialCount = TrialCount

    @property
    def Duration(self):
        r"""每次申请的时长单位：天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Plan(self):
        r"""功能类别
        :rtype: str
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def XMagicType(self):
        r"""single: 原子能力,combined:套餐
        :rtype: str
        """
        return self._XMagicType

    @XMagicType.setter
    def XMagicType(self, XMagicType):
        self._XMagicType = XMagicType

    @property
    def Trial(self):
        r"""此功能是否支持开通测试
        :rtype: bool
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial

    @property
    def BizType(self):
        r"""功能所属业务方
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TrialCount = params.get("TrialCount")
        self._Duration = params.get("Duration")
        self._Plan = params.get("Plan")
        self._XMagicType = params.get("XMagicType")
        self._Trial = params.get("Trial")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XMagicInfo(AbstractModel):
    r"""查询返回的优图信息

    """

    def __init__(self):
        r"""
        :param _Id: 优图Id
        :type Id: int
        :param _CompanyName: 用户公司名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CompanyName: str
        :param _CompanyPermit: https://cos.xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type CompanyPermit: str
        :param _CompanyType: 用户公司行业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CompanyType: str
        :param _Plan: 优图套餐类型
        :type Plan: str
        :param _LicenseType: 测试版还是正式版 test | formal
        :type LicenseType: str
        :param _Status: 0: 预申请，需要补充申请信息
   1: 审批通过，xmagic已签发，正在生效中
    2: 提交完申请资料后待运营审核状态
    3: 申请被驳回，需要重新修改申请资料
    4: 应用包名被修改后触发xmagic审批，当前xmagic已暂停生效
    5: 应用修改包名后，审批未通过状态，可以重新修改应用PB，状态会回到4
        :type Status: int
        :param _Update: 测试license是否已经升级
注意：此字段可能返回 null，表示取不到有效值。
        :type Update: bool
        :param _StartTime: 优图生效开始时间 Status为1的时候
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 优图生效结束时间 Status为1的时候
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _RenewalCount: 续期次数， LicenseType=test时有此字段
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewalCount: int
        :param _Reply: 历次审批的回复
        :type Reply: list of str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 修改时间
        :type UpdatedAt: str
        :param _UpdateTime: 用户更新信息的时间
        :type UpdateTime: str
        :param _Expired: 是否过期
注意：此字段可能返回 null，表示取不到有效值。
        :type Expired: bool
        :param _RestTime: 返回还剩多少秒过期，过期后返回0
注意：此字段可能返回 null，表示取不到有效值。
        :type RestTime: int
        :param _XMagicType: single: 原子能力,combined:套餐
        :type XMagicType: str
        :param _Name: 优图模块名称，自动中英文
        :type Name: str
        :param _Resource: 优图资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.vcube.v20220410.models.RenewResource`
        :param _IsVest: 是否是马甲包
        :type IsVest: bool
        """
        self._Id = None
        self._CompanyName = None
        self._CompanyPermit = None
        self._CompanyType = None
        self._Plan = None
        self._LicenseType = None
        self._Status = None
        self._Update = None
        self._StartTime = None
        self._EndTime = None
        self._RenewalCount = None
        self._Reply = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._UpdateTime = None
        self._Expired = None
        self._RestTime = None
        self._XMagicType = None
        self._Name = None
        self._Resource = None
        self._IsVest = None

    @property
    def Id(self):
        r"""优图Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CompanyName(self):
        r"""用户公司名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CompanyPermit(self):
        r"""https://cos.xxx
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompanyPermit

    @CompanyPermit.setter
    def CompanyPermit(self, CompanyPermit):
        self._CompanyPermit = CompanyPermit

    @property
    def CompanyType(self):
        r"""用户公司行业类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def Plan(self):
        r"""优图套餐类型
        :rtype: str
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def LicenseType(self):
        r"""测试版还是正式版 test | formal
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def Status(self):
        r"""0: 预申请，需要补充申请信息
   1: 审批通过，xmagic已签发，正在生效中
    2: 提交完申请资料后待运营审核状态
    3: 申请被驳回，需要重新修改申请资料
    4: 应用包名被修改后触发xmagic审批，当前xmagic已暂停生效
    5: 应用修改包名后，审批未通过状态，可以重新修改应用PB，状态会回到4
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Update(self):
        r"""测试license是否已经升级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Update

    @Update.setter
    def Update(self, Update):
        self._Update = Update

    @property
    def StartTime(self):
        r"""优图生效开始时间 Status为1的时候
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""优图生效结束时间 Status为1的时候
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RenewalCount(self):
        r"""续期次数， LicenseType=test时有此字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewalCount

    @RenewalCount.setter
    def RenewalCount(self, RenewalCount):
        self._RenewalCount = RenewalCount

    @property
    def Reply(self):
        r"""历次审批的回复
        :rtype: list of str
        """
        return self._Reply

    @Reply.setter
    def Reply(self, Reply):
        self._Reply = Reply

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
    def UpdatedAt(self):
        r"""修改时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def UpdateTime(self):
        r"""用户更新信息的时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Expired(self):
        r"""是否过期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def RestTime(self):
        r"""返回还剩多少秒过期，过期后返回0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RestTime

    @RestTime.setter
    def RestTime(self, RestTime):
        self._RestTime = RestTime

    @property
    def XMagicType(self):
        r"""single: 原子能力,combined:套餐
        :rtype: str
        """
        return self._XMagicType

    @XMagicType.setter
    def XMagicType(self, XMagicType):
        self._XMagicType = XMagicType

    @property
    def Name(self):
        r"""优图模块名称，自动中英文
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Resource(self):
        r"""优图资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.RenewResource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def IsVest(self):
        r"""是否是马甲包
        :rtype: bool
        """
        return self._IsVest

    @IsVest.setter
    def IsVest(self, IsVest):
        self._IsVest = IsVest


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CompanyName = params.get("CompanyName")
        self._CompanyPermit = params.get("CompanyPermit")
        self._CompanyType = params.get("CompanyType")
        self._Plan = params.get("Plan")
        self._LicenseType = params.get("LicenseType")
        self._Status = params.get("Status")
        self._Update = params.get("Update")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RenewalCount = params.get("RenewalCount")
        self._Reply = params.get("Reply")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._UpdateTime = params.get("UpdateTime")
        self._Expired = params.get("Expired")
        self._RestTime = params.get("RestTime")
        self._XMagicType = params.get("XMagicType")
        self._Name = params.get("Name")
        if params.get("Resource") is not None:
            self._Resource = RenewResource()
            self._Resource._deserialize(params.get("Resource"))
        self._IsVest = params.get("IsVest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XMagicResource(AbstractModel):
    r"""优图美视资源包

    """

    def __init__(self):
        r"""
        :param _Id: 资源Id
        :type Id: int
        :param _AppId: 用户appid
        :type AppId: str
        :param _Plan: 套餐类别
        :type Plan: str
        :param _Duration: 单位：年
        :type Duration: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _XMagic: 资源是否已使用
注意：此字段可能返回 null，表示取不到有效值。
        :type XMagic: bool
        :param _StartTime: 资源开始生效时间
        :type StartTime: str
        :param _EndTime: 资源结束生效时间
        :type EndTime: str
        :param _Expired: 资源包是否过期
        :type Expired: bool
        :param _Name: 功能模块名称
        :type Name: str
        :param _XMagicType: single: 原子能力,combined:套餐
        :type XMagicType: str
        :param _BizType: xmagic:优图， avatar：虚拟人
        :type BizType: str
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _IsUse: 资源是否可以使用
        :type IsUse: bool
        """
        self._Id = None
        self._AppId = None
        self._Plan = None
        self._Duration = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._XMagic = None
        self._StartTime = None
        self._EndTime = None
        self._Expired = None
        self._Name = None
        self._XMagicType = None
        self._BizType = None
        self._ResourceId = None
        self._IsUse = None

    @property
    def Id(self):
        r"""资源Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Plan(self):
        r"""套餐类别
        :rtype: str
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Duration(self):
        r"""单位：年
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def XMagic(self):
        r"""资源是否已使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._XMagic

    @XMagic.setter
    def XMagic(self, XMagic):
        self._XMagic = XMagic

    @property
    def StartTime(self):
        r"""资源开始生效时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""资源结束生效时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Expired(self):
        r"""资源包是否过期
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def Name(self):
        r"""功能模块名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def XMagicType(self):
        r"""single: 原子能力,combined:套餐
        :rtype: str
        """
        return self._XMagicType

    @XMagicType.setter
    def XMagicType(self, XMagicType):
        self._XMagicType = XMagicType

    @property
    def BizType(self):
        r"""xmagic:优图， avatar：虚拟人
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def ResourceId(self):
        r"""资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def IsUse(self):
        r"""资源是否可以使用
        :rtype: bool
        """
        return self._IsUse

    @IsUse.setter
    def IsUse(self, IsUse):
        self._IsUse = IsUse


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Plan = params.get("Plan")
        self._Duration = params.get("Duration")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._XMagic = params.get("XMagic")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Expired = params.get("Expired")
        self._Name = params.get("Name")
        self._XMagicType = params.get("XMagicType")
        self._BizType = params.get("BizType")
        self._ResourceId = params.get("ResourceId")
        self._IsUse = params.get("IsUse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XMagicResourceSimpleInfo(AbstractModel):
    r"""优图美视资源包

    """

    def __init__(self):
        r"""
        :param _Id: 资源Id
        :type Id: int
        :param _AppId: 用户appid
        :type AppId: str
        :param _Plan: 套餐类别
        :type Plan: str
        :param _Duration: 单位：年
        :type Duration: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _StartTime: 资源开始生效时间
        :type StartTime: str
        :param _EndTime: 资源结束生效时间
        :type EndTime: str
        :param _Application: 应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Application: :class:`tencentcloud.vcube.v20220410.models.AppInfo`
        :param _XMagic: 开通的优图功能信息
注意：此字段可能返回 null，表示取不到有效值。
        :type XMagic: :class:`tencentcloud.vcube.v20220410.models.XMagicSimpleInfo`
        :param _Status: 优图资源状态
        :type Status: int
        :param _Operation: 操作日期记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: list of str
        :param _IsUse: 是否可以使用
        :type IsUse: bool
        :param _XMagicType: single: 原子能力,combined:套餐
        :type XMagicType: str
        :param _Name: 功能模块名称
        :type Name: str
        :param _BizType: 资源所属业务方 xmagic：优图，avatar：虚拟形象 
        :type BizType: str
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _AutoRenewFlag: 资源自动续费状态
        :type AutoRenewFlag: int
        """
        self._Id = None
        self._AppId = None
        self._Plan = None
        self._Duration = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._StartTime = None
        self._EndTime = None
        self._Application = None
        self._XMagic = None
        self._Status = None
        self._Operation = None
        self._IsUse = None
        self._XMagicType = None
        self._Name = None
        self._BizType = None
        self._ResourceId = None
        self._AutoRenewFlag = None

    @property
    def Id(self):
        r"""资源Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Plan(self):
        r"""套餐类别
        :rtype: str
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Duration(self):
        r"""单位：年
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def StartTime(self):
        r"""资源开始生效时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""资源结束生效时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Application(self):
        r"""应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.AppInfo`
        """
        return self._Application

    @Application.setter
    def Application(self, Application):
        self._Application = Application

    @property
    def XMagic(self):
        r"""开通的优图功能信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.vcube.v20220410.models.XMagicSimpleInfo`
        """
        return self._XMagic

    @XMagic.setter
    def XMagic(self, XMagic):
        self._XMagic = XMagic

    @property
    def Status(self):
        r"""优图资源状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        r"""操作日期记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def IsUse(self):
        r"""是否可以使用
        :rtype: bool
        """
        return self._IsUse

    @IsUse.setter
    def IsUse(self, IsUse):
        self._IsUse = IsUse

    @property
    def XMagicType(self):
        r"""single: 原子能力,combined:套餐
        :rtype: str
        """
        return self._XMagicType

    @XMagicType.setter
    def XMagicType(self, XMagicType):
        self._XMagicType = XMagicType

    @property
    def Name(self):
        r"""功能模块名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BizType(self):
        r"""资源所属业务方 xmagic：优图，avatar：虚拟形象 
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def ResourceId(self):
        r"""资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AutoRenewFlag(self):
        r"""资源自动续费状态
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Plan = params.get("Plan")
        self._Duration = params.get("Duration")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Application") is not None:
            self._Application = AppInfo()
            self._Application._deserialize(params.get("Application"))
        if params.get("XMagic") is not None:
            self._XMagic = XMagicSimpleInfo()
            self._XMagic._deserialize(params.get("XMagic"))
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._IsUse = params.get("IsUse")
        self._XMagicType = params.get("XMagicType")
        self._Name = params.get("Name")
        self._BizType = params.get("BizType")
        self._ResourceId = params.get("ResourceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XMagicSimpleInfo(AbstractModel):
    r"""优图简单信息

    """

    def __init__(self):
        r"""
        :param _Id: XMagic 的Id
        :type Id: int
        :param _Status: XMagic 状态
        :type Status: int
        """
        self._Id = None
        self._Status = None

    @property
    def Id(self):
        r"""XMagic 的Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        r"""XMagic 状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XMagicTrial(AbstractModel):
    r"""可以开通测试的功能

    """

    def __init__(self):
        r"""
        :param _Name: 功能名称
        :type Name: str
        :param _TrialCount: 可以申请的次数
        :type TrialCount: int
        :param _Duration: 每次申请的时长单位：天
        :type Duration: int
        :param _Plan: 功能类别
        :type Plan: str
        :param _XMagicType: single: 原子能力,combined:套餐
        :type XMagicType: str
        :param _BizType: vod：点播 live：直播
        :type BizType: str
        """
        self._Name = None
        self._TrialCount = None
        self._Duration = None
        self._Plan = None
        self._XMagicType = None
        self._BizType = None

    @property
    def Name(self):
        r"""功能名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TrialCount(self):
        r"""可以申请的次数
        :rtype: int
        """
        return self._TrialCount

    @TrialCount.setter
    def TrialCount(self, TrialCount):
        self._TrialCount = TrialCount

    @property
    def Duration(self):
        r"""每次申请的时长单位：天
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Plan(self):
        r"""功能类别
        :rtype: str
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def XMagicType(self):
        r"""single: 原子能力,combined:套餐
        :rtype: str
        """
        return self._XMagicType

    @XMagicType.setter
    def XMagicType(self, XMagicType):
        self._XMagicType = XMagicType

    @property
    def BizType(self):
        r"""vod：点播 live：直播
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TrialCount = params.get("TrialCount")
        self._Duration = params.get("Duration")
        self._Plan = params.get("Plan")
        self._XMagicType = params.get("XMagicType")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        