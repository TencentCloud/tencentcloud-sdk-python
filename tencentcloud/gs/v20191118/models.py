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


class AndroidApp(AbstractModel):
    """安卓应用

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
        """
        self._AndroidAppId = None
        self._Name = None
        self._State = None
        self._AndroidAppVersionInfo = None
        self._CreateTime = None
        self._UserId = None

    @property
    def AndroidAppId(self):
        """安卓应用 Id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def Name(self):
        """安卓应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def State(self):
        """安卓应用状态（上架、下架）
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AndroidAppVersionInfo(self):
        """安卓应用版本列表
        :rtype: list of AndroidAppVersionInfo
        """
        return self._AndroidAppVersionInfo

    @AndroidAppVersionInfo.setter
    def AndroidAppVersionInfo(self, AndroidAppVersionInfo):
        self._AndroidAppVersionInfo = AndroidAppVersionInfo

    @property
    def CreateTime(self):
        """安卓应用创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserId(self):
        """用户 Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidAppVersionInfo(AbstractModel):
    """安卓应用版本信息

    """

    def __init__(self):
        r"""
        :param _AndroidAppVersion: 安卓应用版本
        :type AndroidAppVersion: str
        :param _State: 安卓应用版本创建状态（NORMAL：无、UPLOADING：上传中、
CREATING： 创建中、
CREATE_FAIL：创建失败、CREATE_SUCCESS：创建成功）
        :type State: str
        :param _CreateTime: 安卓应用版本创建时间
        :type CreateTime: str
        """
        self._AndroidAppVersion = None
        self._State = None
        self._CreateTime = None

    @property
    def AndroidAppVersion(self):
        """安卓应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion

    @property
    def State(self):
        """安卓应用版本创建状态（NORMAL：无、UPLOADING：上传中、
CREATING： 创建中、
CREATE_FAIL：创建失败、CREATE_SUCCESS：创建成功）
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        """安卓应用版本创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstance(AbstractModel):
    """安卓实例信息

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

    @property
    def AndroidInstanceId(self):
        """实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def AndroidInstanceRegion(self):
        """实例所在区域
        :rtype: str
        """
        return self._AndroidInstanceRegion

    @AndroidInstanceRegion.setter
    def AndroidInstanceRegion(self, AndroidInstanceRegion):
        self._AndroidInstanceRegion = AndroidInstanceRegion

    @property
    def AndroidInstanceZone(self):
        """实例可用区
        :rtype: str
        """
        return self._AndroidInstanceZone

    @AndroidInstanceZone.setter
    def AndroidInstanceZone(self, AndroidInstanceZone):
        self._AndroidInstanceZone = AndroidInstanceZone

    @property
    def State(self):
        """实例状态：INITIALIZING，NORMAL，PROCESSING
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AndroidInstanceType(self):
        """实例规格
        :rtype: str
        """
        return self._AndroidInstanceType

    @AndroidInstanceType.setter
    def AndroidInstanceType(self, AndroidInstanceType):
        self._AndroidInstanceType = AndroidInstanceType

    @property
    def AndroidInstanceImageId(self):
        """实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def Width(self):
        """分辨率宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """分辨率高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def HostSerialNumber(self):
        """宿主机 ID
        :rtype: str
        """
        return self._HostSerialNumber

    @HostSerialNumber.setter
    def HostSerialNumber(self, HostSerialNumber):
        self._HostSerialNumber = HostSerialNumber

    @property
    def AndroidInstanceGroupId(self):
        """分组 ID
        :rtype: str
        """
        return self._AndroidInstanceGroupId

    @AndroidInstanceGroupId.setter
    def AndroidInstanceGroupId(self, AndroidInstanceGroupId):
        self._AndroidInstanceGroupId = AndroidInstanceGroupId

    @property
    def AndroidInstanceLabels(self):
        """标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._AndroidInstanceLabels

    @AndroidInstanceLabels.setter
    def AndroidInstanceLabels(self, AndroidInstanceLabels):
        self._AndroidInstanceLabels = AndroidInstanceLabels

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PrivateIP(self):
        """内网 IP
        :rtype: str
        """
        return self._PrivateIP

    @PrivateIP.setter
    def PrivateIP(self, PrivateIP):
        self._PrivateIP = PrivateIP


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceAppInfo(AbstractModel):
    """安卓实例应用信息

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
        """
        self._AndroidAppId = None
        self._Name = None
        self._AndroidAppVersion = None
        self._PackageName = None
        self._PackageVersion = None
        self._PackageLabel = None

    @property
    def AndroidAppId(self):
        """应用id
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def Name(self):
        """应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AndroidAppVersion(self):
        """应用版本
        :rtype: str
        """
        return self._AndroidAppVersion

    @AndroidAppVersion.setter
    def AndroidAppVersion(self, AndroidAppVersion):
        self._AndroidAppVersion = AndroidAppVersion

    @property
    def PackageName(self):
        """应用包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        """应用包版本
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def PackageLabel(self):
        """应用包标签
        :rtype: str
        """
        return self._PackageLabel

    @PackageLabel.setter
    def PackageLabel(self, PackageLabel):
        self._PackageLabel = PackageLabel


    def _deserialize(self, params):
        self._AndroidAppId = params.get("AndroidAppId")
        self._Name = params.get("Name")
        self._AndroidAppVersion = params.get("AndroidAppVersion")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._PackageLabel = params.get("PackageLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceImage(AbstractModel):
    """安卓实例镜像信息

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
        """
        self._AndroidInstanceImageId = None
        self._AndroidInstanceImageName = None
        self._AndroidInstanceImageState = None
        self._AndroidInstanceImageZone = None

    @property
    def AndroidInstanceImageId(self):
        """镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def AndroidInstanceImageName(self):
        """镜像名称，由业务方自定义，仅用于展示
        :rtype: str
        """
        return self._AndroidInstanceImageName

    @AndroidInstanceImageName.setter
    def AndroidInstanceImageName(self, AndroidInstanceImageName):
        self._AndroidInstanceImageName = AndroidInstanceImageName

    @property
    def AndroidInstanceImageState(self):
        """镜像状态
        :rtype: str
        """
        return self._AndroidInstanceImageState

    @AndroidInstanceImageState.setter
    def AndroidInstanceImageState(self, AndroidInstanceImageState):
        self._AndroidInstanceImageState = AndroidInstanceImageState

    @property
    def AndroidInstanceImageZone(self):
        """镜像可用区
        :rtype: str
        """
        return self._AndroidInstanceImageZone

    @AndroidInstanceImageZone.setter
    def AndroidInstanceImageZone(self, AndroidInstanceImageZone):
        self._AndroidInstanceImageZone = AndroidInstanceImageZone


    def _deserialize(self, params):
        self._AndroidInstanceImageId = params.get("AndroidInstanceImageId")
        self._AndroidInstanceImageName = params.get("AndroidInstanceImageName")
        self._AndroidInstanceImageState = params.get("AndroidInstanceImageState")
        self._AndroidInstanceImageZone = params.get("AndroidInstanceImageZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidInstanceLabel(AbstractModel):
    """安卓实例标签

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
        """标签键
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
        


class AndroidInstanceTask(AbstractModel):
    """安卓实例任务信息

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
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def AndroidInstanceId(self):
        """实例ID
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
    """安卓实例任务状态信息

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
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """任务状态：SUCCESS，FAILED，PROCESSING，PENDING,CANCELED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AndroidInstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def TaskResult(self):
        """任务执行结果描述，针对某些任务，可以是可解析的 json
        :rtype: str
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def TaskType(self):
        """任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CompleteTime(self):
        """任务完成时间
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
        


class BackUpAndroidInstanceToStorageRequest(AbstractModel):
    """BackUpAndroidInstanceToStorage请求参数结构体

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
        """安卓实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def StorageType(self):
        """存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def ObjectKey(self):
        """自定义对象Key
        :rtype: str
        """
        return self._ObjectKey

    @ObjectKey.setter
    def ObjectKey(self, ObjectKey):
        self._ObjectKey = ObjectKey

    @property
    def Includes(self):
        """包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def Excludes(self):
        """需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Excludes

    @Excludes.setter
    def Excludes(self, Excludes):
        self._Excludes = Excludes

    @property
    def COSOptions(self):
        """COS协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        """
        return self._COSOptions

    @COSOptions.setter
    def COSOptions(self, COSOptions):
        self._COSOptions = COSOptions

    @property
    def S3Options(self):
        """S3存储协议选项
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
    """BackUpAndroidInstanceToStorage返回参数结构体

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
        """实例任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """COS协议参数

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
        """存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """存储区域
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
        


class ConnectAndroidInstanceRequest(AbstractModel):
    """ConnectAndroidInstance请求参数结构体

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
        """用户Session信息
        :rtype: str
        """
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def AndroidInstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def UserIp(self):
        """用户IP，用户客户端的公网IP，用于选择最佳网络链路
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
    """ConnectAndroidInstance返回参数结构体

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
        """服务端session信息
        :rtype: str
        """
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """CopyAndroidInstance请求参数结构体

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
        """源安卓实例 ID
        :rtype: str
        """
        return self._SourceAndroidInstanceId

    @SourceAndroidInstanceId.setter
    def SourceAndroidInstanceId(self, SourceAndroidInstanceId):
        self._SourceAndroidInstanceId = SourceAndroidInstanceId

    @property
    def TargetAndroidInstanceId(self):
        """目的安卓实例 ID
        :rtype: str
        """
        return self._TargetAndroidInstanceId

    @TargetAndroidInstanceId.setter
    def TargetAndroidInstanceId(self, TargetAndroidInstanceId):
        self._TargetAndroidInstanceId = TargetAndroidInstanceId

    @property
    def Includes(self):
        """包含的路径，支持仅含一个通配符*，通配符不能出现在路径开始
        :rtype: list of str
        """
        return self._Includes

    @Includes.setter
    def Includes(self, Includes):
        self._Includes = Includes

    @property
    def Excludes(self):
        """需要排除路径，支持仅含一个通配符*，通配符不能出现在路径开始
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
    """CopyAndroidInstance返回参数结构体

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
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateAndroidInstanceImageRequest(AbstractModel):
    """CreateAndroidInstanceImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageName: 安卓实例镜像名称
        :type AndroidInstanceImageName: str
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceImageName = None
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceImageName(self):
        """安卓实例镜像名称
        :rtype: str
        """
        return self._AndroidInstanceImageName

    @AndroidInstanceImageName.setter
    def AndroidInstanceImageName(self, AndroidInstanceImageName):
        self._AndroidInstanceImageName = AndroidInstanceImageName

    @property
    def AndroidInstanceId(self):
        """安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId


    def _deserialize(self, params):
        self._AndroidInstanceImageName = params.get("AndroidInstanceImageName")
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstanceImageResponse(AbstractModel):
    """CreateAndroidInstanceImage返回参数结构体

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
        """安卓实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """CreateAndroidInstanceLabel请求参数结构体

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
        """标签键
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
        


class CreateAndroidInstanceLabelResponse(AbstractModel):
    """CreateAndroidInstanceLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateAndroidInstanceSSHRequest(AbstractModel):
    """CreateAndroidInstanceSSH请求参数结构体

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
        """实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def ExpiredTime(self):
        """连接过期时间，最长可设置7天
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
    """CreateAndroidInstanceSSH返回参数结构体

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
        """连接私钥，需要保存为文件形式，例如 private_key.pem
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def UserName(self):
        """用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def HostName(self):
        """连接地址
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Port(self):
        """连接端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ConnectCommand(self):
        """连接参考命令
        :rtype: str
        """
        return self._ConnectCommand

    @ConnectCommand.setter
    def ConnectCommand(self, ConnectCommand):
        self._ConnectCommand = ConnectCommand

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """CreateAndroidInstanceWebShell请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例 ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceId(self):
        """实例 ID
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
    """CreateAndroidInstanceWebShell返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 鉴权密钥
        :type Key: str
        :param _Address: 连接地址
        :type Address: str
        :param _Zone: 连接区域
        :type Zone: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Key = None
        self._Address = None
        self._Zone = None
        self._RequestId = None

    @property
    def Key(self):
        """鉴权密钥
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Address(self):
        """连接地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Zone(self):
        """连接区域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = params.get("RequestId")


class CreateAndroidInstancesRequest(AbstractModel):
    """CreateAndroidInstances请求参数结构体

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
        """
        self._Zone = None
        self._Type = None
        self._Number = None
        self._HostSerialNumbers = None
        self._ImageId = None

    @property
    def Zone(self):
        """安卓实例可用区。
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
        """安卓实例类型。
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
        """当 HostSerialNumbers 不为空时，该参数表示每个宿主机要创建的安卓实例数量；
当 HostSerialNumbers 为空时，该参数表示要创建安卓实例的总数量，最大值为 100。
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def HostSerialNumbers(self):
        """宿主机 ID 列表。可以指定宿主机 ID 进行创建；也可以不指定由系统自动分配宿主机。
        :rtype: list of str
        """
        return self._HostSerialNumbers

    @HostSerialNumbers.setter
    def HostSerialNumbers(self, HostSerialNumbers):
        self._HostSerialNumbers = HostSerialNumbers

    @property
    def ImageId(self):
        """镜像 ID。如果不填，将使用默认的系统镜像
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        self._Number = params.get("Number")
        self._HostSerialNumbers = params.get("HostSerialNumbers")
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndroidInstancesResponse(AbstractModel):
    """CreateAndroidInstances返回参数结构体

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
        """安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """CreateAndroidInstancesScreenshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例 ID 列表
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        """实例 ID 列表
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
    """CreateAndroidInstancesScreenshot返回参数结构体

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
        """任务列表
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateSessionRequest(AbstractModel):
    """CreateSession请求参数结构体

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
        """唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        """【已废弃】只在TrylockWorker时生效
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameRegion(self):
        """【已废弃】只在TrylockWorker时生效
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def GameParas(self):
        """游戏参数
        :rtype: str
        """
        return self._GameParas

    @GameParas.setter
    def GameParas(self, GameParas):
        self._GameParas = GameParas

    @property
    def ClientSession(self):
        """客户端session信息，从JSSDK请求中获得。特殊的，当 RunMode 参数为 RunWithoutClient 时，该字段可以为空
        :rtype: str
        """
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def Resolution(self):
        """分辨率,，可设置为1080p或720p或1920x1080格式
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def ImageUrl(self):
        """背景图url，格式为png或jpeg，宽高1920*1080
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def SetNo(self):
        """【已废弃】
        :rtype: int
        """
        return self._SetNo

    @SetNo.setter
    def SetNo(self, SetNo):
        self._SetNo = SetNo

    @property
    def Bitrate(self):
        """【已废弃】
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def MaxBitrate(self):
        """单位Mbps，动态调整最大码率建议值，会按实际情况调整
        :rtype: int
        """
        return self._MaxBitrate

    @MaxBitrate.setter
    def MaxBitrate(self, MaxBitrate):
        self._MaxBitrate = MaxBitrate

    @property
    def MinBitrate(self):
        """单位Mbps，动态调整最小码率建议值，会按实际情况调整
        :rtype: int
        """
        return self._MinBitrate

    @MinBitrate.setter
    def MinBitrate(self, MinBitrate):
        self._MinBitrate = MinBitrate

    @property
    def Fps(self):
        """帧率，可设置为30、45、60、90、120、144
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def UserIp(self):
        """【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Optimization(self):
        """【已废弃】优化项，便于客户灰度开启新的优化项，默认为0
        :rtype: int
        """
        return self._Optimization

    @Optimization.setter
    def Optimization(self, Optimization):
        self._Optimization = Optimization

    @property
    def HostUserId(self):
        """【互动云游】游戏主机用户ID
        :rtype: str
        """
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId

    @property
    def Role(self):
        """【互动云游】角色；Player表示玩家；Viewer表示观察者
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def GameContext(self):
        """游戏相关参数
        :rtype: str
        """
        return self._GameContext

    @GameContext.setter
    def GameContext(self, GameContext):
        self._GameContext = GameContext

    @property
    def RunMode(self):
        """云端运行模式。
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
    """CreateSession返回参数结构体

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
        """服务端session信息，返回给JSSDK
        :rtype: str
        """
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RoleNumber(self):
        """【已废弃】
        :rtype: str
        """
        return self._RoleNumber

    @RoleNumber.setter
    def RoleNumber(self, RoleNumber):
        self._RoleNumber = RoleNumber

    @property
    def Role(self):
        """【互动云游】角色；Player表示玩家；Viewer表示观察者
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteAndroidInstanceImagesRequest(AbstractModel):
    """DeleteAndroidInstanceImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageIds: 镜像 ID 列表
        :type AndroidInstanceImageIds: list of str
        """
        self._AndroidInstanceImageIds = None

    @property
    def AndroidInstanceImageIds(self):
        """镜像 ID 列表
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
    """DeleteAndroidInstanceImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAndroidInstanceLabelRequest(AbstractModel):
    """DeleteAndroidInstanceLabel请求参数结构体

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
        """标签键
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
        


class DeleteAndroidInstanceLabelResponse(AbstractModel):
    """DeleteAndroidInstanceLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAndroidAppsRequest(AbstractModel):
    """DescribeAndroidApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        :param _AndroidAppIds: 应用ID数组
        :type AndroidAppIds: list of str
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._AndroidAppIds = None
        self._Filters = None

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
        """每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AndroidAppIds(self):
        """应用ID数组
        :rtype: list of str
        """
        return self._AndroidAppIds

    @AndroidAppIds.setter
    def AndroidAppIds(self, AndroidAppIds):
        self._AndroidAppIds = AndroidAppIds

    @property
    def Filters(self):
        """过滤条件
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
    """DescribeAndroidApps返回参数结构体

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
        """安卓应用列表
        :rtype: list of AndroidApp
        """
        return self._Apps

    @Apps.setter
    def Apps(self, Apps):
        self._Apps = Apps

    @property
    def TotalCount(self):
        """安卓应用列表长度
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """DescribeAndroidInstanceApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 实例ID
        :type AndroidInstanceId: str
        """
        self._AndroidInstanceId = None

    @property
    def AndroidInstanceId(self):
        """实例ID
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
    """DescribeAndroidInstanceApps返回参数结构体

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
        """安卓应用列表
        :rtype: list of AndroidInstanceAppInfo
        """
        return self._Apps

    @Apps.setter
    def Apps(self, Apps):
        self._Apps = Apps

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAndroidInstanceImagesRequest(AbstractModel):
    """DescribeAndroidInstanceImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceImageIds: 镜像 ID 列表
        :type AndroidInstanceImageIds: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 限制量，默认为20，最大值为100
        :type Limit: int
        """
        self._AndroidInstanceImageIds = None
        self._Offset = None
        self._Limit = None

    @property
    def AndroidInstanceImageIds(self):
        """镜像 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceImageIds

    @AndroidInstanceImageIds.setter
    def AndroidInstanceImageIds(self, AndroidInstanceImageIds):
        self._AndroidInstanceImageIds = AndroidInstanceImageIds

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AndroidInstanceImageIds = params.get("AndroidInstanceImageIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstanceImagesResponse(AbstractModel):
    """DescribeAndroidInstanceImages返回参数结构体

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
        """镜像总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AndroidInstanceImages(self):
        """镜像列表
        :rtype: list of AndroidInstanceImage
        """
        return self._AndroidInstanceImages

    @AndroidInstanceImages.setter
    def AndroidInstanceImages(self, AndroidInstanceImages):
        self._AndroidInstanceImages = AndroidInstanceImages

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """DescribeAndroidInstanceLabels请求参数结构体

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
        """标签键列表
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Values(self):
        """标签值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Offset(self):
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制量，默认为20，最大值为100
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
    """DescribeAndroidInstanceLabels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 安卓实例标签总数
        :type Total: int
        :param _Labels: 安卓实例标签列表
        :type Labels: list of AndroidInstanceLabel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Labels = None
        self._RequestId = None

    @property
    def Total(self):
        """安卓实例标签总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Labels(self):
        """安卓实例标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = params.get("RequestId")


class DescribeAndroidInstanceTasksStatusRequest(AbstractModel):
    """DescribeAndroidInstanceTasksStatus请求参数结构体

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
        """
        self._TaskIds = None
        self._Filter = None
        self._Offset = None
        self._Limit = None

    @property
    def TaskIds(self):
        """任务 ID 列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Filter(self):
        """条件过滤器
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Offset(self):
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAndroidInstanceTasksStatusResponse(AbstractModel):
    """DescribeAndroidInstanceTasksStatus返回参数结构体

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
        """任务状态集合
        :rtype: list of AndroidInstanceTaskStatus
        """
        return self._TaskStatusSet

    @TaskStatusSet.setter
    def TaskStatusSet(self, TaskStatusSet):
        self._TaskStatusSet = TaskStatusSet

    @property
    def Total(self):
        """任务总数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAndroidInstancesRequest(AbstractModel):
    """DescribeAndroidInstances请求参数结构体

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
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AndroidInstanceIds(self):
        """实例ID。每次请求的实例的上限为100。
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidInstanceRegion(self):
        """实例地域。目前还不支持按地域进行聚合查询
        :rtype: str
        """
        return self._AndroidInstanceRegion

    @AndroidInstanceRegion.setter
    def AndroidInstanceRegion(self, AndroidInstanceRegion):
        self._AndroidInstanceRegion = AndroidInstanceRegion

    @property
    def AndroidInstanceZone(self):
        """实例可用区
        :rtype: str
        """
        return self._AndroidInstanceZone

    @AndroidInstanceZone.setter
    def AndroidInstanceZone(self, AndroidInstanceZone):
        self._AndroidInstanceZone = AndroidInstanceZone

    @property
    def AndroidInstanceGroupIds(self):
        """实例分组 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceGroupIds

    @AndroidInstanceGroupIds.setter
    def AndroidInstanceGroupIds(self, AndroidInstanceGroupIds):
        self._AndroidInstanceGroupIds = AndroidInstanceGroupIds

    @property
    def LabelSelector(self):
        """实例标签选择器
        :rtype: list of LabelRequirement
        """
        return self._LabelSelector

    @LabelSelector.setter
    def LabelSelector(self, LabelSelector):
        self._LabelSelector = LabelSelector

    @property
    def Filters(self):
        """字段过滤器。Filter 的 Name 有以下值：
Name：实例名称
UserId：实例用户ID
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
    """DescribeAndroidInstances返回参数结构体

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
        """实例总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AndroidInstances(self):
        """实例列表
        :rtype: list of AndroidInstance
        """
        return self._AndroidInstances

    @AndroidInstances.setter
    def AndroidInstances(self, AndroidInstances):
        self._AndroidInstances = AndroidInstances

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """DescribeInstancesCount请求参数结构体

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
        """游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GroupId(self):
        """实例分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GameRegion(self):
        """游戏区域
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def GameType(self):
        """游戏类型。
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
    """DescribeInstancesCount返回参数结构体

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
        """客户的实例总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Running(self):
        """客户的实例运行数
        :rtype: int
        """
        return self._Running

    @Running.setter
    def Running(self, Running):
        self._Running = Running

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """DestroyAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        """安卓实例 ID 列表
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
    """DestroyAndroidInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExecuteCommandOnAndroidInstancesRequest(AbstractModel):
    """ExecuteCommandOnAndroidInstances请求参数结构体

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
        """安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Command(self):
        """shell 命令
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
    """ExecuteCommandOnAndroidInstances返回参数结构体

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
        """任务集合，可异步查询任务状态
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class Filter(AbstractModel):
    """过滤

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
        """字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段值列表
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
        


class InstallAndroidInstancesAppRequest(AbstractModel):
    """InstallAndroidInstancesApp请求参数结构体

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
        """实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidAppId(self):
        """应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def AndroidAppVersion(self):
        """应用版本
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
    """InstallAndroidInstancesApp返回参数结构体

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
        """任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """标签要求

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
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        """运算符类型。
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
        """标签值列表
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
        


class ModifyAndroidInstanceInformationRequest(AbstractModel):
    """ModifyAndroidInstanceInformation请求参数结构体

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
        """安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Name(self):
        """实例名称
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
    """ModifyAndroidInstanceInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstanceResolutionRequest(AbstractModel):
    """ModifyAndroidInstanceResolution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceId: 安卓实例 ID
        :type AndroidInstanceId: str
        :param _Width: 分辨率宽度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）、双开（A2）、三开（ A3）：建议设置为 1080
实例类型为 四开（A4） 及以上：建议设置为 720
        :type Width: int
        :param _Height: 分辨率高度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）、双开（A2）、三开（ A3）：建议设置为 1920
实例类型为 四开（A4） 及以上：建议设置为 1280
        :type Height: int
        :param _DPI: 每英寸像素点。如果不填，系统将会计算一个合理的数值。修改 DPI 可能会导致 App 异常退出，请谨慎使用！
分辨率为 720x1280：建议配置为 320
分辨率为  1080x1920：建议配置为 480
        :type DPI: int
        """
        self._AndroidInstanceId = None
        self._Width = None
        self._Height = None
        self._DPI = None

    @property
    def AndroidInstanceId(self):
        """安卓实例 ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def Width(self):
        """分辨率宽度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）、双开（A2）、三开（ A3）：建议设置为 1080
实例类型为 四开（A4） 及以上：建议设置为 720
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """分辨率高度。建议按照以下数值设置，避免出现性能不足问题：
实例类型为单开（A1）、双开（A2）、三开（ A3）：建议设置为 1920
实例类型为 四开（A4） 及以上：建议设置为 1280
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def DPI(self):
        """每英寸像素点。如果不填，系统将会计算一个合理的数值。修改 DPI 可能会导致 App 异常退出，请谨慎使用！
分辨率为 720x1280：建议配置为 320
分辨率为  1080x1920：建议配置为 480
        :rtype: int
        """
        return self._DPI

    @DPI.setter
    def DPI(self, DPI):
        self._DPI = DPI


    def _deserialize(self, params):
        self._AndroidInstanceId = params.get("AndroidInstanceId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._DPI = params.get("DPI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstanceResolutionResponse(AbstractModel):
    """ModifyAndroidInstanceResolution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstancesLabelsRequest(AbstractModel):
    """ModifyAndroidInstancesLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _AndroidInstanceLabels: 安卓实例标签列表
        :type AndroidInstanceLabels: list of AndroidInstanceLabel
        :param _Operation: 操作类型。ADD：标签键不存在的添加新标签，标签键存在的将覆盖原有标签REMOVE：根据标签键删除标签REPLACE：使用请求标签列表替换原来所有标签CLEAR：清除所有标签
        :type Operation: str
        """
        self._AndroidInstanceIds = None
        self._AndroidInstanceLabels = None
        self._Operation = None

    @property
    def AndroidInstanceIds(self):
        """安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidInstanceLabels(self):
        """安卓实例标签列表
        :rtype: list of AndroidInstanceLabel
        """
        return self._AndroidInstanceLabels

    @AndroidInstanceLabels.setter
    def AndroidInstanceLabels(self, AndroidInstanceLabels):
        self._AndroidInstanceLabels = AndroidInstanceLabels

    @property
    def Operation(self):
        """操作类型。ADD：标签键不存在的添加新标签，标签键存在的将覆盖原有标签REMOVE：根据标签键删除标签REPLACE：使用请求标签列表替换原来所有标签CLEAR：清除所有标签
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        if params.get("AndroidInstanceLabels") is not None:
            self._AndroidInstanceLabels = []
            for item in params.get("AndroidInstanceLabels"):
                obj = AndroidInstanceLabel()
                obj._deserialize(item)
                self._AndroidInstanceLabels.append(obj)
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAndroidInstancesLabelsResponse(AbstractModel):
    """ModifyAndroidInstancesLabels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAndroidInstancesUserIdRequest(AbstractModel):
    """ModifyAndroidInstancesUserId请求参数结构体

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
        """安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def UserId(self):
        """用户 ID
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
    """ModifyAndroidInstancesUserId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RebootAndroidInstancesRequest(AbstractModel):
    """RebootAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        """实例ID
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
    """RebootAndroidInstances返回参数结构体

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
        """任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResetAndroidInstancesRequest(AbstractModel):
    """ResetAndroidInstances请求参数结构体

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
        """实例ID列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidInstanceImageId(self):
        """指定有效的镜像 ID。
默认取值：默认使用当前镜像。
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def Mode(self):
        """重置模式。在 AndroidInstanceImageId 不为空时才生效。

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
    """ResetAndroidInstances返回参数结构体

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
        """任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """RestartAndroidInstancesApp请求参数结构体

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
        """实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        """应用包名
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
        


class RestartAndroidInstancesAppResponse(AbstractModel):
    """RestartAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RestoreAndroidInstanceFromStorageRequest(AbstractModel):
    """RestoreAndroidInstanceFromStorage请求参数结构体

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
        """安卓实例ID
        :rtype: str
        """
        return self._AndroidInstanceId

    @AndroidInstanceId.setter
    def AndroidInstanceId(self, AndroidInstanceId):
        self._AndroidInstanceId = AndroidInstanceId

    @property
    def ObjectKey(self):
        """自定义备份对象Key
        :rtype: str
        """
        return self._ObjectKey

    @ObjectKey.setter
    def ObjectKey(self, ObjectKey):
        self._ObjectKey = ObjectKey

    @property
    def StorageType(self):
        """存储服务器类型，如 COS、S3。注意：使用 COS 和 S3 都将占用外网带宽。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def COSOptions(self):
        """COS协议选项
        :rtype: :class:`tencentcloud.gs.v20191118.models.COSOptions`
        """
        return self._COSOptions

    @COSOptions.setter
    def COSOptions(self, COSOptions):
        self._COSOptions = COSOptions

    @property
    def S3Options(self):
        """S3存储协议选项
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
    """RestoreAndroidInstanceFromStorage返回参数结构体

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
        """实例任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """S3协议参数

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
        """存储节点
        :rtype: str
        """
        return self._EndPoint

    @EndPoint.setter
    def EndPoint(self, EndPoint):
        self._EndPoint = EndPoint

    @property
    def Bucket(self):
        """存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKeyId(self):
        """密钥 ID
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretAccessKey(self):
        """密钥 Key
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
    """SaveGameArchive请求参数结构体

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
        """游戏用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        """游戏ID
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
    """SaveGameArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartAndroidInstancesAppRequest(AbstractModel):
    """StartAndroidInstancesApp请求参数结构体

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
        """实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        """应用包名
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
        


class StartAndroidInstancesAppResponse(AbstractModel):
    """StartAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartAndroidInstancesRequest(AbstractModel):
    """StartAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        """实例ID
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
    """StartAndroidInstances返回参数结构体

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
        """任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """StartPublishStream请求参数结构体

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
        """唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishUrl(self):
        """推流地址，仅支持rtmp协议
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
    """StartPublishStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartPublishStreamToCSSRequest(AbstractModel):
    """StartPublishStreamToCSS请求参数结构体

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
        """唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamArgs(self):
        """推流参数，推流时携带自定义参数。
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
    """StartPublishStreamToCSS返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopAndroidInstancesAppRequest(AbstractModel):
    """StopAndroidInstancesApp请求参数结构体

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
        """实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def PackageName(self):
        """应用包名
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
    """StopAndroidInstancesApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopAndroidInstancesRequest(AbstractModel):
    """StopAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 实例ID
        :type AndroidInstanceIds: list of str
        """
        self._AndroidInstanceIds = None

    @property
    def AndroidInstanceIds(self):
        """实例ID
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
    """StopAndroidInstances返回参数结构体

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
        """任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """StopGame请求参数结构体

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
        """唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def HostUserId(self):
        """【多人游戏】游戏主机用户ID
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
    """StopGame返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopPublishStreamRequest(AbstractModel):
    """StopPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        """唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
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
    """StopPublishStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SwitchGameArchiveRequest(AbstractModel):
    """SwitchGameArchive请求参数结构体

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
        """游戏用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        """游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameArchiveUrl(self):
        """游戏存档Url
        :rtype: str
        """
        return self._GameArchiveUrl

    @GameArchiveUrl.setter
    def GameArchiveUrl(self, GameArchiveUrl):
        self._GameArchiveUrl = GameArchiveUrl

    @property
    def GameContext(self):
        """游戏相关参数
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
    """SwitchGameArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SyncAndroidInstanceImage(AbstractModel):
    """同步安卓实例镜像信息

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
        """镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def AndroidInstanceImageZone(self):
        """镜像可用区
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
    """SyncAndroidInstanceImage请求参数结构体

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
        """安卓实例镜像 ID
        :rtype: str
        """
        return self._AndroidInstanceImageId

    @AndroidInstanceImageId.setter
    def AndroidInstanceImageId(self, AndroidInstanceImageId):
        self._AndroidInstanceImageId = AndroidInstanceImageId

    @property
    def DestinationZones(self):
        """目的同步可用区列表
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
    """SyncAndroidInstanceImage返回参数结构体

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
        """同步安卓实例镜像列表
        :rtype: list of SyncAndroidInstanceImage
        """
        return self._SyncAndroidInstanceImages

    @SyncAndroidInstanceImages.setter
    def SyncAndroidInstanceImages(self, SyncAndroidInstanceImages):
        self._SyncAndroidInstanceImages = SyncAndroidInstanceImages

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """SyncExecuteCommandOnAndroidInstances请求参数结构体

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
        """安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def Command(self):
        """shell 命令，必须是1秒内能自动结束的命令
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
    """SyncExecuteCommandOnAndroidInstances返回参数结构体

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
        """命令执行结果列表
        :rtype: list of SyncExecuteCommandResult
        """
        return self._CommandResults

    @CommandResults.setter
    def CommandResults(self, CommandResults):
        self._CommandResults = CommandResults

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """同步执行命令结果

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
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Output(self):
        """命令执行输出内容
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Status(self):
        """命令执行结果
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
    """TrylockWorker请求参数结构体

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
        """唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        """游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameRegion(self):
        """游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等，如果不为空，优先按照该区域进行调度分配机器
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def SetNo(self):
        """【废弃】资源池编号
        :rtype: int
        """
        return self._SetNo

    @SetNo.setter
    def SetNo(self, SetNo):
        self._SetNo = SetNo

    @property
    def UserIp(self):
        """【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def GroupId(self):
        """分组ID
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
    """TrylockWorker返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UninstallAndroidInstancesAppRequest(AbstractModel):
    """UninstallAndroidInstancesApp请求参数结构体

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
        """实例ID
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def AndroidAppId(self):
        """应用ID
        :rtype: str
        """
        return self._AndroidAppId

    @AndroidAppId.setter
    def AndroidAppId(self, AndroidAppId):
        self._AndroidAppId = AndroidAppId

    @property
    def PackageName(self):
        """包名
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
    """UninstallAndroidInstancesApp返回参数结构体

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
        """任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """UploadFileToAndroidInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AndroidInstanceIds: 安卓实例 ID 列表
        :type AndroidInstanceIds: list of str
        :param _FileURL: 文件下载 URL
        :type FileURL: str
        :param _DestinationDirectory: 上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :type DestinationDirectory: str
        """
        self._AndroidInstanceIds = None
        self._FileURL = None
        self._DestinationDirectory = None

    @property
    def AndroidInstanceIds(self):
        """安卓实例 ID 列表
        :rtype: list of str
        """
        return self._AndroidInstanceIds

    @AndroidInstanceIds.setter
    def AndroidInstanceIds(self, AndroidInstanceIds):
        self._AndroidInstanceIds = AndroidInstanceIds

    @property
    def FileURL(self):
        """文件下载 URL
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def DestinationDirectory(self):
        """上传目标目录，只能上传到 /sdcard/ 目录或其子目录下
        :rtype: str
        """
        return self._DestinationDirectory

    @DestinationDirectory.setter
    def DestinationDirectory(self, DestinationDirectory):
        self._DestinationDirectory = DestinationDirectory


    def _deserialize(self, params):
        self._AndroidInstanceIds = params.get("AndroidInstanceIds")
        self._FileURL = params.get("FileURL")
        self._DestinationDirectory = params.get("DestinationDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileToAndroidInstancesResponse(AbstractModel):
    """UploadFileToAndroidInstances返回参数结构体

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
        """实例任务集合
        :rtype: list of AndroidInstanceTask
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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