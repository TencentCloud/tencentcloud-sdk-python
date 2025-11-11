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


class AndroidApp(AbstractModel):
    r"""安卓应用

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 安卓应用 Id
        :type AndroidAppId: str
        :param _Name: 安卓应用名称
        :type Name: str
        :param _State: 安卓应用状态（上架、下架）
        :type State: str
        :param _AndroidAppVersionInfo: 安卓应用版本列表
        :type AndroidAppVersionInfo: list of AndroidAppVersionInfo
        :param _CreateTime: 安卓应用创建时间
        :type CreateTime: str
        :param _UserId: 用户 Id
        :type UserId: str
        :param _AppMode: 应用模式（NORMAL : 普通模式；ADVANCED : 高级模式）
        :type AppMode: str
        :param _UpdateState: 应用更新状态，取值：UPLOADING 上传中、CREATING 创建中、CREATE_FAIL 创建失败、CREATE_SUCCESS 创建成功、PACKAGE_NAME_MISMATCH 包名不匹配、VERSION_ALREADY_EXISTS 版本已存在、APP_PARSE_FAIL app 解析失败、APP_EXISTS_SECURITY_RISK app 存在安全风险、NORMAL 默认状态
        :type UpdateState: str
        :param _PackageName: 安卓应用包名
        :type PackageName: str
        """
        self._AndroidAppId = None
        self._Name = None
        self._State = None
        self._AndroidAppVersionInfo = None
        self._CreateTime = None
        self._UserId = None
        self._AppMode = None
        self._UpdateState = None
        self._PackageName = None

    @property
    def AndroidAppId(self):
        r"""安卓应用 Id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def Name(self):
        r"""安卓应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def State(self):
        r"""安卓应用状态（上架、下架）
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AndroidAppVersionInfo(self):
        r"""安卓应用版本列表
        :rtype: list of AndroidAppVersionInfo
        """
        return self._AndroidAppVersionInfo

    @AndroidAppVersionInfo.setter
    def AndroidAppVersionInfo(self, AndroidAppVersionInfo):
        self._AndroidAppVersionInfo = AndroidAppVersionInfo

    @property
    def CreateTime(self):
        r"""安卓应用创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserId(self):
        r"""用户 Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AppMode(self):
        r"""应用模式（NORMAL : 普通模式；ADVANCED : 高级模式）
        :rtype: str
        """
        return self._AppMode

    @AppMode.setter
    def AppMode(self, AppMode):
        self._AppMode = AppMode

    @property
    def UpdateState(self):
        r"""应用更新状态，取值：UPLOADING 上传中、CREATING 创建中、CREATE_FAIL 创建失败、CREATE_SUCCESS 创建成功、PACKAGE_NAME_MISMATCH 包名不匹配、VERSION_ALREADY_EXISTS 版本已存在、APP_PARSE_FAIL app 解析失败、APP_EXISTS_SECURITY_RISK app 存在安全风险、NORMAL 默认状态
        :rtype: str
        """
        return self._UpdateState

    @UpdateState.setter
    def UpdateState(self, UpdateState):
        self._UpdateState = UpdateState

    @property
    def PackageName(self):
        r"""安卓应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._Name = params.get("Name")
        self._State = params.get("State")
        if params.get("AndroidAppVersionInfo") is not None:
            self._AndroidAppVersionInfo = []
            for item in params.get("AndroidAppVersionInfo"):
                obj = AndroidAppVersionInfo()
                obj._deserialize(item)
                self._AndroidAppVersionInfo.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UserId = params.get("UserId")
        self._AppMode = params.get("AppMode")
        self._UpdateState = params.get("UpdateState")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidAppCosInfo(AbstractModel):
    r"""安卓应用Cos数据

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 安卓应用ID
        :type AndroidAppId: str
        :param _FileName: 应用名称（支持 apk 和 tgz 两种格式文件，当应用 AppMode 为 NORMAL 时，只支持上传 apk 类型文件，当应用 AppMode 为 ADVANCED 高级模式时，只支持上传  tgz 类型文件）
        :type FileName: str
        """
        self._AndroidAppId = None
        self._FileName = None

    @property
    def AndroidAppId(self):
        r"""安卓应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def FileName(self):
        r"""应用名称（支持 apk 和 tgz 两种格式文件，当应用 AppMode 为 NORMAL 时，只支持上传 apk 类型文件，当应用 AppMode 为 ADVANCED 高级模式时，只支持上传  tgz 类型文件）
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidAppVersionInfo(AbstractModel):
    r"""安卓应用版本信息

    """

    def __init__(self):
        r"""
        :param _AndroidAppVersion: 安卓应用版本
        :type AndroidAppVersion: str
        :param _State: 安卓应用版本创建状态，取值：NORMAL：无（默认）、UPLOADING：上传中、CREATING： 创建中、CREATE_FAIL：创建失败、PACKAGE_NAME_MISMATCH：包名不匹配、VERSION_ALREADY_EXISTS：版本已存在、APP_PARSE_FAIL： app 解析失败、APP_EXISTS_SECURITY_RISK：app 存在安全风险、CREATE_SUCCESS：创建成功
        :type State: str
        :param _CreateTime: 安卓应用版本创建时间
        :type CreateTime: str
        :param _Command: shell 安装命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :type Command: str
        :param _UninstallCommand: shell 卸载命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :type UninstallCommand: str
        :param _CleanupMode: 应用资源清理模式（实例安装应用所用资源），取值：CLEANUP_ON_UNINSTALL（默认值），卸载 App 时清理；CLEANUP_AFTER_INSTALL，安装 App 后立即清理。普通应用只有 CLEANUP_AFTER_INSTALL 模式。
        :type CleanupMode: str
        :param _AndroidAppVersionName: 安卓应用版本名称（版本描述、备注）
        :type AndroidAppVersionName: str
        :param _Activity: 安卓应用启动页
        :type Activity: str
        :param _VersionName: 应用版本号（Version Name）
        :type VersionName: str
        :param _MD5: 应用包 MD5
        :type MD5: str
        :param _FileSize: 应用包文件大小（字节）
        :type FileSize: int
        :param _PackageName: 安卓应用包名
        :type PackageName: str
        """
        self._AndroidAppVersion = None
        self._State = None
        self._CreateTime = None
        self._Command = None
        self._UninstallCommand = None
        self._CleanupMode = None
        self._AndroidAppVersionName = None
        self._Activity = None
        self._VersionName = None
        self._MD5 = None
        self._FileSize = None
        self._PackageName = None

    @property
    def AndroidAppVersion(self):
        r"""安卓应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion

    @property
    def State(self):
        r"""安卓应用版本创建状态，取值：NORMAL：无（默认）、UPLOADING：上传中、CREATING： 创建中、CREATE_FAIL：创建失败、PACKAGE_NAME_MISMATCH：包名不匹配、VERSION_ALREADY_EXISTS：版本已存在、APP_PARSE_FAIL： app 解析失败、APP_EXISTS_SECURITY_RISK：app 存在安全风险、CREATE_SUCCESS：创建成功
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        r"""安卓应用版本创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Command(self):
        r"""shell 安装命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def UninstallCommand(self):
        r"""shell 卸载命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :rtype: str
        """
        return self._UninstallCommand

    @UninstallCommand.setter
    def UninstallCommand(self, UninstallCommand):
        self._UninstallCommand = UninstallCommand

    @property
    def CleanupMode(self):
        r"""应用资源清理模式（实例安装应用所用资源），取值：CLEANUP_ON_UNINSTALL（默认值），卸载 App 时清理；CLEANUP_AFTER_INSTALL，安装 App 后立即清理。普通应用只有 CLEANUP_AFTER_INSTALL 模式。
        :rtype: str
        """
        return self._CleanupMode

    @CleanupMode.setter
    def CleanupMode(self, CleanupMode):
        self._CleanupMode = CleanupMode

    @property
    def AndroidAppVersionName(self):
        r"""安卓应用版本名称（版本描述、备注）
        :rtype: str
        """
        return self._AndroidAppVersionName

    @AndroidAppVersionName.setter
    def AndroidAppVersionName(self, AndroidAppVersionName):
        self._AndroidAppVersionName = AndroidAppVersionName

    @property
    def Activity(self):
        r"""安卓应用启动页
        :rtype: str
        """
        return self._Activity

    @Activity.setter
    def Activity(self, Activity):
        self._Activity = Activity

    @property
    def VersionName(self):
        r"""应用版本号（Version Name）
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def MD5(self):
        r"""应用包 MD5
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def FileSize(self):
        r"""应用包文件大小（字节）
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def PackageName(self):
        r"""安卓应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._Command = params.get("Command")
        self._UninstallCommand = params.get("UninstallCommand")
        self._CleanupMode = params.get("CleanupMode")
        self._AndroidAppVersionName = params.get("AndroidAppVersionName")
        self._Activity = params.get("Activity")
        self._VersionName = params.get("VersionName")
        self._MD5 = params.get("MD5")
        self._FileSize = params.get("FileSize")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstance(AbstractModel):
    r"""安卓实例信息

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例 ID
        :type AndroidInstanceId: str
        :param _AndroidInstanceRegion: 实例所在区域
        :type AndroidInstanceRegion: str
        :param _AndroidInstanceZone: 实例可用区
        :type AndroidInstanceZone: str
        :param _State: 实例状态：INITIALIZING，NORMAL，PROCESSING
        :type State: str
        :param _AndroidInstanceType: 实例规格
        :type AndroidInstanceType: str
        :param _AndroidInstanceImageId: 实例镜像 ID
        :type AndroidInstanceImageId: str
        :param _Width: 分辨率宽度
        :type Width: int
        :param _Height: 分辨率高度
        :type Height: int
        :param _HostSerialNumber: 宿主机 ID
        :type HostSerialNumber: str
        :param _AndroidInstanceGroupId: 分组 ID
        :type AndroidInstanceGroupId: str
        :param _AndroidInstanceLabels: 标签列表
        :type AndroidInstanceLabels: list of AndroidInstanceLabel
        :param _Name: 名称
        :type Name: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _PrivateIP: 内网 IP
        :type PrivateIP: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _HostServerSerialNumber: 机箱 ID
        :type HostServerSerialNumber: str
        """
        self._AndroidInstanceId = None
        self._AndroidInstanceRegion = None
        self._AndroidInstanceZone = None
        self._State = None
        self._AndroidInstanceType = None
        self._AndroidInstanceImageId = None
        self._Width = None
        self._Height = None
        self._HostSerialNumber = None
        self._AndroidInstanceGroupId = None
        self._AndroidInstanceLabels = None
        self._Name = None
        self._UserId = None
        self._PrivateIP = None
        self._CreateTime = None
        self._HostServerSerialNumber = None

    @property
    def AndroidInstanceId(self):
        r"""实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def AndroidInstanceRegion(self):
        r"""实例所在区域
        :rtype: str
        """
        return self._AndroidInstanceRegion

    @AndroidInstanceRegion.setter
    def AndroidInstanceRegion(self, AndroidInstanceRegion):
        self._AndroidInstanceRegion = AndroidInstanceRegion

    @property
    def AndroidInstanceZone(self):
        r"""实例可用区
        :rtype: str
        """
        return self._AndroidInstanceZone

    @AndroidInstanceZone.setter
    def AndroidInstanceZone(self, AndroidInstanceZone):
        self._AndroidInstanceZone = AndroidInstanceZone

    @property
    def State(self):
        r"""实例状态：INITIALIZING，NORMAL，PROCESSING
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AndroidInstanceType(self):
        r"""实例规格
        :rtype: str
        """
        return self._AndroidInstanceType

    @AndroidInstanceType.setter
    def AndroidInstanceType(self, AndroidInstanceType):
        self._AndroidInstanceType = AndroidInstanceType

    @property
    def AndroidInstanceImageId(self):
        r"""实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def Width(self):
        r"""分辨率宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""分辨率高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def HostSerialNumber(self):
        r"""宿主机 ID
        :rtype: str
        """
        return self._HostSerialNumber

    @HostSerialNumber.setter
    def HostSerialNumber(self, HostSerialNumber):
        self._HostSerialNumber = HostSerialNumber

    @property
    def AndroidInstanceGroupId(self):
        r"""分组 ID
        :rtype: str
        """
        return self._AndroidInstanceGroupId

    @AndroidInstanceGroupId.setter
    def AndroidInstanceGroupId(self, AndroidInstanceGroupId):
        self._AndroidInstanceGroupId = AndroidInstanceGroupId

    @property
    def AndroidInstanceLabels(self):
        r"""标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._AndroidInstanceLabels

    @AndroidInstanceLabels.setter
    def AndroidInstanceLabels(self, AndroidInstanceLabels):
        self._AndroidInstanceLabels = AndroidInstanceLabels

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def PrivateIP(self):
        r"""内网 IP
        :rtype: str
        """
        return self._PrivateIP

    @PrivateIP.setter
    def PrivateIP(self, PrivateIP):
        self._PrivateIP = PrivateIP

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
    def HostServerSerialNumber(self):
        r"""机箱 ID
        :rtype: str
        """
        return self._HostServerSerialNumber

    @HostServerSerialNumber.setter
    def HostServerSerialNumber(self, HostServerSerialNumber):
        self._HostServerSerialNumber = HostServerSerialNumber


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._AndroidInstanceRegion = params.get("AndroidInstanceRegion")
        self._AndroidInstanceZone = params.get("AndroidInstanceZone")
        self._State = params.get("State")
        self._AndroidInstanceType = params.get("AndroidInstanceType")
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._HostSerialNumber = params.get("HostSerialNumber")
        self._AndroidInstanceGroupId = params.get("AndroidInstanceGroupId")
        if params.get("AndroidInstanceLabels") is not None:
            self._AndroidInstanceLabels = []
            for item in params.get("AndroidInstanceLabels"):
                obj = AndroidInstanceLabel()
                obj._deserialize(item)
                self._AndroidInstanceLabels.append(obj)
        self._Name = params.get("Name")
        self._UserId = params.get("UserId")
        self._PrivateIP = params.get("PrivateIP")
        self._CreateTime = params.get("CreateTime")
        self._HostServerSerialNumber = params.get("HostServerSerialNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceAppBlacklist(AbstractModel):
    r"""安卓实例应用黑名单

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _AppBlacklist: 应用黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBlacklist: list of str
        """
        self._AndroidInstanceId = None
        self._AppBlacklist = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def AppBlacklist(self):
        r"""应用黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AppBlacklist

    @AppBlacklist.setter
    def AppBlacklist(self, AppBlacklist):
        self._AppBlacklist = AppBlacklist


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._AppBlacklist = params.get("AppBlacklist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceAppInfo(AbstractModel):
    r"""安卓实例应用信息

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 应用id
        :type AndroidAppId: str
        :param _Name: 应用名称
        :type Name: str
        :param _AndroidAppVersion: 应用版本
        :type AndroidAppVersion: str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _PackageVersion: 应用包版本
        :type PackageVersion: str
        :param _PackageLabel: 应用包标签
        :type PackageLabel: str
        :param _VersionName: 应用包版本号
        :type VersionName: str
        """
        self._AndroidAppId = None
        self._Name = None
        self._AndroidAppVersion = None
        self._PackageName = None
        self._PackageVersion = None
        self._PackageLabel = None
        self._VersionName = None

    @property
    def AndroidAppId(self):
        r"""应用id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def Name(self):
        r"""应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AndroidAppVersion(self):
        r"""应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        warnings.warn("parameter `PackageVersion` is deprecated", DeprecationWarning) 

        r"""应用包版本
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        warnings.warn("parameter `PackageVersion` is deprecated", DeprecationWarning) 

        self._PackageVersion = PackageVersion

    @property
    def PackageLabel(self):
        r"""应用包标签
        :rtype: str
        """
        return self._PackageLabel

    @PackageLabel.setter
    def PackageLabel(self, PackageLabel):
        self._PackageLabel = PackageLabel

    @property
    def VersionName(self):
        r"""应用包版本号
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._Name = params.get("Name")
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._PackageLabel = params.get("PackageLabel")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceDevice(AbstractModel):
    r"""安卓实例设备信息

    """

    def __init__(self):
        r"""
        :param _Brand: 品牌
        :type Brand: str
        :param _Model: 型号
        :type Model: str
        """
        self._Brand = None
        self._Model = None

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Model(self):
        r"""型号
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        self._Brand = params.get("Brand")
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceError(AbstractModel):
    r"""安卓实例错误信息，用于批量安卓实例操作中返回部分操作错误的情况

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _Error: 错误信息
        :type Error: :class:`tencentcloud.gs.v20191118.models.Error`
        """
        self._AndroidInstanceId = None
        self._Error = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Error(self):
        r"""错误信息
        :rtype: :class:`tencentcloud.gs.v20191118.models.Error`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        if params.get("Error") is not None:
            self._Error = Error()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceHostTask(AbstractModel):
    r"""安卓实例宿主机任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _HostSerialNumber: 宿主机序列号
        :type HostSerialNumber: str
        """
        self._TaskId = None
        self._HostSerialNumber = None

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
    def HostSerialNumber(self):
        r"""宿主机序列号
        :rtype: str
        """
        return self._HostSerialNumber

    @HostSerialNumber.setter
    def HostSerialNumber(self, HostSerialNumber):
        self._HostSerialNumber = HostSerialNumber


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._HostSerialNumber = params.get("HostSerialNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceImage(AbstractModel):
    r"""安卓实例镜像信息

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageId: 镜像 ID
        :type AndroidInstanceImageId: str
        :param _AndroidInstanceImageName: 镜像名称，由业务方自定义，仅用于展示
        :type AndroidInstanceImageName: str
        :param _AndroidInstanceImageState: 镜像状态
        :type AndroidInstanceImageState: str
        :param _AndroidInstanceImageZone: 镜像可用区
        :type AndroidInstanceImageZone: str
        :param _AndroidInstanceImageDescription: 镜像描述
        :type AndroidInstanceImageDescription: str
        :param _AndroidVersion: 安卓10
        :type AndroidVersion: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._AndroidInstanceImageId = None
        self._AndroidInstanceImageName = None
        self._AndroidInstanceImageState = None
        self._AndroidInstanceImageZone = None
        self._AndroidInstanceImageDescription = None
        self._AndroidVersion = None
        self._CreateTime = None

    @property
    def AndroidInstanceImageId(self):
        r"""镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def AndroidInstanceImageName(self):
        r"""镜像名称，由业务方自定义，仅用于展示
        :rtype: str
        """
        return self._AndroidInstanceImageName

    @AndroidInstanceImageName.setter
    def AndroidInstanceImageName(self, AndroidInstanceImageName):
        self._AndroidInstanceImageName = AndroidInstanceImageName

    @property
    def AndroidInstanceImageState(self):
        r"""镜像状态
        :rtype: str
        """
        return self._AndroidInstanceImageState

    @AndroidInstanceImageState.setter
    def AndroidInstanceImageState(self, AndroidInstanceImageState):
        self._AndroidInstanceImageState = AndroidInstanceImageState

    @property
    def AndroidInstanceImageZone(self):
        r"""镜像可用区
        :rtype: str
        """
        return self._AndroidInstanceImageZone

    @AndroidInstanceImageZone.setter
    def AndroidInstanceImageZone(self, AndroidInstanceImageZone):
        self._AndroidInstanceImageZone = AndroidInstanceImageZone

    @property
    def AndroidInstanceImageDescription(self):
        r"""镜像描述
        :rtype: str
        """
        return self._AndroidInstanceImageDescription

    @AndroidInstanceImageDescription.setter
    def AndroidInstanceImageDescription(self, AndroidInstanceImageDescription):
        self._AndroidInstanceImageDescription = AndroidInstanceImageDescription

    @property
    def AndroidVersion(self):
        r"""安卓10
        :rtype: str
        """
        return self._AndroidVersion

    @AndroidVersion.setter
    def AndroidVersion(self, AndroidVersion):
        self._AndroidVersion = AndroidVersion

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._AndroidInstanceImageName = params.get("AndroidInstanceImageName")
        self._AndroidInstanceImageState = params.get("AndroidInstanceImageState")
        self._AndroidInstanceImageZone = params.get("AndroidInstanceImageZone")
        self._AndroidInstanceImageDescription = params.get("AndroidInstanceImageDescription")
        self._AndroidVersion = params.get("AndroidVersion")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceInformation(AbstractModel):
    r"""安卓实例信息

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _Name: 实例名称
        :type Name: str
        """
        self._AndroidInstanceId = None
        self._Name = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Name(self):
        r"""实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceLabel(AbstractModel):
    r"""安卓实例标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
        


class AndroidInstanceLabelDetail(AbstractModel):
    r"""安卓实例标签详情

    """

    def __init__(self):
        r"""
        :param _Label: 标签
        :type Label: :class:`tencentcloud.gs.v20191118.models.AndroidInstanceLabel`
        :param _Description: 标签描述
        :type Description: str
        :param _CreateTime: 标签创建时间
        :type CreateTime: str
        """
        self._Label = None
        self._Description = None
        self._CreateTime = None

    @property
    def Label(self):
        r"""标签
        :rtype: :class:`tencentcloud.gs.v20191118.models.AndroidInstanceLabel`
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Description(self):
        r"""标签描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""标签创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        if params.get("Label") is not None:
            self._Label = AndroidInstanceLabel()
            self._Label._deserialize(params.get("Label"))
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceProperty(AbstractModel):
    r"""安卓实例属性

    """

    def __init__(self):
        r"""
        :param _Key: 属性键
        :type Key: str
        :param _Value: 属性值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""属性键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""属性值
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
        


class AndroidInstanceTask(AbstractModel):
    r"""安卓实例任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        """
        self._TaskId = None
        self._AndroidInstanceId = None

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
    def AndroidInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceTaskStatus(AbstractModel):
    r"""安卓实例任务状态信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Status: 任务状态：SUCCESS，FAILED，PROCESSING，PENDING,CANCELED
        :type Status: str
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        :param _TaskResult: 任务执行结果描述，针对某些任务，可以是可解析的 json
        :type TaskResult: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _CompleteTime: 任务完成时间
        :type CompleteTime: str
        """
        self._TaskId = None
        self._Status = None
        self._AndroidInstanceId = None
        self._TaskResult = None
        self._TaskType = None
        self._CreateTime = None
        self._CompleteTime = None

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
    def Status(self):
        r"""任务状态：SUCCESS，FAILED，PROCESSING，PENDING,CANCELED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AndroidInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def TaskResult(self):
        r"""任务执行结果描述，针对某些任务，可以是可解析的 json
        :rtype: str
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def TaskType(self):
        r"""任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def CreateTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CompleteTime(self):
        r"""任务完成时间
        :rtype: str
        """
        return self._CompleteTime

    @CompleteTime.setter
    def CompleteTime(self, CompleteTime):
        self._CompleteTime = CompleteTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._TaskResult = params.get("TaskResult")
        self._TaskType = params.get("TaskType")
        self._CreateTime = params.get("CreateTime")
        self._CompleteTime = params.get("CompleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceUploadFile(AbstractModel):
    r"""安卓实例上传文件信息

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _FileURL: 文件上传 URL
        :type FileURL: str
        :param _DestinationDirectory: 上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :type DestinationDirectory: str
        :param _DestinationFileName: 目标文件名
        :type DestinationFileName: str
        """
        self._AndroidInstanceId = None
        self._FileURL = None
        self._DestinationDirectory = None
        self._DestinationFileName = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def FileURL(self):
        r"""文件上传 URL
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def DestinationDirectory(self):
        r"""上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :rtype: str
        """
        return self._DestinationDirectory

    @DestinationDirectory.setter
    def DestinationDirectory(self, DestinationDirectory):
        self._DestinationDirectory = DestinationDirectory

    @property
    def DestinationFileName(self):
        r"""目标文件名
        :rtype: str
        """
        return self._DestinationFileName

    @DestinationFileName.setter
    def DestinationFileName(self, DestinationFileName):
        self._DestinationFileName = DestinationFileName


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._FileURL = params.get("FileURL")
        self._DestinationDirectory = params.get("DestinationDirectory")
        self._DestinationFileName = params.get("DestinationFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackUpAndroidInstanceRequest(AbstractModel):
    r"""BackUpAndroidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例ID
        :type AndroidInstanceId: str
        :param _Includes: 包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :type Includes: list of str
        :param _Excludes: 需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :type Excludes: list of str
        """
        self._AndroidInstanceId = None
        self._Includes = None
        self._Excludes = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Includes(self):
        r"""包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def Excludes(self):
        r"""需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Excludes

    @Excludes.setter
    def Excludes(self, Excludes):
        self._Excludes = Excludes


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._Includes = params.get("Includes")
        self._Excludes = params.get("Excludes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackUpAndroidInstanceResponse(AbstractModel):
    r"""BackUpAndroidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份 ID
        :type BackupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupId = None
        self._RequestId = None

    @property
    def BackupId(self):
        r"""备份 ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._RequestId = params.get("RequestId")


class BackUpAndroidInstanceToStorageRequest(AbstractModel):
    r"""BackUpAndroidInstanceToStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例ID
        :type AndroidInstanceId: str
        :param _StorageType: 存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :type StorageType: str
        :param _ObjectKey: 自定义对象Key
        :type ObjectKey: str
        :param _Includes: 包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :type Includes: list of str
        :param _Excludes: 需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :type Excludes: list of str
        :param _COSOptions: COS协议选项
        :type COSOptions: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        :param _S3Options: S3存储协议选项
        :type S3Options: :class:`tencentcloud.gs.v20191118.models.S3Options`
        """
        self._AndroidInstanceId = None
        self._StorageType = None
        self._ObjectKey = None
        self._Includes = None
        self._Excludes = None
        self._COSOptions = None
        self._S3Options = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def StorageType(self):
        r"""存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def ObjectKey(self):
        r"""自定义对象Key
        :rtype: str
        """
        return self._ObjectKey

    @ObjectKey.setter
    def ObjectKey(self, ObjectKey):
        self._ObjectKey = ObjectKey

    @property
    def Includes(self):
        r"""包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def Excludes(self):
        r"""需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Excludes

    @Excludes.setter
    def Excludes(self, Excludes):
        self._Excludes = Excludes

    @property
    def COSOptions(self):
        r"""COS协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        """
        return self._COSOptions

    @COSOptions.setter
    def COSOptions(self, COSOptions):
        self._COSOptions = COSOptions

    @property
    def S3Options(self):
        r"""S3存储协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.S3Options`
        """
        return self._S3Options

    @S3Options.setter
    def S3Options(self, S3Options):
        self._S3Options = S3Options


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._StorageType = params.get("StorageType")
        self._ObjectKey = params.get("ObjectKey")
        self._Includes = params.get("Includes")
        self._Excludes = params.get("Excludes")
        if params.get("COSOptions") is not None:
            self._COSOptions = COSOptions()
            self._COSOptions._deserialize(params.get("COSOptions"))
        if params.get("S3Options") is not None:
            self._S3Options = S3Options()
            self._S3Options._deserialize(params.get("S3Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackUpAndroidInstanceToStorageResponse(AbstractModel):
    r"""BackUpAndroidInstanceToStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 实例任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""实例任务 ID
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


class COSOptions(AbstractModel):
    r"""COS协议参数

    """

    def __init__(self):
        r"""
        :param _Bucket: 存储桶
        :type Bucket: str
        :param _Region: 存储区域
        :type Region: str
        """
        self._Bucket = None
        self._Region = None

    @property
    def Bucket(self):
        r"""存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""存储区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanAndroidInstancesAppDataRequest(AbstractModel):
    r"""CleanAndroidInstancesAppData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表（最大100条数据）
        :type AndroidInstanceIds: list of str
        :param _PackageName: 应用包名
        :type PackageName: str
        """
        self._AndroidInstanceIds = None
        self._PackageName = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表（最大100条数据）
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanAndroidInstancesAppDataResponse(AbstractModel):
    r"""CleanAndroidInstancesAppData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class ConnectAndroidInstanceRequest(AbstractModel):
    r"""ConnectAndroidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientSession: 用户Session信息
        :type ClientSession: str
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        :param _UserIp: 用户IP，用户客户端的公网IP，用于选择最佳网络链路
        :type UserIp: str
        """
        self._ClientSession = None
        self._AndroidInstanceId = None
        self._UserIp = None

    @property
    def ClientSession(self):
        r"""用户Session信息
        :rtype: str
        """
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def AndroidInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def UserIp(self):
        r"""用户IP，用户客户端的公网IP，用于选择最佳网络链路
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._ClientSession = params.get("ClientSession")
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectAndroidInstanceResponse(AbstractModel):
    r"""ConnectAndroidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerSession: 服务端session信息
        :type ServerSession: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerSession = None
        self._RequestId = None

    @property
    def ServerSession(self):
        r"""服务端session信息
        :rtype: str
        """
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServerSession = params.get("ServerSession")
        self._RequestId = params.get("RequestId")


class CopyAndroidInstanceRequest(AbstractModel):
    r"""CopyAndroidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceAndroidInstanceId: 源安卓实例 ID
        :type SourceAndroidInstanceId: str
        :param _TargetAndroidInstanceId: 目的安卓实例 ID
        :type TargetAndroidInstanceId: str
        :param _Includes: 包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :type Includes: list of str
        :param _Excludes: 需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :type Excludes: list of str
        """
        self._SourceAndroidInstanceId = None
        self._TargetAndroidInstanceId = None
        self._Includes = None
        self._Excludes = None

    @property
    def SourceAndroidInstanceId(self):
        r"""源安卓实例 ID
        :rtype: str
        """
        return self._SourceAndroidInstanceId

    @SourceAndroidInstanceId.setter
    def SourceAndroidInstanceId(self, SourceAndroidInstanceId):
        self._SourceAndroidInstanceId = SourceAndroidInstanceId

    @property
    def TargetAndroidInstanceId(self):
        r"""目的安卓实例 ID
        :rtype: str
        """
        return self._TargetAndroidInstanceId

    @TargetAndroidInstanceId.setter
    def TargetAndroidInstanceId(self, TargetAndroidInstanceId):
        self._TargetAndroidInstanceId = TargetAndroidInstanceId

    @property
    def Includes(self):
        r"""包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def Excludes(self):
        r"""需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Excludes

    @Excludes.setter
    def Excludes(self, Excludes):
        self._Excludes = Excludes


    def _deserialize(self, params):
        self._SourceAndroidInstanceId = params.get("SourceAndroidInstanceId")
        self._TargetAndroidInstanceId = params.get("TargetAndroidInstanceId")
        self._Includes = params.get("Includes")
        self._Excludes = params.get("Excludes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAndroidInstanceResponse(AbstractModel):
    r"""CopyAndroidInstance返回参数结构体

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


class CreateAndroidAppRequest(AbstractModel):
    r"""CreateAndroidApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 安卓应用名字
        :type Name: str
        :param _UserId: 用户 Id
        :type UserId: str
        :param _AppMode: 应用模式（NORMAL : 普通模式、只支持 apk 文件上传，为默认值；ADVANCED : 高级模式、只支持上传 tgz 文件 和 自定义 shell 命令执行）
        :type AppMode: str
        """
        self._Name = None
        self._UserId = None
        self._AppMode = None

    @property
    def Name(self):
        r"""安卓应用名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserId(self):
        r"""用户 Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AppMode(self):
        r"""应用模式（NORMAL : 普通模式、只支持 apk 文件上传，为默认值；ADVANCED : 高级模式、只支持上传 tgz 文件 和 自定义 shell 命令执行）
        :rtype: str
        """
        return self._AppMode

    @AppMode.setter
    def AppMode(self, AppMode):
        self._AppMode = AppMode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._UserId = params.get("UserId")
        self._AppMode = params.get("AppMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidAppResponse(AbstractModel):
    r"""CreateAndroidApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 应用ID
        :type AndroidAppId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidAppId = None
        self._RequestId = None

    @property
    def AndroidAppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._RequestId = params.get("RequestId")


class CreateAndroidAppVersionRequest(AbstractModel):
    r"""CreateAndroidAppVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 应用ID
        :type AndroidAppId: str
        :param _DownloadUrl: 应用包下载地址
        :type DownloadUrl: str
        :param _Command: 应用 shell 安装命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :type Command: str
        :param _UninstallCommand: 应用 shell 卸载命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :type UninstallCommand: str
        :param _CleanupMode: 应用资源清理模式（实例安装应用所用资源），取值：CLEANUP_ON_UNINSTALL（默认值），卸载 App 时清理；CLEANUP_AFTER_INSTALL，安装 App 后立即清理。普通应用只有 CLEANUP_AFTER_INSTALL 模式。
        :type CleanupMode: str
        """
        self._AndroidAppId = None
        self._DownloadUrl = None
        self._Command = None
        self._UninstallCommand = None
        self._CleanupMode = None

    @property
    def AndroidAppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def DownloadUrl(self):
        r"""应用包下载地址
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Command(self):
        r"""应用 shell 安装命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def UninstallCommand(self):
        r"""应用 shell 卸载命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :rtype: str
        """
        return self._UninstallCommand

    @UninstallCommand.setter
    def UninstallCommand(self, UninstallCommand):
        self._UninstallCommand = UninstallCommand

    @property
    def CleanupMode(self):
        r"""应用资源清理模式（实例安装应用所用资源），取值：CLEANUP_ON_UNINSTALL（默认值），卸载 App 时清理；CLEANUP_AFTER_INSTALL，安装 App 后立即清理。普通应用只有 CLEANUP_AFTER_INSTALL 模式。
        :rtype: str
        """
        return self._CleanupMode

    @CleanupMode.setter
    def CleanupMode(self, CleanupMode):
        self._CleanupMode = CleanupMode


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._DownloadUrl = params.get("DownloadUrl")
        self._Command = params.get("Command")
        self._UninstallCommand = params.get("UninstallCommand")
        self._CleanupMode = params.get("CleanupMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidAppVersionResponse(AbstractModel):
    r"""CreateAndroidAppVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppVersion: 应用版本
        :type AndroidAppVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidAppVersion = None
        self._RequestId = None

    @property
    def AndroidAppVersion(self):
        r"""应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstanceADBRequest(AbstractModel):
    r"""CreateAndroidInstanceADB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstanceADBResponse(AbstractModel):
    r"""CreateAndroidInstanceADB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivateKey: 连接私钥，需要保存为文件形式，例如 private_key.pem
        :type PrivateKey: str
        :param _UserName: 用户名称
        :type UserName: str
        :param _HostName: 连接地址
        :type HostName: str
        :param _Port: 连接端口
        :type Port: int
        :param _ConnectCommand: 连接参考命令
        :type ConnectCommand: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivateKey = None
        self._UserName = None
        self._HostName = None
        self._Port = None
        self._ConnectCommand = None
        self._RequestId = None

    @property
    def PrivateKey(self):
        r"""连接私钥，需要保存为文件形式，例如 private_key.pem
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def UserName(self):
        r"""用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def HostName(self):
        r"""连接地址
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Port(self):
        r"""连接端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ConnectCommand(self):
        r"""连接参考命令
        :rtype: str
        """
        return self._ConnectCommand

    @ConnectCommand.setter
    def ConnectCommand(self, ConnectCommand):
        self._ConnectCommand = ConnectCommand

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PrivateKey = params.get("PrivateKey")
        self._UserName = params.get("UserName")
        self._HostName = params.get("HostName")
        self._Port = params.get("Port")
        self._ConnectCommand = params.get("ConnectCommand")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstanceImageRequest(AbstractModel):
    r"""CreateAndroidInstanceImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageName: 安卓实例镜像名称
        :type AndroidInstanceImageName: str
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _AndroidInstanceImageDescription: 安卓实例镜像描述
        :type AndroidInstanceImageDescription: str
        """
        self._AndroidInstanceImageName = None
        self._AndroidInstanceId = None
        self._AndroidInstanceImageDescription = None

    @property
    def AndroidInstanceImageName(self):
        r"""安卓实例镜像名称
        :rtype: str
        """
        return self._AndroidInstanceImageName

    @AndroidInstanceImageName.setter
    def AndroidInstanceImageName(self, AndroidInstanceImageName):
        self._AndroidInstanceImageName = AndroidInstanceImageName

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def AndroidInstanceImageDescription(self):
        r"""安卓实例镜像描述
        :rtype: str
        """
        return self._AndroidInstanceImageDescription

    @AndroidInstanceImageDescription.setter
    def AndroidInstanceImageDescription(self, AndroidInstanceImageDescription):
        self._AndroidInstanceImageDescription = AndroidInstanceImageDescription


    def _deserialize(self, params):
        self._AndroidInstanceImageName = params.get("AndroidInstanceImageName")
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._AndroidInstanceImageDescription = params.get("AndroidInstanceImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstanceImageResponse(AbstractModel):
    r"""CreateAndroidInstanceImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageId: 安卓实例镜像 ID
        :type AndroidInstanceImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceImageId = None
        self._RequestId = None

    @property
    def AndroidInstanceImageId(self):
        r"""安卓实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstanceLabelRequest(AbstractModel):
    r"""CreateAndroidInstanceLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值。普通场景下，该值不需要填写；高级场景下，需要两个层级进行分组时才填写。
        :type Value: str
        :param _Description: 标签描述
        :type Description: str
        """
        self._Key = None
        self._Value = None
        self._Description = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值。普通场景下，该值不需要填写；高级场景下，需要两个层级进行分组时才填写。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Description(self):
        r"""标签描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstanceLabelResponse(AbstractModel):
    r"""CreateAndroidInstanceLabel返回参数结构体

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


class CreateAndroidInstanceSSHRequest(AbstractModel):
    r"""CreateAndroidInstanceSSH请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        :param _ExpiredTime: 连接过期时间，最长可设置7天
        :type ExpiredTime: str
        """
        self._AndroidInstanceId = None
        self._ExpiredTime = None

    @property
    def AndroidInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def ExpiredTime(self):
        r"""连接过期时间，最长可设置7天
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstanceSSHResponse(AbstractModel):
    r"""CreateAndroidInstanceSSH返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivateKey: 连接私钥，需要保存为文件形式，例如 private_key.pem
        :type PrivateKey: str
        :param _UserName: 用户名称
        :type UserName: str
        :param _HostName: 连接地址
        :type HostName: str
        :param _Port: 连接端口
        :type Port: int
        :param _ConnectCommand: 连接参考命令
        :type ConnectCommand: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivateKey = None
        self._UserName = None
        self._HostName = None
        self._Port = None
        self._ConnectCommand = None
        self._RequestId = None

    @property
    def PrivateKey(self):
        r"""连接私钥，需要保存为文件形式，例如 private_key.pem
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def UserName(self):
        r"""用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def HostName(self):
        r"""连接地址
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Port(self):
        r"""连接端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ConnectCommand(self):
        r"""连接参考命令
        :rtype: str
        """
        return self._ConnectCommand

    @ConnectCommand.setter
    def ConnectCommand(self, ConnectCommand):
        self._ConnectCommand = ConnectCommand

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PrivateKey = params.get("PrivateKey")
        self._UserName = params.get("UserName")
        self._HostName = params.get("HostName")
        self._Port = params.get("Port")
        self._ConnectCommand = params.get("ConnectCommand")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstanceWebShellRequest(AbstractModel):
    r"""CreateAndroidInstanceWebShell请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例 ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceId(self):
        r"""实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstanceWebShellResponse(AbstractModel):
    r"""CreateAndroidInstanceWebShell返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 鉴权密钥
        :type Key: str
        :param _Address: 连接地址
        :type Address: str
        :param _Zone: 连接区域
        :type Zone: str
        :param _ConnectUrl: 访问链接，可以直接使用此链接访问 WebShell
        :type ConnectUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Key = None
        self._Address = None
        self._Zone = None
        self._ConnectUrl = None
        self._RequestId = None

    @property
    def Key(self):
        r"""鉴权密钥
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Address(self):
        r"""连接地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Zone(self):
        r"""连接区域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ConnectUrl(self):
        r"""访问链接，可以直接使用此链接访问 WebShell
        :rtype: str
        """
        return self._ConnectUrl

    @ConnectUrl.setter
    def ConnectUrl(self, ConnectUrl):
        self._ConnectUrl = ConnectUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Address = params.get("Address")
        self._Zone = params.get("Zone")
        self._ConnectUrl = params.get("ConnectUrl")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstancesAccessTokenRequest(AbstractModel):
    r"""CreateAndroidInstancesAccessToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表。每次请求的实例的上限为 500。
        :type AndroidInstanceIds: list of str
        :param _ExpirationDuration: 有效期，默认为 12 小时，最大为 24 小时。支持 s（秒）、m（分）、h（小时）等单位，比如 12h 表示 12 小时，1h2m3s 表示一小时两分三秒
        :type ExpirationDuration: str
        :param _Mode: 模式。
STANDARD：默认值，标准模式
ACCELERATED：加速模式，该模式需要开通加速服务才能生效
        :type Mode: str
        :param _UserIP: 用户 IP。在加速模式下，该字段必填。
        :type UserIP: str
        """
        self._AndroidInstanceIds = None
        self._ExpirationDuration = None
        self._Mode = None
        self._UserIP = None

    @property
    def AndroidInstanceIds(self):
        r"""实例 ID 列表。每次请求的实例的上限为 500。
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def ExpirationDuration(self):
        r"""有效期，默认为 12 小时，最大为 24 小时。支持 s（秒）、m（分）、h（小时）等单位，比如 12h 表示 12 小时，1h2m3s 表示一小时两分三秒
        :rtype: str
        """
        return self._ExpirationDuration

    @ExpirationDuration.setter
    def ExpirationDuration(self, ExpirationDuration):
        self._ExpirationDuration = ExpirationDuration

    @property
    def Mode(self):
        r"""模式。
STANDARD：默认值，标准模式
ACCELERATED：加速模式，该模式需要开通加速服务才能生效
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def UserIP(self):
        r"""用户 IP。在加速模式下，该字段必填。
        :rtype: str
        """
        return self._UserIP

    @UserIP.setter
    def UserIP(self, UserIP):
        self._UserIP = UserIP


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._ExpirationDuration = params.get("ExpirationDuration")
        self._Mode = params.get("Mode")
        self._UserIP = params.get("UserIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstancesAccessTokenResponse(AbstractModel):
    r"""CreateAndroidInstancesAccessToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: token
        :type Token: str
        :param _AccessInfo: 访问信息
        :type AccessInfo: str
        :param _AndroidInstanceErrors: 安卓实例错误列表。列表包含有问题的安卓实例 ID，生成的 Token 对这些有问题的实例无效。
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._AccessInfo = None
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def Token(self):
        r"""token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def AccessInfo(self):
        r"""访问信息
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def AndroidInstanceErrors(self):
        r"""安卓实例错误列表。列表包含有问题的安卓实例 ID，生成的 Token 对这些有问题的实例无效。
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._AccessInfo = params.get("AccessInfo")
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class CreateAndroidInstancesRequest(AbstractModel):
    r"""CreateAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 安卓实例可用区。
ap-guangzhou-3：广州三区
ap-shenzhen-1：深圳一区
ap-xian-ec-1：西安一区
ap-hangzhou-ec-1：杭州一区
        :type Zone: str
        :param _Type: 安卓实例类型。
A1：单开
A2：双开
A3：三开
A4：四开
A5：五开
A6：六开
        :type Type: str
        :param _Number: 当 HostSerialNumbers 不为空时，该参数表示每个宿主机要创建的安卓实例数量；
当 HostSerialNumbers 为空时，该参数表示要创建安卓实例的总数量，最大值为 100。
        :type Number: int
        :param _HostSerialNumbers: 宿主机 ID 列表。可以指定宿主机 ID 进行创建；也可以不指定由系统自动分配宿主机。
        :type HostSerialNumbers: list of str
        :param _ImageId: 镜像 ID。如果不填，将使用默认的系统镜像
        :type ImageId: str
        :param _Labels: 安卓实例标签列表
        :type Labels: list of AndroidInstanceLabel
        """
        self._Zone = None
        self._Type = None
        self._Number = None
        self._HostSerialNumbers = None
        self._ImageId = None
        self._Labels = None

    @property
    def Zone(self):
        r"""安卓实例可用区。
ap-guangzhou-3：广州三区
ap-shenzhen-1：深圳一区
ap-xian-ec-1：西安一区
ap-hangzhou-ec-1：杭州一区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Type(self):
        r"""安卓实例类型。
A1：单开
A2：双开
A3：三开
A4：四开
A5：五开
A6：六开
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Number(self):
        r"""当 HostSerialNumbers 不为空时，该参数表示每个宿主机要创建的安卓实例数量；
当 HostSerialNumbers 为空时，该参数表示要创建安卓实例的总数量，最大值为 100。
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def HostSerialNumbers(self):
        r"""宿主机 ID 列表。可以指定宿主机 ID 进行创建；也可以不指定由系统自动分配宿主机。
        :rtype: list of str
        """
        return self._HostSerialNumbers

    @HostSerialNumbers.setter
    def HostSerialNumbers(self, HostSerialNumbers):
        self._HostSerialNumbers = HostSerialNumbers

    @property
    def ImageId(self):
        r"""镜像 ID。如果不填，将使用默认的系统镜像
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Labels(self):
        r"""安卓实例标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        self._Number = params.get("Number")
        self._HostSerialNumbers = params.get("HostSerialNumbers")
        self._ImageId = params.get("ImageId")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AndroidInstanceLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstancesResponse(AbstractModel):
    r"""CreateAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceIds = None
        self._RequestId = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstancesScreenshotRequest(AbstractModel):
    r"""CreateAndroidInstancesScreenshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        r"""实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstancesScreenshotResponse(AbstractModel):
    r"""CreateAndroidInstancesScreenshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务列表
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务列表
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateCosCredentialRequest(AbstractModel):
    r"""CreateCosCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CosType: Cos 密钥类型，取值： Mobile 云手游、PC 云端游、AndroidApp 云手机应用管理、AndroidAppFile 云手机文件管理、AndroidAppBackup 云手机备份还原
        :type CosType: str
        :param _AndroidAppCosInfo: 云手机应用管理 Cos 数据
        :type AndroidAppCosInfo: :class:`tencentcloud.gs.v20191118.models.AndroidAppCosInfo`
        :param _AndroidAppFileCosInfo: 云手机文件管理 Cos 数据
        :type AndroidAppFileCosInfo: :class:`tencentcloud.gs.v20191118.models.FileCosInfo`
        """
        self._CosType = None
        self._AndroidAppCosInfo = None
        self._AndroidAppFileCosInfo = None

    @property
    def CosType(self):
        r"""Cos 密钥类型，取值： Mobile 云手游、PC 云端游、AndroidApp 云手机应用管理、AndroidAppFile 云手机文件管理、AndroidAppBackup 云手机备份还原
        :rtype: str
        """
        return self._CosType

    @CosType.setter
    def CosType(self, CosType):
        self._CosType = CosType

    @property
    def AndroidAppCosInfo(self):
        r"""云手机应用管理 Cos 数据
        :rtype: :class:`tencentcloud.gs.v20191118.models.AndroidAppCosInfo`
        """
        return self._AndroidAppCosInfo

    @AndroidAppCosInfo.setter
    def AndroidAppCosInfo(self, AndroidAppCosInfo):
        self._AndroidAppCosInfo = AndroidAppCosInfo

    @property
    def AndroidAppFileCosInfo(self):
        r"""云手机文件管理 Cos 数据
        :rtype: :class:`tencentcloud.gs.v20191118.models.FileCosInfo`
        """
        return self._AndroidAppFileCosInfo

    @AndroidAppFileCosInfo.setter
    def AndroidAppFileCosInfo(self, AndroidAppFileCosInfo):
        self._AndroidAppFileCosInfo = AndroidAppFileCosInfo


    def _deserialize(self, params):
        self._CosType = params.get("CosType")
        if params.get("AndroidAppCosInfo") is not None:
            self._AndroidAppCosInfo = AndroidAppCosInfo()
            self._AndroidAppCosInfo._deserialize(params.get("AndroidAppCosInfo"))
        if params.get("AndroidAppFileCosInfo") is not None:
            self._AndroidAppFileCosInfo = FileCosInfo()
            self._AndroidAppFileCosInfo._deserialize(params.get("AndroidAppFileCosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosCredentialResponse(AbstractModel):
    r"""CreateCosCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretID: Cos SecretID
        :type SecretID: str
        :param _SecretKey: Cos SecretKey
        :type SecretKey: str
        :param _SessionToken: Cos Session
        :type SessionToken: str
        :param _CosBucket: Cos Bucket
        :type CosBucket: str
        :param _CosRegion: Cos Region
        :type CosRegion: str
        :param _Path: Cos 操作路径
        :type Path: str
        :param _StartTime: Cos 密钥的起始时间
        :type StartTime: int
        :param _ExpiredTime: Cos 密钥的失效时间
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretID = None
        self._SecretKey = None
        self._SessionToken = None
        self._CosBucket = None
        self._CosRegion = None
        self._Path = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def SecretID(self):
        r"""Cos SecretID
        :rtype: str
        """
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SecretKey(self):
        r"""Cos SecretKey
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SessionToken(self):
        r"""Cos Session
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def CosBucket(self):
        r"""Cos Bucket
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        r"""Cos Region
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def Path(self):
        r"""Cos 操作路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def StartTime(self):
        r"""Cos 密钥的起始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        r"""Cos 密钥的失效时间
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretID = params.get("SecretID")
        self._SecretKey = params.get("SecretKey")
        self._SessionToken = params.get("SessionToken")
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._Path = params.get("Path")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class CreateSessionRequest(AbstractModel):
    r"""CreateSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _GameId: 【已废弃】只在TrylockWorker时生效
        :type GameId: str
        :param _GameRegion: 【已废弃】只在TrylockWorker时生效
        :type GameRegion: str
        :param _GameParas: 游戏参数
        :type GameParas: str
        :param _ClientSession: 客户端session信息，从JSSDK请求中获得。特殊的，当 RunMode 参数为 RunWithoutClient 时，该字段可以为空
        :type ClientSession: str
        :param _Resolution: 分辨率,，可设置为1080p或720p或1920x1080格式
        :type Resolution: str
        :param _ImageUrl: 背景图url，格式为png或jpeg，宽高1920*1080
        :type ImageUrl: str
        :param _SetNo: 【已废弃】
        :type SetNo: int
        :param _Bitrate: 【已废弃】
        :type Bitrate: int
        :param _MaxBitrate: 单位Mbps，动态调整最大码率建议值，会按实际情况调整
        :type MaxBitrate: int
        :param _MinBitrate: 单位Mbps，动态调整最小码率建议值，会按实际情况调整
        :type MinBitrate: int
        :param _Fps: 帧率，可设置为30、45、60、90、120、144
        :type Fps: int
        :param _UserIp: 【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :type UserIp: str
        :param _Optimization: 【已废弃】优化项，便于客户灰度开启新的优化项，默认为0
        :type Optimization: int
        :param _HostUserId: 【互动云游】游戏主机用户ID
        :type HostUserId: str
        :param _Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者
        :type Role: str
        :param _GameContext: 游戏相关参数
        :type GameContext: str
        :param _RunMode: 云端运行模式。
RunWithoutClient：允许无客户端连接的情况下仍保持云端 App 运行
默认值（空）：要求必须有客户端连接才会保持云端 App 运行。
        :type RunMode: str
        """
        self._UserId = None
        self._GameId = None
        self._GameRegion = None
        self._GameParas = None
        self._ClientSession = None
        self._Resolution = None
        self._ImageUrl = None
        self._SetNo = None
        self._Bitrate = None
        self._MaxBitrate = None
        self._MinBitrate = None
        self._Fps = None
        self._UserIp = None
        self._Optimization = None
        self._HostUserId = None
        self._Role = None
        self._GameContext = None
        self._RunMode = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        r"""【已废弃】只在TrylockWorker时生效
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameRegion(self):
        r"""【已废弃】只在TrylockWorker时生效
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def GameParas(self):
        r"""游戏参数
        :rtype: str
        """
        return self._GameParas

    @GameParas.setter
    def GameParas(self, GameParas):
        self._GameParas = GameParas

    @property
    def ClientSession(self):
        r"""客户端session信息，从JSSDK请求中获得。特殊的，当 RunMode 参数为 RunWithoutClient 时，该字段可以为空
        :rtype: str
        """
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def Resolution(self):
        r"""分辨率,，可设置为1080p或720p或1920x1080格式
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def ImageUrl(self):
        r"""背景图url，格式为png或jpeg，宽高1920*1080
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def SetNo(self):
        r"""【已废弃】
        :rtype: int
        """
        return self._SetNo

    @SetNo.setter
    def SetNo(self, SetNo):
        self._SetNo = SetNo

    @property
    def Bitrate(self):
        r"""【已废弃】
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def MaxBitrate(self):
        r"""单位Mbps，动态调整最大码率建议值，会按实际情况调整
        :rtype: int
        """
        return self._MaxBitrate

    @MaxBitrate.setter
    def MaxBitrate(self, MaxBitrate):
        self._MaxBitrate = MaxBitrate

    @property
    def MinBitrate(self):
        r"""单位Mbps，动态调整最小码率建议值，会按实际情况调整
        :rtype: int
        """
        return self._MinBitrate

    @MinBitrate.setter
    def MinBitrate(self, MinBitrate):
        self._MinBitrate = MinBitrate

    @property
    def Fps(self):
        r"""帧率，可设置为30、45、60、90、120、144
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def UserIp(self):
        r"""【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Optimization(self):
        r"""【已废弃】优化项，便于客户灰度开启新的优化项，默认为0
        :rtype: int
        """
        return self._Optimization

    @Optimization.setter
    def Optimization(self, Optimization):
        self._Optimization = Optimization

    @property
    def HostUserId(self):
        r"""【互动云游】游戏主机用户ID
        :rtype: str
        """
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId

    @property
    def Role(self):
        r"""【互动云游】角色；Player表示玩家；Viewer表示观察者
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def GameContext(self):
        r"""游戏相关参数
        :rtype: str
        """
        return self._GameContext

    @GameContext.setter
    def GameContext(self, GameContext):
        self._GameContext = GameContext

    @property
    def RunMode(self):
        r"""云端运行模式。
RunWithoutClient：允许无客户端连接的情况下仍保持云端 App 运行
默认值（空）：要求必须有客户端连接才会保持云端 App 运行。
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        self._GameRegion = params.get("GameRegion")
        self._GameParas = params.get("GameParas")
        self._ClientSession = params.get("ClientSession")
        self._Resolution = params.get("Resolution")
        self._ImageUrl = params.get("ImageUrl")
        self._SetNo = params.get("SetNo")
        self._Bitrate = params.get("Bitrate")
        self._MaxBitrate = params.get("MaxBitrate")
        self._MinBitrate = params.get("MinBitrate")
        self._Fps = params.get("Fps")
        self._UserIp = params.get("UserIp")
        self._Optimization = params.get("Optimization")
        self._HostUserId = params.get("HostUserId")
        self._Role = params.get("Role")
        self._GameContext = params.get("GameContext")
        self._RunMode = params.get("RunMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    r"""CreateSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerSession: 服务端session信息，返回给JSSDK
        :type ServerSession: str
        :param _RoleNumber: 【已废弃】
        :type RoleNumber: str
        :param _Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者
        :type Role: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerSession = None
        self._RoleNumber = None
        self._Role = None
        self._RequestId = None

    @property
    def ServerSession(self):
        r"""服务端session信息，返回给JSSDK
        :rtype: str
        """
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RoleNumber(self):
        r"""【已废弃】
        :rtype: str
        """
        return self._RoleNumber

    @RoleNumber.setter
    def RoleNumber(self, RoleNumber):
        self._RoleNumber = RoleNumber

    @property
    def Role(self):
        r"""【互动云游】角色；Player表示玩家；Viewer表示观察者
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServerSession = params.get("ServerSession")
        self._RoleNumber = params.get("RoleNumber")
        self._Role = params.get("Role")
        self._RequestId = params.get("RequestId")


class DeleteAndroidAppRequest(AbstractModel):
    r"""DeleteAndroidApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 应用ID
        :type AndroidAppId: str
        """
        self._AndroidAppId = None

    @property
    def AndroidAppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAndroidAppResponse(AbstractModel):
    r"""DeleteAndroidApp返回参数结构体

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


class DeleteAndroidAppVersionRequest(AbstractModel):
    r"""DeleteAndroidAppVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 安卓应用 Id
        :type AndroidAppId: str
        :param _AndroidAppVersion: 安卓应用版本
        :type AndroidAppVersion: str
        """
        self._AndroidAppId = None
        self._AndroidAppVersion = None

    @property
    def AndroidAppId(self):
        r"""安卓应用 Id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def AndroidAppVersion(self):
        r"""安卓应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAndroidAppVersionResponse(AbstractModel):
    r"""DeleteAndroidAppVersion返回参数结构体

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


class DeleteAndroidInstanceBackupFilesRequest(AbstractModel):
    r"""DeleteAndroidInstanceBackupFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ObjectKeys: 文件对象键列表
        :type ObjectKeys: list of str
        :param _StorageType: 存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :type StorageType: str
        :param _COSOptions: COS协议选项
        :type COSOptions: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        :param _S3Options: S3存储协议选项
        :type S3Options: :class:`tencentcloud.gs.v20191118.models.S3Options`
        :param _AndroidInstanceZone: 安卓实例可用区。StorageType 为 S3 时，需要填写该字段；StorageType 为 COS 时，不需要填写该字段
        :type AndroidInstanceZone: str
        """
        self._ObjectKeys = None
        self._StorageType = None
        self._COSOptions = None
        self._S3Options = None
        self._AndroidInstanceZone = None

    @property
    def ObjectKeys(self):
        r"""文件对象键列表
        :rtype: list of str
        """
        return self._ObjectKeys

    @ObjectKeys.setter
    def ObjectKeys(self, ObjectKeys):
        self._ObjectKeys = ObjectKeys

    @property
    def StorageType(self):
        r"""存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def COSOptions(self):
        r"""COS协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        """
        return self._COSOptions

    @COSOptions.setter
    def COSOptions(self, COSOptions):
        self._COSOptions = COSOptions

    @property
    def S3Options(self):
        r"""S3存储协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.S3Options`
        """
        return self._S3Options

    @S3Options.setter
    def S3Options(self, S3Options):
        self._S3Options = S3Options

    @property
    def AndroidInstanceZone(self):
        r"""安卓实例可用区。StorageType 为 S3 时，需要填写该字段；StorageType 为 COS 时，不需要填写该字段
        :rtype: str
        """
        return self._AndroidInstanceZone

    @AndroidInstanceZone.setter
    def AndroidInstanceZone(self, AndroidInstanceZone):
        self._AndroidInstanceZone = AndroidInstanceZone


    def _deserialize(self, params):
        self._ObjectKeys = params.get("ObjectKeys")
        self._StorageType = params.get("StorageType")
        if params.get("COSOptions") is not None:
            self._COSOptions = COSOptions()
            self._COSOptions._deserialize(params.get("COSOptions"))
        if params.get("S3Options") is not None:
            self._S3Options = S3Options()
            self._S3Options._deserialize(params.get("S3Options"))
        self._AndroidInstanceZone = params.get("AndroidInstanceZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAndroidInstanceBackupFilesResponse(AbstractModel):
    r"""DeleteAndroidInstanceBackupFiles返回参数结构体

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


class DeleteAndroidInstanceBackupsRequest(AbstractModel):
    r"""DeleteAndroidInstanceBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupIds: 备份ID列表
        :type BackupIds: list of str
        """
        self._BackupIds = None

    @property
    def BackupIds(self):
        r"""备份ID列表
        :rtype: list of str
        """
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds


    def _deserialize(self, params):
        self._BackupIds = params.get("BackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAndroidInstanceBackupsResponse(AbstractModel):
    r"""DeleteAndroidInstanceBackups返回参数结构体

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


class DeleteAndroidInstanceImagesRequest(AbstractModel):
    r"""DeleteAndroidInstanceImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageIds: 镜像 ID 列表
        :type AndroidInstanceImageIds: list of str
        """
        self._AndroidInstanceImageIds = None

    @property
    def AndroidInstanceImageIds(self):
        r"""镜像 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceImageIds

    @AndroidInstanceImageIds.setter
    def AndroidInstanceImageIds(self, AndroidInstanceImageIds):
        self._AndroidInstanceImageIds = AndroidInstanceImageIds


    def _deserialize(self, params):
        self._AndroidInstanceImageIds = params.get("AndroidInstanceImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAndroidInstanceImagesResponse(AbstractModel):
    r"""DeleteAndroidInstanceImages返回参数结构体

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


class DeleteAndroidInstanceLabelRequest(AbstractModel):
    r"""DeleteAndroidInstanceLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
        


class DeleteAndroidInstanceLabelResponse(AbstractModel):
    r"""DeleteAndroidInstanceLabel返回参数结构体

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


class DescribeAndroidAppsRequest(AbstractModel):
    r"""DescribeAndroidApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        :param _AndroidAppIds: 应用ID数组
        :type AndroidAppIds: list of str
        :param _Filters: 过滤条件，支持过滤的字段有：UserId、State、UpdateState、Name、AppMode 。其中 Name 为模糊匹配，其他参数为精确匹配。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._AndroidAppIds = None
        self._Filters = None

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
        r"""每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AndroidAppIds(self):
        r"""应用ID数组
        :rtype: list of str
        """
        return self._AndroidAppIds

    @AndroidAppIds.setter
    def AndroidAppIds(self, AndroidAppIds):
        self._AndroidAppIds = AndroidAppIds

    @property
    def Filters(self):
        r"""过滤条件，支持过滤的字段有：UserId、State、UpdateState、Name、AppMode 。其中 Name 为模糊匹配，其他参数为精确匹配。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AndroidAppIds = params.get("AndroidAppIds")
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
        


class DescribeAndroidAppsResponse(AbstractModel):
    r"""DescribeAndroidApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Apps: 安卓应用列表
        :type Apps: list of AndroidApp
        :param _TotalCount: 安卓应用列表长度
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Apps = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Apps(self):
        r"""安卓应用列表
        :rtype: list of AndroidApp
        """
        return self._Apps

    @Apps.setter
    def Apps(self, Apps):
        self._Apps = Apps

    @property
    def TotalCount(self):
        r"""安卓应用列表长度
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
        if params.get("Apps") is not None:
            self._Apps = []
            for item in params.get("Apps"):
                obj = AndroidApp()
                obj._deserialize(item)
                self._Apps.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstanceAppsRequest(AbstractModel):
    r"""DescribeAndroidInstanceApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstanceAppsResponse(AbstractModel):
    r"""DescribeAndroidInstanceApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Apps: 安卓应用列表
        :type Apps: list of AndroidInstanceAppInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Apps = None
        self._RequestId = None

    @property
    def Apps(self):
        r"""安卓应用列表
        :rtype: list of AndroidInstanceAppInfo
        """
        return self._Apps

    @Apps.setter
    def Apps(self, Apps):
        self._Apps = Apps

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Apps") is not None:
            self._Apps = []
            for item in params.get("Apps"):
                obj = AndroidInstanceAppInfo()
                obj._deserialize(item)
                self._Apps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstanceBackupsRequest(AbstractModel):
    r"""DescribeAndroidInstanceBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupIds: 备份ID列表
        :type BackupIds: list of str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        """
        self._BackupIds = None
        self._Offset = None
        self._Limit = None

    @property
    def BackupIds(self):
        r"""备份ID列表
        :rtype: list of str
        """
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds

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
        r"""每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BackupIds = params.get("BackupIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstanceBackupsResponse(AbstractModel):
    r"""DescribeAndroidInstanceBackups返回参数结构体

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


class DescribeAndroidInstanceImagesRequest(AbstractModel):
    r"""DescribeAndroidInstanceImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageIds: 镜像 ID 列表
        :type AndroidInstanceImageIds: list of str
        :param _AndroidInstanceImageZones: 镜像可用区列表
        :type AndroidInstanceImageZones: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 限制量，默认为20，最大值为100
        :type Limit: int
        :param _Filters: 字段过滤器。Filter 的 Name 有以下值：
ImageName：镜像名称
ImageState：镜像状态
AndroidVersion：安卓版本
        :type Filters: list of Filter
        """
        self._AndroidInstanceImageIds = None
        self._AndroidInstanceImageZones = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def AndroidInstanceImageIds(self):
        r"""镜像 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceImageIds

    @AndroidInstanceImageIds.setter
    def AndroidInstanceImageIds(self, AndroidInstanceImageIds):
        self._AndroidInstanceImageIds = AndroidInstanceImageIds

    @property
    def AndroidInstanceImageZones(self):
        r"""镜像可用区列表
        :rtype: list of str
        """
        return self._AndroidInstanceImageZones

    @AndroidInstanceImageZones.setter
    def AndroidInstanceImageZones(self, AndroidInstanceImageZones):
        self._AndroidInstanceImageZones = AndroidInstanceImageZones

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""字段过滤器。Filter 的 Name 有以下值：
ImageName：镜像名称
ImageState：镜像状态
AndroidVersion：安卓版本
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AndroidInstanceImageIds = params.get("AndroidInstanceImageIds")
        self._AndroidInstanceImageZones = params.get("AndroidInstanceImageZones")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeAndroidInstanceImagesResponse(AbstractModel):
    r"""DescribeAndroidInstanceImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 镜像总数
        :type Total: int
        :param _AndroidInstanceImages: 镜像列表
        :type AndroidInstanceImages: list of AndroidInstanceImage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AndroidInstanceImages = None
        self._RequestId = None

    @property
    def Total(self):
        r"""镜像总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AndroidInstanceImages(self):
        r"""镜像列表
        :rtype: list of AndroidInstanceImage
        """
        return self._AndroidInstanceImages

    @AndroidInstanceImages.setter
    def AndroidInstanceImages(self, AndroidInstanceImages):
        self._AndroidInstanceImages = AndroidInstanceImages

    @property
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
        if params.get("AndroidInstanceImages") is not None:
            self._AndroidInstanceImages = []
            for item in params.get("AndroidInstanceImages"):
                obj = AndroidInstanceImage()
                obj._deserialize(item)
                self._AndroidInstanceImages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstanceLabelsRequest(AbstractModel):
    r"""DescribeAndroidInstanceLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Keys: 标签键列表
        :type Keys: list of str
        :param _Values: 标签值列表
        :type Values: list of str
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 限制量，默认为20，最大值为100
        :type Limit: int
        """
        self._Keys = None
        self._Values = None
        self._Offset = None
        self._Limit = None

    @property
    def Keys(self):
        r"""标签键列表
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Values(self):
        r"""标签值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Offset(self):
        r"""偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Keys = params.get("Keys")
        self._Values = params.get("Values")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstanceLabelsResponse(AbstractModel):
    r"""DescribeAndroidInstanceLabels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 安卓实例标签总数
        :type Total: int
        :param _Labels: 安卓实例标签列表
        :type Labels: list of AndroidInstanceLabel
        :param _AndroidInstanceLabels: 安卓实例标签详情列表
        :type AndroidInstanceLabels: list of AndroidInstanceLabelDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Labels = None
        self._AndroidInstanceLabels = None
        self._RequestId = None

    @property
    def Total(self):
        r"""安卓实例标签总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Labels(self):
        warnings.warn("parameter `Labels` is deprecated", DeprecationWarning) 

        r"""安卓实例标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        warnings.warn("parameter `Labels` is deprecated", DeprecationWarning) 

        self._Labels = Labels

    @property
    def AndroidInstanceLabels(self):
        r"""安卓实例标签详情列表
        :rtype: list of AndroidInstanceLabelDetail
        """
        return self._AndroidInstanceLabels

    @AndroidInstanceLabels.setter
    def AndroidInstanceLabels(self, AndroidInstanceLabels):
        self._AndroidInstanceLabels = AndroidInstanceLabels

    @property
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
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AndroidInstanceLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("AndroidInstanceLabels") is not None:
            self._AndroidInstanceLabels = []
            for item in params.get("AndroidInstanceLabels"):
                obj = AndroidInstanceLabelDetail()
                obj._deserialize(item)
                self._AndroidInstanceLabels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstanceTasksStatusRequest(AbstractModel):
    r"""DescribeAndroidInstanceTasksStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务 ID 列表
        :type TaskIds: list of str
        :param _Filter: 条件过滤器
        :type Filter: list of Filter
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 限制量，默认为20，最大值为100
        :type Limit: int
        :param _RecentDays: 时间范围限制，以天数为单位
        :type RecentDays: int
        """
        self._TaskIds = None
        self._Filter = None
        self._Offset = None
        self._Limit = None
        self._RecentDays = None

    @property
    def TaskIds(self):
        r"""任务 ID 列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Filter(self):
        r"""条件过滤器
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Offset(self):
        r"""偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RecentDays(self):
        r"""时间范围限制，以天数为单位
        :rtype: int
        """
        return self._RecentDays

    @RecentDays.setter
    def RecentDays(self, RecentDays):
        self._RecentDays = RecentDays


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RecentDays = params.get("RecentDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstanceTasksStatusResponse(AbstractModel):
    r"""DescribeAndroidInstanceTasksStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatusSet: 任务状态集合
        :type TaskStatusSet: list of AndroidInstanceTaskStatus
        :param _Total: 任务总数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatusSet = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskStatusSet(self):
        r"""任务状态集合
        :rtype: list of AndroidInstanceTaskStatus
        """
        return self._TaskStatusSet

    @TaskStatusSet.setter
    def TaskStatusSet(self, TaskStatusSet):
        self._TaskStatusSet = TaskStatusSet

    @property
    def Total(self):
        r"""任务总数量
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
        if params.get("TaskStatusSet") is not None:
            self._TaskStatusSet = []
            for item in params.get("TaskStatusSet"):
                obj = AndroidInstanceTaskStatus()
                obj._deserialize(item)
                self._TaskStatusSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstancesAppBlacklistRequest(AbstractModel):
    r"""DescribeAndroidInstancesAppBlacklist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表，数量上限 100
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        r"""实例 ID 列表，数量上限 100
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstancesAppBlacklistResponse(AbstractModel):
    r"""DescribeAndroidInstancesAppBlacklist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBlacklistSet: 黑名单集合
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBlacklistSet: list of AndroidInstanceAppBlacklist
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBlacklistSet = None
        self._RequestId = None

    @property
    def AppBlacklistSet(self):
        r"""黑名单集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AndroidInstanceAppBlacklist
        """
        return self._AppBlacklistSet

    @AppBlacklistSet.setter
    def AppBlacklistSet(self, AppBlacklistSet):
        self._AppBlacklistSet = AppBlacklistSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppBlacklistSet") is not None:
            self._AppBlacklistSet = []
            for item in params.get("AppBlacklistSet"):
                obj = AndroidInstanceAppBlacklist()
                obj._deserialize(item)
                self._AppBlacklistSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstancesByAppsRequest(AbstractModel):
    r"""DescribeAndroidInstancesByApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为 0	
        :type Offset: int
        :param _Limit: 限制量，默认为 20，最大值为 500	
        :type Limit: int
        :param _AndroidAppIds: 应用 ID 列表。当 AndroidIds 为多条数据时（例如 app1, app2），返回的实例列表为：安装了 app1 应用的实例和安装了 app2 应用的实例集合（并集）。
        :type AndroidAppIds: list of str
        :param _Filters: 字段过滤器，Filter 的 Name 有以下值： AndroidInstanceId：实例 Id
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._AndroidAppIds = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，默认为 0	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制量，默认为 20，最大值为 500	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AndroidAppIds(self):
        r"""应用 ID 列表。当 AndroidIds 为多条数据时（例如 app1, app2），返回的实例列表为：安装了 app1 应用的实例和安装了 app2 应用的实例集合（并集）。
        :rtype: list of str
        """
        return self._AndroidAppIds

    @AndroidAppIds.setter
    def AndroidAppIds(self, AndroidAppIds):
        self._AndroidAppIds = AndroidAppIds

    @property
    def Filters(self):
        r"""字段过滤器，Filter 的 Name 有以下值： AndroidInstanceId：实例 Id
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AndroidAppIds = params.get("AndroidAppIds")
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
        


class DescribeAndroidInstancesByAppsResponse(AbstractModel):
    r"""DescribeAndroidInstancesByApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数量
        :type TotalCount: int
        :param _AndroidInstances: 实例列表	
        :type AndroidInstances: list of AndroidInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AndroidInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AndroidInstances(self):
        r"""实例列表	
        :rtype: list of AndroidInstance
        """
        return self._AndroidInstances

    @AndroidInstances.setter
    def AndroidInstances(self, AndroidInstances):
        self._AndroidInstances = AndroidInstances

    @property
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
        if params.get("AndroidInstances") is not None:
            self._AndroidInstances = []
            for item in params.get("AndroidInstances"):
                obj = AndroidInstance()
                obj._deserialize(item)
                self._AndroidInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstancesRequest(AbstractModel):
    r"""DescribeAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 限制量，默认为20，最大值为100
        :type Limit: int
        :param _AndroidInstanceIds: 实例ID。每次请求的实例的上限为100。
        :type AndroidInstanceIds: list of str
        :param _AndroidInstanceRegion: 实例地域。目前还不支持按地域进行聚合查询
        :type AndroidInstanceRegion: str
        :param _AndroidInstanceZone: 实例可用区
        :type AndroidInstanceZone: str
        :param _AndroidInstanceGroupIds: 实例分组 ID 列表
        :type AndroidInstanceGroupIds: list of str
        :param _LabelSelector: 实例标签选择器
        :type LabelSelector: list of LabelRequirement
        :param _Filters: 字段过滤器。Filter 的 Name 有以下值：
Name：实例名称
UserId：实例用户ID
HostSerialNumber：宿主机序列号
HostServerSerialNumber：机箱序列号
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._AndroidInstanceIds = None
        self._AndroidInstanceRegion = None
        self._AndroidInstanceZone = None
        self._AndroidInstanceGroupIds = None
        self._LabelSelector = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AndroidInstanceIds(self):
        r"""实例ID。每次请求的实例的上限为100。
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidInstanceRegion(self):
        r"""实例地域。目前还不支持按地域进行聚合查询
        :rtype: str
        """
        return self._AndroidInstanceRegion

    @AndroidInstanceRegion.setter
    def AndroidInstanceRegion(self, AndroidInstanceRegion):
        self._AndroidInstanceRegion = AndroidInstanceRegion

    @property
    def AndroidInstanceZone(self):
        r"""实例可用区
        :rtype: str
        """
        return self._AndroidInstanceZone

    @AndroidInstanceZone.setter
    def AndroidInstanceZone(self, AndroidInstanceZone):
        self._AndroidInstanceZone = AndroidInstanceZone

    @property
    def AndroidInstanceGroupIds(self):
        r"""实例分组 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceGroupIds

    @AndroidInstanceGroupIds.setter
    def AndroidInstanceGroupIds(self, AndroidInstanceGroupIds):
        self._AndroidInstanceGroupIds = AndroidInstanceGroupIds

    @property
    def LabelSelector(self):
        r"""实例标签选择器
        :rtype: list of LabelRequirement
        """
        return self._LabelSelector

    @LabelSelector.setter
    def LabelSelector(self, LabelSelector):
        self._LabelSelector = LabelSelector

    @property
    def Filters(self):
        r"""字段过滤器。Filter 的 Name 有以下值：
Name：实例名称
UserId：实例用户ID
HostSerialNumber：宿主机序列号
HostServerSerialNumber：机箱序列号
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._AndroidInstanceRegion = params.get("AndroidInstanceRegion")
        self._AndroidInstanceZone = params.get("AndroidInstanceZone")
        self._AndroidInstanceGroupIds = params.get("AndroidInstanceGroupIds")
        if params.get("LabelSelector") is not None:
            self._LabelSelector = []
            for item in params.get("LabelSelector"):
                obj = LabelRequirement()
                obj._deserialize(item)
                self._LabelSelector.append(obj)
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
        


class DescribeAndroidInstancesResponse(AbstractModel):
    r"""DescribeAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数量
        :type TotalCount: int
        :param _AndroidInstances: 实例列表
        :type AndroidInstances: list of AndroidInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AndroidInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AndroidInstances(self):
        r"""实例列表
        :rtype: list of AndroidInstance
        """
        return self._AndroidInstances

    @AndroidInstances.setter
    def AndroidInstances(self, AndroidInstances):
        self._AndroidInstances = AndroidInstances

    @property
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
        if params.get("AndroidInstances") is not None:
            self._AndroidInstances = []
            for item in params.get("AndroidInstances"):
                obj = AndroidInstance()
                obj._deserialize(item)
                self._AndroidInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesCountRequest(AbstractModel):
    r"""DescribeInstancesCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏ID
        :type GameId: str
        :param _GroupId: 实例分组ID
        :type GroupId: str
        :param _GameRegion: 游戏区域
        :type GameRegion: str
        :param _GameType: 游戏类型。
MOBILE：手游
PC：默认值，端游
        :type GameType: str
        """
        self._GameId = None
        self._GroupId = None
        self._GameRegion = None
        self._GameType = None

    @property
    def GameId(self):
        r"""游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GroupId(self):
        r"""实例分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GameRegion(self):
        r"""游戏区域
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def GameType(self):
        r"""游戏类型。
MOBILE：手游
PC：默认值，端游
        :rtype: str
        """
        return self._GameType

    @GameType.setter
    def GameType(self, GameType):
        self._GameType = GameType


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._GroupId = params.get("GroupId")
        self._GameRegion = params.get("GameRegion")
        self._GameType = params.get("GameType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesCountResponse(AbstractModel):
    r"""DescribeInstancesCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 客户的实例总数
        :type Total: int
        :param _Running: 客户的实例运行数
        :type Running: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Running = None
        self._RequestId = None

    @property
    def Total(self):
        r"""客户的实例总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Running(self):
        r"""客户的实例运行数
        :rtype: int
        """
        return self._Running

    @Running.setter
    def Running(self, Running):
        self._Running = Running

    @property
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
        self._Running = params.get("Running")
        self._RequestId = params.get("RequestId")


class DestroyAndroidInstancesRequest(AbstractModel):
    r"""DestroyAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyAndroidInstancesResponse(AbstractModel):
    r"""DestroyAndroidInstances返回参数结构体

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


class DisableAndroidInstancesAppRequest(AbstractModel):
    r"""DisableAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表（最大100条数据）
        :type AndroidInstanceIds: list of str
        :param _PackageName: 应用包名
        :type PackageName: str
        """
        self._AndroidInstanceIds = None
        self._PackageName = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表（最大100条数据）
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableAndroidInstancesAppResponse(AbstractModel):
    r"""DisableAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class DisconnectAndroidInstanceRequest(AbstractModel):
    r"""DisconnectAndroidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisconnectAndroidInstanceResponse(AbstractModel):
    r"""DisconnectAndroidInstance返回参数结构体

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


class DistributeAndroidInstanceImageToHostsRequest(AbstractModel):
    r"""DistributeAndroidInstanceImageToHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostSerialNumbers: 宿主机序列号数组
        :type HostSerialNumbers: list of str
        :param _ImageId: 实例镜像 ID
        :type ImageId: str
        """
        self._HostSerialNumbers = None
        self._ImageId = None

    @property
    def HostSerialNumbers(self):
        r"""宿主机序列号数组
        :rtype: list of str
        """
        return self._HostSerialNumbers

    @HostSerialNumbers.setter
    def HostSerialNumbers(self, HostSerialNumbers):
        self._HostSerialNumbers = HostSerialNumbers

    @property
    def ImageId(self):
        r"""实例镜像 ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._HostSerialNumbers = params.get("HostSerialNumbers")
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeAndroidInstanceImageToHostsResponse(AbstractModel):
    r"""DistributeAndroidInstanceImageToHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceHostTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceHostTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceHostTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DistributeFileToAndroidInstancesRequest(AbstractModel):
    r"""DistributeFileToAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _FileURL: 文件下载 URL
        :type FileURL: str
        :param _DestinationDirectory: 上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :type DestinationDirectory: str
        :param _DestinationFileName: 目标文件名
        :type DestinationFileName: str
        """
        self._AndroidInstanceIds = None
        self._FileURL = None
        self._DestinationDirectory = None
        self._DestinationFileName = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

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
    def DestinationDirectory(self):
        r"""上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :rtype: str
        """
        return self._DestinationDirectory

    @DestinationDirectory.setter
    def DestinationDirectory(self, DestinationDirectory):
        self._DestinationDirectory = DestinationDirectory

    @property
    def DestinationFileName(self):
        r"""目标文件名
        :rtype: str
        """
        return self._DestinationFileName

    @DestinationFileName.setter
    def DestinationFileName(self, DestinationFileName):
        self._DestinationFileName = DestinationFileName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._FileURL = params.get("FileURL")
        self._DestinationDirectory = params.get("DestinationDirectory")
        self._DestinationFileName = params.get("DestinationFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeFileToAndroidInstancesResponse(AbstractModel):
    r"""DistributeFileToAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 实例任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""实例任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DistributePhotoToAndroidInstancesRequest(AbstractModel):
    r"""DistributePhotoToAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _PhotoURL: 照片下载 URL
        :type PhotoURL: str
        """
        self._AndroidInstanceIds = None
        self._PhotoURL = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PhotoURL(self):
        r"""照片下载 URL
        :rtype: str
        """
        return self._PhotoURL

    @PhotoURL.setter
    def PhotoURL(self, PhotoURL):
        self._PhotoURL = PhotoURL


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PhotoURL = params.get("PhotoURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributePhotoToAndroidInstancesResponse(AbstractModel):
    r"""DistributePhotoToAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 实例任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""实例任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class EnableAndroidInstancesAppRequest(AbstractModel):
    r"""EnableAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表（最大100条数据）
        :type AndroidInstanceIds: list of str
        :param _PackageName: 应用包名
        :type PackageName: str
        """
        self._AndroidInstanceIds = None
        self._PackageName = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表（最大100条数据）
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableAndroidInstancesAppResponse(AbstractModel):
    r"""EnableAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class Error(AbstractModel):
    r"""错误信息，用于批量接口中返回部分操作错误

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: str
        :param _Message: 错误详细信息
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        r"""错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误详细信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteCommandOnAndroidInstancesRequest(AbstractModel):
    r"""ExecuteCommandOnAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _Command: shell 命令
        :type Command: str
        """
        self._AndroidInstanceIds = None
        self._Command = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Command(self):
        r"""shell 命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteCommandOnAndroidInstancesResponse(AbstractModel):
    r"""ExecuteCommandOnAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合，可异步查询任务状态
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合，可异步查询任务状态
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class FetchAndroidInstancesLogsRequest(AbstractModel):
    r"""FetchAndroidInstancesLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _BucketName: cos 桶名称
        :type BucketName: str
        :param _BucketRegion: cos 桶区域
        :type BucketRegion: str
        :param _BucketDirectory: cos 桶目录，默认为 /log/
        :type BucketDirectory: str
        :param _RecentDays: 下载最近几天的日志，默认值为 1
        :type RecentDays: int
        """
        self._AndroidInstanceIds = None
        self._BucketName = None
        self._BucketRegion = None
        self._BucketDirectory = None
        self._RecentDays = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def BucketName(self):
        r"""cos 桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        r"""cos 桶区域
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketDirectory(self):
        r"""cos 桶目录，默认为 /log/
        :rtype: str
        """
        return self._BucketDirectory

    @BucketDirectory.setter
    def BucketDirectory(self, BucketDirectory):
        self._BucketDirectory = BucketDirectory

    @property
    def RecentDays(self):
        r"""下载最近几天的日志，默认值为 1
        :rtype: int
        """
        return self._RecentDays

    @RecentDays.setter
    def RecentDays(self, RecentDays):
        self._RecentDays = RecentDays


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        self._BucketDirectory = params.get("BucketDirectory")
        self._RecentDays = params.get("RecentDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchAndroidInstancesLogsResponse(AbstractModel):
    r"""FetchAndroidInstancesLogs返回参数结构体

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


class FileCosInfo(AbstractModel):
    r"""应用文件 Cos 信息

    """

    def __init__(self):
        r"""
        :param _FileId: 文件 Id
        :type FileId: str
        """
        self._FileId = None

    @property
    def FileId(self):
        r"""文件 Id
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤

    """

    def __init__(self):
        r"""
        :param _Name: 字段名
        :type Name: str
        :param _Values: 字段值列表
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""字段值列表
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
        


class ImportAndroidInstanceImageRequest(AbstractModel):
    r"""ImportAndroidInstanceImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 镜像名称
        :type Name: str
        :param _URL: 镜像文件下载地址，要求是 tgz 压缩文件
        :type URL: str
        :param _MD5: 镜像文件 MD5 值
        :type MD5: str
        :param _AndroidVersion: 安卓版本。
ANDROID10：默认值，安卓10
ANDROID12：安卓12
ANDROID14：安卓14
        :type AndroidVersion: str
        :param _Zone: 镜像可用区
        :type Zone: str
        """
        self._Name = None
        self._URL = None
        self._MD5 = None
        self._AndroidVersion = None
        self._Zone = None

    @property
    def Name(self):
        r"""镜像名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def URL(self):
        r"""镜像文件下载地址，要求是 tgz 压缩文件
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def MD5(self):
        r"""镜像文件 MD5 值
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def AndroidVersion(self):
        r"""安卓版本。
ANDROID10：默认值，安卓10
ANDROID12：安卓12
ANDROID14：安卓14
        :rtype: str
        """
        return self._AndroidVersion

    @AndroidVersion.setter
    def AndroidVersion(self, AndroidVersion):
        self._AndroidVersion = AndroidVersion

    @property
    def Zone(self):
        r"""镜像可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._URL = params.get("URL")
        self._MD5 = params.get("MD5")
        self._AndroidVersion = params.get("AndroidVersion")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportAndroidInstanceImageResponse(AbstractModel):
    r"""ImportAndroidInstanceImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageId: 安卓实例镜像 ID
        :type AndroidInstanceImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceImageId = None
        self._RequestId = None

    @property
    def AndroidInstanceImageId(self):
        r"""安卓实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._RequestId = params.get("RequestId")


class InstallAndroidInstancesAppRequest(AbstractModel):
    r"""InstallAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        :param _AndroidAppId: 应用ID
        :type AndroidAppId: str
        :param _AndroidAppVersion: 应用版本
        :type AndroidAppVersion: str
        """
        self._AndroidInstanceIds = None
        self._AndroidAppId = None
        self._AndroidAppVersion = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidAppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def AndroidAppVersion(self):
        r"""应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._AndroidAppId = params.get("AndroidAppId")
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallAndroidInstancesAppResponse(AbstractModel):
    r"""InstallAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class InstallAndroidInstancesAppWithURLRequest(AbstractModel):
    r"""InstallAndroidInstancesAppWithURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        :param _AndroidAppURL: 安卓应用下载 URL
        :type AndroidAppURL: str
        """
        self._AndroidInstanceIds = None
        self._AndroidAppURL = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidAppURL(self):
        r"""安卓应用下载 URL
        :rtype: str
        """
        return self._AndroidAppURL

    @AndroidAppURL.setter
    def AndroidAppURL(self, AndroidAppURL):
        self._AndroidAppURL = AndroidAppURL


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._AndroidAppURL = params.get("AndroidAppURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallAndroidInstancesAppWithURLResponse(AbstractModel):
    r"""InstallAndroidInstancesAppWithURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class LabelRequirement(AbstractModel):
    r"""标签要求

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Operator: 运算符类型。
IN：要求对象的标签键 Key 对应的标签值需满足 Values 中的一个
NOT_IN：要求对象的标签键 Key 对应的标签值不满足 Values 中的任何一个
EXISTS：要求对象标签存在标签键 Key
NOT_EXISTS: 要求对象标签不存在标签键 Key
        :type Operator: str
        :param _Values: 标签值列表
        :type Values: list of str
        """
        self._Key = None
        self._Operator = None
        self._Values = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        r"""运算符类型。
IN：要求对象的标签键 Key 对应的标签值需满足 Values 中的一个
NOT_IN：要求对象的标签键 Key 对应的标签值不满足 Values 中的任何一个
EXISTS：要求对象标签存在标签键 Key
NOT_EXISTS: 要求对象标签不存在标签键 Key
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Values(self):
        r"""标签值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidAppRequest(AbstractModel):
    r"""ModifyAndroidApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 安卓应用 Id
        :type AndroidAppId: str
        :param _Name: 安卓应用名称
        :type Name: str
        :param _UserId: 用户 Id
        :type UserId: str
        """
        self._AndroidAppId = None
        self._Name = None
        self._UserId = None

    @property
    def AndroidAppId(self):
        r"""安卓应用 Id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def Name(self):
        r"""安卓应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserId(self):
        r"""用户 Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._Name = params.get("Name")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidAppResponse(AbstractModel):
    r"""ModifyAndroidApp返回参数结构体

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


class ModifyAndroidAppVersionRequest(AbstractModel):
    r"""ModifyAndroidAppVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidAppId: 安卓应用 Id
        :type AndroidAppId: str
        :param _AndroidAppVersion: 安卓应用版本 Id
        :type AndroidAppVersion: str
        :param _AndroidAppVersionName: 安卓应用版本名称
        :type AndroidAppVersionName: str
        :param _Command: 应用 shell 安装命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :type Command: str
        :param _UninstallCommand: 应用 shell 卸载命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :type UninstallCommand: str
        """
        self._AndroidAppId = None
        self._AndroidAppVersion = None
        self._AndroidAppVersionName = None
        self._Command = None
        self._UninstallCommand = None

    @property
    def AndroidAppId(self):
        r"""安卓应用 Id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def AndroidAppVersion(self):
        r"""安卓应用版本 Id
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion

    @property
    def AndroidAppVersionName(self):
        r"""安卓应用版本名称
        :rtype: str
        """
        return self._AndroidAppVersionName

    @AndroidAppVersionName.setter
    def AndroidAppVersionName(self, AndroidAppVersionName):
        self._AndroidAppVersionName = AndroidAppVersionName

    @property
    def Command(self):
        r"""应用 shell 安装命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def UninstallCommand(self):
        r"""应用 shell 卸载命令（支持多条命令执行，通过 && 组合；只在应用 AppMode 为 ADVANCED 高级模式下 才会生效）
        :rtype: str
        """
        return self._UninstallCommand

    @UninstallCommand.setter
    def UninstallCommand(self, UninstallCommand):
        self._UninstallCommand = UninstallCommand


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        self._AndroidAppVersionName = params.get("AndroidAppVersionName")
        self._Command = params.get("Command")
        self._UninstallCommand = params.get("UninstallCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidAppVersionResponse(AbstractModel):
    r"""ModifyAndroidAppVersion返回参数结构体

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


class ModifyAndroidInstanceInformationRequest(AbstractModel):
    r"""ModifyAndroidInstanceInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _Name: 实例名称
        :type Name: str
        """
        self._AndroidInstanceId = None
        self._Name = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Name(self):
        r"""实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstanceInformationResponse(AbstractModel):
    r"""ModifyAndroidInstanceInformation返回参数结构体

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


class ModifyAndroidInstanceResolutionRequest(AbstractModel):
    r"""ModifyAndroidInstanceResolution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _Width: 分辨率宽度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1080
实例类型为双开（A2） 及以上：建议设置为 720
        :type Width: int
        :param _Height: 分辨率高度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1920
实例类型为双开（A2） 及以上：建议设置为 1280
        :type Height: int
        :param _DPI: 每英寸像素点。如果不填，系统将会计算一个合理的数值。修改 DPI 可能会导致 App 异常退出，请谨慎使用！
分辨率为 720x1280：建议配置为 320
分辨率为  1080x1920：建议配置为 480
        :type DPI: int
        :param _FPS: 帧率。ResolutionType 为 PHYSICAL 时才会修改帧率。另外建议按照以下数值设置，避免出现性能不足问题： 实例类型为单开（A1）：建议设置为 60 实例类型为双开（A2） 及以上：建议设置为 30
        :type FPS: int
        :param _ResolutionType: 修改分辨率类型。修改物理分辨率，需要重启才能生效。
OVERRIDE：默认值，修改覆盖（显示）分辨率
PHYSICAL：修改物理分辨率
        :type ResolutionType: str
        """
        self._AndroidInstanceId = None
        self._Width = None
        self._Height = None
        self._DPI = None
        self._FPS = None
        self._ResolutionType = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Width(self):
        r"""分辨率宽度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1080
实例类型为双开（A2） 及以上：建议设置为 720
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""分辨率高度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1920
实例类型为双开（A2） 及以上：建议设置为 1280
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def DPI(self):
        r"""每英寸像素点。如果不填，系统将会计算一个合理的数值。修改 DPI 可能会导致 App 异常退出，请谨慎使用！
分辨率为 720x1280：建议配置为 320
分辨率为  1080x1920：建议配置为 480
        :rtype: int
        """
        return self._DPI

    @DPI.setter
    def DPI(self, DPI):
        self._DPI = DPI

    @property
    def FPS(self):
        r"""帧率。ResolutionType 为 PHYSICAL 时才会修改帧率。另外建议按照以下数值设置，避免出现性能不足问题： 实例类型为单开（A1）：建议设置为 60 实例类型为双开（A2） 及以上：建议设置为 30
        :rtype: int
        """
        return self._FPS

    @FPS.setter
    def FPS(self, FPS):
        self._FPS = FPS

    @property
    def ResolutionType(self):
        r"""修改分辨率类型。修改物理分辨率，需要重启才能生效。
OVERRIDE：默认值，修改覆盖（显示）分辨率
PHYSICAL：修改物理分辨率
        :rtype: str
        """
        return self._ResolutionType

    @ResolutionType.setter
    def ResolutionType(self, ResolutionType):
        self._ResolutionType = ResolutionType


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._DPI = params.get("DPI")
        self._FPS = params.get("FPS")
        self._ResolutionType = params.get("ResolutionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstanceResolutionResponse(AbstractModel):
    r"""ModifyAndroidInstanceResolution返回参数结构体

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


class ModifyAndroidInstancesAppBlacklistRequest(AbstractModel):
    r"""ModifyAndroidInstancesAppBlacklist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID列表，数量上限100
        :type AndroidInstanceIds: list of str
        :param _AppList: 应用列表
        :type AppList: list of str
        :param _Operation: ADD、REMOVE、CLEAR
        :type Operation: str
        """
        self._AndroidInstanceIds = None
        self._AppList = None
        self._Operation = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID列表，数量上限100
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AppList(self):
        r"""应用列表
        :rtype: list of str
        """
        return self._AppList

    @AppList.setter
    def AppList(self, AppList):
        self._AppList = AppList

    @property
    def Operation(self):
        r"""ADD、REMOVE、CLEAR
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._AppList = params.get("AppList")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesAppBlacklistResponse(AbstractModel):
    r"""ModifyAndroidInstancesAppBlacklist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstancesInformationRequest(AbstractModel):
    r"""ModifyAndroidInstancesInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceInformations: 安卓实例信息数据
        :type AndroidInstanceInformations: list of AndroidInstanceInformation
        """
        self._AndroidInstanceInformations = None

    @property
    def AndroidInstanceInformations(self):
        r"""安卓实例信息数据
        :rtype: list of AndroidInstanceInformation
        """
        return self._AndroidInstanceInformations

    @AndroidInstanceInformations.setter
    def AndroidInstanceInformations(self, AndroidInstanceInformations):
        self._AndroidInstanceInformations = AndroidInstanceInformations


    def _deserialize(self, params):
        if params.get("AndroidInstanceInformations") is not None:
            self._AndroidInstanceInformations = []
            for item in params.get("AndroidInstanceInformations"):
                obj = AndroidInstanceInformation()
                obj._deserialize(item)
                self._AndroidInstanceInformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesInformationResponse(AbstractModel):
    r"""ModifyAndroidInstancesInformation返回参数结构体

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


class ModifyAndroidInstancesLabelsRequest(AbstractModel):
    r"""ModifyAndroidInstancesLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _Operation: 操作类型。ADD：标签键不存在的添加新标签，标签键存在的将覆盖原有标签REMOVE：根据标签键删除标签REPLACE：使用请求标签列表替换原来所有标签CLEAR：清除所有标签
        :type Operation: str
        :param _AndroidInstanceLabels: 安卓实例标签列表
        :type AndroidInstanceLabels: list of AndroidInstanceLabel
        """
        self._AndroidInstanceIds = None
        self._Operation = None
        self._AndroidInstanceLabels = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Operation(self):
        r"""操作类型。ADD：标签键不存在的添加新标签，标签键存在的将覆盖原有标签REMOVE：根据标签键删除标签REPLACE：使用请求标签列表替换原来所有标签CLEAR：清除所有标签
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def AndroidInstanceLabels(self):
        r"""安卓实例标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._AndroidInstanceLabels

    @AndroidInstanceLabels.setter
    def AndroidInstanceLabels(self, AndroidInstanceLabels):
        self._AndroidInstanceLabels = AndroidInstanceLabels


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._Operation = params.get("Operation")
        if params.get("AndroidInstanceLabels") is not None:
            self._AndroidInstanceLabels = []
            for item in params.get("AndroidInstanceLabels"):
                obj = AndroidInstanceLabel()
                obj._deserialize(item)
                self._AndroidInstanceLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesLabelsResponse(AbstractModel):
    r"""ModifyAndroidInstancesLabels返回参数结构体

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


class ModifyAndroidInstancesPropertiesRequest(AbstractModel):
    r"""ModifyAndroidInstancesProperties请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _AndroidInstanceDevice: 安卓实例设备
        :type AndroidInstanceDevice: :class:`tencentcloud.gs.v20191118.models.AndroidInstanceDevice`
        :param _AndroidInstanceProperties: 安卓实例其它属性列表
        :type AndroidInstanceProperties: list of AndroidInstanceProperty
        """
        self._AndroidInstanceIds = None
        self._AndroidInstanceDevice = None
        self._AndroidInstanceProperties = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidInstanceDevice(self):
        r"""安卓实例设备
        :rtype: :class:`tencentcloud.gs.v20191118.models.AndroidInstanceDevice`
        """
        return self._AndroidInstanceDevice

    @AndroidInstanceDevice.setter
    def AndroidInstanceDevice(self, AndroidInstanceDevice):
        self._AndroidInstanceDevice = AndroidInstanceDevice

    @property
    def AndroidInstanceProperties(self):
        r"""安卓实例其它属性列表
        :rtype: list of AndroidInstanceProperty
        """
        return self._AndroidInstanceProperties

    @AndroidInstanceProperties.setter
    def AndroidInstanceProperties(self, AndroidInstanceProperties):
        self._AndroidInstanceProperties = AndroidInstanceProperties


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        if params.get("AndroidInstanceDevice") is not None:
            self._AndroidInstanceDevice = AndroidInstanceDevice()
            self._AndroidInstanceDevice._deserialize(params.get("AndroidInstanceDevice"))
        if params.get("AndroidInstanceProperties") is not None:
            self._AndroidInstanceProperties = []
            for item in params.get("AndroidInstanceProperties"):
                obj = AndroidInstanceProperty()
                obj._deserialize(item)
                self._AndroidInstanceProperties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesPropertiesResponse(AbstractModel):
    r"""ModifyAndroidInstancesProperties返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 安卓实例错误列表
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""安卓实例错误列表
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstancesResolutionRequest(AbstractModel):
    r"""ModifyAndroidInstancesResolution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _Width: 分辨率宽度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1080
实例类型为双开（A2） 及以上：建议设置为 720
        :type Width: int
        :param _Height: 分辨率高度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1920
实例类型为双开（A2） 及以上：建议设置为 1280
        :type Height: int
        :param _DPI: 每英寸像素点。
分辨率为 720x1280：建议配置为 320
分辨率为  1080x1920：建议配置为 480
        :type DPI: int
        :param _FPS: 帧率。ResolutionType 为 PHYSICAL 时才会修改帧率。另外建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 60
实例类型为双开（A2） 及以上：建议设置为 30
        :type FPS: int
        :param _ResolutionType: 修改分辨率类型。修改物理分辨率，需要重启才能生效。
OVERRIDE：默认值，修改覆盖（显示）分辨率
PHYSICAL：修改物理分辨率
        :type ResolutionType: str
        """
        self._AndroidInstanceIds = None
        self._Width = None
        self._Height = None
        self._DPI = None
        self._FPS = None
        self._ResolutionType = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Width(self):
        r"""分辨率宽度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1080
实例类型为双开（A2） 及以上：建议设置为 720
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""分辨率高度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 1920
实例类型为双开（A2） 及以上：建议设置为 1280
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def DPI(self):
        r"""每英寸像素点。
分辨率为 720x1280：建议配置为 320
分辨率为  1080x1920：建议配置为 480
        :rtype: int
        """
        return self._DPI

    @DPI.setter
    def DPI(self, DPI):
        self._DPI = DPI

    @property
    def FPS(self):
        r"""帧率。ResolutionType 为 PHYSICAL 时才会修改帧率。另外建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）：建议设置为 60
实例类型为双开（A2） 及以上：建议设置为 30
        :rtype: int
        """
        return self._FPS

    @FPS.setter
    def FPS(self, FPS):
        self._FPS = FPS

    @property
    def ResolutionType(self):
        r"""修改分辨率类型。修改物理分辨率，需要重启才能生效。
OVERRIDE：默认值，修改覆盖（显示）分辨率
PHYSICAL：修改物理分辨率
        :rtype: str
        """
        return self._ResolutionType

    @ResolutionType.setter
    def ResolutionType(self, ResolutionType):
        self._ResolutionType = ResolutionType


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._DPI = params.get("DPI")
        self._FPS = params.get("FPS")
        self._ResolutionType = params.get("ResolutionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesResolutionResponse(AbstractModel):
    r"""ModifyAndroidInstancesResolution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 安卓实例错误列表
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""安卓实例错误列表
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstancesResourcesRequest(AbstractModel):
    r"""ModifyAndroidInstancesResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表（最大100条数据）
        :type AndroidInstanceIds: list of str
        :param _MemoryQuota: 内存配额（单位 MB）
        :type MemoryQuota: int
        """
        self._AndroidInstanceIds = None
        self._MemoryQuota = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表（最大100条数据）
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def MemoryQuota(self):
        r"""内存配额（单位 MB）
        :rtype: int
        """
        return self._MemoryQuota

    @MemoryQuota.setter
    def MemoryQuota(self, MemoryQuota):
        self._MemoryQuota = MemoryQuota


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._MemoryQuota = params.get("MemoryQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesResourcesResponse(AbstractModel):
    r"""ModifyAndroidInstancesResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstancesUserIdRequest(AbstractModel):
    r"""ModifyAndroidInstancesUserId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _UserId: 用户 ID
        :type UserId: str
        """
        self._AndroidInstanceIds = None
        self._UserId = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

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
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesUserIdResponse(AbstractModel):
    r"""ModifyAndroidInstancesUserId返回参数结构体

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


class RebootAndroidInstanceHostsRequest(AbstractModel):
    r"""RebootAndroidInstanceHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostSerialNumbers: 宿主机序列号集合
        :type HostSerialNumbers: list of str
        """
        self._HostSerialNumbers = None

    @property
    def HostSerialNumbers(self):
        r"""宿主机序列号集合
        :rtype: list of str
        """
        return self._HostSerialNumbers

    @HostSerialNumbers.setter
    def HostSerialNumbers(self, HostSerialNumbers):
        self._HostSerialNumbers = HostSerialNumbers


    def _deserialize(self, params):
        self._HostSerialNumbers = params.get("HostSerialNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootAndroidInstanceHostsResponse(AbstractModel):
    r"""RebootAndroidInstanceHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务 ID 集合，以供任务状态查询，其中 InstanceId 为宿主机序列号
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务 ID 集合，以供任务状态查询，其中 InstanceId 为宿主机序列号
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class RebootAndroidInstancesRequest(AbstractModel):
    r"""RebootAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootAndroidInstancesResponse(AbstractModel):
    r"""RebootAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class RenewAndroidInstancesAccessTokenRequest(AbstractModel):
    r"""RenewAndroidInstancesAccessToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: token
        :type AccessToken: str
        :param _ExpirationDuration: 有效期，默认为 12 小时，最大为 24 小时。支持 s（秒）、m（分）、h（小时）等单位，比如 12h 表示 12 小时，1h2m3s 表示一小时两分三秒
        :type ExpirationDuration: str
        """
        self._AccessToken = None
        self._ExpirationDuration = None

    @property
    def AccessToken(self):
        r"""token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ExpirationDuration(self):
        r"""有效期，默认为 12 小时，最大为 24 小时。支持 s（秒）、m（分）、h（小时）等单位，比如 12h 表示 12 小时，1h2m3s 表示一小时两分三秒
        :rtype: str
        """
        return self._ExpirationDuration

    @ExpirationDuration.setter
    def ExpirationDuration(self, ExpirationDuration):
        self._ExpirationDuration = ExpirationDuration


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._ExpirationDuration = params.get("ExpirationDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewAndroidInstancesAccessTokenResponse(AbstractModel):
    r"""RenewAndroidInstancesAccessToken返回参数结构体

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


class ResetAndroidInstancesRequest(AbstractModel):
    r"""ResetAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID列表
        :type AndroidInstanceIds: list of str
        :param _AndroidInstanceImageId: 指定有效的镜像 ID。
默认取值：默认使用当前镜像。
        :type AndroidInstanceImageId: str
        :param _Mode: 重置模式。在 AndroidInstanceImageId 不为空时才生效。

CleanData：默认选项，清理系统属性和用户数据
KeepSystemProperties：只保留系统属性
KeepData: 保留系统属性和用户数据
        :type Mode: str
        """
        self._AndroidInstanceIds = None
        self._AndroidInstanceImageId = None
        self._Mode = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidInstanceImageId(self):
        r"""指定有效的镜像 ID。
默认取值：默认使用当前镜像。
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def Mode(self):
        r"""重置模式。在 AndroidInstanceImageId 不为空时才生效。

CleanData：默认选项，清理系统属性和用户数据
KeepSystemProperties：只保留系统属性
KeepData: 保留系统属性和用户数据
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAndroidInstancesResponse(AbstractModel):
    r"""ResetAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class RestartAndroidInstancesAppRequest(AbstractModel):
    r"""RestartAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _Activity: 启动页。建议指定启动页来启动应用，避免启动失败。如果启动页为空，系统尝试根据 PackageName 启动，但不保证成功。
        :type Activity: str
        """
        self._AndroidInstanceIds = None
        self._PackageName = None
        self._Activity = None

    @property
    def AndroidInstanceIds(self):
        r"""实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Activity(self):
        r"""启动页。建议指定启动页来启动应用，避免启动失败。如果启动页为空，系统尝试根据 PackageName 启动，但不保证成功。
        :rtype: str
        """
        return self._Activity

    @Activity.setter
    def Activity(self, Activity):
        self._Activity = Activity


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PackageName = params.get("PackageName")
        self._Activity = params.get("Activity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartAndroidInstancesAppResponse(AbstractModel):
    r"""RestartAndroidInstancesApp返回参数结构体

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


class RestoreAndroidInstanceFromStorageRequest(AbstractModel):
    r"""RestoreAndroidInstanceFromStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例ID
        :type AndroidInstanceId: str
        :param _ObjectKey: 自定义备份对象Key
        :type ObjectKey: str
        :param _StorageType: 存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :type StorageType: str
        :param _COSOptions: COS协议选项
        :type COSOptions: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        :param _S3Options: S3存储协议选项
        :type S3Options: :class:`tencentcloud.gs.v20191118.models.S3Options`
        """
        self._AndroidInstanceId = None
        self._ObjectKey = None
        self._StorageType = None
        self._COSOptions = None
        self._S3Options = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def ObjectKey(self):
        r"""自定义备份对象Key
        :rtype: str
        """
        return self._ObjectKey

    @ObjectKey.setter
    def ObjectKey(self, ObjectKey):
        self._ObjectKey = ObjectKey

    @property
    def StorageType(self):
        r"""存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def COSOptions(self):
        r"""COS协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        """
        return self._COSOptions

    @COSOptions.setter
    def COSOptions(self, COSOptions):
        self._COSOptions = COSOptions

    @property
    def S3Options(self):
        r"""S3存储协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.S3Options`
        """
        return self._S3Options

    @S3Options.setter
    def S3Options(self, S3Options):
        self._S3Options = S3Options


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._ObjectKey = params.get("ObjectKey")
        self._StorageType = params.get("StorageType")
        if params.get("COSOptions") is not None:
            self._COSOptions = COSOptions()
            self._COSOptions._deserialize(params.get("COSOptions"))
        if params.get("S3Options") is not None:
            self._S3Options = S3Options()
            self._S3Options._deserialize(params.get("S3Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreAndroidInstanceFromStorageResponse(AbstractModel):
    r"""RestoreAndroidInstanceFromStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 实例任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""实例任务 ID
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


class RestoreAndroidInstanceRequest(AbstractModel):
    r"""RestoreAndroidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _BackupId: 备份 ID
        :type BackupId: str
        """
        self._AndroidInstanceId = None
        self._BackupId = None

    @property
    def AndroidInstanceId(self):
        r"""安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def BackupId(self):
        r"""备份 ID
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreAndroidInstanceResponse(AbstractModel):
    r"""RestoreAndroidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 实例任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""实例任务 ID
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


class S3Options(AbstractModel):
    r"""S3协议参数

    """

    def __init__(self):
        r"""
        :param _EndPoint: 存储节点
        :type EndPoint: str
        :param _Bucket: 存储桶
        :type Bucket: str
        :param _AccessKeyId: 密钥 ID
        :type AccessKeyId: str
        :param _SecretAccessKey: 密钥 Key
        :type SecretAccessKey: str
        """
        self._EndPoint = None
        self._Bucket = None
        self._AccessKeyId = None
        self._SecretAccessKey = None

    @property
    def EndPoint(self):
        r"""存储节点
        :rtype: str
        """
        return self._EndPoint

    @EndPoint.setter
    def EndPoint(self, EndPoint):
        self._EndPoint = EndPoint

    @property
    def Bucket(self):
        r"""存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKeyId(self):
        r"""密钥 ID
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretAccessKey(self):
        r"""密钥 Key
        :rtype: str
        """
        return self._SecretAccessKey

    @SecretAccessKey.setter
    def SecretAccessKey(self, SecretAccessKey):
        self._SecretAccessKey = SecretAccessKey


    def _deserialize(self, params):
        self._EndPoint = params.get("EndPoint")
        self._Bucket = params.get("Bucket")
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretAccessKey = params.get("SecretAccessKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveGameArchiveRequest(AbstractModel):
    r"""SaveGameArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 游戏用户ID
        :type UserId: str
        :param _GameId: 游戏ID
        :type GameId: str
        """
        self._UserId = None
        self._GameId = None

    @property
    def UserId(self):
        r"""游戏用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        r"""游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveGameArchiveResponse(AbstractModel):
    r"""SaveGameArchive返回参数结构体

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


class SetAndroidInstancesBGAppKeepAliveRequest(AbstractModel):
    r"""SetAndroidInstancesBGAppKeepAlive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表（最大100条数据）
        :type AndroidInstanceIds: list of str
        :param _Operation: 操作类型，取值：ADD 添加应用到后台保活列表、REMOVE 从后台保活列表中移除应用、SET 全量设置后台保活列表，替换当前列表。
        :type Operation: str
        :param _PackageNames: 应用包名列表
        :type PackageNames: list of str
        """
        self._AndroidInstanceIds = None
        self._Operation = None
        self._PackageNames = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表（最大100条数据）
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Operation(self):
        r"""操作类型，取值：ADD 添加应用到后台保活列表、REMOVE 从后台保活列表中移除应用、SET 全量设置后台保活列表，替换当前列表。
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PackageNames(self):
        r"""应用包名列表
        :rtype: list of str
        """
        return self._PackageNames

    @PackageNames.setter
    def PackageNames(self, PackageNames):
        self._PackageNames = PackageNames


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._Operation = params.get("Operation")
        self._PackageNames = params.get("PackageNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAndroidInstancesBGAppKeepAliveResponse(AbstractModel):
    r"""SetAndroidInstancesBGAppKeepAlive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class SetAndroidInstancesFGAppKeepAliveRequest(AbstractModel):
    r"""SetAndroidInstancesFGAppKeepAlive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表（最大100条数据）
        :type AndroidInstanceIds: list of str
        :param _Operation: 操作类型，取值：ENABLE 开启保活、DISABLE 关闭保活。当关闭保活时，PackageName 参数传空即可
        :type Operation: str
        :param _PackageName: 应用包名，开启保活时，必须传入 PackageName
        :type PackageName: str
        """
        self._AndroidInstanceIds = None
        self._Operation = None
        self._PackageName = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表（最大100条数据）
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Operation(self):
        r"""操作类型，取值：ENABLE 开启保活、DISABLE 关闭保活。当关闭保活时，PackageName 参数传空即可
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PackageName(self):
        r"""应用包名，开启保活时，必须传入 PackageName
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._Operation = params.get("Operation")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAndroidInstancesFGAppKeepAliveResponse(AbstractModel):
    r"""SetAndroidInstancesFGAppKeepAlive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceErrors: 错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :type AndroidInstanceErrors: list of AndroidInstanceError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AndroidInstanceErrors = None
        self._RequestId = None

    @property
    def AndroidInstanceErrors(self):
        r"""错误列表。如果实例操作都成功，则响应没有这个字段；如果有实例操作失败，该字段包含了实例操作的错误信息
        :rtype: list of AndroidInstanceError
        """
        return self._AndroidInstanceErrors

    @AndroidInstanceErrors.setter
    def AndroidInstanceErrors(self, AndroidInstanceErrors):
        self._AndroidInstanceErrors = AndroidInstanceErrors

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AndroidInstanceErrors") is not None:
            self._AndroidInstanceErrors = []
            for item in params.get("AndroidInstanceErrors"):
                obj = AndroidInstanceError()
                obj._deserialize(item)
                self._AndroidInstanceErrors.append(obj)
        self._RequestId = params.get("RequestId")


class StartAndroidInstancesAppRequest(AbstractModel):
    r"""StartAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _Activity: 启动页。建议指定启动页来启动应用，避免启动失败。如果启动页为空，系统尝试根据 PackageName 启动，但不保证成功。
        :type Activity: str
        """
        self._AndroidInstanceIds = None
        self._PackageName = None
        self._Activity = None

    @property
    def AndroidInstanceIds(self):
        r"""实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Activity(self):
        r"""启动页。建议指定启动页来启动应用，避免启动失败。如果启动页为空，系统尝试根据 PackageName 启动，但不保证成功。
        :rtype: str
        """
        return self._Activity

    @Activity.setter
    def Activity(self, Activity):
        self._Activity = Activity


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PackageName = params.get("PackageName")
        self._Activity = params.get("Activity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAndroidInstancesAppResponse(AbstractModel):
    r"""StartAndroidInstancesApp返回参数结构体

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


class StartAndroidInstancesRequest(AbstractModel):
    r"""StartAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAndroidInstancesResponse(AbstractModel):
    r"""StartAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class StartPublishStreamRequest(AbstractModel):
    r"""StartPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _PublishUrl: 推流地址，仅支持rtmp协议
        :type PublishUrl: str
        """
        self._UserId = None
        self._PublishUrl = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishUrl(self):
        r"""推流地址，仅支持rtmp协议
        :rtype: str
        """
        return self._PublishUrl

    @PublishUrl.setter
    def PublishUrl(self, PublishUrl):
        self._PublishUrl = PublishUrl


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishUrl = params.get("PublishUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamResponse(AbstractModel):
    r"""StartPublishStream返回参数结构体

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


class StartPublishStreamToCSSRequest(AbstractModel):
    r"""StartPublishStreamToCSS请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _PublishStreamArgs: 推流参数，推流时携带自定义参数。
        :type PublishStreamArgs: str
        """
        self._UserId = None
        self._PublishStreamArgs = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamArgs(self):
        r"""推流参数，推流时携带自定义参数。
        :rtype: str
        """
        return self._PublishStreamArgs

    @PublishStreamArgs.setter
    def PublishStreamArgs(self, PublishStreamArgs):
        self._PublishStreamArgs = PublishStreamArgs


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishStreamArgs = params.get("PublishStreamArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamToCSSResponse(AbstractModel):
    r"""StartPublishStreamToCSS返回参数结构体

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


class StopAndroidInstancesAppRequest(AbstractModel):
    r"""StopAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _PackageName: 应用包名
        :type PackageName: str
        """
        self._AndroidInstanceIds = None
        self._PackageName = None

    @property
    def AndroidInstanceIds(self):
        r"""实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        r"""应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAndroidInstancesAppResponse(AbstractModel):
    r"""StopAndroidInstancesApp返回参数结构体

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


class StopAndroidInstancesRequest(AbstractModel):
    r"""StopAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAndroidInstancesResponse(AbstractModel):
    r"""StopAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    r"""StopGame请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _HostUserId: 【多人游戏】游戏主机用户ID
        :type HostUserId: str
        """
        self._UserId = None
        self._HostUserId = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def HostUserId(self):
        r"""【多人游戏】游戏主机用户ID
        :rtype: str
        """
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._HostUserId = params.get("HostUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameResponse(AbstractModel):
    r"""StopGame返回参数结构体

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


class StopPublishStreamRequest(AbstractModel):
    r"""StopPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
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
        


class StopPublishStreamResponse(AbstractModel):
    r"""StopPublishStream返回参数结构体

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


class SwitchGameArchiveRequest(AbstractModel):
    r"""SwitchGameArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 游戏用户ID
        :type UserId: str
        :param _GameId: 游戏ID
        :type GameId: str
        :param _GameArchiveUrl: 游戏存档Url
        :type GameArchiveUrl: str
        :param _GameContext: 游戏相关参数
        :type GameContext: str
        """
        self._UserId = None
        self._GameId = None
        self._GameArchiveUrl = None
        self._GameContext = None

    @property
    def UserId(self):
        r"""游戏用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        r"""游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameArchiveUrl(self):
        r"""游戏存档Url
        :rtype: str
        """
        return self._GameArchiveUrl

    @GameArchiveUrl.setter
    def GameArchiveUrl(self, GameArchiveUrl):
        self._GameArchiveUrl = GameArchiveUrl

    @property
    def GameContext(self):
        r"""游戏相关参数
        :rtype: str
        """
        return self._GameContext

    @GameContext.setter
    def GameContext(self, GameContext):
        self._GameContext = GameContext


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        self._GameArchiveUrl = params.get("GameArchiveUrl")
        self._GameContext = params.get("GameContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchGameArchiveResponse(AbstractModel):
    r"""SwitchGameArchive返回参数结构体

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


class SyncAndroidInstanceImage(AbstractModel):
    r"""同步安卓实例镜像信息

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageId: 镜像 ID
        :type AndroidInstanceImageId: str
        :param _AndroidInstanceImageZone: 镜像可用区
        :type AndroidInstanceImageZone: str
        """
        self._AndroidInstanceImageId = None
        self._AndroidInstanceImageZone = None

    @property
    def AndroidInstanceImageId(self):
        r"""镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def AndroidInstanceImageZone(self):
        r"""镜像可用区
        :rtype: str
        """
        return self._AndroidInstanceImageZone

    @AndroidInstanceImageZone.setter
    def AndroidInstanceImageZone(self, AndroidInstanceImageZone):
        self._AndroidInstanceImageZone = AndroidInstanceImageZone


    def _deserialize(self, params):
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._AndroidInstanceImageZone = params.get("AndroidInstanceImageZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncAndroidInstanceImageRequest(AbstractModel):
    r"""SyncAndroidInstanceImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageId: 安卓实例镜像 ID
        :type AndroidInstanceImageId: str
        :param _DestinationZones: 目的同步可用区列表
        :type DestinationZones: list of str
        """
        self._AndroidInstanceImageId = None
        self._DestinationZones = None

    @property
    def AndroidInstanceImageId(self):
        r"""安卓实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def DestinationZones(self):
        r"""目的同步可用区列表
        :rtype: list of str
        """
        return self._DestinationZones

    @DestinationZones.setter
    def DestinationZones(self, DestinationZones):
        self._DestinationZones = DestinationZones


    def _deserialize(self, params):
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._DestinationZones = params.get("DestinationZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncAndroidInstanceImageResponse(AbstractModel):
    r"""SyncAndroidInstanceImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncAndroidInstanceImages: 同步安卓实例镜像列表
        :type SyncAndroidInstanceImages: list of SyncAndroidInstanceImage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SyncAndroidInstanceImages = None
        self._RequestId = None

    @property
    def SyncAndroidInstanceImages(self):
        r"""同步安卓实例镜像列表
        :rtype: list of SyncAndroidInstanceImage
        """
        return self._SyncAndroidInstanceImages

    @SyncAndroidInstanceImages.setter
    def SyncAndroidInstanceImages(self, SyncAndroidInstanceImages):
        self._SyncAndroidInstanceImages = SyncAndroidInstanceImages

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SyncAndroidInstanceImages") is not None:
            self._SyncAndroidInstanceImages = []
            for item in params.get("SyncAndroidInstanceImages"):
                obj = SyncAndroidInstanceImage()
                obj._deserialize(item)
                self._SyncAndroidInstanceImages.append(obj)
        self._RequestId = params.get("RequestId")


class SyncExecuteCommandOnAndroidInstancesRequest(AbstractModel):
    r"""SyncExecuteCommandOnAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _Command: shell 命令，必须是1秒内能自动结束的命令
        :type Command: str
        """
        self._AndroidInstanceIds = None
        self._Command = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Command(self):
        r"""shell 命令，必须是1秒内能自动结束的命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncExecuteCommandOnAndroidInstancesResponse(AbstractModel):
    r"""SyncExecuteCommandOnAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandResults: 命令执行结果列表
        :type CommandResults: list of SyncExecuteCommandResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CommandResults = None
        self._RequestId = None

    @property
    def CommandResults(self):
        r"""命令执行结果列表
        :rtype: list of SyncExecuteCommandResult
        """
        return self._CommandResults

    @CommandResults.setter
    def CommandResults(self, CommandResults):
        self._CommandResults = CommandResults

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CommandResults") is not None:
            self._CommandResults = []
            for item in params.get("CommandResults"):
                obj = SyncExecuteCommandResult()
                obj._deserialize(item)
                self._CommandResults.append(obj)
        self._RequestId = params.get("RequestId")


class SyncExecuteCommandResult(AbstractModel):
    r"""同步执行命令结果

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Output: 命令执行输出内容
        :type Output: str
        :param _Status: 命令执行结果
        :type Status: str
        """
        self._InstanceId = None
        self._Output = None
        self._Status = None

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
    def Output(self):
        r"""命令执行输出内容
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Status(self):
        r"""命令执行结果
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Output = params.get("Output")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrylockWorkerRequest(AbstractModel):
    r"""TrylockWorker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _GameId: 游戏ID
        :type GameId: str
        :param _GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等，如果不为空，优先按照该区域进行调度分配机器
        :type GameRegion: str
        :param _SetNo: 【废弃】资源池编号
        :type SetNo: int
        :param _UserIp: 【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :type UserIp: str
        :param _GroupId: 分组ID
        :type GroupId: str
        """
        self._UserId = None
        self._GameId = None
        self._GameRegion = None
        self._SetNo = None
        self._UserIp = None
        self._GroupId = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        r"""游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameRegion(self):
        r"""游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等，如果不为空，优先按照该区域进行调度分配机器
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def SetNo(self):
        r"""【废弃】资源池编号
        :rtype: int
        """
        return self._SetNo

    @SetNo.setter
    def SetNo(self, SetNo):
        self._SetNo = SetNo

    @property
    def UserIp(self):
        r"""【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def GroupId(self):
        r"""分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        self._GameRegion = params.get("GameRegion")
        self._SetNo = params.get("SetNo")
        self._UserIp = params.get("UserIp")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrylockWorkerResponse(AbstractModel):
    r"""TrylockWorker返回参数结构体

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


class UninstallAndroidInstancesAppRequest(AbstractModel):
    r"""UninstallAndroidInstancesApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        :param _AndroidAppId: 应用ID
        :type AndroidAppId: str
        :param _PackageName: 包名
        :type PackageName: str
        """
        self._AndroidInstanceIds = None
        self._AndroidAppId = None
        self._PackageName = None

    @property
    def AndroidInstanceIds(self):
        r"""实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidAppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def PackageName(self):
        r"""包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._AndroidAppId = params.get("AndroidAppId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallAndroidInstancesAppResponse(AbstractModel):
    r"""UninstallAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class UploadFileToAndroidInstancesRequest(AbstractModel):
    r"""UploadFileToAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _FileURL: 文件下载 URL
        :type FileURL: str
        :param _DestinationDirectory: 上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :type DestinationDirectory: str
        :param _DestinationFileName: 目标文件名
        :type DestinationFileName: str
        """
        self._AndroidInstanceIds = None
        self._FileURL = None
        self._DestinationDirectory = None
        self._DestinationFileName = None

    @property
    def AndroidInstanceIds(self):
        r"""安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

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
    def DestinationDirectory(self):
        r"""上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :rtype: str
        """
        return self._DestinationDirectory

    @DestinationDirectory.setter
    def DestinationDirectory(self, DestinationDirectory):
        self._DestinationDirectory = DestinationDirectory

    @property
    def DestinationFileName(self):
        r"""目标文件名
        :rtype: str
        """
        return self._DestinationFileName

    @DestinationFileName.setter
    def DestinationFileName(self, DestinationFileName):
        self._DestinationFileName = DestinationFileName


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._FileURL = params.get("FileURL")
        self._DestinationDirectory = params.get("DestinationDirectory")
        self._DestinationFileName = params.get("DestinationFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileToAndroidInstancesResponse(AbstractModel):
    r"""UploadFileToAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 实例任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""实例任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class UploadFilesToAndroidInstancesRequest(AbstractModel):
    r"""UploadFilesToAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Files: 上传文件信息列表
        :type Files: list of AndroidInstanceUploadFile
        """
        self._Files = None

    @property
    def Files(self):
        r"""上传文件信息列表
        :rtype: list of AndroidInstanceUploadFile
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = AndroidInstanceUploadFile()
                obj._deserialize(item)
                self._Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesToAndroidInstancesResponse(AbstractModel):
    r"""UploadFilesToAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 实例任务集合
        :type TaskSet: list of AndroidInstanceTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        r"""实例任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = AndroidInstanceTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")