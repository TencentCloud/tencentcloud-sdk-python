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


class AccessInfo(AbstractModel):
    """HTTP域名相关信息

    """

    def __init__(self):
        r"""
        :param _Host: 域名
        :type Host: str
        :param _Vip: VIP
        :type Vip: str
        """
        self._Host = None
        self._Vip = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Alias(AbstractModel):
    """函数的版本别名

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param _Name: 别名的名称
        :type Name: str
        :param _RoutingConfig: 别名的路由信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _ModTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTime: str
        """
        self._FunctionVersion = None
        self._Name = None
        self._RoutingConfig = None
        self._Description = None
        self._AddTime = None
        self._ModTime = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        self._Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEvent(AbstractModel):
    """异步事件

    """

    def __init__(self):
        r"""
        :param _InvokeRequestId: 调用请求id
        :type InvokeRequestId: str
        :param _InvokeType: 调用类型
        :type InvokeType: str
        :param _Qualifier: 函数版本
        :type Qualifier: str
        :param _Status: 事件状态，RUNNING 表示运行中, FINISHED 表示调用成功, ABORTED 表示调用终止, FAILED 表示调用失败
        :type Status: str
        :param _StartTime: 调用开始时间，格式: "%Y-%m-%d %H:%M:%S.%f"
        :type StartTime: str
        :param _EndTime: 调用结束时间，格式: "%Y-%m-%d %H:%M:%S.%f"
        :type EndTime: str
        """
        self._InvokeRequestId = None
        self._InvokeType = None
        self._Qualifier = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId

    @property
    def InvokeType(self):
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._InvokeRequestId = params.get("InvokeRequestId")
        self._InvokeType = params.get("InvokeType")
        self._Qualifier = params.get("Qualifier")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEventStatus(AbstractModel):
    """异步事件状态

    """

    def __init__(self):
        r"""
        :param _Status: 异步事件状态，RUNNING 表示运行中, FINISHED 表示调用成功, ABORTED 表示调用终止, FAILED 表示调用失败。
        :type Status: str
        :param _StatusCode: 请求状态码
        :type StatusCode: int
        :param _InvokeRequestId: 异步执行请求 Id
        :type InvokeRequestId: str
        """
        self._Status = None
        self._StatusCode = None
        self._InvokeRequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StatusCode = params.get("StatusCode")
        self._InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncTriggerConfig(AbstractModel):
    """函数的异步重试配置详情

    """

    def __init__(self):
        r"""
        :param _RetryConfig: 用户错误的异步重试重试配置
        :type RetryConfig: list of RetryConfig
        :param _MsgTTL: 消息保留时间
        :type MsgTTL: int
        """
        self._RetryConfig = None
        self._MsgTTL = None

    @property
    def RetryConfig(self):
        return self._RetryConfig

    @RetryConfig.setter
    def RetryConfig(self, RetryConfig):
        self._RetryConfig = RetryConfig

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL


    def _deserialize(self, params):
        if params.get("RetryConfig") is not None:
            self._RetryConfig = []
            for item in params.get("RetryConfig"):
                obj = RetryConfig()
                obj._deserialize(item)
                self._RetryConfig.append(obj)
        self._MsgTTL = params.get("MsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfsConfig(AbstractModel):
    """文件系统(cfs)配置描述

    """

    def __init__(self):
        r"""
        :param _CfsInsList: 文件系统信息列表
        :type CfsInsList: list of CfsInsInfo
        """
        self._CfsInsList = None

    @property
    def CfsInsList(self):
        return self._CfsInsList

    @CfsInsList.setter
    def CfsInsList(self, CfsInsList):
        self._CfsInsList = CfsInsList


    def _deserialize(self, params):
        if params.get("CfsInsList") is not None:
            self._CfsInsList = []
            for item in params.get("CfsInsList"):
                obj = CfsInsInfo()
                obj._deserialize(item)
                self._CfsInsList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfsInsInfo(AbstractModel):
    """云函数关联的cfs配置信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户id
        :type UserId: str
        :param _UserGroupId: 用户组id
        :type UserGroupId: str
        :param _CfsId: 文件系统实例id
        :type CfsId: str
        :param _MountInsId: 文件系统挂载点id
        :type MountInsId: str
        :param _LocalMountDir: 本地挂载点
        :type LocalMountDir: str
        :param _RemoteMountDir: 远程挂载点
        :type RemoteMountDir: str
        :param _IpAddress: 文件系统ip，配置 cfs 时无需填写。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param _MountVpcId: 文件系统所在的私有网络id，配置 cfs 时无需填写。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MountVpcId: str
        :param _MountSubnetId: 文件系统所在私有网络的子网id，配置 cfs 时无需填写。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MountSubnetId: str
        """
        self._UserId = None
        self._UserGroupId = None
        self._CfsId = None
        self._MountInsId = None
        self._LocalMountDir = None
        self._RemoteMountDir = None
        self._IpAddress = None
        self._MountVpcId = None
        self._MountSubnetId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def CfsId(self):
        return self._CfsId

    @CfsId.setter
    def CfsId(self, CfsId):
        self._CfsId = CfsId

    @property
    def MountInsId(self):
        return self._MountInsId

    @MountInsId.setter
    def MountInsId(self, MountInsId):
        self._MountInsId = MountInsId

    @property
    def LocalMountDir(self):
        return self._LocalMountDir

    @LocalMountDir.setter
    def LocalMountDir(self, LocalMountDir):
        self._LocalMountDir = LocalMountDir

    @property
    def RemoteMountDir(self):
        return self._RemoteMountDir

    @RemoteMountDir.setter
    def RemoteMountDir(self, RemoteMountDir):
        self._RemoteMountDir = RemoteMountDir

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def MountVpcId(self):
        return self._MountVpcId

    @MountVpcId.setter
    def MountVpcId(self, MountVpcId):
        self._MountVpcId = MountVpcId

    @property
    def MountSubnetId(self):
        return self._MountSubnetId

    @MountSubnetId.setter
    def MountSubnetId(self, MountSubnetId):
        self._MountSubnetId = MountSubnetId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserGroupId = params.get("UserGroupId")
        self._CfsId = params.get("CfsId")
        self._MountInsId = params.get("MountInsId")
        self._LocalMountDir = params.get("LocalMountDir")
        self._RemoteMountDir = params.get("RemoteMountDir")
        self._IpAddress = params.get("IpAddress")
        self._MountVpcId = params.get("MountVpcId")
        self._MountSubnetId = params.get("MountSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Code(AbstractModel):
    """函数代码

    """

    def __init__(self):
        r"""
        :param _CosBucketName: 对象存储桶名称（填写存储桶名称自定义部分，不包含-appid）
        :type CosBucketName: str
        :param _CosObjectName: 对象存储中代码包文件路径，以/开头
        :type CosObjectName: str
        :param _ZipFile: 包含函数代码文件及其依赖项的 zip 格式文件，zip包大小上限为 50MB，使用该接口时要求将 zip 文件的内容转成 base64 编码
        :type ZipFile: str
        :param _CosBucketRegion: 对象存储的地域，地域为北京时需要传入ap-beijing,北京一区时需要传递ap-beijing-1，其他的地域不需要传递。
        :type CosBucketRegion: str
        :param _DemoId: 如果是通过Demo创建的话，需要传入DemoId
        :type DemoId: str
        :param _TempCosObjectName: 如果是从TempCos创建的话，需要传入TempCosObjectName
        :type TempCosObjectName: str
        :param _GitUrl: Git地址。该功能已下线。
        :type GitUrl: str
        :param _GitUserName: Git用户名。该功能已下线。
        :type GitUserName: str
        :param _GitPassword: Git密码。该功能已下线。
        :type GitPassword: str
        :param _GitPasswordSecret: 加密后的Git密码，一般无需指定。该功能已下线。
        :type GitPasswordSecret: str
        :param _GitBranch: Git分支。该功能已下线。
        :type GitBranch: str
        :param _GitDirectory: 代码在Git仓库中的路径。该功能已下线。
        :type GitDirectory: str
        :param _GitCommitId: 指定要拉取的版本。该功能已下线。
        :type GitCommitId: str
        :param _GitUserNameSecret: 加密后的Git用户名，一般无需指定。该功能已下线。
        :type GitUserNameSecret: str
        :param _ImageConfig: 镜像部署时配置TCR镜像信息
        :type ImageConfig: :class:`tencentcloud.scf.v20180416.models.ImageConfig`
        """
        self._CosBucketName = None
        self._CosObjectName = None
        self._ZipFile = None
        self._CosBucketRegion = None
        self._DemoId = None
        self._TempCosObjectName = None
        self._GitUrl = None
        self._GitUserName = None
        self._GitPassword = None
        self._GitPasswordSecret = None
        self._GitBranch = None
        self._GitDirectory = None
        self._GitCommitId = None
        self._GitUserNameSecret = None
        self._ImageConfig = None

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CosObjectName(self):
        return self._CosObjectName

    @CosObjectName.setter
    def CosObjectName(self, CosObjectName):
        self._CosObjectName = CosObjectName

    @property
    def ZipFile(self):
        return self._ZipFile

    @ZipFile.setter
    def ZipFile(self, ZipFile):
        self._ZipFile = ZipFile

    @property
    def CosBucketRegion(self):
        return self._CosBucketRegion

    @CosBucketRegion.setter
    def CosBucketRegion(self, CosBucketRegion):
        self._CosBucketRegion = CosBucketRegion

    @property
    def DemoId(self):
        return self._DemoId

    @DemoId.setter
    def DemoId(self, DemoId):
        self._DemoId = DemoId

    @property
    def TempCosObjectName(self):
        return self._TempCosObjectName

    @TempCosObjectName.setter
    def TempCosObjectName(self, TempCosObjectName):
        self._TempCosObjectName = TempCosObjectName

    @property
    def GitUrl(self):
        return self._GitUrl

    @GitUrl.setter
    def GitUrl(self, GitUrl):
        self._GitUrl = GitUrl

    @property
    def GitUserName(self):
        return self._GitUserName

    @GitUserName.setter
    def GitUserName(self, GitUserName):
        self._GitUserName = GitUserName

    @property
    def GitPassword(self):
        return self._GitPassword

    @GitPassword.setter
    def GitPassword(self, GitPassword):
        self._GitPassword = GitPassword

    @property
    def GitPasswordSecret(self):
        return self._GitPasswordSecret

    @GitPasswordSecret.setter
    def GitPasswordSecret(self, GitPasswordSecret):
        self._GitPasswordSecret = GitPasswordSecret

    @property
    def GitBranch(self):
        return self._GitBranch

    @GitBranch.setter
    def GitBranch(self, GitBranch):
        self._GitBranch = GitBranch

    @property
    def GitDirectory(self):
        return self._GitDirectory

    @GitDirectory.setter
    def GitDirectory(self, GitDirectory):
        self._GitDirectory = GitDirectory

    @property
    def GitCommitId(self):
        return self._GitCommitId

    @GitCommitId.setter
    def GitCommitId(self, GitCommitId):
        self._GitCommitId = GitCommitId

    @property
    def GitUserNameSecret(self):
        return self._GitUserNameSecret

    @GitUserNameSecret.setter
    def GitUserNameSecret(self, GitUserNameSecret):
        self._GitUserNameSecret = GitUserNameSecret

    @property
    def ImageConfig(self):
        return self._ImageConfig

    @ImageConfig.setter
    def ImageConfig(self, ImageConfig):
        self._ImageConfig = ImageConfig


    def _deserialize(self, params):
        self._CosBucketName = params.get("CosBucketName")
        self._CosObjectName = params.get("CosObjectName")
        self._ZipFile = params.get("ZipFile")
        self._CosBucketRegion = params.get("CosBucketRegion")
        self._DemoId = params.get("DemoId")
        self._TempCosObjectName = params.get("TempCosObjectName")
        self._GitUrl = params.get("GitUrl")
        self._GitUserName = params.get("GitUserName")
        self._GitPassword = params.get("GitPassword")
        self._GitPasswordSecret = params.get("GitPasswordSecret")
        self._GitBranch = params.get("GitBranch")
        self._GitDirectory = params.get("GitDirectory")
        self._GitCommitId = params.get("GitCommitId")
        self._GitUserNameSecret = params.get("GitUserNameSecret")
        if params.get("ImageConfig") is not None:
            self._ImageConfig = ImageConfig()
            self._ImageConfig._deserialize(params.get("ImageConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionRequest(AbstractModel):
    """CopyFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 要复制的函数的名称
        :type FunctionName: str
        :param _NewFunctionName: 新函数的名称
        :type NewFunctionName: str
        :param _Namespace: 要复制的函数所在的命名空间，默认为default
        :type Namespace: str
        :param _TargetNamespace: 将函数复制到的命名空间，默认为default
        :type TargetNamespace: str
        :param _Description: 新函数的描述
        :type Description: str
        :param _TargetRegion: 要将函数复制到的地域，不填则默认为当前地域
        :type TargetRegion: str
        :param _Override: 如果目标Namespace下已有同名函数，是否覆盖，默认为否
（注意：如果选择覆盖，会导致同名函数被删除，请慎重操作）
TRUE：覆盖同名函数
FALSE：不覆盖同名函数
        :type Override: bool
        :param _CopyConfiguration: 是否复制函数的属性，包括环境变量、内存、超时、函数描述、标签、VPC等，默认为是。
TRUE：复制函数配置
FALSE：不复制函数配置
        :type CopyConfiguration: bool
        """
        self._FunctionName = None
        self._NewFunctionName = None
        self._Namespace = None
        self._TargetNamespace = None
        self._Description = None
        self._TargetRegion = None
        self._Override = None
        self._CopyConfiguration = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def NewFunctionName(self):
        return self._NewFunctionName

    @NewFunctionName.setter
    def NewFunctionName(self, NewFunctionName):
        self._NewFunctionName = NewFunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TargetNamespace(self):
        return self._TargetNamespace

    @TargetNamespace.setter
    def TargetNamespace(self, TargetNamespace):
        self._TargetNamespace = TargetNamespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TargetRegion(self):
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def CopyConfiguration(self):
        return self._CopyConfiguration

    @CopyConfiguration.setter
    def CopyConfiguration(self, CopyConfiguration):
        self._CopyConfiguration = CopyConfiguration


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._NewFunctionName = params.get("NewFunctionName")
        self._Namespace = params.get("Namespace")
        self._TargetNamespace = params.get("TargetNamespace")
        self._Description = params.get("Description")
        self._TargetRegion = params.get("TargetRegion")
        self._Override = params.get("Override")
        self._CopyConfiguration = params.get("CopyConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionResponse(AbstractModel):
    """CopyFunction返回参数结构体

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


class CreateAliasRequest(AbstractModel):
    """CreateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 别名的名称，在函数级别中唯一，只能包含字母、数字、'_'和‘-’，且必须以字母开头，长度限制为1-64
        :type Name: str
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param _Namespace: 函数所在的命名空间
        :type Namespace: str
        :param _RoutingConfig: 别名的路由信息，需要为别名指定附加版本时，必须提供此参数；	  附加版本指的是：除主版本 FunctionVersion 外，为此别名再指定一个函数可正常使用的版本；   这里附加版本中的 Version 值 不能是别名指向的主版本；  要注意的是：如果想要某个版本的流量全部指向这个别名，不需配置此参数； 目前一个别名最多只能指定一个附加版本
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: 别名的描述信息
        :type Description: str
        """
        self._Name = None
        self._FunctionName = None
        self._FunctionVersion = None
        self._Namespace = None
        self._RoutingConfig = None
        self._Description = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._FunctionName = params.get("FunctionName")
        self._FunctionVersion = params.get("FunctionVersion")
        self._Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasResponse(AbstractModel):
    """CreateAlias返回参数结构体

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


class CreateFunctionRequest(AbstractModel):
    """CreateFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 创建的函数名称，函数名称支持26个英文字母大小写、数字、连接符和下划线，第一个字符只能以字母开头，最后一个字符不能为连接符或者下划线，名称长度2-60
        :type FunctionName: str
        :param _Code: 函数代码. 注意：不能同时指定Cos、ZipFile或 DemoId。
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param _Handler: 函数处理方法名称，名称格式支持 "文件名称.方法名称" 形式（java 名称格式 包名.类名::方法名），文件名称和函数名称之间以"."隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求是 2-60 个字符
        :type Handler: str
        :param _Description: 函数描述,最大支持 1000 个英文字母、数字、空格、逗号、换行符和英文句号，支持中文
        :type Description: str
        :param _MemorySize: 函数运行时内存大小，默认为 128M，可选范围 64、128MB-3072MB，并且以 128MB 为阶梯
        :type MemorySize: int
        :param _Timeout: 函数最长执行时间，单位为秒，可选值范围 1-900 秒，默认为 3 秒
        :type Timeout: int
        :param _Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param _Runtime: 函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10，Nodejs8.9，Nodejs10.15，Nodejs12.16， Php5.2， Php7.4，Go1，Java8 和 CustomRuntime，默认Python2.7
        :type Runtime: str
        :param _VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param _Namespace: 函数所属命名空间
        :type Namespace: str
        :param _Role: 函数绑定的角色
        :type Role: str
        :param _InstallDependency: [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)，TRUE 表示安装，默认值为 FALSE。仅支持 Node.js 函数。
        :type InstallDependency: str
        :param _ClsLogsetId: 函数日志投递到的CLS LogsetID
        :type ClsLogsetId: str
        :param _ClsTopicId: 函数日志投递到的CLS TopicID
        :type ClsTopicId: str
        :param _Type: 函数类型，默认值为Event，创建触发器函数请填写Event，创建HTTP函数级服务请填写HTTP
        :type Type: str
        :param _CodeSource: CodeSource 代码来源，支持ZipFile, Cos, Demo 其中之一
        :type CodeSource: str
        :param _Layers: 函数要关联的Layer版本列表，Layer会按照在列表中顺序依次覆盖。
        :type Layers: list of LayerVersionSimple
        :param _DeadLetterConfig: 死信队列参数
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param _PublicNetConfig: 公网访问配置
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`
        :param _CfsConfig: 文件系统配置参数，用于云函数挂载文件系统
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param _InitTimeout: 函数初始化超时时间，默认 65s，镜像部署函数默认 90s。
        :type InitTimeout: int
        :param _Tags: 函数 Tag 参数，以键值对数组形式传入
        :type Tags: list of Tag
        :param _AsyncRunEnable: 是否开启异步属性，TRUE 为开启，FALSE为关闭
        :type AsyncRunEnable: str
        :param _TraceEnable: 是否开启事件追踪，TRUE 为开启，FALSE为关闭
        :type TraceEnable: str
        :param _AutoDeployClsTopicIndex: 是否自动创建cls索引，TRUE 为开启，FALSE为关闭
        :type AutoDeployClsTopicIndex: str
        :param _AutoCreateClsTopic: 是否自动创建cls主题，TRUE 为开启，FALSE为关闭
        :type AutoCreateClsTopic: str
        :param _ProtocolType: HTTP函数支持的访问协议。当前支持WebSockets协议，值为WS
        :type ProtocolType: str
        :param _ProtocolParams: HTTP函数配置ProtocolType访问协议，当前协议可配置的参数
        :type ProtocolParams: :class:`tencentcloud.scf.v20180416.models.ProtocolParams`
        :param _InstanceConcurrencyConfig: 单实例多并发配置。只支持Web函数。
        :type InstanceConcurrencyConfig: :class:`tencentcloud.scf.v20180416.models.InstanceConcurrencyConfig`
        :param _DnsCache: 是否开启Dns缓存能力。只支持EVENT函数。默认为FALSE，TRUE 为开启，FALSE为关闭
        :type DnsCache: str
        :param _IntranetConfig: 内网访问配置
        :type IntranetConfig: :class:`tencentcloud.scf.v20180416.models.IntranetConfigIn`
        """
        self._FunctionName = None
        self._Code = None
        self._Handler = None
        self._Description = None
        self._MemorySize = None
        self._Timeout = None
        self._Environment = None
        self._Runtime = None
        self._VpcConfig = None
        self._Namespace = None
        self._Role = None
        self._InstallDependency = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._Type = None
        self._CodeSource = None
        self._Layers = None
        self._DeadLetterConfig = None
        self._PublicNetConfig = None
        self._CfsConfig = None
        self._InitTimeout = None
        self._Tags = None
        self._AsyncRunEnable = None
        self._TraceEnable = None
        self._AutoDeployClsTopicIndex = None
        self._AutoCreateClsTopic = None
        self._ProtocolType = None
        self._ProtocolParams = None
        self._InstanceConcurrencyConfig = None
        self._DnsCache = None
        self._IntranetConfig = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Handler(self):
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def InstallDependency(self):
        return self._InstallDependency

    @InstallDependency.setter
    def InstallDependency(self, InstallDependency):
        self._InstallDependency = InstallDependency

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CodeSource(self):
        return self._CodeSource

    @CodeSource.setter
    def CodeSource(self, CodeSource):
        self._CodeSource = CodeSource

    @property
    def Layers(self):
        return self._Layers

    @Layers.setter
    def Layers(self, Layers):
        self._Layers = Layers

    @property
    def DeadLetterConfig(self):
        return self._DeadLetterConfig

    @DeadLetterConfig.setter
    def DeadLetterConfig(self, DeadLetterConfig):
        self._DeadLetterConfig = DeadLetterConfig

    @property
    def PublicNetConfig(self):
        return self._PublicNetConfig

    @PublicNetConfig.setter
    def PublicNetConfig(self, PublicNetConfig):
        self._PublicNetConfig = PublicNetConfig

    @property
    def CfsConfig(self):
        return self._CfsConfig

    @CfsConfig.setter
    def CfsConfig(self, CfsConfig):
        self._CfsConfig = CfsConfig

    @property
    def InitTimeout(self):
        return self._InitTimeout

    @InitTimeout.setter
    def InitTimeout(self, InitTimeout):
        self._InitTimeout = InitTimeout

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AsyncRunEnable(self):
        return self._AsyncRunEnable

    @AsyncRunEnable.setter
    def AsyncRunEnable(self, AsyncRunEnable):
        self._AsyncRunEnable = AsyncRunEnable

    @property
    def TraceEnable(self):
        return self._TraceEnable

    @TraceEnable.setter
    def TraceEnable(self, TraceEnable):
        self._TraceEnable = TraceEnable

    @property
    def AutoDeployClsTopicIndex(self):
        return self._AutoDeployClsTopicIndex

    @AutoDeployClsTopicIndex.setter
    def AutoDeployClsTopicIndex(self, AutoDeployClsTopicIndex):
        self._AutoDeployClsTopicIndex = AutoDeployClsTopicIndex

    @property
    def AutoCreateClsTopic(self):
        return self._AutoCreateClsTopic

    @AutoCreateClsTopic.setter
    def AutoCreateClsTopic(self, AutoCreateClsTopic):
        self._AutoCreateClsTopic = AutoCreateClsTopic

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def ProtocolParams(self):
        return self._ProtocolParams

    @ProtocolParams.setter
    def ProtocolParams(self, ProtocolParams):
        self._ProtocolParams = ProtocolParams

    @property
    def InstanceConcurrencyConfig(self):
        return self._InstanceConcurrencyConfig

    @InstanceConcurrencyConfig.setter
    def InstanceConcurrencyConfig(self, InstanceConcurrencyConfig):
        self._InstanceConcurrencyConfig = InstanceConcurrencyConfig

    @property
    def DnsCache(self):
        return self._DnsCache

    @DnsCache.setter
    def DnsCache(self, DnsCache):
        self._DnsCache = DnsCache

    @property
    def IntranetConfig(self):
        return self._IntranetConfig

    @IntranetConfig.setter
    def IntranetConfig(self, IntranetConfig):
        self._IntranetConfig = IntranetConfig


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        if params.get("Code") is not None:
            self._Code = Code()
            self._Code._deserialize(params.get("Code"))
        self._Handler = params.get("Handler")
        self._Description = params.get("Description")
        self._MemorySize = params.get("MemorySize")
        self._Timeout = params.get("Timeout")
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        self._Runtime = params.get("Runtime")
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._Namespace = params.get("Namespace")
        self._Role = params.get("Role")
        self._InstallDependency = params.get("InstallDependency")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._Type = params.get("Type")
        self._CodeSource = params.get("CodeSource")
        if params.get("Layers") is not None:
            self._Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionSimple()
                obj._deserialize(item)
                self._Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self._DeadLetterConfig = DeadLetterConfig()
            self._DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        if params.get("PublicNetConfig") is not None:
            self._PublicNetConfig = PublicNetConfigIn()
            self._PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        if params.get("CfsConfig") is not None:
            self._CfsConfig = CfsConfig()
            self._CfsConfig._deserialize(params.get("CfsConfig"))
        self._InitTimeout = params.get("InitTimeout")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AsyncRunEnable = params.get("AsyncRunEnable")
        self._TraceEnable = params.get("TraceEnable")
        self._AutoDeployClsTopicIndex = params.get("AutoDeployClsTopicIndex")
        self._AutoCreateClsTopic = params.get("AutoCreateClsTopic")
        self._ProtocolType = params.get("ProtocolType")
        if params.get("ProtocolParams") is not None:
            self._ProtocolParams = ProtocolParams()
            self._ProtocolParams._deserialize(params.get("ProtocolParams"))
        if params.get("InstanceConcurrencyConfig") is not None:
            self._InstanceConcurrencyConfig = InstanceConcurrencyConfig()
            self._InstanceConcurrencyConfig._deserialize(params.get("InstanceConcurrencyConfig"))
        self._DnsCache = params.get("DnsCache")
        if params.get("IntranetConfig") is not None:
            self._IntranetConfig = IntranetConfigIn()
            self._IntranetConfig._deserialize(params.get("IntranetConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFunctionResponse(AbstractModel):
    """CreateFunction返回参数结构体

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


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _Description: 命名空间描述
        :type Description: str
        :param _ResourceEnv: 资源池配置
        :type ResourceEnv: :class:`tencentcloud.scf.v20180416.models.NamespaceResourceEnv`
        """
        self._Namespace = None
        self._Description = None
        self._ResourceEnv = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ResourceEnv(self):
        return self._ResourceEnv

    @ResourceEnv.setter
    def ResourceEnv(self, ResourceEnv):
        self._ResourceEnv = ResourceEnv


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        if params.get("ResourceEnv") is not None:
            self._ResourceEnv = NamespaceResourceEnv()
            self._ResourceEnv._deserialize(params.get("ResourceEnv"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

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


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 新建触发器绑定的函数名称
        :type FunctionName: str
        :param _TriggerName: 新建触发器名称。如果是定时触发器，名称支持英文字母、数字、连接符和下划线，最长100个字符；如果是cos触发器，需要是对应cos存储桶适用于XML API的访问域名(例如:5401-5ff414-12345.cos.ap-shanghai.myqcloud.com);如果是其他触发器，见具体触发器绑定参数的说明
        :type TriggerName: str
        :param _Type: 触发器类型，目前支持 cos 、cmq、 timer、 ckafka、apigw类型。创建函数 URL 请在此填写 http，请参考[创建函数 URL ](https://cloud.tencent.com/document/product/583/100227#33bbbda4-9131-48a6-ac37-ac62ffe01424)。创建 cls 触发器请参考[CLS 创建投递 SCF 任务](https://cloud.tencent.com/document/product/614/61096)。
        :type Type: str
        :param _TriggerDesc: 触发器对应的参数，可见具体[触发器描述说明](https://cloud.tencent.com/document/product/583/39901)
        :type TriggerDesc: str
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        :param _Qualifier: 函数的版本，默认为 $LATEST，建议填写 [$DEFAULT](https://cloud.tencent.com/document/product/583/36149#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)方便后续进行版本的灰度发布。
        :type Qualifier: str
        :param _Enable: 触发器的初始是能状态 OPEN表示开启 CLOSE表示关闭
        :type Enable: str
        :param _CustomArgument: 用户自定义参数，仅支持timer触发器
        :type CustomArgument: str
        :param _Description: 触发器描述
        :type Description: str
        """
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._TriggerDesc = None
        self._Namespace = None
        self._Qualifier = None
        self._Enable = None
        self._CustomArgument = None
        self._Description = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._TriggerDesc = params.get("TriggerDesc")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._Enable = params.get("Enable")
        self._CustomArgument = params.get("CustomArgument")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerInfo: 触发器信息
        :type TriggerInfo: :class:`tencentcloud.scf.v20180416.models.Trigger`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TriggerInfo = None
        self._RequestId = None

    @property
    def TriggerInfo(self):
        return self._TriggerInfo

    @TriggerInfo.setter
    def TriggerInfo(self, TriggerInfo):
        self._TriggerInfo = TriggerInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TriggerInfo") is not None:
            self._TriggerInfo = Trigger()
            self._TriggerInfo._deserialize(params.get("TriggerInfo"))
        self._RequestId = params.get("RequestId")


class DeadLetterConfig(AbstractModel):
    """死信队列参数

    """

    def __init__(self):
        r"""
        :param _Type: 死信队列模式
        :type Type: str
        :param _Name: 死信队列名称
        :type Name: str
        :param _FilterType: 死信队列主题模式的标签形式
        :type FilterType: str
        """
        self._Type = None
        self._Name = None
        self._FilterType = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Name: 别名的名称
        :type Name: str
        :param _Namespace: 函数所在的命名空间
        :type Namespace: str
        """
        self._FunctionName = None
        self._Name = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias返回参数结构体

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


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 要删除的函数名称
        :type FunctionName: str
        :param _Namespace: 函数所属命名空间
        :type Namespace: str
        :param _Qualifier: 填写需要删除的版本号，不填默认删除函数下全部版本。
        :type Qualifier: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction返回参数结构体

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


class DeleteLayerVersionRequest(AbstractModel):
    """DeleteLayerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LayerName: 层名称
        :type LayerName: str
        :param _LayerVersion: 版本号
        :type LayerVersion: int
        """
        self._LayerName = None
        self._LayerVersion = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLayerVersionResponse(AbstractModel):
    """DeleteLayerVersion返回参数结构体

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


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        """
        self._Namespace = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

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


class DeleteProvisionedConcurrencyConfigRequest(AbstractModel):
    """DeleteProvisionedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要删除预置并发的函数的名称
        :type FunctionName: str
        :param _Qualifier: 函数的版本号
        :type Qualifier: str
        :param _Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProvisionedConcurrencyConfigResponse(AbstractModel):
    """DeleteProvisionedConcurrencyConfig返回参数结构体

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


class DeleteReservedConcurrencyConfigRequest(AbstractModel):
    """DeleteReservedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要删除最大独占配额的函数的名称
        :type FunctionName: str
        :param _Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self._FunctionName = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReservedConcurrencyConfigResponse(AbstractModel):
    """DeleteReservedConcurrencyConfig返回参数结构体

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


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数的名称
        :type FunctionName: str
        :param _TriggerName: 要删除的触发器名称
        :type TriggerName: str
        :param _Type: 要删除的触发器类型，目前支持 cos 、cmq、 timer、ckafka 类型
        :type Type: str
        :param _Namespace: 函数所属命名空间
        :type Namespace: str
        :param _TriggerDesc: 如果删除的触发器类型为 COS 触发器，该字段为必填值，存放 JSON 格式的数据 {"event":"cos:ObjectCreated:*"}，数据内容和 SetTrigger 接口中该字段的格式相同；如果删除的触发器类型为定时触发器或 CMQ 触发器，可以不指定该字段
        :type TriggerDesc: str
        :param _Qualifier: 函数的版本，默认为 $LATEST，建议填写 [$DEFAULT](https://cloud.tencent.com/document/product/583/36149#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)方便后续进行版本的灰度发布。
如果删除的触发器类型为 APIGW 触发器,该字段为必填参数
        :type Qualifier: str
        """
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._Namespace = None
        self._TriggerDesc = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._Namespace = params.get("Namespace")
        self._TriggerDesc = params.get("TriggerDesc")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger返回参数结构体

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


class EipConfigIn(AbstractModel):
    """公网访问固定ip配置

    """

    def __init__(self):
        r"""
        :param _EipStatus: Eip开启状态，取值['ENABLE','DISABLE']
        :type EipStatus: str
        """
        self._EipStatus = None

    @property
    def EipStatus(self):
        return self._EipStatus

    @EipStatus.setter
    def EipStatus(self, EipStatus):
        self._EipStatus = EipStatus


    def _deserialize(self, params):
        self._EipStatus = params.get("EipStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipConfigOut(AbstractModel):
    """公网访问固定ip配置

    """

    def __init__(self):
        r"""
        :param _EipStatus: 是否是固定IP，["ENABLE","DISABLE"]
        :type EipStatus: str
        :param _EipAddress: IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddress: list of str
        """
        self._EipStatus = None
        self._EipAddress = None

    @property
    def EipStatus(self):
        return self._EipStatus

    @EipStatus.setter
    def EipStatus(self, EipStatus):
        self._EipStatus = EipStatus

    @property
    def EipAddress(self):
        return self._EipAddress

    @EipAddress.setter
    def EipAddress(self, EipAddress):
        self._EipAddress = EipAddress


    def _deserialize(self, params):
        self._EipStatus = params.get("EipStatus")
        self._EipAddress = params.get("EipAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipOutConfig(AbstractModel):
    """EipOutConfig

    """

    def __init__(self):
        r"""
        :param _EipFixed: 是否是固定IP，["TRUE","FALSE"]
        :type EipFixed: str
        :param _Eips: IP列表
        :type Eips: list of str
        """
        self._EipFixed = None
        self._Eips = None

    @property
    def EipFixed(self):
        return self._EipFixed

    @EipFixed.setter
    def EipFixed(self, EipFixed):
        self._EipFixed = EipFixed

    @property
    def Eips(self):
        return self._Eips

    @Eips.setter
    def Eips(self, Eips):
        self._Eips = Eips


    def _deserialize(self, params):
        self._EipFixed = params.get("EipFixed")
        self._Eips = params.get("Eips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    """函数的环境变量参数

    """

    def __init__(self):
        r"""
        :param _Variables: 环境变量数组
        :type Variables: list of Variable
        """
        self._Variables = None

    @property
    def Variables(self):
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables


    def _deserialize(self, params):
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。过滤条件数量限制为10。
Name可选值：VpcId, SubnetId, ClsTopicId, ClsLogsetId, Role, CfsId, CfsMountInsId, Eip；Values 长度限制为1。
Name可选值：Status, Runtime, FunctionType, PublicNetStatus, AsyncRunEnable, TraceEnable；Values 长度限制为20。
当 Name = Runtime 时，CustomImage 表示过滤镜像类型函数。
        :type Name: str
        :param _Values: 字段的过滤值。
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
        


class Function(AbstractModel):
    """函数列表

    """

    def __init__(self):
        r"""
        :param _ModTime: 修改时间
        :type ModTime: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _Runtime: 运行时
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _FunctionId: 函数ID
        :type FunctionId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Status: 函数状态，状态值及流转[参考此处](https://cloud.tencent.com/document/product/583/47175)
        :type Status: str
        :param _StatusDesc: 函数状态详情
        :type StatusDesc: str
        :param _Description: 函数描述
        :type Description: str
        :param _Tags: 函数标签
        :type Tags: list of Tag
        :param _Type: 函数类型，取值为 HTTP 或者 Event
        :type Type: str
        :param _StatusReasons: 函数状态失败原因
        :type StatusReasons: list of StatusReason
        :param _TotalProvisionedConcurrencyMem: 函数所有版本预置并发内存总和
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalProvisionedConcurrencyMem: int
        :param _ReservedConcurrencyMem: 函数并发保留内存
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedConcurrencyMem: int
        :param _AsyncRunEnable: 函数异步属性，取值 TRUE 或者 FALSE
        :type AsyncRunEnable: str
        :param _TraceEnable: 异步函数是否开启调用追踪，取值 TRUE 或者 FALSE
        :type TraceEnable: str
        """
        self._ModTime = None
        self._AddTime = None
        self._Runtime = None
        self._FunctionName = None
        self._FunctionId = None
        self._Namespace = None
        self._Status = None
        self._StatusDesc = None
        self._Description = None
        self._Tags = None
        self._Type = None
        self._StatusReasons = None
        self._TotalProvisionedConcurrencyMem = None
        self._ReservedConcurrencyMem = None
        self._AsyncRunEnable = None
        self._TraceEnable = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StatusReasons(self):
        return self._StatusReasons

    @StatusReasons.setter
    def StatusReasons(self, StatusReasons):
        self._StatusReasons = StatusReasons

    @property
    def TotalProvisionedConcurrencyMem(self):
        return self._TotalProvisionedConcurrencyMem

    @TotalProvisionedConcurrencyMem.setter
    def TotalProvisionedConcurrencyMem(self, TotalProvisionedConcurrencyMem):
        self._TotalProvisionedConcurrencyMem = TotalProvisionedConcurrencyMem

    @property
    def ReservedConcurrencyMem(self):
        return self._ReservedConcurrencyMem

    @ReservedConcurrencyMem.setter
    def ReservedConcurrencyMem(self, ReservedConcurrencyMem):
        self._ReservedConcurrencyMem = ReservedConcurrencyMem

    @property
    def AsyncRunEnable(self):
        return self._AsyncRunEnable

    @AsyncRunEnable.setter
    def AsyncRunEnable(self, AsyncRunEnable):
        self._AsyncRunEnable = AsyncRunEnable

    @property
    def TraceEnable(self):
        return self._TraceEnable

    @TraceEnable.setter
    def TraceEnable(self, TraceEnable):
        self._TraceEnable = TraceEnable


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._AddTime = params.get("AddTime")
        self._Runtime = params.get("Runtime")
        self._FunctionName = params.get("FunctionName")
        self._FunctionId = params.get("FunctionId")
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        if params.get("StatusReasons") is not None:
            self._StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self._StatusReasons.append(obj)
        self._TotalProvisionedConcurrencyMem = params.get("TotalProvisionedConcurrencyMem")
        self._ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self._AsyncRunEnable = params.get("AsyncRunEnable")
        self._TraceEnable = params.get("TraceEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionLog(AbstractModel):
    """日志信息

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数的名称
        :type FunctionName: str
        :param _RetMsg: 函数执行完成后的返回值
        :type RetMsg: str
        :param _RequestId: 执行该函数对应的requestId
        :type RequestId: str
        :param _StartTime: 函数开始执行时的时间点
        :type StartTime: str
        :param _RetCode: 函数执行结果，如果是 0 表示执行成功，其他值表示失败
        :type RetCode: int
        :param _InvokeFinished: 函数调用是否结束，如果是 1 表示执行结束，其他值表示调用异常
        :type InvokeFinished: int
        :param _Duration: 函数执行耗时，单位为 ms
        :type Duration: float
        :param _BillDuration: 函数计费时间，根据 duration 向上取最近的 100ms，单位为ms
        :type BillDuration: int
        :param _MemUsage: 函数执行时消耗实际内存大小，单位为 Byte
        :type MemUsage: int
        :param _Log: 函数执行过程中的日志输出
        :type Log: str
        :param _Level: 日志等级
        :type Level: str
        :param _Source: 日志来源
        :type Source: str
        :param _RetryNum: 重试次数
        :type RetryNum: int
        """
        self._FunctionName = None
        self._RetMsg = None
        self._RequestId = None
        self._StartTime = None
        self._RetCode = None
        self._InvokeFinished = None
        self._Duration = None
        self._BillDuration = None
        self._MemUsage = None
        self._Log = None
        self._Level = None
        self._Source = None
        self._RetryNum = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def InvokeFinished(self):
        return self._InvokeFinished

    @InvokeFinished.setter
    def InvokeFinished(self, InvokeFinished):
        self._InvokeFinished = InvokeFinished

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def BillDuration(self):
        return self._BillDuration

    @BillDuration.setter
    def BillDuration(self, BillDuration):
        self._BillDuration = BillDuration

    @property
    def MemUsage(self):
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def RetryNum(self):
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")
        self._StartTime = params.get("StartTime")
        self._RetCode = params.get("RetCode")
        self._InvokeFinished = params.get("InvokeFinished")
        self._Duration = params.get("Duration")
        self._BillDuration = params.get("BillDuration")
        self._MemUsage = params.get("MemUsage")
        self._Log = params.get("Log")
        self._Level = params.get("Level")
        self._Source = params.get("Source")
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionVersion(AbstractModel):
    """函数版本信息

    """

    def __init__(self):
        r"""
        :param _Version: 函数版本名称
        :type Version: str
        :param _Description: 版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _ModTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTime: str
        :param _Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Version = None
        self._Description = None
        self._AddTime = None
        self._ModTime = None
        self._Status = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAccountRequest(AbstractModel):
    """GetAccount请求参数结构体

    """


class GetAccountResponse(AbstractModel):
    """GetAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountUsage: 命名空间已使用的信息
        :type AccountUsage: :class:`tencentcloud.scf.v20180416.models.UsageInfo`
        :param _AccountLimit: 命名空间限制的信息
        :type AccountLimit: :class:`tencentcloud.scf.v20180416.models.LimitsInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountUsage = None
        self._AccountLimit = None
        self._RequestId = None

    @property
    def AccountUsage(self):
        return self._AccountUsage

    @AccountUsage.setter
    def AccountUsage(self, AccountUsage):
        self._AccountUsage = AccountUsage

    @property
    def AccountLimit(self):
        return self._AccountLimit

    @AccountLimit.setter
    def AccountLimit(self, AccountLimit):
        self._AccountLimit = AccountLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountUsage") is not None:
            self._AccountUsage = UsageInfo()
            self._AccountUsage._deserialize(params.get("AccountUsage"))
        if params.get("AccountLimit") is not None:
            self._AccountLimit = LimitsInfo()
            self._AccountLimit._deserialize(params.get("AccountLimit"))
        self._RequestId = params.get("RequestId")


class GetAliasRequest(AbstractModel):
    """GetAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Name: 别名的名称
        :type Name: str
        :param _Namespace: 函数所在的命名空间
        :type Namespace: str
        """
        self._FunctionName = None
        self._Name = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAliasResponse(AbstractModel):
    """GetAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param _Name: 别名的名称
        :type Name: str
        :param _RoutingConfig: 别名的路由信息
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: 别名的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _ModTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FunctionVersion = None
        self._Name = None
        self._RoutingConfig = None
        self._Description = None
        self._AddTime = None
        self._ModTime = None
        self._RequestId = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        self._Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._RequestId = params.get("RequestId")


class GetAsyncEventStatusRequest(AbstractModel):
    """GetAsyncEventStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokeRequestId: 异步执行请求 id
        :type InvokeRequestId: str
        """
        self._InvokeRequestId = None

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId


    def _deserialize(self, params):
        self._InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAsyncEventStatusResponse(AbstractModel):
    """GetAsyncEventStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 异步事件状态
        :type Result: :class:`tencentcloud.scf.v20180416.models.AsyncEventStatus`
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
            self._Result = AsyncEventStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class GetFunctionAddressRequest(AbstractModel):
    """GetFunctionAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数的名称
        :type FunctionName: str
        :param _Qualifier: 函数的版本
        :type Qualifier: str
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionAddressResponse(AbstractModel):
    """GetFunctionAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 函数的Cos地址
        :type Url: str
        :param _CodeSha256: 函数的SHA256编码
        :type CodeSha256: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._CodeSha256 = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CodeSha256(self):
        return self._CodeSha256

    @CodeSha256.setter
    def CodeSha256(self, CodeSha256):
        self._CodeSha256 = CodeSha256

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._CodeSha256 = params.get("CodeSha256")
        self._RequestId = params.get("RequestId")


class GetFunctionEventInvokeConfigRequest(AbstractModel):
    """GetFunctionEventInvokeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        :param _Qualifier: 函数版本，默认为$LATEST
        :type Qualifier: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionEventInvokeConfigResponse(AbstractModel):
    """GetFunctionEventInvokeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncTriggerConfig: 异步重试配置信息
        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncTriggerConfig = None
        self._RequestId = None

    @property
    def AsyncTriggerConfig(self):
        return self._AsyncTriggerConfig

    @AsyncTriggerConfig.setter
    def AsyncTriggerConfig(self, AsyncTriggerConfig):
        self._AsyncTriggerConfig = AsyncTriggerConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self._AsyncTriggerConfig = AsyncTriggerConfig()
            self._AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self._RequestId = params.get("RequestId")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数的名称。
- 为保证[获取函数运行日志](https://cloud.tencent.com/document/product/583/18583)接口`GetFunctionLogs`兼容性，输入参数`FunctionName`仍为非必填项，但建议填写该参数，否则可能导致日志获取失败。
- 函数关联日志服务后，建议使用[日志服务](https://cloud.tencent.com/document/product/614/16875)相关接口以获得最佳日志检索体验。
        :type FunctionName: str
        :param _Offset: 数据的偏移量，Offset+Limit不能大于10000
        :type Offset: int
        :param _Limit: 返回数据的长度，Offset+Limit不能大于10000
        :type Limit: int
        :param _Order: 以升序还是降序的方式对日志进行排序，可选值 desc和 asc
        :type Order: str
        :param _OrderBy: 根据某个字段排序日志,支持以下字段：function_name, duration, mem_usage, start_time
        :type OrderBy: str
        :param _Filter: 日志过滤条件。可用来区分正确和错误日志，filter.RetCode=not0 表示只返回错误日志，filter.RetCode=is0 表示只返回正确日志，不传，则返回所有日志
        :type Filter: :class:`tencentcloud.scf.v20180416.models.LogFilter`
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        :param _Qualifier: 函数的版本
        :type Qualifier: str
        :param _FunctionRequestId: 执行该函数对应的requestId
        :type FunctionRequestId: str
        :param _StartTime: 查询的具体日期，例如：2017-05-16 20:00:00，只能与endtime相差一天之内
        :type StartTime: str
        :param _EndTime: 查询的具体日期，例如：2017-05-16 20:59:59，只能与startTime相差一天之内
        :type EndTime: str
        :param _SearchContext: 该字段已下线
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        """
        self._FunctionName = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderBy = None
        self._Filter = None
        self._Namespace = None
        self._Qualifier = None
        self._FunctionRequestId = None
        self._StartTime = None
        self._EndTime = None
        self._SearchContext = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def FunctionRequestId(self):
        return self._FunctionRequestId

    @FunctionRequestId.setter
    def FunctionRequestId(self, FunctionRequestId):
        self._FunctionRequestId = FunctionRequestId

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
    def SearchContext(self):
        return self._SearchContext

    @SearchContext.setter
    def SearchContext(self, SearchContext):
        self._SearchContext = SearchContext


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self._Filter = LogFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._FunctionRequestId = params.get("FunctionRequestId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("SearchContext") is not None:
            self._SearchContext = LogSearchContext()
            self._SearchContext._deserialize(params.get("SearchContext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 函数日志的总数
        :type TotalCount: int
        :param _Data: 函数日志信息
        :type Data: list of FunctionLog
        :param _SearchContext: 该字段已下线
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._SearchContext = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SearchContext(self):
        return self._SearchContext

    @SearchContext.setter
    def SearchContext(self, SearchContext):
        self._SearchContext = SearchContext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("SearchContext") is not None:
            self._SearchContext = LogSearchContext()
            self._SearchContext._deserialize(params.get("SearchContext"))
        self._RequestId = params.get("RequestId")


class GetFunctionRequest(AbstractModel):
    """GetFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要获取详情的函数名称，ResourceId和FunctionName只能传一个
        :type FunctionName: str
        :param _Qualifier: 函数的版本号
默认值: $LATEST
        :type Qualifier: str
        :param _Namespace: 函数所属命名空间
默认值: default
        :type Namespace: str
        :param _ShowCode: 是否显示代码, TRUE表示显示代码，FALSE表示不显示代码,大于1M的入口文件不会显示
        :type ShowCode: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Namespace = None
        self._ShowCode = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ShowCode(self):
        return self._ShowCode

    @ShowCode.setter
    def ShowCode(self, ShowCode):
        self._ShowCode = ShowCode


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        self._ShowCode = params.get("ShowCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionResponse(AbstractModel):
    """GetFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModTime: 函数的最后修改时间
        :type ModTime: str
        :param _CodeInfo: 函数的代码
        :type CodeInfo: str
        :param _Description: 函数的描述信息
        :type Description: str
        :param _Triggers: 函数的触发器列表
        :type Triggers: list of Trigger
        :param _Handler: 函数的入口
        :type Handler: str
        :param _CodeSize: 函数代码大小
        :type CodeSize: int
        :param _Timeout: 函数的超时时间
        :type Timeout: int
        :param _FunctionVersion: 函数的版本
        :type FunctionVersion: str
        :param _MemorySize: 函数的最大可用内存
        :type MemorySize: int
        :param _Runtime: 函数的运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param _FunctionName: 函数的名称
        :type FunctionName: str
        :param _VpcConfig: 函数的私有网络
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param _UseGpu: 是否使用GPU
        :type UseGpu: str
        :param _Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param _CodeResult: 代码是否正确
        :type CodeResult: str
        :param _CodeError: 代码错误信息
        :type CodeError: str
        :param _ErrNo: 代码错误码
        :type ErrNo: int
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        :param _Role: 函数绑定的角色
        :type Role: str
        :param _InstallDependency: 是否自动安装依赖
        :type InstallDependency: str
        :param _Status: 函数状态，状态值及流转[参考说明](https://cloud.tencent.com/document/product/583/47175)
        :type Status: str
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _ClsLogsetId: 日志投递到的Cls日志集
        :type ClsLogsetId: str
        :param _ClsTopicId: 日志投递到的Cls Topic
        :type ClsTopicId: str
        :param _FunctionId: 函数ID
        :type FunctionId: str
        :param _Tags: 函数的标签列表
        :type Tags: list of Tag
        :param _EipConfig: EipConfig配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipOutConfig`
        :param _AccessInfo: 域名信息
        :type AccessInfo: :class:`tencentcloud.scf.v20180416.models.AccessInfo`
        :param _Type: 函数类型，取值为HTTP或者Event
        :type Type: str
        :param _L5Enable: 是否启用L5
        :type L5Enable: str
        :param _Layers: 函数关联的Layer版本信息
        :type Layers: list of LayerVersionInfo
        :param _DeadLetterConfig: 函数关联的死信队列信息
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param _AddTime: 函数创建回见
        :type AddTime: str
        :param _PublicNetConfig: 公网访问配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigOut`
        :param _OnsEnable: 是否启用Ons
注意：此字段可能返回 null，表示取不到有效值。
        :type OnsEnable: str
        :param _CfsConfig: 文件系统配置参数，用于云函数挂载文件系统
注意：此字段可能返回 null，表示取不到有效值。
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param _AvailableStatus: 函数的计费状态，状态值[参考此处](https://cloud.tencent.com/document/product/583/47175#.E5.87.BD.E6.95.B0.E8.AE.A1.E8.B4.B9.E7.8A.B6.E6.80.81)
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableStatus: str
        :param _Qualifier: 函数版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Qualifier: str
        :param _InitTimeout: 函数初始化超时时间
        :type InitTimeout: int
        :param _StatusReasons: 函数状态失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReasons: list of StatusReason
        :param _AsyncRunEnable: 是否开启异步属性
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRunEnable: str
        :param _TraceEnable: 是否开启事件追踪
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceEnable: str
        :param _ImageConfig: 镜像配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageConfig: :class:`tencentcloud.scf.v20180416.models.ImageConfig`
        :param _ProtocolType: HTTP函数支持的访问协议。当前支持WebSockets协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: str
        :param _ProtocolParams: HTTP函数配置ProtocolType访问协议，当前协议配置的参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolParams: :class:`tencentcloud.scf.v20180416.models.ProtocolParams`
        :param _DnsCache: 是否开启DNS缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsCache: str
        :param _IntranetConfig: 内网访问配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetConfig: :class:`tencentcloud.scf.v20180416.models.IntranetConfigOut`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModTime = None
        self._CodeInfo = None
        self._Description = None
        self._Triggers = None
        self._Handler = None
        self._CodeSize = None
        self._Timeout = None
        self._FunctionVersion = None
        self._MemorySize = None
        self._Runtime = None
        self._FunctionName = None
        self._VpcConfig = None
        self._UseGpu = None
        self._Environment = None
        self._CodeResult = None
        self._CodeError = None
        self._ErrNo = None
        self._Namespace = None
        self._Role = None
        self._InstallDependency = None
        self._Status = None
        self._StatusDesc = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._FunctionId = None
        self._Tags = None
        self._EipConfig = None
        self._AccessInfo = None
        self._Type = None
        self._L5Enable = None
        self._Layers = None
        self._DeadLetterConfig = None
        self._AddTime = None
        self._PublicNetConfig = None
        self._OnsEnable = None
        self._CfsConfig = None
        self._AvailableStatus = None
        self._Qualifier = None
        self._InitTimeout = None
        self._StatusReasons = None
        self._AsyncRunEnable = None
        self._TraceEnable = None
        self._ImageConfig = None
        self._ProtocolType = None
        self._ProtocolParams = None
        self._DnsCache = None
        self._IntranetConfig = None
        self._RequestId = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def CodeInfo(self):
        return self._CodeInfo

    @CodeInfo.setter
    def CodeInfo(self, CodeInfo):
        self._CodeInfo = CodeInfo

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def Handler(self):
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def CodeSize(self):
        return self._CodeSize

    @CodeSize.setter
    def CodeSize(self, CodeSize):
        self._CodeSize = CodeSize

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def UseGpu(self):
        return self._UseGpu

    @UseGpu.setter
    def UseGpu(self, UseGpu):
        self._UseGpu = UseGpu

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def CodeResult(self):
        return self._CodeResult

    @CodeResult.setter
    def CodeResult(self, CodeResult):
        self._CodeResult = CodeResult

    @property
    def CodeError(self):
        return self._CodeError

    @CodeError.setter
    def CodeError(self, CodeError):
        self._CodeError = CodeError

    @property
    def ErrNo(self):
        return self._ErrNo

    @ErrNo.setter
    def ErrNo(self, ErrNo):
        self._ErrNo = ErrNo

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def InstallDependency(self):
        return self._InstallDependency

    @InstallDependency.setter
    def InstallDependency(self, InstallDependency):
        self._InstallDependency = InstallDependency

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EipConfig(self):
        return self._EipConfig

    @EipConfig.setter
    def EipConfig(self, EipConfig):
        self._EipConfig = EipConfig

    @property
    def AccessInfo(self):
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def L5Enable(self):
        return self._L5Enable

    @L5Enable.setter
    def L5Enable(self, L5Enable):
        self._L5Enable = L5Enable

    @property
    def Layers(self):
        return self._Layers

    @Layers.setter
    def Layers(self, Layers):
        self._Layers = Layers

    @property
    def DeadLetterConfig(self):
        return self._DeadLetterConfig

    @DeadLetterConfig.setter
    def DeadLetterConfig(self, DeadLetterConfig):
        self._DeadLetterConfig = DeadLetterConfig

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def PublicNetConfig(self):
        return self._PublicNetConfig

    @PublicNetConfig.setter
    def PublicNetConfig(self, PublicNetConfig):
        self._PublicNetConfig = PublicNetConfig

    @property
    def OnsEnable(self):
        return self._OnsEnable

    @OnsEnable.setter
    def OnsEnable(self, OnsEnable):
        self._OnsEnable = OnsEnable

    @property
    def CfsConfig(self):
        return self._CfsConfig

    @CfsConfig.setter
    def CfsConfig(self, CfsConfig):
        self._CfsConfig = CfsConfig

    @property
    def AvailableStatus(self):
        return self._AvailableStatus

    @AvailableStatus.setter
    def AvailableStatus(self, AvailableStatus):
        self._AvailableStatus = AvailableStatus

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def InitTimeout(self):
        return self._InitTimeout

    @InitTimeout.setter
    def InitTimeout(self, InitTimeout):
        self._InitTimeout = InitTimeout

    @property
    def StatusReasons(self):
        return self._StatusReasons

    @StatusReasons.setter
    def StatusReasons(self, StatusReasons):
        self._StatusReasons = StatusReasons

    @property
    def AsyncRunEnable(self):
        return self._AsyncRunEnable

    @AsyncRunEnable.setter
    def AsyncRunEnable(self, AsyncRunEnable):
        self._AsyncRunEnable = AsyncRunEnable

    @property
    def TraceEnable(self):
        return self._TraceEnable

    @TraceEnable.setter
    def TraceEnable(self, TraceEnable):
        self._TraceEnable = TraceEnable

    @property
    def ImageConfig(self):
        return self._ImageConfig

    @ImageConfig.setter
    def ImageConfig(self, ImageConfig):
        self._ImageConfig = ImageConfig

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def ProtocolParams(self):
        return self._ProtocolParams

    @ProtocolParams.setter
    def ProtocolParams(self, ProtocolParams):
        self._ProtocolParams = ProtocolParams

    @property
    def DnsCache(self):
        return self._DnsCache

    @DnsCache.setter
    def DnsCache(self, DnsCache):
        self._DnsCache = DnsCache

    @property
    def IntranetConfig(self):
        return self._IntranetConfig

    @IntranetConfig.setter
    def IntranetConfig(self, IntranetConfig):
        self._IntranetConfig = IntranetConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._CodeInfo = params.get("CodeInfo")
        self._Description = params.get("Description")
        if params.get("Triggers") is not None:
            self._Triggers = []
            for item in params.get("Triggers"):
                obj = Trigger()
                obj._deserialize(item)
                self._Triggers.append(obj)
        self._Handler = params.get("Handler")
        self._CodeSize = params.get("CodeSize")
        self._Timeout = params.get("Timeout")
        self._FunctionVersion = params.get("FunctionVersion")
        self._MemorySize = params.get("MemorySize")
        self._Runtime = params.get("Runtime")
        self._FunctionName = params.get("FunctionName")
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._UseGpu = params.get("UseGpu")
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        self._CodeResult = params.get("CodeResult")
        self._CodeError = params.get("CodeError")
        self._ErrNo = params.get("ErrNo")
        self._Namespace = params.get("Namespace")
        self._Role = params.get("Role")
        self._InstallDependency = params.get("InstallDependency")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._FunctionId = params.get("FunctionId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("EipConfig") is not None:
            self._EipConfig = EipOutConfig()
            self._EipConfig._deserialize(params.get("EipConfig"))
        if params.get("AccessInfo") is not None:
            self._AccessInfo = AccessInfo()
            self._AccessInfo._deserialize(params.get("AccessInfo"))
        self._Type = params.get("Type")
        self._L5Enable = params.get("L5Enable")
        if params.get("Layers") is not None:
            self._Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self._Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self._DeadLetterConfig = DeadLetterConfig()
            self._DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        self._AddTime = params.get("AddTime")
        if params.get("PublicNetConfig") is not None:
            self._PublicNetConfig = PublicNetConfigOut()
            self._PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        self._OnsEnable = params.get("OnsEnable")
        if params.get("CfsConfig") is not None:
            self._CfsConfig = CfsConfig()
            self._CfsConfig._deserialize(params.get("CfsConfig"))
        self._AvailableStatus = params.get("AvailableStatus")
        self._Qualifier = params.get("Qualifier")
        self._InitTimeout = params.get("InitTimeout")
        if params.get("StatusReasons") is not None:
            self._StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self._StatusReasons.append(obj)
        self._AsyncRunEnable = params.get("AsyncRunEnable")
        self._TraceEnable = params.get("TraceEnable")
        if params.get("ImageConfig") is not None:
            self._ImageConfig = ImageConfig()
            self._ImageConfig._deserialize(params.get("ImageConfig"))
        self._ProtocolType = params.get("ProtocolType")
        if params.get("ProtocolParams") is not None:
            self._ProtocolParams = ProtocolParams()
            self._ProtocolParams._deserialize(params.get("ProtocolParams"))
        self._DnsCache = params.get("DnsCache")
        if params.get("IntranetConfig") is not None:
            self._IntranetConfig = IntranetConfigOut()
            self._IntranetConfig._deserialize(params.get("IntranetConfig"))
        self._RequestId = params.get("RequestId")


class GetLayerVersionRequest(AbstractModel):
    """GetLayerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LayerName: 层名称
        :type LayerName: str
        :param _LayerVersion: 版本号
        :type LayerVersion: int
        """
        self._LayerName = None
        self._LayerVersion = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLayerVersionResponse(AbstractModel):
    """GetLayerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompatibleRuntimes: 适配的运行时
        :type CompatibleRuntimes: list of str
        :param _CodeSha256: 层中版本文件的SHA256编码
        :type CodeSha256: str
        :param _Location: 层中版本文件的下载地址
        :type Location: str
        :param _AddTime: 版本的创建时间
        :type AddTime: str
        :param _Description: 版本的描述
        :type Description: str
        :param _LicenseInfo: 许可证信息
        :type LicenseInfo: str
        :param _LayerVersion: 版本号
        :type LayerVersion: int
        :param _LayerName: 层名称
        :type LayerName: str
        :param _Status: 层的具体版本当前状态，状态值[参考此处](https://cloud.tencent.com/document/product/583/47175#.E5.B1.82.EF.BC.88layer.EF.BC.89.E7.8A.B6.E6.80.81)
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompatibleRuntimes = None
        self._CodeSha256 = None
        self._Location = None
        self._AddTime = None
        self._Description = None
        self._LicenseInfo = None
        self._LayerVersion = None
        self._LayerName = None
        self._Status = None
        self._RequestId = None

    @property
    def CompatibleRuntimes(self):
        return self._CompatibleRuntimes

    @CompatibleRuntimes.setter
    def CompatibleRuntimes(self, CompatibleRuntimes):
        self._CompatibleRuntimes = CompatibleRuntimes

    @property
    def CodeSha256(self):
        return self._CodeSha256

    @CodeSha256.setter
    def CodeSha256(self, CodeSha256):
        self._CodeSha256 = CodeSha256

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

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
        self._CompatibleRuntimes = params.get("CompatibleRuntimes")
        self._CodeSha256 = params.get("CodeSha256")
        self._Location = params.get("Location")
        self._AddTime = params.get("AddTime")
        self._Description = params.get("Description")
        self._LicenseInfo = params.get("LicenseInfo")
        self._LayerVersion = params.get("LayerVersion")
        self._LayerName = params.get("LayerName")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class GetProvisionedConcurrencyConfigRequest(AbstractModel):
    """GetProvisionedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要获取预置并发详情的函数名称。
        :type FunctionName: str
        :param _Namespace: 函数所在的命名空间，默认为default。
        :type Namespace: str
        :param _Qualifier: 函数版本号，不传则返回函数所有版本的预置并发信息。
        :type Qualifier: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProvisionedConcurrencyConfigResponse(AbstractModel):
    """GetProvisionedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UnallocatedConcurrencyNum: 该函数剩余可配置的预置并发数。
        :type UnallocatedConcurrencyNum: int
        :param _Allocated: 函数已预置的并发配置详情。
        :type Allocated: list of VersionProvisionedConcurrencyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UnallocatedConcurrencyNum = None
        self._Allocated = None
        self._RequestId = None

    @property
    def UnallocatedConcurrencyNum(self):
        return self._UnallocatedConcurrencyNum

    @UnallocatedConcurrencyNum.setter
    def UnallocatedConcurrencyNum(self, UnallocatedConcurrencyNum):
        self._UnallocatedConcurrencyNum = UnallocatedConcurrencyNum

    @property
    def Allocated(self):
        return self._Allocated

    @Allocated.setter
    def Allocated(self, Allocated):
        self._Allocated = Allocated

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UnallocatedConcurrencyNum = params.get("UnallocatedConcurrencyNum")
        if params.get("Allocated") is not None:
            self._Allocated = []
            for item in params.get("Allocated"):
                obj = VersionProvisionedConcurrencyInfo()
                obj._deserialize(item)
                self._Allocated.append(obj)
        self._RequestId = params.get("RequestId")


class GetRequestStatusRequest(AbstractModel):
    """GetRequestStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _FunctionRequestId: 需要查询状态的请求 id
        :type FunctionRequestId: str
        :param _Namespace: 函数的所在的命名空间
        :type Namespace: str
        :param _StartTime: 查询的开始时间，例如：2017-05-16 20:00:00，不填默认为当前时间 - 15min
        :type StartTime: str
        :param _EndTime: 查询的结束时间，例如：2017-05-16 20:59:59。StartTime 为空时，EndTime 默认为当前时间；StartTime 有值时，需要同时传 EndTime。EndTime 需要晚于 StartTime。
        :type EndTime: str
        """
        self._FunctionName = None
        self._FunctionRequestId = None
        self._Namespace = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionRequestId(self):
        return self._FunctionRequestId

    @FunctionRequestId.setter
    def FunctionRequestId(self, FunctionRequestId):
        self._FunctionRequestId = FunctionRequestId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
        self._FunctionName = params.get("FunctionName")
        self._FunctionRequestId = params.get("FunctionRequestId")
        self._Namespace = params.get("Namespace")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestStatusResponse(AbstractModel):
    """GetRequestStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 函数运行状态的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 函数运行状态数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RequestStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RequestStatus()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class GetReservedConcurrencyConfigRequest(AbstractModel):
    """GetReservedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要获取最大独占配额详情的函数名称。
        :type FunctionName: str
        :param _Namespace: 函数所在的命名空间，默认为default。
        :type Namespace: str
        """
        self._FunctionName = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReservedConcurrencyConfigResponse(AbstractModel):
    """GetReservedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReservedMem: 该函数的最大独占配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMem: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReservedMem = None
        self._RequestId = None

    @property
    def ReservedMem(self):
        return self._ReservedMem

    @ReservedMem.setter
    def ReservedMem(self, ReservedMem):
        self._ReservedMem = ReservedMem

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReservedMem = params.get("ReservedMem")
        self._RequestId = params.get("RequestId")


class ImageConfig(AbstractModel):
    """TCR镜像信息描述

    """

    def __init__(self):
        r"""
        :param _ImageType: 镜像仓库类型，个人版或者企业版：personal/enterprise
        :type ImageType: str
        :param _ImageUri: {domain}/{namespace}/{imageName}:{tag}@{digest}
        :type ImageUri: str
        :param _RegistryId: 用于企业版TCR获取镜像拉取临时凭证，ImageType为"enterprise"时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param _EntryPoint: 参数已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryPoint: str
        :param _Command: 容器的启动命令。该参数为可选参数，如果不填写，则默认使用 Dockerfile 中的 Entrypoint。传入规范，填写可运行的指令，例如 python
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        :param _Args: 容器的启动参数。该参数为可选参数，如果不填写，则默认使用 Dockerfile 中的 CMD。传入规范，以“空格”作为参数的分割标识，例如 -u app.py
注意：此字段可能返回 null，表示取不到有效值。
        :type Args: str
        :param _ContainerImageAccelerate: 镜像加速开关，默认False
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerImageAccelerate: bool
        :param _ImagePort: 镜像函数端口设置
默认值: 9000
-1: 无端口镜像函数
其他: 取值范围 0 ~ 65535
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePort: int
        """
        self._ImageType = None
        self._ImageUri = None
        self._RegistryId = None
        self._EntryPoint = None
        self._Command = None
        self._Args = None
        self._ContainerImageAccelerate = None
        self._ImagePort = None

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageUri(self):
        return self._ImageUri

    @ImageUri.setter
    def ImageUri(self, ImageUri):
        self._ImageUri = ImageUri

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def EntryPoint(self):
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def ContainerImageAccelerate(self):
        return self._ContainerImageAccelerate

    @ContainerImageAccelerate.setter
    def ContainerImageAccelerate(self, ContainerImageAccelerate):
        self._ContainerImageAccelerate = ContainerImageAccelerate

    @property
    def ImagePort(self):
        return self._ImagePort

    @ImagePort.setter
    def ImagePort(self, ImagePort):
        self._ImagePort = ImagePort


    def _deserialize(self, params):
        self._ImageType = params.get("ImageType")
        self._ImageUri = params.get("ImageUri")
        self._RegistryId = params.get("RegistryId")
        self._EntryPoint = params.get("EntryPoint")
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        self._ContainerImageAccelerate = params.get("ContainerImageAccelerate")
        self._ImagePort = params.get("ImagePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConcurrencyConfig(AbstractModel):
    """多并发执行配置描述

    """

    def __init__(self):
        r"""
        :param _DynamicEnabled: 是否开启智能动态并发。'FALSE'时是静态并发。''时取消多并发配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicEnabled: str
        :param _MaxConcurrency: 单实例并发数最大值。取值范围 [1,100]
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConcurrency: int
        """
        self._DynamicEnabled = None
        self._MaxConcurrency = None

    @property
    def DynamicEnabled(self):
        return self._DynamicEnabled

    @DynamicEnabled.setter
    def DynamicEnabled(self, DynamicEnabled):
        self._DynamicEnabled = DynamicEnabled

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency


    def _deserialize(self, params):
        self._DynamicEnabled = params.get("DynamicEnabled")
        self._MaxConcurrency = params.get("MaxConcurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntranetConfigIn(AbstractModel):
    """内网配置

    """

    def __init__(self):
        r"""
        :param _IpFixed: 是否开启固定内网IP
ENABLE 为开启
DISABLE 为不开启

        :type IpFixed: str
        """
        self._IpFixed = None

    @property
    def IpFixed(self):
        return self._IpFixed

    @IpFixed.setter
    def IpFixed(self, IpFixed):
        self._IpFixed = IpFixed


    def _deserialize(self, params):
        self._IpFixed = params.get("IpFixed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntranetConfigOut(AbstractModel):
    """内网配置

    """

    def __init__(self):
        r"""
        :param _IpFixed: 是否启用固定内网IP
ENABLE 为启用
DISABLE 为不启用
        :type IpFixed: str
        :param _IpAddress: 若已启用固定内网IP，则该字段返回使用的IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: list of str
        """
        self._IpFixed = None
        self._IpAddress = None

    @property
    def IpFixed(self):
        return self._IpFixed

    @IpFixed.setter
    def IpFixed(self, IpFixed):
        self._IpFixed = IpFixed

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress


    def _deserialize(self, params):
        self._IpFixed = params.get("IpFixed")
        self._IpAddress = params.get("IpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionRequest(AbstractModel):
    """InvokeFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Qualifier: 触发函数的版本号或别名，默认值为$DEFAULT
        :type Qualifier: str
        :param _Event: 运行函数时的参数，以json格式传入，最大支持的参数长度是 6MB。该字段信息对应函数 [event 入参](https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E)。
        :type Event: str
        :param _LogType: 返回值会包含4KB的日志，可选值为None和Tail，默认值为None。当该值为Tail时，返回参数中的Log字段会包含对应的函数执行日志
        :type LogType: str
        :param _Namespace: 命名空间，不填默认为 default
        :type Namespace: str
        :param _RoutingKey: 函数灰度流量控制调用，以json格式传入，例如{"k":"v"}，注意kv都需要是字符串类型，最大支持的参数长度是1024字节
        :type RoutingKey: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Event = None
        self._LogType = None
        self._Namespace = None
        self._RoutingKey = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Event(self):
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingKey(self):
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Event = params.get("Event")
        self._LogType = params.get("LogType")
        self._Namespace = params.get("Namespace")
        self._RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionResponse(AbstractModel):
    """InvokeFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 函数执行结果
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
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
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _InvocationType: 同步调用请使用[同步 Invoke 调用接口](https://cloud.tencent.com/document/product/583/58400) 或填写同步调用参数 RequestResponse ，建议使用同步调用接口以获取最佳性能；异步调用填写 Event；默认为同步。接口超时时间为 300s，更长超时时间请使用异步调用。
        :type InvocationType: str
        :param _Qualifier: 触发函数的版本号或别名，默认值为 $LATEST
        :type Qualifier: str
        :param _ClientContext: 运行函数时的参数，以json格式传入，同步调用最大支持 6MB，异步调用最大支持 128 KB。该字段信息对应函数 [event 入参](https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E)。
        :type ClientContext: str
        :param _LogType: 异步调用该字段返回为空。
        :type LogType: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _RoutingKey: 函数灰度流量控制调用，以json格式传入，例如{"k":"v"}，注意kv都需要是字符串类型，最大支持的参数长度是1024字节
        :type RoutingKey: str
        """
        self._FunctionName = None
        self._InvocationType = None
        self._Qualifier = None
        self._ClientContext = None
        self._LogType = None
        self._Namespace = None
        self._RoutingKey = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def InvocationType(self):
        return self._InvocationType

    @InvocationType.setter
    def InvocationType(self, InvocationType):
        self._InvocationType = InvocationType

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def ClientContext(self):
        return self._ClientContext

    @ClientContext.setter
    def ClientContext(self, ClientContext):
        self._ClientContext = ClientContext

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingKey(self):
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._InvocationType = params.get("InvocationType")
        self._Qualifier = params.get("Qualifier")
        self._ClientContext = params.get("ClientContext")
        self._LogType = params.get("LogType")
        self._Namespace = params.get("Namespace")
        self._RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeResponse(AbstractModel):
    """Invoke返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 函数执行结果
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
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
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class K8SLabel(AbstractModel):
    """k8s label

    """

    def __init__(self):
        r"""
        :param _Key: label的名称
        :type Key: str
        :param _Value: label的值
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
        


class K8SToleration(AbstractModel):
    """Kubernetes污点容忍，使用时请注意您的Kubernetes版本所支持的字段情况。
    可参考 https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/taint-and-toleration/

    """

    def __init__(self):
        r"""
        :param _Key: 匹配的污点名
        :type Key: str
        :param _Operator: 匹配方式，默认值为: Equal
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Effect: 执行策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Effect: str
        :param _Value: 匹配的污点值，当Operator为Equal时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _TolerationSeconds: 当污点不被容忍时，Pod还能在节点上运行多久
注意：此字段可能返回 null，表示取不到有效值。
        :type TolerationSeconds: int
        """
        self._Key = None
        self._Operator = None
        self._Effect = None
        self._Value = None
        self._TolerationSeconds = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TolerationSeconds(self):
        return self._TolerationSeconds

    @TolerationSeconds.setter
    def TolerationSeconds(self, TolerationSeconds):
        self._TolerationSeconds = TolerationSeconds


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Effect = params.get("Effect")
        self._Value = params.get("Value")
        self._TolerationSeconds = params.get("TolerationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayerVersionInfo(AbstractModel):
    """层版本信息

    """

    def __init__(self):
        r"""
        :param _CompatibleRuntimes: 版本适用的运行时
注意：此字段可能返回 null，表示取不到有效值。
        :type CompatibleRuntimes: list of str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _Description: 版本描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _LicenseInfo: 许可证信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseInfo: str
        :param _LayerVersion: 版本号
        :type LayerVersion: int
        :param _LayerName: 层名称
        :type LayerName: str
        :param _Status: 层的具体版本当前状态，状态值[参考此处](https://cloud.tencent.com/document/product/583/47175#.E5.B1.82.EF.BC.88layer.EF.BC.89.E7.8A.B6.E6.80.81)
        :type Status: str
        :param _Stamp: Stamp
注意：此字段可能返回 null，表示取不到有效值。
        :type Stamp: str
        """
        self._CompatibleRuntimes = None
        self._AddTime = None
        self._Description = None
        self._LicenseInfo = None
        self._LayerVersion = None
        self._LayerName = None
        self._Status = None
        self._Stamp = None

    @property
    def CompatibleRuntimes(self):
        return self._CompatibleRuntimes

    @CompatibleRuntimes.setter
    def CompatibleRuntimes(self, CompatibleRuntimes):
        self._CompatibleRuntimes = CompatibleRuntimes

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Stamp(self):
        return self._Stamp

    @Stamp.setter
    def Stamp(self, Stamp):
        self._Stamp = Stamp


    def _deserialize(self, params):
        self._CompatibleRuntimes = params.get("CompatibleRuntimes")
        self._AddTime = params.get("AddTime")
        self._Description = params.get("Description")
        self._LicenseInfo = params.get("LicenseInfo")
        self._LayerVersion = params.get("LayerVersion")
        self._LayerName = params.get("LayerName")
        self._Status = params.get("Status")
        self._Stamp = params.get("Stamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayerVersionSimple(AbstractModel):
    """指定某个Layer版本

    """

    def __init__(self):
        r"""
        :param _LayerName: 绑定的层名称。解绑层需传递空字符串。
        :type LayerName: str
        :param _LayerVersion: 绑定或解绑层的版本号。解绑函数版本关联的最后一个层版本时，LayerVersion 填 0。
        :type LayerVersion: int
        """
        self._LayerName = None
        self._LayerVersion = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitsInfo(AbstractModel):
    """限制信息

    """

    def __init__(self):
        r"""
        :param _NamespacesCount: 命名空间个数限制
        :type NamespacesCount: int
        :param _Namespace: 命名空间限制信息
        :type Namespace: list of NamespaceLimit
        """
        self._NamespacesCount = None
        self._Namespace = None

    @property
    def NamespacesCount(self):
        return self._NamespacesCount

    @NamespacesCount.setter
    def NamespacesCount(self, NamespacesCount):
        self._NamespacesCount = NamespacesCount

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self._Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceLimit()
                obj._deserialize(item)
                self._Namespace.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesRequest(AbstractModel):
    """ListAliases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Namespace: 函数所在的命名空间
        :type Namespace: str
        :param _FunctionVersion: 如果提供此参数，则只返回与该函数版本有关联的别名
        :type FunctionVersion: str
        :param _Offset: 数据偏移量，默认值为 0
        :type Offset: str
        :param _Limit: 返回数据长度，默认值为 20
        :type Limit: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._FunctionVersion = None
        self._Offset = None
        self._Limit = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

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
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._FunctionVersion = params.get("FunctionVersion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesResponse(AbstractModel):
    """ListAliases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Aliases: 别名列表
        :type Aliases: list of Alias
        :param _TotalCount: 别名总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Aliases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Aliases(self):
        return self._Aliases

    @Aliases.setter
    def Aliases(self, Aliases):
        self._Aliases = Aliases

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
        if params.get("Aliases") is not None:
            self._Aliases = []
            for item in params.get("Aliases"):
                obj = Alias()
                obj._deserialize(item)
                self._Aliases.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListAsyncEventsRequest(AbstractModel):
    """ListAsyncEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Qualifier: 过滤条件，函数版本
        :type Qualifier: str
        :param _InvokeType: 过滤条件，调用类型列表
        :type InvokeType: list of str
        :param _Status: 过滤条件，事件状态列表
        :type Status: list of str
        :param _StartTimeInterval: 过滤条件，开始执行时间左闭右开区间
        :type StartTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`
        :param _EndTimeInterval: 过滤条件，结束执行时间左闭右开区间
        :type EndTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`
        :param _Order: 可选值 ASC 和 DESC，默认 DESC
        :type Order: str
        :param _Orderby: 可选值 StartTime 和 EndTime，默认值 StartTime
        :type Orderby: str
        :param _Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param _Limit: 返回数据长度，默认值为 20，最大值 100
        :type Limit: int
        :param _InvokeRequestId: 过滤条件，事件调用请求id
        :type InvokeRequestId: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None
        self._InvokeType = None
        self._Status = None
        self._StartTimeInterval = None
        self._EndTimeInterval = None
        self._Order = None
        self._Orderby = None
        self._Offset = None
        self._Limit = None
        self._InvokeRequestId = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def InvokeType(self):
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTimeInterval(self):
        return self._StartTimeInterval

    @StartTimeInterval.setter
    def StartTimeInterval(self, StartTimeInterval):
        self._StartTimeInterval = StartTimeInterval

    @property
    def EndTimeInterval(self):
        return self._EndTimeInterval

    @EndTimeInterval.setter
    def EndTimeInterval(self, EndTimeInterval):
        self._EndTimeInterval = EndTimeInterval

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Orderby(self):
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

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
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._InvokeType = params.get("InvokeType")
        self._Status = params.get("Status")
        if params.get("StartTimeInterval") is not None:
            self._StartTimeInterval = TimeInterval()
            self._StartTimeInterval._deserialize(params.get("StartTimeInterval"))
        if params.get("EndTimeInterval") is not None:
            self._EndTimeInterval = TimeInterval()
            self._EndTimeInterval._deserialize(params.get("EndTimeInterval"))
        self._Order = params.get("Order")
        self._Orderby = params.get("Orderby")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAsyncEventsResponse(AbstractModel):
    """ListAsyncEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的事件总数
        :type TotalCount: int
        :param _EventList: 异步事件列表
        :type EventList: list of AsyncEvent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EventList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = AsyncEvent()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._RequestId = params.get("RequestId")


class ListFunctionsRequest(AbstractModel):
    """ListFunctions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param _Orderby: 根据哪个字段进行返回结果排序,支持以下字段：AddTime, ModTime, FunctionName
        :type Orderby: str
        :param _Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param _Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param _SearchKey: 支持FunctionName模糊匹配
        :type SearchKey: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Description: 函数描述，支持模糊搜索
        :type Description: str
        :param _Filters: 过滤条件。
- tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        """
        self._Order = None
        self._Orderby = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._Namespace = None
        self._Description = None
        self._Filters = None

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Orderby(self):
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Order = params.get("Order")
        self._Orderby = params.get("Orderby")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
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
        


class ListFunctionsResponse(AbstractModel):
    """ListFunctions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Functions: 函数列表
        :type Functions: list of Function
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Functions = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

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
        if params.get("Functions") is not None:
            self._Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self._Functions.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListLayerVersionsRequest(AbstractModel):
    """ListLayerVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LayerName: 层名称
        :type LayerName: str
        :param _CompatibleRuntime: 适配的运行时
        :type CompatibleRuntime: list of str
        """
        self._LayerName = None
        self._CompatibleRuntime = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def CompatibleRuntime(self):
        return self._CompatibleRuntime

    @CompatibleRuntime.setter
    def CompatibleRuntime(self, CompatibleRuntime):
        self._CompatibleRuntime = CompatibleRuntime


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._CompatibleRuntime = params.get("CompatibleRuntime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayerVersionsResponse(AbstractModel):
    """ListLayerVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LayerVersions: 层版本列表
        :type LayerVersions: list of LayerVersionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LayerVersions = None
        self._RequestId = None

    @property
    def LayerVersions(self):
        return self._LayerVersions

    @LayerVersions.setter
    def LayerVersions(self, LayerVersions):
        self._LayerVersions = LayerVersions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LayerVersions") is not None:
            self._LayerVersions = []
            for item in params.get("LayerVersions"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self._LayerVersions.append(obj)
        self._RequestId = params.get("RequestId")


class ListLayersRequest(AbstractModel):
    """ListLayers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompatibleRuntime: 适配的运行时
        :type CompatibleRuntime: str
        :param _Offset: 偏移位置
        :type Offset: int
        :param _Limit: 查询数目限制
        :type Limit: int
        :param _SearchKey: 查询key，模糊匹配名称
        :type SearchKey: str
        """
        self._CompatibleRuntime = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def CompatibleRuntime(self):
        return self._CompatibleRuntime

    @CompatibleRuntime.setter
    def CompatibleRuntime(self, CompatibleRuntime):
        self._CompatibleRuntime = CompatibleRuntime

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._CompatibleRuntime = params.get("CompatibleRuntime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayersResponse(AbstractModel):
    """ListLayers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Layers: 层列表
        :type Layers: list of LayerVersionInfo
        :param _TotalCount: 层总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Layers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Layers(self):
        return self._Layers

    @Layers.setter
    def Layers(self, Layers):
        self._Layers = Layers

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
        if params.get("Layers") is not None:
            self._Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self._Layers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListNamespacesRequest(AbstractModel):
    """ListNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param _Offset: 数据的偏移量，默认值为 0
        :type Offset: int
        :param _Orderby: 根据哪个字段进行返回结果排序,支持以下字段：Name,Updatetime
        :type Orderby: str
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param _SearchKey: 关键字匹配搜索，Key 可选值为 Namespace 和 Description，多个搜索条件之间是与的关系
        :type SearchKey: list of SearchKey
        """
        self._Limit = None
        self._Offset = None
        self._Orderby = None
        self._Order = None
        self._SearchKey = None

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
    def Orderby(self):
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Orderby = params.get("Orderby")
        self._Order = params.get("Order")
        if params.get("SearchKey") is not None:
            self._SearchKey = []
            for item in params.get("SearchKey"):
                obj = SearchKey()
                obj._deserialize(item)
                self._SearchKey.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListNamespacesResponse(AbstractModel):
    """ListNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespaces: namespace详情
        :type Namespaces: list of Namespace
        :param _TotalCount: 返回的namespace数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Namespaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

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
        if params.get("Namespaces") is not None:
            self._Namespaces = []
            for item in params.get("Namespaces"):
                obj = Namespace()
                obj._deserialize(item)
                self._Namespaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListTriggersRequest(AbstractModel):
    """ListTriggers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Namespace: 命名空间，默认是default
        :type Namespace: str
        :param _Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param _Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param _OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：add_time，mod_time，默认mod_time
        :type OrderBy: str
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC，默认DESC
        :type Order: str
        :param _Filters: * Qualifier: 函数版本，别名
* TriggerName: 函数触发器名称
* Description: 函数触发器描述
        :type Filters: list of Filter
        """
        self._FunctionName = None
        self._Namespace = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._Order = None
        self._Filters = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._Order = params.get("Order")
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
        


class ListTriggersResponse(AbstractModel):
    """ListTriggers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 触发器总数
        :type TotalCount: int
        :param _Triggers: 触发器列表
        :type Triggers: list of TriggerInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Triggers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self._Triggers = []
            for item in params.get("Triggers"):
                obj = TriggerInfo()
                obj._deserialize(item)
                self._Triggers.append(obj)
        self._RequestId = params.get("RequestId")


class ListVersionByFunctionRequest(AbstractModel):
    """ListVersionByFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名
        :type FunctionName: str
        :param _Namespace: 函数所在命名空间
        :type Namespace: str
        :param _Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param _Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param _OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime, ModTime
        :type OrderBy: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderBy = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVersionByFunctionResponse(AbstractModel):
    """ListVersionByFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: 函数版本。
        :type FunctionVersion: list of str
        :param _Versions: 函数版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of FunctionVersion
        :param _TotalCount: 函数版本总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FunctionVersion = None
        self._Versions = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

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
        self._FunctionVersion = params.get("FunctionVersion")
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = FunctionVersion()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """日志过滤条件，用于区分正确与错误日志

    """

    def __init__(self):
        r"""
        :param _RetCode: filter.RetCode的取值有：
not0 表示只返回错误日志，
is0 表示只返回正确日志，
TimeLimitExceeded 返回函数调用发生超时的日志，
ResourceLimitExceeded 返回函数调用发生资源超限的日志，
UserCodeException 返回函数调用发生用户代码错误的日志，
无输入则返回所有日志。
        :type RetCode: str
        """
        self._RetCode = None

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSearchContext(AbstractModel):
    """日志搜索上下文

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: str
        :param _Limit: 日志条数
        :type Limit: int
        :param _Keyword: 日志关键词
        :type Keyword: str
        :param _Type: 日志类型，支持Application和Platform，默认为Application
        :type Type: str
        """
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Type = None

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
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Namespace(AbstractModel):
    """命名空间

    """

    def __init__(self):
        r"""
        :param _ModTime: 命名空间创建时间
        :type ModTime: str
        :param _AddTime: 命名空间修改时间
        :type AddTime: str
        :param _Description: 命名空间描述
        :type Description: str
        :param _Name: 命名空间名称
        :type Name: str
        :param _Type: 默认default，TCB表示是小程序云开发创建的
        :type Type: str
        """
        self._ModTime = None
        self._AddTime = None
        self._Description = None
        self._Name = None
        self._Type = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._AddTime = params.get("AddTime")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceLimit(AbstractModel):
    """命名空间限制

    """

    def __init__(self):
        r"""
        :param _FunctionsCount: 函数总数
        :type FunctionsCount: int
        :param _Trigger: Trigger信息
        :type Trigger: :class:`tencentcloud.scf.v20180416.models.TriggerCount`
        :param _Namespace: Namespace名称
        :type Namespace: str
        :param _ConcurrentExecutions: 并发量
        :type ConcurrentExecutions: int
        :param _TimeoutLimit: Timeout限制
        :type TimeoutLimit: int
        :param _TestModelLimit: 测试事件限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TestModelLimit: int
        :param _InitTimeoutLimit: 初始化超时限制
        :type InitTimeoutLimit: int
        :param _RetryNumLimit: 异步重试次数限制
        :type RetryNumLimit: int
        :param _MinMsgTTL: 异步重试消息保留时间下限
        :type MinMsgTTL: int
        :param _MaxMsgTTL: 异步重试消息保留时间上限
        :type MaxMsgTTL: int
        """
        self._FunctionsCount = None
        self._Trigger = None
        self._Namespace = None
        self._ConcurrentExecutions = None
        self._TimeoutLimit = None
        self._TestModelLimit = None
        self._InitTimeoutLimit = None
        self._RetryNumLimit = None
        self._MinMsgTTL = None
        self._MaxMsgTTL = None

    @property
    def FunctionsCount(self):
        return self._FunctionsCount

    @FunctionsCount.setter
    def FunctionsCount(self, FunctionsCount):
        self._FunctionsCount = FunctionsCount

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ConcurrentExecutions(self):
        return self._ConcurrentExecutions

    @ConcurrentExecutions.setter
    def ConcurrentExecutions(self, ConcurrentExecutions):
        self._ConcurrentExecutions = ConcurrentExecutions

    @property
    def TimeoutLimit(self):
        return self._TimeoutLimit

    @TimeoutLimit.setter
    def TimeoutLimit(self, TimeoutLimit):
        self._TimeoutLimit = TimeoutLimit

    @property
    def TestModelLimit(self):
        return self._TestModelLimit

    @TestModelLimit.setter
    def TestModelLimit(self, TestModelLimit):
        self._TestModelLimit = TestModelLimit

    @property
    def InitTimeoutLimit(self):
        return self._InitTimeoutLimit

    @InitTimeoutLimit.setter
    def InitTimeoutLimit(self, InitTimeoutLimit):
        self._InitTimeoutLimit = InitTimeoutLimit

    @property
    def RetryNumLimit(self):
        return self._RetryNumLimit

    @RetryNumLimit.setter
    def RetryNumLimit(self, RetryNumLimit):
        self._RetryNumLimit = RetryNumLimit

    @property
    def MinMsgTTL(self):
        return self._MinMsgTTL

    @MinMsgTTL.setter
    def MinMsgTTL(self, MinMsgTTL):
        self._MinMsgTTL = MinMsgTTL

    @property
    def MaxMsgTTL(self):
        return self._MaxMsgTTL

    @MaxMsgTTL.setter
    def MaxMsgTTL(self, MaxMsgTTL):
        self._MaxMsgTTL = MaxMsgTTL


    def _deserialize(self, params):
        self._FunctionsCount = params.get("FunctionsCount")
        if params.get("Trigger") is not None:
            self._Trigger = TriggerCount()
            self._Trigger._deserialize(params.get("Trigger"))
        self._Namespace = params.get("Namespace")
        self._ConcurrentExecutions = params.get("ConcurrentExecutions")
        self._TimeoutLimit = params.get("TimeoutLimit")
        self._TestModelLimit = params.get("TestModelLimit")
        self._InitTimeoutLimit = params.get("InitTimeoutLimit")
        self._RetryNumLimit = params.get("RetryNumLimit")
        self._MinMsgTTL = params.get("MinMsgTTL")
        self._MaxMsgTTL = params.get("MaxMsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceResourceEnv(AbstractModel):
    """命名空间资源池配置

    """

    def __init__(self):
        r"""
        :param _TKE: 基于TKE集群的资源池
注意：此字段可能返回 null，表示取不到有效值。
        :type TKE: :class:`tencentcloud.scf.v20180416.models.NamespaceResourceEnvTKE`
        """
        self._TKE = None

    @property
    def TKE(self):
        return self._TKE

    @TKE.setter
    def TKE(self, TKE):
        self._TKE = TKE


    def _deserialize(self, params):
        if params.get("TKE") is not None:
            self._TKE = NamespaceResourceEnvTKE()
            self._TKE._deserialize(params.get("TKE"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceResourceEnvTKE(AbstractModel):
    """基于TKE的资源池选项

    """

    def __init__(self):
        r"""
        :param _ClusterID: 集群ID
        :type ClusterID: str
        :param _SubnetID: 子网ID
        :type SubnetID: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _DataPath: 数据存储地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DataPath: str
        :param _NodeSelector: node选择器
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSelector: list of K8SLabel
        :param _Tolerations: 污点容忍
注意：此字段可能返回 null，表示取不到有效值。
        :type Tolerations: list of K8SToleration
        :param _Port: scf组件将占用的节点端口起始号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _PodTemplatePatch: yaml格式的pod patch内容，例如
metadata:
  labels:
    key: value
注意：此字段可能返回 null，表示取不到有效值。
        :type PodTemplatePatch: str
        """
        self._ClusterID = None
        self._SubnetID = None
        self._Namespace = None
        self._DataPath = None
        self._NodeSelector = None
        self._Tolerations = None
        self._Port = None
        self._PodTemplatePatch = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def SubnetID(self):
        return self._SubnetID

    @SubnetID.setter
    def SubnetID(self, SubnetID):
        self._SubnetID = SubnetID

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def DataPath(self):
        return self._DataPath

    @DataPath.setter
    def DataPath(self, DataPath):
        self._DataPath = DataPath

    @property
    def NodeSelector(self):
        return self._NodeSelector

    @NodeSelector.setter
    def NodeSelector(self, NodeSelector):
        self._NodeSelector = NodeSelector

    @property
    def Tolerations(self):
        return self._Tolerations

    @Tolerations.setter
    def Tolerations(self, Tolerations):
        self._Tolerations = Tolerations

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def PodTemplatePatch(self):
        return self._PodTemplatePatch

    @PodTemplatePatch.setter
    def PodTemplatePatch(self, PodTemplatePatch):
        self._PodTemplatePatch = PodTemplatePatch


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._SubnetID = params.get("SubnetID")
        self._Namespace = params.get("Namespace")
        self._DataPath = params.get("DataPath")
        if params.get("NodeSelector") is not None:
            self._NodeSelector = []
            for item in params.get("NodeSelector"):
                obj = K8SLabel()
                obj._deserialize(item)
                self._NodeSelector.append(obj)
        if params.get("Tolerations") is not None:
            self._Tolerations = []
            for item in params.get("Tolerations"):
                obj = K8SToleration()
                obj._deserialize(item)
                self._Tolerations.append(obj)
        self._Port = params.get("Port")
        self._PodTemplatePatch = params.get("PodTemplatePatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceUsage(AbstractModel):
    """名称空间已使用信息

    """

    def __init__(self):
        r"""
        :param _Functions: 函数数组
        :type Functions: list of str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _FunctionsCount: 命名空间函数个数
        :type FunctionsCount: int
        :param _TotalConcurrencyMem: 命名空间配额总量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalConcurrencyMem: int
        :param _TotalAllocatedConcurrencyMem: 命名空间并发使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAllocatedConcurrencyMem: int
        :param _TotalAllocatedProvisionedMem: 命名空间预置使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAllocatedProvisionedMem: int
        """
        self._Functions = None
        self._Namespace = None
        self._FunctionsCount = None
        self._TotalConcurrencyMem = None
        self._TotalAllocatedConcurrencyMem = None
        self._TotalAllocatedProvisionedMem = None

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def FunctionsCount(self):
        return self._FunctionsCount

    @FunctionsCount.setter
    def FunctionsCount(self, FunctionsCount):
        self._FunctionsCount = FunctionsCount

    @property
    def TotalConcurrencyMem(self):
        return self._TotalConcurrencyMem

    @TotalConcurrencyMem.setter
    def TotalConcurrencyMem(self, TotalConcurrencyMem):
        self._TotalConcurrencyMem = TotalConcurrencyMem

    @property
    def TotalAllocatedConcurrencyMem(self):
        return self._TotalAllocatedConcurrencyMem

    @TotalAllocatedConcurrencyMem.setter
    def TotalAllocatedConcurrencyMem(self, TotalAllocatedConcurrencyMem):
        self._TotalAllocatedConcurrencyMem = TotalAllocatedConcurrencyMem

    @property
    def TotalAllocatedProvisionedMem(self):
        return self._TotalAllocatedProvisionedMem

    @TotalAllocatedProvisionedMem.setter
    def TotalAllocatedProvisionedMem(self, TotalAllocatedProvisionedMem):
        self._TotalAllocatedProvisionedMem = TotalAllocatedProvisionedMem


    def _deserialize(self, params):
        self._Functions = params.get("Functions")
        self._Namespace = params.get("Namespace")
        self._FunctionsCount = params.get("FunctionsCount")
        self._TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self._TotalAllocatedConcurrencyMem = params.get("TotalAllocatedConcurrencyMem")
        self._TotalAllocatedProvisionedMem = params.get("TotalAllocatedProvisionedMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolParams(AbstractModel):
    """HTTP函数支持其他访问协议的参数

    """

    def __init__(self):
        r"""
        :param _WSParams: WebSockets协议支持的参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WSParams: :class:`tencentcloud.scf.v20180416.models.WSParams`
        """
        self._WSParams = None

    @property
    def WSParams(self):
        return self._WSParams

    @WSParams.setter
    def WSParams(self, WSParams):
        self._WSParams = WSParams


    def _deserialize(self, params):
        if params.get("WSParams") is not None:
            self._WSParams = WSParams()
            self._WSParams._deserialize(params.get("WSParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetConfigIn(AbstractModel):
    """公网访问配置

    """

    def __init__(self):
        r"""
        :param _PublicNetStatus: 是否开启公网访问能力取值['DISABLE','ENABLE']
        :type PublicNetStatus: str
        :param _EipConfig: Eip配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigIn`
        """
        self._PublicNetStatus = None
        self._EipConfig = None

    @property
    def PublicNetStatus(self):
        return self._PublicNetStatus

    @PublicNetStatus.setter
    def PublicNetStatus(self, PublicNetStatus):
        self._PublicNetStatus = PublicNetStatus

    @property
    def EipConfig(self):
        return self._EipConfig

    @EipConfig.setter
    def EipConfig(self, EipConfig):
        self._EipConfig = EipConfig


    def _deserialize(self, params):
        self._PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self._EipConfig = EipConfigIn()
            self._EipConfig._deserialize(params.get("EipConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetConfigOut(AbstractModel):
    """公网访问配置

    """

    def __init__(self):
        r"""
        :param _PublicNetStatus: 是否开启公网访问能力取值['DISABLE','ENABLE']
        :type PublicNetStatus: str
        :param _EipConfig: Eip配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigOut`
        """
        self._PublicNetStatus = None
        self._EipConfig = None

    @property
    def PublicNetStatus(self):
        return self._PublicNetStatus

    @PublicNetStatus.setter
    def PublicNetStatus(self, PublicNetStatus):
        self._PublicNetStatus = PublicNetStatus

    @property
    def EipConfig(self):
        return self._EipConfig

    @EipConfig.setter
    def EipConfig(self, EipConfig):
        self._EipConfig = EipConfig


    def _deserialize(self, params):
        self._PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self._EipConfig = EipConfigOut()
            self._EipConfig._deserialize(params.get("EipConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionRequest(AbstractModel):
    """PublishLayerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LayerName: 层名称，支持26个英文字母大小写、数字、连接符和下划线，第一个字符只能以字母开头，最后一个字符不能为连接符或者下划线，名称长度1-64
        :type LayerName: str
        :param _CompatibleRuntimes: 层适用的运行时，可多选，可选的值对应函数的 Runtime 可选值。
        :type CompatibleRuntimes: list of str
        :param _Content: 层的文件来源或文件内容
        :type Content: :class:`tencentcloud.scf.v20180416.models.Code`
        :param _Description: 层的版本的描述
        :type Description: str
        :param _LicenseInfo: 层的软件许可证
        :type LicenseInfo: str
        """
        self._LayerName = None
        self._CompatibleRuntimes = None
        self._Content = None
        self._Description = None
        self._LicenseInfo = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def CompatibleRuntimes(self):
        return self._CompatibleRuntimes

    @CompatibleRuntimes.setter
    def CompatibleRuntimes(self, CompatibleRuntimes):
        self._CompatibleRuntimes = CompatibleRuntimes

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._CompatibleRuntimes = params.get("CompatibleRuntimes")
        if params.get("Content") is not None:
            self._Content = Code()
            self._Content._deserialize(params.get("Content"))
        self._Description = params.get("Description")
        self._LicenseInfo = params.get("LicenseInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionResponse(AbstractModel):
    """PublishLayerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LayerVersion: 本次创建的层的版本号
        :type LayerVersion: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LayerVersion = None
        self._RequestId = None

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LayerVersion = params.get("LayerVersion")
        self._RequestId = params.get("RequestId")


class PublishVersionRequest(AbstractModel):
    """PublishVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 发布函数的名称
        :type FunctionName: str
        :param _Description: 函数的描述
        :type Description: str
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        """
        self._FunctionName = None
        self._Description = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Description = params.get("Description")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishVersionResponse(AbstractModel):
    """PublishVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: 函数的版本
        :type FunctionVersion: str
        :param _CodeSize: 代码大小
        :type CodeSize: int
        :param _MemorySize: 最大可用内存
        :type MemorySize: int
        :param _Description: 函数的描述
        :type Description: str
        :param _Handler: 函数的入口
        :type Handler: str
        :param _Timeout: 函数的超时时间
        :type Timeout: int
        :param _Runtime: 函数的运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FunctionVersion = None
        self._CodeSize = None
        self._MemorySize = None
        self._Description = None
        self._Handler = None
        self._Timeout = None
        self._Runtime = None
        self._Namespace = None
        self._RequestId = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def CodeSize(self):
        return self._CodeSize

    @CodeSize.setter
    def CodeSize(self, CodeSize):
        self._CodeSize = CodeSize

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Handler(self):
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        self._CodeSize = params.get("CodeSize")
        self._MemorySize = params.get("MemorySize")
        self._Description = params.get("Description")
        self._Handler = params.get("Handler")
        self._Timeout = params.get("Timeout")
        self._Runtime = params.get("Runtime")
        self._Namespace = params.get("Namespace")
        self._RequestId = params.get("RequestId")


class PutProvisionedConcurrencyConfigRequest(AbstractModel):
    """PutProvisionedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要设置预置并发的函数的名称
        :type FunctionName: str
        :param _Qualifier: 函数的版本号，注：$LATEST版本不支持预置并发
        :type Qualifier: str
        :param _VersionProvisionedConcurrencyNum: 预置并发数量，注：所有版本的预置并发数总和存在上限限制，当前的上限是：函数最大并发配额 - 100
        :type VersionProvisionedConcurrencyNum: int
        :param _Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        :param _TriggerActions: 定时预置任务
        :type TriggerActions: list of TriggerAction
        :param _ProvisionedType: 预置类型，
静态预置：Default
动态追踪并发利用率指标预置：ConcurrencyUtilizationTracking
预置类型二选一，设置静态预置时可以设置VersionProvisionedConcurrencyNum。

动态利用率预置可以设置TrackingTarget，MinCapacity，MaxCapacity，保持向后兼容性此时VersionProvisionedConcurrencyNum设置为0.
        :type ProvisionedType: str
        :param _TrackingTarget: 指标追踪的并发利用率。设置范围(0,1)
        :type TrackingTarget: float
        :param _MinCapacity: 缩容时的最小值, 最小值为1
        :type MinCapacity: int
        :param _MaxCapacity: 扩容时的最大值
        :type MaxCapacity: int
        """
        self._FunctionName = None
        self._Qualifier = None
        self._VersionProvisionedConcurrencyNum = None
        self._Namespace = None
        self._TriggerActions = None
        self._ProvisionedType = None
        self._TrackingTarget = None
        self._MinCapacity = None
        self._MaxCapacity = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def VersionProvisionedConcurrencyNum(self):
        return self._VersionProvisionedConcurrencyNum

    @VersionProvisionedConcurrencyNum.setter
    def VersionProvisionedConcurrencyNum(self, VersionProvisionedConcurrencyNum):
        self._VersionProvisionedConcurrencyNum = VersionProvisionedConcurrencyNum

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerActions(self):
        return self._TriggerActions

    @TriggerActions.setter
    def TriggerActions(self, TriggerActions):
        self._TriggerActions = TriggerActions

    @property
    def ProvisionedType(self):
        return self._ProvisionedType

    @ProvisionedType.setter
    def ProvisionedType(self, ProvisionedType):
        self._ProvisionedType = ProvisionedType

    @property
    def TrackingTarget(self):
        return self._TrackingTarget

    @TrackingTarget.setter
    def TrackingTarget(self, TrackingTarget):
        self._TrackingTarget = TrackingTarget

    @property
    def MinCapacity(self):
        return self._MinCapacity

    @MinCapacity.setter
    def MinCapacity(self, MinCapacity):
        self._MinCapacity = MinCapacity

    @property
    def MaxCapacity(self):
        return self._MaxCapacity

    @MaxCapacity.setter
    def MaxCapacity(self, MaxCapacity):
        self._MaxCapacity = MaxCapacity


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._VersionProvisionedConcurrencyNum = params.get("VersionProvisionedConcurrencyNum")
        self._Namespace = params.get("Namespace")
        if params.get("TriggerActions") is not None:
            self._TriggerActions = []
            for item in params.get("TriggerActions"):
                obj = TriggerAction()
                obj._deserialize(item)
                self._TriggerActions.append(obj)
        self._ProvisionedType = params.get("ProvisionedType")
        self._TrackingTarget = params.get("TrackingTarget")
        self._MinCapacity = params.get("MinCapacity")
        self._MaxCapacity = params.get("MaxCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutProvisionedConcurrencyConfigResponse(AbstractModel):
    """PutProvisionedConcurrencyConfig返回参数结构体

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


class PutReservedConcurrencyConfigRequest(AbstractModel):
    """PutReservedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 需要设置最大独占配额的函数的名称
        :type FunctionName: str
        :param _ReservedConcurrencyMem: 函数最大独占配额，注：函数的最大独占配额内存总和上限：用户总并发内存配额 - 12800
        :type ReservedConcurrencyMem: int
        :param _Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self._FunctionName = None
        self._ReservedConcurrencyMem = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def ReservedConcurrencyMem(self):
        return self._ReservedConcurrencyMem

    @ReservedConcurrencyMem.setter
    def ReservedConcurrencyMem(self, ReservedConcurrencyMem):
        self._ReservedConcurrencyMem = ReservedConcurrencyMem

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutReservedConcurrencyConfigResponse(AbstractModel):
    """PutReservedConcurrencyConfig返回参数结构体

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


class PutTotalConcurrencyConfigRequest(AbstractModel):
    """PutTotalConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalConcurrencyMem: 账号并发内存配额，注：账号并发内存配额下限：用户已用并发内存总额 + 12800
        :type TotalConcurrencyMem: int
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        """
        self._TotalConcurrencyMem = None
        self._Namespace = None

    @property
    def TotalConcurrencyMem(self):
        return self._TotalConcurrencyMem

    @TotalConcurrencyMem.setter
    def TotalConcurrencyMem(self, TotalConcurrencyMem):
        self._TotalConcurrencyMem = TotalConcurrencyMem

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTotalConcurrencyConfigResponse(AbstractModel):
    """PutTotalConcurrencyConfig返回参数结构体

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


class RequestStatus(AbstractModel):
    """函数运行状态

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数的名称
        :type FunctionName: str
        :param _RetMsg: 函数执行完成后的返回值
        :type RetMsg: str
        :param _RequestId: 查询的请求 id
        :type RequestId: str
        :param _StartTime: 请求开始时间
        :type StartTime: str
        :param _RetCode: 请求执行结果， 0 表示执行成功，1表示运行中，-1 表示执行异常。
        :type RetCode: int
        :param _Duration: 请求运行耗时，单位：ms
        :type Duration: float
        :param _MemUsage: 请求消耗内存，单位为 MB
        :type MemUsage: float
        :param _RetryNum: 重试次数
        :type RetryNum: int
        """
        self._FunctionName = None
        self._RetMsg = None
        self._RequestId = None
        self._StartTime = None
        self._RetCode = None
        self._Duration = None
        self._MemUsage = None
        self._RetryNum = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def MemUsage(self):
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def RetryNum(self):
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")
        self._StartTime = params.get("StartTime")
        self._RetCode = params.get("RetCode")
        self._Duration = params.get("Duration")
        self._MemUsage = params.get("MemUsage")
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Result(AbstractModel):
    """运行函数的返回

    """

    def __init__(self):
        r"""
        :param _Log: 表示执行过程中的日志输出，异步调用返回为空
        :type Log: str
        :param _RetMsg: 表示执行函数的返回，异步调用返回为空
        :type RetMsg: str
        :param _ErrMsg: 表示执行函数的错误返回信息，异步调用返回为空
        :type ErrMsg: str
        :param _MemUsage: 执行函数时的内存大小，单位为Byte，异步调用返回为空
        :type MemUsage: int
        :param _Duration: 表示执行函数的耗时，单位是毫秒，异步调用返回为空
        :type Duration: float
        :param _BillDuration: 表示函数的计费耗时，单位是毫秒，异步调用返回为空
        :type BillDuration: int
        :param _FunctionRequestId: 此次函数执行的Id
        :type FunctionRequestId: str
        :param _InvokeResult: 请求 Invoke 接口，该参数已弃用。请求 InvokeFunction 接口，该参数值为请求执行[状态码](https://cloud.tencent.com/document/product/583/42611)。
        :type InvokeResult: int
        """
        self._Log = None
        self._RetMsg = None
        self._ErrMsg = None
        self._MemUsage = None
        self._Duration = None
        self._BillDuration = None
        self._FunctionRequestId = None
        self._InvokeResult = None

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def MemUsage(self):
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def BillDuration(self):
        return self._BillDuration

    @BillDuration.setter
    def BillDuration(self, BillDuration):
        self._BillDuration = BillDuration

    @property
    def FunctionRequestId(self):
        return self._FunctionRequestId

    @FunctionRequestId.setter
    def FunctionRequestId(self, FunctionRequestId):
        self._FunctionRequestId = FunctionRequestId

    @property
    def InvokeResult(self):
        return self._InvokeResult

    @InvokeResult.setter
    def InvokeResult(self, InvokeResult):
        self._InvokeResult = InvokeResult


    def _deserialize(self, params):
        self._Log = params.get("Log")
        self._RetMsg = params.get("RetMsg")
        self._ErrMsg = params.get("ErrMsg")
        self._MemUsage = params.get("MemUsage")
        self._Duration = params.get("Duration")
        self._BillDuration = params.get("BillDuration")
        self._FunctionRequestId = params.get("FunctionRequestId")
        self._InvokeResult = params.get("InvokeResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryConfig(AbstractModel):
    """异步重试配置

    """

    def __init__(self):
        r"""
        :param _RetryNum: 重试次数
        :type RetryNum: int
        """
        self._RetryNum = None

    @property
    def RetryNum(self):
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


    def _deserialize(self, params):
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingConfig(AbstractModel):
    """别名的版本路由配置
    其中：随机权重路由附加版本和规则路由附加版本不可以同时配置

    """

    def __init__(self):
        r"""
        :param _AdditionalVersionWeights: 随机权重路由附加版本
        :type AdditionalVersionWeights: list of VersionWeight
        :param _AddtionVersionMatchs: 规则路由附加版本
        :type AddtionVersionMatchs: list of VersionMatch
        """
        self._AdditionalVersionWeights = None
        self._AddtionVersionMatchs = None

    @property
    def AdditionalVersionWeights(self):
        return self._AdditionalVersionWeights

    @AdditionalVersionWeights.setter
    def AdditionalVersionWeights(self, AdditionalVersionWeights):
        self._AdditionalVersionWeights = AdditionalVersionWeights

    @property
    def AddtionVersionMatchs(self):
        return self._AddtionVersionMatchs

    @AddtionVersionMatchs.setter
    def AddtionVersionMatchs(self, AddtionVersionMatchs):
        self._AddtionVersionMatchs = AddtionVersionMatchs


    def _deserialize(self, params):
        if params.get("AdditionalVersionWeights") is not None:
            self._AdditionalVersionWeights = []
            for item in params.get("AdditionalVersionWeights"):
                obj = VersionWeight()
                obj._deserialize(item)
                self._AdditionalVersionWeights.append(obj)
        if params.get("AddtionVersionMatchs") is not None:
            self._AddtionVersionMatchs = []
            for item in params.get("AddtionVersionMatchs"):
                obj = VersionMatch()
                obj._deserialize(item)
                self._AddtionVersionMatchs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKey(AbstractModel):
    """包含搜索关键字和对应的内容

    """

    def __init__(self):
        r"""
        :param _Key: 搜索关键字
        :type Key: str
        :param _Value: 搜索内容
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
        


class StatusReason(AbstractModel):
    """状态原因描述

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _ErrorMessage: 错误描述
        :type ErrorMessage: str
        """
        self._ErrorCode = None
        self._ErrorMessage = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """函数标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签的key
        :type Key: str
        :param _Value: 标签的value
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
        


class TerminateAsyncEventRequest(AbstractModel):
    """TerminateAsyncEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _InvokeRequestId: 终止的调用请求id
        :type InvokeRequestId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _GraceShutdown: true，向指定请求[发送 SIGTERM 终止信号](https://cloud.tencent.com/document/product/583/63969#.E5.8F.91.E9.80.81.E7.BB.88.E6.AD.A2.E4.BF.A1.E5.8F.B7]， ，默认值为 false。
        :type GraceShutdown: bool
        """
        self._FunctionName = None
        self._InvokeRequestId = None
        self._Namespace = None
        self._GraceShutdown = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def GraceShutdown(self):
        return self._GraceShutdown

    @GraceShutdown.setter
    def GraceShutdown(self, GraceShutdown):
        self._GraceShutdown = GraceShutdown


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._InvokeRequestId = params.get("InvokeRequestId")
        self._Namespace = params.get("Namespace")
        self._GraceShutdown = params.get("GraceShutdown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateAsyncEventResponse(AbstractModel):
    """TerminateAsyncEvent返回参数结构体

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


class TimeInterval(AbstractModel):
    """左闭右开时间区间，包括起始时间和结束时间，格式为"%Y-%m-%d %H:%M:%S"

    """

    def __init__(self):
        r"""
        :param _Start: 起始时间（包括在内），格式"%Y-%m-%d %H:%M:%S"
        :type Start: str
        :param _End: 结束时间（不包括在内），格式"%Y-%m-%d %H:%M:%S"
        :type End: str
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trigger(AbstractModel):
    """触发器类型

    """

    def __init__(self):
        r"""
        :param _ModTime: 触发器最后修改时间
        :type ModTime: str
        :param _Type: 触发器类型
        :type Type: str
        :param _TriggerDesc: 触发器详细配置
        :type TriggerDesc: str
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        :param _AddTime: 触发器创建时间
        :type AddTime: str
        :param _Enable: 使能开关
        :type Enable: int
        :param _CustomArgument: 客户自定义参数
        :type CustomArgument: str
        :param _AvailableStatus: 触发器状态
        :type AvailableStatus: str
        :param _ResourceId: 触发器最小资源ID
        :type ResourceId: str
        :param _BindStatus: 触发器和云函数绑定状态
        :type BindStatus: str
        :param _TriggerAttribute: 触发器类型，双向表示两侧控制台均可操作，单向表示SCF控制台单向创建
        :type TriggerAttribute: str
        :param _Qualifier: 触发器绑定的别名或版本
        :type Qualifier: str
        :param _Description: 触发器描述
        :type Description: str
        """
        self._ModTime = None
        self._Type = None
        self._TriggerDesc = None
        self._TriggerName = None
        self._AddTime = None
        self._Enable = None
        self._CustomArgument = None
        self._AvailableStatus = None
        self._ResourceId = None
        self._BindStatus = None
        self._TriggerAttribute = None
        self._Qualifier = None
        self._Description = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument

    @property
    def AvailableStatus(self):
        return self._AvailableStatus

    @AvailableStatus.setter
    def AvailableStatus(self, AvailableStatus):
        self._AvailableStatus = AvailableStatus

    @property
    def ResourceId(self):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        self._ResourceId = ResourceId

    @property
    def BindStatus(self):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        self._BindStatus = BindStatus

    @property
    def TriggerAttribute(self):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        return self._TriggerAttribute

    @TriggerAttribute.setter
    def TriggerAttribute(self, TriggerAttribute):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        self._TriggerAttribute = TriggerAttribute

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._Type = params.get("Type")
        self._TriggerDesc = params.get("TriggerDesc")
        self._TriggerName = params.get("TriggerName")
        self._AddTime = params.get("AddTime")
        self._Enable = params.get("Enable")
        self._CustomArgument = params.get("CustomArgument")
        self._AvailableStatus = params.get("AvailableStatus")
        self._ResourceId = params.get("ResourceId")
        self._BindStatus = params.get("BindStatus")
        self._TriggerAttribute = params.get("TriggerAttribute")
        self._Qualifier = params.get("Qualifier")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAction(AbstractModel):
    """预置定时任务动作

    """

    def __init__(self):
        r"""
        :param _TriggerName: 定时预置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param _TriggerProvisionedConcurrencyNum: 定时预置并发数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerProvisionedConcurrencyNum: int
        :param _TriggerCronConfig: 设置定时触发器的时间配置，cron表达式。Cron 表达式有七个必需字段，按空格分隔。
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerCronConfig: str
        :param _ProvisionedType: 预置类型 Default
注意：此字段可能返回 null，表示取不到有效值。
        :type ProvisionedType: str
        """
        self._TriggerName = None
        self._TriggerProvisionedConcurrencyNum = None
        self._TriggerCronConfig = None
        self._ProvisionedType = None

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def TriggerProvisionedConcurrencyNum(self):
        return self._TriggerProvisionedConcurrencyNum

    @TriggerProvisionedConcurrencyNum.setter
    def TriggerProvisionedConcurrencyNum(self, TriggerProvisionedConcurrencyNum):
        self._TriggerProvisionedConcurrencyNum = TriggerProvisionedConcurrencyNum

    @property
    def TriggerCronConfig(self):
        return self._TriggerCronConfig

    @TriggerCronConfig.setter
    def TriggerCronConfig(self, TriggerCronConfig):
        self._TriggerCronConfig = TriggerCronConfig

    @property
    def ProvisionedType(self):
        return self._ProvisionedType

    @ProvisionedType.setter
    def ProvisionedType(self, ProvisionedType):
        self._ProvisionedType = ProvisionedType


    def _deserialize(self, params):
        self._TriggerName = params.get("TriggerName")
        self._TriggerProvisionedConcurrencyNum = params.get("TriggerProvisionedConcurrencyNum")
        self._TriggerCronConfig = params.get("TriggerCronConfig")
        self._ProvisionedType = params.get("ProvisionedType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerCount(AbstractModel):
    """TriggerCount描述不同类型触发器的数量

    """

    def __init__(self):
        r"""
        :param _Cos: Cos触发器数量
        :type Cos: int
        :param _Timer: Timer触发器数量
        :type Timer: int
        :param _Cmq: Cmq触发器数量
        :type Cmq: int
        :param _Total: 触发器总数
        :type Total: int
        :param _Ckafka: Ckafka触发器数量
        :type Ckafka: int
        :param _Apigw: Apigw触发器数量
        :type Apigw: int
        :param _Cls: Cls触发器数量
        :type Cls: int
        :param _Clb: Clb触发器数量
        :type Clb: int
        :param _Mps: Mps触发器数量
        :type Mps: int
        :param _Cm: Cm触发器数量
        :type Cm: int
        :param _Vod: Vod触发器数量
        :type Vod: int
        :param _Eb: Eb触发器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Eb: int
        """
        self._Cos = None
        self._Timer = None
        self._Cmq = None
        self._Total = None
        self._Ckafka = None
        self._Apigw = None
        self._Cls = None
        self._Clb = None
        self._Mps = None
        self._Cm = None
        self._Vod = None
        self._Eb = None

    @property
    def Cos(self):
        return self._Cos

    @Cos.setter
    def Cos(self, Cos):
        self._Cos = Cos

    @property
    def Timer(self):
        return self._Timer

    @Timer.setter
    def Timer(self, Timer):
        self._Timer = Timer

    @property
    def Cmq(self):
        return self._Cmq

    @Cmq.setter
    def Cmq(self, Cmq):
        self._Cmq = Cmq

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Apigw(self):
        return self._Apigw

    @Apigw.setter
    def Apigw(self, Apigw):
        self._Apigw = Apigw

    @property
    def Cls(self):
        return self._Cls

    @Cls.setter
    def Cls(self, Cls):
        self._Cls = Cls

    @property
    def Clb(self):
        return self._Clb

    @Clb.setter
    def Clb(self, Clb):
        self._Clb = Clb

    @property
    def Mps(self):
        return self._Mps

    @Mps.setter
    def Mps(self, Mps):
        self._Mps = Mps

    @property
    def Cm(self):
        return self._Cm

    @Cm.setter
    def Cm(self, Cm):
        self._Cm = Cm

    @property
    def Vod(self):
        return self._Vod

    @Vod.setter
    def Vod(self, Vod):
        self._Vod = Vod

    @property
    def Eb(self):
        return self._Eb

    @Eb.setter
    def Eb(self, Eb):
        self._Eb = Eb


    def _deserialize(self, params):
        self._Cos = params.get("Cos")
        self._Timer = params.get("Timer")
        self._Cmq = params.get("Cmq")
        self._Total = params.get("Total")
        self._Ckafka = params.get("Ckafka")
        self._Apigw = params.get("Apigw")
        self._Cls = params.get("Cls")
        self._Clb = params.get("Clb")
        self._Mps = params.get("Mps")
        self._Cm = params.get("Cm")
        self._Vod = params.get("Vod")
        self._Eb = params.get("Eb")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInfo(AbstractModel):
    """触发器信息

    """

    def __init__(self):
        r"""
        :param _Enable: 使能开关
        :type Enable: int
        :param _Qualifier: 函数版本或别名
        :type Qualifier: str
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        :param _Type: 触发器类型
        :type Type: str
        :param _TriggerDesc: 触发器详细配置
        :type TriggerDesc: str
        :param _AvailableStatus: 触发器是否可用
        :type AvailableStatus: str
        :param _CustomArgument: 客户自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomArgument: str
        :param _AddTime: 触发器创建时间
        :type AddTime: str
        :param _ModTime: 触发器最后修改时间
        :type ModTime: str
        :param _ResourceId: 触发器最小资源ID
        :type ResourceId: str
        :param _BindStatus: 触发器和云函数绑定状态
        :type BindStatus: str
        :param _TriggerAttribute: 触发器类型，双向表示两侧控制台均可操作，单向表示SCF控制台单向创建
        :type TriggerAttribute: str
        :param _Description: 客户自定义触发器描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Enable = None
        self._Qualifier = None
        self._TriggerName = None
        self._Type = None
        self._TriggerDesc = None
        self._AvailableStatus = None
        self._CustomArgument = None
        self._AddTime = None
        self._ModTime = None
        self._ResourceId = None
        self._BindStatus = None
        self._TriggerAttribute = None
        self._Description = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def AvailableStatus(self):
        return self._AvailableStatus

    @AvailableStatus.setter
    def AvailableStatus(self, AvailableStatus):
        self._AvailableStatus = AvailableStatus

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def ResourceId(self):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        self._ResourceId = ResourceId

    @property
    def BindStatus(self):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        self._BindStatus = BindStatus

    @property
    def TriggerAttribute(self):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        return self._TriggerAttribute

    @TriggerAttribute.setter
    def TriggerAttribute(self, TriggerAttribute):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        self._TriggerAttribute = TriggerAttribute

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Qualifier = params.get("Qualifier")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._TriggerDesc = params.get("TriggerDesc")
        self._AvailableStatus = params.get("AvailableStatus")
        self._CustomArgument = params.get("CustomArgument")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._ResourceId = params.get("ResourceId")
        self._BindStatus = params.get("BindStatus")
        self._TriggerAttribute = params.get("TriggerAttribute")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Name: 别名的名称
        :type Name: str
        :param _FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param _Namespace: 函数所在的命名空间
        :type Namespace: str
        :param _RoutingConfig: 别名的路由信息，需要为别名指定附加版本时，必须提供此参数；	  附加版本指的是：除主版本 FunctionVersion 外，为此别名再指定一个函数可正常使用的版本；   这里附加版本中的 Version 值 不能是别名指向的主版本；  要注意的是：如果想要某个版本的流量全部指向这个别名，不需配置此参数； 目前一个别名最多只能指定一个附加版本
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: 别名的描述
        :type Description: str
        """
        self._FunctionName = None
        self._Name = None
        self._FunctionVersion = None
        self._Namespace = None
        self._RoutingConfig = None
        self._Description = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Name = params.get("Name")
        self._FunctionVersion = params.get("FunctionVersion")
        self._Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

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


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 要修改的函数名称
        :type FunctionName: str
        :param _Handler: 函数处理方法名称。名称格式支持“文件名称.函数名称”形式（java 名称格式 包名.类名::方法名），文件名称和函数名称之间以"."隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求 2-60 个字符
        :type Handler: str
        :param _CosBucketName: 对象存储桶名称
        :type CosBucketName: str
        :param _CosObjectName: 对象存储对象路径
        :type CosObjectName: str
        :param _ZipFile: 包含函数代码文件及其依赖项的 zip 格式文件，使用该接口时要求将 zip 文件的内容转成 base64 编码，最大支持20M
        :type ZipFile: str
        :param _Namespace: 函数所属命名空间
        :type Namespace: str
        :param _CosBucketRegion: 对象存储的地域，注：北京分为ap-beijing和ap-beijing-1
        :type CosBucketRegion: str
        :param _InstallDependency: 是否自动安装依赖
        :type InstallDependency: str
        :param _EnvId: 函数所属环境
        :type EnvId: str
        :param _Publish: 在更新时是否同步发布新版本，默认为：FALSE，不发布
        :type Publish: str
        :param _Code: 函数代码
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param _CodeSource: 代码来源方式，支持 ZipFile, Cos, Inline 之一
        :type CodeSource: str
        """
        self._FunctionName = None
        self._Handler = None
        self._CosBucketName = None
        self._CosObjectName = None
        self._ZipFile = None
        self._Namespace = None
        self._CosBucketRegion = None
        self._InstallDependency = None
        self._EnvId = None
        self._Publish = None
        self._Code = None
        self._CodeSource = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Handler(self):
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CosObjectName(self):
        return self._CosObjectName

    @CosObjectName.setter
    def CosObjectName(self, CosObjectName):
        self._CosObjectName = CosObjectName

    @property
    def ZipFile(self):
        return self._ZipFile

    @ZipFile.setter
    def ZipFile(self, ZipFile):
        self._ZipFile = ZipFile

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CosBucketRegion(self):
        return self._CosBucketRegion

    @CosBucketRegion.setter
    def CosBucketRegion(self, CosBucketRegion):
        self._CosBucketRegion = CosBucketRegion

    @property
    def InstallDependency(self):
        return self._InstallDependency

    @InstallDependency.setter
    def InstallDependency(self, InstallDependency):
        self._InstallDependency = InstallDependency

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Publish(self):
        return self._Publish

    @Publish.setter
    def Publish(self, Publish):
        self._Publish = Publish

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeSource(self):
        return self._CodeSource

    @CodeSource.setter
    def CodeSource(self, CodeSource):
        self._CodeSource = CodeSource


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Handler = params.get("Handler")
        self._CosBucketName = params.get("CosBucketName")
        self._CosObjectName = params.get("CosObjectName")
        self._ZipFile = params.get("ZipFile")
        self._Namespace = params.get("Namespace")
        self._CosBucketRegion = params.get("CosBucketRegion")
        self._InstallDependency = params.get("InstallDependency")
        self._EnvId = params.get("EnvId")
        self._Publish = params.get("Publish")
        if params.get("Code") is not None:
            self._Code = Code()
            self._Code._deserialize(params.get("Code"))
        self._CodeSource = params.get("CodeSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode返回参数结构体

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


class UpdateFunctionConfigurationRequest(AbstractModel):
    """UpdateFunctionConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 要修改的函数名称
        :type FunctionName: str
        :param _Description: 函数描述。最大支持 1000 个英文字母、数字、空格、逗号和英文句号，支持中文
        :type Description: str
        :param _MemorySize: 函数运行时内存大小，默认为 128 M，可选范64M、128 M-3072 M，以 128MB 为阶梯。
        :type MemorySize: int
        :param _Timeout: 函数最长执行时间，单位为秒，可选值范 1-900 秒，默认为 3 秒
        :type Timeout: int
        :param _Runtime: 函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10，Nodejs8.9，Nodejs10.15，Nodejs12.16， PHP5， PHP7，Go1 ， Java8和CustomRuntime
        :type Runtime: str
        :param _Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param _Namespace: 函数所属命名空间
默认值: default
        :type Namespace: str
        :param _VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param _Role: 函数绑定的角色
        :type Role: str
        :param _InstallDependency: [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)，TRUE 表示安装，默认值为 FALSE。仅支持 Node.js 函数。
        :type InstallDependency: str
        :param _ClsLogsetId: 日志投递到的cls日志集ID
        :type ClsLogsetId: str
        :param _ClsTopicId: 日志投递到的cls Topic ID
        :type ClsTopicId: str
        :param _Publish: 在更新时是否同步发布新版本，默认为：FALSE，不发布新版本
        :type Publish: str
        :param _L5Enable: 是否开启L5访问能力，TRUE 为开启，FALSE为关闭
        :type L5Enable: str
        :param _Layers: 函数要关联的层版本列表，层的版本会按照在列表中顺序依次覆盖。
        :type Layers: list of LayerVersionSimple
        :param _DeadLetterConfig: 函数关联的死信队列信息
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param _PublicNetConfig: 公网访问配置
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`
        :param _CfsConfig: 文件系统配置入参，用于云函数绑定CFS文件系统
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param _InitTimeout: 函数初始化执行超时时间
        :type InitTimeout: int
        :param _ProtocolParams: HTTP函数配置ProtocolType访问协议，当前协议可配置的参数
        :type ProtocolParams: :class:`tencentcloud.scf.v20180416.models.ProtocolParams`
        :param _InstanceConcurrencyConfig: 单实例多并发配置。只支持Web函数。
        :type InstanceConcurrencyConfig: :class:`tencentcloud.scf.v20180416.models.InstanceConcurrencyConfig`
        :param _DnsCache: 是否开启Dns缓存能力。只支持EVENT函数。默认为FALSE，TRUE 为开启，FALSE为关闭
        :type DnsCache: str
        :param _IntranetConfig: 内网访问配置
        :type IntranetConfig: :class:`tencentcloud.scf.v20180416.models.IntranetConfigIn`
        :param _IgnoreSysLog: 忽略系统日志上报
        :type IgnoreSysLog: bool
        """
        self._FunctionName = None
        self._Description = None
        self._MemorySize = None
        self._Timeout = None
        self._Runtime = None
        self._Environment = None
        self._Namespace = None
        self._VpcConfig = None
        self._Role = None
        self._InstallDependency = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._Publish = None
        self._L5Enable = None
        self._Layers = None
        self._DeadLetterConfig = None
        self._PublicNetConfig = None
        self._CfsConfig = None
        self._InitTimeout = None
        self._ProtocolParams = None
        self._InstanceConcurrencyConfig = None
        self._DnsCache = None
        self._IntranetConfig = None
        self._IgnoreSysLog = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def InstallDependency(self):
        return self._InstallDependency

    @InstallDependency.setter
    def InstallDependency(self, InstallDependency):
        self._InstallDependency = InstallDependency

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def Publish(self):
        return self._Publish

    @Publish.setter
    def Publish(self, Publish):
        self._Publish = Publish

    @property
    def L5Enable(self):
        return self._L5Enable

    @L5Enable.setter
    def L5Enable(self, L5Enable):
        self._L5Enable = L5Enable

    @property
    def Layers(self):
        return self._Layers

    @Layers.setter
    def Layers(self, Layers):
        self._Layers = Layers

    @property
    def DeadLetterConfig(self):
        return self._DeadLetterConfig

    @DeadLetterConfig.setter
    def DeadLetterConfig(self, DeadLetterConfig):
        self._DeadLetterConfig = DeadLetterConfig

    @property
    def PublicNetConfig(self):
        return self._PublicNetConfig

    @PublicNetConfig.setter
    def PublicNetConfig(self, PublicNetConfig):
        self._PublicNetConfig = PublicNetConfig

    @property
    def CfsConfig(self):
        return self._CfsConfig

    @CfsConfig.setter
    def CfsConfig(self, CfsConfig):
        self._CfsConfig = CfsConfig

    @property
    def InitTimeout(self):
        return self._InitTimeout

    @InitTimeout.setter
    def InitTimeout(self, InitTimeout):
        self._InitTimeout = InitTimeout

    @property
    def ProtocolParams(self):
        return self._ProtocolParams

    @ProtocolParams.setter
    def ProtocolParams(self, ProtocolParams):
        self._ProtocolParams = ProtocolParams

    @property
    def InstanceConcurrencyConfig(self):
        return self._InstanceConcurrencyConfig

    @InstanceConcurrencyConfig.setter
    def InstanceConcurrencyConfig(self, InstanceConcurrencyConfig):
        self._InstanceConcurrencyConfig = InstanceConcurrencyConfig

    @property
    def DnsCache(self):
        return self._DnsCache

    @DnsCache.setter
    def DnsCache(self, DnsCache):
        self._DnsCache = DnsCache

    @property
    def IntranetConfig(self):
        return self._IntranetConfig

    @IntranetConfig.setter
    def IntranetConfig(self, IntranetConfig):
        self._IntranetConfig = IntranetConfig

    @property
    def IgnoreSysLog(self):
        return self._IgnoreSysLog

    @IgnoreSysLog.setter
    def IgnoreSysLog(self, IgnoreSysLog):
        self._IgnoreSysLog = IgnoreSysLog


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Description = params.get("Description")
        self._MemorySize = params.get("MemorySize")
        self._Timeout = params.get("Timeout")
        self._Runtime = params.get("Runtime")
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        self._Namespace = params.get("Namespace")
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._Role = params.get("Role")
        self._InstallDependency = params.get("InstallDependency")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._Publish = params.get("Publish")
        self._L5Enable = params.get("L5Enable")
        if params.get("Layers") is not None:
            self._Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionSimple()
                obj._deserialize(item)
                self._Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self._DeadLetterConfig = DeadLetterConfig()
            self._DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        if params.get("PublicNetConfig") is not None:
            self._PublicNetConfig = PublicNetConfigIn()
            self._PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        if params.get("CfsConfig") is not None:
            self._CfsConfig = CfsConfig()
            self._CfsConfig._deserialize(params.get("CfsConfig"))
        self._InitTimeout = params.get("InitTimeout")
        if params.get("ProtocolParams") is not None:
            self._ProtocolParams = ProtocolParams()
            self._ProtocolParams._deserialize(params.get("ProtocolParams"))
        if params.get("InstanceConcurrencyConfig") is not None:
            self._InstanceConcurrencyConfig = InstanceConcurrencyConfig()
            self._InstanceConcurrencyConfig._deserialize(params.get("InstanceConcurrencyConfig"))
        self._DnsCache = params.get("DnsCache")
        if params.get("IntranetConfig") is not None:
            self._IntranetConfig = IntranetConfigIn()
            self._IntranetConfig._deserialize(params.get("IntranetConfig"))
        self._IgnoreSysLog = params.get("IgnoreSysLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration返回参数结构体

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


class UpdateFunctionEventInvokeConfigRequest(AbstractModel):
    """UpdateFunctionEventInvokeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncTriggerConfig: 异步重试配置信息
        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self._AsyncTriggerConfig = None
        self._FunctionName = None
        self._Namespace = None

    @property
    def AsyncTriggerConfig(self):
        return self._AsyncTriggerConfig

    @AsyncTriggerConfig.setter
    def AsyncTriggerConfig(self, AsyncTriggerConfig):
        self._AsyncTriggerConfig = AsyncTriggerConfig

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self._AsyncTriggerConfig = AsyncTriggerConfig()
            self._AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionEventInvokeConfigResponse(AbstractModel):
    """UpdateFunctionEventInvokeConfig返回参数结构体

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


class UpdateNamespaceRequest(AbstractModel):
    """UpdateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _Description: 命名空间描述
        :type Description: str
        """
        self._Namespace = None
        self._Description = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNamespaceResponse(AbstractModel):
    """UpdateNamespace返回参数结构体

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


class UpdateTriggerRequest(AbstractModel):
    """UpdateTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        :param _Type: 触发器类型
        :type Type: str
        :param _Enable: 触发器开启或关闭，传参为OPEN为开启，CLOSE为关闭
        :type Enable: str
        :param _Qualifier: 函数的版本，默认为 $LATEST，建议填写 [$DEFAULT](https://cloud.tencent.com/document/product/583/36149#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)方便后续进行版本的灰度发布。
        :type Qualifier: str
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        :param _TriggerDesc: TriggerDesc参数
        :type TriggerDesc: str
        :param _Description: 触发器描述
        :type Description: str
        :param _CustomArgument: 用户附加信息
        :type CustomArgument: str
        """
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._Enable = None
        self._Qualifier = None
        self._Namespace = None
        self._TriggerDesc = None
        self._Description = None
        self._CustomArgument = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._Enable = params.get("Enable")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        self._TriggerDesc = params.get("TriggerDesc")
        self._Description = params.get("Description")
        self._CustomArgument = params.get("CustomArgument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTriggerResponse(AbstractModel):
    """UpdateTrigger返回参数结构体

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


class UpdateTriggerStatusRequest(AbstractModel):
    """UpdateTriggerStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 触发器的初始是能状态OPEN表示开启 CLOSE表示关闭
        :type Enable: str
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        :param _Type: 触发器类型
        :type Type: str
        :param _Qualifier: 函数的版本，默认为 $LATEST，建议填写 [$DEFAULT](https://cloud.tencent.com/document/product/583/36149#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)方便后续进行版本的灰度发布。
        :type Qualifier: str
        :param _Namespace: 函数的命名空间
        :type Namespace: str
        :param _TriggerDesc: 如果更新的触发器类型为 COS 触发器，该字段为必填值，存放 JSON 格式的数据 {"event":"cos:ObjectCreated:*"}，数据内容和 SetTrigger 接口中该字段的格式相同；如果更新的触发器类型为定时触发器或 CMQ 触发器，可以不指定该字段
        :type TriggerDesc: str
        """
        self._Enable = None
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._Qualifier = None
        self._Namespace = None
        self._TriggerDesc = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        self._TriggerDesc = params.get("TriggerDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTriggerStatusResponse(AbstractModel):
    """UpdateTriggerStatus返回参数结构体

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


class UsageInfo(AbstractModel):
    """已使用的信息

    """

    def __init__(self):
        r"""
        :param _NamespacesCount: 命名空间个数
        :type NamespacesCount: int
        :param _Namespace: 命名空间详情
        :type Namespace: list of NamespaceUsage
        :param _TotalConcurrencyMem: 当前地域用户并发内存配额上限
        :type TotalConcurrencyMem: int
        :param _TotalAllocatedConcurrencyMem: 当前地域用户已配置并发内存额度
        :type TotalAllocatedConcurrencyMem: int
        :param _UserConcurrencyMemLimit: 用户实际配置的账号并发配额
        :type UserConcurrencyMemLimit: int
        """
        self._NamespacesCount = None
        self._Namespace = None
        self._TotalConcurrencyMem = None
        self._TotalAllocatedConcurrencyMem = None
        self._UserConcurrencyMemLimit = None

    @property
    def NamespacesCount(self):
        return self._NamespacesCount

    @NamespacesCount.setter
    def NamespacesCount(self, NamespacesCount):
        self._NamespacesCount = NamespacesCount

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TotalConcurrencyMem(self):
        return self._TotalConcurrencyMem

    @TotalConcurrencyMem.setter
    def TotalConcurrencyMem(self, TotalConcurrencyMem):
        self._TotalConcurrencyMem = TotalConcurrencyMem

    @property
    def TotalAllocatedConcurrencyMem(self):
        return self._TotalAllocatedConcurrencyMem

    @TotalAllocatedConcurrencyMem.setter
    def TotalAllocatedConcurrencyMem(self, TotalAllocatedConcurrencyMem):
        self._TotalAllocatedConcurrencyMem = TotalAllocatedConcurrencyMem

    @property
    def UserConcurrencyMemLimit(self):
        return self._UserConcurrencyMemLimit

    @UserConcurrencyMemLimit.setter
    def UserConcurrencyMemLimit(self, UserConcurrencyMemLimit):
        self._UserConcurrencyMemLimit = UserConcurrencyMemLimit


    def _deserialize(self, params):
        self._NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self._Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceUsage()
                obj._deserialize(item)
                self._Namespace.append(obj)
        self._TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self._TotalAllocatedConcurrencyMem = params.get("TotalAllocatedConcurrencyMem")
        self._UserConcurrencyMemLimit = params.get("UserConcurrencyMemLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Variable(AbstractModel):
    """变量参数

    """

    def __init__(self):
        r"""
        :param _Key: 变量的名称，不可为空字符
        :type Key: str
        :param _Value: 变量的值，不可为空字符
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
        


class VersionMatch(AbstractModel):
    """带有匹配规则的函数版本

    """

    def __init__(self):
        r"""
        :param _Version: 函数版本名称
        :type Version: str
        :param _Key: 匹配规则的key，调用时通过传key来匹配规则路由到指定版本
header方式：
key填写"invoke.headers.User"，并在 invoke 调用函数时传参 RoutingKey：{"User":"value"}规则匹配调用
        :type Key: str
        :param _Method: 匹配方式。取值范围：
range：范围匹配
exact：字符串精确匹配
        :type Method: str
        :param _Expression: range 匹配规则要求：
需要为开区间或闭区间描述 (a,b) [a,b]，其中 a、b 均为整数
exact 匹配规则要求：
字符串精确匹配
        :type Expression: str
        """
        self._Version = None
        self._Key = None
        self._Method = None
        self._Expression = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Expression(self):
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Key = params.get("Key")
        self._Method = params.get("Method")
        self._Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionProvisionedConcurrencyInfo(AbstractModel):
    """函数版本的预置并发信息，包括设置预置并发数、已完成预置的并发数和预置任务状态。

    """

    def __init__(self):
        r"""
        :param _AllocatedProvisionedConcurrencyNum: 设置的预置并发数。
        :type AllocatedProvisionedConcurrencyNum: int
        :param _AvailableProvisionedConcurrencyNum: 当前已完成预置的并发数。
        :type AvailableProvisionedConcurrencyNum: int
        :param _Status: 预置任务状态，Done表示已完成，InProgress表示进行中，Failed表示部分或全部失败。
        :type Status: str
        :param _StatusReason: 对预置任务状态Status的说明。
        :type StatusReason: str
        :param _Qualifier: 函数版本号
        :type Qualifier: str
        :param _TriggerActions: 预置并发定时任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerActions: list of TriggerAction
        """
        self._AllocatedProvisionedConcurrencyNum = None
        self._AvailableProvisionedConcurrencyNum = None
        self._Status = None
        self._StatusReason = None
        self._Qualifier = None
        self._TriggerActions = None

    @property
    def AllocatedProvisionedConcurrencyNum(self):
        return self._AllocatedProvisionedConcurrencyNum

    @AllocatedProvisionedConcurrencyNum.setter
    def AllocatedProvisionedConcurrencyNum(self, AllocatedProvisionedConcurrencyNum):
        self._AllocatedProvisionedConcurrencyNum = AllocatedProvisionedConcurrencyNum

    @property
    def AvailableProvisionedConcurrencyNum(self):
        return self._AvailableProvisionedConcurrencyNum

    @AvailableProvisionedConcurrencyNum.setter
    def AvailableProvisionedConcurrencyNum(self, AvailableProvisionedConcurrencyNum):
        self._AvailableProvisionedConcurrencyNum = AvailableProvisionedConcurrencyNum

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def TriggerActions(self):
        return self._TriggerActions

    @TriggerActions.setter
    def TriggerActions(self, TriggerActions):
        self._TriggerActions = TriggerActions


    def _deserialize(self, params):
        self._AllocatedProvisionedConcurrencyNum = params.get("AllocatedProvisionedConcurrencyNum")
        self._AvailableProvisionedConcurrencyNum = params.get("AvailableProvisionedConcurrencyNum")
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._Qualifier = params.get("Qualifier")
        if params.get("TriggerActions") is not None:
            self._TriggerActions = []
            for item in params.get("TriggerActions"):
                obj = TriggerAction()
                obj._deserialize(item)
                self._TriggerActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionWeight(AbstractModel):
    """带有权重的函数版本

    """

    def __init__(self):
        r"""
        :param _Version: 函数版本名称
        :type Version: str
        :param _Weight: 该版本的权重
        :type Weight: float
        """
        self._Version = None
        self._Weight = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """私有网络参数配置

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络 的 Id
        :type VpcId: str
        :param _SubnetId: 子网的 Id
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WSParams(AbstractModel):
    """HTTP函数通过WebSockets协议访问时的参数

    """

    def __init__(self):
        r"""
        :param _IdleTimeOut: 空闲超时时间, 单位秒，默认15s。可配置范围1~1800s。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleTimeOut: int
        """
        self._IdleTimeOut = None

    @property
    def IdleTimeOut(self):
        return self._IdleTimeOut

    @IdleTimeOut.setter
    def IdleTimeOut(self, IdleTimeOut):
        self._IdleTimeOut = IdleTimeOut


    def _deserialize(self, params):
        self._IdleTimeOut = params.get("IdleTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        